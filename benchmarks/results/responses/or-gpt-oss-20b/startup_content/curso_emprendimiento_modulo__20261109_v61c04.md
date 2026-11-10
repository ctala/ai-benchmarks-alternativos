# GPT-OSS 20B — startup_content/curso_emprendimiento_modulo

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.03 | quality: 9.72
- latency_total: 18.372s | tokens_per_second: 136.5
- input_tokens: 282 | output_tokens: 2507
- judge_score: 4.8 | justificación: 

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

## 1. Objetivo del módulo  
En este módulo aprenderás a transformar una idea de automatización en un flujo de trabajo funcional usando herramientas de IA y no‑code. Conocerás los conceptos básicos de la automatización inteligente, descubrirás cómo integrar distintos servicios con N8N y verás ejemplos reales que puedes replicar en tu startup sin ser un experto en programación.

---

## 2. Contenido teórico  

### 2.1 ¿Qué es la automatización con IA?  
- **Automatización**: Reemplazo de tareas repetitivas por procesos que se ejecutan sin intervención humana.  
- **IA añadida**: Se utilizan modelos de lenguaje, visión, reconocimiento de voz, etc., para que la automatización sea inteligente (por ejemplo, decidir qué tickets atender primero).  

> **Beneficio clave**: Ahorro de tiempo, reducción de errores y liberación de recursos humanos para tareas estratégicas.

### 2.2 ¿Por qué usar una herramienta no‑code como N8N?  
| Ventaja | Explicación | Ejemplo |
|---------|-------------|---------|
| **Facilidad de uso** | Interfaz de arrastrar‑soltar | Conectar un webhook de tu sitio con un modelo GPT sin escribir código |
| **Escalabilidad** | Se adapta a crecer sin depender de un desarrollador | Agregar nuevos nodos cuando lanzas un nuevo canal de soporte |
| **Integraciones nativas** | 200+ conectores (Zapier, Gmail, Slack, etc.) | Enviar un correo cuando un lead califica alto |
| **Open‑source** | Control total y sin costes mensuales | Hospedarlo en tu propio servidor y personalizar nodos |

### 2.3 Arquitectura básica de un flujo de trabajo IA  
1. **Disparador** (Trigger) – evento que inicia el flujo (p.ej., un nuevo mensaje en WhatsApp).  
2. **Procesamiento** – llamado a una API de IA (ChatGPT, Claude, etc.) o a un nodo de lógica.  
3. **Decisión** – condicionales (if/else) que guían el camino según la respuesta.  
4. **Salida** – acción final (enviar email, actualizar base de datos, etc.).  

> **Tip**: Mantén cada nodo enfocado en una sola tarea; así el flujo es más fácil de depurar y escalar.

---

## 3. Tres ejemplos prácticos de automatización para startups  

| # | Caso de uso | Flujo resumido | Herramientas principales |
|---|--------------|----------------|--------------------------|
| 1 | **Atención al cliente automatizada** | 1️⃣ Cliente envía mensaje en WhatsApp.<br>2️⃣ N8N captura el mensaje.<br>3️⃣ GPT responde con FAQ.<br>4️⃣ Si la pregunta es compleja, se crea un ticket en Zendesk. | N8N, WhatsApp API, OpenAI, Zendesk |
| 2 | **Generación de contenido para redes sociales** | 1️⃣ Entrada: lista de palabras clave.<br>2️⃣ GPT crea un borrador de post.<br>3️⃣ Se programa a través de Buffer.<br>4️⃣ Se asigna una imagen generada por DALL‑E. | N8N, ChatGPT, Buffer, DALL‑E |
| 3 | **Calificación automática de leads** | 1️⃣ Registro de lead en HubSpot.<br>2️⃣ N8N lee la información.<br>3️⃣ GPT analiza datos y asigna una puntuación (1‑10).<br>4️⃣ Se actualiza el lead y se envía alerta al equipo de ventas. | N8N, HubSpot, OpenAI |

> **Ejemplo práctico**: Cada caso incluye un flujo de 5‑6 nodos, que podrás replicar en tu cuenta de N8N.

---

## 4. Ejercicio práctico paso a paso  

**Objetivo del ejercicio**: Crear un flujo de atención al cliente automatizado que responda con FAQ y, si el cliente necesita más ayuda, cree un ticket en Zendesk.

> **Requisitos**:  
> - Cuenta gratuita de N8N (o instancia propia)  
> - Acceso a la API de WhatsApp Business (puedes usar Twilio WhatsApp Sandbox)  
> - API key de OpenAI  
> - Cuenta de Zendesk (plan gratuito)

### 4.1 Paso 1 – Preparar el entorno  
1. Inicia sesión en tu instancia de N8N.  
2. Ve a **Credentials** → **New Credential** → **OpenAI**.  
   - Introduce tu API Key.  
3. Crea otra credencial: **Zendesk**.  
   - URL: `https://tusubdominio.zendesk.com`  
   - Username: tu email de Zendesk.  
   - Password: token de API (puedes generarlo en la configuración de Zendesk).  

### 4.2 Paso 2 – Configurar el disparador  
1. Arrastra el nodo **Webhook** al canvas.  
2. Configura:  
   - **HTTP Method**: POST  
   - **Path**: `/whatsapp`  
3. Copia la URL que N8N te muestra (ej. `https://tuinstancia.n8n.cloud/webhook/whatsapp`).  
4. En Twilio Sandbox, configura el número de WhatsApp para que envíe mensajes a esa URL.

### 4.3 Paso 3 – Enviar el mensaje a ChatGPT  
1. Arrastra un nodo **OpenAI** (Chat API).  
2. Conecta el Webhook → OpenAI.  
3. Configura el prompt:  
   ```
   Pregunta del cliente: {{ $json["body"]["text"] }}
   Responde con la FAQ más relevante. Si no encuentras respuesta, devuelve “No conozco la respuesta, por favor contacta con un representante.”
   ```
4. Guarda y ejecuta una prueba enviando un mensaje de WhatsApp.

### 4.4 Paso 4 – Decidir la acción  
1. Añade un nodo **If**.  
2. Configura la condición:  
   ```
   {{$node["OpenAI"].json["choices"][0]["message"]["content"]}} contains "contacta con un representante"
   ```
3. Si **true** → crea ticket.  
4. Si **false** → envía respuesta al cliente.

### 4.5 Paso 5 – Crear ticket en Zendesk  
1. Arrastra el nodo **Zendesk** → **Create Ticket**.  
2. Conecta la rama **true** del nodo If → Zendesk.  
3. Configura:  
   - **Subject**: “Nuevo cliente necesita asistencia”  
   - **Description**: `{{ $node["Webhook"].json["body"]["text"] }}`  
   - **Requester**: correo del cliente (si lo tienes).  

### 4.6 Paso 6 – Enviar respuesta al cliente  
1. Arrastra un nodo **Twilio** (o WhatsApp API).  
2. Conecta la rama **false** del nodo If → Twilio.  
3. Configura:  
   - **To**: `whatsapp:{{ $node["Webhook"].json["body"]["from"] }}`  
   - **Body**: `{{ $node["OpenAI"].json["choices"][0]["message"]["content"] }}`  

### 4.7 Paso 7 – Activar y probar  
1. Haz clic en **Activate**.  
2. Envía un mensaje de prueba desde tu número de WhatsApp.  
3. Revisa que la respuesta se envíe y que, si es necesario, se cree el ticket en Zendesk.

> **Resultado**: Un flujo completo de atención al cliente que usa IA para responder preguntas frecuentes y solo delega a humanos cuando es imprescindible.

---

## 5. Recursos adicionales  

| Tipo | Recurso | Enlace |
|------|---------|--------|
| **Tutorial N8N** | “Getting Started with N8N: Build Your First Workflow” | <https://n8n.io/docs/getting-started> |
| **API OpenAI** | “Chat Completions API” | <https://platform.openai.com/docs/api-reference/chat> |
| **WhatsApp API** | Twilio Sandbox para WhatsApp | <https://www.twilio.com/docs/whatsapp/sandbox> |
| **Zendesk API** | “Create a Ticket” | <https://developer.zendesk.com/rest_api/docs/support/tickets> |
| **Curso de IA para emprendedores** | “IA para Negocios” (Udemy) | <https://www.udemy.com/course/ia-para-negocios> |
| **Libro** | “Building Automation with N8N” (en inglés) | <https://www.packtpub.com/product/building-automation-with-n8n/9781800209703> |
| **Comunidades** | Foro de N8N | <https://community.n8n.io/> |
| **Video** | “Automating Customer Support with AI” | <https://www.youtube.com/watch?v=XYZ> |

> **Tip**: Guarda los enlaces en un documento de Google Drive y actualízalos cuando cambien versiones o APIs.

---

## 6. Preguntas de autoevaluación  

1. **¿Qué diferencia a la automatización con IA de la automatización tradicional?**  
   - a) La IA no necesita nodos de lógica.  
   - b) La IA puede tomar decisiones basadas en datos y lenguaje.  
   - c) La automatización tradicional solo funciona con código.  

2. **En un flujo de N8N, ¿qué nodo se usa para decidir entre dos caminos (por ejemplo, “si la respuesta contiene X, hacer Y, de lo contrario hacer Z”)?**  
   - a) “If”  
   - b) “Switch”  
   - c) “Router”

3. **Cuando integras ChatGPT en un flujo de atención al cliente, ¿qué información debes incluir en el prompt para que la respuesta sea relevante?**  
   - a) Solo la pregunta del cliente.  
   - b) La pregunta del cliente y una instrucción clara (por ejemplo, “responde con la FAQ”).  
   - c) La pregunta del cliente y la lista completa de productos de la empresa.  

> **Respuestas**: 1b, 2a, 3b

--- 

¡Listo! Ahora tienes un módulo completo, práctico y adaptado a emprendedores sin experiencia técnica. Puedes usarlo tal cual o ajustarlo a las necesidades de tu audiencia.