# GLM 5.3 Flash — startup_content/workshop_outline

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.47 | quality: 9.72
- latency_total: 80.436s | tokens_per_second: 71.1
- input_tokens: 202 | output_tokens: 5716
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

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
### Workshop Práctico · 3 horas · 20-30 fundadores no-técnicos

**La promesa del día:** *Salís de acá con un asistente de IA funcionando para TU startup. No slides sobre el futuro. Una herramienta construida por vos, hoy.*

**Requisito previo (email 72h antes):** cuenta gratuita en ChatGPT o Claude creada + laptop cargada. Sin excepciones.

---

## 1. AGENDA GENERAL

| Horario | Bloque | Formato |
|---|---|---|
| 0:00 – 0:15 | 🔥 Bienvenida: El Muro de los Dolores | Dinámica grupal |
| 0:15 – 0:40 | 🤯 Lo que la IA YA hace por startups como la tuya | Demo en vivo |
| 0:40 – 1:00 | 🧬 El ADN del Asistente (la receta) | Mini-clase + ejercicio en parejas |
| 1:00 – 1:10 | ☕ BREAK | — |
| 1:10 – 2:20 | 🛠️ MANOS A LA OBRA: Construye tu Asistente | Ejercicio principal |
| 2:20 – 2:40 | 🎤 Show & Tell: demos de participantes | Showcase |
| 2:40 – 2:55 | 📈 Del prototipo a tu operación | Charla + roadmap |
| 2:55 – 3:00 | 💥 Cierre y compromisos | Ritual grupal |

---

## 2. BLOQUES DETALLADOS

### 🔥 Bloque 1 — Bienvenida: El Muro de los Dolores (15 min)
- **Objetivo:** Conectar emocionalmente y sembrar la materia prima del ejercicio principal.
- **Dinámica:** Al entrar, cada uno escribe en un post-it *"la tarea repetitiva que más odio hacer en mi startup"* y lo pega en la pared. El facilitador lee 4-5 en voz alta con drama ("¿Responder los mismos 15 mensajes de WhatsApp al día? ¿Alguien más?"). Clasificación rápida en 4 categorías: **Cliente, Contenido, Ventas, Operaciones.**
- **Key takeaway:** *"Hoy no venimos a escuchar sobre IA. Venimos a construir con IA. Y tu asistente va a nacer de ese post-it."*

**Slides: 4** (portada, promesa del día, agenda, instrucción dinámica)

---

### 🤯 Bloque 2 — Lo que la IA YA hace por startups como la tuya (25 min)
- **Objetivo:** Destruir la idea de que "la IA no es para mí / es muy técnica".
- **Dinámica:** 3 demos en vivo, con casos LATAM reales:
  1. **Asistente de cliente:** responde consultas típicas de WhatsApp con el tono de tu marca
  2. **Asistente de contenido:** 1 semana de posts de Instagram en 5 minutos
  3. **Asistente de ventas:** transcripción desordenada de una llamada → propuesta profesional
- Interludio rápido de myth-busting: "No necesitas saber programar / No necesitas pagar / No te va a reemplazar, te va a clonar".
- **Key takeaway:** *"La IA ya hace tareas concretas de tu operación HOY. El único requisito es saber darle instrucciones. Y eso se aprende en una tarde."*

**Slides: 8**

---

### 🧬 Bloque 3 — El ADN del Asistente (20 min)
- **Objetivo:** Darles la receta que van a usar por el resto del workshop (y de sus vidas).
- **Dinámica:**
  - Presentar las **5 piezas**: **ROL + CONTEXTO + TAREA + FORMATO + EJEMPLOS**
  - Demo comparativa: *"prompt malo vs. prompt con ADN completo"* → la audiencia grita las diferencias
  - **Ejercicio en parejas (7 min):** reciben un prompt malo impreso y lo reparan con la plantilla. 2 parejas comparten.
- **Key takeaway:** *"El 80% de tu resultado depende de cómo instruyes. Un asistente vago es culpa tuya, no de la IA."*

**Slides: 7**

---

### ☕ BREAK (10 min)
Post-its de "dolores" siguen en la pared → la gente los lee y se transforma en conversación. Gratis.

---

## 3. 🛠️ EJERCICIO PRINCIPAL: "Construye tu Asistente Fundador" (70 min)

El corazón del workshop. Todos construyen **UN asistente para UNA tarea real**, con herramientas gratuitas. *Detallado aquí porque es el entregable del día:*

| Paso | Tiempo | Qué hacen |
|---|---|---|
| 1. Elegí tu misión | 5' | Retoman su post-it del Muro de Dolores y eligen UNA tarea |
| 2. Llená el Canvas del Asistente | 15' | Plantilla impresa de 1 página (ver abajo) |
| 3. Traducí a instrucciones | 20' | Pasan el canvas a un prompt en ChatGPT/Claude. Facilitador construye el suyo en paralelo en pantalla |
| 4. Stress test | 15' | Prueban con 3 casos: 1 típico, 1 difícil, 1 absurdo/fuera de alcance (esto enseña límites) |
| 5. Iterá y guardá | 15' | Ajustan instrucciones, guardan versión final, la comparten en el grupo de WhatsApp del workshop |

**El Canvas del Asistente (impreso, 1 página):**
1. Nombre de tu asistente (que le pongan nombre no es un capricho: genera ownership)
2. Su rol ("Sos el especialista en...")
3. Contexto de mi startup (qué hago, a quién vendo, cómo hablo)
4. Sus 3 tareas principales
5. Lo que NUNCA debe hacer (restricciones)
6. Tono y formato de salida
7. 2 ejemplos de respuestas ideales

**Cartas de nivel 2** para quien termina antes: *"agregale ejemplos few-shot"*, *"creale una bienvenida"*, *"hacelo que maneje objeciones de precio"*.

⚠️ **Tips de facilitador:** 1-2 co-facilitadores como "mesa de ayuda" circulando. Si alguien trae un caso demasiado complejo, redirigir a la versión simple ("hoy version 1, en casa version 2").

**Slides: 6** (instrucciones por paso, quedan proyectadas como referencia permanente)

---

### 🎤 Show & Tell (20 min)
- **Objetivo:** Presión social positiva + inspiración cruzada.
- **Dinámica:** 4-5 voluntarios demuestran su asistente en vivo (3 min c/u). La audiencia aplaude para elegir el *"Asistente más útil"* y el *"Caso más inesperado"*.
- **Key takeaway:** *"Miren: 20 asistentes distintos construidos en una hora. Por gente que 'no es de tecnología'."*

**Slides: 2**

---

### 📈 Del prototipo a tu operación (15 min)
- **Objetivo:** Que no se quede en un lindo ejercicio de workshop.
- **Dinámica:** Roadmap de 30 días + glimpse del "nivel 2": conectar el asistente a WhatsApp real con herramientas no-code (ManyChat, Zapier, Make). Costos reales: qué se puede en plan gratuito.
- **Key takeaway:** *"Tu asistente es un empleado que mejora cada vez que lo instruyes mejor. Tu único trabajo es entrenarlo."*

**Slides: 5**

---

### 💥 Cierre y compromisos (5 min)
- Cada uno escribe en su post-it original: *"En 7 días uso mi asistente para ___"* y lo pega sobre su dolor inicial. Foto grupal del muro.
- QR al pack de recursos + grupo de WhatsApp + anuncio de sesión de seguimiento en 2 semanas.
- **Key takeaway:** *"El workshop termina hoy. Tu asistente recién empieza."*

**Slides: 3**

---

## 4. MATERIALES Y LOGÍSTICA

**Pre-evento (72h antes):**
- 📧 Email con instrucciones: crear cuenta gratuita ChatGPT/Claude, traer laptop + cargador
- 🖨️ Imprimir: Canvas del Asistente (x1.5 por persona), prompts "rotos" para el ejercicio en parejas, cheat sheet del ADN

**Día del evento:**
- Proyector/HDMI probado + control remoto
- Wi-Fi para invitados con capacidad verificada + **hotspot del celular del facilitador como plan B**
- 4-6 zapatillas/regletas de energía
- Post-its, marcadores, pared libre, name tags, timer visible
- QR impreso al folder de recursos + grupo de WhatsApp

**Plan de contingencia:**
- 🎥 Videos de las demos grabados previamente (si falla internet)
- 🤖 Un asistente de ejemplo pre-construido y guardado, listo para mostrar offline

---

## 5. RECURSOS PARA LLEVAR A CASA

1. **Pack de 15 prompts para fundadores** (validar idea, email a cliente difícil, respuesta a reclamo, post de LinkedIn, pitch de 30 segundos...)
2. **Canvas del Asistente** en versión digital (template Notion)
3. **Cheat sheet imprimible:** El ADN del Asistente (la receta de 5 piezas)
4. **Checklist Roadmap 30 días** para integrar el asistente a su operación
5. **Lista curada de herramientas** free-first: ChatGPT, Claude, Gemini, Perplexity, Gamma, CapCut, ElevenLabs, ManyChat, Make
6. **Grupo de WhatsApp** del workshop + invitación a sesión de seguimiento (¡esto convierte un workshop en comunidad!)

---

## 6. RESUMEN DE SLIDES

| Sección | Slides |
|---|---|
| Bienvenida | 4 |
| Lo que la IA ya hace | 8 |
| El ADN del Asistente | 7 |
| Ejercicio principal | 6 |
| Show & Tell | 2 |
| Del prototipo a la operación | 5 |
| Cierre | 3 |
| **TOTAL** | **~35 slides** |

**Regla de oro:** en la parte práctica, las slides no se presentan — *se dejan proyectadas como manual de instrucciones en vivo.*

---

¿Querés que desarrolle alguno de los materiales en detalle? Puedo armar el **Canvas del Asistente completo**, el **guion palabra por palabra del Bloque 2 (las 3 demos)** o el **email de pre-workshop**. 💪