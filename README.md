# Writing

A working repository for writing, research, and the tooling around it. The top level holds **reusable, general guides**. Project-specific writeups live in their own subfolders.

## General guides

- **[writing-like-a-human.md](writing-like-a-human.md)** — how to write so it doesn't read like AI, the current "tells" that give AI away, how detectors actually work, and the affirmative craft of human writing. Doubles as a checklist for *evaluating* whether a piece was AI-written.
- **[creating-blogs.md](creating-blogs.md)** — how to structure and build a long-form blog post (narrative arc, the self-contained HTML format, diagrams, image slots, the draft→ship loop).
- **[generating-images.md](generating-images.md)** — generating editorial illustrations for posts via OpenRouter image models, and the prompt recipe that produces consistent, non-AI-slop art.
- **[creating-presentations.md](creating-presentations.md)** — turning a post into a fixed-stage HTML slide deck (the frontend-slides approach: 16:9 stage, inline SVG diagrams, style previews, verification).

## Projects

- **[minion-framework/](minion-framework/)** — everything specific to the "Minion Framework" post: the blog, the slide decks, the RL-parallels note, the image-generation script, and the illustrations.

## How these fit together

`writing-like-a-human` is the foundation — read it first. `creating-blogs` is the workflow that uses it. `generating-images` and `creating-presentations` are the two production steps that turn a finished draft into something shippable. Each project folder is a worked example of all four applied together.
