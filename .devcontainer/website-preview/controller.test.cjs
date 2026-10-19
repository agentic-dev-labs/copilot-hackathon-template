const assert = require('node:assert/strict')
const fs = require('node:fs')
const os = require('node:os')
const path = require('node:path')
const { test } = require('node:test')
const { PreviewController, resolveEntry } = require('./controller.cjs')
const { dispatch, renderHtml, createPreview } = require('./extension.cjs')

function fixture(context) {
  const workspace = fs.mkdtempSync(path.join(os.tmpdir(), 'workshop-preview-'))
  fs.mkdirSync(path.join(workspace, 'site'))
  fs.writeFileSync(path.join(workspace, 'site/index.html'), '<html><head><title>T</title></head><body>Synthetic test</body></html>')
  context.after(() => fs.rmSync(workspace, { recursive: true, force: true }))
  const calls = []
  const operations = {
    async open(target) {
      calls.push(`open:${target.entry}`)
      let open = true
      let entry = target.entry
      return {
        isOpen: () => open,
        entry: () => entry,
        async show(next) { calls.push(`show:${next.entry}`); entry = next.entry },
        close() { calls.push('close'); open = false },
      }
    },
  }
  return { workspace, calls, operations, controller: new PreviewController(workspace, operations) }
}

test('entry paths stay inside the website and reject URLs, traversal and symlinks', context => {
  const { workspace } = fixture(context)
  assert.equal(resolveEntry(workspace).entry, 'index.html')
  for (const entry of ['../index.html', '/tmp/index.html', 'https://example.com/', '.secret.html', 'foo\\index.html', '%2e%2e/index.html', 'index.html?x=1', 'App.vue']) {
    assert.throws(() => resolveEntry(workspace, entry))
  }
  fs.symlinkSync(path.join(workspace, 'site/index.html'), path.join(workspace, 'site/linked.html'))
  assert.throws(() => resolveEntry(workspace, 'linked.html'), /symlinks/)
})

test('a missing page fails before any panel opens', async context => {
  const { controller, calls } = fixture(context)
  await assert.rejects(controller.run('start', 'missing.html'), /create-website/)
  assert.deepEqual(calls, [])
})

test('repeated start reuses the panel, stop closes it and files stay unchanged', async context => {
  const { controller, calls, workspace } = fixture(context)
  await controller.run('start')
  const again = await controller.run('start')
  assert.equal(again.reused, true)
  assert.equal(again.server, 'none')
  assert.equal(again.renderingVerified, false)
  const stopped = await controller.run('stop')
  assert.equal(stopped.previewOpen, false)
  await controller.run('stop')
  assert.deepEqual(calls, ['open:index.html', 'show:index.html', 'close'])
  assert.ok(fs.existsSync(path.join(workspace, 'site/index.html')))
})

test('the control channel accepts only bounded preview actions', async context => {
  const { controller, calls } = fixture(context)
  assert.throws(() => dispatch(controller, { action: 'shell' }), /start, stop or status/)
  assert.throws(() => dispatch(controller, { action: 'start', command: 'x' }), /Unexpected/)
  assert.equal(dispatch(controller, { action: 'status' }).previewOpen, false)
  assert.deepEqual(calls, [])
})

test('rendering adds a no-network policy and a base for local assets', context => {
  const { workspace } = fixture(context)
  const target = resolveEntry(workspace)
  const vscode = {
    workspace: { textDocuments: [] },
    Uri: { file: value => value },
  }
  const webview = { cspSource: 'vscode-webview:', asWebviewUri: value => `webview:${value}` }
  const html = renderHtml(vscode, webview, target)
  assert.match(html, /<head><meta http-equiv="Content-Security-Policy"/)
  assert.ok(html.includes(`<base href="webview:${path.join(fs.realpathSync(workspace), 'site')}/">`))
  assert.ok(html.includes("default-src 'none'"))
  const policy = html.match(/content="([^"]+)"/)[1]
  const connect = policy.split(';').find(part => part.trim().startsWith('connect-src')).trim().split(/\s+/).slice(1)
  assert.deepEqual(connect, ['vscode-webview:', 'https://api.open-meteo.com', 'https://geocoding-api.open-meteo.com'])
  assert.deepEqual(policy.match(/https:\/\/[^\s;]+/g), ['https://api.open-meteo.com', 'https://geocoding-api.open-meteo.com'])
  const unsaved = { uri: { fsPath: target.file }, getText: () => '<html><head></head><body>Unsaved edit</body></html>' }
  vscode.workspace.textDocuments.push(unsaved)
  assert.ok(renderHtml(vscode, webview, target).includes('Unsaved edit'))
})

test('a new script, picture or data file redraws the page even when the page text is unchanged', async context => {
  const { workspace } = fixture(context)
  const target = resolveEntry(workspace)
  const drawn = []
  const listeners = {}
  const listen = name => handler => { listeners[name] = handler; return { dispose() {} } }
  const panel = {
    webview: {
      cspSource: 'vscode-webview:',
      asWebviewUri: value => `webview:${value}`,
      set html(value) { drawn.push(value) },
      onDidReceiveMessage: () => ({ dispose() {} }),
    },
    onDidDispose: () => ({ dispose() {} }),
  }
  const vscode = {
    workspace: {
      textDocuments: [],
      createFileSystemWatcher: () => ({ onDidChange: listen('change'), onDidCreate: listen('create'), onDidDelete: listen('delete'), dispose() {} }),
      onDidChangeTextDocument: listen('text'),
      onDidSaveTextDocument: listen('save'),
    },
    window: { createWebviewPanel: () => panel },
    Uri: { file: value => value },
    RelativePattern: class {},
    ViewColumn: { Beside: -2 },
  }
  createPreview(vscode, { workspaceState: { update() {} } }, workspace, target)
  listeners.create({ fsPath: path.join(workspace, 'site/js/workshop-chat.js') })
  await new Promise(resolve => setTimeout(resolve, 250))
  assert.equal(drawn.length, 2)
  assert.notEqual(drawn[0], drawn[1], 'a webview reloads only when its HTML text changes')
  assert.equal(drawn[0].replace(/<!-- preview draw \d+ -->/, ''), drawn[1].replace(/<!-- preview draw \d+ -->/, ''))
})
