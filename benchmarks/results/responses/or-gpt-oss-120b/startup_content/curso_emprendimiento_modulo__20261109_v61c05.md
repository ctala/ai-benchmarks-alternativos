# GPT-OSS 120B — startup_content/curso_emprendimiento_modulo

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 63.343s | tokens_per_second: 38.4
- input_tokens: 282 | output_tokens: 2432
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una profundidad significativa con ejemplos prácticos y herramientas detalladas, todo presentado de manera clara y útil para emprendedores.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3 – **Automatización con IA: De la idea al flujo de trabajo**

---

## 1️⃣ Objetivo del módulo  

Al finalizar este módulo, el emprendedor será capaz de diseñar y poner en marcha flujos de trabajo automatizados que utilicen inteligencia artificial para resolver tareas repetitivas de su startup (atención al cliente, generación de contenido y calificación de leads). Aprenderá a seleccionar la herramienta adecuada (p. ej. **n8n**), a conectar sus aplicaciones favoritas y a medir el impacto de la automatización en tiempo y costos.

---

## 2️⃣ Contenido teórico  

### 2.1 ¿Qué es la automatización con IA?  
| Concepto | Descripción breve | Valor para la startup |
|----------|-------------------|-----------------------|
| **Automatización** | Uso de software para ejecutar tareas sin intervención humana. | Reduce errores y libera tiempo. |
| **Inteligencia artificial** | Algoritmos que “aprenden” de datos (NLP, visión, clasificación). | Añade capacidad de razonamiento (p. ej. entender mensajes, generar texto). |
| **IA + Automatización** | Combina ambas para que la máquina no solo haga la tarea, sino que también tome decisiones informadas. | Mejora la calidad y personaliza la experiencia. |

### 2.2 Arquitectura básica de un flujo automatizado  
1. **Trigger (disparador)** – Evento que inicia el flujo (p. ej. nuevo mensaje en WhatsApp).  
2. **Acciones** – Pasos que el flujo ejecuta (consultar base de datos, llamar a una API de IA, enviar email).  
3. **Condiciones** – “Si… entonces…” que guían la lógica (p. ej. si el sentimiento es negativo, escalar a un agente).  
4. **Salida** – Resultado final (respuesta al cliente, publicación en redes, registro en CRM).

### 2.3 Herramientas low‑code para automatizar con IA  

| Herramienta | Tipo | IA integrada | Integraciones populares | Precio (plan básico) |
|-------------|------|--------------|------------------------|----------------------|
| **n8n** | Open‑source, auto‑hosted o cloud | Conectores a OpenAI, Cohere, Hugging Face, etc. | Gmail, Slack, HubSpot, Airtable, Twilio... | Gratis (self‑host) / $20/mes (cloud) |
| **Make (Integromat)** | SaaS | Módulos de “AI” (OpenAI, Azure) | Shopify, Facebook Ads, Google Sheets... | Gratis hasta 1 000 operaciones/mes |
| **Zapier** | SaaS | Zapier AI Actions (ChatGPT, Whisper) | Trello, Mailchimp, Typeform... | Gratis 100 tareas/mes |
| **Microsoft Power Automate** | SaaS | AI Builder (texto, visión, análisis) | Office 365, Dynamics, Teams... | Desde $15/mes por usuario |

> **Tip para emprendedores no‑técnicos:** comienza con la versión cloud de n8n (https://app.n8n.io) o con Zapier, que ofrecen plantillas pre‑configuradas y una interfaz drag‑and‑drop.

---

## 3️⃣ Tres ejemplos prácticos de automatización para startups  

### 🔹 3.1 Atención al cliente automatizada  
**Flujo:**  
1. Cliente envía mensaje a WhatsApp.  
2. n8n recibe el webhook → envía el texto a **OpenAI GPT‑4** para detectar intención y tono.  
3. Si la intención es “consulta de precios” → responde con un mensaje templado y un botón de “ver catálogo”.  
4. Si el tono es negativo → crea ticket en **HubSpot** y notifica a un agente vía Slack.  

**Beneficio:** Respuestas 24 h, 80 % de preguntas resueltas sin intervención humana.

### 🔹 3.2 Generación de contenido para redes sociales  
**Flujo:**  
1. Cada lunes, un trigger en n8n lee las métricas de la semana (Google Analytics, Facebook Insights).  
2. Con los datos, se envía una solicitud a **ChatGPT** para crear 3 ideas de post (texto + hashtags).  
3. Las ideas se guardan en una hoja de Google Sheets y se envían a un canal de **Discord** para revisión.  
4. Al aprobar, Zapier programa la publicación automática en **Instagram** y **LinkedIn**.  

**Beneficio:** Reduce el tiempo de planificación de contenido en un 70 %.

### 🔹 3.3 Calificación automática de leads  
**Flujo:**  
1. Nuevo lead se registra en **Typeform** (campo: “¿Cuál es tu presupuesto?”).  
2. n8n captura el registro → envía la descripción del proyecto a **OpenAI** para extraer palabras clave (urgencia, sector, tamaño).  
3. Con una regla de puntuación (ej. presupuesto > $5k = +30 pts, sector fintech = +20 pts), se asigna un score.  
4. Si score ≥ 70 → se crea una oportunidad en **Pipedrive** y se envía email de bienvenida con propuesta preliminar.  

**Beneficio:** Acelera el pipeline y evita que el equipo persiga leads de bajo valor.

---

## 4️⃣ Ejercicio práctico paso a paso  

> **Objetivo:** Crear un mini‑flujo en **n8n** que responda automáticamente a preguntas frecuentes de clientes vía WhatsApp usando ChatGPT.  

### Requisitos  
- Cuenta gratuita en **n8n Cloud** (https://app.n8n.io).  
- Cuenta de **Twilio** (para número de WhatsApp) – plan trial es suficiente.  
- API Key de **OpenAI** (puedes obtener una gratis en https://platform.openai.com).  

### Paso a paso  

| Paso | Acción | Detalle |
|------|--------|---------|
| **1** | **Crear proyecto** | En n8n, haz clic en *New Workflow* → ponle nombre *FAQ‑WhatsApp*. |
| **2** | **Trigger de WhatsApp** | Añade el nodo **Webhook** → copia la URL → en Twilio, crea *Messaging Service* → configura *Incoming Message* → usa la URL del webhook como *Request URL*. |
| **3** | **Parsear mensaje** | Añade un nodo **Set** para extraer `{{$json["Body"]}}` (texto del mensaje) y guardarlo como variable `question`. |
| **4** | **Llamada a OpenAI** | Añade nodo **HTTP Request** → método POST → URL `https://api.openai.com/v1/chat/completions` → Header `Authorization: Bearer <TU_API_KEY>` → Body JSON: <br>```json { "model": "gpt-4o-mini", "messages": [{ "role": "system", "content": "Eres un asistente de soporte para una startup de SaaS. Responde en español y sé breve." }, { "role": "user", "content": "{{$node["Set"].json["question"]}}" }], "max_tokens": 150 }``` |
| **5** | **Obtener respuesta** | Añade otro nodo **Set** → crea campo `answer` con expresión `{{$json["choices"][0]["message"]["content"]}}`. |
| **6** | **Responder en WhatsApp** | Añade nodo **HTTP Request** (POST) → URL `https://api.twilio.com/2010-04-01/Accounts/<SID>/Messages.json` → Auth (Basic) usando SID y Auth Token → Body Form: `To=whatsapp:+<número cliente>`, `From=whatsapp:+<tu número Twilio>`, `Body={{$node["Set_2"].json["answer"]}}`. |
| **7** | **Activar el workflow** | Haz clic en *Activate* (arriba a la derecha). |
| **8** | **Probar** | Envía un mensaje a tu número de WhatsApp (p. ej. “¿Cuál es el precio del plan básico?”). Deberías recibir una respuesta automática en menos de 5 s. |

### Qué medir después de la prueba  
- **Tiempo de respuesta** (latencia del webhook).  
- **Tasa de acierto**: revisa si la respuesta cubrió la pregunta.  
- **Feedback del usuario**: agrega una encuesta corta (p. ej. “¿Fue útil la respuesta? 1‑5”).  

> **Tip:** Si la respuesta es demasiado larga, ajusta `max_tokens` o agrega una instrucción “Responde en 2‑3 frases”.

---

## 5️⃣ Recursos adicionales  

| Tipo | Enlace | Comentario |
|------|--------|------------|
| **Documentación n8n** | https://docs.n8n.io/ | Guías paso a paso, plantillas y comunidad. |
| **Plantilla de FAQ‑WhatsApp (n8n)** | https://n8n.io/workflows/12345 | Importa directamente a tu cuenta. |
| **Curso rápido de OpenAI API** | https://platform.openai.com/docs/quickstart | Entiende cómo estructurar prompts y manejar tokens. |
| **Libro blanco: IA para PYMES** | https://www.ia4pymes.com/whitepaper.pdf | Estrategias de automatización a nivel ejecutivo. |
| **Comunidad latinoamericana de n8n** | https://discord.gg/n8n-latam | Soporte en español y casos de uso locales. |
| **Plantilla de calificación de leads (Make)** | https://www.make.com/en/templates/lead-scoring | Alternativa visual para comparar con n8n. |

---

## 6️⃣ Preguntas de autoevaluación  

1. **¿Cuál es la diferencia fundamental entre un trigger y una condición en un flujo automatizado?**  
   *Respuesta esperada:* El trigger inicia el flujo cuando ocurre un evento; la condición evalúa datos dentro del flujo para decidir qué rama ejecutar.

2. **Menciona tres ventajas de combinar IA con automatización en la atención al cliente.**  
   *Respuesta esperada:* (Ej.) Respuestas 24 h, reducción de carga para agentes humanos, personalización basada en intención y tono del mensaje.

3. **En el ejercicio práctico, ¿qué parámetro de la petición a OpenAI controla la longitud de la respuesta y cómo lo ajustarías si la respuesta es demasiado larga?**  
   *Respuesta esperada:* `max_tokens`. Se disminuye su valor para limitar la cantidad de palabras/bytes generados.

--- 

> **¡Listo!** Ahora tienes los conceptos, ejemplos y una guía práctica para implementar tu primer flujo de IA en la startup. Pon a prueba lo aprendido, mide resultados y vuelve a iterar. 🚀