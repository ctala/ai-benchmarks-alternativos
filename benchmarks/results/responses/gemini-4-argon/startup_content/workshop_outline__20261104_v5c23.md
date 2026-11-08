# Gemini 4 Argon — startup_content/workshop_outline

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.06 | quality: 9.72
- latency_total: 43.553s | tokens_per_second: 53.5
- input_tokens: 217 | output_tokens: 2328
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

¡Hola! Qué gran iniciativa. En Latinoamérica, los emprendedores *early-stage* suelen ser el "hombre o mujer orquesta": hacen ventas, marketing, operaciones y atención al cliente al mismo tiempo. Este workshop no debe tratarse sobre "cómo funciona la tecnología", sino sobre **"cómo clonar tu tiempo y escalar sin presupuesto"**.

Aquí tienes el diseño completo del workshop, pensado para mantener la energía alta, evitar la jerga técnica y asegurar que todos salgan con algo funcionando en sus manos.

---

# 🚀 Workshop: "Construye tu Asistente de IA para tu Startup"
**Duración:** 3 horas (Presencial)
**Audiencia:** 20-30 Founders *early-stage* (No-técnicos)
**Meta:** Que cada founder salga con un prototipo funcional de su "Primer Empleado Digital" en su computadora o celular.

---

## 🛠️ Materiales Necesarios (Qué preparar antes)

**Para los participantes (enviar por correo/WhatsApp 48h antes):**
*   Laptop (obligatorio) y cargador.
*   Tener creada una cuenta en ChatGPT (idealmente Plus, pero daremos opciones gratuitas como Poe.com o Claude).
*   Traer en un documento de Word/Docs: 1) Descripción de su startup (1 párrafo), 2) Las 5 preguntas más frecuentes de sus clientes, 3) Un ejemplo de un correo o mensaje de ventas que hayan enviado y haya funcionado.

**Para el espacio y facilitador:**
*   WiFi de alta velocidad (¡Crucial! Probar que aguante 30 dispositivos).
*   Proyector / Pantalla grande con conexión HDMI.
*   2 Flipcharts (rotafolios) con marcadores gruesos.
*   Post-its de dos colores y bolígrafos para cada mesa.
*   **Vital en LatAm:** Regletas/zapatillas eléctricas en todas las mesas y una buena estación de café/agua.
*   Un código QR gigante en la pantalla que lleve a un Notion o Google Doc con los recursos del día.

---

## ⏱️ Agenda Detallada y Estructura de Bloques (3 Horas)

### Bloque 1: El fin del "Founder Pulpo" (20 min)
*   **Objetivo:** Romper el hielo, desmitificar la IA y cambiar el chip mental de "herramienta de búsqueda" a "miembro del equipo".
*   **Dinámica:** *Charla + Rompehielos rápido.* Pregunta a la sala quién trabajó más de 10 horas ayer. Explica la diferencia entre usar ChatGPT como Google vs. usarlo como un pasante superdotado.
*   **Key Takeaway:** "No necesitas saber programar (código); el nuevo lenguaje de programación es el español bien estructurado".
*   **Slide count:** 5 slides (muy visuales, pocos textos).

### Bloque 2: La Auditoría del Dolor (25 min)
*   **Objetivo:** Identificar exactamente qué tarea le van a delegar a su IA hoy (evitar que quieran abarcar todo).
*   **Dinámica:** *Ejercicio con Post-its + Discusión en parejas.*
    *   En Post-its rosas: 3 tareas que odian hacer o les quitan mucho tiempo.
    *   En Post-its verdes: Qué harían si tuvieran 10 horas extra a la semana.
    *   Seleccionan **UNA** tarea repetitiva (Ej: responder dudas en Instagram, redactar propuestas, crear contenido para LinkedIn, filtrar CVs).
*   **Key Takeaway:** "La IA no reemplaza al founder, reemplaza las tareas que drenan la energía del founder".
*   **Slide count:** 3 slides (instrucciones del ejercicio).

### Bloque 3: La Anatomía del Prompt Perfecto (35 min)
*   **Objetivo:** Enseñarles a dar instrucciones precisas a la IA para que no suene como un robot genérico.
*   **Dinámica:** *Charla práctica + Demo en vivo.* Explicar el framework **C.R.E.O.** (Contexto, Rol, Especificaciones, Output/Formato). Hacer una demo en pantalla mostrando un prompt malo ("escríbeme un post de ventas") vs. un prompt nivel Pro usando los datos de la startup de algún voluntario.
*   **Key Takeaway:** "Basura entra, basura sale. La calidad de tu asistente depende de la calidad de tu contexto".
*   **Slide count:** 8 slides (ejemplos del antes y después, desglose del framework).

---
### ☕ BREAK & NETWORKING (15 min)
*Momento para recargar café, conectar entre founders y resolver dudas puntuales con el facilitador.*
*(0 slides, dejar un contador regresivo en pantalla con música energética).*

---

### Bloque 4: Manos a la Obra - Construyendo a tu Clon (50 min)
*   **Objetivo:** Que cada participante configure, alimente y pruebe su propio asistente de IA personalizado.
*   **Dinámica:** *Ejercicio Principal (Ver detalle en la sección 4).* Trabajo individual guiado paso a paso por el facilitador, con soporte mesa por mesa.
*   **Key Takeaway:** "Acabas de crear un activo para tu empresa en menos de una hora y a costo cero".
*   **Slide count:** 4 slides (el paso a paso fijo en pantalla para que nadie se pierda).

### Bloque 5: "Roast my Bot" - Pruebas de Fuego (20 min)
*   **Objetivo:** Validar que los asistentes funcionen bien, iterar errores y aprender de los casos de uso de otros.
*   **Dinámica:** *Demo participativa / Juego de roles.* Los participantes intercambian laptops con el compañero de al lado. El compañero actúa como un "cliente difícil" o "usuario exigente" y chatea con el bot del otro para intentar "romperlo". Luego, 2 o 3 voluntarios pasan al frente a mostrar su bot en la pantalla grande.
*   **Key Takeaway:** "Tu asistente aprende por iteración. Cada error es una instrucción más que debes agregar a su base de conocimiento".
*   **Slide count:** 2 slides.

### Bloque 6: Más allá del Chat y Cierre (15 min)
*   **Objetivo:** Mostrarles el futuro (automatización) sin abrumarlos y cerrar con la energía arriba.
*   **Dinámica:** *Charla inspiracional + Q&A.* Mostrar brevemente (sin hacer tutorial) cómo ese cerebro que acaban de crear se puede conectar en el futuro a WhatsApp, a su web o a su correo usando herramientas No-Code (Make, Zapier, ManyChat). Foto grupal.
*   **Key Takeaway:** "Hoy construyeron el cerebro. Mañana le pondremos manos y pies. No se queden atrás".
*   **Slide count:** 4 slides (incluyendo el QR de recursos y contacto).

---

## 🛠️ 4. El Ejercicio Principal del Workshop (Bloque 4)

**Nombre del ejercicio:** "Mi Primer Empleado Digital"
**Herramienta a usar:** *Custom GPTs* (para los que tienen ChatGPT Plus) o *Poe.com* (gratuito, permite crear bots personalizados fácilmente y compartirlos con un link, ideal para que nadie se quede afuera por no pagar).

**El Paso a Paso (50 min):**

1.  **Bautizo y Rol (5 min):** Ponerle nombre al bot (ej: "Sofía, experta en soporte de [Nombre Startup]") y definir su objetivo único basándose en el Post-it del Bloque 2.
2.  **Inyección de Cerebro - El Prompt Maestro (15 min):** Los founders llenan una plantilla (provista por ti en el Notion) que incluye:
    *   *Quién eres:* Experto en X.
    *   *Tono de voz:* (Ej: Amigable, usa modismos colombianos/mexicanos, empático, conciso).
    *   *Reglas de oro:* (Ej: "Nunca inventes precios", "Siempre termina con una pregunta para cerrar la venta", "Usa emojis moderadamente").
3.  **La Base de Conocimiento (15 min):** Con el material que trajeron de casa, crean un PDF rápido o documento de texto con las FAQs, precios e historia de la empresa, y lo suben al bot (Knowledge Base) para que responda con datos reales de la startup.
4.  **Entrenamiento (15 min):** Chatear con su propio bot, ver qué responde mal, ir a la configuración y ajustar las instrucciones ("Le dije que sea breve pero me escribe testamentos, ¿cómo lo arreglo?").

---

## 🎁 5. Recursos para llevar a casa (El "Goodie Bag" Digital)

A través de un código QR al final, les entregas un link de Notion con:
1.  **El "Cheat Sheet" del Framework C.R.E.O.:** Un PDF de 1 página para imprimir y tener al lado de la computadora.
2.  **Biblioteca de 5 Prompts para Startups:** Prompts listos para copiar y pegar (1. Para estructurar un Pitch Deck, 2. Para responder a clientes enojados, 3. Para crear un calendario de contenidos mensual, 4. Para analizar a la competencia, 5. Para redactar correos en frío).
3.  **Mapa de Herramientas No-Code:** Una lista curada de herramientas para el "siguiente nivel" (ManyChat para Instagram/WhatsApp, Make.com para automatizar, Gamma.app para hacer presentaciones con IA, Perplexity para investigación de mercado).
4.  **Acceso a una Comunidad (Opcional pero recomendado):** Un grupo de WhatsApp de los asistentes al workshop para que compartan los links de sus bots y se den feedback durante la semana siguiente.

---

## 📊 6. Resumen de Slides (Total: ~26 slides)

*   **Bloque 1:** 5 slides
*   **Bloque 2:** 3 slides
*   **Bloque 3:** 8 slides
*   **Break:** 1 slide (Timer)
*   **Bloque 4:** 4 slides
*   **Bloque 5:** 2 slides
*   **Bloque 6:** 4 slides

**Tip de Facilitador LatAm:** Mantén las slides muy limpias. Usa memes locales de emprendimiento para explicar conceptos difíciles. Si la energía baja después del break, haz que todos se pongan de pie para el ejercicio "Roast my Bot". ¡Mucho éxito, la van a romper!