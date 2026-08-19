# Sakana Namazu — startup_content/workshop_outline

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.6 | quality: 8.56
- latency_total: 13.746s | tokens_per_second: 149.0
- input_tokens: 218 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

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

El usuario solicita un outline completo para un workshop presencial de 3 horas para emprendedores early-stage no técnicos (20-30 personas). El título es "Construye tu Asistente de IA para tu Startup - Workshop Práctico".

 Necesito crear:
 1. Agenda detallada con tiempos (3 horas)
 2. Materiales necesarios (preparación previa)
 3. Para cada bloque:
    - Título y duración
    - Objetivo
    - Dinámica
    - Key takeaway
 4. Ejercicio principal del workshop
 5. Recursos para llevar a casa
 6. Slide count estimado por sección

 Tono: Enérgico, práctico, no académico. Debo considerar que son no-técnicos, early-stage, y son 20-30 personas. Debe ser muy hands-on pero sin código. Probablemente usaremos herramientas no-code/low-code como ChatGPT, Claude, Make/Zapier, o plataformas como Voiceflow, Bubble, o simplemente prompts avanzados + automatizaciones simples.

 Estructura de 3 horas:
 - 0:00-0:15: Check-in e intro
 - 0:15-0:45: Fundamentos (qué es un asistente de IA, casos de uso, mitos)
 - 0:45-1:15: Diseño del asistente (el ejercicio de arquitectura no-code)
 - 1:15-1:30: Coffee break
 - 1:30-2:30: Ejercicio principal (construcción hands-on)
 - 2:30-2:50: Presentaciones y feedback
 - 2:50-3:00: Cierre y recursos

 Otra opción:
 - 0:00-0:20: Intro + calentamiento
 - 0:20-0:50: Mapeo de problemas + oportunidades IA
 - 0:50-1:20: Demo + diseño del asistente
 - 1:20-1:35: Break
 - 1:35-2:35: Lab práctico (ejercicio principal)
 - 2:35-2:55: Sharing + retro
 - 2:55-3:00: Cierre

 Voy a proponer usar herramientas accesibles: ChatGPT/Claude (todos likely los usan o conocen), Google Sheets, y Make.com (free tier) o Zapier. O incluso más simple: un "Manual de Sistemas" + Prompts + Automatización con Google Sheets + Gmail. Dado que son 20-30 personas y no técnicos, no quiero que se atoren en configuraciones complejas. Mejor enfocar en: "Tu Mini-Brain de IA en 60 minutos".

 Propuesta de ejercicio principal: Construir un "Asistente de IA" que reciba consultas (simuladas o reales vía formulario Google Forms), procese la información con IA (ChatGPT/Claude/Make), y genere una respuesta/recomendación en un Google Sheet o correo. O aún más simple: Crear un "Agente" en una herramienta accesible como ChatGPT GPTs (si tienen Plus) o usando un prompt sistemático avanzado + automations con Make.

 Dado que pueden no tener todos ChatGPT Plus, mejor usar Make.com (gratis) + OpenAI API (requiere billing) - esto puede ser técnico. 

 Mejor enfoque: Usar herramientas 100% gratuitas y no técnicas:
 - Google Forms → Google Sheets (ya lo saben usar)
 - Plantilla de prompt en ChatGPT Free o Claude Free
 - Presentar una demo donde el facilitador monta un flujo simple en Make.com/Zapier, pero el ejercicio del participante sea diseñar su flujo, crear el prompt sistema, y probarlo manualmente. Es decir, el "build" es diseñar el sistema y el prompt, no necesariamente deployar código.

 El deliverable: Cada equipo (de 3-4 personas) sale con:
 1. Un mapa de su proceso actual vs con IA
 2. Un "System Prompt" listo para usar
 3. Un blueprint de automatización (dibujado o en herramienta simple)
 4. Un prototipo funcional mínimo (incluso si es solo un chat con prompt estructurado)

 Diseño de la experiencia:
 - Trabajo en mesas de 4-5 personas (5-7 mesas).
 - Cada mesa elige un tipo de startup (e-commerce, servicios, edtech, fintech lite, etc.).
 - Construyen un asistente para UN caso de uso específico (ej: responder FAQs, calificar leads, onboarding de clientes, crear briefs de marketing).

 Detalle de bloques:

 Bloque 1: Kick-off & Mindset Shift (20 min)
 - Título: "De trabajar IN la empresa a trabionar ON la empresa con IA"
 - Objetivo: Romper el miedo a lo técnico, entender que un asistente de IA = Prompt + Contexto + Flujo.
 - Dinámica: Charla rápida + ejercicio de "La Tarea que Más Odio" (cada uno escribe en post-it la tarea repetitiva que hace semanalmente). Votación rápida.
 - Key takeaway: La IA no es magia, es un estagiario súper-rápido que necesita instrucciones claras.
 - Slides: 5-6

 Bloque 2: Los 3 Pilares del Asistente (30 min)
 - Título: "Anatomía de un Asistente que Sí Funciona"
 - Objetivo: Entender los 3 componentes: Instrucciones (prompt), Memoria (contexto/base de conocimiento), y Acciones (qué hace con el output).
 - Dinámica: Charla con demo en vivo. El facilitador muestra un asistente malo vs bueno. Uso de GPT/Claude con prompt system.
 - Key takeaway: Un buen asistente no es "una pregunta bonita", es un sistema con roles, reglas y contexto.
 - Slides: 8-10

 Bloque 3: Coffee & Networking (15 min) - No es bloque formal pero va en agenda.

 Bloque 4: Design Sprint - Tu Arquitectura en 10 minutos (25 min)
 - Título: "Blueprint de tu Mini-Brain"
 - Objetivo: Cada equipo define QUÉ hará su asistente, PARA QUIÉN, y CON QUÉ SE ALIMENTA.
 - Dinámica: Ejercicio con canvas impreso (Asistente Canvas): 1. Trigger (qué lo activa), 2. Input (qué info recibe), 3. Brain (qué decide/procesa), 4. Output (qué entrega), 5. Acción (qué hace después).
 - Key takeaway: Si no puedes dibujarlo en una servilleta, no lo podrás automatizar.
 - Slides: 3-4 (instrucciones del canvas)

 Bloque 5: Lab Práctico - Manos a la Obra (60 min)
 - Título: "Build Session: Tu Asistente en Acción"
 - Objetivo: Construir un prototipo funcional mínimo usando herramientas no-code/low-code.
 - Dinámica: Ejercicio hands-on por equipos. El facilitador y 1-2 helpers caminan.
   Opción A: Usar ChatGPT/Claude con un prompt sistemático muy pulido + una hoja de Google Sheets como "base de datos" que alimentan manualmente.
   Opción B: Si la mayoría tiene laptop y cuenta de Make/Zapier (free), armar un flujo simple. Pero puede ser riesgoso para no-técnicos.
   Mejor: Híbrido. 
   Paso 1: Escribir el System Prompt perfecto (20 min).
   Paso 2: Crear una "Base de Conocimiento" en Google Sheets (FAQ, info de producto, precios) (10 min).
   Paso 3: Prueba de fuego: Cada equipo le pasa 3 escenarios reales al prompt y itera (20 min).
   Paso 4: Blueprint de automatización: Dibujar en Miro/paper cómo conectaría esto con su operación (10 min).
 - Key takeaway: Tu asistente ya responde como si trabajara para ti; ahora solo falta conectarlo a tus canales.
 - Slides: 4-5 (pantallas de referencia, ejemplos de prompts, checklist)

 Bloque 6: Demo Rápida & Feedback (20 min)
 - Título: "Show me the Magic"
 - Objetivo: Compartir aprendizajes y ver diversidad de aplicaciones.
