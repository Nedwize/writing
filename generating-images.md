# Generating Images for Writing

How to make editorial illustrations for a post that look intentional — not like AI slop. There's a working reference implementation at [`minion-framework/generate_image.py`](minion-framework/generate_image.py); this guide is the general version of what it does and the prompt recipe that makes it work.

## The mechanism: OpenRouter image models

One small Python script, no SDK. It POSTs a prompt to OpenRouter's `chat/completions` with an image modality, decodes the returned base64, and saves a PNG. Key points from the working script:

- **Endpoint:** `POST https://openrouter.ai/api/v1/chat/completions` with an `Authorization: Bearer <OPENROUTER_API_KEY>` header (read the key from a local `.env`, never hardcode).
- **Body:** `{ "model": <id>, "messages": [{"role":"user","content": <prompt>}], "modalities": [...] }`.
- **Modalities differ by model family:** FLUX models (`black-forest-labs/flux.2-…`) emit image-only → `["image"]`. Google/Gemini image models emit image+text → `["image","text"]`. Branch on the model id.
- **Response shape is inconsistent:** the image can arrive as `choices[0].message.images[*].image_url.url`, or inside `message.content` as an `image_url` part, or as a bare `data:image/...;base64,…` string. Walk all three and grab the first `data:image/` you find.
- **Decode + save:** regex out `data:image/(\w+);base64,(.+)`, `base64.b64decode`, write bytes to `<name>.<ext>`.
- **Log the cost:** after generation, GET `https://openrouter.ai/api/v1/generation?id=<gen_id>` to print the actual `total_cost`. Image gen is cheap but it's good discipline to see it.

Store prompts in a dict keyed by output name so regenerating a specific image is `python3 generate_image.py <name> <model_id>`. This makes prompts versioned, diffable, and re-runnable.

## The prompt recipe (this is what matters)

Generic "make an illustration of X" gives you AI slop. The formula that produced cohesive, magazine-quality art:

1. **Name a real artist / movement and its mechanics.** Not "impressionist" but *"in the style of Claude Monet's impressionist paintings — visible broken brushstrokes, dappled light, soft edges, no hard outlines."* Naming the mechanics (brushstrokes, edges, light) does more than naming the style.
2. **Anchor the composition to specific named works.** *"Compositionally inspired by Monet's La Grenouillère and his garden-at-Giverny scenes."* Real paintings give the model a concrete spatial template.
3. **Describe the scene as blocking, left-to-right.** Who's where, facing which way, doing what. Spell out posture and orientation ("faces right, toward the figures, like a teacher addressing a classroom").
4. **Pin the palette explicitly, with one accent.** List the actual colors (*"lavender, soft blue, olive green, pale ochre, pearly cream"*) and reserve a single accent that matches your post (*"a single rust-brown accent"*). One accent is what makes a set of images feel like a series.
5. **Write an explicit `Avoid:` list.** This is the anti-slop clause. *"Avoid: glossy 3D, neon, sharp digital outlines, AI-art tropes, readable text/labels, water."* Negative prompts kill the defaults that scream "AI made this."
6. **Specify aspect/format** ("wide horizontal composition", "cream paper background") so it drops into the post cleanly.

## Practical notes

- **Generate variants, then choose.** The reference script kept several takes of the hero (`_classroom`, `_clean`, `_monet_v2`, `_renaissance`). Cheap to over-generate and pick.
- **Match the art to the post's palette.** The single-accent rule should use the *same* accent as your CSS (`--accent`). That's why the illustrations and the prose feel like one object.
- **No readable text in images.** Models render garbled text; explicitly forbid labels and put real labels in the surrounding HTML/SVG instead.
- **Keep the prompts with the project**, not here — they're project-specific. This guide is the reusable method; the minion-framework folder is the worked example.

## Caveat about the reference script

`minion-framework/generate_image.py` was written to run from inside the original scrape repo: it reads `../.env` and writes to `pilot/images/`. To reuse it elsewhere, update `ENV_PATH` and `OUT_DIR` at the top of the file, and swap the `PROMPTS` dict for your own.
