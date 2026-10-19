/* Photo Studio helper: Workshop.photo asks the Website preview to repaint a photo with the
 * workshop's picture model, and to save a finished picture into this page's gallery. The page
 * holds no key or secret: the preview signs in as the workshop identity. Only photos of things,
 * places and animals are repainted; the preview checks every photo first and politely refuses
 * anything else. Outside the preview, for example on a published copy, making pictures is off.
 * This file makes no network requests of its own. */
(function () {
    'use strict'

    const preview = window.Workshop && window.Workshop.preview ? window.Workshop.preview() : null
    const waiting = new Map()
    const OFF = 'Making pictures works while you build in the workshop preview. This copy shows the gallery only.'

    window.addEventListener('message', event => {
        const reply = event.data
        if (!reply || !['workshop.photo.result', 'workshop.photo.saved'].includes(reply.type) || !waiting.has(reply.id)) return
        const done = waiting.get(reply.id)
        waiting.delete(reply.id)
        done(reply)
    })

    function ask(message, timeout) {
        if (!preview) return Promise.resolve({ ok: false, error: OFF })
        return new Promise(resolve => {
            const id = `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
            const timer = setTimeout(() => {
                waiting.delete(id)
                resolve({ ok: false, error: 'No answer this time. Please try again.' })
            }, timeout)
            waiting.set(id, reply => { clearTimeout(timer); resolve(reply) })
            preview.postMessage({ ...message, id })
        })
    }

    /** Read an image file or blob as a JPEG data URL, at most maxSide pixels on its longest side. */
    function shrink(file, maxSide = 1024) {
        return new Promise((resolve, reject) => {
            if (!file || !/^image\/(jpeg|png|webp)$/.test(file.type)) {
                reject(new Error('Choose a JPEG, PNG or WebP photo.'))
                return
            }
            const reader = new FileReader()
            reader.onerror = () => reject(new Error('That file could not be read.'))
            reader.onload = () => {
                const image = new Image()
                image.onerror = () => reject(new Error('That file is not a photo this page can open.'))
                image.onload = () => {
                    const scale = Math.min(1, maxSide / Math.max(image.naturalWidth, image.naturalHeight))
                    const canvas = document.createElement('canvas')
                    canvas.width = Math.max(1, Math.round(image.naturalWidth * scale))
                    canvas.height = Math.max(1, Math.round(image.naturalHeight * scale))
                    canvas.getContext('2d').drawImage(image, 0, 0, canvas.width, canvas.height)
                    resolve(canvas.toDataURL('image/jpeg', 0.88))
                }
                image.src = reader.result
            }
            reader.readAsDataURL(file)
        })
    }

    /** Load a picture from this website (such as gallery/sleepy-cat.jpg) as a data URL to send. */
    async function fromUrl(url, maxSide = 1024) {
        const response = await fetch(url)
        if (!response.ok) throw new Error('That picture could not be loaded.')
        return shrink(await response.blob(), maxSide)
    }

    window.Workshop = Object.assign(window.Workshop || {}, {
        photo: {
            /** True inside the workshop's Website preview, where pictures can be made and saved. */
            available: () => Boolean(preview),
            shrink,
            fromUrl,
            /** Repaint a photo: resolves { ok, image, model } or { ok: false, refused?, error }. */
            edit: (image, prompt) => ask({ type: 'workshop.photo.edit', image, prompt }, 200000),
            /** Save a picture made here: resolves { ok, file } or { ok: false, error }. */
            save: (image, title) => ask({ type: 'workshop.photo.save', image, title }, 30000),
        },
    })
})()
