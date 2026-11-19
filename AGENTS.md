# Searenity on Lummi website

This repo is the website at https://searenityonlummi.com. It belongs to Dave Loeppky ([davidloeppky](https://github.com/davidloeppky) on GitHub), who co-owns Searenity on Lummi (a family property on Lummi Island, Washington, where family and friends gather). The site has a calendar, favourite pictures, property logistics, and projects, starting with a septic system he installed. See [docs/site-plan.md](docs/site-plan.md) for the agreed plan and privacy decisions. Terms used here are defined in [GLOSSARY.md](GLOSSARY.md).

These instructions are for any coding agent (Claude Code, Codex, or others). [CLAUDE.md](CLAUDE.md) is a symlink to this file; keep all agent instructions here rather than in agent-specific files. [.claude/settings.json](.claude/settings.json) pre-approves routine commands for Claude only; the rules it encodes (always ask before `git push`, never force push, never `git reset --hard` or `git clean`) apply to every agent.

## Which kind of session this is

- **Dave's session** (the usual case): Dave is building the site. Everything below applies. Do not touch DNS, AWS, or GitHub settings; if something there seems wrong, tell Dave to contact Steve. Change the publish workflow ([.github/workflows/pages.yml](.github/workflows/pages.yml)) only when adding a build step (see [How the site is built](#how-the-site-is-built)).
- **Maintainer session** (Steve, or an agent Steve is running): infrastructure work (domain, DNS, GitHub Pages, collaborators, the publish workflow). Start with [docs/setup.md](docs/setup.md), which has the inventory, access, health check, common tasks, and rebuild steps. Keep that file accurate when anything changes.

## Who you are working with

Dave is comfortable with computers and has done a lot of coding in the past, but is not a current software developer, has not used Claude before, and is using the Claude desktop app rather than a terminal. Work with him like a capable collaborator:

- Explain what you are about to do and what happened afterwards. He can follow technical explanations, but name current tools and conventions (git, GitHub, modern HTML/CSS) briefly rather than assuming he knows them.
- When you need him to click something (a macOS popup, a browser sign-in, an installer), say exactly what he will see and what to click.
- Make routine technical choices yourself and tell him what you chose; he may have opinions, so offer the reasoning on bigger ones. Ask him about content, look and feel, and anything that will appear publicly.
- Content is his. Write in his voice from his material, and check with him before inventing facts, numbers, or claims about the work.
- If something goes wrong, say so plainly, fix it if you can, and if you cannot, tell him what to send his son Steve (who set this up) so Steve can help.

## First session

If [site/index.html](site/index.html) is still the "coming soon" placeholder, this is the start of the project. Before building anything, interview Dave, a few questions at a time, and write what you learn into `docs/site-plan.md` (commit it). Cover:

1. **Scope**: is the site about Searenity on Lummi as a place, with a section for each project? Or only the septic project for now? What other projects might he add later?
2. **Audience**: who is it for (family, neighbours, other DIY builders, future buyers, contractors)? This shapes tone and detail.
3. **Source material**: where are his Pages document, the exported PDF, the original photos, and the videos? Help him copy them into `originals/` (see [Files](#files)).
4. **Videos**: how many, how long, how large? Recommend unlisted YouTube for anything longer than about 30 seconds or larger than about 20 MB, and help him upload if he agrees. Short clips can live in `site/`.
5. **Privacy**: everything published is public, and this repo is public, so even deleted files stay visible in history. Ask him about: street address and house number, permit or inspection documents (often show address and parcel number), names and faces of people other than Dave and family, contractors and suppliers (name them or not), neighbours' property visible in photos, and costs.
6. **Presentation**: any sites he likes, colours, photos he wants on the home page, and the overall form: a conventional multi-page site, a single scrolling story, something closer to a photo book or slide deck. Offer a couple of ideas suited to his material. If he wants to explore looks visually before building, mention [Claude Design](https://www.anthropic.com/news/claude-design-anthropic-labs) (included in his Claude plan): he can try layouts there and hand the result back to build here. It is optional; the default is to iterate on real pages in this repo.

Then propose a page outline and get his OK before building.

## Design help (Claude only)

Once the first real page exists and Dave is working on how the site looks, offer once to install Anthropic's official [frontend-design plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design), which helps produce distinctive pages instead of generic-looking ones. Explain what it does in a sentence, and only install it if he agrees (`/plugin install frontend-design@claude-plugins-official`, or the Desktop app's plugin settings). Then use it for design work. Other agents skip this section.

## How the site is built

- Start with plain HTML and CSS in [site/](site/), with a shared stylesheet (`site/style.css`). Keep it readable by any future helper.
- A build step (a static site generator, image processing, templates for shared headers) is fine when it clearly helps, for example once there are many pages repeating the same layout. Propose it to Dave with the reason first. Choose tools that run on GitHub Actions without secrets, update [.github/workflows/pages.yml](.github/workflows/pages.yml) to build before the upload step, keep the metadata and file-size checks running on the built output, and document the build and local preview commands in this file.
- Pages must work well on both phones and computers; people will often open the site from a link sent by text or email.
- Only the published folder (`site/` today) goes live. Everything else in the repo is never published.

## Files

- `originals/`: Dave's full-size photos, videos, Pages and PDF files. Git ignores it ([.gitignore](.gitignore)), so it never leaves his Mac. Never delete or modify files here; make copies.
- [site/](site/): the published website.
- `site/images/`: web-sized copies of photos. For each photo used:
  1. Copy from `originals/` and convert HEIC to JPEG if needed: `sips -s format jpeg IN.heic --out site/images/NAME.jpg`.
  2. Resize so the long edge is at most 2000 px: `sips -Z 2000 site/images/NAME.jpg`.
  3. Remove hidden location and camera data: `python3 tools/strip-metadata.py site/images`.
  4. If a photo now appears sideways, rotate it with `sips -r 90` (or 180, 270). Always look: many iPhone HEICs store their rotation where `sips -g orientation` reports `<nil>`, and `sips` conversion does not apply it, so the copy comes out sideways (orientation 6 needs `sips -r 90`).
  Use short lowercase file names with dashes (`septic-tank-delivery.jpg`), and give every image `alt` text describing what it shows.
- [tools/strip-metadata.py](tools/strip-metadata.py): removes GPS and camera metadata from JPEG and PNG files. `--check` reports any that still have it.
- [docs/](docs/): notes about the project, including Dave's [getting-started guide](docs/getting-started-202611.md), the site plan, and the [infrastructure runbook](docs/setup.md).

To read text and structure from the PDF, read it directly. Prefer the original photos over images inside the PDF, which are usually compressed; ask Dave to match captions to photos when unclear.

## Saving and previewing

- After each meaningful change, commit using [Conventional Commits](https://www.conventionalcommits.org/): `type: short description`, for example `feat: add septic tank delivery photos`, `fix: correct tank install date`, `docs: update site plan`, `style: enlarge home page photos`. Use plain words after the prefix. Commits give Dave an undo history; tell him he can ask you to go back to an earlier version anytime.
- Before publishing, show Dave the site locally: run `python3 -m http.server 8000 -d site` in the background and `open http://localhost:8000`.
- Run `python3 tools/strip-metadata.py --check site` before every publish.

## Publishing

Publishing means `git push` to `main`. GitHub then checks the site and publishes it at https://searenityonlummi.com, usually within two minutes.

- Only push when Dave has said to publish. Ask "Ready to publish this to the live site?" after he has seen the local preview.
- Before pushing, run `git pull --rebase` in case Steve changed something.
- After pushing, watch the publish with `gh run watch` and tell Dave when it is live, or explain any failure. The publish checks fail if an image still has location data or a file is over 25 MB.
- Never force push, rewrite history, or delete branches. If git gets into a state you do not understand, stop and have Dave contact Steve.

## Setup on a new Mac

If `gh` is not installed or not signed in (`gh auth status`), help Dave install the GitHub CLI from its macOS installer at https://github.com/cli/cli/releases (the `.pkg` file), then run `gh auth login --web --git-protocol https -h github.com` in the background. It prints a one-time code (also copied to the clipboard) and waits; tell Dave the code, have him open https://github.com/login/device, paste it, and approve. When it finishes, run `gh auth setup-git`. He signs in to GitHub as `davidloeppky`. Create the `originals/` folder if it does not exist and show it to him in Finder (`open originals`). The first git command may trigger a macOS popup to install the Command Line Tools; tell him to click Install and wait for it to finish.
