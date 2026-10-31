"""Rebuild the locally hosted Noto Sans SC subsets after adding text.

Requires fonttools and brotli. Pass the official regular and semibold TTFs:
  python scripts/build_fonts.py regular.ttf semibold.ttf
Sources and license: assets/fonts/README.md
"""
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python scripts/build_fonts.py regular.ttf semibold.ttf")
    characters = set(range(0x20, 0x0250))
    for pattern in ("_data/*.yml", "_includes/**/*.html", "_publications/**/*.md",
                    "_news/*.md", "*.html", "zh/*.html"):
        for path in ROOT.glob(pattern):
            characters.update(map(ord, path.read_text(encoding="utf-8")))
    for weight, source in zip((400, 600), sys.argv[1:]):
        font = TTFont(source)
        options = subset.Options()
        options.desubroutinize = True
        builder = subset.Subsetter(options=options)
        builder.populate(unicodes=characters)
        builder.subset(font)
        font.flavor = "woff2"
        destination = ROOT / f"assets/fonts/noto-sans-sc-{weight}.woff2"
        font.save(destination)
        print(f"{destination.name}: {destination.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
