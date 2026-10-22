"""Check the static site with Python's standard library; no install required."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.duplicates = []
        self.links = []
        self.images = []
        self.meta = []
        self.canonical = []
        self.h1 = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.duplicates.append(attrs["id"])
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "img":
            self.images.append(attrs)
        if tag == "meta":
            self.meta.append(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs["href"])
        self.links.extend(attrs[key] for key in ["href", "src"] if attrs.get(key))
        if attrs.get("srcset"):
            self.links.extend(source.strip().split()[0] for source in attrs["srcset"].split(","))


def check():
    pages = {path: Page(path) for path in ROOT.rglob("*.html")}
    errors = []
    for path, page in pages.items():
        name = path.relative_to(ROOT).as_posix()
        if page.h1 != 1:
            errors.append(f"{name}: expected one h1, got {page.h1}")
        if page.duplicates:
            errors.append(f"{name}: duplicate IDs {page.duplicates}")
        if len(page.canonical) != 1:
            errors.append(f"{name}: expected one canonical URL")
        for key, value in [("name", "description"), ("property", "og:image"), ("property", "og:title")]:
            if sum(meta.get(key) == value for meta in page.meta) != 1:
                errors.append(f"{name}: missing or duplicate {value}")
        if page.images:
            if sum(im.get("fetchpriority") == "high" for im in page.images) != 1:
                errors.append(f"{name}: only the first image should have high priority")
            if page.images[0].get("loading") != "eager" or any(im.get("loading") != "lazy" for im in page.images[1:]):
                errors.append(f"{name}: image loading order")
        for image in page.images:
            if not image.get("alt") or not image.get("width") or not image.get("height"):
                errors.append(f"{name}: missing image description or dimensions")
        for value in page.links:
            url = urlsplit(value)
            if url.scheme or url.netloc:
                continue
            decoded = unquote(url.path)
            destination = ROOT / decoded.lstrip("/") if decoded.startswith("/") else path.parent / decoded if decoded else path
            if destination.is_dir():
                destination /= "index.html"
            destination = destination.resolve()
            if not destination.exists():
                errors.append(f"{name}: missing target {value}")
            elif url.fragment and destination in pages and unquote(url.fragment) not in pages[destination].ids:
                errors.append(f"{name}: missing anchor {value}")
        for meta in page.meta:
            if meta.get("property") == "og:image":
                image_path = ROOT / urlsplit(meta["content"]).path.lstrip("/")
                if not image_path.is_file():
                    errors.append(f"{name}: missing sharing image")
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [row.text for row in ET.parse(ROOT / "sitemap.xml").findall("s:url/s:loc", ns)]
    if len(urls) != len(set(urls)):
        errors.append("sitemap: duplicate URLs")
    for url in urls:
        target = ROOT / (urlsplit(url).path.lstrip("/") or "index.html")
        if not target.is_file() or target.name in ["404.html", "paintings.html", "installations.html"]:
            errors.append(f"sitemap: unexpected URL {url}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(json.dumps({"html_pages": len(pages), "local_links_and_anchors": "passed", "page_metadata": "passed", "image_loading": "passed", "sitemap_urls": len(urls)}, ensure_ascii=False))


if __name__ == "__main__":
    check()
