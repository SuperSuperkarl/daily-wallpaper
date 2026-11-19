"""Create an iPhone lock-screen PNG using the OpenAI Images API.

The OpenAI API is billed separately from a ChatGPT subscription.
This script writes only to OUTPUT_PATH and never prints the API key.
"""
from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def main() -> int:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        print("OPENAI_API_KEY is not configured; keeping the existing wallpaper.")
        return 0

    output = Path(os.environ.get("OUTPUT_PATH", "public/lockscreen.png"))
    model = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2.5-flare")
    now = datetime.now(ZoneInfo("Europe/Berlin"))
    day = now.strftime("%A, %d %B %Y")
    prompt = (
        "Create a new, uniquely composed, beautiful premium iPhone LOCK SCREEN "
        "wallpaper in portrait format. Calm, elegant, artistic, cinematic lighting; "
        "a surprising natural or abstract motif, richly detailed yet uncluttered. "
        "Use tasteful colors, harmonious composition, gentle light and texture. "
        "Leave the top 30 percent dark and uncluttered for the iPhone clock and widgets. "
        "Absolutely no text, letters, numbers, logos, UI or watermarks. "
        f"This is the daily artwork for {day} in Berlin. "
        "Never replicate yesterday's composition. "
    )
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "n": 1,
        "size": "1024x1536",
        "quality": "medium",
        "output_format": "png",
        "background": "opaque"
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=240) as response:
            result = json.load(response)
        encoded = result["data"][0]["b64_json"]
        image = base64.b64decode(encoded, validate=True)
        if not image.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError("Image generation did not return a PNG")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(image)
        print(f"Wrote new wallpaper to {output} ({len(image)} bytes)")
        return 0
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1000]
        print(f"OpenAI API HTTP {exc.code}: {detail}", file=sys.stderr)
    except Exception as exc:
        print(f"Image generation failed: {type(exc).__name__}: {exc}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
