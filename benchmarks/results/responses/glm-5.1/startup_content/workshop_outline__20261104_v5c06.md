# GLM-5.1 — startup_content/workshop_outline

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.28 | quality: 9.72
- latency_total: 46.737s | tokens_per_second: 54.1
- input_tokens: 196 | output_tokens: 2528
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

¡Hola, emprendedor! Como facilitador que ha recorrido el ecosistema LatAm, sé exactamente lo que necesitas: **cero humo, pura acción**. Los emprendedores early-stage no tienen tiempo para teorías aburridas sobre redes neuronales; necesitan ahorrar tiempo, validar más rápido y parecer equipos más grandes de lo que son.

Aquí tienes el outline detallado para un workshop intenso, práctico y de alto valor.

---

# 🚀 Outline del Workshop: "Construye tu Asistente de IA para tu Startup"

**Duración:** 3 horas (180 minutos)
**Audiencia:** 20-30 emprendedores early-stage (no-tecnicos)
**Enfoque:** 80% práctico, 20% inspiracional.

---

## 🎒 1. Materiales Necesarios (Preparación previa)

**Para el Facilitador:**
*   Proyector y pantalla (con cable HDMI y adaptadores, el Wi-Fi de las conferencias siempre falla).
*   Pizarra/Whiteboard y marcadores.
*   Cuentas premium activas (ChatGPT Plus o Claude Pro) para hacer demos en vivo sin límites.
*   Plantillas creadas en Notion o Google Docs (con links y códigos QR generados para entregar a los asistentes).

**Para los Asistentes:**
*   Laptops (Obligatorio. Avisar previamente que es un workshop hands-on, no una charla).
*   Cuenta gratuita (o pagada) en ChatGPT y/o Claude.ai.
*   1 problema o "dolor" real de su startup actual (ej: "tardo 3 horas en responder correos de clientes" o "no sé cómo estructurar mi pitch deck").

---

## ⏱️ 2. Agenda Detallada (3 Horas)

*   **00:00 - 00:15 | Bloque 1:** Hola, no estás solo. (Contexto y Mentalidad)
*   **00:15 - 00:45 | Bloque 2:** El arte de hablar con máquinas (Prompting nivel Ninja)
*   **00:45 - 01:45 | Bloque 3:** Manos a la obra: Construyendo tu Asistente (Ejercicio Principal)
*   **01:45 - 02:00 | ☕ Coffee Break**
*   **02:00 - 02:30 | Bloque 4:** Conectando los cables (Integración básica y Automatización)
*   **02:30 - 02:50 | Bloque 5:** Demo Day y Feedback
*   **02:50 - 03:00 | Bloque 6:** Cierre y Recursos

---

## 🛠️ 3. Desglose por Bloques

### Bloque 1: Hola, no estás solo. Contexto y Mentalidad
*   **Duración:** 15 min
*   **Objetivo:** Romper el hielo, quitar el miedo a la IA y alinear expectativas. La IA no quita tu trabajo, te ayuda a hacer el trabajo de 3 personas.
*   **Dinámica:** Charla rápida + Dolor en vivo. Preguntar a la audiencia: "¿Cuál es la tarea que más odian hacer en su startup?". Anotar 3 en la pizarra.
*   **Key Takeaway:** La IA es tu Co-founder de operaciones, no una bola de cristal. Basura entra, basura sale.
*   **Slide count estimado:** 5 slides (Título, El problema, La solución, Reglas del juego, Agenda).

### Bloque 2: El arte de hablar con máquinas (Prompting nivel Ninja)
*   **Duración:** 30 min
*   **Objetivo:** Enseñar la estructura de un prompt perfecto para que dejen de recibir respuestas genéricas.
*   **Dinámica:** Charla explosiva + Demo en vivo. Enseñar el framework **CREATE** (Contexto, Rol, Expectativa, Acción, Tono, Extras). Mostrar un prompt malo ("hazme un post de IG") vs. un prompt bueno usando el framework. Los asistentes lo replican en sus laptops al instante.
*   **Key Takeaway:** Trata a la IA como un pasante brillante pero despistado. Dile quién es, qué quieres, y cómo lo quieres.
*   **Slide count estimado:** 8 slides (Framework, Ejemplo Malo vs Bueno, Tips de contexto, Demo en vivo).

### Bloque 3: Manos a la obra: Construyendo tu Asistente (Ejercicio Principal)
*   **Duración:** 60 min
*   **Objetivo:** Que cada emprendedor salga con un "Custom GPT" (o Prompt Maestro estructurado) funcional para su startup.
*   **Dinámica:** Ejercicio guiado paso a paso.
    *   *Paso 1 (10 min):* Definir el rol del asistente (Ej: Community Manager, Analista de Competencia, Cerrador de Ventas).
    *   *Paso 2 (20 min):* Escribir el "System Prompt" (Instrucciones base) usando el framework.
    *   *Paso 3 (20 min):* Subir Knowledge Base (Subir PDFs de su marca, tono, productos).
    *   *Paso 4 (10 min):* Testing. Intentar "romper" el asistente haciendo preguntas trampa.
*   **Key Takeaway:** Un asistente de IA sin el contexto de tu negocio es inútil. El valor está en la *data* que le das.
*   **Slide count estimado:** 6 slides (Instrucciones paso a paso muy visuales, ejemplos de System Prompts, tiempo restante).

### ☕ Coffee Break (15 min)
*   *Nota del facilitador:* Asegúrate de que el Wi-Fi no colapse cuando 30 personas se conecten a la vez. Fomenta que hablen entre ellos sobre qué están construyendo.

### Bloque 4: Conectando los cables (Integración básica y Automatización)
*   **Duración:** 30 min
*   **Objetivo:** Mostrar cómo sacarle la IA del chat y llevarla al mundo real (Zapier/Make).
*   **Dinámica:** Demo rápida en vivo. Mostrar cómo conectar un correo de Gmail a ChatGPT para que redacte una respuesta automática y la guarde en Notion. *No esperamos que lo hagan ellos en 30 min, pero deben ver que es posible y fácil.*
*   **Key Takeaway:** Si tienes que copiar y pegar de ChatGPT a otra app, estás perdiendo el verdadero superpoder de la IA.
*   **Slide count estimado:** 5 slides (El ecosistema, Diagrama de Zapier/Make, Casos de uso reales para startups, Llamado a la acción).

### Bloque 5: Demo Day y Feedback
*   **Duración:** 20 min
*   **Objetivo:** Crear accountability y aprendizaje colaborativo.
*   **Dinámica:** Discusión. Pedir 3-4 voluntarios que pasen al frente (o compartan pantalla) y muestren qué asistente crearon. Hacerle una pregunta a su asistente en vivo. La audiencia aplaude y da 1 feedback.
*   **Key Takeaway:** Ver lo que otros construyeron inspira nuevas ideas para tu propio negocio.
*   **Slide count estimado:** 2 slides (Timer de 5 min por demo, Instrucciones para el feedback).

### Bloque 6: Cierre y Recursos para llevar a casa
*   **Duración:** 10 min
*   **Objetivo:** Terminar con la energía por las nubes y dejarlos con herramientas para seguir aprendiendo.
*   **Dinámica:** Charla de cierre motivacional. Entrega de un código QR gigante en la pantalla que los lleve a un Google Drive/Notion con todos los recursos.
*   **Key Takeaway:** El 90% de las startups van a usar IA el próximo año; el 10% que la *construya* en su ADN dominará el mercado.
*   **Slide count estimado:** 3 slides (Recursos, Comunidad/Código QR, Agradecimiento).

---

## 🏆 4. Ejercicio Principal del Workshop: "Tu Co-founder Virtual"

**El Reto:** Cada participante debe crear un **Custom GPT** (si tienen cuenta Plus) o un **Prompt Maestro guardado** (si tienen cuenta gratuita) que resuelva una tarea específica que hoy les quita al menos 2 horas a la semana.

**Pasos que seguirán:**
1.  **Elegir el dolor:** Ej. "Tengo que responder RFPs (Request for Proposals) de clientes potenciales y me toma 4 horas."
2.  **Bautizar el Asistente:** Ej. "El Cerrador RFP".
3.  **Configurar el System Prompt:** Escribirán: *"Eres un experto en ventas B2B en LatAm. Tu objetivo es responder RFPs usando la información de nuestra empresa que te voy a proporcionar. Tu tono es profesional pero cercano, sin usar lenguaje demasiado corporativo. Estructura la respuesta en 3 partes:..."*
4.  **Subir Knowledge:** Subirán 1 o 2 PDFs (su pitch deck, su catálogo de precios, o un documento de FAQ).
5.  **Prueba de fuego:** Escribirán en el chat: *"Acabo de recibir esta RFP: [Pegar texto real]. Ayúdame a responderla."* y verán la magia.

*Por qué funciona para no-tecnicos:* Es 100% interfaz visual, no requiere código, usa lenguaje natural y el resultado es inmediato y aplicable a su negocio el lunes a las 8 AM.

---

## 🎒 5. Recursos para llevar a casa (Leave-behind)

Se entregará mediante un link de Notion compartido al final del taller:

1.  **El Framework CREATE en PDF:** Una hoja de referencia rápida para pegar junto al monitor.
2.  **Biblioteca de System Prompts:** 5 plantillas de prompts maestros listos para copiar/pegar (Asistente de Copywriting, Analista de Datos, Brainstorming de Features, Redactor de Cold Emails, Estructurador de Pitch Deck).
3.  **Video-Tutorial de 5 minutos:** Cómo conectar Gmail + ChatGPT usando Zapier (para los que se quedaron con dudas del Bloque 4).
4.  **Lista de Playlists de YouTube/Canales recomendados:** Para seguir aprendiendo sobre IA aplicada a negocios (curada por el facilitador, sin humo).
5.  **Comunidad de WhatsApp del Workshop:** Para compartir prompts y resolver dudas post-evento (clave para el networking en LatAm).

---

## 📊 Resumen de Slide Count Total Estimado: ~29 Slides
*(Consejo del facilitador: Usa poco texto, mucho diseño. Tipografía grande. Si pones mucho texto, los emprendedores se pondrán a leer en vez de escucharte. Tu energía es el motor del taller).* 

¡A romperla! Que este workshop sea el punto de inflexión donde sus startups pasen de moverse en bicicleta a hacerlo en Tesla.