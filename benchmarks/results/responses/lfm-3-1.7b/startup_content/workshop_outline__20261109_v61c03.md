# LFM-3 1.7B — startup_content/workshop_outline

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 7.75 | quality: 8.32
- latency_total: 30.011s | tokens_per_second: 273.0
- input_tokens: 203 | output_tokens: 8192
- judge_score: 3.8 | justificación: 

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

We need to create a complete outline for a 3-hour in-person workshop titled "Construye tu Asistente de IA para tu Startup - Workshop Practico". Audience: early-stage non-technical entrepreneurs (20-30 people). So, we need to keep it practical and energetic, not academic.

Structure requested:
- Agenda detailed with times (3 hours total)
- Materials needed (prepare before)
- For each block: Title & duration, Objective, Dynamic (charla, ejercicio, demo, discusion), Key takeaway.
- Principal exercise of the workshop (all can do).
- Resources to take home.
- Estimated slide count per section.

Let's plan:

Total time: 180 minutes = 3 hours. We'll divide into sections.

Given audience is non-tech, so focus on high-level concepts, simple steps, tools like chatbots, automation, etc. They might have some basic understanding? Not sure but non-technical implies minimal tech skills; we should avoid jargon or explain simply.

Title: "Construct your AI Assistant for your Startup - Practical Workshop"

Possible blocks:

1. Intro & Icebreaker (15 min) - set stage, objectives, expectations. Maybe quick poll.
2. What is an AI Assistant? Real-life use cases for startups (10-5 min talk + interactive?). 
3. Core Components (AI assistant building basics): Prompt engineering, data input, responses (maybe 40 min?) Could be more than 40.
4. Choosing the right tool/platform (like ChatGPT, Claude, local LLM) - decision criteria.
5. Hands-on: Building a simple prompt template using a no-code platform or even free tier? Since they're non-technical, maybe we simulate by writing prompts and using a draft AI? But if possible, we could show a pre-made interface or walk them through creating one step-by-step? Might be limited. I'll propose using a collaborative doc where they write prompts, then test via an online generator.
6. Demo: Live generation of a response to illustrate capabilities.
7. Turning prompts into workflows (automation ideas for startup tasks). Exercise.
8. Main Exercise: Build an AI-powered lead intake form or FAQ bot. All participants do together.
9. Wrap-up & Next Steps.

But we need exactly time breakdown within 3 hours. Let's design around 5 main segments plus breaks. Also include Q&A at end.

Outline:

- Total: 180 mins

Segment A: Welcome & Context (15 min)
   * Title: "Welcome y objetivo del taller"
   * Duration: 15
   * Objective: Introduce workshop purpose, who we are, what they'll get out.
   * Dynamic: Charla + icebreaker poll (quick intro names, current startup stage).
   * Key takeaway: You'll leave knowing you can harness AI as a side-hustle tool.

Break: 5 min (optional rest)

Segment B: ¿Qué es un asistente de IA? Casos reales (10 min)
   * Title: "¿Qué es un Asistente de IA?"
   * Duration: 10
   * Objective: Define AI assistant, differentiate from regular chatbots.
   * Dynamic: Charla short, maybe video clips (but we can just describe). Use visual aids.
   * Key takeaway: It acts as a personal copilot, reduces repetitive tasks, generates content.

Segment C: Componentes esenciales (30 min)
   * Title: "Componentes clave para crear tu propio asistente"
   * Duration: 30
   * Break down: 
        - Input: Prompts, data sources, context (what info you give)
        - Model/Tool: Choose language model, fine-tune vs prompt.
        - Output formatting & moderation.
   * Dynamic: Mini-lecture + interactive quiz.
   * Key takeaway: Three pillars: Clear prompt, reliable model, iterative refinement.

Segment D: Elegir la herramienta adecuada (15 min)
   * Title: "Cuál plataforma usar?"
   * Duration: 15
   * Objective: Compare options without deep technicality.
   * Dynamic: Group discussion, show pros/cons (e.g., free tier vs enterprise, ease of use, cost).
   * Key takeaway: Start with what you already have (Google, Slack) or try free tiers.

Break: 5 min

Segment E: Ejercicio práctico 1 – Crear tu primer prompt (20 min)
   * Title: "Tu primer prompt en 5 minutos"
   * Duration: 20
   * Objective: Write a prompt that yields a useful output (e.g., answer a common question about product, generate sales email, troubleshoot).
   * Dynamic: Small groups share their prompt & expected result. Facilitator gives feedback on clarity.
   * Key takeaway: Quality of prompt matters as much as tool.

Break: 5 min

Segment F: Demo rápido (10 min)
   * Title: "Demostración viva: Generando respuestas en tiempo real".
   * Duration: 10
   * Dynamic: Live demo using an AI (ChatGPT, etc.) responding to a sample user query.
   * Key takeaway: Instant feedback loop.

Segment G: Turning prompts into workflow automations (25 min)
   * Title: "De prompt a automatización: Ideas para tu startup"
   * Duration: 25
   * Objective: Brainstorm ways to embed AI into daily ops (customer support, social media scheduling, research summarization).
   * Dynamic: Whole group brainstorming on sticky notes or virtual board.
   * Key takeaway: Even small automations boost efficiency.

Segment H: Exercicio principal del taller (45 min)
   * Title: "Construye tu Asistente de IA para el lanzamiento de tu producto"
   * Duration: 45 (break into two parts maybe). This is the main hands-on activity all participants do collaboratively.
   * Within this, split into sub-phases:
       - Part A: Define your core task (e.g., answering FAQs, drafting emails, generating ad copy). (15 min)
       - Part B: Create a mock AI assistant using a simple tool (like Copy.ai, or using the free ChatGPT web UI). Provide templates and steps. (30 min)
   * But we need overall all-do. Let's structure as 45 min full-time activity: "Crea tu asistente en vivo" with pairs. Perhaps easier: All participants work in mixed teams of 4, assigned a scenario (product feature, customer inquiry). Each team writes a prompt, chooses a tool, builds a flow chart on paper or digital whiteboard. Then present quickly. That takes ~45 min including presentations. Good.

Segment I: Preguntas y cierre (15 min)
   * Title: "Preguntas, dudas y próximos pasos"
   * Duration: 15
   * Objective: Answer remaining questions, share resources, commit to next action.
   * Dynamic: Open floor.
   * Key takeaway: Actionable steps to start today.

Now compute total: 15+10+30+15+5+20+5+10+45+15 = 155? Wait let's sum properly:

A:15
B:10 =>25
C:30=>55
D:15=>70
E:20=>90
F:10=>100
G:25=>125
H:45=>170
I:15=>185

That's 185 minutes > 180. Need adjust. Reduce break lengths or compress durations. Typically there may be minor overlaps. Maybe combine break intervals as part of segments or shorten some.

Let's aim for exact 180 min. Let's recalc with realistic allocation including breaks.

Proposed final schedule:

0:00-0:05: Registration & Welcome (5 min)
But agenda includes welcome? Let's incorporate.

Option: Use 3 blocks of 60 minutes each? Better to allocate:

| Segment | Time |
|---|---|
| 1. Bienvenida e introducción (10 min) |
| 2. Qué es un asistente de IA (12 min) |
| 3. Componentes clave (25 min) |
| 4. Elegir la herramienta (10 min) |
|   Sub: Breve demo (5 min) |
| 5. Primer ejercicio: redactar tu primer prompt (20 min) |
|   Sub: Breve actividad grupal (5 min) |
| 6. Transición a automatización rápida (15 min) |
| 7. EXERCICIO PRINCIPAL (50 min) |
| 8. Preguntas y cierre (15 min) |

Sum: 10+12+25+10+5+20+5+15+50+15 = 152? Something off. Let's systematically define.

Maybe better to produce a clear table with times adding up to 180.

I'll craft a structured agenda:

- **0:00 – 0:10** (10 min) **Bienvenida & Objetivo**  
  *Charla*: rápido rol, metas.  
  *Takeaway*: sabemos por qué construir un asistente de IA.

- **0:10 – 0:22** (12 min) **¿Qué es un asistente de IA?**  
  *Charla*: definiciones, ejemplos cotidianos para startups.  
  *Takeaway*: se diferencia de un chatbot genérico, es tu copiloto.

- **0:22 – 0:47** (25 min) **Componentes esenciales**  
  *Mini-lesson*: entrada (prompt, datos), motor (modelo/fine-tuning), salida (formato, moderación).  
  *Actividad interactiva*: mini‑quiz con preguntas de opción múltiple.  
  *Takeaway*: los tres pilares: claro, confiable, iterativo.

- **0:47 – 0:57** (10 min) **Elegir la herramienta**  
  *Discusión*: opciones gratuitas vs paid, facilidad de inicio, costos.  
  *Demo rápido*: muestra de una interfaz (puede usar una página web ochatbótica previa).  
  *Takeaway*: empieza donde ya tienes acceso (Google, Slack, ChatGPT).

- **0:57 – 1:17** (20 min) **Primer ejercicio: crear tu primer prompt**  
  *Grupo pequeño (3‑4 personas)*: escriban un prompt que resuelva un problema típico de su startup.  
  *Comparte*: cada grupo muestra su prompt y lo que espera obtener.  
  *Feedback*: guía sobre claridad, contexto.

- **1:17 – 1:32** (15 min) **Breve demo en vivo**  
  *Live demo*: generamos una respuesta usando una herramienta elegida en el paso anterior.

- **1:32 – 2:07** (35 min) **De prompt a automatización: ideas prácticas**  
  *Brainstorm*: cómo integrar el asistente en tareas diarias (respuestas FAQ, generación de emails, programación posts).  
  *Posibles ideas* grabadas en pizarra o app.  
  *Takeaway*: pequeños cambios multiplican productividad.

- **2:07 – 2:52** (45 min) **Exercicio principal “Construye tu Asistente para el lanzamiento”**  
  *Formato*: equipos mixtos de 4‑5. Cada equipo recibe un caso (ej: soporte al cliente, captura de leads, creación de contenido).  
  *Tareas (45 min):*  
     a) Definir la task principal → redactar 2‑3 prompts posibles.  
     b) Elegir una herramienta (usar la que escogieron antes).  
     c) Construir un flujo sencillo: input → prompt → respuesta. Dibujen el flujo en papel o digital.  
     d) Preparar un mini‑plan de prueba (qué preguntan, cuál es la solución esperada).  
  *Presentación rápida* (2 min por equipo).  
  *Takeaway*: tienes un prototipo funcional listo para probar en 24 h.

- **2:52 – 3:07** (15 min) **Cierre, preguntas y recursos**  
  *Open floor*: responder dudas, compartir casos que hayan tomado.  
  *Recursos*: lista de plataformas, tutoriales cortos, modelos de prompt, plantillas.  
  *Next steps*: firmar acción inmediata (ej: crear tu primer prompt esta semana).

Total = 115? Let's add precisely:

Segments durations sum: 
10 + 12 + 25 + 10 + 20 + 15 + 35 + 45 + 15 = 167? Actually mis-summed earlier. Let's recount with new layout:

1. Bienvenida & Objetivo: 10 min
2. ¿Qué es un asistente de IA?: 12 min (total 22)
3. Componentes esenciales: 25 (total 47)
4. Elegir la herramienta: 10 (total 57)
5. Primer ejercicio: 20 (total 77)
6. Breve demo en vivo: 15 (total 92)
7. De prompt a automatización: 35 (total 127)
8. Exercicio principal: 45 (total 172)
9. Cierre y preguntas: 15 (total 187)

That's above 180 again. Hmm. Probably too long. Need 3 hours = 180 minutes. We can reduce some sections: e.g., make "Breve demo" shorter to 10 min, "Automatización" to 25 min, and cut "Componentes" to 20 min.

Let's design fresh with tighter timing.

Let me decide on final schedule breakdown:

| Time (min) | Section | Title | Duration |
|------------|---------|-------|----------|
| 0–5 | 0 | Registro y Bienvenida | 5 |
| 5–17 | 1 | El asistente de IA: ¿Qué es? | 12 |
| 17–42 | 2 | Componentes clave para tu asistente | 25 |
| 42–52 | 3 | Elegir tu herramienta (gratuitas vs pagas) | 10 |
| 52–72 | 4 | Tu primer prompt en 5 minutos (ejercicio) | 20 |
| 72–82 | 5 | Demo rápida en vivo | 10 |
| 82–107 | 6 | Ideas para automatizar tareas (brainstorm) | 25 |
| 107–152 | 7 | **Ejercicio principal: Construye tu asistente para el lanzamiento** (incluye definición, prompt, flujo) | 45 |
| 152–167 | 8 | Preguntas, dudas y cierre | 15 |
| 167–180 | 9 | Tiempo extra de retroalimentación / networking | 13 |

Check sum: 5+12=17, +25=42, +10=52, +20=72, +10=82, +25=107, +45=152, +15=167, +13=180. Good.

Now assign dynamic details to each segment. Include key takeaways.

Need also material preparation: printed handouts, access to computers/tablets, internet, projector, markers, sticky notes, etc.

Slide count estimated per section: approximate slides per topic. Provide for each major block.

The request: "El tono debe ser energico y práctico, no académico."

Thus we will write in Spanish, lively voice, bullet points, exclamation marks sparingly but enough energy.

We also must provide:

- Agenda detallada con tiempos (3 horas)
- Materiales necesarios (preparar antes)
- Para cada bloque: Titulo y duracion, Objetivo, Dinamica, Key Takeaway.
- Ejercicio principal del workshop (todos pueden hacer)
- Recursos para llevar a casa
- Slide count estimado por seccion

We'll produce these items clearly.

Let's craft each "bloque" (section). Possibly label them as Block #. Use tables for clarity.

Will also estimate slide counts per block. Eg:

Block 1: Bienvenida: 5 slides

Block 2: ¿Qué es?: 7 slides

... etc.

Now create content.

---

### Agenda (3 horas, total 180 min)

| Horario | Bloque | Título | Duración | Dinámica | Key Takeaway |
|---|---|---|---|---|---|
| 0:00 – 0:05 | 1 | Registro & Bienvenida | 5 min | Charla rápida + encuesta de nombres | Sabemos por qué construir un asistente de IA y qué esperar. |
| 0:05 – 0:17 | 2 | ¿Qué es un asistente de IA? | 12 min | Charla + ejemplo visual | Es tu copiloto personal: responde preguntas, genera contenido, ahorras tiempo. |
| 0:17 – 0:42 | 3 | Los 3 pilares de tu asistente | 25 min | Mini‑lesson + quiz interactivo | Claridad en el prompt, modelo fiable, iterate y mejora. |
| 0:42 – 0:52 | 4 | Elegir la herramienta adecuada | 10 min | Discusión grupal + demo rápido | Empieza con lo que ya usas (Gmail, Google, ChatGPT) o prueba una versión gratuita. |
| 0:52 – 1:12 | 5 | **Primer ejercicio: redacta tu primer prompt** | 20 min | Trabajo en grupos pequeños (3‑4 personas) → compartir prompt | Un prompt bien escrito transforma cualquier herramienta en valor real. (Nota: 0:52‑1:12 = 20 min) |
| 1:12 – 1:22 | 6 | Demo en vivo (generar respuesta al instante) | 10 min | Demostración práctica de la herramienta que eligiste | Vistas instantáneas y ajustes fáciles dan confianza. |
| 1:22 – 1:47 | 7 | De prompt a automatizaciones diarias: ideas para Startup | 25 min | Brainstorming completo (pizarra o App) | Pequeños ciclos automáticos multiplican productividad (FAQs, correos, schedule). |
| 1:47 – 2:32 | 8 (Principal) | **Ejercicio principal: Construye tu asistente para el lanzamiento** | 45 min | Trabajo en equipos mixtos (4‑5) → definir tarea, escribir prompts, dibujar flujo, plan de prueba; presentación rápida (2 min) | Protagote un prototipo funcional listo para probar en 48 h. |
| 2:32 – 2:47 | 9 | Preguntas, dudas y cierre | 15 min | Redacción abierta, recopilación de recursos | Resolver dudas, compartir casos de éxito, compromiso inmediato. |
| 2:47 – 3:00 | 10 | Networking relajado y entrega de materiales | 13 min | Cierre social, reparto de folletos | Continuar aprendiendo después de la salida. |

Wait time sums exceed 180. Let's recompute with new times:

- 0:05-0:17 = 12? Actually 0:05-0:17 is 12 min. I wrote 12 then later 5+12 = 17 correct.

List durations:

1: 5
2: 12 -> cumulative 17
3: 25 -> cumulative 42
4: 10 -> 52
5: 20 -> 72
6: 10 -> 82
7: 25 -> 107
8: 45 -> 152
9: 15 -> 167
10: 13 -> 180

Ok matches earlier.

Thus final schedule has 10 blocks, but many align with original.

Now details for each block.

Block 1: Bienvenida & registro (5 min). No need elaborate but mention objective: create comfortable environment, align expectations.

Block 2: Define AI assistant. 12 min.

Block 3: Los 3 pilares (25 min). Breakdown: Input (prompt), Model (choice, fine-tuning), Output (moderation, format). Quick quiz.

Block 4: Elegir herramienta (10 min). Discuss free vs paid, integration with existing platforms.

Block 5: Primer ejercicio redacta primer prompt (20 min). Group creation of prompt, share.

Block 6: Demo en vivo (10 min). Show live generation.

Block 7: Automatización ideas (25 min). Brainstorm.

Block 8: Exerciro principal (45 min). Detailed instructions.

Block 9: Preguntas y cierre (15 min). Wrap-up.

Block 10: Networking & entregas (13 min). optional.

If we want only 9 blocks, we can merge last two perhaps. But okay.

Now each block needs: title/título, duration, objetivo, dinamica, key takeaway. Also estimate slide count per block.

Materiales: Laptop/desktop, wifi, projector, flipchart or digital whiteboard, markers, printed handouts, pens, sticky notes, internet. Prep: prepare slide deck (estimated slide count), sample AI outputs, example prompt sheets, maybe a link or QR code to a starter account. Also ask participants to bring laptops (if not all have), phone chargers.

Now produce final answer in organized sections.

We'll adopt headings, bullet lists.

Also note "no-tecnicos": thus avoid deep coding, focus on natural language descriptions. Suggest using AI chat models accessible via browser.

Now build out each block with detail.

### Block 1: Bienvenida & Objetivo (5 min)

- Title: Bienvenida y objetivos
- Duration: 5 min
- Objective: Get everyone settled, state why we are here, introduce facilitator role.
- Dynamica: Charla breve + encuesta rápida (manual o en Miro) de nombre y etapa inicial (idea, validación, crecimiento).
- Key Takeaway: Entrepreneurship requires thinking ahead; you’ll leave ready to turn ideas into AI‑powered tools.

Slides: 3 (title, agenda, icebreaker results).

### Block 2: ¿Qué es un asistente de IA? (12 min)

- Title: El Assistente de IA: ¿Qué es?
- Duration: 12 min
- Objective: Define AI assistant, contrast with chatbot, highlight benefits for startups.
- Dynamica: Charla con ejemplos de apps (Like Beep, Jasper) y video clip (imagen) + 2 questions.
- Key Takeaway: It’s a personal partner that can handle repetitive queries, draft emails, summarize market intel.

Slides: 6.

### Block 3: Los 3 pilares (25 min)

- Title: Los 3 pilares de un asistente de IA útil.
- Duration: 25 min
- Objective: Explain three components: (1) Claridad del prompt, (2) Motor confiable, (3) Salida controlada y iterativa.
- Dynamica: Mini‑lesson (10 min) + Quiz interactivo (5 min) + Guía de casos (10 min).
- Key Takeaway: If any pillar weak, the assistant won’t deliver value.

Slides: 8.

### Block 4: Elegir la herramienta (10 min)

- Title: Elegir la herramienta que usarás.
- Duration: 10 min
- Objective: Choose between free tier, cloud SaaS, local model – consider cost, speed, learning curve.
- Dynamica: Discusión en grupos de 4, presentar 2‑3 opciones (ChatGPT, Microsoft Copilot, open-source). Quick demo 2 min.
- Key Takeaway: Start with what you already have or a generous trial; upgrade when ROI appears.

Slides: 5.

### Block 5: Primer ejercicio: redacta tu primer prompt (20 min)

- Title: Tu primer prompt en 5 minutos.
- Duration: 20 min
- Objective: Draft a concise prompt that solves a typical startup problem (e.g., “Responde a mi FAQ”, “Redacte un correo de venta”).
- Dynamica: Grupos pequeños (3‑4) escriben su prompt, luego comparten en la pantalla. Facilitador da retroalimentación (claridad, contexto).
- Key Takeaway: The quality of your prompt shapes how powerful your assistant becomes.

Slides: 4.

### Block 6: Demo en vivo (10 min)

- Title: Demo en vivo: Genera una respuesta al instante.
- Duration: 10 min
- Objective: Show a live interaction with the chosen tool (use ChatGPT or similar) – respond to a sample user query.
- Dynamica: Live demo – facilitator asks, AI answers, viewers see rapid generation.
- Key Takeaway: Instant feedback loops accelerate development cycles.

Slides: 3.

### Block 7: De prompt a automatizaciones (25 min)

- Title: De prompt a automatización: Ideas para Startup.
- Duration: 25 min
- Objective: Brainstorm concrete ways to embed AI into daily operations.
- Dynamica: Brainstorming group activity with sticky notes/virtual board – list 5‑7 ideas per person.
- Key Takeaway: Small automations (FAQ bot, email draft) multiply productivity.

Slides: 6.

### Block 8: Exercicio principal (45 min)

- Title: Exercicio principal: Construye tu asistente para el lanzamiento.
- Duration: 45 min
- Objective: Teams design a functional AI pilot for a launch‑phase use case.
- Dynamica: Step‑by‑step (see below):
   a) Definir la tarea (15 min) – choose scenario (support, lead capture, content).
   b) Escribir 2‑3 prompts (10 min)
   c) Seleccionar herramienta (refuerzo de decisión de bloque 4) (5 min)
   d) Dibujar flujo (input → prompt → output) (5 min)
   e) Plan de prueba (3 questions, desired outcome) (5 min)
   f) Presentar 2 min (cualquier equipo). (5 min)
   g) Tiempo compartido y retroalimentación (5 min). (Total ≈45)
- Key Takeaway: By the end you’ll have a working prototype you can run tomorrow.

Slides: 10 (overview of flow, prompt examples, team roles).

### Block 9: Preguntas, dudas y cierre (15 min)

- Title: Preguntas, dudas y cierre
- Duration: 15 min
- Objective: Answer remaining questions, share resources, set immediate actions.
- Dynamica: Open floor (live Q&A), distribute cheat sheet.
- Key Takeaway: Continuous learning – keep experimenting, join community, revisit prompts weekly.

Slides: 4.

### Block 10: Networking y entrega de materiales (13 min) optional wrap-up.

But we might combine 9 and 10. To stay under 3 hours we had 13 min left. Keep it brief: "Networking relajado y entregas".

Now compile slide counts per block: Already estimated.

Now materials needed: List before.

Now "Ejercicio principal" we need explicitly described.

Resources for take-home: Printed checklist ("Prompts template", "Flows diagram"), links to free accounts, Cheat sheet with prompts, flowchart template PDF, recommended reading.

Now ensure tone: Energetic, practical. Use exclamations, encouragement, direct address "tú".

Let's flesh out each block with details.

### Block 1 (5 min)

- Title: Bienvenida & Objetivo
- Objective: Create a safe space, align expectations, get participants' names and startup stage.
- Dynamics: Short welcome speech (30 sec), quick poll: "En qué fase estás?" (early idea, validation, growth). Optionally show Kahoot or Miro stickies.
- Takeaway: Knowing where you are helps pick the right AI use case.

Materials: Projector, speakers, printed agenda.

Slide count: 3 (title, agenda, welcome poll results).

### Block 2 (12 min)

- Title: ¿Qué es un Asistente de IA?
- Objective: Define term, differentiate from chatbot, explain benefit for startups (save time, consistency).
- Dynamics: 5 min story of a founder who used an AI assistant to draft proposals; 5 min Q&A flash. Use image/short video.
- Takeaway: Your AI companion will act as a personal copilot.

Slides: 6.

### Block 3 (25 min)

- Title: Los 3 pilares de tu asistente
- Objectives: Clarify prompt, model, output. Emphasize iteration.
- Dynamics: 
   - 5 min mini‑lesson (slides)
   - 10 min interactive quiz (multiple choice, projected)
   - 10 min case studies (realistic prompts for product, marketing, support).
- Takeaway: Build strong, focused prompts; trust free tiers; test and tweak fast.

Slides: 8.

### Block 4 (10 min)

- Title: Elegir la herramienta adecuada
- Objectives: Guide choices: free tier, premium, local LLMs. Consider cost, speed, familiarity.
- Dynamics: Round‑robin presentation of top 3 options, quick live demo of ChatGPT.
- Takeaway: Start small, upgrade when ROI realized.

Slides: 5.

### Block 5 (20 min)

- Title: Tu primer prompt en 5 minutos
- Objectives: Draft first prompt. Encourage specificity.
- Dynamics: Groups of 3‑4 write prompt on paper or shared doc. Share aloud.
- Takeaway: One well‑crafted prompt unlocks power.

Slides: 4.

### Block 6 (10 min)

- Title: Demo en vivo: Genera respuestas al instante
- Objectives: Show real‑time output.
- Dynamics: Facilitator selects random question; AI replies instantly.
- Takeaway: Immediate feedback speeds up iteration.

Slides: 3.

### Block 7 (25 min)

- Title: De prompt a automatización: ideas para Startup
- Objectives: Brainstorm concrete automation ideas using AI.
- Dynamics: Sticky-note wall or digital board. Each participant adds 5 ideas.
- Takeaway: Automating routine tasks saves hours.

Slides: 6.

### Block 8 (45 min) - Excursive principal

We will detail steps:

- Formation: 4‑5 members per team. Assign: Lead, Prompt Writer, Flow Designer, Test Creator.
- Phase A (0:00‑0:15): Define the use case. Example: "Asistente para soporte al cliente" – tasks: answer FAQ, resolve ticket. Write goal.
- Phase B (0:15‑0:25): Craft 2‑3 prompts. Review for clarity.
- Phase C (0:25‑0:30): Pick tool (refer to previous decisions). Keep same across groups.
- Phase D (0:30‑0:35): Draw flow chart: Input → Prompt → Response → Output (optional). 
- Phase E (0:35‑0:40): Design 3 test questions. Expected outcomes.
- Phase F (0:40‑0:45): 2‑minute pitch to class. 
- After presentations, facilitator highlights common patterns and offers next steps.

Key takeaway: You now have a live prototype ready for testing within 48 hours.

Slides: 10 (flow diagrams, prompt examples, team roles).

### Block 9 (15 min)

- Title: Preguntas, dudas y cierre
- Objectives: Resolve doubts, share cheat sheets, announce next meeting if any.
- Dynamics: Open Q&A, link to resource folder, collect commitments.
- Takeaway: Join our community, keep iterating.

Slides: 4.

### Block 10 (13 min)

- Title: Networking relajado y entrega de materiales
- Objectives: Informal chat, hand out take‑home kits.
- Dynamics: Coffee/tea chat, distribute PDFs.
- Takeaway: Continue learning after workshop.

Slides: 3.

Add times match earlier totals: 5+12+25+10+20+10+25+45+15+13 = 165? Wait need 180. Let's recalc using listed durations: I previously allocated 5,12,25,10,20,10,25,45,15,13 = 160? Let's compute again accurately:

1:5
2:12 => 17
3:25 => 42
4:10 => 52
5:20 => 72
6:10 => 82
7:25 => 107
8:45 => 152
9:15 => 167
10:13 => 180

Yes sum 180. Good.

Now we need to match those numbers with the timeline. In earlier table I had different splits but ok.

Now we need to map each block number to those durations.

Let's rewrite timeline aligning to 180 minute slots:

0:00-0:05 (5) Block 1 – Bienvenida & Objetivo.
0:05-0:17 (12) Block 2 – ¿Qué es un asistente de IA?
0:17-0:42 (25) Block 3 – Los 3 pilares.
0:42-0:52 (10) Block 4 – Elegir la herramienta.
0:52-1:12 (20) Block 5 – Primer ejercicio (prompt).
1:12-1:22 (10) Block 6 – Demo en vivo.
1:22-1:47 (25) Block 7 – De prompt a automatización.
1:47-2:32 (45) Block 8 – Exercicio principal.
2:32-2:47 (15) Block 9 – Preguntas y cierre.
2:47-3:00 (13) Block 10 – Networking y entrega.

Works perfectly.

Now estimate slide count per block based on content:

- Block 1: 3 slides.
- Block 2: 6 slides.
- Block 3: 8 slides.
- Block 4: 5 slides.
- Block 5: 4 slides.
- Block 6: 3 slides.
- Block 7: 6 slides.
- Block 8: 10 slides.
- Block 9: 4 slides.
- Block 10: 3 slides.

Total approx = 53 slides. That's reasonable.

Now materials needed: List everything.

- Proyector e pantalla grande.
- Wi-Fi estable.
- Computadoras o tablets con conexión a internet (si no hay suficientes, usar ordenadores compartidos).
- Acceso a cuentas gratis de IA (por ejemplo, ChatGPT Via Reflex or Bing Chat). Pre-alternative: use local demos offline.
- Papel, marcadores, tarjetas adhesivas, post-its para sticky notes.
- Cuadros blancos o pizarra digital.
- Enlaces impresos a tutoriales y plantillas.
- Kits de participación: hoja de prompts, diagrama de flujos, checklist.

Preparation: prepare slide deck (approx 53 slides). Prepare handout: "Guía rápida de prompts", "Plantilla de flujo", "Lista de herramientas".

Time management tips: assign a facilitator for each block, keep Q&A brief.

Now principal exercise details: Let's expand with step-by-step inside block 8.

Write out the steps concisely: 

- Formar equipos (4‑5 personas).
- Cada equipo elige un escenario: soporte, captación de leads, redacción de anuncios, etc.
- 15 min – Definir el problema y el objetivo del asistente.
- 10 min – Redactar 2‑3 prompts concretos.
- 5 min – Seleccionar la herramienta ya decidida.
- 5 min – Dibujar el flujo (iconos: Entrada → Prompt → Respuesta).
- 5 min – Diseñar 3 preguntas de prueba y resultado esperado.
- 5 min – Presentar 2 min (cada equipo).
- Totales ≈45.

Takeaway: "Ya tienes un prototipo listo para probar hoy mismo."

Now resources for take-home: PDFs: "Cheatsheet de prompts", "Flowchart template", "Planta de automatización", "Links a cuentas gratuitas", "Videos cortos" (links). Also recommendation to join Discord/Slack community.

Now incorporate energetics: Use phrases like "¡Vamos!, ¡aprovecha esto!", "¡Hoy vamos a crear algo real!".

Now format answer: Use markdown headings, tables.

Let's begin constructing final response.

-----

## Outline General

- Title
- Audience
- Duration

Then sections:

1. Agenda (timeline table)
2. Materiales necesarios
3. Bloques (detailed per block)
4. Ejercicio principal
5. Recursos para llevar a casa
6. Slide count per section

Make sure each block includes title, duration, objective, dinámica, key takeaway.

Let's go block by block:

### Bloque 1: Bienvenida & Objetivo
- Title: Bienvenida y objetivos
- Duración: 5 min
- Objetivo: Crear ambiente cómodo, conocer nombres, nivel de startup.
- Dinámicas: Bienvenida, encuesta rápida de etapa.
- Key Takeaway: Sabemos dónde estamos empezando y por qué necesitamos un asistente ahora.
- Slides: 3

### Bloque 2: ¿Qué es un asist