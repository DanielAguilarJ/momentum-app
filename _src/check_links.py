"""Comprueba que todos los enlaces internos apuntan a páginas que existen. Uso: python3 -s _src/check_links.py"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from layout import BASE

bad = 0
count = 0
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d != "_src"]
    for f in files:
        if not f.endswith(".html") or f.startswith("google"):
            continue
        src = os.path.join(dirpath, f)
        text = open(src, encoding="utf-8").read()
        for href in re.findall(r'(?:href|src)="(' + re.escape(BASE) + r'[^"#]*)', text):
            count += 1
            rel = href[len(BASE):].lstrip("/")
            target = os.path.join(ROOT, rel)
            if href.endswith("/") or rel == "":
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                bad += 1
                print("ROTO", os.path.relpath(src, ROOT), "->", href)
print(f"{count} enlaces internos revisados, {bad} rotos")
sys.exit(1 if bad else 0)
