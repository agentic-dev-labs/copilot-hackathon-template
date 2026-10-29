---
name: Show my version
about: Day 4's ticket for everyone - your first page shows where it runs and which version it is
title: "Show the environment and version on my website"
labels: ["enhancement"]
assignees: []
---

## What I want

Anyone who opens my website can see at the bottom of the first page where it runs and which
version it is, so that we can all tell which release we are looking at.

## Which page

site/index.html

## User story

As someone who uses my website, I want to see its environment and version at the bottom of the
first page, so that I can tell which release I am looking at.

## Acceptance criteria

- [ ] Given my website in the Website preview, where there is no version.json, when I open the
      first page, then its footer says "Preview".
- [ ] Given my published website after a release, when I open the first page, then its footer
      shows the environment and version from version.json, such as "Production · Version 1.0.0.12".
- [ ] Given a phone-sized screen, when I open the first page, then the footer fits without
      sideways scrolling, and everything else on the page works as before.

## Only change

site/index.html: one small footer at the bottom of the page, with the few lines of style and
script it needs, and one test in checks/test_version.py. The footer's own text is "Preview". A
small script in the page reads version.json with fetch and, when it loads, shows its environment
and version instead, with textContent, never innerHTML; without an environment in the file it
shows Production. When version.json is missing, the footer keeps saying "Preview" and nothing
else changes. The pull request's description starts with "Closes #" and this ticket's number.

Use fictional content only. Do not add packages, frameworks, logins, external services, or real
work data. Follow the repository's instructions files.
