# Creating Blogs

How to take a technical story from "I did a thing" to a shippable long-form post. This is the workflow; pair it with [writing-like-a-human.md](writing-like-a-human.md) for the prose itself.

## The format: one self-contained HTML file

Every draft is a single `.html` file with inline `<style>` — no build step, no framework, opens in any browser. It makes the post portable, diffable, and easy to iterate on (you just save a new `blog_vN.html`). The house style that worked:

- **Editorial, paper-like palette.** Warm cream background (`#f6f3ec`), near-black ink (`#1c1b18`), one accent color (a rust `#7a3b1f`), muted gray for secondary text. Set it in `:root` CSS variables so the whole post retunes from one place.
- **A reading measure, not full width.** `article { max-width: 70ch }`. Long lines kill readability.
- **System font stack for body, mono for code.** Don't over-design the body; let the structure carry it.
- **Reusable components as CSS classes:** `.dek` (italic standfirst), `.callout` (accent-bordered aside), `.footnote`, `.image-slot` (a placeholder describing an image to generate later), tables, and `pre` code blocks.

## The narrative arc

A good technical post is a story, not a manual. The shape that worked:

1. **Open in the middle of the action.** Lead with the concrete situation and the tension — "I needed X, I had $200" — not with background. (See *pacing / in medias res* in the human-writing guide.)
2. **State the stakes with real numbers.** Specific figures (`$7,250`, `25,000 records`, `~36×`) are credibility. Never "a large dataset."
3. **Walk the attempt → the failure → the insight.** The failure mode is the most valuable part; it's what the reader can't get from docs.
4. **Show the solution concretely.** Real code, a real schema, a diagram of the actual architecture.
5. **Compare honestly.** A "where each approach wins/loses" table reads as trustworthy precisely because it concedes things.
6. **End on the strongest sentence.** No "In conclusion." Land the takeaway and stop.

## Structural ingredients that pull weight

- **A dek / standfirst** under the title: one sentence (or three short ones) that says what the post is and what each thing does.
- **Diagrams as inline SVG, not raster.** Hand-author SVG boxes-and-arrows in the post's palette. They stay crisp at any zoom, diff cleanly, and never look like stock art. Keep an ASCII version too for the terminal-reader aesthetic if it fits.
- **Comparison tables** for any "A vs B."
- **A footnote / aside** for the honest technical caveat that interrupts the flow — this is a strong human signal (AI rarely volunteers its own caveats).
- **Code blocks** showing the *one* load-bearing snippet, not everything.
- **Image slots.** Mark where an illustration goes with a placeholder block that contains the *prompt* for it, so image generation is a separate, later step. See [generating-images.md](generating-images.md).

## The draft → ship loop

- **Save versioned files** (`blog_v1.html`, `v2`, …). It's a free undo history and lets you compare directions.
- **Keep a "title candidates" scratch block** at the top of the draft (a dashed-border aside) while iterating — straight options, punchy options, "HN-bait" options. Delete it before publishing.
- **Do an AI-tell editing pass.** Once the draft reads well, run it against [writing-like-a-human.md](writing-like-a-human.md): cut em-dash overuse, the "it's not X, it's Y" template, tripled lists, sign-posty meta-sentences ("It's worth noting…"), and inflated vocabulary. Keep the specifics, the opinions, and the real anecdotes. (The minion-framework project has a worked example of this pass.)
- **Read the first line and the last line in isolation.** The first should hook mid-thought; the last should be quotable.

## Checklist before shipping

- [ ] Opens with a concrete scene/number, not background or a thesis statement
- [ ] Every "large/many/expensive" replaced with a real figure
- [ ] One strong opinion stated without hedging
- [ ] Diagrams are inline SVG in the post's palette
- [ ] An honest caveat/footnote is present
- [ ] AI-tell pass done (em dashes, antithesis template, rule-of-three, "it's worth noting", inflated words)
- [ ] Title block scratch aside deleted
- [ ] Ends on the strongest sentence, no "In conclusion"
- [ ] Image slots filled (or prompts left for the image step)
