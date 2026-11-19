"""Generate a clearly marked demo lock-screen PNG without an OpenAI API key."""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import sys


def font(size: int):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def create(path: Path):
    width, height = 1170, 2532
    im = Image.new("RGB", (width, height))
    pixels = im.load()
    for y in range(height):
        t = y / (height - 1)
        for x in range(width):
            wave = math.sin(x / 210 + y / 510) * 12
            pixels[x, y] = (
                int(17 + 32 * t + wave * 0.15),
                int(30 + 37 * t + wave * 0.25),
                int(57 + 54 * t + wave * 0.45),
            )
    draw = ImageDraw.Draw(im, "RGBA")
    for idx in range(6):
        offset = idx * 86
        draw.ellipse(
            (-280 + offset, 820 + offset, 990 + offset, 2090 + offset),
            outline=(180, 210, 255, 35),
            width=5,
        )
    draw.text((width // 2, 1580), "DAILY WALLPAPER",
              fill=(240, 244, 255, 245), font=font(58), anchor="mm")
    draw.text((width // 2, 1660), "GitHub Pages Testbild",
              fill=(210, 220, 239, 220), font=font(38), anchor="mm")
    draw.text((width // 2, 1735), "Noch kein ChatGPT-generiertes Bild",
              fill=(210, 220, 239, 190), font=font(28), anchor="mm")
    path.parent.mkdir(parents=True, exist_ok=True)
    im.save(path, "PNG", optimize=True)
    print(f"Created demo image: {path} ({im.size})")


if __name__ == "__main__":
    create(Path(sys.argv[1] if len(sys.argv) > 1 else "public/lockscreen.png"))
