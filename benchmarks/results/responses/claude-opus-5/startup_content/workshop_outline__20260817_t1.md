# Claude Opus 5 — startup_content/workshop_outline

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.83 | quality: 10.0
- latency_total: 120.149s | tokens_per_second: 68.2
- input_tokens: 314 | output_tokens: 8192
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y materiales necesarios para el taller.

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

# 🚀 Construye tu Asistente de IA para tu Startup — Workshop Práctico
**Duración:** 3 horas presenciales · **Audiencia:** 20–30 fundadores early-stage NO técnicos · **Formato:** 70% manos en el teclado, 30% charla

---

## 🎯 PROMESA DEL WORKSHOP (la que se anuncia y se cumple)

> "Entras con una tarea que te roba 5 horas a la semana. Sales con un asistente de IA funcionando, entrenado con la información de TU negocio, y un plan de 7 días para ponerlo a trabajar con tu equipo. Cero código. Cero teoría de más."

**Métrica de éxito del facilitador:**
- ≥ 80% de los asistentes salen con un asistente **probado y funcionando**
- ≥ 90% completan el "Plan de 7 días"
- 0 personas atrapadas en problemas de cuenta/login (por eso el pre-work es obligatorio)

---

## 📅 1. AGENDA DETALLADA

| Hora | Bloque | Duración | Modalidad |
|---|---|---|---|
| 00:00 – 00:10 | **B0.** Arranque + Check de setup | 10 min | Ritual + logística |
| 00:10 – 00:25 | **B1.** "Tu competencia ya tiene un empleado que no duerme" | 15 min | Charla + demo shock |
| 00:25 – 00:45 | **B2.** Anatomía de un asistente de IA (sin tecnicismos) | 20 min | Charla + demo en vivo |
| 00:45 – 01:00 | **B3.** Diagnóstico: ¿qué tarea delegas primero? | 15 min | Ejercicio individual + pares |
| 01:00 – 01:10 | ☕ **PAUSA** activa (café + networking dirigido) | 10 min | Break |
| 01:10 – 02:10 | **B4.** 🔬 **LABORATORIO: Construye tu asistente** | 60 min | Ejercicio principal (4 sprints) |
| 02:10 – 02:25 | **B5.** Feria de Asistentes (demos relámpago) | 15 min | Demos + feedback |
| 02:25 – 02:40 | **B6.** De juguete a herramienta: equipo, costos y riesgos | 15 min | Charla + discusión |
| 02:40 – 02:55 | **B7.** Plan de 7 días + compromiso público | 15 min | Ejercicio + cierre |
| 02:55 – 03:00 | **B8.** Recursos, comunidad y siguiente paso | 5 min | Cierre |

**Total: 180 minutos** · Slides totales estimados: **58**

---

## 🧰 2. MATERIALES NECESARIOS

### A. Pre-work OBLIGATORIO (email + WhatsApp, 48h antes)

> **Asunto: 3 tareas de 10 minutos para no perder tiempo el sábado 🔧**

1. **Crear/verificar cuenta** de la herramienta principal (ver Plan A/B/C abajo). *Incluir video de 90 segundos mostrando cómo.*
2. **Traer 3 documentos reales** de su negocio en PDF/Word/texto (los que sea: catálogo de productos, lista de precios, FAQ de clientes, guion de ventas, políticas, propuesta comercial, últimos 10 mensajes de clientes). **Sin datos sensibles de terceros.**
3. **Responder 1 pregunta en el formulario:** *"¿Cuál es la tarea repetitiva que más odias de tu semana?"* → El facilitador lee las respuestas ANTES y ajusta ejemplos a la sala. **Esto es lo que hace que el workshop se sienta hecho a la medida.**

### B. Estrategia de herramientas (crítico en LatAm: no todos pagan USD)

| Plan | Herramienta | Costo | Para quién |
|---|---|---|---|
| **A (default)** | **Gemini → "Gems"** | Gratis con cuenta Google | Todos. Es el estándar de la sala. |
| **B** | **ChatGPT → "Projects"/GPTs** o **Claude → "Projects"** | ~USD 20/mes | Quien ya paga suscripción |
| **C (emergencia)** | **"Prompt Maestro"** pegado en cualquier chat gratuito | Gratis | Wifi malo, cuenta trabada, celular únicamente |

> ⚠️ **Regla de oro del facilitador:** enseñas UN camino (Plan A) desde el proyector. Los del Plan B trabajan en paralelo con la misma plantilla. El Plan C garantiza que **nadie se queda fuera**.

### C. Sala y logística

- [ ] Wifi + **hotspot de respaldo** (2 celulares con datos) + red alterna probada
- [ ] **Regletas / extensiones** (1 por cada 4 personas) — el asesino silencioso de workshops
- [ ] Mesas en islas de 5–6 personas (formato taller, no auditorio)
- [ ] Proyector + adaptadores + **timer grande visible** en pantalla
- [ ] Post-its 3 colores + marcadores gruesos + papel rotafolio
- [ ] Tarjetas de nombre: **Nombre / Startup / "Mi asistente hará: ______"**
- [ ] Café y algo salado a la mano desde el minuto 0

### D. Materiales del facilitador

- [ ] **Cuaderno de trabajo impreso** (8 páginas, ver sección 5) — impreso, no solo digital
- [ ] **Slides** (58) con QR grande en la slide de cada sprint
- [ ] **Carpeta de Drive "Kit del Workshop"** con: plantilla M.A.R.C.O., 12 recetas de asistentes, checklist de privacidad, plan 7 días
- [ ] **Asistente demo pre-construido** ("Sofía, la SDR de Tostado Café") + su versión "mala" para comparar
- [ ] **Kit de emergencia:** documentos ficticios de una startup ("Tostado Café" – catálogo, precios, FAQ, 15 mensajes de clientes) para quien llegue sin material
- [ ] **Grupo de WhatsApp** creado y con link en QR
- [ ] 2–3 **"ángeles" voluntarios** (perfiles algo más técnicos) para apoyo en el laboratorio → 1 ángel por cada 8 personas

---

## 🧩 3. DESGLOSE POR BLOQUE

### B0 · Arranque + Check de setup — 10 min
**Slides: 4**

- **Objetivo:** que el 100% de la sala tenga la herramienta abierta y funcionando ANTES de que empiece el contenido.
- **Dinámica:** Ritual de arranque. Todos abren su herramienta y escriben *"Hola, soy [nombre], fundador de [startup]"*. Levantan la mano quien **no** ve respuesta → los ángeles van directo a esas mesas. Mientras, la sala hace un check-in de 20 segundos por mesa: *"nombre, startup, la tarea que odio"*.
- **Frase gancho:** "En este workshop hay una sola regla: nadie se va sin algo que funcione. Si algo no te funciona, levanta la mano rápido y fuerte."
- **Key takeaway:** *Esto no es una conferencia. Es un taller y tú eres el que construye.*

---

### B1 · "Tu competencia ya tiene un empleado que no duerme" — 15 min
**Slides: 8**

- **Objetivo:** generar urgencia real y **matar el mito** de que "usar IA" = "hacerle preguntas a ChatGPT".
- **Dinámica:**
  1. **Demo shock (5 min):** el facilitador hace la MISMA pregunta a (a) un chat genérico y (b) al asistente demo "Sofía" entrenado con los datos de Tostado Café. Pregunta: *"Un cliente me pide descuento por 200 unidades, ¿qué le respondo?"*. El chat genérico da un consejo de manual; Sofía responde con los precios reales, la política de volumen y el mensaje listo para copiar y pegar a WhatsApp.
  2. **Charla (7 min):** la diferencia no es la IA, es el **contexto**. 3 mini-casos LatAm de fundadores no técnicos (ventas, soporte, contenido) con números concretos de horas ahorradas.
  3. **Encuesta a mano alzada (3 min):** "¿Quién usa IA todos los días? ¿Quién le ha *enseñado* algo sobre su negocio?" → el gap visible es el aprendizaje.
- **Key takeaway:** *ChatGPT genérico es un consultor que nunca leyó tu empresa. Un asistente es un empleado que sí. La diferencia la construyes en 40 minutos.*

---

### B2 · Anatomía de un asistente de IA (sin tecnicismos) — 20 min
**Slides: 12**

- **Objetivo:** entregar UN framework memorizable para escribir instrucciones y mostrar el proceso completo en vivo, de cero a funcionando, en menos de 8 minutos.
- **Dinámica:**
  - **Charla (8 min):** El framework **M.A.R.C.O.** — las 5 piezas de todo asistente:

    | Letra | Pieza | Pregunta que responde | Ejemplo |
    |---|---|---|---|
    | **M** | Misión | ¿Qué hace y qué NO hace? | "Redactas respuestas de WhatsApp a clientes que piden cotización." |
    | **A** | Audiencia | ¿Con quién habla y en qué tono? | "Dueños de cafeterías en Bogotá. Tono cálido, tuteo, sin corporativismos." |
    | **R** | Reglas | ¿Los límites y cuándo llama a un humano? | "Nunca inventes precios. Nunca ofrezcas descuentos >10%. Si preguntan por temas legales, escala a Ana." |
    | **C** | Contexto | ¿Qué debe saber de tu negocio? | Catálogo, precios, políticas, casos de éxito (documentos cargados). |
    | **O** | Output | ¿Cómo se ve la respuesta perfecta? | "Máximo 4 líneas. Termina siempre con una pregunta. Formato listo para copiar." |

  - **Demo en vivo (10 min):** el facilitador construye un asistente de cero en pantalla, narrando cada campo con M.A.R.C.O. **Incluye a propósito un fallo** (el asistente inventa un dato) y lo corrige agregando una regla → modela que iterar es normal.
  - **Q&A rápido (2 min).**
- **Key takeaway:** *M.A.R.C.O. Si tu asistente falla, es porque le falta una de las 5 letras.*

---

### B3 · Diagnóstico: ¿qué tarea delegas primero? — 15 min
**Slides: 6**

- **Objetivo:** que cada persona elija **UN solo** caso de uso, el correcto, antes de tocar el teclado. (El error #1 de los principiantes: querer automatizar todo y no terminar nada.)
- **Dinámica:**
  1. **Individual, 5 min — "El robo de la semana":** en post-its, escriben 6–8 tareas repetitivas de su semana (1 por post-it) y les asignan horas semanales.
  2. **Filtro 3×T (3 min):** se quedan solo con las que cumplen las tres:
     - **Texto** (se hace escribiendo o leyendo)
     - **Tediosa** (se repite ≥3 veces por semana)
     - **Tolerable** (si sale mal, no se cae la empresa ni te demandan)
  3. **En parejas, 5 min:** cada uno presenta su tarea finalista en 60 segundos. El otro hace UNA pregunta: *"¿podrías reconocer una respuesta buena de una mala en 5 segundos?"* Si la respuesta es no, el caso de uso es demasiado difuso → elegir otro.
  4. **2 min:** escriben el ganador en la tarjeta de nombre: *"Mi asistente hará: ______"*.
- **Key takeaway:** *Un asistente, una tarea, una semana. El primero no es el mejor: es el que terminas hoy.*

---

### ☕ PAUSA — 10 min
**Slides: 1** (con la consigna del break en pantalla)

- **No es un break muerto:** en pantalla, la consigna → *"Encuentra a alguien con un caso de uso PARECIDO al tuyo y siéntense juntos en el laboratorio."* Se ahorra 15 minutos de bloqueos después.
- Los ángeles resuelven problemas de cuentas/documentos durante el break.

---

### B4 · 🔬 LABORATORIO: Construye tu asistente — 60 min
**Slides: 10** (una slide-instrucción por sprint, con timer y QR)

> **Este es el corazón del workshop.** Ver detalle completo en la sección 4.

- **Objetivo:** cada participante sale con un asistente creado, alimentado con sus documentos y probado con casos reales.
- **Formato:** 4 sprints cronometrados. En cada uno: instrucción de 90 segundos desde el proyector → trabajo en silencio con timer visible → 60 segundos de "check de mesa" (¿todos vamos?). Facilitador + ángeles rotan permanentemente. **Música de fondo durante el trabajo.**
- **Key takeaway:** *No necesitas saber programar. Necesitas saber explicar tu negocio por escrito.*

---

### B5 · Feria de Asistentes (demos relámpago) — 15 min
**Slides: 3**

- **Objetivo:** validación social, aprendizaje cruzado y el "efecto wow" que hace que la gente cuente el workshop.
- **Dinámica:**
  - **Ronda de mesa (6 min):** en cada isla, todos muestran su asistente en 45 segundos al vecino. La mesa vota al mejor.
  - **Demos al frente (9 min):** 3 ganadores pasan, 2 min cada uno: *(1) qué tarea resuelve, (2) demo en vivo con una pregunta del público, (3) qué le costó más*. El facilitador aplaude fuerte y nombra lo que hizo bien en términos de M.A.R.C.O.
- **Key takeaway:** *En 60 minutos, 25 fundadores no técnicos construyeron 25 herramientas. El techo no es la tecnología, es la claridad.*

---

### B6 · De juguete a herramienta: equipo, costos y riesgos — 15 min
**Slides: 10**

- **Objetivo:** evitar las 3 formas típicas de morir después del workshop: (1) el asistente se queda en tu laptop, (2) alucina y quema un cliente, (3) subes datos que no debías.
- **Dinámica:** charla rápida + discusión abierta con 3 preguntas plantadas.
  1. **Compartir con el equipo:** cómo dar acceso al asistente, y el hábito clave: **una carpeta viva de conocimiento** que alguien actualiza cada semana.
  2. **Escalera de madurez (sin promesas falsas):** `Asistente personal → Asistente compartido con el equipo → Conectado a tu WhatsApp/web con herramientas no-code → Desarrollo a medida`. Se nombran opciones no-code para el paso 3 y se aclara: **eso es el workshop 2, no lo intentes esta semana.**
  3. **Riesgos, sin drama pero sin ingenuidad:**
     - **Alucinaciones:** la regla *"la IA redacta, el humano firma"*. Nunca output directo al cliente sin revisión, en las primeras 2 semanas.
     - **Datos:** checklist rojo → NO subir cédulas/DNI, datos bancarios, historiales médicos, bases de datos de clientes completas, contratos con NDA. Revisar la configuración de "usar mis datos para entrenar".
     - **Dependencia:** documenta tus instrucciones en un Doc propio. Si mañana cambias de herramienta, tu M.A.R.C.O. se muda contigo.
  4. **Costos reales:** de USD 0 a USD 20/mes cubre el 90% de lo que un early-stage necesita este trimestre.
- **Key takeaway:** *La IA redacta, el humano firma. Y lo que no le contarías a un becario nuevo, no lo subas.*

---

### B7 · Plan de 7 días + compromiso público — 15 min
**Slides: 3**

- **Objetivo:** convertir el entusiasmo del sábado en un hábito del lunes.
- **Dinámica:**
  1. **Individual (7 min):** llen