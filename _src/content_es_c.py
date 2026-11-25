from layout import BASE, article_schema
from content_es_a import cta


def faq(items):
    return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)


def mk(path, alt, title, description, h1, body):
    p = dict(lang="es", path=path, alt=alt, title=title, description=description, h1=h1, body=body)
    p["schema"] = article_schema(p)
    return p


CHOOSE = f"""
<h1>Cómo elegir una app para bloquear apps en Android (y qué evitar)</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 6 minutos</p>
<p class="lead">En Google Play hay decenas de apps para bloquear apps y reducir el tiempo de pantalla. Casi todas prometen lo mismo, pero hacen cosas distintas. Esta guía te da una lista de criterios para elegir la que sí resuelve tu problema y evitar las que piden más de lo necesario.</p>

<h2>Primero, define qué quieres resolver</h2>
<ul>
<li><strong>Pasas demasiado tiempo en general.</strong> Necesitas límites diarios por app y estadísticas.</li>
<li><strong>Una sección concreta te atrapa</strong> (Reels, Shorts, Explorar). Necesitas bloqueo por sección, no solo por app.</li>
<li><strong>Te distraes en ciertos momentos</strong> (estudiar, trabajar, dormir). Necesitas horarios, o reglas por lugar y por Wi-Fi.</li>
<li><strong>Quitas el bloqueo cada vez que te tienta.</strong> Necesitas una protección que cueste desactivar.</li>
</ul>

<h2>Lista de criterios para comparar</h2>
<table>
<tr><th>Criterio</th><th>Qué comprobar</th></tr>
<tr><td>Límites por app</td><td>¿Puedes poner un tiempo diario distinto para cada app?</td></tr>
<tr><td>Bloqueo por sección</td><td>¿Bloquea solo los Reels o los Shorts, o te obliga a bloquear toda la app?</td></tr>
<tr><td>Horarios y lugares</td><td>¿Puedes elegir días y horas, o reglas según el lugar o la red Wi-Fi?</td></tr>
<tr><td>Protección</td><td>¿Hay contraseña, desbloqueo de emergencia o un modo difícil de quitar a propósito?</td></tr>
<tr><td>Precio y anuncios</td><td>¿Qué funciones están detrás de un pago? ¿Muestra anuncios, que van contra el objetivo de distraerte menos?</td></tr>
<tr><td>Cuenta</td><td>¿Puedes usarla sin crear una cuenta? Cuantos menos datos entregues, mejor.</td></tr>
<tr><td>Privacidad</td><td>¿Qué lee, dónde lo analiza y si lo envía a un servidor? Léelo en la ficha de Google Play y en su política de privacidad.</td></tr>
<tr><td>Mantenimiento</td><td>¿Se actualizó hace poco? Las apps de bloqueo por sección dependen de que sigan al día con los cambios de Instagram y YouTube.</td></tr>
</table>

<h2>Los permisos: qué es normal y qué no</h2>
<p>Para funcionar, una app bloqueadora necesita saber qué app tienes abierta. Android lo permite con permisos como el acceso a datos de uso, mostrarse sobre otras apps o el servicio de accesibilidad, que además permite reconocer secciones dentro de una app. Que los pida es normal. Lo que no es normal es que pida acceso a tus contactos, SMS o ubicación sin explicar por qué. Antes de aceptar el servicio de accesibilidad, comprueba que la app explica con claridad para qué lo usa y qué hace con lo que lee.</p>

<h2>Cómo probar una app antes de decidirte</h2>
<ol>
<li>Instala solo una app a la vez, para saber cuál funciona.</li>
<li>Crea una única regla sobre tu mayor problema (por ejemplo, Reels o 30 minutos de una red social).</li>
<li>Úsala tres días sin cambiar nada y mira si tu tiempo de pantalla baja.</li>
<li>Si te estorba más de lo que ayuda, desinstálala. No hace falta quedarte con ella.</li>
</ol>

<h2>Dónde encaja Momentum</h2>
<p>Momentum cubre los criterios de la tabla: límites de tiempo por app, bloqueo de secciones como Reels y Shorts, horarios, reglas por lugar o Wi-Fi, contraseña con desbloqueo de emergencia y un modo nuclear. Es gratis, no tiene anuncios y funciona sin cuenta. Lo que lee el servicio de accesibilidad se analiza en tu teléfono y no se guarda ni se envía a ningún servidor.</p>
<p>También tiene límites que conviene conocer: es solo para Android, el bloqueo por sección depende de que Instagram, YouTube y otras apps no cambien cómo están hechas, y necesita el permiso de accesibilidad para esa función.</p>
<p>{cta("guia-elegir-app")}</p>

<h2>Preguntas frecuentes</h2>
{faq([
    ("¿Una app bloqueadora funciona si la puedo desinstalar?", "Puedes desinstalar cualquier app, así que el valor está en lo que hace difícil hacerlo en un momento de impulso: una contraseña, una pausa antes del desbloqueo de emergencia o un modo, como el nuclear, cuya salida anticipada exige una espera larga. Mira la guía de <a href='" + BASE + "/limites-que-no-puedas-saltarte-android/'>límites que no puedas saltarte</a>."),
    ("¿Necesito pagar para bloquear apps?", "No necesariamente. Algunas apps cobran por las funciones principales y otras, como Momentum, ofrecen todas sus funciones gratis."),
    ("¿Es seguro darle permiso de accesibilidad a una app?", "Es un permiso potente, así que solo se lo des a una app que explique para qué lo usa y cuya ficha y política de privacidad digan qué hace con la información. Puedes desactivarlo cuando quieras en Ajustes &gt; Accesibilidad."),
])}
"""

DOOM = f"""
<h1>Cómo dejar el doomscrolling: 7 tácticas que funcionan</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 5 minutos</p>
<p class="lead">Doomscrolling es deslizar sin parar por noticias o publicaciones, muchas veces malas, aunque ya te sientas peor. No es falta de carácter: las apps están diseñadas para que no haya un punto final. La solución es poner fricción en el camino.</p>

<h2>1. Identifica cuándo te pasa</h2>
<p>Durante tres días apunta en qué momento abres la app sin decidirlo: al despertar, en la cama, en el baño, al aburrirte, después de una discusión. Casi siempre hay un disparador, y es más fácil cambiar un momento que cambiar un hábito entero.</p>

<h2>2. Saca la app del camino</h2>
<p>Mueve la app fuera de la pantalla de inicio, a una carpeta en la última pantalla. Cada paso extra es una oportunidad para reconsiderar.</p>

<h2>3. Bloquea la sección que te atrapa</h2>
<p>El scroll sin fin suele estar en una parte concreta: los Reels, los Shorts, Explorar o «Para ti». Si bloqueas solo esa sección, sigues usando los mensajes y lo demás. Hay una explicación paso a paso en la <a href="{BASE}/bloquear-reels-shorts-android/">guía para bloquear Reels y Shorts</a>.</p>

<h2>4. Pon un tope de tiempo diario</h2>
<p>Elige un tiempo realista para cada app, por ejemplo 30 minutos, y deja que la app se bloquee cuando lo alcances. Tomar la decisión una vez es más fácil que tomarla cada vez que abres el celular.</p>

<h2>5. Protege la noche</h2>
<p>El doomscrolling nocturno roba sueño. Programa un bloqueo por horario para la hora antes de dormir y carga el celular lejos de la cama, para que ya no sea lo primero que tocas al despertar.</p>

<h2>6. Ten un sustituto a mano</h2>
<p>Si el hueco queda vacío, el scroll vuelve. Deja un libro, una libreta o unos audífonos donde antes estaba el celular. Para trabajar o estudiar, una sesión de enfoque con temporizador ayuda a empezar. Mira la <a href="{BASE}/tecnica-pomodoro-android/">guía de la técnica Pomodoro</a>.</p>

<h2>7. Silencia lo que te llama</h2>
<p>Desactiva las notificaciones de noticias y de sugerencias de las redes. Deja solo las de personas.</p>

<div class="card"><p>Si el uso del celular te quita el sueño, afecta tu estado de ánimo o interfiere con tu trabajo o tus relaciones de forma constante, habla con un profesional de salud. Una app ayuda con los hábitos, pero no sustituye ese apoyo.</p></div>

<p>{cta("guia-doomscrolling")}</p>

<h2>Preguntas frecuentes</h2>
{faq([
    ("¿Es lo mismo que la adicción al celular?", "No necesariamente. El doomscrolling es un patrón concreto: consumir sin parar contenido, normalmente negativo. Puede formar parte de un uso problemático del celular, pero no es un diagnóstico."),
    ("¿Bloquear la app entera es mejor?", "A veces sí, por ejemplo en el horario de sueño. Pero si necesitas la app para otra cosa, es más sostenible bloquear solo la sección que te atrapa."),
])}
"""

POMO = f"""
<h1>Técnica Pomodoro en Android: cómo usarla para estudiar o trabajar</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 5 minutos</p>
<p class="lead">La técnica Pomodoro divide el trabajo en bloques cortos con descansos. Es sencilla y por eso funciona: empezar una tarea de 25 minutos cuesta menos que empezar «a estudiar toda la tarde».</p>

<h2>En qué consiste</h2>
<p>El método lo creó Francesco Cirillo a finales de los años 80 y toma su nombre de un temporizador de cocina con forma de tomate. La versión clásica es:</p>
<ol>
<li>Elige una tarea.</li>
<li>Pon un temporizador de <strong>25 minutos</strong> y trabaja solo en eso.</li>
<li>Descansa <strong>5 minutos</strong>.</li>
<li>Tras cuatro bloques, haz un descanso más largo, de 15 a 30 minutos.</li>
</ol>

<h2>Cómo usarla bien</h2>
<ul>
<li><strong>Una sola tarea por bloque.</strong> Si aparece algo nuevo, anótalo y sigue.</li>
<li><strong>El celular fuera de la vista.</strong> Si lo usas como temporizador, que sea la app que lo bloquea y no una red social.</li>
<li><strong>El descanso es descanso.</strong> Levántate, bebe agua, mira por la ventana. No abras una red social: un descanso de 5 minutos se convierte en 40.</li>
<li><strong>Ajusta la duración.</strong> Si 25 minutos se te hacen cortos o largos, cambia el tiempo. Lo importante es que sea fijo.</li>
</ul>

<h2>Cómo hacerlo con Momentum</h2>
<p>Momentum tiene un modo enfoque con temporizador Pomodoro (25/5) o con la duración que tú elijas. Además incluye metas diarias y semanales, desafíos y rachas, TimeCoins por cada minuto enfocado y días de gracia para proteger tu racha cuando un día se complica.</p>
<p>Para que el celular no sea la fuente de interrupciones, combínalo con límites por app y con <a href="{BASE}/bloquear-reels-shorts-android/">el bloqueo de Reels y Shorts</a>. Tienes más ideas en la guía para <a href="{BASE}/estudiar-sin-distracciones-celular/">estudiar sin que el celular te distraiga</a>.</p>
<p>{cta("guia-pomodoro")}</p>

<h2>Preguntas frecuentes</h2>
{faq([
    ("¿Cuántos pomodoros hago al día?", "Depende de tu tarea. Empieza con dos o tres y sube poco a poco. Lo importante es la constancia, no la cantidad."),
    ("¿Y si me interrumpen?", "Si es algo breve, anótalo y vuelve. Si es largo, anula ese bloque y empieza uno nuevo cuando puedas; un bloque a medias no cuenta."),
    ("¿Se puede cambiar de 25/5 a otra duración?", "Sí. Momentum permite elegir la duración de tus sesiones de enfoque."),
])}
"""

DETOX = f"""
<h1>Detox digital: un plan de 7 días para empezar hoy</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 6 minutos</p>
<p class="lead">Un detox digital no significa tirar el celular. Significa decidir cuándo y para qué lo usas. Este plan reparte los cambios en una semana para que no te rindas el segundo día.</p>

<h2>Día 1: mide</h2>
<p>No cambies nada todavía. Anota cuánto tiempo pasas hoy en total y en tus tres apps más usadas. Esa cifra es tu punto de partida.</p>

<h2>Día 2: silencia</h2>
<p>Desactiva las notificaciones de todo lo que no sea una persona. Sin avisos, el celular deja de llamarte.</p>

<h2>Día 3: pon límites</h2>
<p>Elige dos apps y asígnales un límite diario realista. En Momentum puedes poner un tiempo a cada app o red social y se bloquea al llegar al tope.</p>

<h2>Día 4: bloquea la sección que te atrapa</h2>
<p>Activa el bloqueo de los Reels, los Shorts o Explorar, según lo tuyo. Sigues pudiendo usar los mensajes. Mira cómo en la <a href="{BASE}/bloquear-reels-shorts-android/">guía para bloquear Reels y Shorts</a>.</p>

<h2>Día 5: protege el sueño</h2>
<p>Programa un horario nocturno en el que las apps distractoras no estén disponibles, y carga el celular fuera de la cama.</p>

<h2>Día 6: simplifica la pantalla</h2>
<p>Prueba el <a href="{BASE}/launcher-minimalista-android/">launcher minimalista</a> durante un día: solo teléfono, mensajes, contactos y las apps que tú permitas. Notarás cuántas veces buscas un icono por reflejo.</p>

<h2>Día 7: revisa y decide</h2>
<p>Compara con el día 1. Mira qué reglas ayudaron y cuáles te estorbaron, y quédate con las que sí. El plan no termina aquí: es un punto de partida para un uso más intencional.</p>

<div class="card"><p>Si te cuesta mucho mantener los límites, puedes proteger tus reglas con una contraseña. Reserva el modo nuclear, que bloquea durante 1 a 3 meses, para cuando ya sepas qué funciona para ti.</p></div>

<p>{cta("guia-detox")}</p>

<h2>Preguntas frecuentes</h2>
{faq([
    ("¿Tengo que dejar las redes sociales?", "No. El objetivo es usarlas por decisión y no por reflejo. Muchas personas conservan sus redes con límites y sin las secciones que más las atrapan."),
    ("¿Cuánto dura un detox digital?", "Puede ser un día, una semana o un mes. Para empezar, siete días bastan para ver qué cambia."),
])}
"""

LIMITS = f"""
<h1>Cómo poner límites que no puedas saltarte en Android</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 5 minutos</p>
<p class="lead">Poner un límite de tiempo es fácil. Lo difícil es no quitarlo cinco minutos después, cuando la tentación aprieta. La solución es decidirlo ahora, con la cabeza fría, y hacer que cambiar de idea cueste un poco.</p>

<h2>Por qué ayuda decidir antes</h2>
<p>Es una idea muy vieja, la de Ulises atándose al mástil para escuchar a las sirenas sin lanzarse al agua. Cuando decides con calma, eliges lo que de verdad quieres. Cuando estás en el momento, decide el impulso. Un buen bloqueo hace que desactivarlo en el impulso sea más trabajoso que respetarlo.</p>

<h2>Las capas de protección de Momentum</h2>
<ol>
<li><strong>Contraseña.</strong> Protege tus reglas para que cambiarlas pida una contraseña numérica. Una idea que funciona: pídele a alguien de confianza que la elija, para que tú no la sepas.</li>
<li><strong>Desbloqueo de emergencia.</strong> Existe para los casos reales en los que necesitas acceder. Antes de desbloquear, la app te pregunta si de verdad necesitas entrar, una pausa que ayuda a no hacerlo por costumbre.</li>
<li><strong>Horarios.</strong> Al fijar días y horas, las apps están bloqueadas sin que tengas que acordarte.</li>
<li><strong>Modo nuclear.</strong> Es el bloqueo más fuerte: bloquea las apps que elijas durante 1 a 3 meses. Para quitarlo antes de tiempo tienes que mantener Momentum abierto y visible durante una espera seguida (30 minutos por defecto), y la espera solo avanza con la app en pantalla.</li>
</ol>

<div class="card"><p><strong>Úsalo con cuidado:</strong> el modo nuclear dura de 1 a 3 meses y deshacerlo antes de tiempo es incómodo a propósito. No lo actives la primera vez que pruebes Momentum y no incluyas apps que necesites para algo esencial, como el banco o un mapa.</p></div>

<h2>Una configuración que suele funcionar</h2>
<ul>
<li>Límite diario en las dos o tres apps que más tiempo te quitan.</li>
<li>Bloqueo de Reels o Shorts.</li>
<li>Horario de noche y de estudio o trabajo.</li>
<li>Contraseña elegida por otra persona.</li>
<li>Modo nuclear solo cuando de verdad quieras un periodo largo y firme (de 1 a 3 meses), con las apps que más te cuestan.</li>
</ul>
<p>{cta("guia-limites")}</p>

<h2>Preguntas frecuentes</h2>
{faq([
    ("¿Puedo desinstalar Momentum para saltarme los límites?", "Android permite desinstalar apps, así que ninguna app puede impedirlo del todo. La contraseña, los horarios y el modo nuclear hacen que desactivar tus reglas sea más difícil en un momento de impulso, pero la decisión final sigue siendo tuya."),
    ("¿Qué pasa si necesito entrar a una app bloqueada de verdad?", "Para eso existe el desbloqueo de emergencia, que antes te pregunta si de verdad necesitas acceder. Con el modo nuclear activo, quitar el bloqueo antes de tiempo exige una espera larga con la app abierta, por eso conviene probar primero los límites normales y reservar ese modo para cuando estés seguro."),
])}
"""

STUDY = f"""
<h1>Cómo estudiar sin que el celular te distraiga: 6 pasos</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 5 minutos</p>
<p class="lead">Estudiar con el celular al lado es una pelea desigual: cada notificación gana unos segundos de tu atención y cuesta mucho recuperarla. Estos seis pasos reducen la tentación antes de que aparezca.</p>

<h2>1. Decide qué vas a estudiar y cuánto tiempo</h2>
<p>«Voy a estudiar» es vago. «Voy a hacer los ejercicios del tema 3 durante dos bloques de 25 minutos» se puede empezar y terminar.</p>

<h2>2. Pon el celular fuera de la vista</h2>
<p>Mejor en otra habitación o dentro de una mochila. Si lo necesitas para estudiar, deja visible solo la app que usas.</p>

<h2>3. Programa un horario de estudio</h2>
<p>En Momentum puedes bloquear apps por días y horas. Así, de lunes a viernes, de 5 a 8 de la tarde, las redes sociales no están disponibles sin que tengas que acordarte.</p>

<h2>4. Usa reglas por lugar</h2>
<p>Si estudias en la biblioteca o en la escuela, Momentum permite reglas por lugar o por red Wi-Fi, para bloquear las distracciones justo ahí.</p>

<h2>5. Trabaja en bloques</h2>
<p>La <a href="{BASE}/tecnica-pomodoro-android/">técnica Pomodoro</a> ayuda a empezar: 25 minutos de estudio y 5 de descanso. El descanso es para moverte, no para abrir una red social.</p>

<h2>6. Mide y recompénsate</h2>
<p>Al final de la semana revisa cuántos bloques de enfoque hiciste. Momentum registra rachas y metas diarias y semanales, y da TimeCoins por cada minuto enfocado. Una racha visible motiva a seguir.</p>

<p>{cta("guia-estudiar")}</p>

<h2>Preguntas frecuentes</h2>
{faq([
    ("¿Y si necesito el celular para estudiar?", "Bloquea solo lo que te distrae. Con los límites por app y los horarios puedes dejar disponibles las apps que sí usas para estudiar."),
    ("¿Sirve para estudiantes de secundaria o universidad?", "Sí. La técnica y las reglas por horario o lugar sirven en cualquier nivel."),
])}
"""


def pages():
    return [
        mk("/elegir-app-para-bloquear-apps-android/", "/en/choose-app-blocker-android/",
           "Cómo elegir una app para bloquear apps en Android (y qué evitar)",
           "Criterios para elegir una app bloqueadora en Android: límites, bloqueo por sección, horarios, protección, privacidad y permisos. Con una lista de comprobación.",
           "Cómo elegir una app para bloquear apps en Android (y qué evitar)", CHOOSE),
        mk("/dejar-doomscrolling/", "/en/stop-doomscrolling/",
           "Cómo dejar el doomscrolling: 7 tácticas que funcionan",
           "Qué es el doomscrolling y siete tácticas para dejarlo: identificar disparadores, bloquear la sección que te atrapa, límites de tiempo, protección nocturna y sustitutos.",
           "Cómo dejar el doomscrolling: 7 tácticas que funcionan", DOOM),
        mk("/tecnica-pomodoro-android/", "/en/pomodoro-technique-android/",
           "Técnica Pomodoro en Android: cómo usarla para estudiar o trabajar",
           "Qué es la técnica Pomodoro (25 minutos de enfoque y 5 de descanso), cómo aplicarla bien y cómo usar el temporizador de enfoque de Momentum en Android.",
           "Técnica Pomodoro en Android: cómo usarla para estudiar o trabajar", POMO),
        mk("/detox-digital-7-dias/", "/en/digital-detox-7-days/",
           "Detox digital: plan de 7 días para empezar hoy (Android)",
           "Plan de detox digital de 7 días en Android: medir, silenciar notificaciones, límites, bloquear Reels y Shorts, proteger el sueño y simplificar la pantalla de inicio.",
           "Detox digital: un plan de 7 días para empezar hoy", DETOX),
        mk("/limites-que-no-puedas-saltarte-android/", None,
           "Cómo poner límites de tiempo que no puedas saltarte en Android",
           "Cómo hacer que tus límites de uso del celular duren: contraseña, desbloqueo de emergencia, horarios y modo nuclear en Momentum, con precauciones de uso.",
           "Cómo poner límites que no puedas saltarte en Android", LIMITS),
        mk("/estudiar-sin-distracciones-celular/", None,
           "Cómo estudiar sin que el celular te distraiga: 6 pasos",
           "Seis pasos para estudiar sin distracciones del celular: horarios de bloqueo, reglas por lugar, técnica Pomodoro y seguimiento de rachas en Android.",
           "Cómo estudiar sin que el celular te distraiga: 6 pasos", STUDY),
    ]
