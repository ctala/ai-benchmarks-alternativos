# Claude Opus 4.8 (suscripción) — startup_content/workshop_outline

- model_id: `claude-opus-4-8`
- success: True  | final: 7.23 | quality: 10.0
- latency_total: 85.595s | tokens_per_second: 70.0
- input_tokens: 2026 | output_tokens: 5990
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que se ajusta perfectamente a las necesidades de los emprendedores no técnicos, ofreciendo un plan práctico y utilizable.

## Respuesta completa

# 🚀 Construye tu Asistente de IA para tu Startup
## Workshop Práctico · 3 horas · Presencial

> **Audiencia:** 20-30 emprendedores early-stage, no-técnicos
> **Promesa:** Sales con un asistente de IA funcionando para TU negocio. No teoría. Sale-and-build.
> **Tono:** Manos a la masa. Si algo se rompe, mejor — así se aprende.

---

## 🎯 Resultado de aprendizaje (la promesa al asistente)

Al final de las 3 horas, cada persona se va con **un asistente de IA configurado y probado** que resuelve UNA tarea real de su startup (responder clientes, redactar contenido, calificar leads, etc.), más un plan claro para escalarlo.

---

## 📋 1. AGENDA DETALLADA (180 min)

| # | Bloque | Tiempo | Reloj | Tipo |
|---|--------|--------|-------|------|
| 0 | Bienvenida y "termómetro de IA" | 15 min | 0:00–0:15 | Energizer + encuadre |
| 1 | Desmitificando la IA (sin tecnicismos) | 20 min | 0:15–0:35 | Charla + demo |
| 2 | Cazando tu "tarea dolorosa" | 20 min | 0:35–0:55 | Ejercicio individual |
| 3 | El arte de pedir bien (prompting) | 25 min | 0:55–1:20 | Charla + práctica |
| — | ☕ **PAUSA** | 10 min | 1:20–1:30 | Café + networking |
| 4 | **EJERCICIO PRINCIPAL: Construye tu asistente** | 50 min | 1:30–2:20 | Hands-on guiado |
| 5 | Conéctalo a tu negocio (automatización) | 20 min | 2:20–2:40 | Demo + discusión |
| 6 | Riesgos, costos y errores comunes | 12 min | 2:40–2:52 | Charla rápida |
| 7 | Pitch relámpago + cierre y recursos | 8 min | 2:52–3:00 | Showcase + cierre |

**Total: 180 min** (con buffer real dentro de cada bloque).

---

## 🎒 2. MATERIALES NECESARIOS (preparar ANTES)

### Para el facilitador
- [ ] **Cuentas demo listas:** ChatGPT (gratis + una Plus para demo), Claude, y una herramienta no-code de automatización (ej. n8n o Make) con un flujo de ejemplo ya armado.
- [ ] **2-3 asistentes pre-construidos** como ejemplo en vivo (un "respondedor de clientes", un "generador de posts", un "calificador de leads").
- [ ] **Slides** (conteo abajo, ~52 slides).
- [ ] **Plantilla de prompt impresa** (1 hoja por persona) — el "esqueleto de prompt".
- [ ] **Hoja de "Caza tu tarea dolorosa"** impresa (Bloque 2).
- [ ] **QR gigante** que apunta a la carpeta de recursos (Drive/Notion).
- [ ] **Tarjetas de colores / post-its** para dinámicas.
- [ ] **Cronómetro visible** proyectado (¡disciplina de tiempo!).

### Para los participantes (comunicar 48h antes por mail/WhatsApp)
- [ ] **Laptop cargado** (NO solo celular — el ejercicio principal va mejor en pantalla grande).
- [ ] **Cuenta gratuita de ChatGPT y/o Claude ya creada** (mandar tutorial de 2 min).
- [ ] **Traer 1 problema real** de su startup que les quita tiempo cada semana.
- [ ] Datos de ejemplo de su negocio (un correo tipo de cliente, su descripción de producto, su tono de marca).

### Logística de sala
- [ ] WiFi probado con 30 dispositivos (¡el asesino #1 de workshops!). Plan B: hotspot.
- [ ] Mesas en islas de 4-5 personas (para apoyo entre pares).
- [ ] Enchufes / regletas suficientes.
- [ ] Agua y café para la pausa.

---

## 🧩 3. DESGLOSE POR BLOQUE

---

### BLOQUE 0 — Bienvenida y "Termómetro de IA" · 15 min
- **Objetivo:** Romper el hielo, medir el nivel real de la sala y bajar la ansiedad del no-técnico.
- **Dinámica (energizer):** "Línea humana" — todos se paran y se ubican en una línea imaginaria: de "nunca usé IA" a "la uso todos los días". Conversan con su vecino 60 seg: *¿qué te frustra de la IA?*
- **Contenido:** Encuadre del workshop, la promesa ("te vas con algo funcionando"), reglas del juego ("se vale equivocarse, se vale preguntar").
- **🔑 Key takeaway:** "No necesitas saber programar para tener IA trabajando para ti hoy."
- **Slides:** 5

---

### BLOQUE 1 — Desmitificando la IA (sin tecnicismos) · 20 min
- **Objetivo:** Entender QUÉ es un asistente de IA y qué puede/no puede hacer, en lenguaje de emprendedor.
- **Dinámica:** Charla corta + **demo en vivo** (le pido a la IA que escriba un correo de cobranza amable frente a todos, en 30 segundos).
- **Contenido:**
  - La analogía del "pasante brillante pero olvidadizo".
  - 4 cosas que la IA hace excelente: escribir, resumir, clasificar, conversar.
  - 3 cosas donde falla: datos en tiempo real, matemática fina, inventa con seguridad ("alucina").
  - Asistente vs. chatbot vs. automatización (sin jerga).
- **🔑 Key takeaway:** "La IA es un pasante infinito: rápido y barato, pero necesita instrucciones claras y supervisión."
- **Slides:** 9

---

### BLOQUE 2 — Cazando tu "tarea dolorosa" · 20 min
- **Objetivo:** Que cada persona elija UNA tarea concreta para automatizar hoy (foco = éxito).
- **Dinámica:** Ejercicio individual con hoja impresa, luego comparten en su isla (3 min).
- **Contenido / herramienta:** Matriz simple **Frecuencia × Fastidio**. Listan 5 tareas repetitivas → puntúan → eligen la que está arriba-derecha.
  - Ejemplos para gatillar ideas: responder dudas frecuentes de clientes, redactar posts, resumir reuniones, calificar leads, traducir, hacer descripciones de productos.
- **🔑 Key takeaway:** "El mejor primer asistente resuelve una tarea aburrida que haces cada semana — no la más impresionante."
- **Slides:** 4

---

### BLOQUE 3 — El arte de pedir bien (Prompting) · 25 min
- **Objetivo:** Aprender el "esqueleto de prompt" que convierte respuestas mediocres en útiles.
- **Dinámica:** Mini-charla + **práctica guiada** (todos prueban en su laptop al mismo tiempo, mismo ejemplo).
- **Contenido — el esqueleto R-C-T-F:**
  - **R**ol: "Eres mi asistente de atención al cliente…"
  - **C**ontexto: qué hace tu startup, tono de marca.
  - **T**area: qué quieres exactamente.
  - **F**ormato: cómo quieres la respuesta (lista, correo, 3 opciones…).
  - Bonus: dar ejemplos ("así respondemos nosotros").
- **Antes/Después** en vivo: prompt malo vs. prompt con esqueleto.
- **🔑 Key takeaway:** "No le pidas a la IA como a Google. Háblale como a un nuevo empleado en su primer día: dale rol, contexto y un ejemplo."
- **Slides:** 8

---

### ☕ PAUSA · 10 min
Café, baño, networking. Música. El facilitador circula resolviendo dudas de cuentas/login antes del ejercicio grande.

---

### BLOQUE 4 — 🏗️ EJERCICIO PRINCIPAL: Construye tu asistente · 50 min
*(Detallado en la sección 4 abajo.)*
- **Objetivo:** Cada persona construye y prueba un asistente personalizado para su tarea dolorosa.
- **Dinámica:** Hands-on guiado paso a paso + apoyo entre pares por islas + facilitador y/o ayudantes circulando.
- **🔑 Key takeaway:** "Ya tienes un asistente real funcionando. Ahora es cosa de mejorarlo, no de empezar de cero."
- **Slides:** 6 (pasos numerados grandes en pantalla, mientras ellos trabajan)

---

### BLOQUE 5 — Conéctalo a tu negocio (automatización) · 20 min
- **Objetivo:** Mostrar cómo el asistente deja de ser un chat y empieza a trabajar solo (visión de futuro accionable).
- **Dinámica:** **Demo en vivo** de una automatización no-code (ej. correo entra → IA redacta borrador de respuesta) + discusión abierta "¿dónde lo enchufarías tú?".
- **Contenido:**
  - 3 niveles de madurez: (1) copiar/pegar en el chat, (2) asistente personalizado guardado, (3) automatización conectada a tus herramientas.
  - Panorama de herramientas no-code (sin vender ninguna): para WhatsApp, correo, planillas.
- **🔑 Key takeaway:** "El salto de valor está en conectar el asistente a donde ya trabajas — pero empieza simple y escala."
- **Slides:** 7

---

### BLOQUE 6 — Riesgos, costos y errores comunes · 12 min
- **Objetivo:** Que usen IA de forma responsable y no se quemen (ni en plata ni en confianza).
- **Dinámica:** Charla rápida estilo "los 5 errores que vas a cometer".
- **Contenido:**
  - **Alucinaciones:** verifica datos sensibles, nunca publiques a ciegas.
  - **Datos privados:** qué NO pegar (datos de clientes, info legal/financiera sensible).
  - **Costos:** gratis vs. pago, en qué momento conviene pagar.
  - **Dependencia:** la IA asiste, tú decides.
- **🔑 Key takeaway:** "Confía, pero verifica. Tú firmas, no la IA."
- **Slides:** 5

---

### BLOQUE 7 — Pitch relámpago + cierre · 8 min
- **Objetivo:** Celebrar lo construido, generar compromiso y entregar recursos.
- **Dinámica:** 3-4 voluntarios muestran su asistente en 30 seg ("muéstrame qué hace") + cierre.
- **Contenido:** Entrega de recursos (QR), compromiso de UNA acción para esta semana (lo escriben en un post-it y se lo llevan), invitación a comunidad/seguimiento.
- **🔑 Key takeaway:** "Lo construiste en 50 minutos. Imagina en una semana. El siguiente paso es usarlo mañana."
- **Slides:** 3

---

## 🛠️ 4. EJERCICIO PRINCIPAL (detallado)

### "Tu primer asistente en 5 pasos"
**Formato:** Cada participante usa la tarea dolorosa que eligió en el Bloque 2. Trabajan en su laptop con ChatGPT o Claude. Lo hacemos como herramienta gratuita y universal: **un "asistente personalizado" guardado** (ej. un *Custom GPT* / *Proyecto*, o como mínimo un prompt-plantilla reutilizable). Pantalla del facilitador muestra los pasos en grande.

| Paso | Qué hacen | Tiempo |
|------|-----------|--------|
| **1. Define el trabajo** | Escriben en 1 frase qué hará el asistente y para quién. | 5 min |
| **2. Arma el cerebro (instrucciones)** | Usan el esqueleto R-C-T-F del Bloque 3 para escribir las instrucciones base del asistente: rol, contexto de su startup, tono, qué debe y no debe hacer. | 12 min |
| **3. Aliméntalo con ejemplos** | Pegan 1-2 ejemplos reales (un correo de cliente típico, su descripción de producto, su tono de marca). | 8 min |
| **4. Pruébalo en caso real** | Le pasan un caso real de su negocio y revisan la respuesta. | 10 min |
| **5. Afina (loop de mejora)** | Le dicen qué corregir ("muy formal", "muy largo", "agrega un saludo") y vuelven a probar. Repiten 2-3 veces. | 10 min |
| **Cierre** | Le ponen nombre a su asistente y lo guardan. 🎉 | 5 min |

**Criterio de éxito visible:** "Si tu asistente respondió tu caso real de forma usable (aunque haya que editar), ganaste."

**Soporte:** 1 facilitador + idealmente 1-2 ayudantes circulando. Las islas se ayudan entre sí. Para los más rápidos: reto extra → "agrégale una segunda habilidad".

**Plan B (sin WiFi / no técnico):** ejercicio en papel con la plantilla R-C-T-F + prueba en celular vía datos móviles.

---

## 📦 5. RECURSOS PARA LLEVAR A CASA (carpeta vía QR)

1. **Plantilla R-C-T-F de prompts** (editable + impresa).
2. **Galería de 20 prompts listos** para tareas de startup (ventas, marketing, soporte, operaciones).
3. **Las instrucciones base de los 3 asistentes de ejemplo** (copiar y adaptar).
4. **Guía 1-página:** "Cómo crear tu asistente personalizado paso a paso" (con capturas).
5. **Checklist de seguridad:** qué datos NO pegar + cómo verificar.
6. **Mapa de herramientas no-code** para conectar tu asistente (con niveles según presupuesto).
7. **Reto de 7 días:** una mini-tarea de IA por día para consolidar el hábito.
8. **Acceso a comunidad / canal** de seguimiento y dudas.
9. **Slides del workshop** en PDF.

---

## 🖼️ 6. CONTEO DE SLIDES POR SECCIÓN

| Bloque | Slides |
|--------|--------|
| 0 · Bienvenida + Termómetro | 5 |
| 1 · Desmitificando la IA | 9 |
| 2 · Caza tu tarea dolorosa | 4 |
| 3 · Prompting (R-C-T-F) | 8 |
| 4 · Ejercicio principal | 6 |
| 5 · Conéctalo a tu negocio | 7 |
| 6 · Riesgos y costos | 5 |
| 7 · Pitch + cierre | 3 |
| Portada + transiciones + buffer | 5 |
| **TOTAL** | **≈ 52 slides** |

**Regla de diseño:** máximo 1 idea por slide, fuente grande, más imágenes/capturas que texto. Si una slide tiene un párrafo, divídela en dos.

---

## 💡 Tips de facilitación (bonus)

- **Cronómetro proyectado siempre.** El enemigo del taller práctico es irse en charla.
- **Energía cada 25 min:** una pregunta a la sala, un "levanten la mano si…", un mini-aplauso.
- **Celebra los errores en vivo:** cuando algo falle (¡y fallará!), úsalo como enseñanza. "¡Perfecto, esto pasa siempre, miren cómo lo arreglamos!"
- **Ten ayudantes** si son 30 personas — el ejercicio principal se cae sin soporte 1-a-1.
- **Captura testimonios** al final (los pitches relámpago son oro para tu marketing 😉).

---

¿Quieres que te genere alguno de estos materiales completos? Te puedo armar **las slides en texto**, la **galería de 20 prompts**, la **hoja "Caza tu tarea dolorosa"**, o las **instrucciones base de los 3 asistentes de ejemplo** — listos para imprimir/copiar. Dime cuál atacamos primero.