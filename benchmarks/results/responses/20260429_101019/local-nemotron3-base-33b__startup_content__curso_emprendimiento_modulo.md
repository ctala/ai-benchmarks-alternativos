# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — startup_content/curso_emprendimiento_modulo

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 7.3 | quality: 9.44
- latency_total: 42.895s | tokens_per_second: 65.9
- input_tokens: 251 | output_tokens: 2828
- judge_score: 4.6 | justificación: 

## Respuesta completa

## **Módulo 3 – Automatización con IA: De la Idea al Flujo de Trabajo**  

---

### 1️⃣ Objetivo del módulo  
Aprenderás a transformar una idea de negocio en un **flujo de trabajo automatizado con IA**, usando herramientas accesibles (como n8n) que no requieren conocimientos de programación. Al final del módulo serás capaz de diseñar, implementar y medir automatizaciones que ahorren tiempo, mejoren la atención al cliente y aumenten tus ventas.

---

### 2️⃣ Contenido teórico  

#### ¿Qué es la automatización con IA?  
- **Automatización**: ejecución de tareas repetitivas sin intervención humana.  
- **IA (Inteligencia Artificial)**: algoritmos que “aprenden” de datos para tomar decisiones o generar resultados (p. ej., clasificar, traducir, recomendar).  
- **Combinación**: la IA añade **inteligencia** a la automatización tradicional (p. ej., un chatbot que entiende el lenguaje natural en vez de seguir reglas rígidas).  

#### Herramientas clave  

| Herramienta | Qué hace | Por qué es útil para emprendedores |
|-------------|----------|-----------------------------------|
| **n8n (Node-based Automation)** | Plataforma de código abierto para crear flujos de trabajo arrastrando nodos (disparadores, acciones, decisiones). Integra cientos de apps (Google Sheets, Gmail, WhatsApp, OpenAI, etc.). | No requiere programación, es **gratuita** (auto‑hosted) o tiene planes cloud con precios bajos. Ideal para conectar apps y añadir pasos de IA (p. ej., generar texto con OpenAI). |
| **Zapier** | Similar a n8n pero SaaS (en la nube). | Muy fácil de usar, buen soporte y plantillas preconstruidas. |
| **Make (Integromat)** | Visual flow builder con lógica avanzada. | Útil cuando se necesita lógica condicional compleja. |
| **OpenAI / Claude / Gemini API** | Modelos de IA que pueden generar texto, resumir, traducir, clasificar, etc. | Se integran mediante HTTP requests dentro de n8n para añadir “cerebro” de IA a cualquier flujo. |

**Concepto básico de un flujo en n8n**  
1. **Disparador (Trigger)** – evento que inicia el flujo (ej.: “Nuevo mensaje en WhatsApp”).  
2. **Procesamiento** – pasos que pueden incluir filtros, transformaciones, llamadas a IA, etc.  
3. **Acción (Action)** – lo que se hace después (enviar email, crear registro en Google Sheets, publicar en Instagram).  

---

### 3️⃣ 3 Ejemplos prácticos de automatización para startups  

| # | Caso de uso | Qué se automatiza | Herramientas recomendadas | Resultado esperado |
|---|-------------|-------------------|---------------------------|--------------------|
| **1** | **Atención al cliente automatizada** | Responder preguntas frecuentes, crear tickets y asignar a tu equipo. | n8n + WhatsApp / Telegram → OpenAI (chatbot) → Google Sheets (registro) → Gmail (respuesta). | Respuestas 24/7, reducción del 60‑80 % del tiempo de respuesta y menos carga para tu equipo. |
| **2** | **Generación de contenido para redes sociales** | Crear posts, captions, hashtags y mini‑imágenes a partir de un brief. | n8n → Google Docs (brief) → OpenAI (texto) → Canva API (imagen) → Instagram / Facebook (publicar). | Publicación diaria de contenido de calidad sin necesidad de redactor o diseñador. |
| **3** | **Calificación automática de leads** | Asignar un score a cada lead basado en comportamiento (descargas, visitas, emails). | n8n → HubSpot / Mailchimp (captura de lead) → Google Sheets (base de datos) → OpenAI (análisis de texto) → Slack (alerta). | Priorización de leads calientes, aumento del cierre de ventas en ~15 %. |

---

### 4️⃣ Ejercicio práctico paso a paso  
**Objetivo:** Crear un flujo que **captura un nuevo lead desde un formulario de Google Forms, lo califique usando IA y lo envía a un canal de Slack** (para que tu equipo lo revise).  

> **Requisitos previos**  
> - Cuenta en **Google Forms** (crea un formulario sencillo: Nombre, Email, Fuente).  
> - Cuenta en **Slack** (crea un canal llamado `#leads`).  
> - Regístrate en **n8n.cloud** (plan gratuito) o descarga la versión auto‑hosted (Docker).  
> - Acceso a la **API de OpenAI** (obtén tu `API Key`).  

#### Paso 1 – Preparar el formulario  
1. Crea un nuevo Google Form con los campos: **Nombre**, **Email**, **Origen** (p. ej., “Redes”, “Evento”, “Referral”).  
2. Copia la URL del formulario; la usaremos como disparador.

#### Paso 2 – Crear la cuenta en n8n  
1. Inicia sesión en n8n.cloud.  
2. En el panel izquierdo, haz clic en **“+ Create Flow”** → ponle nombre: **“Calificación de Leads IA”**.

#### Paso 3 – Añadir el disparador (Trigger)  
1. Busca el nodo **“Google Forms”** → arrástralo al lienzo.  
2. Conecta la cuenta Google (OAuth).  
3. Selecciona **“New Form Response”**.  
4. Introduce la URL del formulario o el ID del formulario.  
5. **Testea** el nodo para asegurarte de que captura una respuesta.

#### Paso 4 – Procesar los datos (Transform)  
1. Añade un nodo **“Set”** (para crear un string con la información del lead).  
2. En la expresión, concatena: `{{ $json["response_1"] }}` (nombre) + `{{ $json["response_2"] }}` (email) + `{{ $json["response_3"] }}` (origen).  
3. Opcional: usa un nodo **“Function”** para limpiar datos (p. ej., quitar espacios).  

#### Paso 5 – Llamada a la IA (OpenAI)  
1. Añade el nodo **“OpenAI”** → elige la opción **“Chat Completion”**.  
2. Configura:  
   - **Model**: `gpt-3.5-turbo` (rápido y barato).  
   - **Prompt** (ejemplo):  

   ```
   Evalúa la calidad de este lead y dame un score de 1 a 10.
   Información: Nombre: {{ $json["response_1"] }}, Email: {{ $json["response_2"] }}, Origen: {{ $json["response_3"] }}.
   Responde solo con un número y una breve justificación (ej: "8 - Buen origen y email profesional").
   ```  
3. Conecta el nodo de “Set” (o la salida del formulario) al nodo OpenAI.  
4. **Testea** la llamada y verifica que la salida sea un número + texto.

#### Paso 6 – Guardar el resultado (opcional)  
1. Añade un nodo **“Google Sheets”** → “Add Row”.  
2. Selecciona tu hoja de cálculo y mapea:  
   - **Nombre** → `{{ $json["response_1"] }}`  
   - **Email** → `{{ $json["response_2"] }}`  
   - **Origen** → `{{ $json["response_3"] }}`  
   - **Score IA** → `{{ $json["choices"][0]["text"] }}` (extrae el número).  

#### Paso 7 – Notificar a Slack  
1. Añade el nodo **“Slack”** → “Send Channel Message”.  
2. Conecta tu cuenta Slack y elige el canal `#leads`.  
3. En el mensaje, escribe:  

   ```
   *Nuevo Lead*  
   Nombre: {{ $json["response_1"] }}  
   Email: {{ $json["response_2"] }}  
   Origen: {{ $json["response_3"] }}  
   Score IA: {{ $json["choices"][0]["text"] | regex Find "\d+" }}  
   ```

4. **Testea** el nodo para confirmar que el mensaje llega a Slack.

#### Paso 8 – Activar y monitorear  
1. Haz clic en **“Execute Workflow”** (botón de play).  
2. Envía una respuesta de prueba al Google Form.  
3. Revisa:  
   - Que el registro se añada a Google Sheets.  
   - Que Slack reciba el mensaje con el score.  

#### Paso 9 – Mejoras (opcional)  
- Añade un **filtrado** para solo notificar leads con score > 7.  
- Usa **n8n → “Delay”** para enviar un email de bienvenida después de la calificación.  

---

### 5️⃣ Recursos adicionales  

| Tipo | Enlace | Descripción |
|------|--------|-------------|
| **Tutorial oficial n8n** | <https://docs.n8n.io/> | Guía paso a paso, ejemplos de flujos y videos. |
| **Plantilla de flujo “Lead Scoring”** | <https://github.com/n8n-io/n8n-examples/tree/main/lead-scoring> | Código listo para importar en n8n. |
| **Curso gratuito de IA para no‑técnicos** | <https://learn.openai.com/> | Introducción a prompts y uso de la API. |
| **Blog de casos de éxito latinoamericanos** | <https://www.startupi.io/blog/automacion-ia> | Historias de startups de México, Colombia y Perú que usan n8n. |
| **Community Slack** | <https://n8n.io/community/> | Grupo de usuarios donde puedes preguntar dudas técnicas. |

---

### 6️⃣ Preguntas de autoevaluación  

1. **¿Qué componente del flujo de n8n se encarga de “despertar” la automatización y por qué es esencial para conectar tu formulario con el resto del proceso?**  
   a) Action  
   b) Trigger (Disparador)  
   c) Filter  

2. **Si quieres que el chatbot de atención al cliente entienda mejor el idioma español, ¿qué paso deberías agregar en n8n antes de enviar el mensaje a la IA?**  
   a) Un nodo “Translate” que convierta el texto a inglés.  
   b) Un nodo “Set” que añada un prompt en español.  
   c) No es necesario; la IA ya detecta el idioma automáticamente.  

3. **¿Cuál es la ventaja principal de usar n8n auto‑hosted frente a una solución SaaS como Zapier para una startup con presupuesto limitado?**  
   a) n8n tiene más apps integradas.  
   b) n8n es gratuito y puedes escalar sin costos de suscripción por usuario.  
   c) n8n permite usar código JavaScript sin limitaciones.  

---  

¡Felicidades! Con este módulo ya tienes las bases para **convertir cualquier idea en un flujo de trabajo automatizado con IA**. Practica los pasos, experimenta y verás cómo tu tiempo y recursos se liberan para enfocarte en lo que realmente importa: **crecer tu negocio**. 🚀