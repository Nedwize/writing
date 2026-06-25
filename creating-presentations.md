# Creating Presentations

How to turn a finished post into a self-contained HTML slide deck that looks designed, not templated. Worked examples (two font variants of the same deck) live in [`minion-framework/slides/`](minion-framework/slides/).

## The model: a fixed 16:9 stage that scales

The whole approach rests on one idea: **author every slide at a fixed 1920×1080 canvas, then scale the entire canvas to fit the window with a single CSS transform.** Don't reflow content responsively — letterbox/pillarbox instead. This is what keeps slides looking identical on a laptop, a projector, and a phone.

- A `.deck-viewport` fills the window; a `.deck-stage` is fixed at `1920×1080` with `transform-origin: 0 0`.
- One JS line on load/resize: `scale = min(innerWidth/1920, innerHeight/1080)`, then `translate` to center. That's the entire responsive story.
- Each `.slide` is absolutely positioned, `1920×1080`, toggled with `.active`/`.visible` classes (via `visibility`/`opacity`, **not** `display:none` — display toggling breaks later fl/grid layout rules).

## Building the deck

- **Single HTML file, inline CSS/JS, zero dependencies.** Fonts from Google Fonts / Fontshare — never system fonts as display type.
- **A controller class** handling: keyboard nav (arrows/space/Home/End), touch swipe, mouse wheel, a progress bar, and a page counter. Keep all chrome *outside* the stage so it doesn't scale.
- **Staggered reveal animations.** A `.reveal` class (opacity + translateY) with `transition-delay` steps (`.d1…d6`) applied to a slide's children on `.visible`. One well-orchestrated entrance per slide beats scattered micro-animations.
- **Respect `prefers-reduced-motion`** — collapse animation durations.
- **Inline editing affordance** (optional): a hover hotzone + `E` key that toggles `contenteditable` on text, so you can fix copy in the browser.

## Make it look authored, not "AI deck"

- **Commit to one aesthetic** with `:root` variables and carry it across every slide. The example decks use a "Field Manual" look (cream/ink/rust, a faint engineering-grid background, a mono running header/footer, serif or grotesk display).
- **Diagrams are inline SVG**, redrawn in the deck's palette — the same architecture/data-flow diagrams from the post, not screenshots. Crisp at any scale.
- **Reuse the post's illustrations** as framed "plates" with mono captions. The deck and the blog should feel like the same object.
- **Pick a font deliberately.** Avoid the defaults everyone converges on (Inter, Roboto, Space Grotesk). The example keeps two variants — an ornate serif (Fraunces) and a clean sans (Hanken Grotesk) — so you can A/B the feel.

## Pacing: speaker-led vs reading-first

Decide up front who the deck is for:

- **Speaker-led / sparse:** one idea per slide, big type, lots of air, more slides. Use for live talks.
- **Reading-first / dense:** self-contained slides with tables, captions, annotated diagrams. Use for async sharing.

When a slide overflows, **split it into two** — never shrink type until it's cramped.

## The style-preview step

Before building the whole deck, generate **three single-slide title previews** in different directions (e.g. a safe option, a bold option, and a wildcard that matches the source material), open them, and let the human pick. People discover what they want by seeing it, not by describing it. Then build the full deck in the chosen direction.

## Verify before you ship

Render the deck headless (Playwright/Chromium) and check, for every slide:

- **No overflow:** each `.slide` has `scrollWidth ≤ 1920` and `scrollHeight ≤ 1080`.
- **Images resolve:** every `<img>` has `naturalWidth > 0` (catches broken relative paths after moving files).
- **Screenshot the key slides** at 1280×720 and eyeball them.

This catches the two failure modes that matter — content spilling off the fixed stage, and broken asset paths — before anyone opens it.

## Tooling note

These decks were built with the **frontend-slides** Claude Code skill, which encodes this whole flow (style previews → fixed-stage generation → verification). The output is a plain HTML file, so it stands on its own without the skill.
