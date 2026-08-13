# DeepSeek V4 Flash 0731 — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 202.61s | tokens_per_second: 26.9
- input_tokens: 198 | output_tokens: 5451
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que facilita la comprensión. Ofrece insights útiles y es directamente aplicable para emprendedores no técnicos.

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

¡Perfecto! Como facilitador con experiencia en Latinoamérica, sé que el secreto está en el "menos teoría, más acción" y en conectar con los problemas reales del emprendedor local. Este outline está diseñado para que salgan con algo funcional en las manos, no solo con apuntes.

Aquí tienes el outline completo del workshop:

---

# Outline del Workshop: "Construye tu Asistente de IA para tu Startup"

**Duración:** 3 horas (180 minutos)  
**Formato:** Presencial, dinámico y 100% práctico.  
**Audiencia:** 20-30 emprendedores no-técnicos early-stage.

**Objetivo General:** Que cada participante termine el workshop con un prototipo funcional de su propio asistente de IA (un bot/configuración) listo para usar en su idea de negocio, sin escribir una sola línea de código.

---

## 1. Agenda Detallada (3 Horas)

- **0:00 - 0:15 (15 min):** Bloque 1 - Check-in y Energía.  
- **0:15 - 0:45 (30 min):** Bloque 2 - El ABC de la IA para no-técnicos (+ Demo).  
- **0:45 - 1:25 (40 min):** Bloque 3 - Ejercicio Parte 1: Diseña tu Asistente (Lienzo).  
- **1:25 - 2:15 (50 min):** Bloque 4 - Ejercicio Parte 2: Construye tu Asistente (Manos a la obra).  
- **2:15 - 2:50 (35 min):** Bloque 5 - Showcase: "Rompe mi bot" (Pitching).  
- **2:50 - 3:00 (10 min):** Bloque 6 - Cierre Energético y Recursos Paquetes.

---

## 2. Materiales Necesarios (Preparar antes)

**Para el Facilitador y Organización:**
- Proyector y pantalla grande.
- Wi-Fi fiable y cables de extensión múltiple. (¡Imprescindible!).
- Speaker portátil para videos cortos (opcional).
- Papelógrafos y marcadores.
- **Equipo de apoyo:** Ideal 2-3 "Coaches" (pueden ser asistentes) que ayuden a los participantes atascados. Ratio 1:10.

**Para los Participantes (Avisar en la invitación):**
- Laptop o tablet con teclado, **con batería cargada**.
- **Cuenta de correo activa.**
- *Pre-tarea* (enviar 2 días antes): Crear una cuenta gratuita en **OpenAI (ChatGPT)** y en **Poe.com** (alternativa que no requiere pago y es friendly para LatAm). Si no tienen, se les dará tiempo para crearla al inicio.

**Material Impreso/Digital (crear antes):**
- **Plantilla del "Lienzo del Asistente" (Paperdeck/PDF)** – explicaré la estructura en el punto 4.
- QR code con todos los recursos para llevar a casa.

---

## 3. Desglose de Bloques

### Bloque 1: Check-in y Energía (15 min)
- **Título:** "Rompiendo el hielo: ¿Qué vendería tu abuela con IA?"
- **Objetivo:** Conocer al público, identificar sus "dolores" diarios y medir el nivel de ansiedad frente a la IA. Establecer el tono informal y práctico.
- **Dinámica:** *Charlas breves y activación.*
  - Facilitador pregunta: "¿Quién ha usado ChatGPT y se quedó con cara de ?" (levantan la mano).
  - Icebreaker: En 30 segundos, cada persona presenta su nombre, su startup y una tarea que *odia* hacer (ej: responder emails, facturar, postear en redes).
  - El facilitador escribe estos "odios" en un papelógrafo y les dice: "Hoy, todas estas cosas se irán a la canasta de la IA".
- **Key Takeaway:** "La IA no te va a quitar el negocio; un emprendedor que usa IA le va a quitar tus clientes".

### Bloque 2: El ABC de la IA para no-técnicos (30 min)
- **Título:** "La IA no es magia: es tu nuevo becario que trabaja 24/7."
- **Objetivo:** Desmitificar la IA generativa. Entender qué son los "Prompts" y las herramientas no-code que usaremos.
- **Dinámica:** **Charla corta + Demo en vivo (El quiebre de la clase).**
  - Presentar 3 herramientas clave: **ChatGPT/Claude** (el cerebro), **Zapier/Make** (las manos), y **Poe/Glide** (el cuerpo de presentación).
  - **Demo "WOW":** El facilitador escribe un prompt malo: *"Escríbeme algo de marketing"* y lo muestra. Luego escribe el mismo prompt con contexto LatAm: *"Eres un community manager experto en cafeterías en CDMX. Escribe un tweet viral para atraer a estudiantes universitarios. Usa humor, emojis y un Call-to-Action"*. Este antes/después es el momento más valioso.
  - Discusión rápida: "¿En qué áreas de tu negocio aplicarías esto?" (Atención al cliente, generación de contenido, investigación de mercado).
- **Key Takeaway:** "No necesitas saber programar, necesitas saber *pedir bien*. El Prompt es tu nuevo superpoder".

### Bloque 3: Ejercicio Parte 1 - Diseña tu Asistente (40 min)
- **Título:** "Paso 1: Da personalidad a tu bot. Define su rol y su "know-how"."
- **Objetivo:** Que cada emprendedor defina el propósito, tono y conocimiento de su asistente antes de tocar teclas. Evitar crear un "bot genérico".
- **Dinámica:** *Ejercicio guiado con Lienzo físico (papel).*
  - Entregar la plantilla **"Lienzo del Asistente"** (ver ejercicio principal más abajo).
  - Guiar a los participantes para llenar:
    1. **Rol:** ¿Quién es? (Ej: Asistente de ventas).
    2. **Audiencia:** ¿Para quién es? (Ej: Jóvenes de 18-25).
    3. **Tono:** ¿Formal, pícaro, profesional?
    4. **Obstáculo:** ¿Qué "no" tiene que hacer? (Limitar respuestas).
    5. **Datos:** ¿Qué sabe? (Ej: Los precios de la cafetería).
  - Juntarse en parejas de 2 personas y darse feedback por 5 minutos.
- **Key Takeaway:** "Un buen bot necesita un buen guion. La claridad inicial ahorra horas de frustración después".

### Bloque 4: Ejercicio Parte 2 - Construye tu Asistente (50 min)
- **Título:** "Paso 2: Manos a la obra - De la hoja al bot funcional."
- **Objetivo:** Construir el asistente funcional. Los participantes podrán elegir **"La vía rápida"** o **"La vía Power"**.
- **Dinámica:** *Tutorial práctico paso a paso (el facilitador proyecta mientras ellos replican).*
  - **Vía Rápida (para todos, sin herramientas complejas):** Usar **Poe.com**. Crear un "Bot" pegando el texto del Lienzo como Prompt inicial. Guardar. ¡Listo! Ya tienen un enlace para compartir.
  - **Vía Power (para los que quieren más):** Usar **ChatGPT** con la opción "Custom GPTs" (si tiene Plus) o dar un enlace a **Glide** para crear una mini-app con un chatbot incorporado.
  - El facilitador y los coaches circulan resolviendo dudas. "¿Dónde pongo el prompt?", "¿Cómo limito que hable de precios?".
- **Key Takeaway:** "Tu primer asistente será un borrador feo, pero es tuyo. La iteración es tu mejor amiga, no el perfeccionismo".

### Bloque 5: Showcase - "Rompe mi bot" (35 min)
- **Título:** "Pon a prueba a tu IA en vivo. Sin piedad."
- **Objetivo:** Validar los bots, aprender de los errores de otros y celebrar los éxitos.
- **Dinámica:** *Pitching + Testing en grupo.*
  - Seleccionar 3 voluntarios (los más atrevidos).
  - Conectan el laptop al proyector.
  - Le piden al bot que haga su tarea (ej: vender un café).
  - El resto del público puede hacer las preguntas más "malvadas" posibles: "¿Cuál es tu número de tarjeta?", "Quiero uno gratis". El bot debe resistir.
  - El facilitador da feedback constructivo sobre el tono y la efectividad del prompt.
- **Key Takeaway:** "El feedback temprano y brusco de tus usuarios (y colegas) evita desastres de producto después".

### Bloque 6: Cierre Energético y Recursos (10 min)
- **Título:** "Tu plan de 7 días para lanzar tu asistente."
- **Objetivo:** Sellar el aprendizaje y dejar tarea clara para la semana.
- **Dinámica:** *Charla motivacional corta + Q&A rápido.*
  - Resumen de las 3 reglas de oro: 1) Promptear con detalle, 2) Probar constantemente, 3) No temer a sustituir tareas, no a ti.
  - Proyectar el QR con todos los recursos del take-home.
- **Key Takeaway:** "La mejor IA es la que usas todos los días. Ahora es tu turno".

---

## 4. Ejercicio Principal del Workshop

**Nombre:** El Lienzo del Asistente (Assistant Canvas)

Este es el corazón del workshop. Es una plantilla de 1 página (física o en Figma/Canva) que cada emprendedor llena en el Bloque 3 y usa en el Bloque 4.

**Secciones del lienzo:**

1. **Nombre del Bot:** "VendeTaco" o "SoporteLio".
2. **Misión (1 frase):** ¿Qué problema resuelve? (Ej: "Responder dudas sobre la entrega de mis productos").
3. **Rol Profesional:** (Ej: "Asesor de moda personal").
4. **Tono de Voz:** (Selecciona: Amigable / Formal / Informal / Irónico).
5. **Audiencia Objetivo:** (Edad, ciudad, intereses).
6. **Datos Internos (El "Conocimiento"):** Escribir 3-5 puntos clave que el bot debe saber.
   - *(Esto es crucial, lo convertimos en el System Prompt del bot)*.
7. **Reglas de Oro (Restricciones):** Escribir 2 cosas que NO debe hacer (ej: "No dar descuentos mayores a 10%", "No hablar de política").
8. **Ejemplo de interacción:** Escribir 1 pregunta típica del usuario y 1 posible respuesta ideal.

*Cómo se usa:* Después de llenarlo, el participante copia todo el texto del lienzo y lo pega como "System Prompt" en Poe o ChatGPT.

---

## 5. Recursos para Llevar a Casa

(Entregar como un documento PDF descargable y/o Notion vía QR).

1. **Banco de Prompts (Prompt Library):** 20 prompts listos para usar en tu startup (Post para IG, Email de venta, Pitch deck, análisis de competencia, etc.) adaptados a contexto LatAm.
2. **Herramientas Clave:**
   - Cerebro: **ChatGPT**, **Claude.ai**, **Google Gemini**.
   - Automatización: **Zapier** (para conectarlo con Google Sheets/WhatsApp).
   - Construcción de Bots: **Poe.com**, **Glide Apps** (no-code).
   - Copywriting: **Copy.ai**.
3. **Video Completo:** Un video grabado de 30 minutos con el paso a paso de cómo construir el bot en Poe, para que lo repasen si se pierden.
4. **Comunidad:** Enlace a un grupo privado de **WhatsApp o Telegram** ("Comunidad IA Emprendedores") para resolver dudas post-workshop.
5. **Guía de Costos:** Comparativa de planes gratuitos vs. pagos (relevante para créditos escasos en LatAm).

---

## 6. Slide Count Estimado por Sección

- **Bloque 1 (Check-in):** 3 slides (Título, Agenda, Dinámica Icebreaker).
- **Bloque 2 (ABC - Charla y Demo):** 8 slides (Qué es LLM, Tipos de IA, Herramientas no-code, Cómo hacer un buen prompt, Ejemplo de prompt malo/bueno, Esquema del "Becario IA").
- **Bloque 3 (Lienzo):** 4 slides (Explicación del Lienzo, Ejemplo resuelto de una cafetería, 2 slides para los pasos).
- **Bloque 4 (Construcción):** 10 slides (Tutorial de Poe - 5 pasos, Tutorial de Custom GPT - 3 pasos, Errores comunes, Consejos de "copy-paste").
- **Bloque 5 (Showcase):** 2 slides (Rúbrica de validación rápida y Normas de "Rompe mi Bot").
- **Bloque 6 (Cierre):** 3 slides (Reglas de oro, Recursos QR, Contacto/Redes).

**Total estimado: 30 slides.** (Perfecto para un ritmo rápido y energético).

---

**Consejo final de facilitador:** En LatAm, el público valora la autenticidad. Si una demo falla, no te asustes. Aprovecha el error para enseñar: "¡Mira! Esto es exactamente lo que pasa si tu prompt no es claro. ¡Miren lo que hizo el bot, es más divertido así!". La energía se contagia. ¡A romperla!