# Gemma 4 31B (Spark llama-server Q4_K_M) — startup_content/workshop_outline

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 7.52 | quality: 9.2
- latency_total: 180.291s | tokens_per_second: 9.7
- input_tokens: 206 | output_tokens: 1743
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Hola! Como facilitador, sé que con emprendedores no-técnicos el mayor enemigo es la **parálisis por análisis** y el miedo a la "caja negra" de la tecnología. 

El objetivo de este workshop no es enseñarles a programar, sino a **diseñar flujos de valor**. Vamos a pasar de la teoría a la implementación en tiempo récord utilizando herramientas *No-Code*.

Aquí tienes el blueprint completo.

---

# 🚀 Workshop: Construye tu Asistente de IA para tu Startup
**Enfoque:** *Practical, No-Code, Value-Driven.*

## 1. Agenda Detallada (180 Minutos)

| Tiempo | Bloque | Actividad | Formato |
| :--- | :--- | :--- | :--- |
| **00:00 - 00:20** | **El Mindset de la IA** | De "Chatbot" a "Empleado Digital" | Charla Energética |
| **00:20 - 00:50** | **Diseño de Prompting** | El Arte de dar Instrucciones | Demo + Ejercicio |
| **00:50 - 01:20** | **Arquitectura de Conocimiento** | Alimentando a tu IA (RAG simplificado) | Ejercicio Práctico |
| **01:20 - 01:30** | **Break Energético** | Networking rápido | Receso |
| **01:30 - 02:30** | **Build Time: El MVP** | Construcción del Asistente | Hands-on (Laboratorio) |
| **02:30 - 02:50** | **Demo Day & Feedback** | Presentación de prototipos | Pitch rápido |
| **02:50 - 03:00** | **Roadmap & Cierre** | Siguientes pasos y recursos | Cierre |

---

## 2. Materiales Necesarios

### Para el Facilitador:
- Proyector y audio.
- Conexión a internet estable (indispensable).
- Cuenta Pro de OpenAI (para mostrar GPTs) o Poe.com.
- Timer visual en pantalla.

### Para los Emprendedores (Enviar por email 3 días antes):
- **Hardware:** Laptop (no tablets ni celulares).
- **Cuentas creadas:** OpenAI (ChatGPT Plus preferiblemente) o una cuenta en **MindStudio** o **Chatbase** (herramientas No-Code ideales para startups).
- **Activo de negocio:** Un documento PDF o link a su web con la información de su producto/servicio (para usar como base de conocimientos).

---

## 3. Desglose de Bloques

### Bloque 1: El Mindset de la IA (20 min)
*   **Objetivo:** Cambiar la percepción de la IA como un buscador a una herramienta de ejecución.
*   **Dinámica:** Charla corta con ejemplos reales de startups que automatizan soporte, ventas o onboarding.
*   **Key Takeaway:** "La IA no reemplaza al emprendedor, sino que le da un equipo de 10 personas virtuales".
*   **Slides:** 4-5 slides (Visuales, muchos logos y ejemplos).

### Bloque 2: Diseño de Prompting (30 min)
*   **Objetivo:** Dominar la estructura de un prompt profesional (Rol $\rightarrow$ Contexto $\rightarrow$ Tarea $\rightarrow$ Formato).
*   **Dinámica:** *Live Editing*. Tomamos un prompt malo ("Hazme un plan de ventas") y lo transformamos en uno experto en vivo.
*   **Key Takeaway:** La calidad del output depende de la especificidad del input.
*   **Slides:** 6-8 slides (Plantillas de "Copy-Paste").

### Bloque 3: Arquitectura de Conocimiento (30 min)
*   **Objetivo:** Entender que la IA es inteligente, pero no conoce el negocio del alumno.
*   **Dinámica:** Ejercicio de "Curaduría de Datos". Identificar qué documentos (FAQ, Manual de Marca, Precios) necesita su asistente para no alucinar.
*   **Key Takeaway:** Tu ventaja competitiva no es la IA, sino tus datos propios.
*   **Slides:** 5 slides (Diagrama simple de flujo de datos).

### Bloque 4: Build Time - El MVP (60 min) 🛠️
*   **Objetivo:** Salir con un asistente funcional y desplegado.
*   **Dinámica:** Laboratorio guiado. El facilitador marca los pasos en pantalla y los alumnos ejecutan en sus laptops.
*   **Key Takeaway:** "Hecho es mejor que perfecto". El asistente debe resolver UN solo problema específico.
*   **Slides:** 3 slides (Checklist de pasos).

### Bloque 5: Demo Day & Feedback (20 min)
*   **Objetivo:** Validar la utilidad del asistente con pares.
*   **Dinámica:** 3-4 voluntarios presentan su asistente. El resto hace una pregunta "difícil" para probar la robustez de la IA.
*   **Key Takeaway:** Iterar basándose en el uso real.
*   **Slides:** 1 slide (Cronómetro).

### Bloque 6: Roadmap & Cierre (10 min)
*   **Objetivo:** Dar claridad sobre cómo escalar esto.
*   **Dinámica:** Charla de cierre y entrega de recursos digitales.
*   **Key Takeaway:** La IA evoluciona semanalmente; la curiosidad es la habilidad más importante.
*   **Slides:** 2 slides (Links y contacto).

---

## 4. Ejercicio Principal: "El Empleado Digital"

El ejercicio central consiste en crear un **Asistente Especializado** utilizando una herramienta No-Code (ej. GPTs de OpenAI o Chatbase).

**El reto:** Construir un asistente que cumpla una de estas tres funciones:
1.  **SDR Virtual:** Califica leads y agenda citas basándose en el pitch de la startup.
2.  **Customer Success Bot:** Resuelve dudas técnicas usando el manual de usuario del producto.
3.  **Strategist de Contenido:** Crea posts para LinkedIn siguiendo la voz de marca del fundador.

**Pasos del ejercicio:**
1.  **Definir el Rol:** "Eres el Director de Ventas de [Startup X]..."
2.  **Cargar Conocimiento:** Subir el PDF de precios o la web de la empresa.
3.  **Configurar Guardrails:** "Si el cliente pregunta por X, no respondas, dirígelo a este email".
4.  **Testeo:** Probar el bot con el compañero de al lado.

---

## 5. Recursos para llevar a casa (The Toolkit)

Entregar un PDF o Notion Page con:
- **Prompt Library:** 10 plantillas de prompts para crecimiento (Growth), Operaciones y Ventas.
- **Stack Sugerido:** Lista de herramientas (OpenAI, Make.com, Zapier, Perplexity, Anthropic).
- **Guía de Curaduría:** Checklist de qué documentos preparar para entrenar IAs.
- **Comunidad:** Acceso a un grupo de WhatsApp/Slack para seguimiento.

---

## 6. Resumen de Slides Estimado

| Sección | Slides | Enfoque |
| :--- | :---: | :--- |
| Mindset | 5 | Inspiracional / Visual |
| Prompting | 8 | Educativo / Práctico |
| Conocimiento | 5 | Técnico Simple / Diagramas |
| Build Time | 3 | Guía paso a paso |
| Demo Day | 1 | Dinámico |
| Cierre | 2 | Acción inmediata |
| **Total** | **24** | **Ritmo rápido** |