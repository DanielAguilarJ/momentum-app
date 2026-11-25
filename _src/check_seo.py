"""Revisa título, descripción, un solo h1 y JSON-LD válido en cada página. Uso: python3 -s _src/check_seo.py"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
titles = {}
problems = 0
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("_src", "_web")]
    for f in files:
        if f != "index.html":
            continue
        p = os.path.join(dirpath, f)
        t = open(p, encoding="utf-8").read()
        rel = os.path.relpath(p, ROOT)
        title = re.search(r"<title>(.*?)</title>", t).group(1)
        desc = re.search(r'name="description" content="(.*?)"', t).group(1)
        h1 = len(re.findall(r"<h1[\s>]", t))
        msgs = []
        if len(title) > 70:
            msgs.append(f"título largo ({len(title)})")
        if not 70 <= len(desc) <= 175:
            msgs.append(f"descripción de {len(desc)} caracteres")
        if h1 != 1:
            msgs.append(f"{h1} h1")
        if title in titles:
            msgs.append("título repetido con " + titles[title])
        titles[title] = rel
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
            try:
                json.loads(block)
            except ValueError:
                msgs.append("JSON-LD inválido")
        if msgs:
            problems += 1
            print(rel, "->", "; ".join(msgs))
print(f"{len(titles)} páginas revisadas, {problems} con avisos")
