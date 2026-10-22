"""Optional editorial helper; the generated HTML works without Python or a build."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import re
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
URL = "https://puwei-lab.github.io/"
ALIASES = {"paintings.html": "works.html", "installations.html": "works.html"}


class HeadInfo(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.in_title = False
        self.title = ""
        self.description = ""
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = attrs.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, text):
        if self.in_title:
            self.title += text


def load(name):
    return json.loads((ROOT / "assets" / name).read_text())


def create_not_found():
    template = (ROOT / "index.html").read_text()
    template = re.sub(r'<a class="brand"[^>]*>.*?</a>', lambda m: m[0].replace("<h1>", "").replace("</h1>", ""), template, count=1)
    main = '''<main id="main" class="shell" tabindex="-1"><section class="page-intro"><p class="eyebrow">PUWEI WU / 404</p><h1>404<span class="zh-title">找不到頁面</span></h1></section><div class="prose"><p>可以回到首頁，或從作品與展覽繼續瀏覽。</p><p lang="en">Return to the homepage, or explore the works and exhibitions.</p></div><div class="error-links"><a href="index.html">返回首頁 Home ↗</a><a href="works.html">作品 Works ↗</a><a href="exhibitions.html">展覽 Exhibitions ↗</a></div></main>'''
    template = re.sub(r"<main\b.*?</main>", lambda _: main, template, count=1, flags=re.S)
    template = re.sub(r"<title>.*?</title>", "<title>找不到頁面 404 — 吳柏葳 PUWEI WU</title>", template, count=1)

    def rooted(match):
        value = match[2]
        if value.startswith(("/", "#")) or urlsplit(value).scheme:
            return match[0]
        return f'{match[1]}="/{value}"'

    template = re.sub(r'(href|src)="([^"]+)"', rooted, template)
    (ROOT / "404.html").write_text(template)


def prepare():
    catalogue = {row["page"]: row for row in load("catalogue.json")}
    series = {row["path"]: row for row in load("series.json")}
    exhibitions = {"exhibitions/" + row["id"] + ".html": row for row in load("exhibitions.json")}
    create_not_found()
    public_urls = []
    counts = {"pages": 0, "images": 0, "priority_images": 0}
    for path in sorted(ROOT.rglob("*.html")):
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text()
        info = HeadInfo(text.split("</head>", 1)[0])
        description = info.description
        cover = "assets/images/hero-representative-002-view.webp"
        if relative in catalogue:
            work = catalogue[relative]
            title = work["title_zh"] + (" / " + work["title_en"] if work["title_en"] else "")
            description = "｜".join(filter(None, [title, work.get("creation_date", work["year"]), work["medium"], work["dimensions"], "吳柏葳 PUWEI WU"]))
            cover = work["cover"] or cover
        elif relative in series:
            group = series[relative]
            description = f'{group["zh"]} {group["en"]}｜吳柏葳 PUWEI WU 的作品系列，瀏覽各件作品圖片、創作年份、媒材與尺寸。'
            cover = "assets/images/" + group["cover"] + "-view.webp"
        elif relative in exhibitions:
            event = exhibitions[relative]
            description = "｜".join([event["zh"], event.get("date", event["year"]), event["venue"], "吳柏葳 PUWEI WU 展覽現場紀錄"])
            cover = "assets/images/" + event["cover"] + "-view.webp"
        elif relative == "index.html":
            description = "吳柏葳 PUWEI WU 的藝術家個人網站，展示作品系列、展覽現場、藝術家簡介與聯絡資訊。"
        elif relative in ["works.html", *ALIASES]:
            description = "依系列瀏覽吳柏葳 PUWEI WU 的作品，包含作品圖片、創作年份、媒材、尺寸與展出紀錄。"
        elif relative == "exhibitions.html":
            description = "吳柏葳 PUWEI WU 的個展與聯展現場紀錄，依年份瀏覽展覽照片及參展作品。"
        elif relative == "about.html":
            description = "吳柏葳 PUWEI WU 的中英文藝術家簡介與創作關注。"
        elif relative == "cv.html":
            description = "吳柏葳 PUWEI WU 的學歷、個展、聯展、駐村、獲獎與提名紀錄。"
        elif relative == "contact.html":
            description = "聯絡藝術家吳柏葳 PUWEI WU：Email winsonwu97@gmail.com，Instagram @puwei_2862。"
        elif relative == "404.html":
            description = "找不到這個頁面。回到吳柏葳 PUWEI WU 的首頁，或瀏覽作品與展覽。"
        description = re.sub(r"\s+", " ", description).strip()
        if len(description) > 175:
            description = description[:174] + "…"
        canonical = URL + ("" if relative == "index.html" else ALIASES.get(relative, relative))
        if relative not in ALIASES and relative != "404.html":
            public_urls.append(canonical)
        prefix = "/" if relative == "404.html" else "../" * (len(path.relative_to(ROOT).parts) - 1)
        title = escape(info.title, quote=True)
        desc = escape(description, quote=True)
        extra = f'''<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="吳柏葳 PUWEI WU">
<meta property="og:locale" content="zh_TW">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{URL + cover}">
<meta property="og:image:alt" content="{title}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{URL + cover}">'''
        if relative in ALIASES or relative == "404.html":
            extra += '\n<meta name="robots" content="noindex,follow">'
        text = re.sub(r'<meta name="description" content="[^"]*">', lambda _: f'<meta name="description" content="{desc}">', text, count=1)
        text = re.sub(r'\s*<!-- site metadata -->.*?<!-- /site metadata -->\s*', "", text, flags=re.S)
        text = text.replace("</head>", "\n<!-- site metadata -->\n" + extra + "\n<!-- /site metadata -->\n</head>", 1)
        text = re.sub(r'<main id="main" class="shell">', '<main id="main" class="shell" tabindex="-1">', text)
        text = re.sub(r'<article class="series-item"(?! tabindex)', '<article class="series-item" tabindex="-1"', text)
        first = True

        def image_loading(match):
            nonlocal first
            tag = re.sub(r'\s+(loading|fetchpriority)="[^"]*"', "", match[0])
            priority = first
            first = False
            counts["images"] += 1
            if priority:
                counts["priority_images"] += 1
            return tag[:-1] + (' loading="eager" fetchpriority="high">' if priority else ' loading="lazy">')

        text = re.sub(r"<img\b[^>]*>", image_loading, text)
        path.write_text(text)
        counts["pages"] += 1
    ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", ns)
    sitemap = ET.Element("{" + ns + "}urlset")
    for url in public_urls:
        entry = ET.SubElement(sitemap, "{" + ns + "}url")
        ET.SubElement(entry, "{" + ns + "}loc").text = url
    ET.indent(sitemap)
    ET.ElementTree(sitemap).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: " + URL + "sitemap.xml\n")
    (ROOT / ".nojekyll").touch()
    print(json.dumps({**counts, "sitemap_urls": len(public_urls)}, ensure_ascii=False))


if __name__ == "__main__":
    prepare()
