import{a as e,f as t,i as n,l as r,n as i,o as a,r as o,s,t as c,u as l}from"./three.module.DdMD1GhI.js";var u=52,d=80,f=1,p=`
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
`,m=`
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
`;function h(h,g){let _;try{_=new c({canvas:h,antialias:!0,powerPreference:`high-performance`})}catch{return null}let v=new o(`#1c1446`);_.setClearColor(v,1),_.setPixelRatio(Math.min(window.devicePixelRatio,1.6));let y=new r,b=new s(32,1,.5,200),x=new i(.74,.3,.74),S=4160,C=new Float32Array(S*2),w=new e(x,new l({vertexShader:p,fragmentShader:m,uniforms:{uTime:{value:0},uLived:{value:g.lived},uRise:{value:g.reduced?2:0},uField:{value:v},uLivedColor:{value:new o(`#a78bfa`)},uAheadColor:{value:new o(`#4b3aa6`)},uCurrentColor:{value:new o(`#fbbf24`)},uFogNear:{value:90},uFogFar:{value:190}}}),S),T=new a;for(let e=0;e<d;e++)for(let t=0;t<u;t++){let n=e*u+t;T.makeTranslation((t-51/2)*f,0,-e*f+10),w.setMatrixAt(n,T),C[n*2]=t,C[n*2+1]=e}x.setAttribute(`aCell`,new n(C,2)),w.frustumCulled=!1,y.add(w);let E=w.material.uniforms,D=new t,O=!0;function k(){let e=h.clientWidth,t=h.clientHeight;e&&t&&(_.setSize(e,t,!1),b.aspect=e/t,O=b.aspect>1,b.updateProjectionMatrix())}new ResizeObserver(k).observe(h),k();let A=g.lived,j=g.lived,M=g.reduced?2:0,N=M,P=0,F=0,I=0,L=0,R=!1,z=0,B=performance.now();function V(){O?(b.position.set(-4+I*4,58+L*3,50),D.set(-16,0,-24),E.uFogNear.value=92,E.uFogFar.value=190):(b.position.set(I*2,34+L*2,70),D.set(0,0,18),E.uFogNear.value=70,E.uFogFar.value=150),b.lookAt(D)}function H(e){let t=Math.min((e-B)/1e3,.05);B=e,j+=(A-j)*(1-Math.exp(-t*5)),N+=(M-N)*(1-Math.exp(-t*.9)),I+=(P-I)*(1-Math.exp(-t*2.5)),L+=(F-L)*(1-Math.exp(-t*2.5)),E.uTime.value=e/1e3,E.uLived.value=j,E.uRise.value=N,V(),_.render(y,b),R&&!g.reduced&&(z=requestAnimationFrame(H))}function U(){cancelAnimationFrame(z),B=performance.now(),z=requestAnimationFrame(H)}return h.classList.add(`ready`),U(),{setLived(e,t=!0){A=e,(!t||g.reduced)&&(j=e),g.reduced&&U()},rise(){M=2,g.reduced&&(N=2)},setPointer(e,t){P=e,F=t},setVisible(e){e!==R&&(R=e,e?U():cancelAnimationFrame(z))}}}export{h as createWeeks};