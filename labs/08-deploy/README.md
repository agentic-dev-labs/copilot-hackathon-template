# Lab 08: Publish Your Website

**Objective:** Publish your own reviewed website through the prepared GitHub Actions workflow
and verify its URL, without installing anything on the laptop or signing into Azure.

**Time-box:** 45 minutes

**Prerequisites:** Labs 00-02, a working `site/index.html`, and the facilitator's prepared Actions
deployment access. All CLI commands run in the Codespaces Bash terminal.

> This lab runs on **Day 1**, after Lab 02. Lab numbers group topics; they are not the order
> of the week. See [the agenda](../../docs/AGENDA.md).

The facilitator prepares deployment access. You change the app's label and trigger a workflow;
you do not copy credentials into code or need an Azure portal login.

## Show and Try

The presenter demonstrates review, commit, push, and **Run workflow**, then you repeat. Start
the deployment in the first part of the block so build time overlaps the final checks/discussion.
The 45 minutes cover review and dispatch (15), deployment and inspection (20), and verification (10).

This publishes **your `site/`**, not the vendor application. The `website` target has a separate
derived name ending in `-web`; `vendor` keeps the existing business-app name for Days 2-5.
Do not use the vendor target as a workaround for a missing website. The workshop builds with
Copilot; it does not embed a Copilot model or agent runtime in the deployed page.

## Steps

1. Open `config.json`. Use your assigned, unique workshop label, for example:

   ```json
   {
     "displayName": "Synthetic Team Seven"
   }
   ```

2. Check what will be derived from it:

   ```bash
   python app/config.py --target website
   python -m app.site --check
   uv run pytest
   uv run ruff check .
   ```

   The first command prints the website's name. The second checks an entry page, permitted asset
   types, bounded size, and a fingerprint. Keep PDFs, raw extracts, credentials, and unrelated files
   out of `site/`. Markdown notes are not served or copied into the image. Review intended JSON and
   images too; an extension check is not a security scanner. Each asset is limited to 2 MiB, the
   site to 100 files and 20 MiB. The facilitator assigns unique labels across repositories.

3. Open **Source Control**, inspect each changed file, and stage only your intended website,
   configuration, and reviewed skill files. Do not stage `research/` or private material.
   Enter a message and **Commit**, then **Push** (or **Sync Changes** if instructed). Saving,
   committing, and pushing are separate. Use a branch/PR if the repository requires it; merge
   only after the required review. Ask a helper if Git reports a conflict instead of forcing it.
4. In your repository's browser tab, open **Actions > Deploy my app > Run workflow** on `main`.
   Select **target: website** and leave **connect_dataverse** unchecked. Confirm the intended
   repository and branch. Clicking once is enough; inspect the run before retrying a failed request.
5. The workflow runs tests and lint, then **Read config.json**. If your label is still `Your Name`, it stops there
   with a message telling you to edit the file. That is the guard working, not a failure.
6. The **Build the image** step builds your container remotely. Nothing is built on your laptop.
7. When the run finishes, open the **run summary**. Your URL is printed there.
8. Open it. Confirm it is your website, with the content and interactions you just reviewed.
   The workflow checks exact entry-page bytes and the asset fingerprint, not a required title.
9. Open `/healthz` at the same app origin. Confirm `status` is `ok` and `commit` matches
   the workflow's tested commit. A healthy response from an older revision is not this deployment.

10. Add a fictional item on the deployed page, refresh, check persistence, remove it, and refresh
   again. The new URL has separate localStorage from the Codespaces preview. Empty initial data
   is expected. Test it yourself or with Playwright, keeping automation observations distinct.

**Done when:** the workflow succeeds for the intended commit and **website** target, the
verified URL serves your actual page, and the add/refresh/remove journey works at that origin.
A healthy container alone does not prove the buttons, charts, or storage behaviour work.

## What you just learned

The preview is temporary; deployment is a deliberate Actions operation, not something every push
does automatically. A label identifies a training deployment, not a user or authorization boundary.
You can stop the Codespace after saving/pushing; that does not delete the separately deployed app.
Agree retention with the facilitator. Do not delete personal GitHub accounts or shared Azure resources.

## If something goes wrong

| Symptom                               | Cause                                                     | Fix                                                                                                                                          |
| ------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Stops on **Read config.json**         | Name is still `Your Name`, or it has no letters or digits | Edit `config.json` and push again                                                                                                            |
| Deployment rejected on the name       | Derived name is invalid                                   | Names are lowercase, letters, digits and hyphens, 32 characters at most. Run `python app/config.py` to see yours                             |
| The run cannot sign in to Azure       | Organization secrets are missing                          | Tell the facilitator; nothing on your side is wrong                                                                                          |
| Stops on prepared access/commit check | Missing Actions configuration or the branch moved         | Ask the owner to check the named settings; retest the exact branch. Do not sign into Azure as a workaround.                                  |
| Page shows the vendor table           | Wrong deployment target or URL                           | Use the website target and its verified run-summary URL; do not overwrite the business app. |
| Website validation fails              | Missing entry point, invalid asset, or excessive size     | Inspect `python -m app.site --check`; keep only intentional web assets under `site/`. |

**Stretch goal:** Change something visible in `site/index.html`, push, and run the website workflow again.
Watch the same URL update rather than a new app appearing.

## Optional extras

Pick any of these if you finish early. None of them are required.

1. **Get reviewed (5-10 min).** Open a PR for a small change and request Copilot code review if
   enabled. Inspect one finding against code and tests. If effort levels are offered, identify
   their purpose; a second review is optional and consumes additional usage.
2. **Let it write the summary.** Have Copilot generate the pull request description, then check it
   against your actual diff.
3. **Read the run log (5 min).** Identify the triggering user, commit, image tag, and time. Discuss
   retention requirements before treating it as a long-term record.
4. **Test the guard locally (5 min).** Run `python -m pytest tests/test_app_config.py -q` to see
   placeholder validation tested without changing the shared app or triggering a failed deployment.

## Official References

- [Awesome Copilot](https://github.com/github/awesome-copilot/) and [web-design-reviewer](https://github.com/github/awesome-copilot/tree/main/skills/web-design-reviewer): inspect provenance, dependencies, and source before reuse.
- [Playwright MCP](https://github.com/microsoft/playwright-mcp): headless browser verification inside Codespaces; built-in browser tools are optional.
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): branch, commit, PR, review, and merge.
- [Commit and PR smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions) and [PR summaries](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary).
- [GitHub Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) and [using Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions).
- [Container Apps with GitHub Actions](https://learn.microsoft.com/azure/container-apps/github-actions): deployment and registry authentication. The workshop uses its checked-in workflow, not every option in the guide.
- [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) and [whole-week coverage](../../docs/REFERENCES.md).
