# Minion Framework — writeups & assets

Everything specific to the post *"I Built Claude's Dynamic Workflows by Accident, Two Weeks Before Anthropic Shipped Them."* The Minion Framework is a SQLite-backed agent fan-out (N Claude Code "Armies", each spawning ephemeral "minions") used to build a ~25,000-record fine-tuning corpus on a flat-rate subscription instead of paying per-token API rates.

## Contents

- **`blog/blog_v12.html`** — the current blog post (the latest of the drafts; self-contained HTML).
- **`slides/`** — two variants of the talk deck (fixed-stage 16:9 HTML):
  - `minion-framework-slides.html` — Fraunces serif headlines
  - `minion-framework-slides-sans.html` — Hanken Grotesk (simpler) headlines
  - 20 slides each: about-the-author, the task, the Reddit-thread→JSON conversion, the architecture, Gru, the cost arbitrage, the Dynamic Workflows comparison, and a connect slide.
- **`images/`** — the Monet/Renaissance illustrations of "Gru and the Minion Armies" (several hero variants + the Gru console). The blog and decks reference `image1_hero_classroom.jpeg` and `image4_gru_console.jpeg`.
- **`generate_image.py`** — the script that produced these images (OpenRouter image models; the `PROMPTS` dict holds the exact Gru/Minion prompts).
- **`rl_parallels.md`** — a note arguing the framework is mostly *not* RL, and where the few honest parallels actually are.

## Notes

- **Image paths** in `blog/blog_v12.html` and both decks were rewritten to `../images/…` when this folder was created, so they resolve from here. Verified rendering.
- **`generate_image.py` paths** still assume the original scrape repo layout (it reads `../.env` and writes to `pilot/images/`). To re-run it from here, update `ENV_PATH` and `OUT_DIR` at the top of the file.
- **Left behind in the scrape repo on purpose:** the older blog drafts (`blog.html`, `blog_v1`–`blog_v11`), `blog_v6_edits.md` (the AI-tell editing pass), and `AGENT_WORKER_PROMPT.md` (the live worker prompt that runs the pipeline). Nothing was deleted — say the word if you want any of those pulled in or the old drafts cleaned up.

## See also (general guides, one level up)

- [`../writing-like-a-human.md`](../writing-like-a-human.md)
- [`../creating-blogs.md`](../creating-blogs.md)
- [`../generating-images.md`](../generating-images.md)
- [`../creating-presentations.md`](../creating-presentations.md)
