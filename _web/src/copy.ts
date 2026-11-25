// Landing copy. Every feature named here exists in the app (checked in InTime, 2026-11-24/25).
// Strings in `disclosure` are copied from app/src/main/res/values*/strings_accessibility_disclosure.xml.

export type Lang = "es" | "en";

export const BASE = "https://danielaguilarj.github.io/momentum-app";
export const PACKAGE = "com.momentummm.app";
export const GITHUB = "https://github.com/AndreaAguilarJ/InTime";

export function playUrl(lang: Lang, content: string): string {
  const ref = `utm_source%3Dmomentum-web%26utm_medium%3Dweb%26utm_content%3D${content}${lang === "en" ? "-en" : ""}`;
  return `https://play.google.com/store/apps/details?id=${PACKAGE}&hl=${lang === "es" ? "es_419" : "en"}&referrer=${ref}`;
}

const es = {
  lang: "es" as Lang,
  path: "/",
  alt: "/en/",
  title: "Momentum: bloqueador de apps y de Reels y Shorts para Android",
  description:
    "Bloquea Reels y Shorts sin bloquear toda la app, pon límites de tiempo a tus apps y reduce tu tiempo de pantalla. Gratis, sin anuncios y sin cuenta.",
  skip: "Saltar al contenido",
  nav: { features: "Funciones", privacy: "Privacidad", guides: "Guías", guidesPath: "/guias/", other: "English", cta: "Descargar" },
  hero: {
    h1a: "Bloquea los Reels.",
    h1b: "Conserva la app.",
    lead: "Momentum corta solo la parte que te atrapa, como los Reels de Instagram o los Shorts de YouTube, y deja tus mensajes funcionando. Gratis, sin anuncios y sin crear cuenta.",
    cta: "Descargar gratis en Google Play",
    how: "Ver cómo funciona",
    meta: "Android 8.0 o superior · En español, inglés, portugués, alemán y francés",
  },
  phone: {
    simulated: "Pantalla simulada",
    tabs: ["Para ti", "Siguiendo"],
    caption: "Audio original",
    detected: "Reels · detectado",
    blockTitle: "Reels bloqueado",
    blockText: "Tus mensajes siguen disponibles.",
    blockButton: "Volver al inicio",
    inbox: "Mensajes",
    chats: [
      ["Mamá", "¿Llegas a cenar?"],
      ["Equipo del proyecto", "Ya subí la presentación"],
      ["Ana", "Jaja sí, mañana te cuento"],
      ["Luis", "¿Vamos al gimnasio a las 7?"],
    ],
  },
  story: {
    label: "Cómo funciona",
    beats: [
      ["Reconoce la sección.", "Cuando abres los Reels, los Shorts o Explorar, Momentum lo detecta en ese momento, dentro de tu teléfono."],
      ["La bloquea al instante.", "Aparece la pantalla de bloqueo o vuelves al inicio. El siguiente video ya no empieza solo."],
      ["Lo demás sigue abierto.", "Tus mensajes, tu perfil y el resto de la app funcionan como siempre."],
    ],
  },
  weeks: {
    h2: "Una vida de 80 años cabe en 4,160 semanas.",
    text: "Momentum te muestra la tuya en una cuadrícula, dentro de la app, en widgets y como fondo de pantalla. Cuesta más regalarle una semana al scroll cuando la ves.",
    age: "Tu edad",
    lived: "semanas vividas",
    left: "por delante",
    note: "Cálculo aproximado sobre una vida de 80 años.",
    alt: "Cuadrícula de 4,160 semanas: 52 columnas por año y 80 filas, una por cada año de vida",
  },
  features: {
    h2: "Barreras que no dependen de tu fuerza de voluntad.",
    lead: "Tú eliges cuánto, cuándo y dónde. Momentum se encarga de cumplirlo.",
    limits: {
      title: "Un límite diario para cada app",
      text: "Ponle minutos a cada app o red social. Al llegar al límite, Momentum la bloquea hasta el día siguiente.",
      today: "Hoy",
      of: "de",
      min: "min",
      blocked: "Bloqueada",
    },
    schedule: {
      title: "Horarios y lugares",
      text: "Bloquea por días y horas, o según el lugar o la red Wi‑Fi: en clase, en la oficina o en casa.",
      days: ["L", "M", "M", "J", "V", "S", "D"],
      classes: "Clases",
      sleep: "Dormir",
      wifi: "Wi‑Fi de casa",
      wifiRule: "Modo enfoque",
    },
    focus: {
      title: "Modo enfoque con Pomodoro",
      text: "Sesiones de 25/5 o de la duración que elijas, con metas, rachas y días de gracia para que un mal día no rompa tu racha.",
      session: "Sesión de enfoque",
      streak: "Racha",
      days: "días",
      grace: "1 día de gracia disponible",
    },
    moreTitle: "Y además",
    more: [
      ["message-circle", "Solo comunicación", "Permite los mensajes y bloquea feeds, historias y reels."],
      ["radiation", "Modo nuclear", "El bloqueo más fuerte, de 1 a 3 meses. Quitarlo antes exige una espera seguida con Momentum abierto, de 30 minutos por defecto."],
      ["key-round", "Contraseña y emergencia", "Protege tus reglas con contraseña y guarda un desbloqueo de emergencia."],
      ["globe", "Sitios web", "Bloquea las páginas que te distraen en los navegadores compatibles."],
      ["smartphone", "Launcher minimalista", "Una pantalla de inicio simple, con teléfono, mensajes y contactos."],
    ],
  },
  privacy: {
    h2: "El permiso de accesibilidad, sin letra chica.",
    text: "Android solo deja saber qué app o sección tienes abierta a través del servicio de accesibilidad. Antes de pedirlo, Momentum te muestra un aviso. Este es un extracto, con sus palabras exactas:",
    points: [
      ["Se analiza en tu teléfono.", "Nada de lo que ves se envía a un servidor."],
      ["No se guarda ni se comparte.", "Ni lo que ves ni lo que escribes."],
      ["Lo apagas cuando quieras.", "En Ajustes de Android > Accesibilidad."],
    ],
  },
  disclosure: {
    title: "Uso del servicio de accesibilidad",
    intro: "Momentum usa la API AccessibilityService de Android para bloquear las apps, las secciones dentro de las apps (como Reels o Shorts) y los sitios web que tú eliges, en el momento en que los abres.",
    readsTitle: "Qué datos lee",
    reads: [
      "Qué app está abierta en la pantalla.",
      "El contenido de la pantalla de las apps en las que configuras un bloqueo, para reconocer secciones como Reels o Shorts.",
    ],
    useTitle: "Para qué los usa",
    use: "Se analizan en tu teléfono en el momento. Momentum no guarda lo que ves ni lo que escribes, no lo envía a ningún servidor y no lo comparte con nadie.",
    accept: "Aceptar y continuar",
    decline: "No, gracias",
    caption: "Extracto del aviso que muestra la app.",
  },
  compare: {
    h2: "Lo que ya trae tu teléfono, y lo que le falta.",
    cols: ["", "Bienestar digital de Android", "Temporizador de Shorts de YouTube", "Momentum"],
    rows: [
      ["Bloquea solo Reels o Shorts", "No, bloquea toda la app", "Solo los Shorts de YouTube", "Sí, en varias apps"],
      ["Tus mensajes siguen funcionando", "No, se bloquean con la app", "No aplica", "Sí"],
      ["Instagram, TikTok, Facebook y X", "Sí, como apps completas", "No", "Sí"],
      ["Difícil de quitar en un momento de tentación", "Se quita desde Ajustes", "Con más de 0 minutos, el aviso se descarta", "Contraseña y modo nuclear"],
    ],
    source: "Detalles y fuentes en la guía",
    sourcePath: "/bloquear-reels-shorts-android/",
  },
  free: {
    words: ["Gratis.", "Sin anuncios.", "Sin cuenta."],
    text: "Todas las funciones están disponibles sin pagar, la app no muestra publicidad y puedes usarla sin registrarte.",
  },
  guides: { h2: "Guías para dejar el scroll infinito", all: "Ver todas las guías" },
  faq: {
    h2: "Preguntas frecuentes",
    items: [
      ["¿Momentum es gratis?", "Sí. Todas las funciones están disponibles sin pago y la app no muestra anuncios."],
      ["¿Necesito crear una cuenta?", "No. Puedes usar Momentum sin crear cuenta."],
      ["¿Puedo bloquear solo los Reels sin bloquear todo Instagram?", "Sí. Momentum puede bloquear únicamente la sección de Reels de Instagram o los Shorts de YouTube, y dejarte usar los mensajes y el resto de la app. También tiene un modo solo comunicación que permite mensajes y bloquea feeds, historias y reels."],
      ["¿Por qué pide el permiso de accesibilidad?", "Android solo permite detectar qué app o sección tienes abierta a través del servicio de accesibilidad. Momentum lo usa únicamente para aplicar tus reglas: cuando una coincide, muestra la pantalla de bloqueo o vuelve al inicio. El servicio solo se activa si lo aceptas en el aviso de la app y lo enciendes en los ajustes de Android."],
      ["¿Y si quiero quitar el bloqueo en un momento de tentación?", "Puedes proteger tus reglas con contraseña y usar un desbloqueo de emergencia. Además existe el modo nuclear, el bloqueo más fuerte: bloquea las apps que elijas durante 1 a 3 meses, y para quitarlo antes de tiempo hay que mantener Momentum abierto y visible durante una espera larga y seguida (30 minutos por defecto)."],
      ["¿Funciona si Instagram o YouTube cambian su diseño?", "Las apps cambian su diseño con frecuencia. Si Instagram o YouTube modifican cómo está armada una sección, la detección puede fallar hasta que Momentum se actualice. Por eso conviene mantener la app al día."],
      ["¿Momentum es una herramienta de accesibilidad para personas con discapacidad?", "No. Usa el servicio de accesibilidad de Android solo para sus funciones de bloqueo."],
      ["¿Está afiliada a Instagram, YouTube o TikTok?", "No. Momentum es independiente y no tiene relación con esas apps."],
    ],
  },
  dawn: {
    h2: "Mañana empieza sin scroll.",
    steps: ["Instala Momentum desde Google Play.", "Elige qué bloquear: una sección, una app o un horario.", "Activa el servicio cuando la app te lo explique."],
    cta: "Descargar gratis en Google Play",
  },
  footer: {
    note: "Momentum no está afiliado a Instagram, YouTube, TikTok ni a ninguna otra app que permite bloquear. Las marcas pertenecen a sus dueños.",
    guides: "Guías",
    source: "Código en GitHub",
  },
  schemaName: "Momentum: Bloquea Reels y Apps",
  schemaDescription:
    "Bloqueador de apps y redes sociales para Android: bloquea Reels y Shorts, limita el tiempo de pantalla y activa el modo enfoque.",
  ogLocale: "es_419",
};

export type Copy = typeof es;

const en: Copy = {
  lang: "en",
  path: "/en/",
  alt: "/",
  title: "Momentum: App Blocker and Reels & Shorts Blocker for Android",
  description:
    "Block Reels and Shorts without blocking the whole app, set time limits for your apps and cut your screen time. Free, no ads and no account needed.",
  skip: "Skip to content",
  nav: { features: "Features", privacy: "Privacy", guides: "Guides", guidesPath: "/en/guides/", other: "Español", cta: "Download" },
  hero: {
    h1a: "Block the Reels.",
    h1b: "Keep the app.",
    lead: "Momentum cuts out only the part that hooks you, like Instagram Reels or YouTube Shorts, and keeps your messages working. Free, no ads and no account.",
    cta: "Get it free on Google Play",
    how: "See how it works",
    meta: "Android 8.0 or later · In English, Spanish, Portuguese, German and French",
  },
  phone: {
    simulated: "Simulated screen",
    tabs: ["For you", "Following"],
    caption: "Original audio",
    detected: "Reels · detected",
    blockTitle: "Reels blocked",
    blockText: "Your messages are still available.",
    blockButton: "Back to home",
    inbox: "Messages",
    chats: [
      ["Mom", "Are you home for dinner?"],
      ["Project team", "Uploaded the slides"],
      ["Ana", "Haha yes, tell you tomorrow"],
      ["Luis", "Gym at 7?"],
    ],
  },
  story: {
    label: "How it works",
    beats: [
      ["It spots the section.", "When you open Reels, Shorts or Explore, Momentum detects it right then, on your phone."],
      ["It blocks it instantly.", "The block screen appears or you go back home. The next video no longer starts by itself."],
      ["Everything else stays open.", "Your messages, your profile and the rest of the app work as usual."],
    ],
  },
  weeks: {
    h2: "An 80-year life fits in 4,160 weeks.",
    text: "Momentum shows you yours as a grid, inside the app, in widgets and as a wallpaper. It is harder to give a week away to the scroll when you can see it.",
    age: "Your age",
    lived: "weeks lived",
    left: "ahead",
    note: "Rough estimate based on an 80-year life.",
    alt: "Grid of 4,160 weeks: 52 columns per year and 80 rows, one for each year of life",
  },
  features: {
    h2: "Barriers that do not depend on willpower.",
    lead: "You choose how much, when and where. Momentum makes it stick.",
    limits: {
      title: "A daily limit for every app",
      text: "Give each app or social network its minutes. When you reach the limit, Momentum blocks it until the next day.",
      today: "Today",
      of: "of",
      min: "min",
      blocked: "Blocked",
    },
    schedule: {
      title: "Schedules and places",
      text: "Block by days and hours, or by place or Wi‑Fi network: in class, at the office or at home.",
      days: ["M", "T", "W", "T", "F", "S", "S"],
      classes: "Classes",
      sleep: "Sleep",
      wifi: "Home Wi‑Fi",
      wifiRule: "Focus mode",
    },
    focus: {
      title: "Focus mode with Pomodoro",
      text: "Sessions of 25/5 or any length you choose, with goals, streaks and grace days so one bad day does not break your streak.",
      session: "Focus session",
      streak: "Streak",
      days: "days",
      grace: "1 grace day available",
    },
    moreTitle: "And also",
    more: [
      ["message-circle", "Communication only", "Allows messages and blocks feeds, stories and reels."],
      ["radiation", "Nuclear mode", "The strongest block, for 1 to 3 months. Removing it early takes an uninterrupted wait with Momentum open, 30 minutes by default."],
      ["key-round", "Password and emergency", "Protect your rules with a password and keep an emergency unlock."],
      ["globe", "Websites", "Block the sites that distract you in supported browsers."],
      ["smartphone", "Minimalist launcher", "A simple home screen with phone, messages and contacts."],
    ],
  },
  privacy: {
    h2: "The accessibility permission, no fine print.",
    text: "Android only lets an app know which app or section is open through the accessibility service. Before asking for it, Momentum shows you a notice. Here is an excerpt, in its exact words:",
    points: [
      ["It is analysed on your phone.", "Nothing you see is sent to a server."],
      ["Nothing is stored or shared.", "Not what you see, not what you type."],
      ["You turn it off any time.", "In Android Settings > Accessibility."],
    ],
  },
  disclosure: {
    title: "Use of the Accessibility Service",
    intro: "Momentum uses Android's AccessibilityService API to block the apps, the sections inside apps (such as Reels or Shorts) and the websites you choose, at the moment you open them.",
    readsTitle: "What data it reads",
    reads: [
      "Which app is open on the screen.",
      "The screen content of the apps where you set up a block, to recognise sections such as Reels or Shorts.",
    ],
    useTitle: "What it is used for",
    use: "It is analysed on your phone in real time. Momentum does not store what you see or type, does not send it to any server and does not share it with anyone.",
    accept: "Accept and continue",
    decline: "No, thanks",
    caption: "Excerpt of the notice the app shows.",
  },
  compare: {
    h2: "What your phone already has, and what it lacks.",
    cols: ["", "Android Digital Wellbeing", "YouTube Shorts timer", "Momentum"],
    rows: [
      ["Blocks only Reels or Shorts", "No, it blocks the whole app", "Only YouTube Shorts", "Yes, in several apps"],
      ["Your messages keep working", "No, they are blocked with the app", "Not applicable", "Yes"],
      ["Instagram, TikTok, Facebook and X", "Yes, as whole apps", "No", "Yes"],
      ["Hard to remove in a moment of temptation", "Removed from Settings", "Above 0 minutes, the reminder can be dismissed", "Password and nuclear mode"],
    ],
    source: "Details and sources in the guide",
    sourcePath: "/en/block-reels-shorts-android/",
  },
  free: {
    words: ["Free.", "No ads.", "No account."],
    text: "Every feature is available without paying, the app shows no ads and you can use it without signing up.",
  },
  guides: { h2: "Guides to stop doomscrolling", all: "See all guides" },
  faq: {
    h2: "Frequently asked questions",
    items: [
      ["Is Momentum free?", "Yes. All features are available without payment and the app shows no ads."],
      ["Do I need an account?", "No. You can use Momentum without creating an account."],
      ["Can I block only Reels without blocking all of Instagram?", "Yes. Momentum can block just the Reels section of Instagram or YouTube Shorts and let you keep using messages and the rest of the app. It also has a communication-only mode that allows messages and blocks feeds, stories and reels."],
      ["Why does it ask for the accessibility permission?", "Android only lets an app see which app or section is open through the accessibility service. Momentum uses it only to apply your rules: when one matches, it shows the block screen or returns to the home screen. The service only turns on if you accept the notice in the app and enable it in Android settings."],
      ["What if I want to remove the block in a moment of temptation?", "You can protect your rules with a password and use an emergency unlock. There is also nuclear mode, the strongest block: it locks the apps you choose for 1 to 3 months, and turning it off early means keeping Momentum open and visible for a long, uninterrupted wait (30 minutes by default)."],
      ["Does it still work if Instagram or YouTube change their design?", "Apps change their design often. If Instagram or YouTube change how a section is built, detection can fail until Momentum is updated. That is why it is worth keeping the app up to date."],
      ["Is Momentum an accessibility tool for people with disabilities?", "No. It uses Android's accessibility service only for its blocking features."],
      ["Is it affiliated with Instagram, YouTube or TikTok?", "No. Momentum is independent and has no relationship with those apps."],
    ],
  },
  dawn: {
    h2: "Tomorrow starts without the scroll.",
    steps: ["Install Momentum from Google Play.", "Choose what to block: a section, an app or a schedule.", "Turn on the service when the app explains it."],
    cta: "Get it free on Google Play",
  },
  footer: {
    note: "Momentum is not affiliated with Instagram, YouTube, TikTok or any other app it lets you block. Trademarks belong to their owners.",
    guides: "Guides",
    source: "Source on GitHub",
  },
  schemaName: "Momentum: App & Reels Blocker",
  schemaDescription:
    "App and social media blocker for Android: block Reels and Shorts, limit screen time and use focus mode.",
  ogLocale: "en_US",
};

export const COPY: Record<Lang, Copy> = { es, en };
