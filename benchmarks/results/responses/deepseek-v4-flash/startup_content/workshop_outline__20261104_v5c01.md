# DeepSeek V4 Flash (OpenRouter) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 53.321s | tokens_per_second: 51.3
- input_tokens: 198 | output_tokens: 2736
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el workshop.

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

¡Excelente iniciativa! Este workshop es justo lo que los emprendedores no-técnicos necesitan para dejar de tener miedo a la IA y empezar a usarla como un "co-fundador" digital. Aquí tienes el outline completo, diseñado para ser dinámico, práctico y memorable.

---

### **Título:** Construye tu Asistente de IA para tu Startup - Workshop Práctico
**Duración:** 3 horas (con 1 receso de 10 min)
**Audiencia:** 20-30 emprendedores early-stage, perfil no-técnico (sin saber programar).
**Formato:** Presencial, con mesas de trabajo (4-5 personas por mesa).

---

### **1. Materiales Necesarios (Preparación Previa)**

**Para el Facilitador:**
- **Proyector y pantalla.**
- **Pizarra blanca o rotafolio** con marcadores de colores.
- **Conexión a internet estable** (con respaldo de hotspot).
- **Micrófono inalámbrico** (opcional, pero recomendado para energía).
- **Slides** (ver sección 6).
- **Post-its grandes** (3 colores: amarillo, rosa, azul).
- **Cronómetro visible** (en proyector o app).
- **Música de fondo** (playlist energética para ejercicios).

**Para los Participantes:**
- **Laptop o tablet** (obligatorio para el ejercicio práctico).
- **Cuenta de OpenAI (ChatGPT Plus)** o **Cuenta de Google (para Bard/Gemini)**. *Recomendar crear 1-2 días antes.*
- **Cuenta de Zapier (nivel gratuito)**. *Crear 1 día antes.*
- **Un problema o proceso real de su startup** anotado en un papel (ej: "responder FAQs de clientes, programar reuniones, generar reportes de ventas).

---

### **2. Agenda Detallada (3 horas)**

| **Hora | Bloque | Duración | Actividad | Objetivo | Dinámica | Key Takeaway | Slides**
-------|-------|-------|-------|-------|-------|-------
**0:00 - 0:15** | **1. Bienvenida & "El Miedo es el Enemigo"** | 15 min | Romper el hielo, desmitificar la IA y conectar con el problema real. | Charla rápida + Dinámica "¿Qué te detiene?" (Post-it de miedos en la pared). | **"No necesitas saber programar. Necesitas saber preguntar."** | 5
**0:15 - 0:45** | **2. De la Idea al Prompt: El ABC del Ingeniero de Prompts** | 30 min | Aprender a escribir prompts efectivos (no "magia", sino estructura). | Demo en vivo: Mostrar 3 prompts malos vs 3 buenos para el mismo problema. Ejercicio individual: Escribir 3 prompts para su startup. | **"Prompt = Instrucciones + Contexto + Formato."** | 8
**0:45 - 1:15** | **3. El Asistente de Atención al Cliente (Demo Rápida)** | 30 min | Ver cómo automatizar una conversación básica sin código. | Demo en vivo: Mostrar **ChatGPT + Zapier** para recibir un email, resumirlo y responder automáticamente. | **"No construyas un chatbot desde cero. Conecta herramientas que ya existen."** | 6
**1:15 - 1:25** | **RECESO (10 min)** | 10 min | Café, networking, revisar prompts. | - | - | -
**1:25 - 2:15** | **4. EJERCICIO PRINCIPAL: Construye tu Asistente de IA en 50 min** | 50 min | Construir un asistente funcional que resuelva un problema real de su startup. | **Trabajo en equipos de 4-5 personas.** Guía paso a paso (ver sección 4). Facilitador circula apoyando. | **"En 50 minutos puedes tener un MVP de un asistente de IA."** | 2 (instrucciones)
**2:15 - 2:40** | **5. Show & Tell: 3 MVP en 3 Minutos** | 25 min | Compartir resultados, celebrar logros y aprender de otros. | 3 equipos (elegidos al azar) presentan su asistente en 3 min cada uno. Feedback rápido del grupo. | **"El peor asistente del taller es mejor que no tener ninguno."** | 3
**2:40 - 3:00** | **6. Cierre: De MVP a Producto Real** | 20 min | Próximos pasos: cómo iterar, medir y escalar. | Charla final + Entrega de "Kit de Supervivencia" (recursos). Preguntas y respuestas. Foto grupal. | **"Mañana, tu asistente será tu empleado más productivo."** | 4

---

### **3. Para Cada Bloque (Detalle)**

#### **Bloque 1: Bienvenida (0:00 - 0:15)**
- **Objetivo:** Que todos se sientan cómodos, que identifiquen su "miedo" principal y que sepan que el taller es para ellos.
- **Dinámica:**
    - Facilitador: "¡Bienvenidos! Hoy van a construir algo que ayer solo era una idea. Pero primero, una pregunta: ¿Qué es lo que más te detiene para usar IA en tu startup? ¡Escribe tu miedo en un post-it y pégalo en la pared!"
    - Mientras pegan, el facilitador lee 2-3 en voz alta y los desmiente: "No necesitas un PhD. Necesitas un prompt."
- **Key Takeaway:** **"No necesitas saber programar. Necesitas saber preguntar."**

#### **Bloque 2: El ABC del Prompt (0:15 - 0:45)**
- **Objetivo:** Pasar de "preguntar a ChatGPT" a "dar *instrucciones* a un asistente.
- **Estructura del Prompt:**
    - *Mal:* "Haz un asistente para clientes.* (Muy vago).
    - *Bueno:* "Actúa como un agente de atención al cliente para mi startup, que vende [tu producto. Habla en tono amigable. Si el cliente pregunta '¿Cómo hago X?', responde con el paso 1, 2, 3. Responde en menos de 3 oraciones."
- **Ejercicio (5 min):** Cada persona escribe 3 prompts para su startup. Luego comparten en pareja.

#### **Bloque 3:3: Demo (0:45 - 1:15)**
- **Objetivo:** Mostrar que no es magia, es conectar.
- **Demo:**
    - **Paso 1:** Tiene un formulario de Google Forms.
    - **Paso 2:** Zapier recibe el formulario → lo envía a ChatGPT.
    - **Paso 3:** ChatGPT recibe el texto → lo transforma en respuesta amigable → la envía a Google Sheets.
- **¡Funciona!** El facilitador muestra el resultado en 2 minutos.
- **Key Takeaway:** "No construyas un chatbot desde cero. Conecta herramientas que ya existen."

#### **4. EJERCICIO PRINCIPAL (1:25 - 2:15)**

**Título:** **"Construye tu Asistente de IA en 50 minutos"**
**Objetivo:** Cada equipo debe construir un asistente que resuelva un **un proceso real** de su startup.

**Instrucciones para el Facilitador:**
1. **Dividir en equipos de 4-5 (1 min).**
2. **Elegir un problema común** (el más votado o el del equipo). Ej: "Responder preguntas de clientes sobre envíos."
3. **Guía paso a paso (proyectada en pantalla):**
    - **Min 0-5: Definir el Rol.** Escribir: "Eres un asistente de envíos para una startup de e-commerce. Tu tono es amable y proactivo. Tu base de conocimiento es: [3 datos clave]."
    - **Min 5-15: Crear el Prompt Maestro.** (En ChatGPT o Bard).** Copiar el rol + instrucciones de formato (ej: "Respuesta en 3 oraciones, incluye enlace de seguimiento").
    - **Min 15-25: Probar con 3 preguntas reales.** (Ej: "¿Dónde está mi pedido?", "¿Cuánto cuesta el envío a México?")
    - **Min 25-35: Corregir errores.** (Si responde mal, añadir "Si no sabes, di: 'Lo siento, transfiero con un humano'")
    - **Min 35-45: Conectar con una herramienta.** (Opcional: Conectar a un Google Sheet o Slack usando Zapier - solo si hay tiempo).
    - **Min 45-50: Preparar demo de 3 min.** (Qué problema resuelve, mostrar la conversación más loca que respondió bien).
4. **Facilitador circula:** Ayuda a equipos lentos, corrige prompts, celebra logros.

---

### **5. Recursos para Llevar a Casa (Kit de Supervivencia)**

**Documento PDF (1 página) que incluye:**
1. **Plantilla de Prompt Maestro:**
    - `[ROL]` Eres un asistente de [función] para una startup de [industria].
    - `[TONO]` Habla en tono [amable/profesional/divertido].
    - `[INSTRUCCIONES]` Sigue estos pasos: [1,2,3].
    - `[FORMATO]` Respuesta en [número] oraciones.
    - `[FALLBACK]` Si no sabes, di: [frase].
2. **Enlaces a herramientas:**
    - **ChatGPT** (chat.openai.com)
    - **Bard** (bard.google.com)
    - **Zapier** (zapier.com) - *Link a tutorial de 3 min.*
    - **Notion AI** (notion.so) - *Para bases de conocimiento.*
3. **5 Prompts Poderosos para Startups (ejemplos):**
    - "Genera 10 ideas de marketing para [producto] para [audiencia]."
    - "Reescribe este email de ventas en tono más persuasivo."
    - "Resume este feedback de cliente en 3 puntos clave."
    - "Crea un guión de llamada de ventas de 30 segundos."
    - "Escribe un post de LinkedIn sobre [tema] en tono inspirador."
4. **Reto de 7 Días:** "Cada día, automatiza un proceso de 5 min con IA. Empieza con: Día 1 - Responder un email, Día 2 - Generar un post, etc."

---

### **6. Slide Count Estimado**

| Sección | Slides |
|-------|-------|
| 1. Bienvenida & "El Miedo es el Enemigo" | 5 |
| 2. El ABC del Prompt | 8 |
| 3. Demo: Asistente de Atención | 6 |
| 4. Ejercicio Principal (instrucciones) | 2 |
| 5. Show & Tell | 3 |
| 6. Cierre & Recursos | 4 |
| **Total** | **28 slides** |

**Nota:** Los slides deben ser **visuales, con poco texto**. Usa imágenes de personas, no de robots. El tono debe ser: "Tú puedes hacer esto."

---

**¡Buena suerte con el workshop!** Será un éxito.