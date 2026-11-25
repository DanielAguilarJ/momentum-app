"""Plantilla compartida del sitio de Momentum (sin dependencias externas)."""
import json
from html import escape

BASE = "https://danielaguilarj.github.io/momentum-app"
PACKAGE = "com.momentummm.app"
GITHUB = "https://github.com/AndreaAguilarJ/InTime"
SITE_NAME = "Momentum"
TODAY = "2026-11-25"

CSS = """
:root{--bg:#fff;--fg:#1b1d2a;--muted:#5b6075;--line:#e4e6f0;--accent:#4f46e5;--accent-fg:#fff;--card:#f6f7fc}
@media (prefers-color-scheme:dark){:root{--bg:#10111a;--fg:#ecedf6;--muted:#a3a7bd;--line:#262838;--accent:#818cf8;--accent-fg:#10111a;--card:#181a28}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.top{border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;gap:16px;min-height:60px;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--fg);text-decoration:none}
.brand img{width:32px;height:32px;border-radius:8px}
nav{margin-left:auto;display:flex;gap:16px;font-size:15px;flex-wrap:wrap}
nav a{color:var(--muted);text-decoration:none}
nav a:hover{color:var(--accent)}
h1{font-size:2.1rem;line-height:1.2;margin:36px 0 12px;letter-spacing:-.01em}
h2{font-size:1.45rem;line-height:1.3;margin:40px 0 8px}
h3{font-size:1.1rem;margin:24px 0 4px}
p,ul,ol{margin:0 0 16px}
li{margin-bottom:6px}
.lead{font-size:1.15rem;color:var(--muted)}
.cta{display:inline-block;background:var(--accent);color:var(--accent-fg);padding:13px 22px;border-radius:12px;font-weight:700;text-decoration:none;margin:6px 0}
.cta:hover{opacity:.9}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:20px 0}
.card p:last-child{margin-bottom:0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin:18px 0}
.grid .card{margin:0}
.grid h3{margin-top:0}
.meta{color:var(--muted);font-size:14px;margin-bottom:20px}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:15px}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:var(--card)}
details{border-bottom:1px solid var(--line);padding:12px 0}
summary{cursor:pointer;font-weight:600}
details p{margin:8px 0 0}
.weeks{display:grid;grid-template-columns:repeat(52,1fr);gap:2px;margin:18px 0}
.weeks i{aspect-ratio:1;background:var(--accent);border-radius:1px}
.weeks i.f{background:var(--line)}
footer{border-top:1px solid var(--line);margin-top:56px;padding:28px 0 48px;color:var(--muted);font-size:14px}
footer a{color:var(--muted)}
"""


def play_url(content, lang="es_419"):
    """Enlace a Google Play con referrer, para medir qué página trae instalaciones."""
    ref = f"utm_source%3Dmomentum-web%26utm_medium%3Dweb%26utm_content%3D{content}"
    return (f"https://play.google.com/store/apps/details?id={PACKAGE}"
            f"&hl={lang}&referrer={ref}")


def jsonld(data):
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


NAV = {
    "es": [("/bloquear-reels-shorts-android/", "Bloquear Reels y Shorts"),
           ("/reducir-tiempo-de-pantalla-android/", "Tiempo de pantalla"),
           ("/vida-en-semanas/", "Vida en semanas"),
           ("/launcher-minimalista-android/", "Launcher minimalista")],
    "en": [("/en/block-reels-shorts-android/", "Block Reels & Shorts"),
           ("/en/reduce-screen-time-android/", "Screen time"),
           ("/en/life-in-weeks-app/", "Life in weeks")],
}
LANG_TXT = {"es": ("es", "es_419", "English", "Android: Momentum", "Descargar gratis en Google Play"),
            "en": ("en", "en", "Español", "Android: Momentum", "Get it free on Google Play")}


def page(p):
    """p: dict con lang, path, title, description, h1, body, alt (ruta del otro idioma), schema (lista)."""
    lang = p["lang"]
    url = BASE + p["path"]
    alt_lang = "en" if lang == "es" else "es"
    alt_url = BASE + p["alt"] if p.get("alt") else None
    nav = "".join(f'<a href="{BASE}{h}">{escape(t)}</a>' for h, t in NAV[lang])
    other = (f'<a href="{alt_url}" hreflang="{alt_lang}" lang="{alt_lang}">{LANG_TXT[alt_lang][2]}</a>'
             if alt_url else "")
    home = "/" if lang == "es" else "/en/"
    hreflangs = ""
    if alt_url:
        es_url, en_url = (url, alt_url) if lang == "es" else (alt_url, url)
        hreflangs = (f'<link rel="alternate" hreflang="es" href="{es_url}">'
                     f'<link rel="alternate" hreflang="en" href="{en_url}">'
                     f'<link rel="alternate" hreflang="x-default" href="{es_url}">')
    og_img = BASE + "/assets/og.png"
    schema = "".join(jsonld(s) for s in p.get("schema", []))
    foot_note = {
        "es": "Momentum no está afiliado a Instagram, YouTube, TikTok ni a ninguna otra app que permite bloquear. "
              "Las marcas pertenecen a sus dueños.",
        "en": "Momentum is not affiliated with Instagram, YouTube, TikTok or any other app it lets you block. "
              "Trademarks belong to their owners."}[lang]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(p['title'])}</title>
<meta name="description" content="{escape(p['description'])}">
<link rel="canonical" href="{url}">
{hreflangs}
<meta name="theme-color" content="#4f46e5">
<link rel="icon" href="{BASE}/assets/icon.png" type="image/png">
<meta property="og:type" content="{'website' if p.get('home') else 'article'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{escape(p['title'])}">
<meta property="og:description" content="{escape(p['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">
<meta property="og:locale" content="{'es_419' if lang == 'es' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>
{schema}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{BASE}{home}"><img src="{BASE}/assets/icon.png" alt="" width="32" height="32">{SITE_NAME}</a>
<nav>{nav}{other}</nav>
</div></header>
<main class="wrap">
{p['body']}
</main>
<footer><div class="wrap">
<p>{foot_note}</p>
<p><a href="{GITHUB}">GitHub</a></p>
</div></footer>
</body>
</html>
"""


def article_schema(p, published=TODAY):
    url = BASE + p["path"]
    return [{
        "@context": "https://schema.org", "@type": "Article",
        "headline": p["h1"], "description": p["description"],
        "inLanguage": p["lang"], "mainEntityOfPage": url,
        "datePublished": published, "dateModified": TODAY,
        "image": BASE + "/assets/og.png",
        "author": {"@type": "Organization", "name": SITE_NAME, "url": BASE + "/"},
        "publisher": {"@type": "Organization", "name": SITE_NAME,
                      "logo": {"@type": "ImageObject", "url": BASE + "/assets/icon.png"}},
    }]
