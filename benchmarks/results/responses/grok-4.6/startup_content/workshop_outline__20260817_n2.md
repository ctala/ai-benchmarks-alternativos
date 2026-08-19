# Grok 4.6 — startup_content/workshop_outline

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 98.362s | tokens_per_second: 41.4
- input_tokens: 387 | output_tokens: 4074
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y dinámicas de bloques bien estructuradas.

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

**CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP**  
Workshop práctico · 3 horas · 20-30 emprendedores early-stage no técnicos

Tono del workshop: energético, directo, “manos a la obra”. Cero slides de historia de la IA. Desde el minuto 1: “Hoy sales de aquí con un asistente funcionando para tu startup”.

---

### 1. Agenda detallada (180 minutos)

| Horario     | Bloque                              | Min |
|-------------|-------------------------------------|-----|
| 00:00-00:15 | Bienvenida + Icebreaker + Contrato  | 15  |
| 00:15-00:35 | El momento: por qué ahora y para qué | 20  |
| 00:35-00:55 | Anatomía de un Asistente (sin código) | 20 |
| 00:55-01:20 | Demo en vivo: construyo uno en 12 min | 25 |
| 01:20-01:30 | Break                               | 10  |
| 01:30-02:30 | EJERCICIO PRINCIPAL: Construye el tuyo | 60 |
| 02:30-02:50 | Show & Tell + feedback rápido       | 20  |
| 02:50-03:00 | Cierre, recursos y siguiente paso   | 10  |

Buffer realista incluido. Si se atrasa el ejercicio, se recorta 5 min del Show & Tell.

---

### 2. Materiales necesarios (preparar antes)

**Facilitador**
- Laptop + HDMI + clicker + timer grande visible (proyector o pantalla)
- Wifi del venue testeado + hotspot de backup
- 2 cuentas listas: ChatGPT (Plus preferible para Custom GPT) y Claude o Gemini como plan B
- 30 copias impresas del **Canvas del Asistente IA** (1 página, ver ejercicio)
- Post-its de 3 colores + marcadores + cinta
- Música energética de entrada y del break (playlist lista)
- 3 ejemplos reales de startups Latam ya resueltos (e-commerce, servicio profesional, SaaS B2B)
- Lista de asistencia + stickers de “Asistente listo”
- Grupo de WhatsApp del workshop creado (se comparte al final)
- Agua, café y algo dulce para el break

**Participantes (comunicar 48 h antes)**
- Laptop + cargador (imprescindible)
- Cuenta gratuita en chat.openai.com (crear antes, no el día del workshop)
- Un dolor concreto de su startup escrito en una frase (pre-work de 2 minutos)
- Audífonos por si hay ruido

**Pre-work email (enviar 2 días antes)**  
Asunto: “Mañana sales con tu primer empleado IA. Trae esto.”  
Cuerpo corto, energético, con el link para crear cuenta y la pregunta: “¿Qué tarea repetitiva te quita 3+ horas a la semana?”

---

### 3. Bloques detallados

**Bloque 1 — Bienvenida + Icebreaker + Contrato**  
Duración: 15 min  
Objetivo: Bajar la ansiedad “yo no soy técnico” y alinear expectativas.  
Dinámica: Charla corta (3 min) + ronda rápida de 20 segundos por persona de pie (“Soy [nombre], mi startup hace X, la tarea que más odio es Y”) + contrato verbal (“Hoy no hay preguntas tontas, hay asistentes mal promptados”).  
Key takeaway: “No vas a programar. Vas a diseñar un empleado que trabaja 24/7.”

**Bloque 2 — El momento: por qué ahora y para qué**  
Duración: 20 min  
Objetivo: Que cada uno identifique 1-2 casos de uso reales en su startup (no “IA en general”).  
Dinámica: Charla con 4 casos Latam concretos (atención al cliente, calificación de leads, contenido, onboarding) + 4 min de discusión en parejas: “¿Dónde se te va el tiempo hoy?”.  
Key takeaway: “El asistente no reemplaza tu cerebro. Reemplaza las 15 tareas que haces como robot.”

**Bloque 3 — Anatomía de un Asistente (sin código)**  
Duración: 20 min  
Objetivo: Entender las 6 piezas que todo asistente necesita (rol, tareas, conocimiento, tono, límites, pruebas).  
Dinámica: Charla visual + llenado colectivo en vivo de un canvas de ejemplo (una startup de delivery de comida saludable).  
Key takeaway: “Un buen asistente = instrucciones claras + contexto de tu negocio + límites. El modelo ya es inteligente. Tú le das el trabajo.”

**Bloque 4 — Demo en vivo**  
Duración: 25 min  
Objetivo: Demostrar que se puede construir algo útil en menos de 15 minutos.  
Dinámica: Demo 100 % en vivo (nada grabado). Construyo un asistente para una startup ficticia de la sala usando ChatGPT (Custom GPT si hay Plus, si no system prompt + custom instructions). Pruebo 3 escenarios en caliente, muestro un fallo y lo corrijo en 30 segundos.  
Key takeaway: “Si yo lo hice mal a propósito y lo arreglé en vivo, tú también puedes.”

**Bloque 5 — Break**  
10 min. Música, café, “no hablen de la IA, hablen de su startup”.

**Bloque 6 — EJERCICIO PRINCIPAL** (ver sección 4)  
60 min

**Bloque 7 — Show & Tell + feedback**  
Duración: 20 min  
Objetivo: Validación social + aprendizaje cruzado.  
Dinámica: 6-7 voluntarios muestran 90 segundos su asistente (pantalla o leen el prompt + 1 prueba). El resto da 1 feedback con post-it: “Lo que más me gustó” / “Prueba esto”.  
Key takeaway: “El mejor asistente de la sala no es el más técnico. Es el que resolvió el dolor más concreto.”

**Bloque 8 — Cierre**  
Duración: 10 min  
Objetivo: Que se vayan con siguiente acción clara y sensación de “ya empecé”.  
Dinámica: Recap de 3 frases + entrega de recursos + foto grupal + stickers. Cierre: “Mañana úsalo 20 minutos con un cliente o un documento real. Eso es todo.”  
Key takeaway: “Hoy construiste la v1. La v2 la haces tú esta semana.”

---

### 4. Ejercicio principal (el que todos pueden hacer)

**Nombre:** “Tu primer empleado IA en 60 minutos”  
Herramienta: ChatGPT (gratis alcanza). Plan B: Claude.ai o Gemini.

**Material:** Canvas impreso de 1 página (frente y dorso):

Frente (diseño – 15 min en silencio + 5 min en pareja):
1. Nombre y rol del asistente (ej: “Martina, analista de clientes de [Startup]”)
2. El dolor que resuelve (1 frase)
3. 3-5 tareas concretas que SÍ debe hacer
4. Qué conocimiento necesita (pega aquí links, pega texto de tu web, FAQs, precios…)
5. Tono y personalidad (3 adjetivos + 1 ejemplo de frase)
6. Límites duros (qué NUNCA debe hacer o inventar)

Dorso (construcción – 30 min):
- Template de system prompt listo para copiar/pegar y personalizar (se los doy yo)
- Espacio para 3 pruebas reales que van a correr
- Caja de “iteración”: qué cambiaste después de la primera prueba

**Flujo del ejercicio (60 min cronometrados):**
- 0-5 min: Explico el canvas y el template (muy rápido)
- 5-20 min: Llenan el frente en silencio (música baja)
- 20-25 min: 1 minuto cada uno le cuenta a su vecino
- 25-50 min: Abren ChatGPT, pegan el template, personalizan, suben 1-2 documentos o pegan texto, corren las 3 pruebas, iteran
- 50-60 min: Dejan el asistente “presentable” y anotan 1 mejora para esta semana

Todo el mundo termina con algo que puede seguir usando el lunes. Los que tienen ChatGPT Plus pueden convertirlo en Custom GPT en los últimos 8 minutos (les muestro el botón).

---

### 5. Recursos para llevar a casa

Entregar en un solo PDF + carpeta Drive + grupo de WhatsApp:

- Canvas del Asistente IA (versión editable)
- Biblioteca de 12 system prompts listos (atención al cliente, calificación de leads, creador de contenido, analista de reuniones, onboarding, etc.)
- Checklist “Cómo alimentar a tu asistente con tus documentos reales”
- Lista corta de herramientas no-code (Custom GPTs, Poe, Chatbase, Voiceflow free tier, Make + OpenAI, WhatsApp + IA)
- Guía de 1 página: “3 pruebas que le tienes que hacer a tu asistente esta semana”
- Invitación al grupo de WhatsApp del workshop (solo participantes) para dudas las siguientes 2 semanas
- Oferta opcional: “Office hours” de 