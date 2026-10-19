/* Optional "Ask my page" chat bubble: Workshop.addChat() adds a small assistant to any page.
 * In the workshop's Website preview it asks the workshop's AI model about what the page shows;
 * the preview signs in, so the page holds no key or secret. Anywhere else, for example a
 * published copy, it says that it only answers while you build. Text is always set with
 * textContent, never as HTML, and this file makes no network requests of its own. */
(function () {
    'use strict'

    let preview = null
    try {
        preview = typeof acquireVsCodeApi === 'function' ? acquireVsCodeApi() : null
    } catch {
        preview = null
    }
    const waiting = new Map()

    window.addEventListener('message', event => {
        const reply = event.data
        if (!reply || reply.type !== 'workshop.answer' || !waiting.has(reply.id)) return
        const done = waiting.get(reply.id)
        waiting.delete(reply.id)
        done(reply)
    })

    /** Ask the Website preview; resolve with { ok, answer } or { ok: false, error }. */
    function askPreview(question, page, title) {
        return new Promise(resolve => {
            const id = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
            const timer = setTimeout(() => {
                waiting.delete(id)
                resolve({ ok: false, error: 'No answer this time. Please try again.' })
            }, 45000)
            waiting.set(id, reply => { clearTimeout(timer); resolve(reply) })
            preview.postMessage({ type: 'workshop.ask', id, question, page, title })
        })
    }

    const STYLE = `
.chat { position: fixed; right: 1.2rem; bottom: 1.2rem; z-index: 20; display: flex; flex-direction: column; align-items: flex-end; gap: 0.6rem; }
.chat-toggle { display: inline-flex; align-items: center; gap: 0.5rem; border: 0; border-radius: 99px; padding: 0.75rem 1.15rem; background: var(--accent-strong); color: #fff; font: inherit; font-weight: 700; box-shadow: var(--shadow-lift); cursor: pointer; }
.chat-icon { position: relative; width: 1.15rem; height: 0.85rem; border-radius: 0.35rem; background: currentColor; }
.chat-icon::after { content: ""; position: absolute; left: 0.2rem; bottom: -0.32rem; border: 0.2rem solid transparent; border-top-color: currentColor; border-left-color: currentColor; }
.chat-panel { display: flex; flex-direction: column; width: min(22rem, calc(100vw - 2.4rem)); max-height: min(30rem, 70vh); overflow: hidden; background: var(--paper); color: var(--ink); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow-lift); }
.chat-panel[hidden] { display: none; }
.chat-head { display: flex; align-items: center; justify-content: space-between; gap: 0.5rem; padding: 0.7rem 0.9rem; background: var(--accent-soft); }
.chat-close { border: 0; background: transparent; color: inherit; font-size: 1.4rem; line-height: 1; cursor: pointer; }
.chat-log { flex: 1; display: flex; flex-direction: column; gap: 0.5rem; overflow-y: auto; padding: 0.8rem; }
.chat-bubble { max-width: 85%; margin: 0; padding: 0.55rem 0.8rem; border-radius: 1rem; line-height: 1.4; white-space: pre-wrap; }
.chat-bot { align-self: flex-start; background: var(--canvas); }
.chat-me { align-self: flex-end; background: var(--accent-strong); color: #fff; }
.chat-thinking { color: var(--muted); font-style: italic; }
.chat-form { display: flex; gap: 0.4rem; padding: 0.6rem; border-top: 1px solid var(--line); }
.chat-input { flex: 1; min-width: 0; padding: 0.55rem 0.85rem; border: 1px solid var(--line); border-radius: 99px; font: inherit; }
.chat-send { border: 0; border-radius: 99px; padding: 0.55rem 1rem; background: var(--accent-strong); color: #fff; font: inherit; font-weight: 700; cursor: pointer; }
.chat-send:disabled { opacity: 0.6; cursor: wait; }
.chat :focus-visible { outline: 3px solid var(--focus); outline-offset: 2px; }
`

    function make(tag, className, text) {
        const node = document.createElement(tag)
        if (className) node.className = className
        if (text) node.textContent = text
        return node
    }

    /** What the assistant reads: the visible text except the chat itself, then the ticked state of
     *  checkboxes and the descriptions of pictures, which the visible text leaves out. */
    function pageText(widget) {
        widget.style.display = 'none'
        const text = document.body.innerText
        widget.style.display = ''
        const extras = []
        for (const box of document.querySelectorAll('input[type=checkbox]')) {
            const label = box.labels && box.labels[0] ? box.labels[0].innerText : ''
            const name = (box.getAttribute('aria-label') || label).trim()
            if (name) extras.push(`${box.checked ? 'Ticked' : 'Not ticked'}: ${name}`)
        }
        for (const picture of document.querySelectorAll('img[alt]')) {
            if (picture.alt.trim()) extras.push(`Picture: ${picture.alt.trim()}`)
        }
        return extras.length ? `${text}\n\nAlso on the page:\n${extras.join('\n')}` : text
    }

    /** Add the chat bubble once; options: title, greeting, placeholder. */
    function addChat(options = {}) {
        if (document.getElementById('workshop-chat')) return
        const title = options.title || 'Ask my page'
        const style = make('style')
        style.textContent = STYLE
        document.head.append(style)

        const root = make('div', 'chat')
        root.id = 'workshop-chat'
        const toggle = make('button', 'chat-toggle')
        toggle.type = 'button'
        toggle.setAttribute('aria-expanded', 'false')
        toggle.setAttribute('aria-controls', 'workshop-chat-panel')
        toggle.append(make('span', 'chat-icon'), make('span', '', options.button || 'Ask'))
        const panel = make('section', 'chat-panel')
        panel.id = 'workshop-chat-panel'
        panel.hidden = true
        panel.setAttribute('aria-label', title)
        const head = make('div', 'chat-head')
        const close = make('button', 'chat-close', '\u00d7')
        close.type = 'button'
        close.setAttribute('aria-label', 'Close the chat')
        head.append(make('strong', '', title), close)
        const log = make('div', 'chat-log')
        log.setAttribute('role', 'log')
        log.setAttribute('aria-live', 'polite')
        const form = make('form', 'chat-form')
        const input = make('input', 'chat-input')
        input.type = 'text'
        input.maxLength = 500
        input.placeholder = options.placeholder || 'Ask a question'
        input.setAttribute('aria-label', 'Your question')
        const send = make('button', 'chat-send', 'Send')
        send.type = 'submit'
        form.append(input, send)
        panel.append(head, log, form)
        root.append(panel, toggle)
        document.body.append(root)

        const say = (who, text) => {
            const bubble = make('p', `chat-bubble chat-${who}`, text)
            log.append(bubble)
            log.scrollTop = log.scrollHeight
            return bubble
        }
        const open = show => {
            panel.hidden = !show
            toggle.setAttribute('aria-expanded', String(show))
            if (show) input.focus()
            else toggle.focus()
        }
        say('bot', options.greeting || 'Hi! Ask me anything about this page.')
        toggle.addEventListener('click', () => open(panel.hidden))
        close.addEventListener('click', () => open(false))
        panel.addEventListener('keydown', event => { if (event.key === 'Escape') open(false) })
        form.addEventListener('submit', async event => {
            event.preventDefault()
            const question = input.value.trim()
            if (!question || send.disabled) return
            input.value = ''
            say('me', question)
            if (!preview) {
                say('bot', 'I answer questions while you build in the workshop preview. On this copy of the page I am switched off.')
                return
            }
            send.disabled = true
            const thinking = say('bot chat-thinking', 'Thinking...')
            const reply = await askPreview(question, pageText(root), document.title)
            thinking.remove()
            send.disabled = false
            say('bot', reply.ok ? reply.answer : reply.error)
            input.focus()
        })
    }

    window.Workshop = Object.assign(window.Workshop || {}, { addChat })
})()
