// 4,160 weeks (52 × 80) laid out as a field that recedes from the viewer:
// the weeks you lived are near and lit, the ones ahead stretch into the distance.
import {
  BoxGeometry,
  Color,
  InstancedBufferAttribute,
  InstancedMesh,
  Matrix4,
  PerspectiveCamera,
  Scene,
  ShaderMaterial,
  Vector3,
  WebGLRenderer,
} from "three";

const COLS = 52;
const ROWS = 80;
const GAP = 1.0;

const vertex = /* glsl */ `
  uniform float uTime;
  uniform float uLived;
  uniform float uRise;
  attribute vec2 aCell;
  varying float vState;
  varying vec3 vNormal;
  varying float vDepth;
  varying float vCurrent;

  void main() {
    float idx = aCell.y * 52.0 + aCell.x;
    float lived = 1.0 - step(uLived, idx);
    float current = 1.0 - step(0.5, abs(idx - floor(uLived)));
    vState = lived;
    vCurrent = current;

    // Assemble wave: rows rise from below one after another, the near rows first.
    float delay = aCell.y / 80.0 * 0.7 + aCell.x / 52.0 * 0.12;
    float r = clamp((uRise - delay) / 0.3, 0.0, 1.0);
    r = 1.0 - pow(1.0 - r, 3.0);

    vec3 p = position;
    p.y *= mix(0.35, 1.0 + lived * 0.6, r) + current * 2.2;
    p *= mix(0.2, 1.0, r);
    vec3 offset = vec3(0.0);
    offset.y = (1.0 - r) * -6.0 + sin(uTime * 1.1 + aCell.y * 0.22 + aCell.x * 0.1) * 0.07 * r;
    offset.y += current * (0.55 + sin(uTime * 3.0) * 0.18);

    vec4 world = modelMatrix * instanceMatrix * vec4(p, 1.0);
    world.xyz += offset;
    vec4 mv = viewMatrix * world;
    vDepth = -mv.z;
    vNormal = normalize(mat3(modelMatrix) * normal);
    gl_Position = projectionMatrix * mv;
  }
`;

const fragment = /* glsl */ `
  uniform vec3 uField;
  uniform vec3 uLivedColor;
  uniform vec3 uAheadColor;
  uniform vec3 uCurrentColor;
  uniform float uFogNear;
  uniform float uFogFar;
  varying float vState;
  varying vec3 vNormal;
  varying float vDepth;
  varying float vCurrent;

  void main() {
    vec3 light = normalize(vec3(-0.4, 1.0, 0.55));
    float diff = max(dot(vNormal, light), 0.0);
    float top = step(0.5, vNormal.y);
    vec3 base = mix(uAheadColor, uLivedColor, vState);
    base = mix(base, uCurrentColor, vCurrent);
    vec3 col = base * (0.42 + 0.7 * diff) + top * vState * 0.08;
    float fog = smoothstep(uFogNear, uFogFar, vDepth);
    col = mix(col, uField, fog * 0.9);
    gl_FragColor = vec4(col, 1.0);
  }
`;

export type WeeksGrid = {
  setLived(weeks: number, animate?: boolean): void;
  rise(): void;
  setPointer(x: number, y: number): void;
  setVisible(v: boolean): void;
};

export function createWeeks(canvas: HTMLCanvasElement, opts: { reduced: boolean; lived: number }): WeeksGrid | null {
  let renderer: WebGLRenderer;
  try {
    renderer = new WebGLRenderer({ canvas, antialias: true, powerPreference: "high-performance" });
  } catch {
    return null;
  }
  const field = new Color("#1c1446");
  renderer.setClearColor(field, 1);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.6));

  const scene = new Scene();
  const camera = new PerspectiveCamera(32, 1, 0.5, 200);

  const geometry = new BoxGeometry(0.74, 0.3, 0.74);
  const count = COLS * ROWS;
  const cell = new Float32Array(count * 2);
  const mesh = new InstancedMesh(
    geometry,
    new ShaderMaterial({
      vertexShader: vertex,
      fragmentShader: fragment,
      uniforms: {
        uTime: { value: 0 },
        uLived: { value: opts.lived },
        uRise: { value: opts.reduced ? 2 : 0 },
        uField: { value: field },
        uLivedColor: { value: new Color("#a78bfa") },
        uAheadColor: { value: new Color("#4b3aa6") },
        uCurrentColor: { value: new Color("#fbbf24") },
        uFogNear: { value: 90 },
        uFogFar: { value: 190 },
      },
    }),
    count,
  );
  const m = new Matrix4();
  for (let row = 0; row < ROWS; row++) {
    for (let col = 0; col < COLS; col++) {
      const i = row * COLS + col;
      // Year 0 is nearest the viewer; the rows ahead recede.
      m.makeTranslation((col - (COLS - 1) / 2) * GAP, 0, -row * GAP + 10);
      mesh.setMatrixAt(i, m);
      cell[i * 2] = col;
      cell[i * 2 + 1] = row;
    }
  }
  geometry.setAttribute("aCell", new InstancedBufferAttribute(cell, 2));
  mesh.frustumCulled = false;
  scene.add(mesh);
  const u = (mesh.material as ShaderMaterial).uniforms;

  const look = new Vector3();
  let wide = true;
  function resize() {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    wide = camera.aspect > 1;
    camera.updateProjectionMatrix();
  }
  const ro = new ResizeObserver(resize);
  ro.observe(canvas);
  resize();

  let target = opts.lived;
  let lived = opts.lived;
  let riseTarget = opts.reduced ? 2 : 0;
  let rise = riseTarget;
  let px = 0;
  let py = 0;
  let cx = 0;
  let cy = 0;
  let visible = false;
  let raf = 0;
  let last = performance.now();

  function place() {
    // Wide screens: the field fills the right two thirds, seen from above its near edge.
    if (wide) {
      camera.position.set(-4 + cx * 4, 58 + cy * 3, 50);
      look.set(-16, 0, -24);
      u.uFogNear.value = 92;
      u.uFogFar.value = 190;
    } else {
      camera.position.set(cx * 2, 34 + cy * 2, 70);
      look.set(0, 0, 18);
      u.uFogNear.value = 70;
      u.uFogFar.value = 150;
    }
    camera.lookAt(look);
  }

  function frame(now: number) {
    const dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    lived += (target - lived) * (1 - Math.exp(-dt * 5));
    rise += (riseTarget - rise) * (1 - Math.exp(-dt * 0.9));
    cx += (px - cx) * (1 - Math.exp(-dt * 2.5));
    cy += (py - cy) * (1 - Math.exp(-dt * 2.5));
    u.uTime.value = now / 1000;
    u.uLived.value = lived;
    u.uRise.value = rise;
    place();
    renderer.render(scene, camera);
    if (visible && !opts.reduced) raf = requestAnimationFrame(frame);
  }
  function kick() {
    cancelAnimationFrame(raf);
    last = performance.now();
    raf = requestAnimationFrame(frame);
  }
  canvas.classList.add("ready");
  kick();

  return {
    setLived(weeks, animate = true) {
      target = weeks;
      if (!animate || opts.reduced) lived = weeks;
      if (opts.reduced) kick();
    },
    rise() {
      riseTarget = 2;
      if (opts.reduced) rise = 2;
    },
    setPointer(x, y) {
      px = x;
      py = y;
    },
    setVisible(v) {
      if (v === visible) return;
      visible = v;
      if (v) kick();
      else cancelAnimationFrame(raf);
    },
  };
}
