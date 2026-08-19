# GLM 5 — startup_content/workshop_outline

- model_id: `z-ai/glm-5`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 56.083s | tokens_per_second: 61.5
- input_tokens: 195 | output_tokens: 3447
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una agenda detallada y materiales necesarios, con un enfoque práctico y útil para emprendedores no técnicos.

## Respuesta completa

¡Hola! Qué excelente iniciativa. Como facilitador que ha trabajado con emprendedores en la región, sé que la clave aquí es **desmitificar la tecnología** y enfocarse en el valor de negocio, no en el código. Los emprendedores latimos somos pragmáticos: queremos herramientas que nos ahorren tiempo y dinero "ya".

Aquí tienes el outline diseñado para ser dinámico, interactivo y con resultados tangibles.

---

# Workshop: "Construye tu Asistente de IA para tu Startup"
**Formato:** Presencial | **Duración:** 3 horas | **Audiencia:** 20-30 emprendedores early-stage (no-tecnicos)

---

## 1. Agenda Detallada (180 minutos)

| Hora | Bloque | Actividad Principal |
| :--- | :--- | :--- |
| **00:00 - 00:20** | **Bienvenida & Mindset** | Rompehielo, expectativas y la promesa del taller. |
| **00:20 - 00:50** | **Bloque 1: El Cerebro de tu Startup** | Charla relámpago: Casos de uso reales en LatAm. |
| **00:50 - 01:35** | **Bloque 2: El Arte del Prompting** | Ejercicio guiado: De novato a experto en instrucciones. |
| **01:35 - 01:45** | **Break Energético** | Networking y café (vital para la energía). |
| **01:45 - 02:45** | **Bloque 3: Manos a la Obra** | Ejercicio Principal: Creación del Asistente. |
| **02:45 - 03:00** | **Cierre & Kit de Salida** | Demo de resultados, Q&A y recursos. |

---

## 2. Materiales Necesarios (Preparación)

**Para el Facilitador:**
*   Proyector y audio decente (para demos en vivo).
*   Conexión WiFi de respaldo (siempre falla en el momento crítico).
*   Cuenta Plus de ChatGPT (o similar) para demos en pantalla.
*   Presentación en Google Slides/PowerPoint (visual, poco texto).

**Para los Participantes:**
*   **Laptop o Smartphone obligatorio** (idealmente laptop).
*   Acceso a una cuenta gratuita de ChatGPT o Claude (enviar recordatorio previo).
*   **"Canvas del Asistente" (Físico):** Una hoja tamaño carta con una estructura vacía para rellenar (Rol, Contexto, Tarea, Formato). Imprimir 30 copias.
*   Post-its y marcadores.

---

## 3. Detalle por Bloque

### Bloque 1: El Cerebro de tu Startup (30 min)
**Título:** "IA no te quitará el trabajo, un emprendedor que usa IA sí"

*   **Objetivo:** Cambiar la mentalidad de "la IA es complicada" a "la IA es mi becario digital".
*   **Dinámica:**
    *   **Charla (10 min):** Explicar qué es un LLM (Modelo de Lenguaje Grande) con analogía simple: "Es como tener un becario superdotado que leyó toda internet, pero que necesita instrucciones claras".
    *   **Discusión (15 min):** "Dolor vs. Solución". Preguntar a la audiencia: "¿Qué tarea repetitiva odian hacer?" (Ej: Responder emails, hacer posts para Instagram, analizar competencia). Escribir los dolores en la pizarra.
    *   **Demo (5 min):** Mostrar 3 ejemplos rápidos de valor:
        1.  Generar un borrador de email frío para ventas.
        2.  Resumir un texto legal complicado.
        3.  Crear una tabla de contenido para un plan de negocios.
*   **Key Takeaway:** La IA es un amplificador de tu tiempo. No es magia, es conversación.

### Bloque 2: El Arte del Prompting (45 min)
**Título:** "Aprende a pedir para que te den"

*   **Objetivo:** Que los participantes entiendan que la calidad de la respuesta depende de la calidad de la instrucción (Prompt).
*   **Dinámica:**
    *   **Charla Visual (10 min):** Presentar la fórmula mágica: **R + C + T + F** (Rol + Contexto + Tarea + Formato).
    *   **Ejercicio "Antes y Después" (20 min):**
        *   Pedirles que escriban un prompt malo: "Ayúdame con mi marketing".
        *   Ver el resultado mediocre.
        *   Aplicar la fórmula: "Actúa como un experto en marketing digital para startups Fintech en Colombia [Rol]. Mi público son millennials sin ahorros [Contexto]. Crea 3 ideas de posts para Instagram [Tarea]. Usa un tono divertido y emojis [Formato]".
        *   Comparar resultados.
    *   **Discusión (15 min):** ¿Qué pasó? ¿Por qué la segunda respuesta fue mejor?
*   **Key Takeaway:** No le hables a la máquina como a Google. Háblale como a un pasante nuevo que necesita contexto.

### Bloque 3: Manos a la Obra (60 min) - *El Núcleo*
**Título:** "Tu Primer Empleado Digital"

*   **Objetivo:** Diseñar y probar un "Asistente" específico para una necesidad real de su startup.
*   **Dinámica (Ejercicio Principal - Ver punto 4):**
    *   Trabajo individual guiado usando el "Canvas del Asistente".
    *   El facilitador recorre la sala ayudando ("debugging") prompts.
*   **Key Takeaway:** Tienen un prototipo funcional de un asistente que pueden usar el lunes por la mañana.

### Cierre (15 min)
**Título:** "El lunes empieza la aventura"

*   **Objetivo:** Consolidar el aprendizaje y dar siguiente pasos.
*   **Dinámica:**
    *   **Demo relámpago (10 min):** Pedir a 3 voluntarios que compartan su pantalla y muestren su asistente en acción (solo 2 min cada uno). Celebrar los éxitos.
    *   **Q&A (5 min):** Preguntas rápidas.
*   **Key Takeaway:** La perfección es enemiga de la ejecución. Empiecen hoy.

---

## 4. Ejercicio Principal del Workshop: "El Canvas del Asistente"

Este ejercicio se hace durante el Bloque 3. Es la parte práctica donde ocurre la "magia".

**Paso 1: Definir el Dolor (Papel y Lápiz - 10 min)**
Cada emprendedor toma su hoja "Canvas del Asistente". Debe elegir **UNA** tarea específica que le quita tiempo.
*   *Ejemplos:* "Responder quejas de clientes", "Crear titulares para LinkedIn", "Resumir reuniones".

**Paso 2: Diseñar el Prompt Maestro (Lápiz - 15 min)**
En la hoja, rellenan las 4 casillas:
1.  **ROL:** "Eres un experto en..."
2.  **CONTEXTO:** "Mi startup vende X, mi cliente es Y, mi tono es Z..."
3.  **TAREA:** "Tu trabajo es crear/resumir/escribir..."
4.  **LIMITES:** "No uses jerga técnica, sé breve, usa bullets".

**Paso 3: Entrenamiento en Vivo (Laptop - 25 min)**
*   Abren ChatGPT/Claude.
*   Copian su "Prompt Maestro".
*   **Iteración:** La IA responderá. El emprendedor debe corregirla: "Muy largo", "Muy formal", "No entendió el producto".
*   **Guardado:** Guardan el chat con un nombre específico (ej: "Mi Asistente de Ventas") para seguir usándolo después.

**Paso 4: Intercambio (10 min)**
Se turnan con el compañero de al lado para probar el asistente del otro (validación cruzada).

---

## 5. Recursos para llevar a casa (Takeaways)

Al salir, los participantes reciben un enlace (QR code o email) con:

1.  **PDF "La Biblia del Prompting para Startups":** Resumen de la fórmula R+C+T+F y 10 plantillas pre-hechas (Email de ventas, Análisis de competencia, Descripción de producto).
2.  **Canvas del Asistente (PDF descargable):** Para que puedan replicar el ejercicio con su equipo.
3.  **Lista de Herramientas Gratuitas:** Una lista curada de herramientas IA gratuit/freemium útiles para emprendedores (ChatGPT, Claude, Canva Magic, Gamma para presentaciones).
4.  **Checklist de Implementación:** 3 pasos para integrar la IA en su semana laboral.

---

## 6. Slide Count Estimado

*El diseño debe ser limpio, muchas imágenes, poco texto.*

*   **Intro (5 slides):** Título, Facilitador, Agenda, Reglas del juego (preguntar es gratis), Rompehielo.
*   **Bloque 1 (8 slides):** ¿Qué es IA? (analogía), Casos de uso LatAm (fotos reales), El miedo vs la realidad, Demo rápida.
*   **Bloque 2 (10 slides):** La fórmula mágica (R+C+T+F), Ejemplo malo vs bueno (comparativa visual), Errores comunes, Tips de "trucos" (dar ejemplos a la IA).
*   **Bloque 3 (5 slides):** Instrucciones del ejercicio, Timer en pantalla, Preguntas guía.
*   **Cierre (5 slides):** Recursos, Comunidad, Agradecimiento, Contacto.
*   **Total:** ~33 slides.

---

**Nota para el facilitador:** Mantén la energía alta. Si alguien dice "no me salió", valida su esfuerzo y ayúdale a ajustar una palabra. El objetivo es que se vayan sintiendo que tienen el control de la herramienta, no al revés.