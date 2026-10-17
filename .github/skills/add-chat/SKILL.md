---
name: add-chat
description: 'Add an "Ask my page" chat bubble to a learner''s workshop website. It answers questions about what the page shows, using the workshop AI through the Website preview. Use /add-chat once a page exists.'
argument-hint: 'Optional idea page, such as team-lunch'
user-invocable: true
disable-model-invocation: true
---

# Add a Chat Bubble

Give the learner's page a small "Ask my page" assistant. It reads what is visible on the page and
answers in plain words. The page holds no key or secret: the Website preview signs in as the
workshop identity and asks the workshop's chat model. Never add a server, package, API key, or
network call to the page, and do not edit the preview helper.

1. Find the page. Default to `site/index.html`; an idea name such as `team-lunch` means
   `site/ideas/team-lunch/index.html`. If it does not exist, say **"Let's create your website
   first with /create-website."** and stop.
2. If the page already contains `Workshop.addChat`, say the chat is already there and stop.
3. Copy [workshop-chat.js](../create-website/assets/js/workshop-chat.js) unchanged to
   `site/js/workshop-chat.js`, unless that file already exists.
4. Right after the page's `js/workshop.js` script tag, add
   `<script src="js/workshop-chat.js"></script>`. From a page in `site/ideas/<name>/` the path is
   `../../js/workshop-chat.js`.
5. At the very end of the page's own inline script, add one line that names the bubble after the
   page, for example `Workshop.addChat({ title: 'Ask my planner' })`. Change nothing else. Add one
   line to the brief under `## Changes so far`: "Added an Ask my page chat".
6. Run `python3 scripts/website_preview.py start` yourself (for an idea page add its path relative
   to `site/`, such as `ideas/team-lunch/index.html`) and require `previewOpen: true`.
7. Hand over in three short lines:
   - **"Select Ask at the bottom right and ask: What is on this page?"**
   - **"Check the answer against the page yourself. The assistant can be wrong."**
   - **"It answers while you build here; a published copy says it is switched off."**

If the bubble replies that the assistant is not switched on, this Codespace lacks the workshop
secrets or needs a restart: show the exact message to a helper. Do not install anything, add keys,
or change settings. Everything on the page stays fictional.

Official references: [VS Code webviews](https://code.visualstudio.com/api/extension-guides/webview)
and [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills).
