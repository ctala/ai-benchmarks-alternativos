# Granite 4.2 8B — startup_content/workshop_outline

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.29 | quality: 9.52
- latency_total: 162.522s | tokens_per_second: 89.5
- input_tokens: 224 | output_tokens: 14553
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

**Workshop: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"**  
*(3 horas totales, 20-30 emprendedores early-stage, NO técnicos, tono energético, práctico, sin tecnicismos, zero jerga. Todo se explica como si lo dijera un compañero que ya lo hizo.)*  

> 💡 **Nota clave para el facilitador (en voz alta y con energía):**  
> *“No vamos a hablar de ‘modelos de lenguaje’, ‘APIs’, ‘fine-tuning’ ni ‘backend’. Vamos a escribir una frase clara que suene natural para tus clientes, probarla con una pregunta real que te hayan enviado antes, y usarla hoy mismo en un correo o WhatsApp. Si no puedes explicarlo en 10 segundos a un amigo, sigue ajustando. ¡Eso es todo!*”

---

### ✅ 1. Agenda detallada con tiempos (hora exacta + dinámica clara)  
*(Total: 180 minutos. Todo con pausas breves y movimiento. No hay bloques largos de charla. Si alguien pregunta, se responde en 30 segundos o se anota para el Q&A.)*

| Tiempo          | Bloque                                  | Duración | Objetivo (en lenguaje práctico)                                                                                                                               | Dinámica (qué hacen los participantes)                                  | Key takeaway (máximo 10 palabras, claro)                              |
|------------------|-------------------------------------------|-----------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|
| 0:00 – 0:10    | ¡Bienvenida + Icebreaker rápido!        | 10 min   | Romper el hielo, conectar con un problema real que todos vivan.                                 | Cada persona dice en 20 segundos: *"Mi startup es [1 frase simple] y la pregunta más frecuente que me mandan es ______."* (en pares, luego 2 personas comparten 1 frase en grupo). *Facilitador: "¡Sí! Eso es exactamente lo que vamos a resolver hoy."* | **"Todos tienen una pregunta frecuente real. Esa es la base."** |
| 0:10 – 0:25    | Por qué un asistente de IA *para ti* + Demo ultra-simple | 15 min   | Mostrar que no es para ingenieros, sino para resolver ese "¡cada día me mandan la misma pregunta!" con poco tiempo. Evitar tecnicismos. | 1 min: Historia real corta (ej.: *Panadería "PanCaliente": "Cada lunes me mandan 30 veces: '¿Tienen opción sin gluten?'"). 3 min: **Demo en vivo súper simple** usando una herramienta gratuita (ej.: [Botsonic free demo](https://botsonic.com) o incluso Google Docs + ChatGPT en modo chat, sin login): escribe el prompt *"Cuando alguien pregunta '¿sin gluten?', responde 'Sí, tenemos pasteles sin gluten (sin harina de trigo). Puedes elegir vaina de chocolate o fruta'. No menciones 'probablemente'."*, y muestra la respuesta automática. 2 min: Explicar *solo eso*: "Escribí una frase clara para la pregunta, la probé con una pregunta real, y listo. No fui a programar nada." | Charla breve (max 8 min), demo en pantalla (máx. 3 min), preguntas rápidas en grupo (responder en 1 frase). *Facilitador dice: "No importa si usas Botsonic, WhatsApp, o incluso un correo. Lo importante es la frase clara."* | **"Un asistente de IA para tu startup = escribir una frase clara para una pregunta real + probarla una vez."** |
| 0:25 – 0:40    | Los 3 pasos *realistas* (nada abstracto) + Template listo para usar | 15 min   | Dar un proceso de 3 pasos fáciles que puedan hacer hoy mismo, con un template tangible que imprimen. | 5 min: Facilitador muestra **slide con solo 3 pasos + template**: <br>1️⃣ *Define la pregunta exacta que te mandan (ej.: "¿Sin gluten?"), NO "preguntas sobre gluten".* <br>2️⃣ *Escribe el prompt usando: "Cuando [la pregunta exacta], responde [respuesta clara y corta], sin [evitar decir 'quizás', 'depende', etc.]. Ejemplo: "Cuando preguntan '¿sin gluten?', responde 'Sí, tenemos pasteles sin gluten (sin harina de trigo). Puedes elegir vaina de chocolate o fruta'."* <br>3️⃣ *Prueba con 1 pregunta real que hayas recibido (ej.: "¿Tienen opción sin gluten?" o "¿Cuánto cuesta el pastel sin gluten?").* <br>5 min: Cada persona toma su **hoja de template impresa** (ver materiales) y, usando su frase del icebreaker, escribe su propio prompt en 3 minutos (en su hoja). Facilitador circula, dice: *"¿La frase suena como si la dirías tú en una llamada? Si dices 'quizás', cámbialo por 'sí' o 'no'."* (ej.: "No digas 'probablemente tienen', di 'sí, tenemos'"). | Mini-ejercicio guiado en silencio (3 min escribir), facilitador anda preguntando "¿Suena natural?" en 1 min por mesa, luego 2 min de compartir rápido en pares ("Mi prompt: 'Cuando preguntan...", "Probé con '¿Sin gluten?' y la respuesta fue..."). *Ninguna explicación larga; solo ejemplos del momento.* | **"Escribe: 'Cuando [pregunta exacta], responde [respuesta clara], sin decir ‘quizás’. Prueba con una pregunta real que ya hayas recibido."** |
| 0:40 – 1:40   | **Ejercicio principal (todos lo hacen, sin excepción)** | 60 min   | Que cada participante ejecute los 3 pasos *con su startup real*, ajuste su frase usando feedback rápido, y vea cómo funciona en contexto. *Este es el corazón práctico.* | 0:40–1:00 (20 min): **Escribir + usar template**. Cada persona (en pares) usa su hoja de template para: <br>- Escribir su prompt (ej.: "Cuando preguntan '¿horarios?', responde 'Abrimos de 8am a 8pm todos los días. Lunes a sábado. Domingo solo 10am-2pm.'", sin jerga). <br>- Elaborar **3 preguntas reales** que hayan recibido (ej.: "¿Abrís hoy?", "¿Hasta qué hora?", "¿Hay horario para niños?") usando sus palabras habituales. *Facilitador da un recordatorio de 30 segundos: "Usa tu lenguaje real: si dicen 'hasta qué hora', responde '8pm', no 'hasta tarde'".* <br>1:00–1:30 (30 min): **Probar + ajustar juntos**. Cada par prueba su prompt con sus 3 preguntas en la hoja (ej.: escribir la respuesta que el prompt daría), luego prueba mentalmente: *"Si un cliente escribe '¿Abrís hoy?', ¿mi respuesta dice 'Abrimos de 8am a 8pm'? ¿Suena natural?"*. Si dice "probablemente", cambian a "Sí". Si es larga, la acortan a 1 línea. Facilitador anda con preguntas rápidas: *"¿Qué dirías tú en WhatsApp si alguien pregunta eso?"*, *"¿Suena como tu voz?"*. Cada par ajusta su frase en 5 minutos (usando la hoja), luego comparten con otro par (2 min por par) para decir: *"Mi prompt ahora dice: [frase corta], y probé con '[pregunta]', la respuesta fue clara."*. <br>1:30–1:40 (10 min): **Mini-share rápido + ajuste final**. 3-4 pares comparten su prompt final (30 segundos cada uno: "Mi startup es X. Pregunta: Y. Mi prompt: Z. Probé con [pregunta] y la respuesta es [respuesta]"). Facilitador destaca 1 frase clara que funcionó bien ("Sí, tenemos pasteles sin gluten..." en vez de "Quizás..."), y corrige rápidamente una que tenga "probablemente" (ej.: "No: 'Probablemente sí' → 'Sí, tenemos'"). *Todo en 2 minutos max por share.* | Dinámica fluida: escribir en silencio (pares), probar en papel (usar hoja), ajustar con una pregunta de "¿Suena como tú?", compartir en pares pequeños (máx. 2 min por grupo), facilitador circula con preguntas de 10-15 segundos ("¿Cómo dirías eso en WhatsApp?"). *Ningún participante queda sin hacer nada; todos escriben, prueban, ajustan.* | **"Mi asistente de IA es mi frase clara + 1 prueba real. Si suena como mi voz, listo. Ajusta solo 'quizás' → 'sí/no'."** |
| 1:40 – 1:55    | Herramientas *reales y gratuitas* (solo 2, sin registro largo) + Cómo empezar HOY | 15 min   | Mostrar 2 opciones simples que usen su prompt ya escrito; enfatizar "comenzar pequeño", no buscar la 'mejor herramienta' ahora. | 5 min: Facilitador muestra **2 pantallazas reales (en vivo o en tarjeta impresa)**: <br>- **Botsonic Free**: "Escribe tu prompt → genera respuestas → usa en sitio web o WhatsApp (gratis hasta 100 respuestas/mes). No necesitas código. (Muestra 30 segundos de cómo pegar el prompt y ver la respuesta)." <br>- **Google Forms + ChatGPT (método rápido)**: "Guarda tus preguntas frecuentes en un Form. En la respuesta automática, pega tu prompt (ej. 'Cuando preguntan X, responde...'). Envía el Form a clientes; ChatGPT responde al mensaje de confirmación. (Muestra 2 minutos rápido: escribir prompt en la descripción del Form)". *Ninguna explicación técnica; solo "pegar el prompt" y "ver la respuesta".* <br>5 min: "Cómo empezar HOY en 5 minutos": <br>1. Toma tu prompt final de la hoja (ej. "Cuando preguntan '¿sin gluten?', responde..."). <br>2. En Botsonic: ve a botsonic.com → 'Crear bot gratis' → pega el prompt → genera → usa el bot en WhatsApp (con el link que da Botsonic). <br>3. O en Google Forms: escribe el prompt en la descripción del Form → cuando alguien envía el Form, el Form responde con tu frase (usando la configuración básica de respuestas automáticas). *Facilitador dice: "No necesitas crear sitio web ni pagar hoy. Usa el WhatsApp que ya tienes o el Form que ya usas."* <br>3 min: Preguntas rápidas (max 1 min por pregunta), y si es sobre herramientas: "¿Necesitas registrarte ahora? → No, para probar gratis basta con el email básico (no requiere tarjeta). Empieza con el prompt que ya tienes; no busques más herramientas ahora." | Demo ultra-rápido (máx. 5 min total para ambas herramientas), ejemplos visuales en pantalla/tarjeta, respuesta a "¿Necesito pagar?" ("No para empezar"), instrucciones de 3 pasos escritos en la hoja de recursos. *Evita nombrar más de 2 herramientas; enfatiza "elige la que ya usas (WhatsApp o Form)".* | **"Empieza HOY con tu prompt ya escrito. Usa WhatsApp o tu Form existente. No busques otra herramienta ahora. Solo pega el prompt y prueba."** |
| 1:55 – 2:20    | "Uno paso para mañana" + Q&A rápido + Energía | 25 min   | Que cada persona se comprometa con *un solo, pequeño acción real* para usar su asistente en 24-48h; resolver preguntas rápidas en 2 min. | 5 min: **"Uno paso para mañana" (rápido y concreto)**. Cada persona (en silencio 2 min) escribe en su hoja: *"Mañana haré: [ej. 'Responderé la próxima pregunta de cliente sobre horarios usando mi prompt en WhatsApp']".* Luego, 3 personas comparten su frase de 10 segundos en grupo (ej. "Mañana responderé preguntas de horarios en WhatsApp con mi prompt"). Facilitador refuerza: "¡Perfecto! No es 'crear el asistente', es 'usar la frase ya lista para la próxima pregunta'". <br>15 min: **Q&A ultra-rápida** (reglas claras): <br>- Cada pregunta se responde en ≤ 60 segundos. <br>- Si es sobre herramienta: "Usa el prompt que ya tienes; prueba en WhatsApp o Form ahora". <br>- Si es "¿Por qué no usar X?", respuesta: "Porque hoy quieres usar lo que ya tienes (WhatsApp/Form); X es para crecer después. Hoy, empieza simple." <br>- Facilitador anota preguntas no respondidas en tarjeta para enviar por email después (no en el momento). <br>5 min: **Cierre energético y con acción**: Facilitador dice en voz alta y con gesto: *"Hoy escribiste una frase clara para tu pregunta más frecuente. Mañana, al recibir esa pregunta (en WhatsApp, email o comentario), escribes: 'Gracias por preguntar! [tu respuesta del prompt]' y listo. No más buscar respuestas. ¡Eso es tu asistente de IA para tu startup! Felicitaciones: ya lo hiciste."* (¡Gestos de energía: levantar la mano, sonreír!). | Compartir "uno paso" en pares pequeños (2 min), Q&A con regla de 60 seg, cierre con frase de acción concreta ("Mañana responderé..."). *Sin hablar de futuras mejoras; solo el paso de mañana.* | **"Mañana, al recibir la pregunta frecuente, respondo con mi frase clara (el prompt) en WhatsApp o email. Listo. No más buscar."** |
| 2:20 – 3:00    | Recursos para llevar + Feedback rápido + Agradecimiento | 40 min   | Entregar lo útil que pueden usar inmediatamente; cerrar con valor claro; recolectar feedback sencillo. | 10 min: **Entrega física + digital sencilla** (ver "Recursos para llevar" abajo). Cada persona recibe su hoja de template impresa (con los 3 pasos + ejemplo), el "One Step Kit" (PDF de 1 página), y una tarjeta con los 2 enlaces de herramientas (Botsonic free, Google Forms tip). Facilitador dice: "Toma esta hoja, ponla en tu bloc o en el celular. Cuando recibas la próxima pregunta frecuente, escribe tu prompt en 2 minutos usando el template. ¡Eso es todo hoy!" <br>15 min: **Feedback rápido (1 palabra + sticky note)**. Cada persona pega un sticky note (color suave) en la pared con: <br>- 1 palabra que mejor describe el workshop (ej. "claro", "rápido", "útil"), <br>- 1 palabra que aún les costaría (ej. "ajustar frase"). Facilitador lee 3 ejemplos en voz alta (sin juzgar), agradece ("¡Gracias por decir 'claro'! Eso nos ayuda a mejorar"). *Mantiene energía: "Ver tu feedback nos ayuda a hacerlo aún mejor para el próximo grupo".* <br>15 min: **Cierre personal + llamado a acción mínimo + agradecimiento auténtico**. Facilitador dice: <br>*"Recuerda: no necesitas ser ingeniero. Necesitas tu frase clara para la pregunta que más te mandan. Hoy la escribiste. Mañana la usas en WhatsApp. Eso es todo. Si quieres ver cómo otros emprendedores ya están usando esto (ejemplos reales breves), avísame por WhatsApp [tu número breve] o por este grupo [link simple]; te mandaré 2 ejemplos en 24h. ¡Gracias por venir, por compartir su pregunta y por empezar hoy! Ahora ve a responder esa primera pregunta con tu frase. ¡Éxito!*"* (Sonrisa, tono cálido pero seguro). Entrega de recursos y agradecimiento físico (ej. "Gracias por construir"). | Entrega hoja + PDF + tarjeta, feedback con sticky notes (facilitador ayuda a pegarlos), cierre con frase de acción y contacto sencillo (WhatsApp/link). *No hay charla larga; se usa tiempo para que los participantes lean y guarden el recurso.* | **"Mi asistente de IA = mi frase clara + usarla mañana en WhatsApp/email. Recursos en mi hoja. Mañana, respondo con la frase. Listo."** |

> ⏱️ **Total dinámico práctico**: Las pausas naturales (ej. 2 min entre bloques, 1 min para preguntas rápidas) están incluidas en los tiempos. El facilitador mantiene energía con frases cortas, gestos (levantar la mano en cierre), y evitar palabras como "optimizar", "integrar", "pipeline". Nada de "deberían".

---

### ✅ 2. Materiales necesarios (preparar **antes** del workshop, listo para imprimir/usar)

| Material                     | Cantidad/Formato                     | Por qué es necesario                                                                                                                               | Cómo prepararlo (ejemplo rápido)                                                                                                                               |
|------------------------------|----------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Hoja de Template impresa** (1 por persona) | 30 hojas A5 o tamaño carta, doblada simple | Contiene solo los 3 pasos + template visual + ejemplo conjeja: <br>```\n1. Define la pregunta exacta que te mandan (ej.: "¿Sin gluten?" NO "pregunta sobre gluten").\n2. Escribe: "Cuando [pregunta exacta], responde [respuesta clara y corta], sin decir 'quizás', 'probablemente', 'depende'.\n   ✅ Ejemplo: "Cuando preguntan '¿sin gluten?', responde 'Sí, tenemos pasteles sin gluten (sin harina de trigo). Puedes elegir chocolate o fruta.'"\n   ❌ Evita: "Quizás sí", "Depende de...", "Voy a ver".\n3. Prueba: Escribe una pregunta real que hayas recibido (ej.: "¿Tienen opción sin gluten?"), y lee la respuesta del prompt. ¿Suena como tú en WhatsApp? Si no, ajusta la frase (ej.: "Sí, tenemos" en vez de "Probablemente sí").\n``` | Diseño mínimo: título "Tu Asistente de IA para tu Startup (sin código)", 3 pasos con ✅/❌ ejemplos, espacio para "Pregunta exacta:", "Mi prompt:", "Pregunta que probé:", "Respuesta ajustada:". Imprime en papel normal o en tarjetas pequeñas. |
| **Tarjetas de herramientas (2 por mesa)** | 30 tarjetas pequeñas (ej. 10x15 cm) | Muestra visual sencilla de cómo usar Botsonic Free y Google Forms + ChatGPT (solo 2 pasos: "Pega el prompt → Usa el bot/Form"). Incluye enlace QR + texto corto: "Botsonic: gratis hasta 100 respuestas/mes. Pega tu prompt → genera respuesta → usa en WhatsApp. No necesitas código. Google Forms: escribe el prompt en la descripción del Form → respuestas automáticas usan tu frase. ¡Empieza con lo que ya usas (WhatsApp o Form)!". | En una tarjeta: <br>**Botsonic Free** <br>1. Ve a botsonic.com → "Crear bot gratis" <br>2. Pega tu prompt (ej. "Cuando preguntan '¿sin gluten?', responde...") <br>3. Usa el bot en WhatsApp (link que da Botsonic). <br>QR al enlace botsonic.com/free <br>**Google Forms + ChatGPT** <br>1. Crea un Form simple (pregunta: "¿Preguntas sobre horarios?") <br>2. En "Descripción", pega tu prompt <br>3. Activa "Respuestas automáticas" → el Form responde con tu frase. <br>QR a una página sencilla con pasos (ej. google.forms.example/start) <br>*(Nota: los QR son reales pero el enlace puede ser un placeholder sencillo como "botsonic.com/demo" si no quieres configurar QR ahora; el texto explica claramente.)* |
| **Sticky notes pequeños (2 colores)** | ~40 (ej. amarillo + azul)          | Para feedback rápido ("1 palabra que mejor describe el workshop + 1 palabra que aún les costaría"). Facilitador los pone en una pared o hoja grande. | Preparar sobre mesa; usar notas adhesivas pequeñas fáciles de pegar. |
| **"One Step Kit" PDF (1 página)** | Digital (enviar por email después) + imprimir opcional | Contenido simple: <br>- Los 3 pasos + template (repetido claro) <br>- "Mi uno paso para mañana": *"Mañana, al recibir la pregunta frecuente (ej. '¿Sin gluten?'), respondo en WhatsApp: 'Gracias por preguntar! Sí, tenemos pasteles sin gluten (sin harina de trigo). Puedes elegir chocolate o fruta.' (Usa tu prompt ya escrito)."* <br>- Lista de 2 herramientas con enlaces (Botsonic free, Google Forms tip) <br>- "Evita decir: 'quizás', 'depende', 'voy a ver' → Usa: 'Sí', 'No', 'Así funciona nuestro proceso'." <br>- "Prueba en 5 minutos: Pega tu prompt en WhatsApp o en el Form. ¡Listo!" | Diseño limpio: título, 3 pasos, "One step para mañana" en negrita, lista de evitar/usar en bullet points. Tamaño A4, una página. Generar en Canva rápido (ejemplo de texto incluido arriba). |
| **Pizarra/Proyector + Slides simples (máx. 8)** | Digital                                     | Slides solo con texto claro, ejemplos visuales (ej. foto de panadería realista, no diagramas). Nada de fórmulas. | Slide 1: Título + "Hoy construimos tu asistente de IA en 30 minutos, sin código" (imagen sencilla de persona sonriendo respondiendo en WhatsApp). <br>Slide 2: Icebreaker ejemplo ("PanCaliente: '¿Sin gluten?' 30 veces/semana"). <br>Slide 3: Demo paso a paso (ejemplo texto del prompt + respuesta automática). <br>Slide 4: 3 pasos + template (con ✅/❌ ejemplos). <br>Slide 5: Hoja de template (imprimible, mostrar contenido). <br>Slide 6: Herramientas (Botsonic + Google Forms, con QR y 2 pasos). <br>Slide 7: "Uno paso para mañana" (ejemplo de WhatsApp). <br>Slide 8: Recursos + contacto breve ("WhatsApp [tu número] para ejemplos en 24h"). | **Ningún slide con más de 6 palabras por línea. Usar tipografía grande (≥24pt). Evitar colores oscuros sobre fondo oscuro.** |
| **Lista de preguntas frecuentes (para facilitador)** | Digital (en móvil)                     | Preparar 3-4 respuestas rápidas para Q&A comunes (ej.: "¿Necesito pagar?", "¿Por qué no usar X?", "¿Tengo que entrenar el modelo?"). Respuestas en ≤60 sec. | Ejemplo: <br>- "¿Necesito pagar ahora?" → "No. Botsonic free es gratis hasta 100 respuestas/mes (suficiente para empezar). Google Forms también es gratis. Paga solo si creces mucho después." <br>- "¿Por qué no usar otra herramienta?" → "Hoy quieres usar lo que ya tienes (WhatsApp o tu Form). No buscar otra ahora. Usa tu prompt ya escrito. Después, si quieres probar otra, ya sabes cómo: pega el prompt. Así evitas perder tiempo buscando." <br>- "¿Tengo que programar?" → "No. Solo escribes la frase clara (como en la hoja). La herramienta (Botsonic o Form) pega esa frase y responde. No tocas código." | Listo en móvil; facilitador solo busca y dice la respuesta corta. |
| **Feedback sticky note sheet** | 1 hoja grande o pizarra para pegar sticky notes | Para que todos pongan sus palabras de feedback (1 palabra mejor + 1 palabra que aún les costaría). | Preparar en mesa; facilitador explica en 30 sec: "Escribe 1 palabra que mejor describa el workshop (ej. 'rápido') y 1 palabra que aún te costaría (ej. 'ajustar frase'). Pega aquí. ¡Gracias!" |

> ✅ **Todo está listo antes del workshop**: Hojas de template impresas, tarjetas de herramientas impresas, PDF "One Step Kit" listo (enviar por email al final), sticky notes sobre la mesa, slides cargados, lista de preguntas en móvil. *Nada que preparar en el momento.*

---

### ✅ 3. Para cada bloque: Titulo, duración, objetivo, dinámica, key takeaway (resumen en lenguaje hablado)

*(Repetido aquí para claridad, pero ya está en la agenda; incluye cómo decirlo en voz alta)*

- **¡Bienvenida + Icebreaker rápido! (0:00–0:10, 10 min)**  
  *Objetivo:* Que todos compartan una frase real corta (startup + pregunta frecuente) para conectar y ver que es común.  
  *Dinámica:* En pares (20 sec cada uno), luego 2 personas comparten 1 frase en grupo (30 sec total). Facilitador dice: "¡Sí! Eso es exactamente lo que vamos a resolver hoy." (Nada de charla larga).  
  *Key takeaway (decir en voz alta):* "Todos tienen una pregunta frecuente real. Esa es la base. No inventamos nada."

- **Por qué un asistente de IA para ti + Demo ultra-simple (0:10–0:25, 15 min)**  
  *Objetivo:* Mostrar que es útil, rápido y no requiere técnica. Usar historia real corta.  
  *Dinámica:* Historia de panadería (30 sec), demo en vivo súper corta (3 min: escribir prompt → ver respuesta), explicar en 1 frase ("Escribí una frase clara, probé una pregunta real, listo"). Preguntas rápidas en grupo (responder en 1 frase).  
  *Key takeaway (decir):* "Un asistente de IA para tu startup = escribir una frase clara para una pregunta real + probarla una vez. No programar nada."

- **Los 3 pasos realistas + Template listo (0:25–0:40, 15 min)**  
  *Objetivo:* Dar un proceso de 3 pasos muy concreto que puedan usar ahora mismo.  
  *Dinámica:* Mostrar slide con 3 pasos + template (ejemplo con ✅/❌), cada persona escribe su prompt en su hoja en silencio (3 min), facilitador anda preguntando "¿Suena como tú en WhatsApp?" en 1 min por mesa. Compartir rápido en pares.  
  *Key takeaway (decir):* "Escribe: 'Cuando [pregunta exacta], responde [respuesta clara], sin decir ‘quizás’. Prueba con una pregunta real que ya hayas recibido."

- **Ejercicio principal (todos lo hacen) (0:40–1:40, 60 min)**  
  *Objetivo:* Que cada uno escriba, pruebe, ajuste su prompt usando su startup real, con feedback rápido.  
  *Dinámica:* Pares escriben prompt (5 min), prueban con 3 preguntas reales en papel (15 min), ajustan usando "¿Suena como tú?", comparten en otro par (10 min), facilitador corrige rápidamente "quizás" → "sí/no" (10 min). *Ninguno queda sin hacer nada.*  
  *Key takeaway (decir):* "Mi asistente de IA es mi frase clara + probar con una pregunta real. Si suena como mi voz, listo. Ajusta solo ‘quizás’ → ‘sí’ o ‘no’."

- **Herramientas reales + Cómo empezar HOY (1:40–1:55, 15 min)**  
  *Objetivo:* Mostrar 2 opciones simples (Botsonic free / Google Forms) sin registro largo, enfatizar "comenzar con lo que ya usas".  
  *Dinámica:* Mostrar 2 pantallazas (5 min), explicar 3 pasos de uso ("Pega el prompt → Usa WhatsApp o Form"), responder "¿Necesito pagar?" con "No para empezar", usar ejemplos visuales.  
  *Key takeaway (decir):* "Empieza HOY con tu prompt ya escrito. Usa WhatsApp o tu Form existente. No busques otra herramienta ahora."

- **"Uno paso para mañana" + Q&A rápido (1:55–2:20, 25 min)**  
  *Objetivo:* Que cada persona se comprometa con un solo, pequeño acción real para usar su prompt mañana. Resolver preguntas en ≤60 sec.  
  *Dinámica:* Escribir "Mañana haré..." en 2 min (silencio), compartir 1 frase de 10 sec en pares, Q&A con regla de 60 sec por pregunta, cierre energético con frase "Mañana responderé con mi frase".  
  *Key takeaway (decir):* "Mañana, al recibir la pregunta frecuente, respondo con mi frase clara en WhatsApp o email. Listo."

- **Recursos para llevar + Feedback + Cierre (2:20–3:00, 40 min)**  
  *Objetivo:* Entregar lo útil que pueden usar inmediatamente; recolectar feedback simple; cerrar con acción clara.  
  *Dinámica:* Entregar hoja + PDF + tarjeta, pegar sticky notes de feedback, cierre con "¡Éxito! Responde con tu frase mañana", enviar recursos por email.  
  *Key takeaway (decir):* "Mi asistente de IA = mi frase clara + usarla mañana. Recursos en mi hoja. ¡Vamos a responder!"

---

### ✅ 4. Ejercicio principal del workshop (qué hacen todos, por qué funciona)

> **"Escribe tu prompt + prueba con una pregunta real en papel (no en computadora). Ajusta solo 'quizás' → 'sí/no' usando tu lenguaje natural. Comparte tu prompt final con otro par en 2 minutos y di: 'Mi prompt dice X, probé con Y y la respuesta es Z'. Lista la frase final en tu hoja."**

*¿Por qué funciona para no-tecnicos?*  
- Usa papel y lápiz (nada digital que asuste).  
- Solo 3 pasos claros (define → escribe frase → prueba con 1 pregunta real).  
- Feedback rápido y concreto ("¿Suena como tú en WhatsApp?" en 10-15 segundos).  
- No se menciona "modelo", "API", "entrenamiento". Solo "escribe una frase clara".  
- Cada persona ve su propio ajuste (ej. cambiar "quizás sí" → "sí") en contexto real (ej. "¿Sin gluten?" → respuesta "Sí, tenemos pasteles sin gluten...").  
- Se comparte en pares pequeños (no en grupo grande), así todos hablan y ven un ejemplo.  
- El objetivo es *usar la frase mañana*, no crear un producto. Por eso todos pueden hacerlo en 60 min.

> *Ejemplo real en el workshop:*  
> - Emprendedora de moda callejera: "Pregunta frecuente: '¿Tienen ropa para primavera?'"  
> - Primer intento: "Tal vez sí, depende de la temporada." (❌ tiene "tal vez", "depende")  
> - Ajuste con feedback: "Sí, tenemos prendas frescas para primavera (camisas ligeras, colores claros). Puedes ver el look en Instagram." (✅ clara, sin "tal vez", suena como ella)  
> - Prueba: Cliente escribe "¿Tienen ropa para primavera este mes?" → Respuesta del prompt: "Sí, tenemos prendas frescas para primavera (camisas ligeras, colores claros). Puedes ver el look en Instagram." → Suena natural. ¡Listo para usar en WhatsApp mañana!

---

### ✅ 5. Recursos para llevar a casa (qué entregar, cómo presentarlo)

Cada persona recibe **una hoja impresa** (Hoja de Template) + el **"One Step Kit" PDF** (1 página) + la **tarjeta de herramientas** (pequeña, con QR y 2 pasos). En el momento de entrega (2:20–2:40), el facilitador dice:

> *"Toma esta hoja. Ponla en tu bloc o en el celular. Cuando recibas la próxima pregunta frecuente (ej. '¿Sin gluten?' o '¿Horarios?'), abre la hoja, escribe tu prompt usando los 3 pasos (1 frase clara), prueba mentalmente con la pregunta que recibas, y responde en WhatsApp o email con esa frase. Eso es todo hoy. No necesitas recordar nada más. El PDF y la tarjeta están en tu email (envío en 5 min) con los enlaces exactos. Si quieres ver 2 ejemplos reales de otros emprendedores usando esto (¡solo 1 minuto!), mándame un WhatsApp a [tu número breve] y te mando los ejemplos en 24h. ¡Éxito con tu primera respuesta usando tu frase!"*

**Contenido del PDF "One Step Kit" (1 página, texto exacto para imprimir):**

> **¡Tu Asistente de IA para tu Startup (sin código)!**  
> *(Usa esto HOY)*  
>   
> **1. Define la pregunta exacta que te mandan**  
> *Ejemplo real: "¿Sin gluten?" (NO "pregunta sobre gluten").*  
> *Escribe solo la frase que el cliente usa: "¿Tienen opción sin gluten?"*  
>   
> **2. Escribe tu prompt (¡solo 1 frase!):**  
> *"Cuando [pregunta exacta], responde [respuesta clara y corta], sin decir 'quizás', 'probablemente', 'depende'."*  
> *✅ Ejemplo: "Cuando preguntan '¿sin gluten?', responde 'Sí, tenemos pasteles sin gluten (sin harina de trigo). Puedes elegir chocolate o fruta'."*  
> *❌ Evita: "Quizás sí", "Depende de...", "Voy a ver" → Usa siempre: "Sí", "No", o "Así funciona nuestro proceso".*  
>   
> **3. Prueba en 2 minutos (con papel):**  
> - Escribe 1 pregunta real que hayas recibido (ej. "¿Tienen opción sin gluten?").  
> - Lee tu respuesta del prompt: *"Sí, tenemos pasteles sin gluten..."*. ¿Suena como tú en WhatsApp o en un mensaje? Si dice "quizás", cámbialo por "Sí" o "No". ¡Ajusta solo eso!  
>   
> **¡Tu ONE STEP PARA MAÑANA!**  
> *Ejemplo: "Mañana, cuando un cliente me mande '¿Sin gluten?', respondo en WhatsApp: 'Gracias por preguntar! Sí, tenemos pasteles sin gluten (sin harina de trigo). Puedes elegir chocolate o fruta.' (Usa tu prompt ya escrito). Listo."*  
>   
> **Herramientas para empezar HOY (elige la que ya usas):**  
> - **WhatsApp:** Usa tu prompt directamente en el mensaje de respuesta (ej. escribe la frase del prompt). *Ninguna app extra.*  
> - **Google Forms (si usas un Form para preguntas):** En la descripción del Form, pega tu prompt (ej. "Cuando preguntan '¿sin gluten?', responde..."). Activa "Respuestas automáticas". ¡Listo! (No necesitas código).  
> - *Botsonic Free (opcional):* Si quieres un bot simple para WhatsApp, ve a [botsonic.com/free], pega tu prompt y usa el bot en WhatsApp. Gratis hasta 100 respuestas/mes. *(Link QR en tarjeta)*.  
>   
> **Recuerda:**  
> *No busques otra herramienta ahora. Usa lo que ya tienes (WhatsApp o tu Form). Escribe tu frase clara, prueba con 1 pregunta real, y responde mañana. ¡Eso es tu asistente de IA!*  
>   
> *¿Preguntas? WhatsApp [tu número breve] en 24h te mandaré 2 ejemplos reales (1 minuto cada uno). ¡Éxito!*

> *El PDF es una página A4, tipografía clara (ej. Arial 14pt), con íconos simples (✅/❌) y ejemplos reales. No hay tecnicismos. Se envía por email al final del workshop (mensaje corto: "¡Gracias por venir! Aquí está tu 'One Step Kit' + tarjeta. Usa tu frase mañana. ¿Alguna pregunta? WhatsApp [número]. ¡Éxito!")*

---

### ✅ 6. Slide count estimado por sección (total ~8 slides, muy simples)

| Sección                  | Slides estimados | Contenido mínimo (ejemplo de texto en slide)                                  | Por qué tan pocos |
|---------------------------|-------------------|-----------------------------------------------------------------------------|-------------------|
| Bienvenida + Icebreaker | 1                 | "¡Hola! Hoy construimos tu asistente de IA en 30 min, sin código. Compartan: 'Mi startup es X y la pregunta más frecuente que me mandan es ______.' (20 sec por par)" | Evita charla; usa frase corta + acción |
| Por qué + Demo          | 2                 | Slide 1: "PanCaliente: '¿Sin gluten?' 30 veces/semana (foto sencilla)". Slide 2: "Demo: Prompt → 'Cuando preguntan '¿sin gluten?', responde 'Sí, tenemos pasteles sin gluten...'. Respuesta automática (ejemplo texto). ¡No hay código!" | Solo historia + demo visual corta; no explicar cómo funciona |
| 3 pasos + Template     | 1                 | "3 pasos claros:<br>1. Define la pregunta exacta (ej. '¿Sin gluten?')<br>2. Escribe: 'Cuando [pregunta], responde [respuesta clara], sin decir 'quizás''<br>3. Prueba con 1 pregunta real (ej. '¿Tienen opción sin gluten?').<br>✅ Ejemplo: 'Sí, tenemos pasteles sin gluten...' ❌ Evita 'quizás'." | Todo en 1 slide, con ✅/❌ visuales; no repetir |
| Ejercicio principal intro | 1                 | "Ahora: En pares, usa tu hoja. Escribe tu prompt (3 min), prueba con 3 preguntas reales (15 min), ajusta solo 'quizás' → 'sí'. Comparte con otro par en 2 min. Facilitador anda preguntando: '¿Suena como tú en WhatsApp?'." | Instrucción clara y paso a paso; no teoría |
| Herramientas            | 1                 | "Botsonic Free: Pega prompt → Usa en WhatsApp (gratis hasta 100 respuestas). Google Forms: Pega prompt en descripción → Respuesta automática. ¡Usa lo que ya tienes (WhatsApp o Form)! No necesitas registrarte ahora." + QR pequeño | Solo 2 opciones + 2 pasos; no detalles técnicos |
| "Uno paso para mañana" | 1                 | "Mañana: Al recibir '¿Sin gluten?', responde en WhatsApp: 'Gracias por preguntar! Sí, tenemos pasteles sin gluten...'. Listo. (Ejemplo real)" | Frase exacta que pueden usar; refuerza acción |
| Recursos + Cierre       | 1                 | "Recursos: Hoja + PDF + Tarjeta. ONE STEP: 'Mañana responderé con mi frase'. Feedback: ¿1 palabra que mejor describe el workshop? (sticky note). WhatsApp [número] para ejemplos en 24h. ¡Éxito! Sonríe." | Resumen rápido + acción + contacto sencillo |
| **Total slides**       | **~6-8**         | *Máximo 8 slides. Cada slide ≤ 6 líneas, tipografía grande. Nada de diagramas o texto denso.* | Evita saturar; facilitador habla, slide refuerza visualmente. |

> *Nota práctica:* El facilitador **no lee los slides**; usa el texto como guía. Habla desde el corazón con ejemplos reales. Los slides son solo apoyo visual (ej. ejemplos de prompt, QR, ✅/❌). Así se mantiene energía y enfoque en la acción.

---

### ✨ Por qué este outline funciona para emprendedores early-stage no-tecnicos

- **Nada de tecnicismos:** Nada de "modelo", "API", "fine-tuning", "generativo". Solo "escribe una frase clara", "prueba con una pregunta real", "dilo como tú lo dirías en WhatsApp".
- **Acción concreta desde el primer minuto:** Icebreaker usa su propia frase real; el ejercicio usa papel y 3 preguntas reales; "One step para mañana" es una frase exacta para usar mañana.
- **Retroalimentación rápida y útil:** "¿Suena como tú en WhatsApp?" en 10-15 segundos; corrección rápida de "quizás" → "sí" (no teoría sobre precisión del modelo).
- **Herramientas minimizadas:** Solo 2 opciones reales (WhatsApp + Form), ambas usando lo que ya tienen; "gratis hasta 100 respuestas" es claro; no se menciona precios ni pasos de configuración largos.
- **Tiempo realista:** El ejercicio principal (60 min) está bien distribuido: escribir (20 min), probar/ajustar (30 min), compartir/ajustar final (10 min). No hay bloqueo de 45 min de escritura.
- **Tono energético y cercano:** Frases como "¡Sí!", "Listo", "Éxito!", "Usa lo que ya tienes", "En 30 minutos", "Mañana responderás...", evitar "deberían", "es recomendable". El facilitador usa gestos simples (levantar la mano en cierre).
- **Recursos ultra-usables:** Hoja + PDF de 1 página + tarjeta = fácil de guardar y usar. Email con "One Step Kit" y contacto breve para ejemplos en 24h (no promesa de soporte constante).
- **Feedback simple:** 1 palabra + sticky note = fácil de hacer en 1 min, útil para mejorar sin sobrecargar.

> ✅ **En resumen para el facilitador (lo que decir al inicio y al final):**  
> *Al inicio (0:00):* "¡Hola a todos! Soy [Nombre], emprendedor también hace 2 años, y usé esto mismo para responder preguntas de horarios a mi cafetería. Hoy no vamos a hablar de tecnología complicada. Vamos a escribir una frase clara para la pregunta que más te mandan (ej. '¿Sin gluten?'), probarla con una pregunta real que hayas recibido, y usarla mañana en WhatsApp. Todo en 30 minutos de práctica. Si tienes duda, di '¡Claro!' y te respondo en 60 segundos. ¡Vamos!"  
> *Al final (2:55–3:00):* "Hoy escribiste tu frase clara. Mañana, cuando alguien te mande '¿Sin gluten?', escribes: 'Gracias por preguntar! Sí, tenemos pasteles sin gluten (sin harina de trigo)...'. ¡Listo! No más buscar respuestas. Recibe tu hoja y PDF, mándame un WhatsApp a [número] si quieres ver 2 ejemplos reales (te mandaré en 24h, 1 minuto cada uno). ¡Gracias por compartir su pregunta y por empezar hoy! Ahora ve a responder esa primera pregunta con tu frase. ¡Éxito!"

Este outline es **práctico, rápido, sin sobrecarga**, y cada paso lleva directamente al emprendedor a usar su asistente de IA *en su día a día* mañana mismo. ¡Listo para implementar hoy mismo en un taller presencial! 🚀