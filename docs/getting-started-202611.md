# Getting started: building searenityonlummi.com with Claude (November 2026)

This guide is a snapshot from November 2026, written for Dave's first setup. Apps and screens change, so if a step no longer matches what you see, ask Claude or Steve rather than following it exactly. For how things work today, see [AGENTS.md](../AGENTS.md) and the [infrastructure runbook](setup.md).

Hi Dad! This guide gets you from nothing to working on the website with Claude, an AI assistant that can write the website for you while you tell it what you want. Expect about an hour for the setup. You won't need to write the code yourself; Claude does that part and explains what it is doing as it goes, and you can dig into the details as much as you like.

Where things are already set up:

- The website address **searenityonlummi.com** works and shows a "coming soon" page.
- The website's files live on GitHub at [github.com/BigLep/searenityonlummi.com](https://github.com/BigLep/searenityonlummi.com), and you have access as **davidloeppky**. When you tell Claude to publish, the live site updates within a couple of minutes.

If you get stuck at any step, take a screenshot and send it to Steve.

## What you need

- Your Mac, and its password (installers will ask for it).
- Your GitHub password for **davidloeppky**.
- The Claude guest pass link Steve sent you.
- Your septic writeup: the Pages document, the PDF, and the original photos and videos.

## Step 1: Get a Claude account

Wait to do this until the day you plan to start, because the trial clock starts when you accept it.

1. Open the guest pass link from Steve and sign up with your usual email address.
2. The pass gives you 7 days of Claude Pro free. Pro is what lets Claude build things on your computer.
3. After 7 days it becomes $20/month unless you cancel. If you are enjoying it, keep it; if not, cancel in Claude's settings under billing before the 7 days end.

## Step 2: Install the Claude app

1. Go to https://claude.ai/download, download the Mac app, and drag it into Applications.
2. Open it and sign in with the same email address.

## Step 3: Make a folder for the website

1. In Finder, open your **Documents** folder.
2. Make a new folder called **searenityonlummi.com**. Leave it empty.

## Step 4: Start Claude in that folder

1. In the Claude app, switch to **Code** (Claude's mode for working with files on your Mac).
2. When it asks which folder to work in, choose the **searenityonlummi.com** folder you just made.
3. Copy this message into Claude and send it:

> I'm Dave. I'm not a programmer and I'm new to Claude. Please download the website from https://github.com/BigLep/searenityonlummi.com into this folder, then read AGENTS.md and help me finish setting up so you can publish changes for me. Walk me through anything I need to click.

What to expect while Claude sets up:

- **Permission requests.** Claude asks before running commands on your Mac. Most routine ones are pre-approved. If it asks and the explanation makes sense, allow it. If you are unsure, ask Claude "what does this do?" before answering.
- **A popup to install "Command Line Tools".** Click **Install** and wait for it to finish (it can take 5 to 10 minutes). This is normal and only happens once.
- **Installing the GitHub tool.** Claude will download an installer; click through it like any Mac app installer.
- **Signing in to GitHub.** Claude will give you a short code (like `ABCD-1234`). Go to https://github.com/login/device, sign in as **davidloeppky**, paste the code, and approve.

## Step 5: Put your material where Claude can see it

Claude will have created a folder called **originals** inside your website folder. Anything in **originals** stays on your Mac and is never put on the website; Claude makes smaller, cleaned-up copies of the photos it uses.

Copy into **originals**:

- The Pages document and the PDF.
- The **original** photos, not the ones inside the PDF (those are lower quality). In the Photos app, select the photos, then choose **File > Export > Export Unmodified Original**, and pick the **originals** folder.
- The videos.

## Step 6: Plan the site with Claude

Send Claude:

> Interview me about the website I want to build before you build anything.

Claude will ask about what the site should cover, who it is for, how to handle the videos, what should stay private, and how it should look and be laid out. Answer as much or as little as you like; you can change your mind later.

## Ideas for what to say next

Once the plan is set, talk to Claude the way you would to a helpful person sitting next to you.

Big-picture ideas, good early on:

- "What would be a creative way to showcase this project? A single scrolling story? Something more like a photo book or a slide deck?"
- "Show me two or three different looks for the home page so I can pick one."
- "Tell the septic project as a timeline, from the old system failing to the final inspection."
- "Make a before-and-after comparison I can slide back and forth."
- "Explain how a septic system works with a simple diagram, for visitors who have never thought about it."
- "Which of my photos are the strongest? Suggest a few for the home page."
- "Write a short 'lessons learned' section from my notes, in my voice."

Everyday requests:

- "Make a page for the septic project from my PDF, using the original photos."
- "Show me the site on my computer." (You will see it in your browser before anyone else does.)
- "The photo of the tank going in should be bigger, and put it first."
- "Rewrite this section so it is shorter and less technical."
- "Undo the last change." or "Go back to how it looked yesterday."
- "Publish it." (This updates the live website. Claude will check with you first.)
- "What did we do last time, and what is left?"

## Each time you come back

Open the Claude app, switch to **Code**, choose the **searenityonlummi.com** folder, and start with:

> Get the latest version of the site, and remind me where we left off.

## Good to know

- **Nothing goes live until you say "publish".** Everything before that happens only on your Mac.
- **You cannot really break anything.** Every change is saved in a history, and Claude can go back to any earlier version.
- **The website is public, and so are its files on GitHub.** Even something removed later stays in the history. Think twice before publishing addresses, permit documents, or other people's faces or names.
- **When Claude gets something wrong, say so.** "That's not right, the tank was delivered in May" works fine.
