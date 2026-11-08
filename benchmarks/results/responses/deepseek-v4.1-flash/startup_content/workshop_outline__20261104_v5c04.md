# DeepSeek V4.1 Flash — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.64 | quality: 9.72
- latency_total: 35.207s | tokens_per_second: 121.6
- input_tokens: 199 | output_tokens: 4281
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

# Workshop: "Construye tu Asistente de IA para tu Startup"
### Outline completo para 3 horas presenciales | 20-30 emprendedores early-stage no-técnicos

---

## 🎯 Filosofía del workshop

**Cero código. Cero teoría innecesaria. Todos salen con un asistente funcionando.**

La regla de oro: cada persona termina la sesión con un link funcional de su asistente de IA, entrenado con información de SU startup, listo para compartir con su equipo o probar con un cliente.

**Estructura base:** 20% inspiración → 30% construcción guiada → 40% ejercicio práctico → 10% cierre y recursos.

---

## 📋 AGENDA DETALLADA (180 minutos)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00–0:10 | Bienvenida + Rompehielos | 10 min |
| 0:10–0:30 | Bloque 1: Qué es (y qué NO es) un asistente de IA | 20 min |
| 0:30–0:50 | Bloque 2: Demo en vivo — De cero a asistente en 15 min | 20 min |
| 0:50–1:05 | Bloque 3: Define tu caso de uso (ejercicio rápido) | 15 min |
| 1:05–1:15 | ☕ Break | 10 min |
| 1:15–2:15 | Bloque 4: EJERCICIO PRINCIPAL — Construye tu asistente | 60 min |
| 2:15–2:35 | Bloque 5: Prueba, comparte y mejora (show & tell) | 20 min |
| 2:35–2:50 | Bloque 6: Cómo llevarlo a producción sin morir en el intento | 15 min |
| 2:50–3:00 | Cierre + Recursos + Q&A | 10 min |

**Nota de facilitación:** Los tiempos son guía. Si el ejercicio principal se desborda, recorta el Bloque 6 a 10 min pero NUNCA el show & tell (es donde ocurre la magia y el networking).

---

## 🧰 MATERIALES NECESARIOS (preparar antes)

### Infraestructura del espacio
- [ ] Proyector + HDMI/USB-C + adaptadores (probar 30 min antes)
- [ ] WiFi de alta capacidad (confirmar ancho de banda para 30 dispositivos) + red de respaldo (hotspot 4G)
- [ ] Mesas en islas de 5-6 personas (facilita peer support)
- [ ] Pizarra o rotafolio + marcadores gruesos
- [ ] Cronómetro visible (pantalla o timer grande)
- [ ] Cables de carga / regletas (la gente llega con batería al 40%)

### Herramientas digitales (cuentas y accesos)
- [ ] Cuentas demo creadas en la plataforma elegida (recomendado: **Chatbase, Botpress o Voiceflow** — no-code, plan free suficiente)
- [ ] **Plan B crítico:** 5-8 "cuentas semilla" ya creadas por si el registro falla en vivo
- [ ] Documento compartido (Notion/Google Doc) con: links de registro, guía paso a paso, prompts de ejemplo
- [ ] QR codes impresos y en slides para: registro a la plataforma, doc de recursos, formulario de feedback
- [ ] Datos de ejemplo listos para cargar (FAQ ficticia de una startup, 1-2 páginas)

### Materiales físicos
- [ ] Tarjetas de "Caso de uso" (una por persona, con 12-15 ejemplos distintos pre-impresos)
- [ ] Post-its (2 colores) y sharpies
- [ ] Stickers o tarjetas de "✅ Asistente funcionando" para celebrar hitos
- [ ] Snacks + café/agua (el break de 10 min es estratégico, no decorativo)
- [ ] Cartel grande con el WiFi y la contraseña (legible desde el fondo)

### Preparación del facilitador
- [ ] Ensayar la demo EN VIVO 3 veces (con el WiFi real del venue si es posible)
- [ ] Tener el asistente demo YA construido como respaldo si el live coding falla
- [ ] Preparar 3 "prompts de rescate" para gente bloqueada
- [ ] Briefing a 2-3 voluntarios/asistentes (uno por cada 10 personas) para soporte durante el ejercicio

---

## 🎬 DESGLOSE POR BLOQUES

---

### BLOQUE 0 — Bienvenida + Rompehielos
**Duración:** 10 min | **Slides:** 3

**Objetivo:** Bajar la ansiedad tecnológica y crear energía de comunidad.

**Dinámica:** 
- Bienvenida de 2 min con promesa clara: *"En 3 horas te vas con un asistente de IA funcionando. Sin código. Sin excusas."*
- Rompehielos de 3 min: "Levanta la mano si…" (¿has usado ChatGPT? ¿tienes un bot en tu web? ¿crees que la IA te va a reemplazar?). Genera risas y calibra el nivel del grupo.
- Presentación rápida de vecinos de mesa (30 seg c/u): nombre + startup + qué tarea repetitiva odias hacer.

**Key takeaway:** *"Hoy no venimos a aprender sobre IA. Venimos a construir con IA."*

---

### BLOQUE 1 — Qué es (y qué NO es) un asistente de IA
**Duración:** 20 min | **Slides:** 8

**Objetivo:** Desmitificar el concepto y alinear expectativas. Que entiendan la diferencia entre chatbot genérico y asistente entrenado con SUS datos.

**Dinámica:** Charla interactiva (12 min) + mini-discusión en mesas (8 min).
- Analogía central: *"ChatGPT es un pasante brillante que no conoce tu negocio. Un asistente de IA es ese mismo pasante después de leer todo tu manual, tu FAQ y tus políticas."*
- Los 3 componentes en lenguaje simple: **Cerebro** (el modelo), **Memoria** (tus datos), **Canal** (dónde vive: web, WhatsApp, Slack).
- Mostrar 3 ejemplos reales de startups LatAm usando asistentes (soporte, onboarding, ventas).
- Discusión en mesas: "¿Dónde duele más en tu startup el soporte/atención repetitiva?" → anotar en post-it.

**Key takeaway:** *"Un asistente útil = modelo + tus datos + un caso de uso concreto. Sin tus datos, es solo ChatGPT con otro nombre."*

---

### BLOQUE 2 — Demo en vivo: De cero a asistente en 15 min
**Duración:** 20 min | **Slides:** 5

**Objetivo:** Que vean con sus propios ojos que es posible y simple. Eliminar la barrera del "yo no puedo".

**Dinámica:** Demo en vivo proyectada (15 min) + Q&A rápido (5 min).
- Construir EN VIVO un asistente de ejemplo (ej: "Asistente de soporte para una fintech ficticia") desde cero: crear cuenta → cargar FAQ → personalizar tono → probar → publicar link.
- **Narrar cada clic** y mostrar los errores comunes (y cómo se arreglan).
- El asistente demo queda publicado para que lo prueben desde sus celulares.

**Key takeaway:** *"Lo que acabas de ver toma 15 minutos. Lo difícil no es la herramienta, es decidir QUÉ va a resolver."*

---

### BLOQUE 3 — Define tu caso de uso
**Duración:** 15 min | **Slides:** 4

**Objetivo:** Que cada persona salga con UN caso de uso concreto y acotado para construir en el ejercicio principal.

**Dinámica:** Ejercicio individual + validación en parejas (5 min solo, 5 min en parejas, 5 min plenaria).
- Repartir tarjetas de casos de uso (soporte FAQ, onboarding de clientes, calificación de leads, asistente interno de políticas, guía de producto, etc.).
- Cada persona completa una plantilla de 4 líneas en un post-it:
  1. **Mi asistente ayudará a:** [quién]
  2. **A resolver:** [qué tarea concreta]
  3. **Usando estos datos:** [qué info tengo a mano]
  4. **En este canal:** [web / WhatsApp / interno]
- Regla de oro: si tu caso de uso necesita "toda la empresa", es demasiado grande. **Acótalo.**
- Validación en parejas: "¿Se entiende? ¿Es alcanzable en 45 min?"

**Key takeaway:** *"Un caso de uso pequeño y real vale más que uno ambicioso y vago. Hoy construimos el primero; el resto viene después."*

---

### ☕ BREAK
**Duración:** 10 min

**Dinámica:** Café + networking. El facilitador y voluntarios circulan resolviendo dudas de registro/logística. **Crítico:** confirmar que todos tienen cuenta creada ANTES de empezar el ejercicio.

---

### BLOQUE 4 — 🚀 EJERCICIO PRINCIPAL: Construye tu asistente
**Duración:** 60 min | **Slides:** 6 (slides-guía paso a paso)

**Objetivo:** Que cada participante construya, entrene y publique su propio asistente de IA funcional con datos de su startup.

**Dinámica:** Construcción guiada paso a paso (facilitador proyecta cada paso, todos lo hacen simultáneamente) + soporte de voluntarios en mesas.

**Estructura interna del bloque (marcar tiempos en pantalla):**

| Min | Paso | Instrucción |
|-----|------|-------------|
| 0–10 | **Setup** | Crear cuenta, elegir plantilla, nombrar el asistente |
| 10–25 | **Alimentar la memoria** | Cargar datos: pegar FAQ, subir 1-2 docs, o escribir el "system prompt" con la plantilla provista |
| 25–35 | **Darle personalidad** | Definir tono, nombre, mensaje de bienvenida, restricciones ("no inventes precios") |
| 35–50 | **Probar y romper** | Cada uno hace 5 preguntas a su asistente (3 fáciles, 2 difíciles). Anotar qué falla |
| 50–60 | **Iterar una vez** | Corregir el fallo más grande (agregar dato faltante o ajustar instrucción) y republicar |

**Reglas del ejercicio:**
- **Kit de datos de respaldo:** quien no trajo datos de su startup usa el dataset de ejemplo provisto (no se permite "no tengo nada").
- **Hito celebrado:** cuando alguien publica su asistente → sticker de "✅ Funcionando" + foto para redes.
- **Regla del vecino:** antes de llamar al voluntario, preguntar a la persona de al lado (fomenta peer learning y descongestiona el soporte).

**Key takeaway:** *"Ya tienes un asistente vivo. No es perfecto — y no necesita serlo. Es la versión 0.1 que puedes mejorar mañana."*

---

### BLOQUE 5 — Prueba, comparte y mejora (Show & Tell)
**Duración:** 20 min | **Slides:** 3

**Objetivo:** Validación social, aprendizaje entre pares y detectar mejoras obvias.

**Dinámica:** "Speed-testing" rotativo (12 min) + plenaria de aprendizajes (8 min).
- En cada mesa, cada persona comparte el link de su asistente y el vecino le hace 2 preguntas "trampa". Se anotan los mejores fallos y los mejores aciertos.
- Plenaria: 3-4 voluntarios proyectan su asistente en vivo. El grupo sugiere una mejora. El facilitador destaca patrones ("mira cómo X resolvió el tono", "esto es un prompt que puedes copiar").
- Cierre del bloque: cada uno anota en post-it **"La próxima mejora de mi asistente será: ___"**.

**Key takeaway:** *"La mejor forma de mejorar tu asistente es ponerlo frente a alguien que no seas tú. Feedback real > perfeccionismo."*

---

### BLOQUE 6 — De demo a producción sin morir en el intento
**Duración:** 15 min | **Slides:** 6

**Objetivo:** Dar el mapa realista de qué sigue para pasar de "prototipo de workshop" a "asistente en producción".

**Dinámica:** Charla ágil con checklist accionable + preguntas.
- Los 4 pasos para llevarlo a producción: **1) Validar con usuarios reales → 2) Elegir canal (web/WhatsApp) → 3) Definir métricas (¿resuelve? ¿escala? ¿costo por conversación?) → 4) Iterar semanalmente.**
- Advertencias honestas: alucinaciones, privacidad de datos, costos que crecen, cuándo NO usar un asistente.
- Checklist "¿Está listo mi asistente para clientes reales?" (7 preguntas).

**Key takeaway:** *"El asistente del workshop es el borrador. Producción = validar con 10 usuarios reales esta semana y medir si resuelve. Si no mides, no mejora."*

---

### CIERRE — Recursos + Q&A
**Duración:** 10 min | **Slides:** 2

**Objetivo:** Que se vayan con todo lo necesario para continuar solos y con ganas de volver.

**Dinámica:** Entrega de recursos (QR) + ronda rápida de compromisos + foto grupal.
- Cada persona escribe su compromiso de 1 semana: *"Antes del próximo [día], voy a ___ con mi asistente."*
- Foto grupal con los asistentes publicados en pantalla.
- QR a: doc de recursos, comunidad (WhatsApp/Slack del cohorte), formulario de feedback.

**Key takeaway:** *"No te llevas un certificado. Te llevas un asistente funcionando y una comunidad para seguir construyendo."*

---

## 🏆 EJERCICIO PRINCIPAL — Resumen ejecutivo

**"Tu Primer Asistente en 60 Minutos"**

Cada participante construye un asistente de IA no-code, entrenado con información real de su startup, en la plataforma elegida (Chatbase/Botpress/Voiceflow). Al finalizar:

✅ Tiene un asistente publicado con link compartible
✅ Lo entrenó con al menos 1 fuente de datos propia (FAQ, doc o system prompt)
✅ Lo probó con 5 preguntas e iteró al menos una vez
✅ Lo validó con un par que le hizo preguntas "trampa"

**Garantías de éxito del ejercicio:**
- Plantilla de system prompt provista (copy-paste, solo rellenar campos)
- Dataset de respaldo para quien no trajo datos
- 1 voluntario de soporte por cada 10 personas
- Red de respaldo si falla el WiFi
- Hito celebrado con sticker al publicar

---

## 📚 RECURSOS PARA LLEVAR A CASA

1. **Guía PDF "De 0 a asistente en producción"** — los 4 pasos + checklist de 7 preguntas
2. **Biblioteca de prompts** — 15 system prompts probados por caso de uso (soporte, ventas, onboarding, interno)
3. **Comparativa de plataformas no-code** — precios, límites del plan free, pros/contras (Chatbase, Botpress, Voiceflow, otros)
4. **Plantilla de "Caso de uso"** — el framework de 4 líneas del Bloque 3, en Notion editable
5. **Video grabación del workshop** (si se grabó) + link al asistente demo del facilitador
6. **Comunidad del cohorte** — grupo de WhatsApp/Slack para seguimiento y dudas post-workshop
7. **Lista de "errores comunes y cómo evitarlos"** — 10 pitfalls de asistentes en producción (alucinaciones, privacidad, costos)
8. **Reto de 7 días** — un email/mensaje diario con una micro-mejora para aplicar a tu asistente

---

## 📊 CONTEO ESTIMADO DE SLIDES

| Sección | Slides |
|---------|--------|
| Portada + Bienvenida + Rompehielos | 3 |
| Bloque 1: Qué es un asistente | 8 |
| Bloque 2: Demo en vivo | 5 |
| Bloque 3: Define tu caso de uso | 4 |
| Bloque 4: Ejercicio principal (guía paso a paso) | 6 |
| Bloque 5: Show & Tell | 3 |
| Bloque 6: De demo a producción | 6 |
| Cierre + Recursos | 2 |
| **TOTAL** | **~37 slides** |

**Regla de diseño:** máximo 25 palabras por slide, una idea por slide, tipografía 28pt+. Los slides son apoyo visual, no guion. El valor está en la demo y el ejercicio.

---

## 💡 NOTAS FINALES PARA EL FACILITADOR

- **Energía sostenida:** cambia de formato cada 15-20 min (charla → demo → ejercicio → discusión). La atención decae rápido.
- **El enemigo #1 es el WiFi.** Ten plan B siempre. Un asistente que no carga mata el momentum.
- **Celebra los fallos:** cuando un asistente responde mal en el show & tell, aplaude y úsalo como lección. Normaliza la iteración.
- **No todos terminan al mismo ritmo.** Ten "misiones extra" preparadas para los rápidos (agregar segundo canal, probar tono distinto, conectar más datos).
- **Documenta en vivo:** toma fotos de post-its y asistentes publicados. Es material de marketing y de mejora del próximo cohorte.

**Promesa final del workshop:** *"Entraste sin saber qué era un asistente de IA. Sales con uno funcionando, entrenado con tu startup, y el mapa para ponerlo frente a clientes reales esta semana."* 🚀