# Temporary Facilitator Notes

This dot-folder keeps preparation material separate from the attendee labs. It is
not private: anyone who can read this repository can read these files and their
Git history. The repository owner explicitly approved that disclosure on 2026-09-09.
No passwords, tokens, or service credentials belong here.

## Documents

- [RUN-OF-SHOW.md](RUN-OF-SHOW.md): presenter script, demos, timing, and fallbacks.
- [ENGAGEMENT-BRIEF.md](ENGAGEMENT-BRIEF.md): stakeholder context and internal planning history.

Existing confidentiality labels remain applicable; do not redistribute the material
outside the approved repository audience. Docker builds exclude this entire folder.
Unless stated otherwise, commands and repository paths in these documents are relative
to the repository root, not to this folder.

## Pre-workshop Reminder

**Target: 2026-10-12**, two weeks before the workshop starts on 2026-10-26.
This is a written reminder, not an automatically scheduled task.

1. Add `/.facilitator/` to the repository-root `.gitignore`.
2. Run `git rm -r --cached -- .facilitator` from the repository root. This stops
   tracking the folder while keeping its files on that machine.
3. Commit and push both the ignore-rule change and the staged removals.
4. Confirm `git ls-files -- .facilitator` is empty and
   `git check-ignore .facilitator/README.md` reports the ignore rule applies.
5. Check any existing team repositories separately. Updating this template does
   not update copies that were already created from it.

**Important:** `.gitignore` alone does not stop tracking files. Untracking or deleting
them does not erase earlier commits, downloaded copies, forks, or existing team
repositories. If the material must become confidential again, it requires a separate
access/history-removal plan; the steps above only remove it from the current checkout.

After untracking, fresh Codespaces will not receive these documents. Keep an approved
backup before relying on their removal from the workshop repository.