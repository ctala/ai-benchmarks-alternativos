# Gemini 3.5 Flash Lite — startup_content/workshop_outline

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 8.42 | quality: 9.44
- latency_total: 7.595s | tokens_per_second: 226.3
- input_tokens: 188 | output_tokens: 1719
- judge_score: 4.6 | justificación: 

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

¡Hola a todos! Qué gran iniciativa. Como facilitador en toda la región, te aseguro que este formato vuelve locos (en el buen sentido) a los emprendedores. Nada de teoría aburrida: aquí venimos a ensuciarnos las manos con IA sin saber escribir una sola línea de código. 

Aquí tienes el blueprint completo, diseñado con ritmo, energía y foco en el "hacer".

---

# 📋 Master Outline del Workshop

**Título:** Construye tu Asistente de IA para tu Startup - Workshop Práctico  
**Duración:** 3 horas (180 minutos)  
**Audiencia:** 20-30 emprendedores *early-stage* no-técnicos  
**Tono:** Enérgico, pragmático, sin jerga técnica innecesaria ("cero humo").  

---

## 1. Materiales Necesarios (Checklist Pre-Workshop)

*   **Para los asistentes:**
    *   Laptop cargada (Wi-Fi estable es OBLIGATORIO).
    *   Cuenta gratuita creada previamente en [Make.com](https://www.make.com) o [Voiceflow](https://www.voiceflow.com) (según la plataforma elegida) y OpenAI (ChatGPT).
    *   Tener claro en 2 líneas qué hace su startup (su "Elevator Pitch").
*   **Para el facilitador (Tú):**
    *   Proyector y adaptador HDMI/USB-C.
    *   Post-its y marcadores (por si acaso hay que hacer un diagrama mental rápido).
    *   Playlist de música electrónica/lo-fi para el momento de "manos a la obra".
    *   Templates pre-construidos (blueprints) para compartir por si alguien se atora técnicamente.

---

## 2. Agenda Detallada y Estructura por Bloques

### Bloque 1: Rompehielos y Mentalidad IA (El "Por qué")
*   **Duración:** 20 minutos
*   **Objetivo:** Desmitificar la IA, alinear expectativas y entender que la IA no es un juguete, sino un co-fundador operativo barato.
*   **Dinámica:** Charla interactiva de 10 min + Dinámica relámpago "Mi mayor cuello de botella" (en parejas, 5 min) + puesta en común (5 min).
*   **Key Takeaway:** No necesitas programar para automatizar; necesitas saber qué problema quieres resolver.
*   **Slide Count Estimado:** 5 slides.

### Bloque 2: Anatomía de un Buen Asistente (El "Qué")
*   **Duración:** 25 minutos
*   **Objetivo:** Enseñar a diseñar prompts avanzados y entender cómo "alimentar" de contexto a una IA para que hable por tu startup.
*   **Dinámica:** Demo en vivo en pantalla grande. Crearemos un prompt maestro para un rol específico (ej: soporte al cliente) en vivo usando los dolores de un asistente del público.
*   **Key Takeaway:** La IA es tan buena como el contexto y las restricciones que le das (Rol + Contexto + Tarea + Formato).
*   **Slide Count Estimado:** 6 slides.

### Bloque 3: *Hands-On* - El Taller de Construcción (El "Cómo")
*   **Duración:** 80 minutos (El corazón del workshop)
*   **Objetivo:** Que cada emprendedor construya y pruebe su propio asistente funcional de IA adaptado a su negocio.
*   **Dinámica:** Ejercicio práctico guiado (paso a paso). *Ver detalle en la sección 4.* Habrá música de fondo y asistencia "circulante" (tú y un asistente resolviendo dudas en las mesas).
*   **Key Takeaway:** ¡Lo logré! Si pude hacer esto en una hora, puedo automatizar el 30% de operación la próxima semana.
*   **Slide Count Estimado:** 3 slides (principalmente guías visuales de los pasos).

*Pausa para café / Networking rápido: 10 minutos (crucial para bajar revoluciones y destrabar casos)*

### Bloque 4: Integración y Casos de Uso en el Mundo Real
*   **Duración:** 25 minutos
*   **Objetivo:** Ver cómo conectar este asistente con herramientas del día a día (WhatsApp, Notion, Email, Web).
*   **Dinámica:** Demostración rápida de integraciones (ej: conectar el bot a un formulario o WhatsApp) + Discusión abierta de casos de uso de los asistentes construidos.
*   **Key Takeaway:** Un asistente aislado sirve poco; integrado a tus canales de venta o soporte, es una máquina de hacer dinero y ahorrar tiempo.
*   **Slide Count Estimado:** 4 slides.

### Bloque 5: Pitch Relámpago y Cierre de Impacto
*   **Duración:** 20 minutos
*   **Objetivo:** Celebrar los logros, inspirar acción inmediata y cerrar con energía alta.
*   **Dinámica:** "Show & Tell". 3 valientes muestran rápidamente en la pantalla grande lo que construyeron y cómo les va a ahorrar horas esta misma semana. Entrega de recursos y cierre.
*   **Key Takeaway:** El futuro pertenece a los fundadores que implementan en horas, no en meses. ¡A ejecutar!
*   **Slide Count Estimado:** 2 slides.

---

## 3. Ejercicio Principal del Workshop: "El Asistente Todoterreno"

Para este workshop, utilizaremos **Voiceflow** o **Make.com + OpenAI** (recomiendo Voiceflow por su interfaz visual tipo nodo, muy amigable para no-técnicos).

*   **Reto:** Construir un Asistente Virtual de IA para la startup de cada participante que responda preguntas frecuentes (FAQs), califique leads (prospectos) o actúe como un coach interno.
*   **Paso a Paso del Ejercicio:**
    1.  **Definir la Persona:** ¿Quién es tu bot? (Ej: "Sofia, la asistente de ventas de mi app de fitness").
    2.  **Cargar el Contexto (Knowledge Base):** Subir un PDF con la info de su startup o copiar/pegar sus precios, servicios y políticas en la cajita de conocimiento de la IA.
    3.  **Configurar el Comportamiento (System Prompt):** Darle instrucciones estrictas: *"Eres amable, directo, usas emojis, y si no sabes algo, pides el correo del usuario"*.
    4.  **Probar y Ajustar:** Usar el chat de prueba integrado para hacerle "bullying" al bot (hacerle preguntas trampa) y afinar sus respuestas.
    5.  **Publicar:** Obtener el link o el código embed para ponerlo a prueba en un navegador web.

---

## 4. Recursos para Llevar a Casa (Kit Post-Workshop)

Envía este correo a todos los asistentes al terminar el evento:

1.  **Notion Template:** "El Prompt Deck para Startups" (Una base de datos con más de 20 prompts probados para marketing, ventas, legales y operaciones).
2.  **Guía PDF en 1 página:** "Checklist para conectar tu IA a WhatsApp sin morir en el intento".
3.  **Acceso a la comunidad:** Un grupo de Slack/WhatsApp temporal para resolver dudas de los siguientes 7 días.
4.  **El Link de la grabación** del paso a paso técnico (por si quieren repetirlo el domingo en la noche).

---
*¡Listo! Con este diseño, la energía no decae, la gente se lleva algo funcionando a su casa y sales posicionado como un referente práctico en tecnología aplicada a negocios en Latinoamérica.*