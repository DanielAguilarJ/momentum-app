"""Genera las guías, el sitemap y la lista de guías para la portada.
Uso: python3 -s _src/build.py && (cd _web && npm run build)"""
import json
import os
import sys
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import content_en as en
import content_en_b as enb
import content_es_a as esa
import content_es_b as esb
import content_es_c as esc
from layout import BASE, TODAY, page

HUB = {"es": ("/guias/", "Guías de Momentum para usar menos el celular",
              "Guías prácticas para reducir tu tiempo de pantalla en Android: bloquear Reels y Shorts, detox digital, técnica Pomodoro, vida en semanas y más.",
              "Guías para usar menos el celular", "Todas las guías, con pasos que puedes aplicar hoy."),
       "en": ("/en/guides/", "Momentum guides to use your phone less",
              "Practical guides to cut your screen time on Android: block Reels and Shorts, digital detox, Pomodoro technique, life in weeks and more.",
              "Guides to use your phone less", "All the guides, with steps you can apply today.")}
RELATED_TITLE = {"es": "Más guías", "en": "More guides"}

CONTENT = (esa.home(), esa.reels(), esb.screen(), esb.life(), esb.launcher(), *esc.pages(),
           en.home(), en.reels(), en.screen(), en.life(), *enb.pages())


def guides(lang):
    return [p for p in CONTENT if p["lang"] == lang and not p.get("home")]


def link_list(items):
    return "<ul>" + "".join(f'<li><a href="{BASE}{p["path"]}">{escape(p["h1"])}</a></li>' for p in items) + "</ul>"


def finish():
    pages = list(CONTENT)
    for lang in ("es", "en"):
        g = guides(lang)
        for p in pages:
            if p["lang"] != lang:
                continue
            if p.get("home"):
                p["body"] = p["body"].replace("<!--GUIDES-->", link_list(g) + (
                    f'<p><a href="{BASE}{HUB[lang][0]}">{"Ver todas las guías" if lang == "es" else "See all guides"}</a></p>'))
            else:
                i = g.index(p)
                rel = [g[(i + k) % len(g)] for k in (1, 2, 3)]
                p["body"] += f'<h2>{RELATED_TITLE[lang]}</h2>' + link_list(rel)
        path, title, desc, h1, lead = HUB[lang]
        alt = HUB["en" if lang == "es" else "es"][0]
        hub_body = f"<h1>{h1}</h1><p class=\"lead\">{lead}</p>" + "".join(
            f'<div class="card"><h3><a href="{BASE}{p["path"]}">{escape(p["h1"])}</a></h3><p>{escape(p["description"])}</p></div>'
            for p in g)
        pages.append(dict(lang=lang, path=path, alt=alt, title=title, description=desc, h1=h1, body=hub_body, schema=[]))
    return pages


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def write_guides_json():
    """Lista de guías para la portada en Astro (_web), que sustituye a las portadas de Python."""
    data = {lang: [dict(path=p["path"], h1=p["h1"], description=p["description"]) for p in guides(lang)]
            for lang in ("es", "en")}
    write("_web/src/data/guides.json", json.dumps(data, ensure_ascii=False, indent=1) + "\n")


def main():
    PAGES = finish()
    seen = set()
    for p in PAGES:
        assert p["path"] not in seen, p["path"]
        seen.add(p["path"])
        if p.get("home"):
            continue  # las portadas "/" y "/en/" las genera Astro en _web/
        write(p["path"].lstrip("/") + "index.html", page(p))
    write_guides_json()
    paths = {p["path"] for p in PAGES}
    for p in PAGES:
        if p.get("alt"):
            assert p["alt"] in paths, (p["path"], p["alt"])

    urls = []
    for p in PAGES:
        links = ""
        if p.get("alt"):
            es, en_ = (p["path"], p["alt"]) if p["lang"] == "es" else (p["alt"], p["path"])
            links = (f'<xhtml:link rel="alternate" hreflang="es" href="{BASE}{es}"/>'
                     f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}{en_}"/>')
        prio = "1.0" if p.get("home") and p["lang"] == "es" else ("0.9" if p.get("home") else "0.8")
        urls.append(f"<url><loc>{BASE}{p['path']}</loc><lastmod>{TODAY}</lastmod>"
                    f"<priority>{prio}</priority>{links}</url>")
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
          'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write(".nojekyll", "")
    write("404.html", page(dict(
        lang="es", path="/404.html", title="Página no encontrada · Momentum", description="Página no encontrada.",
        h1="No encontramos esa página",
        body=f'<h1>No encontramos esa página</h1><p><a href="{BASE}/">Volver a Momentum</a> · '
             f'<a href="{BASE}/en/">Back to Momentum</a></p>')))
    print(f"{len(PAGES)} páginas generadas")


if __name__ == "__main__":
    main()
