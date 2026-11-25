import{a as e,c as t,d as n,i as r,l as i,o as a,r as o,s,t as c,u as l}from"./three.module.DdMD1GhI.js";var u=[[`#fb7185`,`#f59e0b`],[`#38bdf8`,`#6366f1`],[`#34d399`,`#0ea5e9`],[`#a78bfa`,`#fb7185`],[`#fbbf24`,`#f43f5e`],[`#818cf8`,`#22d3ee`]],d=`
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
`,f=`
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
`;function p(p,m){let h;try{h=new c({canvas:p,antialias:!0,alpha:!1,powerPreference:`high-performance`})}catch{return null}let g=new o(`#07060f`);h.setClearColor(g,1),h.setPixelRatio(Math.min(window.devicePixelRatio,1.75));let _=new i,v=new s(36,1,.1,80);v.position.set(0,0,15);let y=window.matchMedia(`(max-width: 860px)`).matches?56:110,b=new t(.9,1.6),x=new Float32Array(y),S=new Float32Array(y),C=new Float32Array(y),w=new Float32Array(y),T=new Float32Array(y*3),E=new Float32Array(y*3),D=new o;for(let e=0;e<y;e++){x[e]=e/y+Math.random()*.02,S[e]=Math.random()*Math.PI*2,C[e]=1.9+Math.random()*2.7,w[e]=Math.random();let[t,n]=u[e%u.length];D.set(t).toArray(T,e*3),D.set(n).toArray(E,e*3)}b.setAttribute(`aOffset`,new r(x,1)),b.setAttribute(`aAngle`,new r(S,1)),b.setAttribute(`aRadius`,new r(C,1)),b.setAttribute(`aSeed`,new r(w,1)),b.setAttribute(`aColorA`,new r(T,3)),b.setAttribute(`aColorB`,new r(E,3));let O={uFlow:{value:0},uFall:{value:0},uTime:{value:0},uDesat:{value:0},uSpread:{value:1},uCenter:{value:new n},uNight:{value:g}},k=new l({vertexShader:d,fragmentShader:f,uniforms:O,transparent:!0}),A=new e(b,k,y),j=new a;for(let e=0;e<y;e++)A.setMatrixAt(e,j);A.frustumCulled=!1,_.add(A);let M=0,N=0;function P(){if(M=p.clientWidth,N=p.clientHeight,!M||!N)return;h.setSize(M,N,!1),v.aspect=M/N,v.updateProjectionMatrix();let e=Math.tan(v.fov*Math.PI/360)*v.position.z,t=e*v.aspect,n=v.aspect<.9;n?O.uCenter.value.set(0,-e*.25):O.uCenter.value.set(t*.5,0),O.uSpread.value=n?.62:1}let F=new ResizeObserver(P);F.observe(p),P();let I=0,L=1,R=Math.random(),z=0,B=0,V=0,H=0,U=0,W=0,G=!0,K=0,q=performance.now();function J(e){let t=Math.min((e-q)/1e3,.05);q=e;let n=I<.16?1:I<.42?.35:0,r=I<.42?0:.9,i=I<.68?0:Math.min((I-.68)/.24,1);L+=(n-L)*(1-Math.exp(-t*1.6)),B+=(r-B)*(1-Math.exp(-t*2.2)),z+=(i-z)*(1-Math.exp(-t*2.6)),R+=L*t*.028,U+=(V-U)*(1-Math.exp(-t*3)),W+=(H-W)*(1-Math.exp(-t*3)),v.position.x=U*.9,v.position.y=W*.6,v.lookAt(U*.3,W*.2,0),O.uTime.value=e/1e3,O.uFlow.value=R,O.uDesat.value=B,O.uFall.value=z,h.render(_,v),G&&!m.reduced&&(K=requestAnimationFrame(J))}function Y(){cancelAnimationFrame(K),q=performance.now(),K=requestAnimationFrame(J)}return Y(),p.classList.add(`ready`),{setScroll(e){I=e,m.reduced&&(L=0,B=e<.42?0:.9,z=e<.68?0:1,Y())},setPointer(e,t){V=e,H=t},setVisible(e){e!==G&&(G=e,e?Y():cancelAnimationFrame(K))},destroy(){cancelAnimationFrame(K),F.disconnect(),b.dispose(),k.dispose(),h.dispose()}}}export{p as createRiver};