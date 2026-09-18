# Temporary Facilitator Notes

This dot-folder keeps preparation material separate from the attendee labs. It is
not private: anyone who can read this repository can read these files and their
Git history. The repository owner explicitly approved that disclosure on 2026-09-09.
No passwords, tokens, or service credentials belong here.

## Documents

- [RUN-OF-SHOW.md](RUN-OF-SHOW.md): historical presenter script, superseded by the 18 September meeting refit.
- [ENGAGEMENT-BRIEF.md](ENGAGEMENT-BRIEF.md): stakeholder context and internal planning history.
- [Coverage and official references](../docs/REFERENCES.md): attendee-safe lookup guide for every feature family and daily optional tasks.

The current [facilitator guide](../docs/FACILITATOR.md) and [agenda](../docs/AGENDA.md) start with
concepts, Chat, a shared first website, manual checks, and saved work. Tuesday is supported own-idea
building after conceptual overviews. Tools and engineering depth belong to Days 3-5; Dataverse
setup knowledge is preserved in the attendee-safe [post-workshop reference](../post-workshop/dataverse/README.md).
That folder is not a copy of these private preparation notes. All attendee work stays in Codespaces.
The historical run sheet and brief retain prior planning and quotations, not current procedures.
Keep prepared fallbacks labelled and the published day boundaries unchanged.

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

## Official References

- [Ignoring files](https://docs.github.com/en/get-started/git-basics/ignoring-files): why ignore rules do not untrack files already in Git.
- [Copilot features](https://docs.github.com/en/copilot/get-started/features) and [VS Code releases](https://code.visualstudio.com/updates): recheck product coverage before delivery.
