# GLM 5.2 — startup_content/workshop_outline

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 35.831s | tokens_per_second: 73.1
- input_tokens: 196 | output_tokens: 2621
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un outline detallado y práctico que se ajusta perfectamente a las necesidades de emprendedores no técnicos, con insights útiles y aplicables.

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

¡Hola! Qué excelente iniciativa. Como facilitador que ha recorrido el ecosistema Latam, te digo algo: los emprendedores early-stage no necesitan saber qué es el *backpropagation* o entender de tensores. Necesitan **ahorrar tiempo, validar más rápido y parecer equipos más grandes de lo que son**. 

Este workshop está diseñado para que en 3 horas salgan con un asistente virtual funcional (un GPT personalizado o un prompt system) que resuelva un cuello de botella real en su startup.

Aquí tienes el outline completo, con tono pragmático, enérgico y 100% orientado a la acción.

---

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"

**Duración:** 3 horas (180 min)
**Audiencia:** 20-30 emprendedores early-stage no-técnicos.
**Requisito previo:** Tener una cuenta de ChatGPT Plus (GPT-4) o Claude Pro. (Se les debe avisar al inscribirse).

---

## 1. Materiales Necesarios (Preparación previa)

**Para el facilitador:**
*   Proyector y pantalla.
*   Conexión a internet robusta (¡crítico!).
*   Tu propio "GPT" o Asistente terminado para hacer la Demo en vivo.
*   Slides con poco texto y mucho contraste.
*   Pizarrón/marcadores o papelógrafos para la lluvia de ideas.

**Para los asistentes:**
*   Laptops (obligatorio, no tablets).
*   Cuentas activas de ChatGPT Plus o Claude Pro.
*   1 caso de uso real de su startup que quieran resolver (ej: "tardo mucho en responder correos de clientes" o "no sé cómo estructurar mis posts de LinkedIn").

---

## 2. Agenda Detallada y Bloques

### Bloque 1: Bienvenida y Hackeo de la Mente Emprendedora (20 min)
*   **Título:** De Fundador Ahogado a Director de Orquesta.
*   **Objetivo:** Cambiar el chip de "la IA me va a quitar el trabajo" a "la IA es mi primer empleado multifuncional".
*   **Dinámica:** Charla rápida e interactiva. Preguntar a la audiencia cuántas horas a la semana pierden en tareas operativas. Mostrar 3 ejemplos rápidos de prompts malos vs. prompts buenos.
*   **Key Takeaway:** La IA no es un oráculo mágico, es un empleado brillante pero literal que necesita un manual de operaciones claro.
*   **Slide count:** 6 slides (Título, El problema, El cambio de mentalidad, Prompt Malo vs Bueno, Reglas del juego, Transición).

### Bloque 2: Anatomía de un Asistente de IA (25 min)
*   **Título:** El ADN de tu Asistente: Contexto, Rol y Restricciones.
*   **Objetivo:** Entender los 4 componentes de un "System Prompt" (Instrucción) de alto nivel.
*   **Dinámica:** Charla demostrativa. Explico el framework **C.A.R.T.** (Contexto, Acción, Rol, Tono). En vivo, armo un prompt para un asistente de soporte al cliente usando el framework.
*   **Key Takeaway:** Si no le das contexto a la IA, te dará respuestas genéricas de Wikipedia. El contexto es el rey.
*   **Slide count:** 5 slides (Framework C.A.R.T., Ejemplo de Contexto, Ejemplo de Rol/Tono, Restricciones, Demo en vivo).

### Bloque 3: Demo en Vivo - De Cero a Asistente en 5 Minutos (15 min)
*   **Título:** Mira esto: Tu COO Virtual.
*   **Objetivo:** Mostrar lo fácil y rápido que es crear un Asistente (usando la función "Custom GPTs" de OpenAI o "Projects" de Claude).
*   **Dinámica:** Demo en pantalla grande. Creo un asistente desde cero en vivo. Le subo un PDF con un manual de marca y le doy instrucciones. Le hago una pregunta difícil para mostrar cómo responde con el contexto dado.
*   **Key Takeaway:** No se requiere código. Solo se requiere claridad mental sobre cómo funciona tu negocio.
*   **Slide count:** 3 slides (Pantalla de creación, Subida de archivos, Prueba en vivo - *la mayor parte del tiempo es la pantalla de ChatGPT*).

### Bloque 4: Ejercicio Principal - Construcción (60 min)
*   *(Ver detalles en la sección 4)*
*   **Título:** Manos a la obra: Construyendo a tu "Primer Empleado".
*   **Objetivo:** Que cada asistente salga con un asistente funcional y probado.
*   **Dinámica:** Trabajo individual guiado. Yo voy pasando por las mesas con 2-3 asistentes ayudando a desbloquearlos.
*   **Key Takeaway:** La primera versión siempre será mala, pero iterar en vivo es como pulir un diamante.
*   **Slide count:** 4 slides (Instrucciones del ejercicio, Paso 1: Rol, Paso 2: Conocimiento, Paso 3: Prueba, Temporizador de 60 min en pantalla).

### Bloque 5: Break y Networking Temático (10 min)
*   **Título:** Café, Croquetas y Prompts.
*   **Objetivo:** Desconectar la vista de la pantalla y generar sinergia.
*   **Dinámica:** Pausa libre. Pego en la pared 3 "Retos Latam" para que los discutan tomando café.
*   **Key Takeaway:** El networking es mejor cuando hay un tema en común del que hablar.
*   **Slide count:** 1 slide (Pantalla con el cronómetro y los 3 retos de conversación).

### Bloque 6: Showcase y Feedback (30 min)
*   **Título:** Demo Day: Mostrando a los Monstruos.
*   **Objetivo:** Aprender de los errores y aciertos de otros.
*   **Dinámica:** Discusión. Se eligen 3-4 voluntarios al azar. Conectan su laptop, muestran su asistente, le hacen una pregunta en vivo. La audiencia da feedback. Yo hago de "Dragons' Den" (Shark Tank) dando 1 mejora rápida para cada uno.
*   **Key Takeaway:** Ver el uso de la IA en otros nichos te da ideas para tu propio negocio.
*   **Slide count:** 2 slides (Título del Showcase, Reglas de feedback).

### Bloque 7: Cierre y Recursos (20 min)
*   **Título:** El Plan de Acción del Lunes a las 9 AM.
*   **Objetivo:** Asegurar que la herramienta no se quede en el olvido después del workshop.
*   **Dinámica:** Charla de cierre y entrega de recursos. Compromiso público: cada uno dice en qué tarea usarán su asistente el próximo lunes.
*   **Key Takeaway:** La IA solo funciona si se convierte en un hábito diario.
*   **Slide count:** 4 slides (El error común del lunes, Compromiso público, Recursos para llevar, Agradecimiento y Contacto).

**Total Slides Estimadas:** ~25 slides (Diseño minimalista, alto contraste, tipografía grande).

---

## 3. Detalle del Ejercicio Principal (Bloque 4 - 60 min)

**Nombre:** "Contratando a tu IA: De Briefing a Prueba de Fuego"

**Paso 1: El Briefing (10 min)**
Cada emprendedor debe elegir UNA tarea específica que odia hacer o que le quita mucho tiempo. (Ej: *Redactar emails de seguimiento de ventas, estructurar el newsletter semanal, responder dudas de inversores*).
Deben escribir en un documento en blanco:
1. ¿Qué hace exactamente el asistente?
2. ¿Qué NO debe hacer? (Restricciones).
3. ¿Cómo debe sonar? (Tono de voz).

**Paso 2: Construcción (15 min)**
Van a la plataforma (ChatGPT Plus > Explore > Create a GPT).
*   Llenan la sección de "Instructions" usando el framework C.A.R.T.
*   *Opcional:* Si trajeron un PDF (manual de ventas, historial de correos, tono de voz de la marca), lo suben a "Knowledge".

**Paso 3: Prueba de Fuego (20 min) - "El Test del Cliente Enojado"**
Cada emprendedor debe hacerle a su nuevo asistente 3 preguntas o peticiones:
1. Una petición normal.
2. Una petición fuera de los límites (para ver si el asistente se rehúsa correctamente).
3. Una petición compleja o con un tono difícil (ej: "Hazlo más corto pero sin perder el enfoque comercial agresivo").

**Paso 4: Iteración (15 min)**
Basado en las respuestas, deben ajustar las instrucciones en la configuración para corregir alucinaciones o desviaciones de tono. El facilitador recorre la sala ayudando a "afinar" los prompts.

---

## 4. Recursos para Llevar a Casa (Swipe File)

Al finalizar, se les envía por correo (o se escanea un código QR) un "Kit de Supervivencia IA para Startups" que incluye:

1.  **El Framework C.A.R.T. (PDF imprimible):** Una plantilla de 1 página para que cada vez que vayan a crear un prompt complejo, la llenen mentalmente.
2.  **Biblioteca de 10 "Mega-Prompts" para Startups Latam:**
    *   Mega-Prompt para Analizar Competencia.
    *   Mega-Prompt para Estructurar Pitch Decks.
    *   Mega-Prompt para Resumir Feedback de Usuarios.
    *   Mega-Prompt para Crear Calendarios de Contenido.
    *   (Y 6 más orientados a operaciones, ventas y marketing).
3.  **Lista de Verificación de "Alucinaciones":** 5 señales de alerta para saber cuándo la IA está inventando datos y cómo corregirlo.
4.  **Directorio de Herramientas No-Code:** Enlaces directos a plataformas donde pueden conectar su nuevo asistente a WhatsApp, Telegram o su web sin saber programar (Make, Zapier, Voiceflow).
5.  **Comunidad:** Invitación a un grupo de WhatsApp/Discord exclusivo para los asistentes del workshop para compartir prompts y actualizaciones de IA.

---

### 💡 Tips del Facilitador para el Éxito:
*   **Manejo de la energía:** A la hora 1.5 (después del ejercicio largo), la gente estará cansada. El Break es sagrado. En el Showcase, mantén un ritmo rápido (máximo 5 min por persona).
*   **Gestión de expectativas:** Recuérdales que la IA a veces falla. Normalízalo. El objetivo no es la perfección, es el *speed to iteration*.
*   **Lenguaje Latam:** Usa analogías locales. En lugar de "optimización de recursos", usa "hacer más con menos plata". En lugar de "onboarding", usa "el manual del nuevo pasante". 

¡Mucho éxito en el workshop! Vas a ver caras de asombro cuando se den cuenta del poder que acaban de desbloquear.