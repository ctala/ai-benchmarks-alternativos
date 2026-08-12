# Ling 3.0 Flash — startup_content/workshop_outline

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.97 | quality: 9.72
- latency_total: 20.121s | tokens_per_second: 385.3
- input_tokens: 234 | output_tokens: 7753
- judge_score: 4.8 | justificación: 

## Respuesta completa

# 🚀 "Construye tu Asistente de IA para tu Startup"
### Workshop Presencial — 3 Horas | 20-30 emprendedores early-stage no-técnicos

---

## 📋 AGENDA COMPLETA (180 minutos)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 – 0:15 | 🔥 Apertura: "La IA ya llegó y no espera" | 15 min |
| 0:15 – 0:45 | 🧠 Bloque 1: El panorama IA para tu startup | 30 min |
| 0:45 – 1:15 | 🛠️ Bloque 2: Cómo funciona un asistente de IA (con demo en vivo) | 30 min |
| 1:15 – 1:25 | ☕ Break + Networking | 10 min |
| 1:25 – 2:15 | 🏗️ Bloque 3: Ejercicio principal — Construye tu asistente | 50 min |
| 2:15 – 2:45 | 🎤 Bloque 4: Presentación de prototipos + feedback | 30 min |
| 2:45 – 3:00 | 🎯 Cierre + Recursos + Próximos pasos | 15 min |

---

## 🎒 MATERIALES NECESARIOS (Preparar antes)

### Para el facilitador:
- [ ] Laptop con proyector HDMI/USB-C + cable
- [ ] Cuenta de ChatGPT Plus (o API key para demo en vivo)
- [ ] Cuenta de **Voiceflow** o **Botpress** pre-configurada (plataforma no-code para construir el asistente)
- [ ] Cuenta de **Make.com** o **Zapier** (para la demo de integraciones)
- [ ] Cuenta de **Google Slides** compartida (link en cada laptop o proyectado)
- [ ] Wi-Fi estable con contraseña visible en pantalla al entrar
- [ ] Timer visible (pantalla o proyectado)

### Para cada participante:
- [ ] Laptop con WiFi (traer la suya)
- [ ] Cuenta de **ChatGPT** creada previamente (free o Plus — enviar email pre-workshop con instrucciones)
- [ ] Cuenta de **Voiceflow** o **Botpress** creada previamente (registro 2 min — enviar email pre-workshop)
- [ ] Cuenta de **Make.com** o **Zapier** creada previamente (registro 2 min)
- [ ] Cuaderno / libreta para notas

### Para el espacio:
- [ ] Sala con mesas de 4-5 personas (configuración en parejas/grupos pequeños)
- [ ] Pizarra blanca o papel kraft grande + marcadores
- [ ] Post-its de 3 colores
- [ ] Marcadores gruesos
- [ ] Café, agua, snacks disponibles desde la entrada
- [ ] **Print de la "Quick-Start Guide"** (1 página, impresa para cada participante) — ver sección de recursos

### Pre-workshop (enviar 3-5 días antes):
- [ ] Email con: link de registro a Voiceflow/Botpress, link de registro a Make/Zapier, link de registro a ChatGPT, link al Google Slides del workshop, link a un video de 5 min introductorio opcional
- [ ] Encuesta corta (Typeform/Google Form): "¿Cuál es el mayor dolor de tu startup hoy?" (para personalizar la demo)
- [ ] Confirmar que todos tienen laptop funcional

---

## 📐 DETALLE DE CADA BLOQUE

---

### 🔥 BLOQUE 0 — Apertura: "La IA ya llegó y no espera"
**⏱ Duración:** 15 minutos (0:00 – 0:15)

**🎯 Objetivo:**
Crear energía desde el minuto uno. Que cada participante entienda que NO necesita saber programar para usar IA en su startup. Romper el mito de "la IA es solo para ingenieros."

**🎭 Dinámica:**
- **Min 0-3:** El facilitador entra con energía alta. Sin presentación formal larga. Empieza con una pregunta al público: *"¿Quién aquí ha usado ChatGPT esta semana?"* (levantar manos — generar energía). Luego: *"¿Y saben que con eso pueden construir un asistente que trabaje para su startup 24/7?"*
- **Min 3-8:** "El momento WTF" — Mostrar 3 ejemplos REALES de asistentes de IA construidos por startups no-técnicas en Latinoamérica (o similar):
  1. Una founder de e-commerce en Colombia que construyó un asistente de atención al cliente en 2 horas con Voiceflow + ChatGPT → redujo tickets en 60%
  2. Una startup de fintech en México que creó un onboarding assistant para sus usuarios → aumentó conversión de signup en 35%
  3. Un founder solo que automatizó su outreach con IA → 50 emails personalizados en 10 min
- **Min 8-13:** Reglas del juego: *"Hoy NO vamos a escribir código. Hoy vamos a ensamblar como si fuera LEGO. Al final del taller, cada equipo va a tener un prototipo funcional de su asistente de IA."*
- **Min 13-15:** Formar equipos de 3-4 personas (pre-asignados o por interés de industria). Cada equipo recibe una hoja de "Mission Brief" (1 página con el desafío de su asistente).

**💡 Key Takeaway:**
"La IA es un copiloto, no un reemplazo. Tú eres el director creativo — la IA hace el trabajo pesado."

**📊 Slide Count:** 5 slides

---

### 🧠 BLOQUE 1 — El Panorama IA para tu Startup
**⏱ Duración:** 30 minutos (0:15 – 0:45)

**🎯 Objetivo:**
Dar al participante un mapa mental claro de qué puede hacer la IA para su startup (y qué NO puede), sin jerga técnica. Que identifiquen 2-3 casos de uso concretos para su negocio.

**🎭 Dinámica:**
- **Min 0-10 — Charla rápida "IA 101 para Founders":**
  - ¿Qué es un LLM? Explicación con analogía: *"Imaginen que contrataron al empleado más leído del mundo, que trabaja en milisegundos, nunca duerme, y aprende de cada conversación."*
  - Los 3 tipos de IA que un founder necesita conocer HOY:
    1. **Generativa** (texto, imágenes) → ChatGPT, Claude, Gemini
    2. **Automatización** (conectar herramientas) → Make, Zapier, n8n
    3. **Conversacional** (asistentes, chatbots) → Voiceflow, Botpress, CustomGPT
  - Lo que la IA HACE bien para startups: responder FAQs, generar contenido, calificar leads, onboarding, resumir documentos, traducción
  - Lo que la IA NO hace bien (todavía): tomar decisiones de negocio complejas, manejar emociones humanas en crisis, reemplazar la relación con el cliente

- **Min 10-20 — Ejercicio individual "El Mapa de Dolor" (5 min):**
  - Cada participante escribe en un Post-it (color 1): **"El mayor problema operativo de mi startup que me roba tiempo"**
  - Se pega en la pizarra por categoría (Atención al cliente / Ventas / Operaciones / Marketing / Otros)
  - Facilitador agrupa rápidamente en la pizarra y señala patrones: *"¿Ven? El 70% de la sala tiene el mismo dolor: atención al cliente o gestión de leads. Eso es exactamente donde un asistente de IA brilla."*

- **Min 20-30 — Discusión en parejas (2 personas, 5 min):**
  - *"Elige UNA de esas categorías de dolor. ¿Cómo sería un asistente de IA que resuelva ese problema para tu startup?"*
  - Cada pareja comparte una idea en voz alta (facilitador toma nota en pizarra)

**💡 Key Takeaway:**
"Tu startup tiene al menos 1 problema que un asistente de IA puede resolver esta semana. No necesitas esperar a que la tecnología madure — las herramientas ya están aquí."

**📊 Slide Count:** 12 slides (visuales, con ejemplos de startups reales)

---

### 🛠️ BLOQUE 2 — Cómo Funciona un Asistente de IA (Demo En Vivo)
**⏱ Duración:** 30 minutos (0:45 – 1:15)

**🎯 Objetivo:**
Que los participantes entiendan la "arquitectura simple" de un asistente de IA (sin código) y vean una demo en vivo construida en tiempo real. Que se sientan capaces de replicarlo.

**🎭 Dinámica:**
- **Min 0-8 — Explicación visual "La Arquitectura del Asistente":**
  - Presentar los 3 componentes de un asistente de IA no-code:
    1. **🧠 El Cerebro** = ChatGPT / Claude (genera las respuestas inteligentes)
    2. **🗺️ El Mapa** = Voiceflow / Botpress (define el flujo de conversación — qué pregunta, qué responde, qué hace)
    3. **🔌 Las Conexiones** = Make / Zapier (conecta el asistente con Google Sheets, CRM, email, WhatsApp, etc.)
  - Analogía: *"Piensen en un restaurante. El Cerebro es el chef (prepara la respuesta), el Mapa es el mesero (sigue el flujo de la orden), y las Conexiones son la cocina y el sistema de pago (integran todo)."*
  - Diagrama simple en slide (visual, no técnico)

- **Min 8-22 — Demo en vivo: Construyendo un asistente de atención al cliente (14 min):**
  - **Min 8-10:** Abrir Voiceflow (o Botpress) en pantalla compartida. Mostrar la interfaz. *"Esto es lo que van a usar hoy. Es como PowerPoint pero para chatbots."*
  - **Min 10-14:** Crear un flujo simple paso a paso:
    1. Crear un "Intent" → el usuario dice "Quiero devolver un producto"
    2. Conectar a ChatGPT como motor de respuestas → *"Aquí le decimos a la IA qué tono usar y qué información tiene disponible"*
    3. Agregar un "Action" → cuando el usuario quiere devolver, enviar un email automático con Make/Zapier
    4. Probar el flujo EN VIVO escribiendo en el chat → la sala ve la magia en tiempo real
  - **Min 14-17:** Agregar una integración: conectar con Google Sheets → cada conversación del usuario se guarda en una hoja de cálculo. *"Así tienen datos de sus clientes sin escribir una línea de código."*
  - **Min 17-22:** Mostrar el resultado final: un asistente funcional que responde preguntas de producto, procesa devoluciones, y guarda todo en una hoja. *"Esto lo construimos en 12 minutos. Ustedes van a construir el suyo en 45 minutos."*

- **Min 22-28 — Q&A rápido + "Miedos comunes" (6 min):**
  - Responder las 3 preguntas más frecuentes que surgieron en la encuesta pre-workshop
  - *"¿Y si la IA dice algo incorrecto?"* → Se explica el concepto de "instrucciones de sistema" y "knowledge base" — la IA sigue las reglas que tú le das
  - *"¿Es caro?"* → Mostrar costos: Voiceflow free tier, ChatGPT free tier, Make free tier → prototipo por $0
  - *"¿Necesito saber de IA?"* → *"Necesitas saber de tu negocio. Eso es lo que importa."*

- **Min 28-30 — Transición al ejercicio:**
  - *"Ahora es su turno. En 45 minutos van a construir el prototipo de su propio asistente. Vamos a trabajar en equipos de 3-4."*

**💡 Key Takeaway:**
"Un asistente de IA es como armar un flujo en PowerPoint + conectar con herramientas que ya usas. No necesitas saber programar. Necesitas saber qué quiere tu cliente."

**📊 Slide Count:** 8 slides + demo en vivo (no slides, pero incluir en el timing)

---

### ☕ BREAK
**⏱ Duración:** 10 minutos (1:15 – 1:25)
- Café, agua, snacks
- Música de fondo energética
- Facilitador circula, responde dudas rápidas, motiva

---

### 🏗️ BLOQUE 3 — Ejercicio Principal: "Construye Tu Asistente"
**⏱ Duración:** 50 minutos (1:25 – 2:15)

**🎯 Objetivo:**
Que cada equipo tenga un prototipo FUNCIONAL y TESTEABLE de un asistente de IA para su startup, construido con herramientas no-code.

**🎭 Dinámica:**

**FASE 1: Planificación (10 min | 1:25 – 1:35)**
- Cada equipo recibe una **"Build Sheet"** (hoja impresa de 1 página con instrucciones paso a paso)
- Pasos:
  1. **Definir el caso de uso** (1 min): ¿Qué problema va a resolver tu asistente? (Atención al cliente / Generación de leads / Onboarding / Otro)
  2. **Escribir 5 preguntas de usuario** (3 min): Qué le va a preguntar el usuario al asistente
  3. **Definir las respuestas** (3 min): Escribir el "prompt del sistema" que va a guiar a la IA — usando la plantilla del facilitador
  4. **Definir 1 acción automatizada** (3 min): ¿Qué va a hacer el asistente además de responder? (enviar email, guardar en Google Sheets, agendar llamada, etc.)
- Facilitador y 1-2 ayudantes circulan entre mesas, resuelven dudas técnicas

**FASE 2: Construcción (25 min | 1:35 – 2:00)**
- Equipos abren **Voiceflow** o **Botpress** en sus laptops
- Siguen la guía visual paso a paso (impresa + en pantalla)
- El facilitador hace "rondas de checkpoint" cada 8 minutos:
  - **Min 8 (1:43):** *"¿Ya tienen el flujo básico? Muéstrenme el primer intent."*
  - **Min 16 (1:51):** *"¿Ya tienen la IA respondiendo? Pruébenlo entre ustedes."*
  - **Min 23 (1:58):** *"Faltan 7 minutos. Agreguen la acción automatizada y hagan una prueba final."*

**FASE 3: Pulir y Preparar Presentación (15 min | 2:00 – 2:15)**
- Cada equipo prepara una **mini-demo de 2 minutos** para presentar a la sala
- Usan esta estructura rápida (en pantalla):
  1. *"Nuestro asistente resuelve [PROBLEMA]"*
  2. *"Puede hacer [ACCIONES]"*
  3. *"La demo muestra [DEMO EN VIVO]"*
- Facilitador ayuda a los equipos que van más lentos (tener un "plan B" — un template pre-armado que puedan personalizar rápido)

**💡 Key Takeaway:**
"Si puedes armar un pitch deck, puedes construir un asistente de IA. Es más fácil de lo que piensas, y el resultado habla por sí solo."

**📊 Slide Count:** 5 slides (la guía visual del ejercicio proyectada)

---

### 🎤 BLOQUE 4 — Presentación de Prototipos + Feedback
**⏱ Duración:** 30 minutos (2:15 – 2:45)

**🎯 Objetivo:**
Que cada equipo presente su prototipo, reciba feedback constructivo de pares y del facilitador, y vean la diversidad de soluciones que surgieron de la misma herramienta.

**🎭 Dinámica:**
- **Min 0-2:** Instrucciones de presentación:
  - Cada equipo: **2 minutos de demo en vivo** + **1 minuto de feedback de la sala**
  - Regla de feedback: *"Una cosa que me gusta + una sugerencia para mejorar"*
- **Min 2-25:** Presentaciones (6-8 equipos × 3 min = ~20-24 min)
  - Facilitador proyecta la demo de cada equipo en pantalla
  - Anima, hace preguntas, celebra wins
  - Si un equipo tiene problemas técnicos, el facilitador ayuda a rescatar la demo
- **Min 25-28:** **"Wall de Wins"** — Cada equipo escribe en un Post-it (color 2): *"Lo más poderoso que descubrí hoy"* y lo pega en la pared
- **Min 28-30:** Facilitador lee 3-4 Post-its en voz alta, genera celebración grupal

**💡 Key Takeaway:**
"En 45 minutos, sin saber programar, cada equipo construyó algo funcional. La barrera de entrada a la IA es más baja que nunca — la diferencia es la velocidad con la que actúes."

**📊 Slide Count:** 5 slides (template de feedback, contador de tiempo, tips de presentación)

---

### 🎯 BLOQUE 5 — Cierre + Recursos + Próximos Pasos
**⏱ Duración:** 15 minutos (2:45 – 3:00)

**🎯 Objetivo:**
Dejar a cada participante con un plan de acción concreto, recursos para seguir construyendo, y una sensación de momentum.

**🎭 Dinámica:**
- **Min 0-5 — "Tu Plan de Acción en 3 Pasos"** (facilitador proyecta):
  1. **Esta semana:** Termina de armar tu asistente con los datos reales de tu startup (la plantilla que construiste hoy es el 70% del trabajo)
  2. **Esta semana:** Comparte el prototipo con 3 clientes reales y recoge feedback
  3. **Próximo mes:** Conecta tu asistente a tu CRM / herramienta de email y automatiza el flujo completo

- **Min 5-10 — Recursos para Llevar a Casa** (ver sección detallada abajo)
  - Facilitador recorre cada recurso brevemente (30 seg cada uno)
  - Entrega del **"AI Startup Toolkit"** (USB o link en QR proyectado)

- **Min 10-13 — "La Pregunta del Día":**
  - *"Si pudieras construir UN asistente de IA mañana para tu startup, ¿cuál sería?"*
  - 2-3 personas comparten en voz alta (rápido, energético)

- **Min 13-15 — Cierre:**
  - Facilitador cierra con un mensaje de poder: *"La IA no es el futuro de las startups. Es el presente. Y ustedes se fueron hoy con las herramientas para aprovecharlo AHORA. No necesitan permiso. No necesitan un equipo de ingenieros. Necesitan su próxima idea y 45 minutos."*
  - Foto grupal 📸
  - Entrega de certificado de participación (opcional, impreso)
  - Link al Google Form de feedback del workshop (3 min, 5 preguntas)

**💡 Key Takeaway:**
"La IA es un acelerador, no un sustituto. Tu ventaja competitiva no es la tecnología — es tu velocidad para implementarla."

**📊 Slide Count:** 5 slides

---

## 📦 RECURSOS PARA LLEVAR A CASA

### 📄 "AI Startup Toolkit" (entregar como PDF digital + link QR en la última slide)

| Recurso | Descripción | Link |
|---------|-------------|------|
| **Quick-Start Guide** | Hoja de 1 página con los pasos para replicar el asistente de hoy (capturas de pantalla + instrucciones) | Preparar como PDF |
| **Prompt Template Library** | 10 prompts listos para usar: atención al cliente, generación de contenido, calificación de leads, onboarding, etc. | Preparar como PDF |
| **Voiceflow / Botpress Tutorial** | Video de 10 min (grabado por el facilitador o tutorial oficial) para profundizar | Link a YouTube |
| **Make.com / Zapier Templates** | 5 templates de automatización listos para importar (ej: "Nuevo lead → Email automático → Google Sheets") | Links a templates públicos |
| **AI Tools Stack para Startups** | Lista curada de 20 herramientas no-code de IA organizadas por caso de uso (con costos y nivel de dificultad) | Preparar como PDF |
| **"AI for Startups" Reading List** | 5 artículos/ebooks esenciales para seguir aprendiendo | Preparar como PDF |
| **Community Slack / WhatsApp Group** | Canal para que los participantes se conecten, compartan avances y hagan preguntas post-workshop | Crear antes del workshop |
| **Certificate of Completion** | Certificado digital individual con nombre del participante | Generar con Canva |

### 📧 Email de seguimiento (enviar 24-48 horas después):
- Resumen del workshop con links a todos los recursos
- Grabación de la demo en vivo (si fue grabada)
- Link al Google Slides completo del workshop
- Invitación al grupo de comunidad (Slack/WhatsApp)
- Encuesta de feedback (si no se hizo en el cierre)
- Oferta de "Office Hours" virtual de 30 min para cada equipo (opcional, 1 semana después)

---

## 📊 SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides |
|---------|--------|
| Bloque 0 — Apertura | 5 |
| Bloque 1 — El Panorama IA | 12 |
| Bloque 2 — Cómo Funciona (Demo) | 8 |
| Bloque 3 — Ejercicio (guía visual) | 5 |
| Bloque 4 — Presentaciones | 5 |
| Bloque 5 — Cierre | 5 |
| **TOTAL** | **~40 slides** |

*Nota: Slides son visuales y mínimos. La mayor parte del contenido es demostración en vivo, ejercicio práctico y discusión. Los slides apoyan, no dominan.*

---

## 🏆 EJERCICIO PRINCIPAL DETALLADO

### "Build Your AI Assistant" — 45 minutos

**Contexto:** Cada equipo (3-4 personas) construye un prototipo funcional de un asistente de IA para su startup usando **Voiceflow** (o **Botpress**) + **ChatGPT** + **Make/Zapier**.

**El desafío del día:**
> *"Tu startup [nombre del equipo] recibe 50 consultas de clientes al día. Queremos un asistente de IA que pueda responder las preguntas más frecuentes, calificar leads interesados, y derivar casos complejos a una persona real."*

**Paso a paso (impreso en la Build Sheet):**

| Paso | Qué hacer | Tiempo |
|------|-----------|--------|
| 1 | Abre Voiceflow/Botpress en tu navegador | 2 min |
| 2 | Crea un nuevo proyecto llamado "[Nombre de tu startup] Assistant" | 1 min |
| 3 | Define 3 "Intents" (intenciones del usuario) — ej: "Pregunta de precio", "Quiero devolver", "Quiero hablar con un humano" | 5 min |
| 4 | Para cada Intent, escribe el "System Prompt" — la instrucción que le das a ChatGPT sobre cómo responder | 5 min |
| 5 | Diseña el flujo visual: conecta los Intents con las respuestas y las acciones | 10 min |
| 6 | Conecta Make.com/Zapier: cuando el usuario dice "Quiero devolver", envía un email automático con su info | 10 min |
| 7 | Prueba el asistente entre todos en el equipo | 5 min |
| 8 | Prepara la demo de 2 minutos | 5 min |
| 9 | Pulir y presentar | 7 min |

**Plantilla de System Prompt (proporcionada en la Build Sheet):**
```
Eres el asistente de IA de [NOMBRE DE TU STARTUP]. 
Tu empresa vende [QUÉ VENDEN]. 
Responde de forma amigable, directa y en español. 
Si no sabes la respuesta, di "Déjame consultar con mi equipo" y ofrece enviar un email.
Nunca inventes información sobre precios o productos.
Si el usuario parece frustrado, ofrece conectarlo con una persona.
```

**Criterios de éxito (checklist para facilitadores):**
- [ ] El equipo tiene al menos 3 Intents funcionales
- [ ] La IA responde con el tono correcto (amigable, profesional)
- [ ] Al menos 1 acción automatizada está conectada (email, Google Sheets, etc.)
- [ ] El equipo puede hacer una demo en vivo de 2 minutos
- [ ] Al menos un miembro del equipo puede explicar cómo funciona cada componente

---

## 💡 TIPS PARA EL FACILITADOR

1. **Energía > Perfección:** Si algo sale mal técnicamente, improviza y sigue. Los participantes recordarán la experiencia, no el error.
2. **Rondas de checkpoint:** Cada 8 min en la fase de construcción. Esto evita que equipos se queden atrás.
3. **Tener un "Plan B" listo:** Un template pre-construido en Voiceflow/Botpress que equipos atrasados puedan personalizar rápido.
4. **Rotar entre mesas:** Dedica 2-3 min a cada equipo en cada checkpoint. Las preguntas típicas son: "¿dónde está el botón de...?" y "¿cómo conectamos con...?"
5. **Celebración constante:** Cuando un equipo logra algo (por pequeño que sea), hazlo público: *"¡Ese equipo acaba de hacer que su IA envíe un email! Eso es nivel Netflix."*
6. **El tono es TODO:** Eres un coach, no un profesor. Habla como si les estuvieras mostrando un truco genial, no como si dieras una clase.

---

*"No se trata de que los fundadores se conviertan en ingenieros de IA. Se trata de que se conviertan en directores creativos de IA."*