// The endless feed as a 3D river of short-video cards spiralling up past the phone.
// Scroll drives it: the flow brakes with mass (VU ballistics), drains of colour, then the cards fall away.
import {
  Color,
  InstancedBufferAttribute,
  InstancedMesh,
  Matrix4,
  PerspectiveCamera,
  PlaneGeometry,
  Scene,
  ShaderMaterial,
  Vector2,
  WebGLRenderer,
} from "three";

const PALETTE = [
  ["#fb7185", "#f59e0b"],
  ["#38bdf8", "#6366f1"],
  ["#34d399", "#0ea5e9"],
  ["#a78bfa", "#fb7185"],
  ["#fbbf24", "#f43f5e"],
  ["#818cf8", "#22d3ee"],
];

const vertex = /* glsl */ `
  uniform float uFlow;
  uniform float uFall;
  uniform float uTime;
  uniform vec2 uCenter;
  uniform float uSpread;
  attribute float aOffset;
  attribute float aAngle;
  attribute float aRadius;
  attribute float aSeed;
  attribute vec3 aColorA;
  attribute vec3 aColorB;
  varying vec2 vUv;
  varying vec3 vA;
  varying vec3 vB;
  varying float vSeed;
  varying float vFade;

  mat3 rotY(float a) { float c = cos(a), s = sin(a); return mat3(c, 0., -s, 0., 1., 0., s, 0., c); }
  mat3 rotZ(float a) { float c = cos(a), s = sin(a); return mat3(c, s, 0., -s, c, 0., 0., 0., 1.); }
  mat3 rotX(float a) { float c = cos(a), s = sin(a); return mat3(1., 0., 0., 0., c, s, 0., -s, c); }

  void main() {
    vUv = uv;
    vA = aColorA;
    vB = aColorB;
    vSeed = aSeed;

    float t = fract(aOffset + uFlow * (0.75 + aSeed * 0.5));
    float y = mix(-7.5, 7.5, t);
    float ang = aAngle + t * 4.4;
    float r = aRadius * uSpread;
    vec3 c = vec3(uCenter.x + cos(ang) * r, y + uCenter.y, sin(ang) * r - 1.5);

    // Falling: each card drops and tumbles on its own curve.
    float f = clamp(uFall * (1.1 + aSeed * 0.9) - aSeed * 0.25, 0.0, 1.0);
    float ff = f * f;
    c.y -= ff * 16.0;
    c.x += (aSeed - 0.5) * ff * 6.0;
    c.z += ff * 3.0 * (aSeed - 0.3);

    vec3 p = position;
    p = rotZ(sin(uTime * 0.5 + aSeed * 6.28) * 0.12 + ff * (aSeed - 0.5) * 5.0) * p;
    p = rotX(ff * 2.0 * (aSeed + 0.2)) * p;
    p = rotY(-ang * 0.35 + 0.4) * p;

    vec4 mv = modelViewMatrix * vec4(c + p, 1.0);
    // Fog toward the night: far cards and the top/bottom of the column dissolve.
    float depth = -mv.z;
    vFade = smoothstep(26.0, 9.0, depth) * smoothstep(0.0, 0.12, t) * smoothstep(1.0, 0.82, t) * (1.0 - smoothstep(0.55, 1.0, f));
    gl_Position = projectionMatrix * mv;
  }
`;

const fragment = /* glsl */ `
  uniform float uTime;
  uniform float uDesat;
  uniform vec3 uNight;
  varying vec2 vUv;
  varying vec3 vA;
  varying vec3 vB;
  varying float vSeed;
  varying float vFade;

  float rbox(vec2 p, vec2 b, float r) {
    vec2 q = abs(p) - b + r;
    return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
  }

  void main() {
    vec2 uv = vUv;
    vec2 p = (uv - 0.5) * vec2(0.5625, 1.0);
    float d = rbox(p, vec2(0.2812, 0.5), 0.045);
    float mask = 1.0 - smoothstep(-0.004, 0.002, d);
    if (mask < 0.01) discard;

    float tt = uTime * 0.35 + vSeed * 20.0;
    vec2 b1 = vec2(0.30 + 0.18 * sin(tt), 0.62 + 0.14 * cos(tt * 0.8));
    vec2 b2 = vec2(0.70 + 0.16 * cos(tt * 0.7), 0.36 + 0.16 * sin(tt * 1.1));
    float g1 = exp(-pow(length((uv - b1) * vec2(1.0, 0.62)) * 3.0, 2.0));
    float g2 = exp(-pow(length((uv - b2) * vec2(1.0, 0.62)) * 2.6, 2.0));
    vec3 base = mix(uNight, vA * 0.22, 0.75);
    vec3 col = base + vA * g1 * 0.95 + vB * g2 * 0.85;

    // Short-video furniture: shade at top and bottom, progress line, action rail, caption bars.
    col *= mix(0.55, 1.0, smoothstep(0.0, 0.28, uv.y)) * mix(0.7, 1.0, smoothstep(1.0, 0.82, uv.y));
    float prog = fract(uTime * 0.18 + vSeed);
    float line = step(abs(uv.y - 0.075), 0.006);
    col = mix(col, mix(vec3(0.35), vec3(1.0), step(uv.x, prog)), line * 0.9);
    for (int i = 0; i < 3; i++) {
      float dot = 1.0 - smoothstep(0.018, 0.026, length((uv - vec2(0.87, 0.30 + float(i) * 0.08)) * vec2(0.5625, 1.0)));
      col = mix(col, vec3(0.95), dot * 0.85);
    }
    float bar1 = step(abs(uv.y - 0.17), 0.011) * step(0.09, uv.x) * step(uv.x, 0.55);
    float bar2 = step(abs(uv.y - 0.13), 0.009) * step(0.09, uv.x) * step(uv.x, 0.38);
    col = mix(col, vec3(0.92), bar1 * 0.75 + bar2 * 0.45);

    // Edge light, so each card reads as a lit screen in the dark.
    float rim = smoothstep(-0.02, 0.0, d);
    col += rim * 0.10;

    float lum = dot(col, vec3(0.299, 0.587, 0.114));
    col = mix(col, vec3(lum) * vec3(0.78, 0.8, 0.95), uDesat);
    col = mix(uNight, col, vFade);
    gl_FragColor = vec4(col, mask);
  }
`;

export type River = {
  setScroll(p: number): void;
  setPointer(x: number, y: number): void;
  setVisible(v: boolean): void;
  destroy(): void;
};

export function createRiver(canvas: HTMLCanvasElement, opts: { reduced: boolean }): River | null {
  let renderer: WebGLRenderer;
  try {
    renderer = new WebGLRenderer({ canvas, antialias: true, alpha: false, powerPreference: "high-performance" });
  } catch {
    return null;
  }
  const night = new Color("#07060f");
  renderer.setClearColor(night, 1);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75));

  const scene = new Scene();
  const camera = new PerspectiveCamera(36, 1, 0.1, 80);
  camera.position.set(0, 0, 15);

  const small = window.matchMedia("(max-width: 860px)").matches;
  const count = small ? 56 : 110;
  const geometry = new PlaneGeometry(0.9, 1.6);
  const offset = new Float32Array(count);
  const angle = new Float32Array(count);
  const radius = new Float32Array(count);
  const seed = new Float32Array(count);
  const colA = new Float32Array(count * 3);
  const colB = new Float32Array(count * 3);
  const c = new Color();
  for (let i = 0; i < count; i++) {
    offset[i] = i / count + Math.random() * 0.02;
    angle[i] = Math.random() * Math.PI * 2;
    radius[i] = 1.9 + Math.random() * 2.7;
    seed[i] = Math.random();
    const [a, b] = PALETTE[i % PALETTE.length];
    c.set(a).toArray(colA, i * 3);
    c.set(b).toArray(colB, i * 3);
  }
  geometry.setAttribute("aOffset", new InstancedBufferAttribute(offset, 1));
  geometry.setAttribute("aAngle", new InstancedBufferAttribute(angle, 1));
  geometry.setAttribute("aRadius", new InstancedBufferAttribute(radius, 1));
  geometry.setAttribute("aSeed", new InstancedBufferAttribute(seed, 1));
  geometry.setAttribute("aColorA", new InstancedBufferAttribute(colA, 3));
  geometry.setAttribute("aColorB", new InstancedBufferAttribute(colB, 3));

  const uniforms = {
    uFlow: { value: 0 },
    uFall: { value: 0 },
    uTime: { value: 0 },
    uDesat: { value: 0 },
    uSpread: { value: 1 },
    uCenter: { value: new Vector2() },
    uNight: { value: night },
  };
  const material = new ShaderMaterial({ vertexShader: vertex, fragmentShader: fragment, uniforms, transparent: true });
  const mesh = new InstancedMesh(geometry, material, count);
  const identity = new Matrix4();
  for (let i = 0; i < count; i++) mesh.setMatrixAt(i, identity);
  mesh.frustumCulled = false;
  scene.add(mesh);

  let width = 0;
  let height = 0;
  function resize() {
    width = canvas.clientWidth;
    height = canvas.clientHeight;
    if (!width || !height) return;
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    const halfH = Math.tan((camera.fov * Math.PI) / 360) * camera.position.z;
    const halfW = halfH * camera.aspect;
    const narrow = camera.aspect < 0.9;
    // The column stands behind the phone: right third on desktop, lower centre on phones.
    if (narrow) uniforms.uCenter.value.set(0, -halfH * 0.25);
    else uniforms.uCenter.value.set(halfW * 0.5, 0);
    uniforms.uSpread.value = narrow ? 0.62 : 1;
  }
  const ro = new ResizeObserver(resize);
  ro.observe(canvas);
  resize();

  let scroll = 0;
  let speed = 1;
  let flow = Math.random();
  let fall = 0;
  let desat = 0;
  let px = 0;
  let py = 0;
  let cx = 0;
  let cy = 0;
  let visible = true;
  let raf = 0;
  let last = performance.now();

  function frame(now: number) {
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    // Targets from the scroll story: hero 0–0.16 flows, detect slows, block stops and drains, inbox falls.
    const targetSpeed = scroll < 0.16 ? 1 : scroll < 0.42 ? 0.35 : 0;
    const targetDesat = scroll < 0.42 ? 0 : 0.9;
    const targetFall = scroll < 0.68 ? 0 : Math.min((scroll - 0.68) / 0.24, 1);
    // Mass and damping: the feed brakes like a needle, not a switch.
    speed += (targetSpeed - speed) * (1 - Math.exp(-dt * 1.6));
    desat += (targetDesat - desat) * (1 - Math.exp(-dt * 2.2));
    fall += (targetFall - fall) * (1 - Math.exp(-dt * 2.6));
    flow += speed * dt * 0.028;
    cx += (px - cx) * (1 - Math.exp(-dt * 3));
    cy += (py - cy) * (1 - Math.exp(-dt * 3));
    camera.position.x = cx * 0.9;
    camera.position.y = cy * 0.6;
    camera.lookAt(cx * 0.3, cy * 0.2, 0);

    uniforms.uTime.value = now / 1000;
    uniforms.uFlow.value = flow;
    uniforms.uDesat.value = desat;
    uniforms.uFall.value = fall;
    renderer.render(scene, camera);
    if (visible && !opts.reduced) raf = requestAnimationFrame(frame);
  }

  function start() {
    cancelAnimationFrame(raf);
    last = performance.now();
    raf = requestAnimationFrame(frame);
  }
  start();
  canvas.classList.add("ready");

  return {
    setScroll(p) {
      scroll = p;
      if (opts.reduced) {
        speed = 0;
        desat = p < 0.42 ? 0 : 0.9;
        fall = p < 0.68 ? 0 : 1;
        start();
      }
    },
    setPointer(x, y) {
      px = x;
      py = y;
    },
    setVisible(v) {
      if (v === visible) return;
      visible = v;
      if (v) start();
      else cancelAnimationFrame(raf);
    },
    destroy() {
      cancelAnimationFrame(raf);
      ro.disconnect();
      geometry.dispose();
      material.dispose();
      renderer.dispose();
    },
  };
}
