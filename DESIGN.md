# Momentum landing · design system

Built world, recorded after the 2026-11-25 build (`_web/`). Surface: the landing pages `/` and `/en/` (Persuade). The guides keep their own reading layout from `_src/layout.py`.

## World

The page travels from a 1 a.m. doomscroll to dawn. Night ground lit only by the phone and a WebGL river of short-video cards; a violet field for the 4,160-week grid; a sunrise over a dark horizon for the close.

## Color

| Token | Value | Role |
|---|---|---|
| `--night` | #07060F | Ground of hero, story, features, trust, guides, FAQ |
| `--night-2` / `--night-3` | #0D0B1D / #16122C | Demo panels |
| `--ink` / `--ink-2` / `--ink-3` | #EEF0FF / #BCBFD9 / #9094B3 | Text tiers on night |
| `--violet-3` | #C4B5FD | Second line of display headings, active state, detection brackets |
| `--violet-2` / `--violet` | #A78BFA / #8B5CF6 | Bars, lived weeks, block mark |
| `--violet-field` | #1C1446 | Weeks section, Momentum column of the comparison |
| `--mint` | #34D399 | "Allowed / time back" (checks, focus ticks, Wi‑Fi rule) |
| `--rose` | #FB7185 | Limit reached |
| `--amber` | #FBBF24 | Current week, streak, sun |

Contrast: body text on night is ≥ 9:1; `--ink-3` captions ≥ 6:1. The primary button is a light pill (`--ink` on `--night` text).

## Type

- Display: Bricolage Grotesque Variable, `font-stretch` 78–84 %, weight 700–750, tracking −0.035 to −0.045 em, max 6 rem.
- Body: Geist Variable, 17 px base, lead 1.1–1.28 rem.
- Mono: Geist Mono Variable, only for time and counts (status bar, minutes, week tallies, step numbers).
- All three are self-hosted through Fontsource; no external font requests.

## Components

- **Phone** (`Phone.astro`): CSS 3D device; screens `feed → detect → block → inbox` switched by `data-state`. Labelled "Pantalla simulada / Simulated screen".
- **Detection brackets**: four violet corners and a tag; the only ornament in the system.
- **Demo panel**: 28 px radius, night-3 → night-2 gradient, 1 px inner line, low violet shadow with offset.
- **Timetable**: 7-day × 24-hour grid with violet (classes) and indigo (sleep) blocks.
- **Buttons**: light pill (primary), text link with arrow (secondary).
- Icons: Lucide, inlined at build, stroke 1.75.

## Motion

- One authored moment: the sticky scroll story (380 vh). Beat 0 hero, 1 detect, 2 block, 3 messages. The river brakes with mass (exponential approach), drains to grey, then the cards fall.
- Weeks grid assembles row by row when the section arrives and re-lights on the age slider.
- Sun rises with scroll in the close.
- Smooth scroll with Lenis. `prefers-reduced-motion` turns off Lenis, the river loop, the timer and the sun; every scene renders one still frame.
- No JS or no WebGL: the story reads as a list; the scenes fall back to a static glow.

## Performance

Three.js (≈530 KB raw) loads only after first paint for the hero and only near the weeks section for the grid. Both scenes pause when off screen. Pixel ratio is capped at 1.75 / 1.6.

## Provenance of rasters

No new raster ships. `assets/icon.png` and `assets/og.png` are the existing app assets. Every card, phone screen and grid is drawn in code (CSS or WebGL shaders), so nothing needs replacing with real material, except that real Android screenshots could later replace the simulated phone.
