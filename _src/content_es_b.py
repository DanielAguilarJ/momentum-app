from layout import BASE, article_schema
from content_es_a import cta


def life_grid(lived, total=4160):
    cells = "".join('<i></i>' if n < lived else '<i class="f"></i>' for n in range(total))
    return f'<div class="weeks" role="img" aria-label="Cuadrícula de 80 años de vida en semanas: {lived} semanas vividas y {total - lived} por vivir">{cells}</div>'


SCREEN_BODY = f"""
<h1>Cómo reducir el tiempo de pantalla en el celular: 8 pasos que sí funcionan</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 6 minutos</p>
<p class="lead">Decir «voy a usar menos el celular» casi nunca basta. Lo que funciona es cambiar el entorno para que lo fácil sea usarlo menos. Estos son ocho pasos, en orden, que puedes aplicar hoy en Android.</p>

<h2>1. Mide primero cuánto usas cada app</h2>
<p>Antes de ponerte metas, mira los datos reales. Android tiene su panel de Bienestar digital, y Momentum muestra cuánto tiempo pasas en cada app, tus apps más usadas, tu evolución por semana y un resumen semanal comparado con la semana anterior. Casi todo el mundo se sorprende con el resultado.</p>

<h2>2. Elige solo dos o tres apps culpables</h2>
<p>Intentar controlar todo a la vez es la receta para rendirte el tercer día. Mira tu lista y elige las dos o tres apps donde más tiempo se te va sin darte cuenta, normalmente una red social y una de videos.</p>

<h2>3. Pon un límite diario a esas apps</h2>
<p>Un límite diario convierte «un rato más» en una decisión concreta. En Momentum le asignas un tiempo a cada app o red social y, cuando lo alcanzas, la app se bloquea.</p>

<h2>4. Bloquea la sección, no toda la app</h2>
<p>Muchas veces el problema no es la app sino una parte: los Reels, los Shorts o la pestaña Explorar. Si bloqueas toda la app pierdes también los mensajes, y eso te empuja a quitar el bloqueo. Bloquear solo la sección que te atrapa es más fácil de mantener. Tienes los pasos en la <a href="{BASE}/bloquear-reels-shorts-android/">guía para bloquear Reels y Shorts</a>.</p>

<h2>5. Programa horarios para dormir y para trabajar</h2>
<p>El scroll nocturno es de los hábitos que más cuesta cortar. Un bloqueo por horario, con los días y las horas que elijas, hace que las apps distractoras no estén disponibles justo cuando más te tientan: al estudiar, al trabajar o antes de dormir. Momentum también permite reglas por lugar o por red Wi-Fi.</p>

<h2>6. Quita las notificaciones que no necesitas</h2>
<p>Muchas veces abres el celular porque una notificación te llamó. En los ajustes de Android desactiva las de apps que no son de personas: promociones, sugerencias de videos, «te extrañamos». Deja solo mensajes y llamadas.</p>

<h2>7. Haz que el celular sea más aburrido</h2>
<p>Los colores y los iconos están diseñados para llamar la atención. Dos cambios ayudan: mover las apps tentadoras fuera de la pantalla de inicio y, en muchos teléfonos, poner la pantalla en escala de grises en las horas de descanso. Si quieres ir más lejos, el <a href="{BASE}/launcher-minimalista-android/">launcher minimalista</a> deja solo teléfono, mensajes y contactos.</p>

<h2>8. Sustituye el hábito, no solo lo quites</h2>
<p>Si quitas el scroll y no pones nada en su lugar, el hueco se llena con otra app. Usa ese tiempo para una sesión de enfoque: Momentum trae un temporizador Pomodoro (25/5) o con la duración que elijas, con metas diarias y semanales y rachas. Revisa tu resumen cada semana y ajusta los límites.</p>

<div class="card"><p><strong>Una advertencia útil:</strong> el modo más estricto de Momentum (el modo nuclear) bloquea las apps que elijas durante 1 a 3 meses, y quitarlo antes de tiempo exige una espera larga y seguida con la app abierta. Empieza con límites normales y protégelos con contraseña, y reserva el modo nuclear para cuando ya conozcas tus hábitos.</p></div>

<p>{cta("guia-pantalla-final")}</p>

<h2>Preguntas frecuentes</h2>
<details><summary>¿Cuántas horas de pantalla son demasiadas?</summary><p>No hay un número que sirva para todos. Lo útil es comparar con tu propia meta: cuánto tiempo te gustaría dedicar a cada app y cuánto dedicas en realidad. Por eso el primer paso es medir.</p></details>
<details><summary>¿Necesito pagar para usar los límites de tiempo?</summary><p>No. En Momentum los límites, los horarios y el resto de las funciones están disponibles sin pago.</p></details>
<details><summary>¿Puedo seguir usando mis mensajes?</summary><p>Sí. Puedes bloquear solo las secciones que te distraen o usar el modo solo comunicación, que permite los mensajes y bloquea feeds, historias y reels.</p></details>
"""


LIFE_BODY = f"""
<h1>Tu vida en semanas: qué es y cómo verla en tu celular</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 4 minutos</p>
<p class="lead">Una vida de 80 años cabe en una cuadrícula de 4,160 cuadritos. Cada uno es una semana. Verla completa en una sola pantalla cambia la forma de pensar el tiempo.</p>

<h2>De dónde viene la idea</h2>
<p>La visualización se popularizó con el artículo «Your Life in Weeks», que el escritor Tim Urban publicó en 2014 en <a href="https://waitbutwhy.com/2014/05/life-weeks.html">Wait But Why</a>. Urban dibuja una vida de 90 años (4,680 semanas) como una cuadrícula en la que cada fila es un año, y pregunta si estás aprovechando tus semanas. La idea conecta con una tradición mucho más antigua, el <em>memento mori</em>: recordar que el tiempo es finito para decidir mejor cómo usarlo.</p>

<h2>Cómo se calcula</h2>
<p>Cada año tiene 52 semanas, así que 80 años son 80 × 52 = 4,160 semanas. Aquí tienes un ejemplo para una persona de 25 años: las semanas vividas están en color y las que quedan, en gris.</p>
{life_grid(25 * 52)}
<p class="meta">Ilustración de ejemplo: 1,300 semanas vividas de 4,160. No es una predicción de nadie; la esperanza de vida cambia de una persona a otra.</p>

<h2>Para qué sirve</h2>
<ul>
<li><strong>Dar perspectiva.</strong> Ver el total ayuda a distinguir lo urgente de lo importante.</li>
<li><strong>Planear por semanas.</strong> Una semana es una unidad más manejable que un año para empezar un hábito.</li>
<li><strong>Reducir el tiempo perdido.</strong> Ver «semanas» en vez de «minutos» hace más visible lo que cuesta una hora de scroll.</li>
</ul>

<h2>Cómo verla en tu celular con Momentum</h2>
<p>Momentum incluye una sección llamada «Mi vida en semanas»:</p>
<ol>
<li>Introduce tu fecha de nacimiento. La app calcula tus semanas vividas y las que quedan según una expectativa de vida que tú puedes ajustar.</li>
<li>Elige los colores de las semanas vividas, de las futuras y del fondo.</li>
<li>Añade el widget a la pantalla de inicio: mantén pulsada la pantalla, elige «Widgets» y busca «Mi vida en semanas».</li>
<li>Si prefieres, guarda la cuadrícula como imagen o ponla como fondo de pantalla.</li>
</ol>
<p>También tienes widgets del progreso del año y de frases motivadoras.</p>
<p>{cta("guia-vida-semanas")}</p>

<h2>Preguntas frecuentes</h2>
<details><summary>¿Por qué 4,160 cuadritos?</summary><p>Porque Momentum parte de 80 años de vida: 80 por 52 semanas. Puedes ajustar la expectativa de vida en la app para que se parezca más a tus circunstancias.</p></details>
<details><summary>¿Es una predicción de cuánto voy a vivir?</summary><p>No. Es una forma de visualizar el tiempo, no un pronóstico. Ninguna cuadrícula puede decir cuánto vivirás.</p></details>
<details><summary>¿Necesito una cuenta?</summary><p>No para usar Momentum. La app te pide tu fecha de nacimiento para dibujar tu cuadrícula.</p></details>
"""


LAUNCHER_BODY = f"""
<h1>Launcher minimalista: un celular sin distracciones, sin cambiar de teléfono</h1>
<p class="meta">Actualizado el 25 de noviembre de 2026 · Lectura de 4 minutos</p>
<p class="lead">Un «dumbphone» es un celular básico que solo sirve para llamar y mandar mensajes. Mucha gente los usa para desconectarse, pero no quiere renunciar al mapa, al banco o a la cámara de su teléfono actual. Un launcher minimalista te da lo primero sin quitarte lo segundo.</p>

<h2>Qué es un launcher</h2>
<p>El launcher es la pantalla de inicio de tu Android: los iconos, los widgets y el cajón de aplicaciones. Cambiarlo no borra tus apps ni tus datos; solo cambia lo que ves al desbloquear el teléfono. Si la pantalla de inicio muestra veinte iconos de colores, cada vez que la miras tienes veinte invitaciones a abrir algo.</p>

<h2>Qué ofrece el modo mínimo de Momentum</h2>
<ul>
<li>Una interfaz simple que muestra solo lo esencial: teléfono, mensajes y contactos.</li>
<li>Menos iconos de colores y menos tentaciones, para un detox digital sin cambiar de teléfono.</li>
<li>Una lista de apps permitidas en el modo mínimo, para que añadas las pocas que sí necesitas.</li>
<li>Una opción para salir del modo mínimo cuando lo necesites.</li>
</ul>

<h2>Cómo activarlo</h2>
<ol>
<li>Instala Momentum desde Google Play.</li>
<li>Abre la sección del teléfono mínimo y pulsa <strong>Establecer como launcher por defecto</strong>.</li>
<li>Selecciona <strong>Momentum</strong> en la lista y marca «Usar siempre» si quieres que sea permanente.</li>
<li>Activa el modo mínimo.</li>
</ol>
<p>Si más adelante quieres volver a tu launcher anterior, puedes cambiarlo en los ajustes de Android, en las apps predeterminadas. El nombre exacto del menú varía según la marca del teléfono.</p>
<p>{cta("guia-launcher")}</p>

<h2>Consejos para que funcione</h2>
<ul>
<li><strong>Empieza por un fin de semana.</strong> Probar dos días sin presión es más fácil que prometerte un mes.</li>
<li><strong>Permite solo lo que necesitas.</strong> Un mapa o el banco sí; una red social, no.</li>
<li><strong>Combínalo con límites.</strong> Las apps que dejes disponibles pueden tener su límite diario y su horario. Mira la <a href="{BASE}/reducir-tiempo-de-pantalla-android/">guía de tiempo de pantalla</a>.</li>
</ul>

<h2>Preguntas frecuentes</h2>
<details><summary>¿Pierdo mis apps o mis datos si uso el modo mínimo?</summary><p>No. Cambiar de launcher solo cambia la pantalla de inicio. Tus apps y tus datos siguen en el teléfono.</p></details>
<details><summary>¿Puedo seguir usando una app que no esté en la lista?</summary><p>Mientras el modo mínimo está activo la pantalla muestra solo las apps esenciales y las que agregues a la lista. Puedes salir del modo mínimo cuando quieras.</p></details>
"""


def screen():
    p = dict(lang="es", path="/reducir-tiempo-de-pantalla-android/", alt="/en/reduce-screen-time-android/",
             title="Cómo reducir el tiempo de pantalla en el celular: 8 pasos (Android)",
             description="Ocho pasos para reducir tu tiempo de pantalla en Android: medir, límites por app, horarios, bloquear Reels y Shorts, launcher minimalista y modo enfoque.",
             h1="Cómo reducir el tiempo de pantalla en el celular: 8 pasos que sí funcionan", body=SCREEN_BODY)
    p["schema"] = article_schema(p)
    return p


def life():
    p = dict(lang="es", path="/vida-en-semanas/", alt="/en/life-in-weeks-app/",
             title="Tu vida en semanas: qué es y cómo verla en tu celular",
             description="Qué es la visualización de tu vida en semanas (4,160 cuadritos), de dónde viene la idea de Tim Urban y cómo ver la tuya con un widget y un fondo de pantalla en Android.",
             h1="Tu vida en semanas: qué es y cómo verla en tu celular", body=LIFE_BODY)
    p["schema"] = article_schema(p)
    return p


def launcher():
    p = dict(lang="es", path="/launcher-minimalista-android/", alt=None,
             title="Launcher minimalista en Android: dumbphone sin cambiar de teléfono",
             description="Qué es un launcher minimalista, cómo activarlo en Android y cómo dejar solo teléfono, mensajes y contactos para reducir distracciones sin cambiar de celular.",
             h1="Launcher minimalista: un celular sin distracciones, sin cambiar de teléfono", body=LAUNCHER_BODY)
    p["schema"] = article_schema(p)
    return p
