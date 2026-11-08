# Granite 4.2 8B — startup_content/workshop_outline

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 140.237s | tokens_per_second: 62.4
- input_tokens: 224 | output_tokens: 8751
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una agenda detallada y ejercicios prácticos que son directamente aplicables para emprendedores no técnicos, con un enfoque en la utilidad práctica y la profundidad en la explicación de cómo automatizar tareas específicas.

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

¡Claro! Aquí tienes un **outline completo, práctico, energético y sin tecnicismos** para un workshop presencial de **3 horas** titulado:  
**"Construye tu Asistente de IA para tu Startup – Workshop Práctico"**, dirigido a emprendedores early-stage **no técnicos (20–30 personas)**.  

El tono es claro, cercano, motivador y enfocado en acción: *“Hoy haremos algo real, sin jerga, sin código que no entiendes”.*  

---

### ✅ **Resumen rápido del enfoque**  
- **Ningún código que escriban.** Usamos una herramienta visual y de un clic (Make.com + IA generativa integrada).  
- **Todo en español.** Nada de inglés técnico.  
- **Enfoque en su problema real:** ¿Qué tarea repetitiva les consume tiempo en la startup? (ej. enviar correos de seguimiento, armar resúmenes de llamadas, responder preguntas frecuentes).  
- **Resultado tangible al final:** Cada emprendedor lleva un "asistente de IA" listo para usar (un flujo automático que hace su tarea más rápida).  

> *Ejemplo real usado en la charla:* “Si vendes cursos online y pierdes tiempo escribiendo correos de seguimiento para quienes no responden, hoy construirás un asistente que envíe ese correo automáticamente 2 días después de que la persona no responde.”

---

### 📅 **Agenda detallada (3 horas exactas, con pausas naturales)**  

| Tiempo | Bloque | Duración | Objetivo | Dinámica | Key Takeaway (1 frase clara) |
|---------|--------|----------|----------|----------|-----------------------------|
| 0:00 – 0:10 | **¡Bienvenidos + Por qué hoy es útil!** | 10 min | Que entiendan *inmediatamente* por qué vale la pena usar IA para ellos (no “futuro”, sino *ahora*). | **Demo rápida + historia real corta** (ej. emprendedor que ahorró 5 horas/semana con un asistente de IA para correos de seguimiento). Pregunta abierta: *“¿Qué tarea te cuesta tiempo repetir esta semana?”* (escritorio, chat, correos). Escucha 2–3 respuestas rápidas en grupo. | *“No necesitas ser técnico para usar IA para automatizar tu tarea más repetitiva y cansadora.”* |
| 0:10 – 0:25 | **Entender tu “problema de fondo” (no la IA)** | 15 min | Que identifiquen *exactamente* la tarea que quieren automatizar (ej. “Escribir el correo de seguimiento para clientes que no responden”). | **Ejercicio rápido en parejas (5 min):** Cada pareja escribe en una hoja: (1) La tarea (ej. “Enviar correo de seguimiento”), (2) Cuándo la hacen (ej. “Después de 2 días sin respuesta”), (3) Qué les cuesta (ej. “Pierdo tiempo escribiéndolo cada vez”). (4) ¿Qué respondería idealmente? (ej. “Corto, amable, con llamada a acción”). Luego, comparten 1 frase por pareja en grupo (5 min). | *“Define la tarea como: ‘Enviar [qué] cuando [cuándo] porque [qué cuesta].’ Así la IA entiende exactamente qué hacer.”* |
| 0:25 – 0:45 | **Construye tu asistente paso a paso (demo + práctica guiada)** | 20 min | Que vean cómo crear el flujo en <5 minutos usando una herramienta visual (Make.com + IA generativa integrada). | **Demo en vivo (5 min):** Mostrar el flujo en Make.com: (1) Trigger = “Nuevo correo sin respuesta después de 2 días”, (2) Acción = “Usar IA para escribir el correo (plantilla simple + contexto de la tarea)”, (3) Enviar correo. Explicar cada paso en 1 frase: *“El disparador es la señal (ej. no respondió), la IA escribe el texto (no tú), y se envía.”* <br> **Práctica guiada en grupo (15 min):** Cada emprendedor (en su laptop o tablet que ya está lista) replica el flujo con *su propia tarea* (usando sus respuestas del ejercicio). Yo circulo, ayudo con 1 frase: *“¿Qué es la señal? (ej. no respondió), ¿qué quieres que diga el correo? (ej. ‘Hola, solo recordando…’)”. No hay preguntas técnicas; solo guía paso a paso. Usa tarjetas físicas con pasos visuales (Trigger → IA escribe → Enviar). | *“Tu asistente se activa solo cuando ocurre la señal (ej. no respondió), y la IA escribe el texto para ti. Tú solo revisas y envías.”* |
| 0:45 – 0:55 | **Pausa activa + micro-ajuste (¡práctica rápida!)** | 10 min | Que prueben el flujo con un caso real pequeño (ej. enviar el correo de seguimiento a 1 cliente de prueba). | **Ejercicio micro (5 min):** Cada uno usa su flujo recién creado para enviar el correo a un cliente ficticio (ej. “Hola Juan, solo recordando mi curso…”). En 2 min, escriben el correo *con la IA* (en la herramienta), lo revisan 30 segundos y lo envían a su propio correo de prueba (ej. su Gmail). <br> **Discusión rápida (5 min):** “¿Qué salió bien? ¿Qué cambiarías en 1 frase?” (ej. “La IA escribió demasiado largo”, “Quería más amable”). Yo anoto 1 mejora común en la pizarra. | *“Prueba el flujo con un caso real pequeño (1 cliente) antes de usarlo con todos. Así ajustas en 2 minutos, no después.”* |
| 0:55 – 1:20 | **Ejercicio principal del workshop (¡todo el grupo hace lo mismo!)** | 25 min | Que construyan *su propio asistente de IA funcional* para su tarea real, con ajuste rápido. | **Ejercicio principal (estructurado pero simple, 20 min):** <br> 1. **Elegir su tarea** (usar la plantilla: “Enviar [qué] cuando [cuándo] porque [qué cuesta]”). <br> 2. **Crear el flujo en Make.com** (guía visual en tarjeta: Trigger → IA escribe → Enviar). Usar la IA de Make.com para “Escribe un correo corto y amable” (ej. “Escribe el correo de seguimiento para un cliente que no respondió a mi oferta de curso”). <br> 3. **Probar con 1 cliente real (o ficticio pero creíble)**: enviar el correo generado a su propio Gmail de prueba. <br> 4. **Ajustar en 2 minutos**: revisar el texto generado, cambiar 1 frase si falta claridad o tono (ej. “En lugar de ‘¿Te interesa?’, digo ‘¿Te gustaría probar el primer capítulo gratis?’”). <br> **Yo como facilitador circulo**, cada 2 min respondo solo 1 pregunta por persona: *“¿Qué es la señal?”, “¿Qué quieres que diga el correo?”, “¿Qué cambiarías en 1 frase?”*. No explico herramientas; solo guío con preguntas. <br> **Fin del ejercicio (5 min):** Cada uno dice en 15 segundos: *“Mi asistente hace: [tarea] cuando [señal], y yo solo reviso y envío.”* | *“Tu asistente se activa solo cuando ocurre la señal (ej. no respondió), escribe el texto con IA, y tú solo lo revisas en 30 segundos. Listo para usar hoy.”* |
| 1:20 – 1:35 | **Compartir & aprender rápido (ritmo rápido, sin charla larga)** | 15 min | Que vean que otros emprendedores tienen problemas similares y soluciones simples. | **Ronda de 2 minutos por persona (max 5 personas para no cansar):** Cada uno dice: (1) Su tarea, (2) La señal (ej. “no respondió en 2 días”), (3) La mejora que hizo en 1 frase (ej. “Cambié ‘¿Te interesa?’ por ‘¿Te gustaría probar el primer capítulo gratis?’”). Yo anoto en pizarra 3 patrones comunes (ej. “Usar ‘probar gratis’ en llamadas a acción”, “Mencionar nombre del cliente”). <br> **Resumen rápido de patrones (5 min):** “Muchos dicen ‘¿Te interesa?’ → mejor ‘¿Te gustaría probar X gratis?’ porque suena menos presionante. Muchos olvidan decir ‘Hola [nombre]’ → añade calidez. Así, la IA escribe mejor si le das 1 frase clara como guía.” | *“Escucha cómo otros ajustaron 1 frase: ‘probar gratis’ > ‘¿Te interesa?’. Usa esa frase simple para que tu asistente suene natural.”* |
| 1:35 – 1:50 | **¿Qué hacer HOY? (Plan de acción concreto en 3 pasos)** | 15 min | Que tengan un plan claro y realista para usar el asistente en los próximos 3 días. | **Ejercicio de acción (10 min):** En su hoja de trabajo (entregada al inicio), completan: <br> 1. **Mi tarea:** “Enviar [ej. correo de seguimiento] cuando [ej. no respondió en 2 días]”. <br> 2. **Mi señal clara:** “Cliente no respondió después de 2 días”. <br> 3. **Mi frase de ajuste (1 frase):** “Ejemplo: ‘Hola [nombre], solo recordando mi curso y te invito a probar el primer capítulo gratis sin compromiso.’” <br> 4. **Mi primer paso HOY (ej. ‘Hoy mismo, crear el flujo en Make.com usando mi tarea y la frase de ajuste; enviar el correo a mi cliente de prueba en 10 min’).” <br> **Discusión rápida (5 min):** Cada uno dice su “primer paso HOY” en 10 segundos. Yo resumo en la pizarra: *“Hoy: crear flujo → enviar a 1 cliente de prueba → revisar 30 seg.”* | *“No esperes a que esté perfecto. Usa el flujo hoy mismo con 1 cliente (real o de prueba), revisa 30 segundos y envía. Eso es todo para empezar.”* |
| 1:50 – 2:00 | **Preguntas rápidas + próximos pasos claros** | 10 min | Que salgan con claridad sobre qué hacer, dónde encontrar ayuda y qué evitar. | **Preguntas en grupo (5 min):** Recoger 2–3 preguntas más comunes (ej. “¿Necesito pagar algo?”, “¿Cómo conecto mi Gmail?”). Respuestas en 1 frase: *“Make.com tiene versión gratuita para hasta 100 flujos/mes; no necesitas pagar para empezar. Conectas tu Gmail con 2 clics en la app.”* <br> **Próximos pasos claros (5 min):** <br> - **Hoy mismo:** Crear el flujo en Make.com usando su hoja de acción (3 pasos). <br> - **En 2 días:** Enviar el correo de prueba a 1 cliente real (o a un amigo que simule no responder). <br> - **Recursos para llevar:** Enlace al tutorial visual (enlace sencillo), hoja de acción impresa, lista de 3 frases de ajuste (ej. “probar gratis”, “sin compromiso”, “Hola [nombre]”). <br> - **¿Ayuda?** Si se atascan, usar el grupo de WhatsApp del workshop (link en hoja) o escribir a [tu nombre] en 24h (ej. “Hola, mi flujo no envía, ¿qué hago?”). | *“Hoy crea el flujo. En 2 días prueba con 1 cliente. Usa la hoja y el enlace. Si te atascas, escribe en el grupo de WhatsApp – te respondo en menos de 24h.”* |
| 2:00 – 3:00 | **Cierre energético + compromiso concreto + agradecimiento** | 60 min | Que salgan motivados, con acción clara y sin sobrecarga. | **Cierre (10 min):** <br> - Yo comparto una historia muy corta (30 seg): *“Una emprendedora de cursos online usó este método hace 1 semana. En 3 días, envió 5 correos de seguimiento con IA, revisó 30 segundos cada uno y no perdió tiempo escribiendo. Ahorró 4 horas la semana. Hoy tú haces lo mismo.”* <br> - **Compromiso en grupo (5 min):** Cada uno dice en 10 segundos: *“Mi primer paso hoy será: [ej. ‘Crear el flujo en Make.com con mi frase de ajuste’].”* (Se escucha en círculo rápido, energía alta). <br> - **Entrega física (5 min):** Entregar cada persona su hoja de acción impresa (con los 3 pasos + patrones de frase + enlace sencillo), y una tarjeta “Mi asistente de IA” con: *“Tarea → Señal → Frase de ajuste → Paso hoy”.* <br> - **Agradecimiento + llamado a compartir:** *“Si usas tu asistente en la próxima semana, escribe una frase corta en el grupo de WhatsApp: ‘¡Usé mi asistente y ahorré X minutos!’ – así te animamos a todos.”* <br> - **Pausa final ligera (5 min):** Café/bebida disponible, conversación informal (“¿Qué te gustó más? ¿Qué cambiarías?”). Yo circulo, escucho, agradezco. | *“Hoy construiste tu asistente de IA en 3 pasos: definir la tarea, usar la señal y ajustar 1 frase. Mañana, crea el flujo y envía a 1 cliente. Eso es todo para empezar.”* |

> *Nota sobre tiempo:* La pausa de 60 min al final incluye cierre, compromiso, entrega de materiales y conversación ligera. Es natural y evita que el workshop se sienta apresurado.

---

### 📦 **Materiales necesarios (preparar antes del workshop)**  

| Tipo | Detalle | Por qué |
|-------|---------|---------|
| **Herramienta visual** | Cuenta gratuita en [Make.com](https://www.make.com) para cada participante (crea cuentas previas con nombre de usuario simple como `emprendedor1@startup-ia.com`, etc., y comparte el enlace de inicio rápido). | Evita que los participantes tengan que crear cuentas en el momento. |
| **Plantilla visual de flujo (tarjeta impresa)** | 1 tarjeta por persona (formato A5 o tamaño de mano): <br> *“Trigger → IA escribe → Enviar”* con iconos simples (alarma para “señal”, lápiz para “IA escribe”, sobre para “Enviar”). Texto en español claro: “Dispara cuando ocurre [ej. no respondió], la IA escribe el texto, tú revisas y envías”. | Guía visual sin texto técnico; los ves alrededor de la mesa. |
| **Hoja de acción impresa (1 por persona)** | Tamaño carta o A5, con: <br> 1. Mi tarea: “Enviar ______ cuando ______ porque ______” <br> 2. Mi señal clara: “Cliente no respondió en ___ días” <br> 3. Mi frase de ajuste (ej. “Hola [nombre], solo recordando… y te invito a probar X gratis sin compromiso.”) <br> 4. Mi primer paso HOY (ej. “Hoy crear flujo en Make.com y enviar a 1 cliente de prueba”). <br> 5. Lista de 3 frases de ajuste rápidas (ej. “probar gratis”, “sin compromiso”, “Hola [nombre]”). | Todo en español sencillo; sirve como guía para el ejercicio principal y el plan de acción. |
| **Tarjeta “Mi asistente de IA” (impresa)** | Pequeña tarjeta (tipo post-it) con: <br> *“Tarea → Señal → Frase de ajuste → Paso hoy”* + ejemplo visual. | Llevar a casa, pegar en escritorio. Refuerza el mensaje. |
| **Enlaces simples (en la hoja y tarjeta)** | - Enlace directo a la guía visual de Make.com para flujos de correo (ej. `make.com/guia-correos-empresarios`). <br> - Enlace al grupo de WhatsApp del workshop (ej. `wa.link/startup-ia-grupo`). <br> - *No usar términos como “API”, “integración”, “workflow”.* Usar: “Crear el flujo”, “Enviar el correo”. | Acceso fácil sin confusión. |
| **Equipo técnico mínimo** | - 1 laptop + proyector para demo. <br> - 1 tableta o laptop extra para circulación (si hay más de 10 personas). <br> - Micrófono pequeño si el espacio es grande (>20). <br> - Café/bebida ligera (agua, té, algo dulce). | Para demo clara y poder ayudar en el ejercicio guiado. |
| **Preparación previa (24–48h antes)** | - Crear todas las cuentas Make.com con nombres simples y activar la conexión a Gmail (usar la opción “Conectar cuenta de Gmail” en Make.com). <br> - Probar el flujo con una tarea de prueba (ej. “Enviar correo de seguimiento” con IA) para asegurar que funcione en 3 pasos. <br> - Imprimir todas las tarjetas, hojas de acción y tarjetas “Mi asistente” (cantidad = número de participantes + 2 extras). <br> - Preparar la pizarra o papel grande con los 3 patrones de frase (ej. “probar gratis > ¿te interesa?”, “sin compromiso”, “Hola [nombre]”) listos para anotar. | Evita problemas técnicos en el momento y tiempo perdido. |

> ✅ *Importante:* Todas las cuentas de Make.com deben estar listas con Gmail conectado antes del workshop. No permitir que los participantes creen cuentas en el momento; así evitas perder tiempo.

---

### 🔥 **Ejercicio principal del workshop (lo que todos hacen, paso a paso)**  

> **Título del ejercicio:** *“Construye tu asistente de IA para tu tarea real en 20 minutos”*  

**Pasos (todos hacen exactamente esto, guiados por preguntas simples):**  
1. Usar su hoja de acción para completar: *“Enviar [tarea] cuando [señal] porque [costo]”* (ej. “Enviar correo de seguimiento cuando no respondió en 2 días porque pierdo tiempo escribiéndolo”).  
2. Ir a Make.com (en su cuenta ya creada), elegir “Crear flujo nuevo”, elegir trigger: *“Nuevo correo sin respuesta después de X días”* (Make.com tiene un disparador preconfigurado para “no respondió a correo” o usar “Fecha de última interacción” si es necesario; si no, usar “Enviar correo manual” como trigger simple para prueba). *Nota: En la práctica real, el disparador más simple para correos es “Cuando recibo un correo y no hay respuesta en X días” – Make.com lo tiene en la galería de flujos.* Si hay dudas, usar “Cuando recibo un correo” + “Verificar si hay respuesta” (con IA para detectar respuesta simple). *Para simplificar al máximo, usar trigger: “Nuevo correo en mi bandeja” + acción IA para escribir el correo de seguimiento; el “después de 2 días” se gestiona con una pequeña tabla en Make.com o se prueba con un correo de prueba (no es crítico que sea automático 2 días exactos para el ejercicio; se enfoca en el proceso).**  
3. En la acción, elegir “Usar IA para escribir texto”: escribir prompt simple como *“Escribe un correo corto y amable para un cliente que no respondió a mi oferta de curso. Incluye: saludo con nombre, recordatorio breve, invita a probar el primer capítulo gratis sin compromiso, y una llamada a acción clara.”* (esto es el prompt que ellos escriben con sus palabras; yo les doy este ejemplo en la demo).  
4. Enviar el correo a su propio Gmail (ej. `miemail@gmail.com`).  
5. En 2 minutos, abrir el correo generado, leerlo en voz alta, cambiar **solo 1 frase** si suena muy formal o confusa (ej. cambiar “¿Te interesa?” por “¿Te gustaría probar el primer capítulo gratis?”), y enviarlo a su cliente de prueba (puede ser su propio Gmail o un amigo que diga “no respondí”).  
6. En su hoja de acción, escribir: *“Mi primer paso HOY: Crear el flujo en Make.com con mi frase de ajuste y enviar a 1 cliente de prueba en 10 min.”*  

**Por qué funciona para no técnicos:**  
- No se enseña Make.com en profundidad; solo se usa 3 pasos visuales (Trigger → IA escribe → Enviar).  
- El prompt para IA es claro y usa lenguaje natural (“escribe un correo corto y amable…”).  
- El ajuste es solo 1 frase (no escribir de nuevo todo).  
- Se prueba con 1 cliente de prueba (no con todos los clientes reales de inmediato).  
- Todo se hace en la herramienta visual de Make.com (botones, no código).  

> *Ejemplo real usado en la demo:*  
> *Tarea:* “Enviar correo de seguimiento para clientes que no responden a mi curso online.”  
> *Señal:* “No respondió después de 2 días.”  
> *Prompt para IA:* “Escribe un correo corto y amable: ‘Hola [nombre], solo recordando mi curso online. No hay presión. ¿Te gustaría probar el primer capítulo gratis sin compromiso?’”  
> *Resultado generado por IA:* “Hola Juan, solo quería recordarte mi curso. ¿Te interesa?” → *Ajuste del emprendedor:* “¿Te gustaría probar el primer capítulo gratis sin compromiso?” (1 cambio, 10 segundos). *Listo.*

---

### 📚 **Recursos para llevar a casa (incluidos en hoja y tarjeta)**  

1. **Hoja de acción impresa** (ya incluida en materiales): con los 4 pasos y la frase de ajuste.  
2. **Tarjeta “Mi asistente de IA”** (pequeña, para el escritorio): *“Tarea → Señal → Frase de ajuste → Paso hoy”* + ejemplo.  
3. **Enlace sencillo** (en la hoja y tarjeta): `make.com/guia-correos-empresarios` (guía visual de 3 pasos en español, sin tecnicismos; incluye capturas de pantalla simples). *Ejemplo de texto en la guía:* “1. Haz clic en ‘Crear flujo’. 2. Elige ‘Nuevo correo en mi bandeja’ como disparador. 3. Elige ‘Usar IA para escribir texto’. 4. Escribe tu prompt como: ‘Escribe un correo corto y amable para [cliente] que no respondió…’. 5. Elige ‘Enviar a mi Gmail’. ¡Listo!”.  
4. **Grupo de WhatsApp para apoyo rápido** (link `wa.link/startup-ia-grupo`): para enviar preguntas como “Mi flujo no envía” o “¿Cómo digo ‘probar gratis’ mejor?”. *Yo respondo en menos de 24h.* (Yo como facilitador me comprometo a responder en 24h; no es un servicio profesional, es apoyo del workshop).  
5. **Lista de 3 frases de ajuste rápidas** (en la hoja):  
   > - “¿Te gustaría probar el primer capítulo **gratis** sin compromiso?” (en lugar de “¿Te interesa?”)  
   > - “Solo recordando, no hay prisas.” (en lugar de “¿Por qué no respondiste?”)  
   > - “Hola [nombre],” (siempre incluye el nombre al inicio).  
   > *Por qué: suena natural, no presionante, fácil de recordar.*  

> *No incluir en los recursos:* términos como “API”, “webhook”, “integración”, “workflow”, “prompt engineering”. Solo frases como “escribe un correo”, “elige ‘usar IA para escribir texto’”, “envía a mi Gmail”.

---

### 📊 **Slide count estimado por sección (total ~25–30 slides, muy visual, pocos textos)**  

| Sección | Slides | Contenido visual (ejemplo) | Texto mínimo (máx. 1 frase por slide) |
|----------|--------|---------------------------|--------------------------------------|
| 1. Bienvenidos + Por qué hoy (10 min) | 3 slides | - Slide 1: Foto amigable de emprendedores trabajando (no oficinas frías); texto: “¿Pierdes tiempo escribiendo correos de seguimiento? Hoy lo automatizas en 5 minutos.” <br> - Slide 2: Historia real corta (foto pequeña + 2 líneas: “María vendía cursos online. Perdía 5h/semana escribiendo correos. Usó IA en 1 día y ahorró tiempo.”) <br> - Slide 3: Pregunta abierta en pantalla: “¿Qué tarea te cuesta tiempo repetir esta semana? (Ej: enviar correo de seguimiento)” | Texto claro, sin tecnicismos. Usa iconos (alarma para “tarea”, reloj para “repetir”). |
| 2. Entender tu problema (15 min) | 3 slides | - Slide 1: Plantilla visual en pantalla: “Enviar [qué] cuando [cuándo] porque [qué cuesta]” + iconos (correo para “Enviar”, reloj para “cuándo”, reloj + gasto para “qué cuesta”). <br> - Slide 2: Ejemplo real en pantalla (ej. “Enviar correo de seguimiento cuando no respondió en 2 días porque pierdo tiempo escribiéndolo”). <br> - Slide 3: Resultado del ejercicio en parejas (ej. “María: enviar correo de seguimiento → cuando no respondió en 2 días → pierdo 1h/semana”). | Máximo 1 frase por slide. Usa colores suaves (azul claro, verde suave). |
| 3. Construye tu asistente (20 min) | 4 slides | - Slide 1: Flujo visual simple (3 bloques: Trigger → IA escribe → Enviar) con iconos y texto corto: “Dispara cuando ocurre [señal]”, “IA escribe el texto”, “Tú revisas y envías”. <br> - Slide 2: Demo en vivo (captura de pantalla simple de Make.com con los 3 pasos; no más detalles técnicos). Texto: “Hago clic aquí → escribe con IA → envío”. <br> - Slide 3: Guía de preguntas para guiar (ej. “¿Qué es la señal?”, “¿Qué quieres que diga el correo?”). Texto: “Pregúntate solo esto: ‘Cuándo ocurre esto?’ y ‘¿Qué quiero que diga el correo?’”. <br> - Slide 4: “No escribes el correo tú. La IA escribe. Tú solo revisas 30 segundos y envías.” (frase clave en negrita). | Evitar texto largo. Usar iconos y frases de 5–7 palabras. |
| 4. Pausa + micro-ajuste (10 min) | 1 slide | - Slide: “Prueba con 1 cliente ahora mismo → revisa 30 seg → envía”. Icono de correo + reloj de 30 seg. Texto: “Hazlo en 5 min. No esperes a usarlo con todos.” | Muy visual, solo acción. |
| 5. Ejercicio principal (25 min) | 2 slides | - Slide 1: “Tu turno: Usa tu hoja → Completa la plantilla → Crea el flujo en Make.com → Envía a 1 cliente de prueba (tu Gmail o un amigo)”. Texto: “20 min total. Yo te guío paso a paso.” <br> - Slide 2: “Ajusta solo 1 frase si suena formal o confusa. Ej: ‘¿Te interesa?’ → ‘¿Te gustaría probar el primer capítulo gratis?’”. | Guía clara, sin pasos extra. |
| 6. Compartir & patrones (15 min) | 3 slides | - Slide 1: 3 patrones comunes (ej. “probar gratis > ¿te interesa?”, “sin compromiso”, “Hola [nombre]”) con ejemplos reales de los participantes (anotados en pizarra; en slides se muestra como texto simple). <br> - Slide 2: Resumen rápido: “Escucha cómo otros ajustaron 1 frase. Usa eso para tu correo.” <br> - Slide 3: “¿Qué dijeron los 3 que compartieron?” (ej. “María cambió ‘¿Te interesa?’ por ‘¿Te gustaría probar gratis?’, Juan dijo ‘Hola Juan’ al inicio”). | Mostrar patrones reales de los participantes (no inventados). |
| 7. ¿Qué hacer HOY? (15 min) | 3 slides | - Slide 1: Hoja de acción en pantalla (ejemplo lleno: “Enviar correo de seguimiento cuando no respondió en 2 días porque pierdo tiempo; frase: ‘Hola [nombre], solo recordando… y te invito a probar el primer capítulo gratis sin compromiso.’”). <br> - Slide 2: “Mi primer paso HOY: Crear flujo en Make.com y enviar a 1 cliente de prueba en 10 min.” (texto claro). <br> - Slide 3: Próximos pasos en 3 puntos: “Hoy: crear flujo → En 2 días: enviar a 1 cliente real → Si te atascas: escribe en el grupo WhatsApp (link).” | Texto directo, sin jerga. |
| 8. Cierre energético (60 min) | 3 slides | - Slide 1: Historia corta de María (foto pequeña + 2 líneas: “Usó este método, ahorró 4h la semana, envió 5 correos en 10 min”). Texto: “Tú puedes hacer lo mismo hoy.” <br> - Slide 2: Compromiso en grupo (ej. “Mi primer paso hoy será: Crear el flujo en Make.com”). Pide que todos digan su compromiso en 10 segundos (en círculo). <br> - Slide 3: Recursos en pantalla: enlace `make.com/guia-correos`, link WhatsApp, tarjeta “Mi asistente”. Texto: “Lleva tu hoja. Usa el flujo hoy. Si te atascas, escribe en el grupo. ¡Te animamos!” | Visual cálido, tono animado. |
| **Total estimado** | **~25–30 slides** | Cada slide tiene máximo 1 frase clave + imagen/icono simple. No hay diapositivas llenas de texto. | ✅ Cumple con “tono energético y práctico”, sin academismo. |

> *Nota sobre slides:* No se usan diapositivas para explicar Make.com en detalle. Solo se muestran los 3 pasos del flujo (Trigger → IA escribe → Enviar) y el ejemplo de prompt. La demo en vivo es el momento clave; los slides son apoyo visual mínimo.

---

### ✅ **Por qué este outline funciona para emprendedores early-stage no técnicos**

- **Nada de código, nada de tecnicismos:** Usa siempre frases como “escribe el correo”, “elige ‘usar IA para escribir texto’”, “envía a tu Gmail”.  
- **Acción concreta desde el primer minuto:** Pregunta “¿Qué tarea te cuesta tiempo repetir esta semana?” → no teoría.  
- **Guía paso a paso con preguntas simples:** “¿Qué es la señal?”, “¿Qué quieres que diga el correo?”. Evita que piensen demasiado.  
- **Prueba pequeña primero:** Enviar el correo a 1 cliente de prueba (no a todos los clientes) → baja ansiedad, alta confianza.  
- **Ajuste de 1 frase:** Fácil de recordar y hacer (no reescribir todo). Usa ejemplos reales de los mismos emprendedores.  
- **Plan de acción claro en 3 pasos:** “Hoy crear flujo → En 2 días enviar a 1 cliente → Si te atascas, escribe en el grupo WhatsApp”. No “investigar más”, no “estudiar IA”.  
- **Recursos simples y listos para usar:** Enlace sencillo, hoja impresa, tarjeta para el escritorio. No PDFs largos.  
- **Tono energético pero real:** Historias cortas, frases como “¡Hoy lo haces en 5 minutos!”, “Prueba con 1 cliente ahora mismo”, “Te respondo en menos de 24h”. Evita frases como “revoluciona”, “transforma”, “innovación”. Usa “ahorras tiempo”, “hace tu tarea más fácil”, “envías el correo en 2 minutos”.  
- **Tiempo realista:** Las pausas naturales (pausa activa, micro-ajuste, compartir rápido) evitan que el grupo se canse. 3 horas se sienten fluidas.  
- **Facilitador como guía, no experto:** Yo no explico Make.com en detalle; guío con preguntas. Esto hace que los participantes se sientan capaces.

---

### 📌 **Resumen rápido para ti (para llevar en tu bolso)**

> **Título:** Construye tu Asistente de IA para tu Startup – Workshop Práctico (3 horas, no técnicos)  
> **Audiencia:** Emprendedores early-stage (20–30), sin experiencia técnica.  
> **Objetivo final:** Cada uno lleva un flujo de IA listo para usar (en Make.com) para automatizar su tarea repetitiva más cansadora (ej. correo de seguimiento), y un plan de acción claro (“Hoy crear flujo → En 2 días enviar a 1 cliente”).  
> **Clave del tono:** Energético, claro, sin palabras como “API”, “workflow”, “prompt engineering”. Usa frases como “escribe el correo”, “elige ‘usar IA para escribir texto’”, “revisa 30 segundos”.  
> **Materiales clave que preparar antes:** Cuentas Make.com listas con Gmail conectado, tarjetas de flujo visual, hoja de acción impresa, tarjeta “Mi asistente”, enlaces simples, grupo WhatsApp para apoyo.  
> **Ejercicio principal:** Todos completan su hoja → crean el flujo en Make.com usando su frase de ajuste (1 frase) → envían a 1 cliente de prueba → ajustan 1 frase en 2 minutos.  
> **Recursos para llevar:** Hoja de acción + tarjeta “Mi asistente” + enlace sencillo a guía visual + link WhatsApp para apoyo rápido (yo respondo en ≤24h).  
> **Slides:** ~25–30, muy visuales, 1 frase por slide, iconos simples, sin texto largo.  

¡Listo! Este outline es **práctico, preparado, fácil de ejecutar** y **responde exactamente a lo que necesitan los emprendedores early-stage no técnicos**: *“Quiero que me ayudes a ahorrar tiempo hoy, sin aprender a programar.”*  

Si quieres, puedo generarte también:  
- El archivo PDF de la hoja de acción (con diseño simple),  
- La guía visual de 3 pasos para Make.com (en español, 1 pantalla por paso),  
- El mensaje de WhatsApp para el grupo de apoyo.  

¡Solo dime cuál y te lo preparo en 20 minutos!  

¡Éxito con el workshop! 🚀