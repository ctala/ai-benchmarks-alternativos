# DeepSeek V3 — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 42.782s | tokens_per_second: 47.9
- input_tokens: 198 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que proporciona información práctica y útil para emprendedores no técnicos, aunque podría profundizar un poco más en ciertos aspectos.

## Respuesta completa

# **Workshop: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"**
**Duración:** 3 horas presenciales | **Audiencia:** 20-30 emprendedores early-stage no-técnicos
**Tono:** Energético, práctico, orientado a la acción.

---

### **1. AGENDA DETALLADA (3h)**
*   **Bloque 0: Bienvenida & Setup (15 min)**
*   **Bloque 1: Desmitificando la IA: Tu Nuevo Cofundador Digital (30 min)**
*   **Bloque 2: Descubre el Dolor de tu Startup que la IA Puede Aliviar (30 min)**
*   **--- PAUSA / NETWORKING (15 min) ---**
*   **Bloque 3: De la Idea al Prototipo: La Caja de Herramientas No-Code (40 min)**
*   **BLOQUE PRINCIPAL: Ejercicio Práctico - ¡Ensambla tu Primer Asistente! (35 min)**
*   **Bloque 4: Presentaciones Relámpago y Próximos Pasos (15 min)**

---

### **2. MATERIALES NECESARIOS (Preparar antes)**
*   **Para el facilitador:**
    *   Laptop, proyector, micrófono (si la sala es grande).
    *   Cuentas PRO/Premium en plataformas no-code (ej: Make.com, Zapier, Bubble) para demo fluida.
    *   Cuenta en ChatGPT Plus/Claude/Copia para demostraciones en vivo.
    *   Slides (ver estimado por sección más abajo).
    *   Cronómetro visible.
*   **Para los participantes:**
    *   **Requisito previo:** Pedir que traigan su laptop y que tengan creadas cuentas gratuitas básicas en **ChatGPT** y en una plataforma como **Make.com** (Zapier) o **Botpress** (dependiendo del ejercicio elegido).
    *   Sala con mesas para trabajar en parejas o individualmente.
    *   Pizarras blancas o pads de papel + marcadores para cada mesa.
    *   Sticky notes.
    *   WiFi robusto y de acceso fácil.
    *   **Handout físico** con: Agenda, espacio para notas, lista de recursos y pasos del ejercicio principal.

---

### **3. BLOQUES DETALLADOS**

#### **BLOQUE 0: Bienvenida & Setup (15 min)**
*   **Dinámica:** Charla energética + instrucción práctica.
*   **Objetivo:** Romper el hielo, establecer el tono práctico y asegurar que todos tengan el setup técnico listo.
*   **Key Takeaway:** "En 3 horas, no solo aprenderás, sino que **construirás algo tangible** para tu startup."
*   **Actividad:**
    1.  Saludo de alta energía, presentación breve del facilitador con ejemplos de IA en startups latinoamericanas.
    2.  Instrucción clara: "Saquen sus laptops. Abran el navegador. Verifiquen que pueden acceder a: 1) ChatGPT, 2) Make.com".
    3.  Pregunta rápida de levantamanos: "¿Quién ha usado ChatGPT más de 5 veces?" / "¿Quién ha automatizado algo en su vida o negocio?".

#### **BLOQUE 1: Desmitificando la IA: Tu Nuevo Cofundador Digital (30 min)**
*   **Dinámica:** Charla visual con DEMOS EN VIVO rápidas y contundentes.
*   **Objetivo:** Quitar el miedo técnico y mostrar la IA como una "herramienta de leverage" para el emprendedor.
*   **Key Takeaway:** La IA no es magia, es un **trabajador infatigable y especializado** que tú puedes dirigir.
*   **Contenido:**
    *   **NO es:** Explicar transformers o algoritmos.
    *   **SÍ es:** Mostrar ejemplos concretos:
        *   Demo 1: De una descripción de cliente a un correo de ventas personalizado en 10 segundos.
        *   Demo 2: De una idea de post a 10 ideas de contenido con calendario.
        *   Demo 3: De un documento lleno de datos de entrevistas a usuarios a un resumen de "pain points" clave.

#### **BLOQUE 2: Descubre el Dolor de tu Startup que la IA Puede Aliviar (30 min)**
*   **Dinámica:** Ejercicio guiado individual/en parejas + discusión grupal.
*   **Objetivo:** Identificar **una** área de su startup donde un asistente de IA generaría impacto inmediato (ventas, soporte, contenido, investigación).
*   **Key Takeaway:** El problema bien definido es el 80% del éxito. No se trata de usar IA por usarla.
*   **Actividad (Ejercicio de "Mapa de Dolor"):**
    1.  Plantilla en slide/pizarra: "¿Qué tarea te quita **más tiempo** y es **repetitiva**?" / "¿Qué información tienes desorganizada (chats, correos, notas)?" / "¿Qué interacción con clientes no escalas?".
    2.  5 min individual: Escribir en sticky notes sus 2-3 "dolores" principales.
    3.  10 min en mesas: Agrupar y priorizar dolores comunes.
    4.  10 min grupal: Compartir 1-2 dolores por mesa. Facilitador los categoriza en tiempo real (ej: "Atención al cliente", "Generación de leads", "Análisis de datos").

#### **--- PAUSA / NETWORKING (15 min) ---**
*   **Consigna:** "Hablen con alguien que tenga un 'dolor' similar al suyo. Intercambien ideas."

#### **BLOQUE 3: De la Idea al Prototipo: La Caja de Herramientas No-Code (40 min)**
*   **Dinámica:** Demo magistral PASO A PASO de un caso concreto.
*   **Objetivo:** Mostrar cómo las piezas (LLM + No-Code + APIs) se unen para crear un asistente funcional.
*   **Key Takeaway:** Tú puedes **orquestar** la tecnología sin saber programar.
*   **Contenido:**
    *   **Caso Ejemplo:** "Asistente que califica leads desde un formulario web".
    *   Demo en vivo (lenta, clara):
        1.  El "trigger" (nuevo dato en Google Sheets).
        2.  La "acción mágica" (envío del dato a ChatGPT con un "prompt" bien diseñado).
        3.  El "resultado" (la IA devuelve un score y comentario).
        4.  La "acción posterior" (el resultado se guarda en Sheets o envía un Slack).
    *   **Énfasis en el PROMPT como la pieza clave:** Mostrar la plantilla y cómo mejorarla.

---

### **4. EJERCICIO PRINCIPAL DEL WORKSHOP (35 min)**
**Título:** **"Ensambla tu Asistente: Automatiza tu Primer Flujo de Trabajo"**
**Objetivo:** Que cada participante salga con un prototipo funcional, aunque sea mínimo.
**Instrucciones Guiadas (Facilitador con cronómetro):**
1.  **Min 0-5:** Elige TU dolor prioritario del Bloque 2. Ej: "Clasificar preguntas frecuentes de mis clientes de WhatsApp".
2.  **Min 5-15:** **Diseña tu Prompt** en un doc. Usa la plantilla: "Eres un asistente especializado en [tu industria]. Tu tarea es [acción concreta]. La información de entrada es: [ejemplo de dato]. Formato de salida: [ej: lista, sí/no, score]".
3.  **Min 15-30:** **Construye el flujo en Make.com/Zapier.**
    *   Paso 1 (Trigger): Elige una opción simple (ej: "Clic en un botón webhook" o "Nueva fila en Google Sheets").
    *   Paso 2 (Acción de IA): Conecta el módulo de ChatGPT/OpenAI. Pega tu prompt. Mapea la data de entrada.
    *   Paso 3 (Resultado): Añade un módulo para ver el resultado (ej: "Enviar por email a mí" o "Guardar en nota").
4.  **Min 30-35:** **PRUEBA y DEPURA.** Ejecuta el flujo una vez con datos de ejemplo. ¿Funcionó? ¿Cómo mejorar el prompt?
**Soporte:** Facilitador y asistentes caminan por la sala resolviendo dudas rá