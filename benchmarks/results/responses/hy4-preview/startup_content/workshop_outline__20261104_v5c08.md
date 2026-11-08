# Tencent Hy4 preview — startup_content/workshop_outline

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.13 | quality: 9.44
- latency_total: 44.392s | tokens_per_second: 53.4
- input_tokens: 223 | output_tokens: 2371
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

¡Hola! Qué buen proyecto. Como facilitador, sé que en Latinoamérica el emprendedor es **echado para adelante** y necesita ver resultados el mismo día, no teoría de silicio. Si les hablas de "transformers" o "redes neuronales" en la primera media hora, los pierdes.

Aquí tienes el diseño del workshop **"Construye tu Asistente de IA para tu Startup"**, pensado para que salgan con la herramienta funcionando en sus celulares o laptops.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup

**Duración Total:** 180 minutos (3 horas)
**Audiencia:** 20-30 Emprendedores (Nivel: No técnico)
**Vibe:** Energético, "Manos a la obra", Práctico.

## 1. Preparativos y Materiales (Checklist antes del evento)

Para que esto fluya, no podemos depender del wifi del lugar.

*   **Conectividad:** Internet dedicado para el facilitador. Recomendar a los asistentes traer datos móviles cargados por si falla el WiFi del venue.
*   **Herramientas:** Cuenta de OpenAI (ChatGPT Plus - *recomendado para usar GPTs*) o acceso a Google Gemini / Claude.
*   **Material Físico:**
    *   Impresión de la **"Plantilla de Prompt Maestro"** (1 por persona).
    *   Post-its y marcadores.
    *   Código QR gigante en la pantalla de inicio para descargar el PDF de recursos.
*   **Setup del Facilitador:**
    *   Proyector y adaptadores HDMI/USB-C.
    *   Un ejemplo de GPT (Asistente) ya creado para mostrar al inicio.

---

## 2. Agenda Detallada (El "Run of Show")

### Bloque 1: El "Mindset" de la IA (Romper el Hielo)
**Duración:** 30 minutos
**Objetivo:** Desmitificar la IA. Pasar de "es una caja mágica" a "es mi nuevo empleado gratis".

*   **Dinámica:**
    *   *Charla Relámpago (10 min):* No hables de tecnología. Habla de **delegación**. La IA es un pasante muy inteligente pero que necesita instrucciones claras.
    *   *Demo en Vivo (10 min):* Muestra un Asistente de IA ya creado (ej. Un experto en Marketing para Cafeterías) resolviendo un problema real en 30 segundos.
    *   *Ejercicio Rápido (10 min):* "La Pregunta Tonta". Pídanles que le pregunten a su ChatGPT/Gemini algo sobre su modelo de negocio para ver qué responde (generalmente algo genérico).
*   **Key Takeaway:** La IA no te va a quitar el trabajo, pero un emprendedor que usa IA le va a quitar el trabajo a uno que no.
*   **Slides Estimados:** 5-8 slides.

---

### Bloque 2: La Anatomía de un "Buen" Prompt (La Estructura)
**Duración:** 30 minutos
**Objetivo:** Aprender la estructura CO-STAR (Contexto, Objetivo, Estilo, Tono, Audiencia, Respuesta) o una simplificada para LATAM: **Rol - Tarea - Contexto - Formato**.

*   **Dinámica:**
    *   *Charla (10 min):* Explicar por qué fallan los prompts (falta de contexto). Introducir la fórmula mágica.
    *   *Ejercicio en Parejas (15 min):* Escribir un prompt para redactar un mensaje de ventas para WhatsApp usando la fórmula.
    *   *Discusión (5 min):* 2 voluntarios leen su prompt y la sala vota: ¿Suena a robot o a humano?
*   **Key Takeaway:** "Basura entra, basura sale" (GIGO). La calidad de tu respuesta depende de la calidad de tu instrucción.
*   **Slides Estimados:** 6-10 slides.

---

### Bloque 3: ¡Manos a la Obra! (El Ejercicio Principal)
**Duración:** 60 minutos
**Objetivo:** Construir un "Asistente Experto" personalizado (Custom GPT o Gem) para un área específica de su startup (Ventas, Soporte, Contenido).

*   **Dinámica:**
    *   *Demo Paso a Paso (15 min):* El facilitador crea un GPT desde cero en pantalla.
        1.  Ir a "Explorar GPTs" -> "Crear".
        2.  Configurar (Nombre, Descripción).
        3.  *El Cerebro:* Pegar las instrucciones (usando la fórmula del Bloque 2).
        4.  Subir conocimientos (opcional: subir un PDF de precios o menú).
    *   **Work Time (30 min):** Los participantes construyen su propio asistente.
        *   *Facilitador:* Camina entre las mesas ayudando a destrabar a los que tienen errores (troubleshooting).
    *   **Show & Tell (15 min):** 3 participantes muestran su asistente a todo el grupo y reciben feedback.
*   **Key Takeaway:** No necesitas programar para tener software propietario. Tu "prompt" es tu código.
*   **Slides Estimados:** 3-5 slides (aquí se usa poco slide y mucho pantallazo en vivo).

---

### Bloque 4: Estrategia de Implementación y Límites
**Duración:** 30 minutos
**Objetivo:** Dónde NO usar IA y cómo integrarla en el flujo de trabajo diario.

*   **Dinámica:**
    *   *Charla (10 min):* Alucinaciones (mentiras de la IA), privacidad de datos y el factor humano.
    *   *Ejercicio Grupal (10 min):* "El Mapa de la IA". En una hoja, dibujar un proceso de su negocio (ej. Onboarding de cliente) y marcar con un post-it verde dónde entra la IA y rojo dónde NO debe entrar.
    *   *Discusión (10 min):* Compartir hallazgos.
*   **Key Takeaway:** La IA es el copiloto, tú eres el piloto. Nunca publiques nada sin revisarlo.
*   **Slides Estimados:** 5 slides.

---

### Bloque 5: Cierre y Compromiso
**Duración:** 15 minutos (más 15 de networking)
**Objetivo:** Asegurar que apliquen lo aprendido mañana mismo.

*   **Dinámica:**
    *   *Charla (5 min):* Resumen de lo logrado.
    *   *Acción (5 min):* "La Promesa". Pedir que saquen el celular y pongan una alarma para mañana a las 9:00 AM que diga: "Usar mi Asistente para [Tarea X]".
    *   *Cierre (5 min):* Entrega de certificados digitales o acceso a la comunidad de WhatsApp.
*   **Key Takeaway:** La mejor IA del mundo es inútil si no la usas.
*   **Slides Estimados:** 2 slides.

---

## 3. El Ejercicio Principal (Detalle Técnico para No-Técnicos)

**Nombre:** "Tu Primer Empleado Digital"

Usaremos la funcionalidad de **GPTs Personalizados (OpenAI)** o **Gems (Google)** porque es visual, no requiere código (no-code) y es gratuito (en el caso de Google) o accesible (versión Plus de ChatGPT).

**Instrucciones para los participantes:**
1.  Abre ChatGPT o Gemini.
2.  Busca "Crear un GPT" o "Nuevo Gem".
3.  **Instrucciones (El Cerebro):** Vas a copiar y pegar este texto (rellenando los espacios):
    > "Actúa como un experto en [Tu Industria, ej. Fitness]. Tu objetivo es ayudarme a crear contenido para redes sociales.
    > **Contexto:** Mi startup vende [Producto] a [Audiencia].
    > **Tono:** Amigable, motivador, usando jerga de Latinoamérica (no español de España).
    > **Reglas:** No inventes precios. Siempre termina con una pregunta para generar engagement."
4.  **Prueba:** Hazle una pregunta difícil a tu asistente para ver si respeta las reglas.

---

## 4. Recursos para llevar a casa (El "Swag Bag" Digital)

Al final, proyecta un código QR o envía un link con una carpeta de Drive/Notion que contenga:

1.  **La Chuleta de Prompts (PDF):** Una hoja con 10 prompts listos para copiar y pegar (para Email Marketing, para Ideas de Negocio, para Analizar Contratos, etc.).
2.  **Plantilla de Configuración:** El esqueleto del prompt del Bloque 3 en Word/Google Docs para que solo rellenen espacios.
3.  **Lista de Herramientas:** Los 5 "Top AI Tools" para emprendedores (ej. Gamma.app para slides, Suno para música, etc.).
4.  **Grupo de WhatsApp/Telegram:** Para seguir compartiendo dudas.

---

### Consejos Pro para el Facilitador (Tips LATAM):
*   **Música:** Ten una playlist de reggaeton o rock en español suave al entrar y en los breaks.
*   **Idioma:** Usa términos locales. No digas "ordenador", di "computadora". No digas "móvil" si en el país dicen "celular".
*   **Errores:** Cuando algo falle en vivo (que va a pasar), ríete y úsalo como lección: "Vean, esto es lo que pasa cuando no le damos buen contexto". Eso genera empatía.