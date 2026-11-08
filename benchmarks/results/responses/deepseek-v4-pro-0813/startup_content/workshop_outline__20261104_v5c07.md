# DeepSeek V4 Pro (0813) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.12 | quality: 9.72
- latency_total: 57.071s | tokens_per_second: 46.3
- input_tokens: 198 | output_tokens: 2641
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

Aquí tienes el outline completo. Está diseñado con el espíritu *"Manos a la obra"* (Hands-on), evitando la teoría densa y enfocándose en que cada emprendedor salga con un prototipo funcional y un plan de acción.

---

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup"
**Formato:** Presencial | 3 Horas | 20-30 personas
**Audiencia:** Emprendedores early-stage no-técnicos
**Filosofía:** 20% Concepto, 80% Acción. Si no lo tocas, no lo aprendes.

---

### 1. Agenda Detallada (3 Horas)

| Hora | Duración | Bloque |
| :--- | :--- | :--- |
| 09:00 - 09:15 | 15 min | **Apertura & "El Problema del Tiempo"** |
| 09:15 - 09:45 | 30 min | **Bloque 1: IA para Startups sin Código** |
| 09:45 - 10:45 | 60 min | **Bloque 2: Manos a la Obra (Ejercicio Principal)** |
| 10:45 - 11:00 | 15 min | ☕ *Bio-Break / Networking rápido* |
| 11:00 - 11:30 | 30 min | **Bloque 3: Entrenando a tu Pasante Digital** |
| 11:30 - 11:55 | 25 min | **Bloque 4: Demo Day & Feedback** |
| 11:55 - 12:00 | 5 min | **Cierre y Próximos Pasos** |

---

### 2. Materiales Necesarios (Preparación Previa)

**Por parte del Facilitador:**
1.  **Presentación (Slides):** Visuales, con memes locales y capturas de pantalla gigantes.
2.  **Plantilla de "Prompt Maestro":** Un documento de Google Docs o Notion pre-escrito con espacios en blanco para que ellos lo llenen.
3.  **Checklist de Herramientas:** PDF con comparativa de precios (Free vs Pro) de herramientas.

**Logística del Espacio:**
- Mesas redondas o estilo "cabaret" (grupos de 4-5) para fomentar colaboración.
- Proyector de alta definición (vamos a leer texto en pantalla).
- Extensiones eléctricas y regletas en cada mesa. **Crítico.**
- Post-its y marcadores Sharpie en cada mesa.

**Por parte del Asistente (Comunicar 48h antes):**
- Laptop (no tablet) y cargador.
- **Cuenta creada en:** OpenAI (ChatGPT) o Anthropic (Claude). *Tener la sesión iniciada antes de llegar.*
- Tener en mente 1 tarea repetitiva y molesta de su startup (ej: responder correos de precios, generar ideas para redes, resumir feedback de clientes).

---

### 3. Desarrollo de Bloques

#### 🟢 Apertura (15 min)
- **Título:** "El Problema del Tiempo"
- **Objetivo:** Romper el hielo y crear urgencia sobre la automatización.
- **Dinámica:** *Charla interactiva.* El facilitador pregunta: "¿Quién aquí siente que trabaja 12 horas pero avanza 4?". Mostrar estadísticas de cuánto tiempo pierde un fundador en tareas administrativas.
- **Key Takeaway:** *"No necesitas un CTO para tener un equipo. Hoy construiremos a tu primer empleado digital."*

#### 🔵 Bloque 1: IA para Startups sin Código (30 min)
- **Título:** "Tu Nuevo Pasante Digital"
- **Objetivo:** Desmitificar la IA Generativa y mostrar 3 casos de uso directos para early-stage.
- **Dinámica:** *Demo en vivo.* El facilitador abre ChatGPT/Claude y muestra:
    1.  **El Analista:** Pegar un Excel desordenado y pedirle insights.
    2.  **El Copywriter:** Generar 5 versiones de un post de LinkedIn.
    3.  **El Soporte:** Responder un correo de un cliente molesto en tono profesional.
- **Key Takeaway:** *"La IA no reemplaza tu criterio, reemplaza tus minutos de teclear."*

#### 🟡 Bloque 2: Manos a la Obra (60 min) - *El Ejercicio Principal*
- **Título:** "Construyendo tu 'GPT' de Atención al Cliente"
- **Objetivo:** Que cada emprendedor construya un asistente funcional que responda preguntas frecuentes sobre su startup.
- **Dinámica:** *Ejercicio guiado paso a paso.*
    1.  **Paso 1 (10 min):** Acceder a la sección "Explorar GPTs" (ChatGPT) o "Projects" (Claude).
    2.  **Paso 2 (15 min):** Llenar la "Plantilla de Prompt Maestro" (El facilitador la lee en voz alta y ellos llenan los huecos: Nombre de la startup, pitch, tono de voz, objeciones comunes).
    3.  **Paso 3 (20 min):** "El Juego de Roles". Un compañero de mesa le hace preguntas difíciles al asistente del otro (ej: "¿Por qué eres tan caro?", "¿Tienes descuento?"). El creador debe ajustar el prompt para corregir las respuestas incorrectas.
    4.  **Paso 4 (15 min):** Compartir en la mesa. ¿Quién logró la respuesta más "humana"?
- **Key Takeaway:** *"Un buen asistente no nace, se entrena. La calidad de la salida depende de la calidad de tu instrucción."*

#### 🔴 Bloque 3: Entrenando a tu Pasante (30 min)
- **Título:** "Más Allá del FAQ: Automatizando tu Caos"
- **Objetivo:** Enseñar a conectar el asistente con datos reales (PDFs, links) y otras herramientas (Zapier/Make).
- **Dinámica:** *Demo técnica superficial + Discusión.*
    - Mostrar cómo subir un PDF (ej: Manual de marca o Pitch Deck) al asistente para que responda en base a ese contexto.
    - Mencionar (sin profundizar) cómo conectar esto a Gmail o Slack.
    - *Discusión:* ¿Qué tarea de su semana les gustaría automatizar primero?
- **Key Takeaway:** *"El asistente que construiste hoy puede convertirse en tu secretaria, tu analista o tu community manager mañana."*

#### 🟣 Bloque 4: Demo Day & Feedback (25 min)
- **Título:** "La Hora de la Verdad"
- **Objetivo:** Validar lo aprendido y generar confianza pública.
- **Dinámica:** *Presentaciones relámpago.*
    - Pedir a 3 o 4 voluntarios que pasen al frente.
    - Conectan su laptop al proyector.
    - Le hacen UNA pregunta difícil a su asistente en vivo.
    - El público aplaude si la respuesta es buena; si es mala, el facilitador ayuda a corregir el prompt en tiempo real (esto es oro puro para el aprendizaje).
- **Key Takeaway:** *"Iterar en público es la forma más rápida de aprender."*

#### ⚪ Cierre (5 min)
- **Título:** "No lo dejes morir"
- **Objetivo:** Asegurar continuidad post-evento.
- **Dinámica:** *Charla motivacional.*
    - "La herramienta que construiste hoy es gratis. El costo es tu tiempo para entrenarla."
    - Invitar a un canal de Slack/Discord de la comunidad para seguir compartiendo prompts.
- **Key Takeaway:** *"El mejor fundador no es el que más sabe, es el que mejor delega."*

---

### 4. Ejercicio Principal del Workshop (Detalle)

**Nombre:** "Mi Asistente de Ventas Nivel 1"

**Contexto:** Los emprendedores early-stage pasan horas respondiendo los mismos correos: "¿Qué hacen?", "¿Cuánto cuesta?", "¿Por qué no me sirve X competidor?".

**La Tarea:**
1.  **Construir:** Usar la interfaz de "Custom GPT" (o Claude Project).
2.  **Configurar:**
    - **Nombre:** "Asistente de [Nombre de la Startup]".
    - **Personalidad:** Amable, experto, pero NO robótico.
    - **Conocimiento Base:**
        - *¿Qué hace tu startup?* (1 párrafo)
        - *¿Precios?* (Rango o "Depende del plan")
        - *¿Diferenciadores?* (¿Por qué tú y no la competencia?)
        - *¿Objeciones?* (¿Qué excusas ponen los clientes? Ej: "Es muy caro", "No lo necesito ahora").
3.  **Probar:** Hacer 5 preguntas estándar.
4.  **Refinar:** Ajustar el prompt añadiendo reglas como: "Nunca inventes precios. Si no sabes, pide el correo del usuario."

**Resultado:** Cada persona sale con un link/ventana activa de un asistente que puede responder preguntas de clientes mejor que ellos mismos en un mal día.

---

### 5. Recursos para Llevar a Casa (Kit de Supervivencia)

Se entrega un PDF digital o impreso con:

1.  **La "Biblia del Prompt":** 10 plantillas de prompts listas para copiar y pegar (Idea de negocio, Análisis FODA, Email marketing, Guiones para TikTok, etc.).
2.  **Mapa de Herramientas:**
    - *Gratis:* ChatGPT, Claude, Gemini, Perplexity.
    - *Automatización (Intermedio):* Zapier, Make.com.
    - *Avanzado (Para cuando levanten capital):* Langchain, botpress.
3.  **Glosario Anti-Tech:** Qué significa "Token", "Contexto", "Alucinación" y "RAG" explicado con analogías de cocina.
4.  **Acceso al "Prompt Vault"** (Carpeta de Google Drive compartida) donde la comunidad sube sus mejores prompts.

---

### 6. Slide Count Estimado por Sección

*Nota: Menos es más. Las slides son apoyo visual, no teleprompter.*

- **Portada / Intro:** 2 slides (Título, Agenda).
- **El Problema:** 3 slides (1 estadística impactante, 1 meme, 1 transición).
- **Bloque 1 (Conceptos):** 5 slides (Qué es, Qué no es, 3 Casos de uso con screenshots).
- **Bloque 2 (Ejercicio):** 4 slides (Paso 1, Paso 2, Paso 3, Errores comunes).
- **Bloque 3 (Avanzado):** 4 slides (PDFs, Conexiones, Ejemplo visual de flujo).
- **Cierre:** 2 slides (Recursos, Gracias/QR de la comunidad).
- **Total Estimado:** **20 slides.** (Perfecto para 3 horas de interacción; la magia ocurre en el navegador, no en la pantalla).