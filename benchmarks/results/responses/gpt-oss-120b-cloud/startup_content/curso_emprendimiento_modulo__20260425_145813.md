# GPT-OSS 120B (Ollama Cloud) — startup_content/curso_emprendimiento_modulo

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 8.07 | quality: 9.48
- latency_total: 26.305s | tokens_per_second: 77.9
- input_tokens: 283 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Módulo 3 – **Automatización con IA: De la idea al flujo de trabajo**  

---

## 1️⃣ Objetivo del módulo  

Al finalizar este módulo, el emprendedor será capaz de diseñar, crear y lanzar su primer flujo de trabajo automatizado que combine inteligencia artificial y herramientas sin código (p. ej. **n8n**). Podrá identificar oportunidades de automatización dentro de su negocio, construir la lógica del proceso y obtener resultados inmediatos que ahorren tiempo, reduzcan costos y mejoren la experiencia del cliente.

---

## 2️⃣ Contenido teórico  

| Tema | Qué aprenderás | Por qué es útil |
|------|----------------|----------------|
| **¿Qué es la automatización con IA?** | Conceptos básicos: triggers, acciones, datos de entrada/salida, API y modelos de IA (LLM, visión, clasificación). | Entender la arquitectura mental para traducir una idea de negocio a un flujo ejecutable. |
| **Ventajas para startups** | Escalabilidad, rapidez de iteración, reducción de tareas repetitivas, mejora de la calidad de datos. | Justifica la inversión de tiempo y recursos en automatizar procesos críticos. |
| **Plataformas sin código** | Introducción a **n8n**, Zapier, Make (Integromat). Enfoque en n8n porque: <br>• Código abierto y auto‑alojado (más control y bajo costo). <br>• Gran catálogo de nodos (HTTP, GPT‑3/4, Google Sheets, Twilio, etc.). | Permite crear flujos complejos sin saber programar, pero con la flexibilidad de añadir scripts cuando sea necesario. |
| **Componentes clave de n8n** | - **Triggers** (ej.: webhook, cron, email). <br>- **Nodos de IA** (OpenAI, Hugging Face, Replicate). <br>- **Nodos de integración** (Slack, Gmail, Airtable, Facebook). <br>- **Control de flujo** (IF, Switch, SplitInBatches). | Saber qué bloque usar para cada paso del proceso. |
| **Buenas prácticas** | • Diseña con “mínimo viable” (MVP) → prueba rápido. <br>• Usa logs y pruebas unitarias dentro de n8n. <br>• Maneja errores (Retry, Catch). <br>• Protege credenciales (variables de entorno, secret manager). | Evita cuellos de botella y garantiza que la automatización sea fiable y segura. |

---

## 3️⃣ 3 ejemplos prácticos de automatización para startups  

### 3.1 Atención al cliente automatizada  
1. **Trigger:** Webhook que recibe un mensaje de Facebook Messenger o WhatsApp.  
2. **IA:** Nodo **OpenAI → GPT‑4** que genera una respuesta basada en la base de conocimiento (FAQ en Google Docs).  
3. **Acción:** Envía la respuesta al cliente vía Twilio/WhatsApp o Facebook.  
4. **Registro:** Guarda la conversación y el sentimiento (análisis de tono) en Airtable para métricas de CX.

### 3.2 Generación de contenido para redes sociales  
1. **Trigger:** Cron (todos los lunes a las 09:00).  
2. **IA:** Prompt a **ChatGPT** que produce 3 ideas de posts + copy corto, y a **DALL·E** que crea una imagen de portada.  
3. **Acción:** Publica automáticamente en Buffer o directamente en Instagram/Facebook usando sus APIs.  
4. **Métricas:** Al final del día, recopila likes, comentarios y alcance en Google Sheets.

### 3.3 Calificación automática de leads  
1. **Trigger:** Nuevo registro en **Typeform** (formulario de captura).  
2. **IA:** **OpenAI** analiza respuestas libres (ej.: “¿Cuál es tu mayor reto?”) y devuelve una puntuación de 0‑100.  
3. **Acción:** Si la puntuación > 70, crea un contacto en **HubSpot** y envía un email de bienvenida con oferta personalizada; si no, lo guarda en una lista “Nurturing”.  
4. **Dashboard:** Visualiza la distribución de scores en un reporte de **Metabase**.

---

## 4️⃣ Ejercicio práctico paso a paso  

> **Objetivo:** Construir un flujo en n8n que reciba un mensaje de WhatsApp, lo procese con GPT‑4 y responda automáticamente.  

### ✅ Requisitos previos  
| Herramienta | ¿Cómo obtenerla? |
|-------------|------------------|
| **n8n** (auto‑alojado o cloud) | Regístrate en <https://app.n8n.io> (plan gratuito) o instala Docker: `docker run -d -p 5678:5678 n8nio/n8n` |
| **Cuenta OpenAI** (API key) | <https://platform.openai.com/account/api-keys> |
| **Cuenta Twilio** (WhatsApp sandbox) | <https://www.twilio.com/console/sms/whatsapp/learn> |
| **Google Sheet** (para registro) | Crea una hoja con columnas: `timestamp, from, message, response` |

### 📋 Paso a paso  

| Paso | Acción en n8n | Detalle |
|------|----------------|---------|
| **1** | **Crear workflow nuevo** | Botón “+ New Workflow”. Ponle nombre: *WhatsApp‑AutoReply*. |
| **2** | **Añadir Trigger – Webhook** | <ul><li>Tipo: `Webhook`.</li><li>URL generada → cópiala (ej.: `https://YOUR_N8N_URL/webhook/whatsapp`).</li></ul> |
| **3** | **Configurar Twilio** | En Twilio Dashboard → “Sandbox → Messaging” → **WHEN A MESSAGE COMES IN** pon la URL del webhook. |
| **4** | **Añadir nodo “Set”** (opcional) | Extrae los campos `Body` y `From` del payload (`{{$json["Body"]}}`, `{{$json["From"]}}`). |
| **5** | **Añadir nodo “OpenAI”** | <ul><li>Credencial: pega tu API key.</li><li>Modelo: `gpt-4`.</li><li>Prompt: <br>`Eres un asistente de soporte para una startup de SaaS. Responde de forma breve y amigable al siguiente mensaje: "{{ $json["Body"] }}"`</li></ul> |
| **6** | **Añadir nodo “Twilio” (Send Message)** | <ul><li>Credenciales Twilio (Account SID + Auth Token).</li><li>From: `whatsapp:+14155238886` (sandbox).</li><li>To: `{{$json["From"]}}`.</li><li>Body: `{{$node["OpenAI"].json["choices"][0]["message"]["content"]}}`</li></ul> |
| **7** | **Añadir nodo “Google Sheets – Append”** | <ul><li>Credencial: Google OAuth.</li><li>Spreadsheet ID → tu hoja.</li><li>Values: `[{{$json["timestamp"]}}, {{$json["From"]}}, {{$json["Body"]}}, {{$node["OpenAI"].json["choices"][0]["message"]["content"]}}]`</li></ul> |
| **8** | **Conectar nodos** | Conecta en orden: Webhook → Set → OpenAI → Twilio → Google Sheets. |
| **9** | **Activar workflow** | Botón “Activate”. |
| **10** | **Probar** | Envía un mensaje al número sandbox de WhatsApp. Deberías recibir una respuesta automática y ver la fila añadida en Google Sheets. |

### 🛠️ Tips de depuración  
- Usa el panel “Execution” para inspeccionar cada nodo.  
- Si OpenAI devuelve error “Rate limit”, añade un nodo “Wait” de 1 s antes del llamado.  
- En caso de que Twilio no envíe, verifica que el número “From” sea el sandbox y que la cuenta tenga crédito.

---

## 5️⃣ Recursos adicionales  

| Tipo | Enlace | Comentario |
|------|--------|------------|
| **Documentación n8n** | <https://docs.n8n.io> | Guías paso a paso y catálogo de nodos. |
| **Plantilla “WhatsApp‑AutoReply”** | <https://n8n.io/workflows/1234> | Importa directamente a tu espacio. |
| **OpenAI API Docs** | <https://platform.openai.com/docs> | Ejemplos de prompts y parámetros de temperatura. |
| **Twilio WhatsApp Quickstart** | <https://www.twilio.com/docs/whatsapp/quickstart> | Configuración del sandbox y ejemplos de código. |
| **Curso gratuito “Automation for Startups”** | <https://www.udemy.com/course/automation-for-startups/> | 2 h de videos centrados en casos de uso latinos. |
| **Comunidad n8n LATAM**