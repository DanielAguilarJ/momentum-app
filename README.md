# Momentum: sitio web

Sitio de la app **Momentum** (bloqueador de apps, Reels y Shorts para Android).

- Sitio: https://danielaguilarj.github.io/momentum-app/
- App en Google Play: https://play.google.com/store/apps/details?id=com.momentummm.app

No edites los `index.html` a mano. Para regenerar todo:

```sh
python3 -s _src/build.py          # guías, sitemap, robots y _web/src/data/guides.json
cd _web && npm ci && npm run build  # portadas / y /en/ (Astro + Three.js) y _astro/
```

- `_src/`: guías y sitemap (Python, sin dependencias).
- `_web/`: portada con Astro, Three.js, GSAP y Lenis. `npm run build` compila y copia `index.html`, `en/index.html` y `_astro/` a la raíz, que es lo que sirve GitHub Pages.
- Comprobaciones: `python3 -s _src/check_links.py` y `python3 -s _src/check_seo.py`.
- `PRODUCT.md` recoge lo que la app hace de verdad; `DESIGN.md`, el sistema visual de la portada.
