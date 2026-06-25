# CLAUDE.md

Working repo for writing + the tooling around it. General guides live at the top level; each project has its own folder.

## Before you write or build
- Read the relevant guide first: `writing-like-a-human.md`, `creating-blogs.md`, `generating-images.md`, `creating-presentations.md`.
- Match the house voice in `writing-like-a-human.md`. Always do an AI-tell pass before calling a draft done: cut em-dash overuse, the "it's not X, it's Y" template, tripled lists, "it's worth noting", and inflated words. Keep specifics, opinions, and real anecdotes.

## Git
- Remote `origin`: `git@github.com:Nedwize/writing.git`. Default branch is `main`.
- **Always use [Conventional Commits](https://www.conventionalcommits.org/)** — `<type>(<optional scope>): <description>` (e.g. `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`).

## Conventions
- **Blogs & decks are single self-contained HTML files** — inline CSS/JS, zero dependencies, opens in a browser.
- **Palette:** cream `#f6f3ec`, ink `#1c1b18`, one rust accent `#7a3b1f`. Body max-width `70ch`. Set colors in `:root`.
- **Diagrams are inline SVG** in that palette — never raster/screenshots.
- **Version drafts** as `blog_vN.html`; never overwrite the previous one.
- **Slides:** fixed 1920×1080 stage scaled to the window (see `creating-presentations.md`). Don't reflow per device.

## Starting a new project
One kebab-case folder per project (mirror `minion-framework/`):
```
<project-name>/
├── README.md          # what it is, contents, any path caveats
├── blog/
│   └── blog_v1.html   # drafts, versioned (v1, v2, …)
├── images/            # illustrations
├── slides/            # optional: decks
└── notes.md           # optional: supporting notes
```
- Paths from `blog/` and `slides/` point to `../images/`.
- Start `README.md` from day one; add the project to the top-level `README.md` index.
- Only `slides/` and extra notes are optional — `README.md`, `blog/`, and `images/` are the baseline.

## Images
- Generate with `minion-framework/generate_image.py` (OpenRouter). Follow the prompt recipe in `generating-images.md`: name a real artist + mechanics, anchor to specific works, pin the palette with one accent, and always include an explicit `Avoid:` list.

## Working rules
- **Never delete drafts or move files without asking.** Default to copy unless told to move.
- After moving any HTML, **fix relative image paths and verify images render** (headless load, `naturalWidth > 0`).
- For decks, **verify no slide overflows** the 1920×1080 stage before shipping.
- Keep general/reusable knowledge at the top level; keep project-specific work in its folder.
