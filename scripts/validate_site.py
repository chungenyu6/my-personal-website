#!/usr/bin/env python3
"""Validate the dependency-free static site using Python's standard library."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = sorted(set(ROOT.glob("*.html")) | set(ROOT.glob("**/index.html")))
IGNORED_PARTS = {"my-old-web", "_site", ".git"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []
        self.ids: list[str] = []
        self.images: list[dict[str, str | None]] = []
        self.h1_count = 0
        self.has_title = False
        self.has_lang = False
        self.has_viewport = False
        self._in_title = False
        self._title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html" and values.get("lang"):
            self.has_lang = True
        if tag == "meta" and values.get("name") == "viewport":
            self.has_viewport = True
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self.h1_count += 1
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if tag in {"a", "link", "script", "img", "source"}:
            attribute = "href" if tag in {"a", "link"} else "src"
            if values.get(attribute):
                self.links.append((tag, values[attribute] or ""))
        if tag == "img":
            self.images.append(values)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.has_title = bool("".join(self._title_text).strip())

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_text.append(data)


def is_ignored(path: Path) -> bool:
    return bool(set(path.relative_to(ROOT).parts) & IGNORED_PARTS)


def resolve_local_url(page: Path, url: str) -> Path | None:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or url.startswith(("mailto:", "tel:", "data:")):
        return None
    path_text = unquote(parsed.path)
    if not path_text:
        return page
    if path_text.startswith("/"):
        target = ROOT / path_text.removeprefix("my-personal-website/").lstrip("/")
    else:
        target = page.parent / path_text
    target = target.resolve()
    if target.is_dir():
        target = target / "index.html"
    return target


def validate_page(page: Path) -> list[str]:
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    relative = page.relative_to(ROOT)
    errors: list[str] = []

    if not parser.has_lang:
        errors.append(f"{relative}: missing html lang")
    if not parser.has_title:
        errors.append(f"{relative}: missing non-empty title")
    if not parser.has_viewport:
        errors.append(f"{relative}: missing viewport meta")
    if parser.h1_count != 1:
        errors.append(f"{relative}: expected 1 h1, found {parser.h1_count}")

    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        errors.append(f"{relative}: duplicate ids: {', '.join(duplicates)}")

    for image in parser.images:
        if image.get("alt") is None:
            errors.append(f"{relative}: image missing alt attribute")
        if not image.get("width") or not image.get("height"):
            errors.append(f"{relative}: image missing width/height")

    for tag, url in parser.links:
        if url.startswith("#"):
            target_id = url[1:]
            if target_id and target_id not in parser.ids:
                errors.append(f"{relative}: missing fragment target {url}")
            continue
        target = resolve_local_url(page, url)
        if target is not None and not target.exists():
            errors.append(f"{relative}: broken local {tag} reference {url}")

    return errors


def main() -> int:
    pages = [page for page in HTML_FILES if not is_ignored(page)]
    errors = [error for page in pages for error in validate_page(page)]

    css = (ROOT / "assets/styles.css").read_text(encoding="utf-8")
    for url in re.findall(r'url\(["\']?([^"\')]+)', css):
        if url.startswith("data:"):
            continue
        target = (ROOT / "assets" / url).resolve()
        if not target.exists():
            errors.append(f"assets/styles.css: broken asset reference {url}")

    required = [
        ROOT / ".nojekyll",
        ROOT / "robots.txt",
        ROOT / "sitemap.xml",
        ROOT / "site.webmanifest",
        ROOT / "assets/documents/cv-chung-en-johnny-yu.pdf",
        ROOT / "assets/images/social-card.jpg",
    ]
    for item in required:
        if not item.exists():
            errors.append(f"missing required file: {item.relative_to(ROOT)}")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Site validation passed: {len(pages)} HTML pages checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
