from layout import BASE, PACKAGE, TODAY, play_url, article_schema


def cta(where, text="Descargar gratis en Google Play"):
    return f'<a class="cta" href="{play_url(where)}" rel="noopener">{text}</a>'


HOME_BODY = f"""
<h1>Momentum: bloqueador de apps y de Reels para Android</h1>
<p class="lead">Bloquea solo los Reels de Instagram o los Shorts de YouTube, pon límites de tiempo a tus apps y recupera tu concentración. Es gratis, no tiene anuncios y funciona sin crear cuenta.</p>
<p>{cta("home-top")}</p>

<h2>Qué puedes hacer con Momentum</h2>
<div class="grid">
<div class="card"><h3>Bloquear Reels y Shorts</h3><p>Apaga solo la sección que te atrapa, como los Reels de Instagram o los Shorts de YouTube, y sigue usando los mensajes y el resto de la app.</p></div>
<div class="card"><h3>Límites de tiempo por app</h3><p>Pon un límite diario a cada app o red social. Al alcanzarlo, Momentum la bloquea.</p></div>
<div class="card"><h3>Horarios y lugares</h3><p>Bloquea por días y horas, o según el lugar o la red Wi-Fi: en la escuela, en la oficina o en casa.</p></div>
<div class="card"><h3>Modo enfoque y Pomodoro</h3><p>Sesiones de enfoque de 25/5 o con la duración que elijas, con metas, rachas y días de gracia.</p></div>
<div class="card"><h3>Launcher minimalista</h3><p>Cambia tu pantalla de inicio por una interfaz simple con teléfono, mensajes y contactos, sin cambiar de teléfono.</p></div>
<div class="card"><h3>Mi vida en semanas</h3><p>Ve tu vida como una cuadrícula de semanas, con widgets y fondo de pantalla para recordar qué importa.</p></div>
</div>

<h2>Cómo empezar en tres pasos</h2>
<ol>
<li><strong>Instala Momentum</strong> desde Google Play. No necesitas crear una cuenta.</li>
<li><strong>Elige qué bloquear</strong>: una sección como Reels o Shorts, una app completa con límite diario, o un horario.</li>
<li><strong>Activa el servicio de accesibilidad</strong> cuando la app te lo explique. Es lo que le permite saber qué app o sección tienes abierta para aplicar tus reglas.</li>
</ol>
<p>{cta("home-steps")}</p>

<h2>Guías para dejar el scroll infinito</h2>
<ul>
<li><a href="{BASE}/bloquear-reels-shorts-android/">Cómo bloquear los Reels de Instagram y los Shorts de YouTube en Android</a></li>
<li><a href="{BASE}/reducir-tiempo-de-pantalla-android/">Cómo reducir el tiempo de pantalla en el celular: 8 pasos</a></li>
<li><a href="{BASE}/vida-en-semanas/">Tu vida en semanas: qué es y cómo verla en tu celular</a></li>
<li><a href="{BASE}/launcher-minimalista-android/">Launcher minimalista: un celular sin distracciones sin cambiar de teléfono</a></li>
</ul>

<h2>Tu privacidad</h2>
<p>Tus reglas de bloqueo y lo que lee el servicio de accesibilidad se quedan en tu teléfono. Momentum no lo guarda, no lo envía a ningún servidor y no lo comparte con terceros. Puedes desactivar el servicio cuando quieras en Ajustes &gt; Accesibilidad.</p>

<h2>Preguntas frecuentes</h2>
<details><summary>¿Momentum es gratis?</summary><p>Sí. Todas las funciones están disponibles sin pago y la app no muestra anuncios.</p></details>
<details><summary>¿Necesito crear una cuenta?</summary><p>No. Puedes usar Momentum sin crear cuenta.</p></details>
<details><summary>¿Puedo bloquear solo los Reels sin bloquear todo Instagram?</summary><p>Sí. Momentum puede bloquear únicamente la sección de Reels de Instagram o los Shorts de YouTube, y dejarte usar los mensajes y el resto de la app. También tiene un modo solo comunicación que permite mensajes y bloquea feeds, historias y reels.</p></details>
<details><summary>¿Por qué pide el permiso de accesibilidad?</summary><p>Android solo permite detectar qué app o sección tienes abierta a través del servicio de accesibilidad. Momentum lo usa únicamente para aplicar tus reglas: cuando una coincide, muestra la pantalla de bloqueo o vuelve al inicio. El servicio solo se activa si lo aceptas en el aviso de la app y lo enciendes en los ajustes de Android.</p></details>
<details><summary>¿Y si quiero quitar el bloqueo en un momento de tentación?</summary><p>Puedes proteger tus reglas con contraseña y usar un desbloqueo de emergencia. Además existe el modo nuclear, el bloqueo más fuerte: una vez activado no se puede quitar hasta que termine el periodo que elegiste.</p></details>
<details><summary>¿Momentum es una herramienta de accesibilidad para personas con discapacidad?</summary><p>No. Usa el servicio de accesibilidad de Android solo para sus funciones de bloqueo.</p></details>
<details><summary>¿Está afiliada a Instagram, YouTube o TikTok?</summary><p>No. Momentum es independiente y no tiene relación con esas apps.</p></details>
<p>{cta("home-bottom")}</p>
"""


def home():
    return dict(
        lang="es", path="/", home=True, alt="/en/",
        title="Momentum: bloqueador de apps y de Reels y Shorts para Android",
        description="Bloquea Reels y Shorts sin bloquear toda la app, pon límites de tiempo a tus apps y reduce tu tiempo de pantalla. Gratis, sin anuncios y sin cuenta.",
        h1="Momentum", body=HOME_BODY,
        schema=[{
            "@context": "https://schema.org", "@type": "MobileApplication",
            "name": "Momentum: Bloquea Reels y Apps", "alternateName": "Momentum",
            "operatingSystem": "Android 8.0+", "applicationCategory": "LifestyleApplication",
            "description": "Bloqueador de apps y redes sociales para Android: bloquea Reels y Shorts, limita el tiempo de pantalla y activa el modo enfoque.",
            "url": BASE + "/", "inLanguage": ["es", "en", "pt", "de", "fr"],
            "downloadUrl": f"https://play.google.com/store/apps/details?id={PACKAGE}",
            "installUrl": f"https://play.google.com/store/apps/details?id={PACKAGE}",
            "image": BASE + "/assets/icon.png",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        }])


REELS_BODY = f"""
<h1>Cómo bloquear los Reels de Instagram y los Shorts de YouTube en Android</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 6 minutos</p>
<p class="lead">Abres Instagram «solo un momento» a ver un mensaje y, cuarenta minutos después, sigues deslizando videos cortos. Esta guía explica qué puedes hacer con los ajustes que ya trae tu celular y las apps, y cómo bloquear solo esa sección con Momentum.</p>

<h2>Por qué es tan difícil dejar los videos cortos</h2>
<p>Los Reels, los Shorts y los videos de TikTok comparten el mismo diseño: cada video dura segundos, el siguiente empieza solo y no hay un final natural. No hay un punto en el que la pantalla te diga «ya viste suficiente». Por eso la fuerza de voluntad pierde con frecuencia contra el diseño, y por eso conviene poner una barrera que no dependa de acordarte en el momento.</p>

<h2>Lo que puedes hacer sin instalar nada</h2>
<h3>En YouTube: limita o apaga los Shorts</h3>
<p>YouTube añadió en octubre de 2025 un temporizador diario para el feed de Shorts y, en abril de 2026, empezó a permitir fijarlo en cero minutos, que apaga la mayoría de los Shorts en el celular. Se activa en el ajuste de gestión del tiempo de la app. La ubicación exacta y la disponibilidad dependen de tu versión de YouTube y de tu cuenta, así que si no lo ves, actualiza la app. Con un límite mayor que cero, el aviso que aparece al llegar al tope se puede descartar, así que funciona como un freno suave.</p>
<h3>En Instagram: no hay un interruptor para los Reels</h3>
<p>Instagram no tiene un ajuste que desactive los Reels. Lo que sí puedes hacer es reducirlos: cambiar el inicio a la vista «Siguiendo», marcar los Reels que no quieres con «No me interesa» y ajustar tus preferencias de contenido sugerido. Ayuda, pero los Reels siguen apareciendo en Explorar y en los mensajes.</p>
<h3>En Android: un límite para toda la app</h3>
<p>Los temporizadores de apps de Bienestar digital de Android limitan la app completa. Funcionan, pero tienen un inconveniente: cuando se acaba el tiempo bloquean también los mensajes directos, que quizá sí necesitas.</p>

<h2>Bloquear solo la sección con Momentum</h2>
<p>Momentum bloquea la sección concreta (los Reels de Instagram, los Shorts de YouTube, Explorar y otras) y deja el resto de la app disponible. Además trae protecciones para que no desactives la regla en un momento de tentación.</p>
<ol>
<li>Instala Momentum desde Google Play. No necesitas crear una cuenta.</li>
<li>Abre <strong>Ajustes &gt; Bloqueo dentro de Apps</strong>. Verás reglas listas para usar, como Reels de Instagram, Explorar, Shorts de YouTube y Reels de Facebook, entre otras.</li>
<li>Toca el aviso para activar el monitoreo. Momentum te explica para qué usa el servicio de accesibilidad y te lleva a los ajustes de Android para encenderlo.</li>
<li>Activa las reglas que quieras. La pantalla muestra cuántas están activas.</li>
<li>Abre Instagram o YouTube. Cuando entras a la sección bloqueada, Momentum muestra su pantalla de bloqueo o te devuelve al inicio, y el resto de la app sigue funcionando.</li>
</ol>
<p>{cta("guia-reels-pasos")}</p>

<h2>Cómo evitar que lo desactives en un momento de tentación</h2>
<ul>
<li><strong>Contraseña:</strong> protege tus reglas para que cambiarlas exija una contraseña.</li>
<li><strong>Modo solo comunicación:</strong> permite los mensajes y bloquea feeds, historias y reels.</li>
<li><strong>Horarios:</strong> bloquea por días y horas, por ejemplo mientras estudias o duermes.</li>
<li><strong>Modo nuclear:</strong> es el bloqueo más fuerte. Una vez activado, no se puede quitar hasta que termine el periodo que elegiste. Úsalo con cuidado.</li>
</ul>

<h2>Una limitación honesta</h2>
<p>Las apps cambian su diseño con frecuencia. Si Instagram o YouTube modifican cómo está armada una sección, la detección puede fallar hasta que Momentum se actualice. Por eso conviene mantener la app al día.</p>

<h2>Preguntas frecuentes</h2>
<details><summary>¿Bloquear los Reels bloquea también los mensajes de Instagram?</summary><p>No. La regla de Reels bloquea solo esa sección. Puedes seguir usando los mensajes y el resto de la app.</p></details>
<details><summary>¿Funciona con TikTok?</summary><p>Momentum incluye reglas para varias apps, entre ellas TikTok, Facebook, Snapchat y X, además de Instagram y YouTube. Las secciones disponibles varían según la app.</p></details>
<details><summary>¿Momentum lee mis mensajes?</summary><p>No guarda ni envía a ningún servidor lo que lee el servicio de accesibilidad. Esa información se analiza en tu teléfono en el momento y no se comparte con terceros.</p></details>
<details><summary>¿Cuesta algo?</summary><p>No. Todas las funciones son gratis y la app no tiene anuncios.</p></details>
<p>{cta("guia-reels-final")}</p>
<p class="meta">Fuentes sobre los controles de YouTube: <a href="https://support.google.com/youtube/thread/382356516/a-new-way-to-manage-your-time-on-shorts">comunicado de YouTube sobre el temporizador de Shorts</a> y <a href="https://www.theverge.com/streaming/912898/youtube-shorts-feed-limit-zero-minutes">The Verge sobre el límite en cero minutos</a>.</p>
"""


def reels():
    p = dict(
        lang="es", path="/bloquear-reels-shorts-android/", alt="/en/block-reels-shorts-android/",
        title="Cómo bloquear Reels de Instagram y Shorts de YouTube en Android",
        description="Guía paso a paso para bloquear solo los Reels y los Shorts en Android sin bloquear los mensajes: opciones nativas de YouTube e Instagram y cómo hacerlo con Momentum.",
        h1="Cómo bloquear los Reels de Instagram y los Shorts de YouTube en Android", body=REELS_BODY)
    p["schema"] = article_schema(p)
    return p
