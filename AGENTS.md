# Searenity on Lummi website

This repo is the website at https://searenityonlummi.com. It belongs to Dave Loeppky, who lives at Searenity on Lummi (the family home on Lummi Island, Washington) and uses the site to showcase his construction projects, starting with a septic system he installed. Terms used here are defined in [GLOSSARY.md](GLOSSARY.md).

These instructions are for any coding agent (Claude Code, Codex, or others). `CLAUDE.md` is a symlink to this file; keep all agent instructions here rather than in agent-specific files. `.claude/settings.json` pre-approves routine commands for Claude only; the rules it encodes (always ask before `git push`, never force push, never `git reset --hard` or `git clean`) apply to every agent.

## Which kind of session this is

- **Dave's session** (the usual case): Dave is building the site. Everything below applies. Do not touch DNS, AWS, GitHub settings, or `.github/`; if something there seems wrong, tell Dave to contact Steve.
- **Maintainer session** (Steve, or an agent Steve is running): infrastructure work (domain, DNS, GitHub Pages, collaborators, the publish workflow). Start with [docs/setup.md](docs/setup.md), which has the inventory, access, health check, common tasks, and rebuild steps. Keep that file accurate when anything changes.

## Who you are working with

Dave is comfortable with computers but is not a programmer, has not used Claude before, and is using the Claude desktop app rather than a terminal. Work with him like a patient, capable helper:

- Explain what you are about to do in plain language before doing it, and what happened afterwards. No jargon without a one-line explanation.
- When you need him to click something (a macOS popup, a browser sign-in, an installer), say exactly what he will see and what to click.
- Make the technical choices yourself and tell him what you chose. Ask him about content, look and feel, and anything that will appear publicly.
- Content is his. Write in his voice from his material, and check with him before inventing facts, numbers, or claims about the work.
- If something goes wrong, say so plainly, fix it if you can, and if you cannot, tell him what to send his son Steve (who set this up) so Steve can help.

## First session

If `site/index.html` is still the "coming soon" placeholder, this is the start of the project. Before building anything, interview Dave, a few questions at a time, and write what you learn into `docs/site-plan.md` (commit it). Cover:

1. **Scope**: is the site about Searenity on Lummi as a place, with a section for each project? Or only the septic project for now? What other projects might he add later?
2. **Audience**: who is it for (family, neighbours, other DIY builders, future buyers, contractors)? This shapes tone and detail.
3. **Source material**: where are his Pages document, the exported PDF, the original photos, and the videos? Help him copy them into `originals/` (see Files below).
4. **Videos**: how many, how long, how large? Recommend unlisted YouTube for anything longer than about 30 seconds or larger than about 20 MB, and help him upload if he agrees. Short clips can live in `site/`.
5. **Privacy**: everything published is public, and this repo is public, so even deleted files stay visible in history. Ask him about: street address and house number, permit or inspection documents (often show address and parcel number), names and faces of people other than Dave and family, contractors and suppliers (name them or not), neighbours' property visible in photos, and costs.
6. **Look and feel**: any sites he likes, colours, photos he wants on the home page.

Then propose a page outline and get his OK before building.

## How the site is built

- Plain HTML and CSS in `site/`, with no build step, framework, or package manager. Pages can share one stylesheet (`site/style.css`). Keep it simple enough that any future helper can read it.
- Every page must work well on a phone, since that is how most people will see it.
- Pages are published exactly as they are in `site/`. Anything outside `site/` is never published.

## Files

- `originals/`: Dave's full-size photos, videos, Pages and PDF files. Git ignores it, so it never leaves his Mac. Never delete or modify files here; make copies.
- `site/`: the published website.
- `site/images/`: web-sized copies of photos. For each photo used:
  1. Copy from `originals/` and convert HEIC to JPEG if needed: `sips -s format jpeg IN.heic --out site/images/NAME.jpg`.
  2. Resize so the long edge is at most 2000 px: `sips -Z 2000 site/images/NAME.jpg`.
  3. Remove hidden location and camera data: `python3 tools/strip-metadata.py site/images`.
  4. If a photo now appears sideways, rotate it with `sips -r 90` (or 180, 270).
  Use short lowercase file names with dashes (`septic-tank-delivery.jpg`), and give every image `alt` text describing what it shows.
- `tools/strip-metadata.py`: removes GPS and camera metadata from JPEG and PNG files. `--check` reports any that still have it.
- `docs/`: notes about the project, including Dave's getting-started guide and the site plan.

To read text and structure from the PDF, read it directly. Prefer the original photos over images inside the PDF, which are usually compressed; ask Dave to match captions to photos when unclear.

## Saving and previewing

- After each meaningful change, commit with a short message that says what changed in plain words ("Add septic tank delivery photos"). This gives Dave an undo history; tell him he can ask you to go back to an earlier version anytime.
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
