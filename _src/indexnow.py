"""Avisa a los buscadores que usan IndexNow (Bing, Yandex, etc.) de las URLs del sitemap.
Uso: python3 -s _src/indexnow.py"""
import json
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://danielaguilarj.github.io/momentum-app"
key = next(f[:-4] for f in os.listdir(ROOT) if re.fullmatch(r"[0-9a-f]{32}\.txt", f))
urls = re.findall(r"<loc>([^<]+)</loc>", open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read())
body = json.dumps({"host": "danielaguilarj.github.io", "key": key,
                   "keyLocation": f"{BASE}/{key}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                             headers={"Content-Type": "application/json; charset=utf-8"})
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        print("IndexNow:", r.status, "con", len(urls), "URLs")
except urllib.error.HTTPError as e:
    print("IndexNow error", e.code, e.read()[:200])
