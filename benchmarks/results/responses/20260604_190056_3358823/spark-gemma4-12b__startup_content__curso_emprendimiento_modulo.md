# Gemma 4 12B (Spark llama-server Q4_K_M) — startup_content/curso_emprendimiento_modulo

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.96 | quality: 9.44
- latency_total: 94.384s | tokens_per_second: 24.8
- input_tokens: 236 | output_tokens: 2342
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes el diseño del **Módulo 3** diseñado específicamente para emprendedores que buscan eficiencia operativa sin necesidad de saber programar.

---

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del módulo
Al finalizar este módulo, el emprendedor será capaz de identificar procesos repetitivos en su modelo de negocio y diseñar flujos de trabajo automatizados que integren Inteligencia Artificial. El objetivo es que el alumno pase de "usar ChatGPT manualmente" a crear sistemas que trabajen por él las 24 horas, permitiéndole escalar su operación sin aumentar proporcionalmente sus costos operativos o su carga de trabajo manual.

---

## 2. Contenido Teórico

### ¿Qué es la automatización con IA?
Tradicionalmente, la automatización consistía en reglas rígidas (Ejemplo: *"Si recibo un correo con la palabra 'Factura', muévelo a la carpeta X"*). La **Automatización con IA** añade una capa de "juicio" o "razonamiento". Ahora, el sistema puede entender el contexto (Ejemplo: *"Lee este correo, entiende si el cliente está enojado o feliz, resume su problema y redacta una respuesta personalizada en tono amable"*).

### El concepto de "Trigger" y "Action"
Para automatizar, debemos pensar en términos de disparadores:
*   **Trigger (Disparador):** El evento que inicia todo (ej. un cliente llena un formulario, llega un mensaje de WhatsApp, se publica un video en YouTube).
*   **Action (Acción):** Lo que sucede después (ej. enviar un email, guardar datos en un Excel, generar una imagen, enviar una alerta a Slack).

### Herramientas Clave: El "Pegamento" de tu negocio
Para conectar diferentes aplicaciones (como Google Sheets, WhatsApp, Instagram y OpenAI), necesitamos plataformas de integración.
*   **n8n:** Es nuestra herramienta estrella. A diferencia de Zapier (que puede volverse muy caro rápidamente), n8n es una herramienta de automatización basada en nodos (visual). Permite crear flujos complejos conectando "bloques" de diferentes servicios. Es ideal para emprendedores porque permite ver el mapa de cómo viaja la información desde que entra hasta que se procesa con la IA.

---

## 3. Ejemplos Prácticos para Startups

### A. Atención al cliente automatizada (Triaje de tickets)
*   **Flujo:** El cliente escribe por WhatsApp $\rightarrow$ n8n recibe el mensaje $\rightarrow$ La IA analiza el sentimiento y la urgencia $\rightarrow$ Si es una queja urgente, envía una alerta inmediata al celular del dueño; si es una duda común, la IA responde automáticamente con información de precios y horarios.
*   **Beneficio:** Respuesta instantánea y priorización de problemas críticos.

### B. Generación de contenido para redes sociales (Repurposing)
*   **Flujo:** Subes un video largo a una carpeta de Google Drive $\rightarrow$ n8n detecta el archivo $\rightarrow$ La IA extrae los puntos clave $\rightarrow$ La IA redacta 3 posts para Instagram, 1 hilo para X (Twitter) y un guion para un Reel $\rightarrow$ Se guardan automáticamente en un documento de "Planificación de Contenidos".
*   **Beneficio:** Creas contenido para toda la semana en menos de 5 minutos.

### C. Calificación automática de leads (Lead Scoring)
*   **Flujo:** Un prospecto llena un formulario en tu web $\rightarrow$ n8n envía los datos a la IA $\rightarrow$ La IA evalúa el presupuesto y la necesidad del cliente (del 1 al 10) $\rightarrow$ Si la puntuación es > 8, se agenda automáticamente una cita en tu calendario; si es menor, se le envía un correo con contenido educativo.
*   **Beneficio:** Solo pierdes tiempo hablando con clientes que realmente pueden comprarte.

---

## 4. Ejercicio Práctico: "Tu primer flujo de calificación de Leads"

En este ejercicio, vas a construir la estructura de un flujo que califica prospectos automáticamente. *Nota: No necesitas configurar todo el código, sino diseñar la lógica en el lienzo.*

**Escenario:** Tienes una consultoría y quieres filtrar a quienes tienen presupuesto antes de agendar una reunión.

**Paso a paso:**
1.  **Identifica el Trigger:** Elige una herramienta de formulario (Google Forms, Typeform o Tally). Define que el disparador será "Nuevo envío de formulario".
2.  **Define la entrada de datos:** El formulario debe preguntar: *¿Cuál es tu presupuesto estimado?* y *¿Cuál es tu principal problema hoy?*
3.  **Diseña el "Prompt" de IA:** En tu flujo de n8n (o la herramienta que elijas), prepara la instrucción para la IA:
    > *"Actúa como un experto en ventas. Analiza las respuestas del cliente. Si el presupuesto es mayor a $1000 USD y el problema es urgente, califícalo como 'Prioridad Alta'. Si es menor, califícalo como 'Seguimiento'. Responde solo con una palabra: ALTA, MEDIA o BAJA."*
4.  **Define la Acción Final:**
    *   Si la respuesta es **ALTA**: Enviar un mensaje automático por Slack o Email diciendo: "¡Nuevo cliente caliente! Agenda la llamada".
    *   Si la respuesta es **BAJA**: Enviar un correo automático con un PDF de "Guía gratuita".
5.  **Tarea para el alumno:** Dibuja en una hoja de papel o en una herramienta de pizarra (como Miro) el mapa de este flujo: *Formulario $\rightarrow$ IA $\rightarrow$ Condición (Si/No) $\rightarrow$ Acción.*

---

## 5. Recursos Adicionales
*   **n8n.io:** Tutoriales básicos de "Cómo crear tu primer workflow".
*   **OpenAI API Documentation:** Para entender cómo enviar datos a GPT-4.
*   **PlantUML / Miro:** Herramientas recomendadas para diagramar tus flujos antes de construirlos.
*   **Plantilla de Prompts:** "Guía de prompts para clasificación de datos" (Entregable del curso).

---

## 6. Preguntas de Autoevaluación
1.  ¿Cuál es la diferencia principal entre una automatización tradicional y una automatización con IA?
2.  En un flujo de trabajo, ¿qué función cumple el "Trigger" y por qué es importante identificarlo claramente?
3.  Si tuvieras que automatizar la respuesta a correos de clientes, ¿cuáles serían los 3 pasos (nodos) principales que debería tener tu flujo en n8n?