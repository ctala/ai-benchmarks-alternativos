# GPT-OSS 120B — startup_content/curso_emprendimiento_modulo

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.05 | quality: 9.76
- latency_total: 11.387s | tokens_per_second: 179.9
- input_tokens: 282 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una guía completa y práctica para emprendedores sobre la automatización con IA.

## Respuesta completa

# Módulo 3 – **Automatización con IA: De la idea al flujo de trabajo**  

---  

## 1️⃣ Objetivo del módulo  
Al finalizar este módulo, el emprendedor será capaz de diseñar, montar y probar un flujo de trabajo automatizado que aproveche la inteligencia artificial para resolver una necesidad real de su startup (atención al cliente, generación de contenidos o calificación de leads). No se requieren conocimientos de programación; basta con saber usar herramientas visuales como **n8n** y los servicios de IA en la nube.

---  

## 2️⃣ Contenido teórico  

| Tema | Qué aprenderás | Por qué es útil |
|------|----------------|----------------|
| **Qué es la automatización con IA** | - Diferencia entre automatización tradicional y automatización potenciada por IA.<br>- Conceptos clave: disparadores (triggers), acciones, APIs, “prompt engineering”. | Permite que tareas repetitivas se ejecuten sin intervención humana y, a la vez, añadan valor cognitivo (p.ej. análisis de texto). |
| **Arquitectura de un flujo de trabajo** | - Componentes básicos: *trigger* → *transformación* → *acción*.<br>- Cómo se conectan los servicios (CRM, redes sociales, email, bases de datos). | Visualizar el proceso ayuda a identificar cuellos de botella y puntos donde la IA aporta mayor impacto. |
| **Introducción a n8n** | - Qué es n8n (plataforma de automatización “low‑code”).<br>- Ventajas: auto‑hosting, comunidad, cientos de nodos preconstruidos, posibilidad de usar JavaScript opcionalmente.<br>- Cómo crear una cuenta/instancia (Docker, n8n.cloud, o la versión desktop). | n8n es la herramienta central del módulo; su interfaz visual permite armar flujos sin escribir código. |
| **Servicios de IA que se integran fácilmente** | - OpenAI (ChatGPT, embeddings).<br>- Cohere, Anthropic, Google Gemini.<br>- APIs de visión (OCR, reconocimiento de imágenes). | Estas APIs son “cajas negras” que convierten texto, imágenes o audio en datos procesables por n8n. |
| **Buenas prácticas** | - Diseñar flujos “fail‑safe”.<br>- Manejo de errores y reintentos.<br>- Protección de datos sensibles (encriptación, variables de entorno).<br>- Monitoreo y métricas básicas. | Evita que la automatización se rompa y garantiza cumplimiento de normativas (p.ej. GDPR, Ley de Protección de Datos de México). |

---  

## 3️⃣ 3 ejemplos prácticos de automatización para startups  

### 👉 3.1 Atención al cliente automatizada  

| Paso | Acción en n8n | IA involucrada |
|------|---------------|----------------|
| **Trigger** | Nuevo mensaje en WhatsApp Business (n8n → Twilio). | — |
| **Transformación** | Enviar el texto a **OpenAI Chat Completion** con un prompt que indique: “Responde como agente de soporte, mantén tono amigable, usa la base de conocimientos adjunta”. | GPT‑4 (o modelo equivalente). |
| **Acción** | Enviar la respuesta al cliente vía WhatsApp. | — |
| **Enriquecimiento** | Guardar el historial en Airtable + etiquetar el ticket con “sentiment” (análisis de sentimiento usando OpenAI). | GPT‑4 (sentiment). |
| **Valor** | Respuestas instantáneas 24/7, reducción de tickets manuales en un 40 %. | — |

---

### 👉 3.2 Generación de contenido para redes sociales  

| Paso | Acción en n8n | IA involucrada |
|------|---------------|----------------|
| **Trigger** | Cada lunes a las 09:00 (Cron). | — |
| **Transformación** | Llamar a **OpenAI** con prompt: “Escribe 5 ideas de posts para Instagram sobre tendencias en fintech para Latinoamérica, incluye copy de 150 caracteres y 3 hashtags”. | GPT‑4. |
| **Acción** | Guardar ideas en Google Sheet y publicar la primera en Buffer (programación automática). | — |
| **Enriquecimiento** | Usar **Stable Diffusion** (o DALL·E) para generar una imagen a partir del título del post. | Modelo de generación de imágenes. |
| **Valor** | Contenido fresco sin pasar horas brainstorming; aumenta engagement y consistencia. | — |

---

### 👉 3.3 Calificación automática de leads  

| Paso | Acción en n8n | IA involucrada |
|------|---------------|----------------|
| **Trigger** | Nuevo lead en HubSpot (Webhook). | — |
| **Transformación** | Extraer datos del lead y crear un **embedding** con OpenAI (text‑embedding‑ada‑002). | Modelo de embeddings. |
| **Acción** | Comparar embedding con un “perfil ideal de cliente” almacenado en Pinecone (vector DB). |
| **Decisión** | Si la similitud > 0.85 → mover lead a “Qualified” y enviar email de bienvenida; si no, etiquetar como “Nurturing”. |
| **Valor** | Prioriza ventas, reduce tiempo de filtrado manual en un 70 %. | — |

---  

## 4️⃣ Ejercicio práctico paso a paso  
> **Objetivo:** Crear un flujo en n8n que reciba preguntas de clientes por WhatsApp y responda automáticamente usando GPT‑4.  

### 📋 Requisitos previos  
1. Cuenta en **n8n.cloud** (o Docker/desktop).  
2. Cuenta de **Twilio** (WhatsApp Sandbox) – [Guía rápida de Twilio](https://www.twilio.com/docs/whatsapp/quickstart).  
3. API Key de **OpenAI** (plan gratuito o de pago).  

### 🛠️ Paso a paso  

| Paso | Acción | Detalles |
|------|--------|----------|
| 1️⃣ | **Crear un nuevo workflow** | En n8n → “New Workflow”, ponle nombre: `WhatsApp IA Support`. |
| 2️⃣ | **Añadir Trigger** | Arrastra el nodo **Twilio Trigger**.<br>Configura: <br>• `Account SID` y `Auth Token` (de Twilio).<br>• `Webhooks URL` → n8n genera una URL; copia y pega en la consola de Twilio > *Messaging > Settings > Request URL*. |
| 3️⃣ | **Obtener el mensaje** | El nodo entregará `body` (texto del cliente). Añade un **Set** node para renombrar a `question`. |
| 4️⃣ | **Llamar a OpenAI** | Arrastra **HTTP Request** node.<br>Configura: <br>• **Method:** POST <br>• **URL:** `https://api.openai.com/v1/chat/completions` <br>• **Headers:** `Authorization: Bearer <TU_API_KEY>` <br>• **Body (JSON):** <br>```json\n{\n  "model": "gpt-4o-mini",\n  "messages": [{\"role\": \"system\", \"content\": \"Eres un agente de soporte amigable y respondes en español latinoamericano. Usa respuestas breves y claras.\"},\n               {\"role\": \"user\", \"content\": \"{{ $json.question }}\"}]\n}\n``` |
| 5️⃣ | **Parsear respuesta** | Añade un **Set** node → crea campo `answer` con expresión `{{ $json.choices[0].message.content }}`. |
| 6️⃣ | **Responder al cliente** | Arrastra **Twilio Node** (Send Message). <br>Configura: <br>• `From`: número de sandbox de WhatsApp (p.ej. `whatsapp:+14155238886`). <br>• `To`: `{{ $json.from }}` (viene del trigger). <br>• `Body`: `{{ $json.answer }}`. |
| 7️⃣ | **Guardar historial (opcional)** | Añade un nodo **Google Sheets** → crea fila con `question`, `answer`, `timestamp`. |
| 8️⃣ | **Activar el workflow** | Haz click en **Activate** (esquina superior derecha). |
| 9️⃣ | **Probar** | Envía un mensaje al número de WhatsApp sandbox desde tu móvil. Deberías recibir una respuesta generada por IA en segundos. |
| 🔟 | **Iterar** | Ajusta el *prompt* en el nodo HTTP para mejorar tono, incluir FAQ, etc. Observa los logs en n8n → **Execution List**. |

> **Tip:** Si el mensaje contiene datos sensibles (p.ej. número de tarjeta), agrega un nodo **IF** que detecte palabras clave y redirija a un agente humano (Webhook a Slack).  

---  

## 5️⃣ Recursos adicionales  

| Tipo | Enlace | Comentario |
|