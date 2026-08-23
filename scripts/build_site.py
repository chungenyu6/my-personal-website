#!/usr/bin/env python3
"""Create the exact static artifact published to GitHub Pages."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
PUBLIC_PATHS = [
    "index.html",
    "404.html",
    "favicon.ico",
    ".nojekyll",
    "robots.txt",
    "sitemap.xml",
    "site.webmanifest",
    "assets",
    "publications",
    "news",
    "research",
    "learn",
]


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()

    for relative in PUBLIC_PATHS:
        source = ROOT / relative
        destination = OUTPUT / relative
        if source.is_dir():
            shutil.copytree(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)

    file_count = sum(1 for item in OUTPUT.rglob("*") if item.is_file())
    print(f"Static artifact built: {file_count} files in {OUTPUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
