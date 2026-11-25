// Page orchestration: smooth scroll, the scroll story, lazy WebGL scenes, small live demos.
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

gsap.registerPlugin(ScrollTrigger);

const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const finePointer = window.matchMedia("(pointer: fine)").matches;
const $ = <T extends Element = HTMLElement>(s: string, root: ParentNode = document) => root.querySelector<T>(s);

/* Smooth scroll with inertia (off for reduced motion). */
let lenis: Lenis | null = null;
if (!reduced) {
  lenis = new Lenis({ lerp: 0.1, anchors: { offset: -72 }, autoRaf: false });
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((time) => lenis?.raf(time * 1000));
  gsap.ticker.lagSmoothing(0);
}

/* Navigation: solid once the page moves, hidden while scrolling down through the story. */
const nav = $("[data-nav]");
let lastY = 0;
function onScroll() {
  const y = window.scrollY;
  nav?.classList.toggle("solid", y > 24);
  nav?.classList.toggle("hidden", y > 400 && y > lastY + 2);
  if (y < lastY - 2) nav?.classList.remove("hidden");
  lastY = y;
}
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

/* The scroll story. */
const stage = $("[data-stage]");
const phone = $("[data-phone]");
const device = $("[data-device]");
type RiverApi = import("./feed-river").River;
let river: RiverApi | null = null;
let stageProgress = 0;

function beatFor(p: number) {
  return p < 0.16 ? 0 : p < 0.42 ? 1 : p < 0.68 ? 2 : 3;
}
const STATES = ["feed", "detect", "block", "inbox"];

function measureMobile() {
  if (!stage) return;
  const hero = $(".hero-copy", stage);
  const story = $(".story", stage);
  if (!hero || !story) return;
  stage.style.setProperty("--hero-h", `${hero.offsetHeight}px`);
  stage.style.setProperty("--story-h", `${Math.max(...[...story.querySelectorAll<HTMLElement>(".beat")].map((b) => b.offsetHeight))}px`);
}

if (stage && phone) {
  ScrollTrigger.create({
    trigger: stage,
    start: "top top",
    end: "bottom bottom",
    onUpdate(self) {
      stageProgress = self.progress;
      const beat = beatFor(stageProgress);
      if (stage.dataset.beat !== String(beat)) {
        stage.dataset.beat = String(beat);
        phone.dataset.state = STATES[beat];
      }
      river?.setScroll(stageProgress);
    },
  });
  measureMobile();
  window.addEventListener("resize", measureMobile);
  document.fonts?.ready.then(measureMobile);
}

/* Pointer: tilt the phone and drift the cameras. */
let weeks: import("./weeks-grid").WeeksGrid | null = null;
if (finePointer && !reduced) {
  window.addEventListener(
    "pointermove",
    (e) => {
      const x = (e.clientX / window.innerWidth) * 2 - 1;
      const y = (e.clientY / window.innerHeight) * 2 - 1;
      river?.setPointer(x, -y);
      weeks?.setPointer(x, -y);
      if (phone) {
        phone.style.setProperty("--ry", `${-16 + x * 7}deg`);
        phone.style.setProperty("--rx", `${5 - y * 5}deg`);
      }
    },
    { passive: true },
  );
}

function whenVisible(el: Element, onChange: (v: boolean) => void, margin = "0px") {
  const io = new IntersectionObserver((entries) => entries.forEach((e) => onChange(e.isIntersecting)), { rootMargin: margin });
  io.observe(el);
}

function webglOK() {
  try {
    const c = document.createElement("canvas");
    return !!(c.getContext("webgl2") || c.getContext("webgl"));
  } catch {
    return false;
  }
}
const canGL = webglOK();

/* Hero river: loaded after first paint so the headline is never waiting on WebGL. */
const riverCanvas = $<HTMLCanvasElement>("[data-river]");
if (riverCanvas && canGL) {
  const boot = async () => {
    const { createRiver } = await import("./feed-river");
    river = createRiver(riverCanvas, { reduced });
    river?.setScroll(stageProgress);
    if (stage) whenVisible(stage, (v) => river?.setVisible(v));
  };
  "requestIdleCallback" in window ? requestIdleCallback(() => boot(), { timeout: 1200 }) : setTimeout(boot, 300);
}

/* Weeks grid: loaded as the section approaches, assembled when it arrives. */
const weeksSection = $("[data-weeks]");
const weeksCanvas = $<HTMLCanvasElement>("[data-weeks-canvas]");
const ageInput = $<HTMLInputElement>("[data-age]");
const ageOut = $("[data-age-out]");
const livedOut = $("[data-lived]");
const leftOut = $("[data-left]");
const fmt = new Intl.NumberFormat(document.documentElement.lang === "es" ? "es-MX" : "en-US");

function ageWeeks() {
  return Number(ageInput?.value ?? 25) * 52;
}
function paintAge() {
  if (!ageInput) return;
  const age = Number(ageInput.value);
  const w = age * 52;
  if (ageOut) ageOut.textContent = String(age);
  if (livedOut) livedOut.textContent = fmt.format(w);
  if (leftOut) leftOut.textContent = fmt.format(4160 - w);
  const pct = ((age - Number(ageInput.min)) / (Number(ageInput.max) - Number(ageInput.min))) * 100;
  ageInput.style.setProperty("--fill", `${pct}%`);
  weeks?.setLived(w);
}
ageInput?.addEventListener("input", paintAge);
paintAge();

if (weeksSection && weeksCanvas && canGL) {
  let booted = false;
  whenVisible(
    weeksSection,
    async (near) => {
      if (!near || booted) return;
      booted = true;
      const { createWeeks } = await import("./weeks-grid");
      weeks = createWeeks(weeksCanvas, { reduced, lived: ageWeeks() });
      whenVisible(weeksSection, (v) => {
        weeks?.setVisible(v);
        if (v) weeks?.rise();
      }, "-15% 0px");
    },
    "600px",
  );
}

/* Focus demo: a real countdown while it is on screen. */
const focus = $("[data-focus]");
const clock = $("[data-clock]");
const ticks = focus ? [...focus.querySelectorAll<HTMLElement>("[data-ticks] i")] : [];
if (focus && clock) {
  let seconds = 25 * 60;
  let timer = 0;
  const paint = () => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    clock.textContent = `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
    const done = 25 - Math.ceil(seconds / 60);
    ticks.forEach((t, i) => t.classList.toggle("on", i < done));
  };
  whenVisible(focus, (v) => {
    clearInterval(timer);
    if (!v || reduced) return;
    timer = window.setInterval(() => {
      // Sped up for the demo: the 25 minutes pass in about 36 seconds.
      seconds = seconds > 0 ? seconds - 7 : 25 * 60;
      if (seconds < 0) seconds = 0;
      paint();
    }, 1000 / 6);
  });
}

/* Dawn: the sun clears the horizon as the close arrives. */
const dawn = $("[data-dawn]");
const sun = $("[data-sun]");
if (dawn && sun && !reduced) {
  gsap.fromTo(
    sun,
    { "--sun-y": "70%" },
    { "--sun-y": "30%", ease: "none", scrollTrigger: { trigger: dawn, start: "top bottom", end: "bottom bottom", scrub: true } },
  );
} else if (sun) {
  sun.style.setProperty("--sun-y", "30%");
}

/* Keep the phone readable when its section leaves the screen on small devices. */
if (device && !finePointer) device.style.setProperty("--rz", "0deg");
