# Gemma 4 12B (Spark llama-server, reasoning) — startup_content/curso_emprendimiento_modulo

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.96 | quality: 9.44
- latency_total: 88.829s | tokens_per_second: 25.5
- input_tokens: 236 | output_tokens: 2269
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes la estructura del Módulo 3, diseñada bajo un enfoque de **"Aprender haciendo" (Learning by doing)**, pensando específicamente en emprendedores que necesitan resultados rápidos sin complicaciones técnicas excesivas.

---

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del módulo
Al finalizar este módulo, serás capaz de identificar tareas repetitivas en tu negocio y transformarlas en flujos de trabajo automatizados utilizando inteligencia artificial. Aprenderás a conectar diferentes herramientas para que "trabajen por ti" en segundo plano, permitiéndote escalar tu operación, reducir errores humanos y dedicar más tiempo a la estrategia y al crecimiento de tu emprendimiento.

---

## 2. Contenido Teórico: El "Cerebro" de tu Negocio

### ¿Qué es la Automatización con IA?
Tradicionalmente, la automatización consistía en reglas fijas: *"Si pasa A, haz B"*. Por ejemplo: *"Si recibo un correo, enviarlo a la carpeta de ventas"*. 

La **Automatización con IA** añade una capa de razonamiento. Ahora la regla es: *"Si recibo un correo, **analízalo con IA** para entender la intención del cliente y, dependiendo de si es una queja, una duda o una compra, decide si responder automáticamente, enviarlo a un humano o agendar una cita"*.

### Herramientas Clave: El ecosistema No-Code
Para construir estos flujos sin saber programar, utilizamos herramientas de "orquestación":

*   **n8n:** Es como un tablero de piezas de LEGO. Te permite conectar aplicaciones (Google Sheets, WhatsApp, Instagram, Gmail) y poner "nodos" de IA en medio. Es extremadamente potente y permite crear flujos complejos de forma visual.
*   **Zapier / Make:** Son los competidores más conocidos. Aunque n8n ofrece mayor flexibilidad técnica, estas herramientas son excelentes para automatizaciones sencillas y rápidas.
*   **Modelos de Lenguaje (LLMs):** Aquí es donde entra la IA (como GPT-4 o Claude). Estos actúan como el "empleado inteligente" dentro de tu flujo de trabajo que lee, resume, escribe y clasifica la información.

---

## 3. Ejemplos Prácticos para Startups

### A. Atención al Cliente Automatizada
*   **El Problema:** Recibes decenas de mensajes por DM o WhatsApp preguntando precios y horarios, y tardas horas en responder.
*   **El Flujo:** Un cliente escribe por WhatsApp $\rightarrow$ n8n recibe el mensaje $\rightarrow$ La IA analiza la pregunta $\rightarrow$ Si es sobre precios, la IA responde con el catálogo $\rightarrow$ Si es una queja compleja, la IA envía una alerta urgente a tu celular para que tú intervengas.

### B. Generación de Contenido para Redes Sociales
*   **El Problema:** Te falta tiempo para crear contenido constante en 3 plataformas distintas.
*   **El Flujo:** Subes un video largo a una carpeta de Google Drive $\rightarrow$ La IA extrae los puntos clave $\rightarrow$ La IA redacta 3 posts para Instagram, 1 hilo para X (Twitter) y un guion para TikTok $\rightarrow$ Las herramientas de programación (como Buffer) publican automáticamente.

### C. Calificación Automática de Leads (Prospectos)
*   **El Problema:** Recibes muchos formularios de contacto, pero no sabes cuáles son los clientes con mayor potencial de compra.
*   **El Flujo:** Alguien llena un formulario en tu web $\rightarrow$ n8n envía los datos a la IA $\rightarrow$ La IA califica al cliente del 1 al 10 basándose en su presupuesto y necesidad $\rightarrow$ Si es un "10", se crea automáticamente una tarea en tu calendario para llamarlo hoy mismo.

---

## 4. Ejercicio Práctico: Crea tu primer "Filtro de Leads"

En este ejercicio, diseñaremos la lógica de un flujo para calificar prospectos automáticamente. No necesitas configurar todo el software hoy, pero debes diseñar el **mapa de flujo**.

**Instrucciones:**

1.  **Identifica el disparador (Trigger):** ¿Por dónde llegan tus clientes? (Ejemplo: Formulario de Google, mensaje de Instagram, correo).
2.  **Define los criterios de calificación:** Escribe 3 puntos que definen a un "cliente ideal". (Ejemplo: 1. Tiene presupuesto de +$500, 2. Necesita el servicio en menos de 30 días, 3. Es una empresa de más de 5 empleados).
3.  **Diseña el "Prompt" de la IA:** Escribe la instrucción que le darías a la IA para que analice al cliente.
    *   *Ejemplo:* "Actúa como un experto en ventas. Analiza el siguiente texto de un cliente: [Datos del formulario]. Basado en mis criterios (presupuesto, tiempo, tamaño de empresa), asígnale una puntuación de 1 a 10 y dime brevemente por qué."
4.  **Define la acción final:** ¿Qué debe pasar si el cliente es un "10"? (Ejemplo: Enviarle un correo de agradecimiento y enviarme una notificación por Telegram).

**Entregable:** Dibuja en una hoja o usa una herramienta como *Miro* o *Canva* un diagrama de flujo simple que conecte estos 4 pasos.

---

## 5. Recursos Adicionales

*   **Guía de n8n para Principiantes:** [Enlace a documentación o video tutorial sugerido]
*   **Plantilla de Prompts para Calificación de Leads:** (Documento PDF descargable con 5 variaciones de prompts).
*   **Comunidad de Automatización:** Enlace a grupo de Telegram/Discord para compartir flujos de trabajo.

---

## 6. Preguntas de Autoevaluación

1.  ¿Cuál es la diferencia principal entre una automatización tradicional y una automatización con IA?
2.  Si tienes un proceso que te quita más de 2 horas al día y es repetitivo, ¿cuáles serían los 3 pasos básicos para empezar a automatizarlo?
3.  En el ejemplo de "Calificación de Leads", ¿por qué es importante que la IA tenga criterios claros antes de asignar una puntuación?