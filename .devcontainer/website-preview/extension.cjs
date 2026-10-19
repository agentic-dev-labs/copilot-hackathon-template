const fs = require('node:fs')
const net = require('node:net')
const path = require('node:path')
const { PreviewController, resolveEntry } = require('./controller.cjs')
const { createAssistant, createChatHandler } = require('./assistant.cjs')
const { createPhotoHandler } = require('./photo.cjs')

const VIEW_TYPE = 'workshopSite'
const ENTRY_KEY = 'workshopSite.entry'
// The owner approved Open-Meteo for the Weather starter (forecast, city search and past weather);
// everything else stays offline.
const ALLOWED_APIS = ['https://api.open-meteo.com', 'https://geocoding-api.open-meteo.com', 'https://archive-api.open-meteo.com']
const controllers = new Map()
const sockets = []
let chatHandler
let photoHandler
// The "Ask my page" bubble posts questions here; answers come from the workshop's chat model.
const answerQuestion = message => {
  chatHandler = chatHandler || createChatHandler(createAssistant())
  return chatHandler(message)
}
// Photo Studio pages post photos here; photo.cjs checks and changes them, and saves pictures to the page's gallery.
const handlePhoto = (message, folders) => {
  photoHandler = photoHandler || createPhotoHandler()
  return photoHandler(message, folders)
}

function escapeHtml(text) {
  return String(text).replace(/[&<>"']/g, character => `&#${character.charCodeAt(0)};`)
}

function renderHtml(vscode, webview, target) {
  const open = vscode.workspace.textDocuments.find(document => document.uri.fsPath === target.file)
  const source = open ? open.getText() : fs.readFileSync(target.file, 'utf8')
  const base = `${webview.asWebviewUri(vscode.Uri.file(target.directory))}/`
  const resources = webview.cspSource
  const policy = `default-src 'none'; img-src ${resources} data:; font-src ${resources}; style-src ${resources} 'unsafe-inline'; script-src ${resources} 'unsafe-inline'; connect-src ${resources} ${ALLOWED_APIS.join(' ')}; form-action 'none'`
  const head = `<meta http-equiv="Content-Security-Policy" content="${policy}"><base href="${base}">`
  return /<head[^>]*>/i.test(source) ? source.replace(/<head[^>]*>/i, match => match + head) : head + source
}

function createPreview(vscode, context, workspace, target, restoredPanel) {
  const site = vscode.Uri.file(path.join(workspace, 'site'))
  const options = { enableScripts: true, localResourceRoots: [site] }
  const panel = restoredPanel || vscode.window.createWebviewPanel(
    VIEW_TYPE, 'Website preview',
    { viewColumn: vscode.ViewColumn.Beside, preserveFocus: true },
    { ...options, retainContextWhenHidden: true },
  )
  panel.webview.options = options
  let current = target
  let disposed = false
  let timer
  let draws = 0
  const draw = () => {
    if (disposed) return
    try {
      // A webview reloads only when its HTML text changes. Numbering each draw makes a new
      // script, picture, style or data file show too, not just edits to the page itself.
      panel.webview.html = `${renderHtml(vscode, panel.webview, current)}\n<!-- preview draw ${++draws} -->`
    } catch (error) {
      panel.webview.html = `<p style="font-family:sans-serif">Preview needs attention: ${escapeHtml(error.message)}</p>`
    }
  }
  const refresh = () => { clearTimeout(timer); timer = setTimeout(draw, 150) }
  const insideSite = uri => uri.fsPath.startsWith(site.fsPath + path.sep)
  const watcher = vscode.workspace.createFileSystemWatcher(new vscode.RelativePattern(site, '**/*'))
  const subscriptions = [
    watcher, watcher.onDidChange(refresh), watcher.onDidCreate(refresh), watcher.onDidDelete(refresh),
    vscode.workspace.onDidChangeTextDocument(event => { if (event.document.uri.fsPath === current.file) refresh() }),
    vscode.workspace.onDidSaveTextDocument(document => { if (insideSite(document.uri)) refresh() }),
    panel.webview.onDidReceiveMessage(async message => {
      const photo = typeof message?.type === 'string' && message.type.startsWith('workshop.photo.')
      const reply = photo
        ? await handlePhoto(message, { pageDirectory: current.directory, siteDirectory: path.join(workspace, 'site') })
        : await answerQuestion(message)
      if (reply && !disposed) panel.webview.postMessage(reply)
    }),
  ]
  panel.onDidDispose(() => {
    disposed = true
    clearTimeout(timer)
    for (const subscription of subscriptions) subscription.dispose()
  })
  context.workspaceState.update(ENTRY_KEY, target.entry)
  draw()
  return {
    isOpen: () => !disposed,
    entry: () => current.entry,
    async show(next) {
      current = next
      context.workspaceState.update(ENTRY_KEY, next.entry)
      panel.reveal(vscode.ViewColumn.Beside, true)
      draw()
    },
    close: () => panel.dispose(),
  }
}

function dispatch(controller, request) {
  if (!request || !['start', 'stop', 'status'].includes(request.action)) throw new Error('Use start, stop or status only.')
  if (Object.keys(request).some(key => !['action', 'entry'].includes(key))) throw new Error('Unexpected preview request field.')
  if (request.action === 'status') return controller.status()
  return controller.run(request.action, request.entry)
}

async function listen(workspace, controller, output) {
  const directory = path.join(workspace, '.workshop-preview')
  if (fs.existsSync(directory) && fs.lstatSync(directory).isSymbolicLink()) throw new Error('Preview control directory must not be a symlink.')
  fs.mkdirSync(directory, { recursive: true, mode: 0o700 })
  const filename = path.join(directory, 'site.sock')
  if (fs.existsSync(filename)) {
    if (!fs.lstatSync(filename).isSocket()) throw new Error('Preview socket path is occupied by another file.')
    const active = await new Promise((resolve, reject) => {
      const probe = net.createConnection(filename)
      probe.once('connect', () => { probe.destroy(); resolve(true) })
      probe.once('error', error => error.code === 'ECONNREFUSED' ? resolve(false) : reject(error))
    })
    if (active) throw new Error('Another preview helper already owns this workspace socket.')
    fs.unlinkSync(filename)
  }
  const server = net.createServer(connection => {
    connection.setTimeout(30000, () => connection.destroy())
    let buffer = ''
    let received = false
    connection.on('error', () => {})
    connection.on('data', async chunk => {
      if (received) return
      buffer += chunk.toString()
      if (buffer.length > 8192) return connection.destroy()
      if (!buffer.includes('\n')) return
      received = true
      try {
        const result = await dispatch(controller, JSON.parse(buffer.split('\n')[0]))
        connection.end(JSON.stringify({ ok: true, result }) + '\n')
      } catch (error) {
        connection.end(JSON.stringify({ ok: false, error: error.message }) + '\n')
      }
    })
  })
  await new Promise((resolve, reject) => {
    server.once('error', reject)
    server.listen(filename, resolve)
  })
  fs.chmodSync(filename, 0o600)
  server.on('error', error => output.appendLine(error.message))
  sockets.push(server)
}

async function activate(context) {
  const vscode = require('vscode')
  if (!vscode.workspace.isTrusted) return
  const output = vscode.window.createOutputChannel('Workshop Website')
  context.subscriptions.push(output)
  for (const folder of vscode.workspace.workspaceFolders || []) {
    const workspace = folder.uri.fsPath
    if (!fs.existsSync(path.join(workspace, '.github/skills/create-website/SKILL.md'))) continue
    const controller = new PreviewController(workspace, {
      open: target => createPreview(vscode, context, workspace, target),
    })
    controllers.set(workspace, controller)
    try { await listen(workspace, controller, output) } catch (error) { output.appendLine(error.message) }
  }
  const only = () => {
    if (controllers.size === 1) return [...controllers.entries()][0]
    throw new Error('Open exactly one workshop workspace to use the website preview.')
  }
  context.subscriptions.push(vscode.window.registerWebviewPanelSerializer(VIEW_TYPE, {
    async deserializeWebviewPanel(panel) {
      try {
        const [workspace, controller] = only()
        const target = resolveEntry(workspace, context.workspaceState.get(ENTRY_KEY, 'index.html'))
        controller.preview = createPreview(vscode, context, workspace, target, panel)
      } catch { panel.dispose() }
    },
  }))
  context.subscriptions.push(vscode.commands.registerCommand('workshopSite.open', async uri => {
    try {
      const [workspace, controller] = only()
      const file = uri?.fsPath || vscode.window.activeTextEditor?.document.uri.fsPath
      const site = path.join(workspace, 'site') + path.sep
      const entry = file && file.startsWith(site) && file.endsWith('.html') ? path.relative(site, file).split(path.sep).join('/') : undefined
      await controller.run('start', entry)
    } catch (error) { vscode.window.showErrorMessage(error.message) }
  }))
  context.subscriptions.push(vscode.commands.registerCommand('workshopSite.close', async () => {
    try { await only()[1].run('stop') } catch (error) { vscode.window.showErrorMessage(error.message) }
  }))
}

async function deactivate() {
  for (const server of sockets) server.close()
  controllers.clear()
}

module.exports = { activate, deactivate, dispatch, renderHtml, createPreview }
