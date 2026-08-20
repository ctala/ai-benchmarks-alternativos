# DeepSeek V4 Pro (0813) — startup_content/curso_emprendimiento_modulo

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 129.431s | tokens_per_second: 32.6
- input_tokens: 245 | output_tokens: 4223
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

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

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del módulo

Al finalizar este módulo, serás capaz de identificar procesos repetitivos en tu emprendimiento que pueden automatizarse con inteligencia artificial, diseñar flujos de trabajo básicos usando herramientas visuales como n8n y poner en marcha tu primera automatización real que combine captura de datos, análisis con IA y envío de información a otras aplicaciones, sin necesidad de saber programar.

---

## 2. Contenido teórico

### ¿Qué es la automatización con IA?

La automatización tradicional ejecuta tareas siguiendo reglas fijas: "si pasa A, haz B". La automatización con IA agrega una capa de inteligencia que permite **entender, clasificar, generar o decidir** dentro del flujo.

Por ejemplo, en lugar de enviar todos los correos de clientes a la misma carpeta, un flujo con IA puede leer el mensaje, detectar si es una queja, una consulta de precios o un agradecimiento, y enviarlo al equipo correcto o responder automáticamente.

**Componentes clave de un flujo de trabajo automatizado:**

- **Disparador (Trigger):** evento que inicia el flujo (llega un correo, se llena un formulario, se publica un video).
- **Acciones:** pasos que se ejecutan (enviar mensaje, guardar en hoja de cálculo, publicar en redes).
- **Nodos de IA:** pasos donde un modelo de lenguaje (como GPT) analiza, resume, clasifica o genera texto.
- **Conexiones:** la lógica que une los pasos (puede incluir condiciones: si el lead es "caliente", avisar por WhatsApp; si no, guardar para newsletter).

### Herramientas: n8n y alternativas

**n8n** es una herramienta de automatización de código abierto que funciona con un editor visual de arrastrar y soltar. No necesitas programar, aunque si sabes un poco de lógica, podrás hacer flujos más potentes.

Ventajas de n8n para emprendedores:

- Tiene plan gratuito (n8n.cloud) o puedes instalarlo en tu propio servidor.
- Incluye nodos para cientos de aplicaciones: Gmail, Google Sheets, Slack, WhatsApp, Telegram, WordPress, Shopify, HubSpot, etc.
- Permite integrar modelos de IA como OpenAI, Anthropic, Google Gemini o modelos locales.
- La comunidad hispana ha crecido y hay muchas plantillas listas para usar.

Otras herramientas similares: **Zapier**, **Make (Integromat)**, **Activepieces**. La lógica es parecida: eliges un disparador, agregas acciones y conectas aplicaciones. En este curso usaremos n8n por su flexibilidad y costo accesible.

---

## 3. Ejemplos prácticos de automatización para startups

### 3.1 Atención al cliente automatizada

**Problema:** Recibes decenas de mensajes por Instagram, WhatsApp o correo con preguntas repetidas: precios, horarios, envíos, devoluciones.

**Solución con IA:**

1. Un formulario o bandeja de entrada recibe el mensaje.
2. Un nodo de IA clasifica la intención: "precio", "envío", "reclamo", "otro".
3. Si es una pregunta frecuente, la IA redacta una respuesta personalizada con la información de tu negocio (la obtienes de una base de conocimiento o de un documento que subiste).
4. Si es un reclamo o una consulta compleja, el flujo envía una alerta a un humano por Slack o Telegram con el resumen del mensaje.

**Herramientas típicas:** n8n + OpenAI + Gmail/WhatsApp Business + Slack.

### 3.2 Generación de contenido para redes sociales

**Problema:** Publicar todos los días en Instagram, LinkedIn o Facebook consume tiempo y creatividad.

**Solución con IA:**

1. Cada vez que publicas un artículo en tu blog o grabas un video, el flujo se dispara (RSS, YouTube, WordPress).
2. La IA lee el contenido y genera 3 versiones de copy para redes sociales, adaptadas a cada plataforma (tono más formal para LinkedIn, más cercano para Instagram).
3. El flujo crea las imágenes con una plantilla (puede usar Canva API o simplemente adjuntar la imagen destacada).
4. Programa las publicaciones automáticamente en Buffer, Metricool o directamente en las APIs de las redes.

**Herramientas típicas:** n8n + OpenAI + WordPress/YouTube + Buffer/Canva.

### 3.3 Calificación automática de leads

**Problema:** Llegan muchos contactos desde tu página web, pero no sabes cuáles están listos para comprar.

**Solución con IA:**

1. Un formulario de contacto o un chatbot captura datos: nombre, empresa, cargo, presupuesto, necesidad.
2. Un nodo de IA analiza las respuestas y asigna un puntaje (por ejemplo, de 0 a 100) y una etiqueta: "Caliente", "Tibio", "Frío".
3. Si el lead es "Caliente", se envía una notificación inmediata a tu WhatsApp o Slack con un resumen y se crea una tarea en tu CRM (HubSpot, Pipedrive, Notion).
4. Si es "Tibio", se guarda en una hoja de cálculo para una secuencia de correos de nutrición.
5. Si es "Frío", se archiva o se agrega a una lista de newsletter.

**Herramientas típicas:** n8n + OpenAI + Google Sheets + HubSpot/Notion + Slack/WhatsApp.

---

## 4. Ejercicio práctico paso a paso

### Escenario: Automatizar la recepción de leads desde un formulario

Vas a crear un flujo en n8n que haga lo siguiente:

1. Reciba los datos de un formulario (puede ser un formulario de Google, Typeform o un webhook de tu web).
2. Use IA para clasificar al lead como "Caliente", "Tibio" o "Frío" según su mensaje.
3. Guarde el resultado en una hoja de Google Sheets.
4. Si el lead es "Caliente", envíe un mensaje a tu Slack (o Telegram) para que lo contactes de inmediato.

> **Nota:** Este ejercicio usa la versión cloud gratuita de n8n. No necesitas instalar nada.

### Paso 1: Crear cuenta en n8n

- Entra a [n8n.cloud](https://n8n.cloud) y regístrate con tu correo.
- Elige el plan gratuito (incluye 20 ejecuciones de flujo por día, suficiente para practicar).
- Una vez dentro, verás el panel principal. Haz clic en **"New Workflow"**.

### Paso 2: Agregar el disparador Webhook

- En el lienzo en blanco, haz clic en **"+"** para agregar un nodo.
- Busca **"Webhook"** y selecciónalo.
- En la configuración del nodo:
  - **HTTP Method:** POST
  - **Path:** `lead` (puedes poner cualquier nombre)
  - **Response Mode:** "Immediate Response" (para que el formulario no espere)
- Haz clic en **"Execute Node"** para activar el webhook. Verás una URL de prueba. Cópiala.

### Paso 3: Simular el envío de un formulario

Para probar, usaremos un JSON de ejemplo. En el nodo Webhook, activa la opción **"Use Raw Body"** o simplemente usaremos el modo por defecto.

- Abre una pestaña nueva y pega la URL del webhook en un cliente como Postman, o usa este comando en tu terminal (opcional):

```bash
curl -X POST https://tu-instancia.n8n.cloud/webhook/lead \
  -H "Content-Type: application/json" \
  -d '{"nombre":"María López","empresa":"Startup XYZ","mensaje":"Necesito automatizar mi atención al cliente, tengo presupuesto aprobado para este mes"}'
```

Si no quieres usar terminal, puedes usar [webhook.site](https://webhook.site) para generar un envío de prueba o simplemente conectar más adelante un formulario real.

### Paso 4: Agregar nodo de IA (OpenAI)

- Vuelve a n8n y agrega un nuevo nodo después del Webhook.
- Busca **"OpenAI"** y selecciona **"Message a Model"** (o "Text Classifier" si está disponible).
- Conecta el nodo Webhook al nodo OpenAI.
- En la configuración:
  - **Resource:** Chat
  - **Model:** `gpt-4o-mini` (más económico)
  - **Messages:** Agrega un mensaje de tipo "User" y escribe:

```
Eres un asistente que clasifica leads para una startup. Según el siguiente mensaje del lead, responde solo con una palabra: "Caliente", "Tibio" o "Frío".

Mensaje del lead: {{ $json.body.mensaje }}

Criterios:
- Caliente: menciona presupuesto, urgencia o necesidad clara de compra.
- Tibio: muestra interés pero sin urgencia ni presupuesto.
- Frío: solo pide información general.
```

- Necesitarás agregar tu API Key de OpenAI. Ve a [platform.openai.com](https://platform.openai.com), crea una cuenta y genera una API Key. En n8n, haz clic en "Create New Credential" y pega la clave.

### Paso 5: Agregar nodo Google Sheets

- Agrega un nodo **"Google Sheets"** después del nodo OpenAI.
- Conecta el nodo OpenAI al nodo Google Sheets.
- Configura:
  - **Resource:** Sheet
  - **Operation:** Append
  - **Document:** crea una hoja de cálculo en Google Drive con columnas: `Nombre`, `Empresa`, `Mensaje`, `Clasificación`, `Fecha`.
  - **Sheet Name:** el nombre de la pestaña (por defecto "Hoja 1").
  - **Mapping:** asigna los campos:
    - `Nombre` → `{{ $('Webhook').item.json.body.nombre }}`
    - `Empresa` → `{{ $('Webhook').item.json.body.empresa }}`
    - `Mensaje` → `{{ $('Webhook').item.json.body.mensaje }}`
    - `Clasificación` → `{{ $('OpenAI').item.json.message.content }}` (o el campo donde esté la respuesta)
    - `Fecha` → `{{ $now.format('yyyy-MM-dd HH:mm') }}`

- Autoriza el acceso a tu cuenta de Google cuando n8n lo solicite.

### Paso 6: Agregar condición y notificación a Slack

- Agrega un nodo **"IF"** después de Google Sheets (o antes, según prefieras).
- Configura la condición:
  - **Value 1:** `{{ $('OpenAI').item.json.message.content }}`
  - **Operation:** Contains
  - **Value 2:** `Caliente`
- En la rama "true", agrega un nodo **"Slack"** (o **"Telegram"** si prefieres).
  - Conecta tu cuenta de Slack (necesitarás crear un webhook entrante en Slack).
  - En el mensaje escribe:

```
🔥 Lead caliente recibido:
Nombre: {{ $('Webhook').item.json.body.nombre }}
Empresa: {{ $('Webhook').item.json.body.empresa }}
Mensaje: {{ $('Webhook').item.json.body.mensaje }}
```

- En la rama "false", puedes no hacer nada o agregar un nodo "NoOp".

### Paso 7: Activar el flujo y probar

- Haz clic en **"Save"** y luego en **"Activate"** (interruptor en la esquina superior derecha).
- Vuelve a enviar una solicitud al webhook con un mensaje que claramente sea de un lead caliente (por ejemplo, "Necesito implementar un chatbot esta semana, tengo $5000 de presupuesto").
- Revisa tu hoja de Google Sheets: debería aparecer la fila con la clasificación "Caliente".
- Revisa tu Slack: deberías recibir la notificación.

¡Felicidades! Creaste tu primera automatización con IA.

---

## 5. Recursos adicionales

- **Documentación oficial de n8n:** [docs.n8n.io](https://docs.n8n.io) – guías paso a paso y referencia de nodos.
- **Plantillas de n8n:** [n8n.io/workflows](https://n8n.io/workflows) – busca "lead scoring", "customer support", "social media" y adáptalas.
- **Comunidad en español:** Busca en YouTube canales como "Automatizaciones con n8n" o únete a grupos de Telegram/WhatsApp de emprendedores que usan IA.
- **Curso gratuito de n8n en YouTube:** "n8n Tutorial for Beginners" (en inglés, pero con subtítulos) o canales en español como "Aprende n8n".
- **OpenAI API documentation:** [platform.openai.com/docs](https://platform.openai.com/docs) – para entender cómo funciona el modelo y sus límites.
- **Google Sheets API:** si quieres profundizar en la integración con hojas de cálculo.

---

## 6. Preguntas de autoevaluación

Responde estas preguntas para comprobar tu comprensión del módulo. Las respuestas están al final.

**1. ¿Cuál es la diferencia principal entre una automatización tradicional y una automatización con IA?**

a) La automatización con IA es más cara y difícil de implementar.  
b) La automatización tradicional solo ejecuta reglas fijas, mientras que la con IA puede entender, clasificar o generar contenido.  
c) No hay diferencia, ambas hacen lo mismo.  
d) La automatización con IA solo sirve para chatbots.

**2. En un flujo de n8n, ¿qué función cumple el nodo "Webhook"?**

a) Envía correos electrónicos automáticamente.  
b) Actúa como disparador: recibe datos desde un formulario o aplicación externa e inicia el flujo.  
c) Conecta con Google Sheets.  
d) Clasifica leads usando IA.

**3. En el ejercicio práctico, ¿qué condición usamos para enviar una notificación a Slack?**

a) Si el lead es "Frío".  
b) Si el lead es "Tibio".  
c) Si el lead es "Caliente".  
d) Siempre, sin importar la clasificación.

### Respuestas correctas:

1. **b)** La automatización tradicional solo ejecuta reglas fijas, mientras que la con IA puede entender, clasificar o generar contenido.  
2. **b)** Actúa como disparador: recibe datos desde un formulario o aplicación externa e inicia el flujo.  
3. **c)** Si el lead es "Caliente".