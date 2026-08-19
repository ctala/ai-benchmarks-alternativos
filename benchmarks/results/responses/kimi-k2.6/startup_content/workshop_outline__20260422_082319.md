# Kimi K2.6 — startup_content/workshop_outline

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.6 | quality: 9.72
- latency_total: 467.21s | tokens_per_second: 15.3
- input_tokens: 218 | output_tokens: 7169
- judge_score: 4.8 | justificación: 

## Respuesta completa

 Aquí tienes el outline completo, diseñado para que salgan habiendo **construido algo real**, no solo teoría.

---

# 🤖 Construye tu Asistente de IA para tu Startup — Workshop Práctico
**Audiencia:** Emprendedores early-stage, no-técnicos (20-30 pax)  
**Duración:** 3 horas presenciales  
**Formato:** 30% charla/demo / 70% hacer

---

## 1. AGENDA DETALLADA (3 Horas Cronometradas)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 - 0:15 | 🔥 Bienvenida: El Fundador vs. El Robot | 15 min |
| 0:15 - 0:45 | 🩺 Diagnóstico: ¿Dónde te está doliendo? | 30 min |
| 0:45 - 1:15 | 🧰 El Arsenal: Herramientas No-Code | 30 min |
| 1:15 - 1:30 | ☕ Break + Setup Técnico | 15 min |
| 1:30 - 2:30 | 🛠️ Laboratorio: Build Session (Ejercicio Principal) | 60 min |
| 2:30 - 2:50 | ⚔️ Ring de Batalla: Test & Itera | 20 min |
| 2:50 - 3:00 | 🚀 Cierre: Roadmap de 7 Días | 10 min |

---

## 2. MATERIALES NECESARIOS (Preparar Antes)

### Logística del Salón
- WiFi de alta capacidad (30 personas consumiendo IA simultáneo; pide al venue banda ancha dedicada).
- Proyector + HDMI + adaptadores (USB-C/HDMI).
- 3 regletas largas con tomas de corriente repartidas por el salón.
- Micrófono inalámbrico si el salón es grande.
- Agua, café y snacks para el break.

### Para Cada Participante (Físico)
- **Canvas del Asistente** impreso (1 por persona, tamaño A4 o A3).
- **Plantilla de System Prompt** impresa (1 por persona).
- Post-its pequeños y marcadores.
- Sticker de "IA Team Member" para laptop (puro marketing/emoción).

### Digitales / Pre-Work (Enviar 48h antes por email/WhatsApp)
- **Checklist previa:** Traer laptop cargada, tener cuenta de Google activa, traer un archivo PDF/Word sobre su startup (precios, FAQ, propuesta de valor, tono de marca).
- **Plan B:** Tener 3 cuentas de Google "demo" creadas por si alguien olvida la suya.
- **Backup offline:** Descargar la plantilla del prompt en PDF por si se cae el internet.

---

## 3. BLOQUES DETALLADOS

### 🔥 Bloque 0: Bienvenida — El Fundador vs. El Robot
- **Duración:** 15 min
- **Dinámica:** Icebreaker + Charla.
  - *Actividad:* Cada uno saluda a su vecino durante 30 segundos **simulando ser un chatbot de atención al cliente mal programado** (respuestas robóticas, loops infinitos). Ríen, bajan la ansiedad técnica.
  - Luego, el facilitador comparte la promesa: "Hoy sales con un empleado digital que trabaja gratis los domingos".
- **Objetivo:** Eliminar el miedo a "lo técnico" y alinear expectativas prácticas.
- **Key Takeaway:** *No necesitas ser programador para delegar en IA. Necesitas ser claro, como con cualquier nuevo empleado.*
- **Slides:** 5

---

### 🩺 Bloque 1: Diagnóstico — ¿Dónde te está doliendo?
- **Duración:** 30 min
- **Dinámica:** Charla corta (10 min) + Ejercicio individual (20 min).
  - **Charla:** El facilitador presenta los 4 "Dolores Clásicos" del early-stage: (1) Responder lo mismo 20 veces al día, (2) Calificar leads sin criterio, (3) Onboarding manual, (4) Perder ventas por no atender rápido.
  - **Ejercicio:** Cada uno rellena el *Canvas del Asistente* respondiendo: ¿Qué tarea hago hoy que me roba energía creativa? ¿Qué información necesita saber alguien para hacerla por mí? ¿Qué tono debe usar (formal, cercano, irreverente)?
- **Objetivo:** Identificar UNA tarea específica, medible y repetitiva para automatizar hoy.
- **Key Takeaway:** *No automatices todo tu negocio. Automatiza la tarea que, si dejas de hacerla, tu startup sigue respirando.*
- **Slides:** 8

---

### 🧰 Bloque 2: El Arsenal — Herramientas No-Code
- **Duración:** 30 min
- **Dinámica:** Demo en vivo (20 min) + Discusión en parejas (10 min).
  - El facilitador hace **3 micro-demos proyectando su pantalla** (sin asumir conocimiento previo):
    1. **Google AI Studio** (gratis): Cómo subir un PDF de una startup real y hacer preguntas.
    2. **ChatGPT (GPT personalizado)**: Si tienen Plus, es el Ferrari; si no, el prompt sirve igual.
    3. **Make + Gmail** (vista rápida): Cómo conectar el asistente para que responda emails automáticamente (solo se muestra, no se construye).
  - Luego, en parejas, discuten: "¿Cuál de estas resuelve MI dolor de hoy?"
- **Objetivo:** Mostrar que el stack existe, es accesible en LATAM y no requiere tarjeta de crédito corporativa.
- **Key Takeaway:** *Por $0 a $20 dólares al mes tienes un equipo de operaciones que no duerme, no pide vacaciones y no renuncia.*
- **Slides:** 10

---

### 🛠️ Bloque 3: Laboratorio — Build Session (Ejercicio Principal)
- **Duración:** 60 min
- **Dinámica:** Ejercicio guiado paso a paso. Todos con laptop abierta.
- **Objetivo:** Salir con un asistente funcional, probado y personalizado.
- **Key Takeaway:** *Tu asistente es tan bueno como tus instrucciones y tu base de conocimiento. Un mal prompt = un mal empleado.*

**Desarrollo de los 60 min (cronometrados en pantalla):**

| Min | Actividad |
|-----|-----------|
| 0-10 | **Paso 1 — Elige el trabajo:** Usando el Canvas del Bloque 1, escribe en una oración: "Mi asistente ayudará a [X] a hacer [Y] sin [Z]". Ej: "Mi asistente ayudará a calificar leads sin que yo lea cada email". |
| 10-25 | **Paso 2 — Dalle personalidad:** Rellenan la *Plantilla de System Prompt* (rol, tono, reglas duras, qué NO debe decir, formato de salida). El facilitador muestra un ejemplo en vivo. |
| 25-40 | **Paso 3 — Dale memoria:** Suben su archivo de conocimiento (PDF/Word de su startup) a Google AI Studio o lo pegan en el prompt si usan ChatGPT. |
| 40-55 | **Paso 4 — Ponlo a chambear:** Testean con 3 escenarios reales: (1) Cliente feliz, (2) Cliente enojado, (3) Cliente que pregunta algo que NO está en la base de conocimiento. |
| 55-60 | **Paso 5 — Guarda y copia:** Guardan el prompt final, el link de la conversación y lo pegan en un doc. |

- **Slides:** 12 (uno por paso + screenshots grandes y legibles)

---

### ⚔️ Bloque 4: Ring de Batalla — Test & Itera
- **Duración:** 20 min
- **Dinámica:** Speed-dating de pruebas.
  - Forman parejas. Por 7 min: Persona A es el "cliente más difícil del mundo" (exigente, vago, enojón) y Persona B observa cómo su asistente responde desde la laptop de B. Luego invierten roles.
  - Los últimos 6 min son *shares rápidos* al grupo: "¿En qué falló tu asistente? ¿Qué ajustaste?"
- **Objetivo:** Identificar huecos en el conocimiento y aprender a iterar prompts en caliente.
- **Key Takeaway:** *Si tu asistente no falló en el taller, fallará con tu cliente real. Mejor descubrirlo ahora.*
- **Slides:** 3

---

### 🚀 Bloque 5: Cierre — Roadmap de 7 Días
- **Duración:** 10 min
- **Dinámica:** Charra rápida + Compromiso público.
  - El facilitador proyecta el "Checklist de la Semana 1": Conectar a WhatsApp/Email, probar con 5 clientes reales, medir tiempo ahorrado.
  - Compromiso rápido: Cada uno dice en voz alta a su vecino: *"Esta semana voy a poner a trabajar a mi asistente en..."*
  - Entrega de recursos (QR a carpeta de drive + plantillas).
- **Objetivo:** Asegurar que no muera en el drive.
- **Key Takeaway:** *Un asistente guardado en tu laptop no vende. Hay que ponerlo a chambear.*
- **Slides:** 4

---

## 4. EJERCICIO PRINCIPAL DEL WORKSHOP
**Nombre:** *"Tu Primer Empleado Digital en 60 Min"*

**Qué hacen:** Cada emprendedor construye, entrena y prueba un asistente conversacional para UNA tarea específica de su startup usando una herramienta gratuita (Google AI Studio) o su cuenta de ChatGPT.

**Cómo funciona paso a paso (para no-técnicos):**

1. **Define el puesto:** Escribe el "contrato" de tu asistente. Ejemplo: "Eres el community manager de una fintech mexicana. Tu trabajo es responder DMs de Instagram sobre cómo funciona nuestra tarjeta de crédito virtual."
2. **Dale un manual de inducción (System Prompt):** Usa la plantilla para decirle quién es, cómo debe hablar (¿"tú" o "usted"?), qué información puede compartir y qué debe escalar a un humano.
3. **Dale contexto (Knowledge Base):** Sube el archivo real de tu startup (lista de precios, FAQ, pitch). Esto es su "biblia".
4. **Simulacro de atención:** Escribe 3 mensajes de clientes reales (o inventados) y ve cómo responde. Si dice algo raro, corrige el prompt. Es como entrenar a un practicante.
5. **Exporta:** Copia el prompt final y guárdalo. Ese es tu "receta" para usarlo esta semana.

**Por qué todos pueden hacerlo:** No se escribe código. Es llenar espacios en blanco, subir un PDF y chatear. Si sabes usar Gmail, puedes hacer esto.

---

## 5. RECURSOS PARA LLEVAR A CASA
*(Entregar vía QR impreso en tarjeta + link en email post-evento)*

1. **📋 Canvas del Asistente de IA** (PDF editable) — para diseñar futuros bots.
2. **📝 Plantilla Madre de System Prompt** (Google Docs / Notion) — copiar y pegar.
3. **⚖️ Comparativa de Herramientas para LATAM** — Gratis vs. Pago, con precios aproximados en USD y qué país las acepta fácil.
4. **📹 Grabación de las Demos** — video corto de 10 min subido a Drive.
5. **🧠 Cheat Sheet: 30 Prompts para Operar tu Startup** — ventas, marketing, atención, finanzas.
6. **💬 Grupo de WhatsApp/Telegram del Taller** — para dudas durante los 7 días siguientes.
7. **🎁 Bonus:** Guía *"Cómo conectar tu asistente a WhatsApp Business sin saber programar"* (usando herramientas tipo Wati/Trengo).

---

## 6. SLIDE COUNT ESTIMADO POR SECCIÓN

| Sección | Slides | Notas |
|---------|--------|-------|
| Bienvenida & Mindset | 5 | Incluye foto de un café derramado vs. un bot trabajando. |
| Diagnóstico | 8 | Muestra los 4 dolores + ejemplo de canvas lleno. |
| Arsenal de Herramientas | 10 | Screenshots grandes, precios en USD, logos claros. |
| Laboratorio (Build) | 12 | Un slide por paso. Texto enorme para que se lea desde atrás. |
| Ring de Batalla | 3 | Instrucciones + temporizador en pantalla. |
| Cierre & Next Steps | 4 | Checklist visual + QR gigante a los recursos. |
| **TOTAL** | **~42 slides** | Ritmo rápido: ~14 slides/hora. Nada denso. |

---

### 💡 Tip Final para el Facilitador
> **Repite como mantra:** *"No estamos aquí para crear Skynet. Estamos aquí para que dejes de responder '¿Cuál es el precio?' 40 veces al día."*

Esa frase resume el espíritu: **práctico, rentable y sin código.**