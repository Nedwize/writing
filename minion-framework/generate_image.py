"""Generate a single image via OpenRouter image-generation models.

Reads OPENROUTER_API_KEY from ../.env. Saves base64-decoded PNG to ./images/.
Usage:
    python3 pilot/generate_image.py <output_name> <model_id>

Example:
    python3 pilot/generate_image.py image1_hero black-forest-labs/flux.2-klein-4b
"""

from __future__ import annotations

import base64
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
OUT_DIR = ROOT / "pilot" / "images"


def load_api_key() -> str:
    if not ENV_PATH.exists():
        raise SystemExit(f"No .env at {ENV_PATH}")
    for raw in ENV_PATH.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip() == "OPENROUTER_API_KEY":
            return v.strip().strip('"').strip("'")
    raise SystemExit("OPENROUTER_API_KEY not found in .env")


PROMPTS = {
    "image1_hero": (
        "Editorial illustration in the style of Claude Monet's impressionist "
        "paintings — visible broken brushstrokes, dappled light, soft edges, no "
        "hard outlines. Compositionally inspired by Monet's La Grenouillère "
        "(group of figures around water) and his garden-at-Giverny scenes. "
        "A tall narrow figure (silhouette of Gru from Despicable Me — long "
        "black coat, scarf, pointy nose) stands on the left in backlit "
        "silhouette, holding a clipboard, treated as a Monet figure-in-a-"
        "landscape. Below and to the right, sixteen small Minion figures "
        "(yellow ovals, blue overalls, goggles) at little desks with glowing "
        "terminals, rendered as quick impressionist dabs rather than crisp "
        "cartoons — think the figures in Monet's Sunday at Argenteuil. Faint "
        "atmospheric lines connect every Minion to a central database glow "
        "labeled 'work_queue'. Palette: Monet's typical lavender / mauve / "
        "soft blue / olive green / pale ochre / pearly cream, with a single "
        "accent of rust-brown for Gru's clipboard and the queue's central "
        "glow. Cream paper background. Wide horizontal composition. Avoid: "
        "glossy 3D, neon, sharp digital outlines, AI-art tropes."
    ),
    "image4_gru_console": (
        "Editorial illustration in the style of Claude Monet's interior "
        "figure paintings (Camille at the Window 1873, Le Déjeuner 1873) — "
        "visible broken brushstrokes, dappled morning light through a tall "
        "window, soft edges, no hard outlines. The figure rendered as "
        "light-and-color rather than crisp form. "
        "COMPOSITION: a quiet study scene viewed from a three-quarter angle. "
        "A tall thin figure clearly evoking Gru from Despicable Me — bald "
        "head with pale tan skin (NOT a black silhouette, give him his "
        "actual cartoon coloring), long pointed nose, long dark "
        "charcoal-gray tailored coat, gray-and-blue striped scarf — sits "
        "at a sturdy wooden writing desk in the center-right of the frame. "
        "He holds a steaming porcelain mug in one hand. In front of him on "
        "the desk: a single matte monitor glowing softly with a tabular "
        "dashboard — visible as abstract rows of numbers and a horizontal "
        "gauge bar at the bottom filled about three-quarters of the way in "
        "rust-brown. The monitor's soft glow is the focal point in the "
        "interior shadow, but it is not aggressive or neon. "
        "TO HIS LEFT, a tall French window with white curtains parted, "
        "opens onto a sunlit green meadow outside. Through the window, "
        "blurred and atmospheric in the impressionist tradition, distant "
        "rows of small Minion figures (yellow capsule bodies, blue "
        "overalls, round goggles) sit at little wooden desks across the "
        "meadow — painted as quick impressionist dabs, very small and "
        "distant, like Monet's distant figures in his garden scenes. The "
        "window provides the room's primary morning light. Solid grassy "
        "ground outside, absolutely no water, no pond, no river. "
        "Mood: calm, attentive, morning warmth. Gru is observing, not "
        "panicked. "
        "Palette: lavender shadows in the interior, soft peach and pearly "
        "cream in the window light, warm wood tones on the desk, the "
        "monitor's gentle rust-brown gauge as the single accent, distant "
        "emerald green and cerulean blue in the outdoor scene through the "
        "window. Near-square or wide composition. "
        "Avoid: glossy 3D, neon, sharp digital outlines, AI-art tropes, "
        "water or pond outside the window, Gru as a pure black silhouette "
        "(give him pale cartoon skin), bright or aggressive monitor glow "
        "that overwhelms the scene, modern minimalist office decor (it's a "
        "writer's study, not a tech office), any readable text on the "
        "dashboard (the rows should be abstract number-shapes, not "
        "letters)."
    ),
    "image1_hero_classroom": (
        "Editorial illustration in the style of Claude Monet's outdoor "
        "impressionist paintings — visible broken brushstrokes, dappled "
        "sunlight, soft edges, no hard outlines. Compositionally inspired by "
        "Monet's sunlit garden scenes (Garden at Giverny, Poppies at "
        "Argenteuil, The Artist's Garden at Vétheuil) — a bright midday "
        "meadow with green grass, scattered wildflowers, cerulean blue sky "
        "with soft white clouds. Solid grassy ground throughout — absolutely "
        "no water, no pond, no river. "
        "COMPOSITION: a classroom-style arrangement. On the LEFT, at the "
        "front of the scene, stands a tall thin figure clearly evoking Gru "
        "from Despicable Me — bald head with pale tan skin (NOT a black "
        "silhouette, give him his actual cartoon coloring), long pointed "
        "nose, long dark charcoal-gray tailored coat, gray-and-blue striped "
        "scarf — rendered impressionistically as a Monet figure but with "
        "natural skin tone visible. He holds a clipboard and FACES RIGHT, "
        "toward the Minions, in the posture of a teacher addressing a "
        "classroom. "
        "To the right, sixteen small Minion figures (yellow capsule bodies, "
        "blue overalls, round goggles) sit in NEAT ROWS at small wooden "
        "writing desks placed on the grass — each Minion oriented FACING "
        "LEFT toward Gru, like attentive students facing their teacher at "
        "the front of a classroom. Each desk has a small matte laptop or "
        "open notebook on it, lit by ordinary daytime sun — no glowing "
        "screens, no artificial light. Render the Minions as quick "
        "impressionist dabs. "
        "Palette: cerulean and soft blue sky, emerald and viridian green "
        "grass, yellow Minion bodies, pale ochre on the wooden desks, "
        "lavender shadows on the grass, with a single accent of rust-brown "
        "for Gru's clipboard. Wide horizontal composition. No text or labels "
        "anywhere in the image. Avoid: any water, pond, or river; Gru as a "
        "black silhouette (he should have his pale cartoon skin tone "
        "showing); glowing screens or artificial light; glossy 3D; neon; "
        "sharp digital outlines; AI-art tropes."
    ),
    "image1_hero_clean": (
        "Editorial illustration in the style of Claude Monet's impressionist "
        "paintings — visible broken brushstrokes, dappled light, soft edges, no "
        "hard outlines. Compositionally inspired by Monet's La Grenouillère "
        "(group of figures around water) and his garden-at-Giverny scenes. "
        "A tall narrow figure (silhouette of Gru from Despicable Me — long "
        "black coat, scarf, pointy nose) stands on the left in backlit "
        "silhouette, holding a clipboard, treated as a Monet figure-in-a-"
        "landscape. Below and to the right, sixteen small Minion figures "
        "(yellow ovals, blue overalls, goggles) at little desks with glowing "
        "terminals, rendered as quick impressionist dabs rather than crisp "
        "cartoons — think the figures in Monet's Sunday at Argenteuil. Faint "
        "atmospheric lines connect every Minion to a central warm glow at "
        "the back of the scene — no text labels anywhere in the image, no "
        "writing of any kind. Palette: Monet's typical lavender / mauve / "
        "soft blue / olive green / pale ochre / pearly cream, with a single "
        "accent of rust-brown for Gru's clipboard and the central glow. "
        "Cream paper background. Wide horizontal composition. Avoid: glossy "
        "3D, neon, sharp digital outlines, AI-art tropes, any visible text "
        "or labels in the image."
    ),
    "image1_hero_monet_v2": (
        "Editorial illustration in the style of Claude Monet's outdoor "
        "impressionist paintings — visible broken brushstrokes, dappled "
        "light, soft edges, no hard outlines, the wind almost visible in the "
        "brushwork. Compositionally and chromatically inspired by Monet's "
        "'Woman with a Parasol — Madame Monet and Her Son' (1875): a "
        "wind-swept outdoor scene with a low horizon, a vast cerulean and "
        "cobalt blue sky filled with broken white clouds, and a sweeping "
        "field of emerald and viridian green grass dotted with wildflowers "
        "and white highlights. A tall narrow figure (silhouette of Gru from "
        "Despicable Me — long black coat, scarf, pointy nose) stands on a "
        "small grassy rise on the left in backlit silhouette, holding a "
        "clipboard, treated as a Monet figure-in-a-landscape. Lower and to "
        "the right, scattered across the green field, sixteen small Minion "
        "figures (yellow ovals, blue overalls, goggles) sit at little desks "
        "with softly glowing terminals, rendered as quick impressionist dabs "
        "rather than crisp cartoons. Faint atmospheric lines connect every "
        "Minion to a central warm glow further back in the field — no text "
        "labels anywhere in the image. Palette: cerulean and cobalt blue "
        "sky, emerald and viridian green grass, white highlights, soft "
        "yellows, with a single accent of rust-brown for Gru's clipboard "
        "and the central glow. Wide horizontal composition. Avoid: glossy "
        "3D, neon, sharp digital outlines, AI-art tropes, indoor or abstract "
        "settings, any visible text labels in the image."
    ),
    "image1_hero_renaissance": (
        "Editorial illustration in the style of Italian High Renaissance "
        "painting (Raphael, Botticelli, Leonardo) — soft sfumato edges, "
        "balanced classical composition, idealized figures, warm chiaroscuro "
        "lighting, gold-leaf undertones. Setting: an open Renaissance "
        "courtyard with classical columns and a pastoral Tuscan landscape "
        "stretching behind toward distant blue hills. On the left, a tall "
        "narrow figure — silhouette of Gru from Despicable Me, his long "
        "pointed-nose profile preserved, reimagined as a Renaissance patron "
        "in flowing dark velvet robes with a stiff collar, holding a "
        "parchment scroll instead of a clipboard, painted with the gravitas "
        "of a Botticelli noble. Below and to the right, sixteen small Minion "
        "figures (yellow ovals, blue overalls, goggles) sit at low wooden "
        "writing desks with parchment, ink, and candlelight, rendered at "
        "Renaissance scale (small figures, in deference to the patron) but "
        "preserving their cartoon body shapes — treated like classical putti "
        "rather than crisp animation. A central warm glow connects to all "
        "the Minions through faint painterly light beams — no visible text "
        "labels. Palette: deep umber, sienna, terracotta, ochre, deep "
        "crimson, lapis blue, warm gold leaf, with a single accent of "
        "rust-brown for the patron's scroll. Cream parchment background. "
        "Wide horizontal composition with classical perspective. Avoid: "
        "anachronistic modern elements, glossy 3D, neon, AI-art tropes, "
        "visible text — should feel like a panel from a 16th-century "
        "altarpiece or fresco."
    ),
}


def generate(name: str, model: str) -> Path:
    if name not in PROMPTS:
        raise SystemExit(f"Unknown prompt name: {name}. Options: {list(PROMPTS)}")

    api_key = load_api_key()
    prompt = PROMPTS[name]

    # FLUX models emit image-only; Gemini emits image+text. Pick by family.
    if model.startswith("google/"):
        modalities = ["image", "text"]
    else:
        modalities = ["image"]

    body = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "modalities": modalities,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://thrive.club",
            "X-Title": "Thrive blog image gen",
        },
        method="POST",
    )

    print(f"POST openrouter.ai  model={model}  prompt={name}")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"HTTP {e.code} — {err_body}", file=sys.stderr)
        raise SystemExit(2)

    # Response shape: choices[0].message either has .images (list of
    # {type:image_url,image_url:{url:data:image/png;base64,...}}) or content
    # carrying the same. Walk both, take first base64 PNG we find.
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    def _save_data_url(data_url: str) -> Path:
        m = re.match(r"data:image/(\w+);base64,(.+)", data_url, re.DOTALL)
        if not m:
            raise SystemExit(f"Unrecognized data URL: {data_url[:80]}...")
        ext, b64 = m.group(1), m.group(2)
        out = OUT_DIR / f"{name}.{ext}"
        out.write_bytes(base64.b64decode(b64))
        return out

    try:
        choice = payload["choices"][0]["message"]
    except (KeyError, IndexError):
        print("Unexpected response shape:")
        print(json.dumps(payload, indent=2)[:2000])
        raise SystemExit(3)

    gen_id = payload.get("id")
    usage = payload.get("usage") or {}
    if usage:
        in_tok = usage.get("prompt_tokens", "?")
        out_tok = usage.get("completion_tokens", "?")
        print(f"usage: in={in_tok}  out={out_tok}  total={usage.get('total_tokens','?')}")
    if gen_id:
        # Ask OpenRouter for the actual cost of this generation
        try:
            cost_req = urllib.request.Request(
                f"https://openrouter.ai/api/v1/generation?id={gen_id}",
                headers={"Authorization": f"Bearer {api_key}"},
            )
            with urllib.request.urlopen(cost_req, timeout=30) as cr:
                cost_data = json.loads(cr.read()).get("data") or {}
                if "total_cost" in cost_data:
                    print(f"cost: ${cost_data['total_cost']:.5f}  (id={gen_id})")
        except Exception as e:
            print(f"(cost lookup failed: {e})")

    images = choice.get("images") or []
    for img in images:
        url = img.get("image_url", {}).get("url") or img.get("url")
        if url and url.startswith("data:image/"):
            out = _save_data_url(url)
            print(f"saved: {out}  ({out.stat().st_size:,} bytes)")
            return out

    content = choice.get("content")
    if isinstance(content, list):
        for part in content:
            if isinstance(part, dict) and part.get("type") == "image_url":
                url = part.get("image_url", {}).get("url", "")
                if url.startswith("data:image/"):
                    out = _save_data_url(url)
                    print(f"saved: {out}  ({out.stat().st_size:,} bytes)")
                    return out
    if isinstance(content, str) and content.startswith("data:image/"):
        out = _save_data_url(content)
        print(f"saved: {out}  ({out.stat().st_size:,} bytes)")
        return out

    print("No image in response. Raw payload:")
    print(json.dumps(payload, indent=2)[:3000])
    raise SystemExit(4)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        raise SystemExit(1)
    generate(sys.argv[1], sys.argv[2])
