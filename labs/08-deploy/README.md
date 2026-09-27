# Lab 08: Save, Share, and Keep Building

**Objective:** Review and preserve your work, explain one checked feature, and keep improving it.
Publishing through the prepared workflow is an optional supported extension.

**Time-box:** 45 minutes

**Prerequisites:** Your page and manual checks from Labs 00-02. Stay in browser-based Codespaces.
The core finish does not require Actions access, an Azure login, or a public URL.

> This lab runs on **Day 1**, after Lab 02. Lab numbers group topics; they are not the order
> of the week. See [the agenda](../../docs/AGENDA.md).

The 45 minutes cover review and saving (15), personal building or supported publication (20),
and a final check (10). At 14:45 the whole group moves to pair playback.

## Show and Try

The presenter repeats the save -> review -> commit -> push sequence, then stops for your turn.
The saved website is your work; a running preview is a separate thing. You may show your own
screen to a neighbour without making its port public.

## Steps

1. Save your files. Open **Source Control** and read the actual changes, not only Chat's summary.
   Keep only intended website assets and your fictional planning note. No credentials or private data.
2. Select the **+** beside each reviewed file, enter a short message, and **Commit**, then
   **... > Push**. Ask a helper about conflicts or a required PR; never force a push.
3. Open the assigned repository on GitHub and select the same branch. Confirm the latest
   message and your changed files are there. Saving in the editor alone does not complete this check.
4. Continue with one small improvement, or take the optional publishing route below with a helper.
   Repeat the relevant browser check after each change. Review, commit, and push the final version.
5. Show one feature to a neighbour and explain what you expected, what you observed, and any
   limitation. Record the next improvement in your brief rather than starting another large task.

**Done when:** your reviewed work is visible on GitHub, your page still works in the private
preview, and you can explain a real check. A deployment or saved browser state is not required.

## What you just learned

You can preserve and improve a project without starting again. A push stores commits on GitHub;
deployment deliberately publishes a running website. Neither proves the page works: you check it.

## If something goes wrong

| Symptom                               | Cause                                                 | Fix                                                                                                              |
| ------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Stops on **Read config.json**         | The prepared workshop label is missing                | Ask the helper to check the unique label before retrying.                                                        |
| Deployment rejected on the name       | Derived name is invalid                               | Names are lowercase, letters, digits and hyphens, 32 characters at most. Run `python app/config.py` to see yours |
| The run cannot sign in to Azure       | Organization secrets are missing                      | Tell the facilitator; nothing on your side is wrong                                                              |
| Stops on prepared access/commit check | Missing Actions configuration or the branch moved     | Ask the owner to check the named settings; retest the exact branch. Do not sign into Azure as a workaround.      |
| Page shows the vendor table           | Wrong deployment target or URL                        | Use the website target and its verified run-summary URL; do not overwrite the business app.                      |
| Website validation fails              | Missing entry point, invalid asset, or excessive size | Inspect `python -m app.site --check`; keep only intentional web assets under `site/`.                            |

## Optional extras

### Publish With a Helper

Choose this instead of further building when your page is ready and prepared access is available.
You can also use Tuesday's supported build time. A slow or blocked deployment does not prevent
Monday's core finish. Day 4 teaches the machinery in depth.

1. Ask the helper to confirm your unique label in `config.json`, the reviewed commit on `main`,
   and deployment access. The workflow retains tests, lint, asset validation, and revision checks;
   these are not replaced by the simplified instructions. Required PR review still applies.
2. In GitHub open **Actions > Deploy my app > Run workflow**. Choose **target: website** and
   leave **connect_dataverse** unchecked. Confirm the repository and branch. Click once.
3. When that run succeeds, open its **run summary** and the verified URL. Confirm this is your
   own website, not the separate vendor app. No attendee Azure sign-in is needed.
4. Repeat your actual button or add/remove check at this new URL. If you added remembering,
   test add -> refresh -> remove -> refresh here too. This URL starts with separate browser data;
   preview entries do not move automatically.
5. Agree how long the deployment will remain and who owns cleanup. Never delete shared resources.

**Publication checked when:** the intended website workflow succeeded, its verified URL serves
your reviewed page, and your chosen interaction works at that URL. Do not call a preview a deployment.

### Facilitator Checks, Not a Beginner Command List

Run these in Codespaces before dispatch when helping with a publication:

```bash
uv run python app/config.py --target website
uv run python -m app.site --check
uv run pytest
uv run ruff check .
```

The website target publishes only allowed `site/` assets; keep PDFs, extracts and private notes
out. Markdown is not served. Limits remain 2 MiB per asset, 100 files, and 20 MiB total. Asset
validation is not a full security scanner. Inspect JSON and images as well as code.
The workflow checks the exact commit and entry-page bytes/content fingerprint through `/healthz`
and the page response. Inspect those results if a run is ambiguous; a healthy older revision
is not this deployment. The website and vendor targets stay separate; never select vendor
as a workaround. Building with Copilot does not embed an AI runtime in the published page.

After saving and pushing, stop unused Codespaces through the Codespaces menu. Closing the tab
does not immediately stop compute. Stopping the Codespace does not delete a separate deployment.

## Official References

- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow): branch, commit, PR, review, and merge.
- [Commit and PR smart actions](https://code.visualstudio.com/docs/editing/copilot-smart-actions) and [PR summaries](https://docs.github.com/en/copilot/how-tos/copilot-on-github/copilot-for-github-tasks/create-a-pr-summary).
- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart) and [using Actions secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).
- [Container Apps with GitHub Actions](https://learn.microsoft.com/azure/container-apps/github-actions): deployment and registry authentication. The workshop uses its checked-in workflow, not every option in the guide.
- [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) and [whole-week coverage](../../docs/REFERENCES.md).
