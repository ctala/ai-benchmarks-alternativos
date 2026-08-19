# Gemma 4 26B MoE (3.8B activos) — startup_content/workshop_outline

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.1 | quality: 9.44
- latency_total: 100.6s | tokens_per_second: 16.1
- input_tokens: 207 | output_tokens: 1621
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Hola! Como facilitador, entiendo perfectamente el reto: tienes un grupo de emprendedores que tienen hambre de resultados, pero que pueden sentirse intimidados por la tecnología. El secreto de este workshop no es enseñarles a programar, sino enseñarles a **"orquestar"** la IA para que trabaje para ellos.

Aquí tienes el diseño de la experiencia.

---

# Workshop: Construye tu Asistente de IA para tu Startup
**Formato:** Presencial | **Duración:** 3 Horas | **Perfil:** Emprendedores No-Técnicos

## 1. Agenda Detallada (Timeline)

*   **00:00 - 00:15:** Bienvenida, Contexto y "El Mindset del Orquestador"
*   **00:15 - 00:45:** Bloque 1: De la Idea al Prompt Maestro (Ingeniería de Prompts)
*   **00:45 - 01:30:** Bloque 2: El Laboratorio de Agentes (Construcción Práctica)
*   **01:30 - 01:45:** *Break de Networking (Café & Conexiones)*
*   **01:45 - 02:30:** Bloque 3: Automatización de Flujos (IA + Herramientas No-Code)
*   **02:30 - 02:50:** Demo Show & Pitch de Asistentes (Presentación de resultados)
*   **02:50 - 03:00:** Cierre, Roadmap y Recursos

---

## 2. Materiales Necesarios (Pre-Workshop)

**Para el Facilitador:**
*   Proyector y sonido de alta calidad.
*   Pizarra blanca y marcadores de colores.
*   Demo lista: Un asistente ya configurado en ChatGPT (GPTs) o Claude para mostrar el "antes y después".

**Para los Participantes (Enviar por email 48h antes):**
*   **Hardware:** Laptop con batería cargada (obligatorio).
*   **Software:** Cuenta activa en ChatGPT (Plus preferiblemente para usar GPTs) o Claude.ai.
*   **Pre-work:** Traer anotado 1 proceso repetitivo de su startup que odien hacer (ej: redactar emails de ventas, resumir reuniones, analizar feedback de clientes).

---

## 3. Estructura de Bloques

### Bloque 1: De la Idea al Prompt Maestro
*   **Duración:** 30 min
*   **Objetivo:** Entender que la IA no es un buscador (Google), sino un empleado inteligente al que hay que darle contexto.
*   **Dinámica:** *Charla interactiva + Ejercicio de "Prompting Inverso"*. Yo les doy un resultado mediocre y ellos deben adivinar qué instrucción falló.
*   **Key Takeaway:** El framework **R-C-I** (Rol, Contexto, Instrucción). Si no le das un rol, es un genérico; si le das un rol, es un experto.
*   **Slide Count:** 5-7 slides.

### Bloque 2: El Laboratorio de Agentes (EJERCICIO PRINCIPAL)
*   **Duración:** 45 min
*   **Objetivo:** Construir un "Custom GPT" o un "Project" en Claude que actúe como un miembro específico de su equipo.
*   **Dinámica:** *Hands-on Workshop*. Los emprendedores aplican el framework aprendido para configurar su asistente.
*   **Key Takeaway:** Un asistente útil no solo responde preguntas, tiene una **personalidad, un conocimiento base y un objetivo claro.**
*   **Slide Count:** 3 slides (instrucciones visuales paso a paso).

### Bloque 3: Automatización de Flujos (IA + No-Code)
*   **Duración:** 45 min
*   **Objetivo:** Ver cómo el asistente sale de la ventana del chat y entra en su flujo de trabajo real.
*   **Dinámica:** *Demo en vivo + Discusión de casos de uso*. Muestro cómo conectar la IA con Zapier o Make (ej: "Cuando llegue un email de cliente -> IA lo analiza -> Crea un ticket en Notion").
*   **Key Takeaway:** La IA por sí sola es un juguete; la IA conectada a tus herramientas es un empleado.
*   **Slide Count:** 6-8 slides (muchos diagramas de flujo).

---

## 4. El Ejercicio Principal: "Tu Primer Empleado Digital"

Este es el corazón del workshop. Cada participante debe salir con un asistente funcional.

**Pasos del ejercicio:**
1.  **Definición del Perfil:** El participante elige su proceso (ej: "Customer Success").
2.  **Configuración de Instrucciones (System Prompt):** Usando el framework R-C-I, redactan el "Manual de Operaciones" de su asistente.
    *   *Ejemplo:* "Eres el experto en Customer Success de [Nombre Startup]. Tu tono es empático pero resolutivo. Tu objetivo es clasificar los tickets de soporte en: Urgente, Consulta o Feedback."
3.  **Carga de Conocimiento (Knowledge):** Suben un PDF con su FAQ o su manual de marca para que la IA no alucine.
4.  **Test de Estrés:** El facilitador pasa por las mesas y les lanza un "reto" (ej: "Pídele que responda a un cliente muy enojado usando tu manual").

---

## 5. Recursos para llevar a casa (The "Startup AI Toolkit")

Entregarás un PDF (o Notion Page) con:
*   **Cheat Sheet de Prompts:** Una lista de 20 prompts listos para copiar y pegar para tareas de marketing, ventas y operaciones.
*   **Directorio de Herramientas:** Una lista curada de herramientas No-Code (Zapier, Make, Airtable) y de IA (Perplexity, Claude, Midjourney).
*   **Guía de "Cómo seguir":** Roadmap de aprendizaje para pasar de "usuario de chat" a "arquitecto de soluciones de IA".

---

## 6. Resumen de Slides Estimado

*   **Intro/Mindset:** 7 slides
*   **Bloque 1 (Prompting):** 7 slides
*   **Bloque 2 (Construcción):** 3 slides (guía visual)
*   **Bloque 3 (Automatización):** 8 slides
*   **Cierre/Q&A:** 5 slides
*   **TOTAL:** ~30 slides (Pocas palabras, muchas imágenes y diagramas).

---

**💡 Tip de Facilitador para Latam:**
En Latinoamérica, los emprendedores suelen ser muy prácticos y orientados a la optimización de costos. Durante todo el workshop, usa la narrativa de **"Cómo ahorrarte el sueldo de un asistente junior usando este bot"**. Eso hará que la atención se mantenga al 100%.