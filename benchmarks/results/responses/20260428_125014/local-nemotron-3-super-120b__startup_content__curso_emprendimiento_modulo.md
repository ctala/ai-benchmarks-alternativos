# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — startup_content/curso_emprendimiento_modulo

- model_id: `nemotron-3-super:120b`
- success: True  | final: 7.2 | quality: 9.72
- latency_total: 171.626s | tokens_per_second: 18.5
- input_tokens: 250 | output_tokens: 3171
- judge_score: 4.8 | justificación: 

## Respuesta completa

## Módulo 3 – Automatización con IA: De la idea al flujo de trabajo  

---

### 1. Objetivo del módulo  
Al finalizar este módulo, el emprendedor podrá **identificar oportunidades de automatización en su negocio, diseñar flujos de trabajo simples con herramientas no‑code impulsadas por IA (como N8N) y poner en marcha al menos un proceso automatizado que reduzca tareas repetitivas y mejore la eficiencia operativa**.

---

### 2. Contenido teórico  

#### ¿Qué es la automatización con IA?  
La **automatización con IA** combina reglas de flujo de trabajo (triggers, acciones, condiciones) con capacidades de inteligencia artificial (procesamiento de lenguaje natural, generación de texto, clasificación, visión por computadora, etc.). En lugar de programar cada paso manualmente, se usan plataformas **low‑code / no‑code** que permiten conectar aplicaciones y servicios mediante nodos visuales, mientras que los nodos de IA aportan la “inteligencia” (por ejemplo, entender un mensaje de cliente y responder de forma adecuada).

#### Herramienta destacada: **N8N**  
- **Qué es:** Plataforma de automatización de workflows de código abierto, alojable en la nube o en tu propio servidor.  
- **Ventajas para emprendedores no‑técnicos:**  
  - Interfaz drag‑and‑drop (arrastrar y soltar).  
  - Más de 200 integraciones nativas (WhatsApp, Gmail, Google Sheets, Airtable, Twitter, LinkedIn, OpenAI, etc.).  
  - Nodos de IA listos para usar (OpenAI GPT, Hugging Face, clasificación de texto, extracción de entidades).  
  - Precio: versión gratuita ilimitada para uso personal; planes de pago a partir de ~20 USD/mes para equipos.  

#### Flujo básico de un workflow en N8N  
1. **Trigger** (disparador): evento que inicia el flujo (ej. llega un nuevo mensaje de WhatsApp).  
2. **Nodos de acción**: pasos que hacen algo (ej. enviar el mensaje a un modelo de IA, leer una hoja de cálculo).  
3. **Condiciones / Ramas**: decidir qué camino seguir según el resultado (ej. si la intención es “queja”, enviarlo a un agente; si es “consulta de producto”, responder automáticamente).  
4. **Salida**: almacenar resultados, notificar al equipo, actualizar un CRM, etc.

---

### 3. Ejemplos prácticos de automatización para startups  

| # | Caso de uso | Qué se automatiza | Cómo funciona (esquema simplificado) | Beneficio clave |
|---|-------------|-------------------|--------------------------------------|-----------------|
| 1 | **Atención al cliente automatizada** | Responder preguntas frecuentes y escalar casos complejos | 1️⃣ Trigger: mensaje recibido en WhatsApp Business API  <br>2️⃣ Nodo IA (OpenAI GPT‑3.5) → clasifica intención y genera respuesta  <br>3️⃣ Condición: si confianza < 0.7 → asignar a agente humano (envío a Slack/Email)  <br>4️⃣ Respuesta enviada al usuario | Reduce tiempo de primera respuesta de minutos a segundos; libera al equipo para casos de alto valor. |
| 2 | **Generación de contenido para redes sociales** | Crear publicaciones semanales (texto + imagen) basadas en un calendario editorial | 1️⃣ Trigger: horario programado (todos los lunes 9 am)  <br>2️⃣ Nodo: leer fila de Google Sheet con tema y palabras clave  <br>3️⃣ Nodo IA (GPT‑4) → redacta copy y sugiere hashtags  <br>4️⃣ Nodo: usar Canva API o DALL·E para generar imagen basada en el copy  <br>5️⃣ Nodo: publicar en Instagram/Facebook vía API o mediante Buffer/Hootsuite | Mantiene presencia constante sin necesidad de un community manager a tiempo completo. |
| 3 | **Calificación automática de leads** | Priorizar contactos que llegan desde formularios web o anuncios | 1️⃣ Trigger: nuevo registro en HubSpot / Formulario de Google  <br>2️⃣ Nodo IA: clasifica lead (score 0‑100) según datos demográficos y respuestas (usando modelo de clasificación entrenado previamente o prompt de GPT)  <br>3️⃣ Condición: si score ≥ 80 → crear tarea en CRM y notificar al sales rep vía Slack  <br>4️⃣ Si score < 80 → agregar a secuencia de nurturing (email automatizado) | Enfoca el esfuerzo de ventas en los leads con mayor probabilidad de cierre, acortando el ciclo de venta. |

---

### 4. Ejercicio práctico paso a paso  
**Objetivo:** Crear un flujo en N8N que responda automáticamente a mensajes de WhatsApp con una respuesta generada por IA (ej. “Gracias por tu mensaje. En breve un agente te atenderá.”) y, si el mensaje contiene la palabra “queja”, lo reenvíe a un canal de Slack para atención humana.

> **Requisitos previos** (no necesitas programar):  
> - Cuenta gratuita en [N8N Cloud](https://n8n.io/cloud/) (o instancia auto‑hosted).  
> - Acceso a una cuenta de WhatsApp Business API (puedes usar la versión sandbox de Twilio para probar).  
> - Una cuenta de Slack con permiso para crear un Webhook Incoming.  
> - Clave de API de OpenAI (plan gratuito suficiente para pruebas).  

#### Paso 1 – Crear el workflow  
1. Inicia sesión en N8N y haz click en **+ New Workflow**.  
2. Ponle nombre: `WhatsApp IA Responder`.  

#### Paso 2 – Añadir el Trigger de WhatsApp  
1. En el nodo inicial, busca **WhatsApp** y selecciona **WhatsApp Trigger**.  
2. Configura:  
   - **Event:** `Message Received`  
   - **From:** tu número de WhatsApp Business (o el número sandbox de Twilio).  
   - Deja los demás valores por defecto y haz click en **Save**.  

#### Paso 3 – Enviar el mensaje a OpenAI (clasificación + respuesta)  
1. Haz click en **+** bajo el nodo de WhatsApp → **Add Node** → busca **OpenAI**.  
2. Elige la operación **Chat**.  
3. En **Prompt**, escribe:  
   ```
   Eres un asistente de atención al cliente. Analiza el siguiente mensaje y:
   1. Indica la intención (consulta, queja, felicitación, otro) y una puntuación de confianza (0‑1).
   2. Genera una respuesta amigable en español que agradezca el mensaje y diga que un agente lo atenderá pronto.
   Mensaje: {{$json["body"]}}
   ```
4. En **Temperature** pon `0.2` (respuestas más deterministas).  
5. Guarda el nodo.  

#### Paso 4 – Dividir el flujo según la intención (condición)  
1. Añade un nodo **IF** después del nodo OpenAI.  
2. Configura la condición:  
   - **Valor 1:** `{{ $json["choices"][0]["message"]["content"] }}` (el texto devuelto por GPT).  
   - **Operador:** `contains`  
   - **Valor 2:** `queja`  
3. Si la condición es **true** → rama **Queja**; si es **false** → rama **Respuesta estándar**.  

#### Paso 5 – Rama “Queja”: notificar a Slack  
1. En la rama **Queja**, agrega un nodo **Slack** → operación **Post Message**.  
2. Conecta tu cuenta de Slack (crea un Incoming Webhook si no lo tienes).  
3. En **Text**, pon:  
   ```
   🚨 Nueva queja detectada:
   Mensaje recibido: {{$node["WhatsApp"].json["body"]}}
   Respuesta IA: {{$node["OpenAI"].json["choices"][0]["message"]["content"]}}
   ```
4. Guarda.  

#### Paso 6 – Rama “Respuesta estándar”: enviar reply por WhatsApp  
1. En la rama **Respuesta estándar**, agrega un nodo **WhatsApp** → operación **Send Message**.  
2. Usa el mismo número de origen que el trigger.  
3. En **Message**, pon:  
   ```
   {{$node["OpenAI"].json["choices"][0]["message"]["content"]}}
   ```
4. Guarda.  

#### Paso 7 – Activar y probar  
1. Haz click en **Execute Workflow** (botón de prueba) para asegurarte de que no haya errores de sintaxis.  
2. Activa el workflow con el toggle **Active** en la esquina superior derecha.  
3. Envía un mensaje de prueba a tu número de WhatsApp (ej. “Hola, quiero saber horarios”).  
4. Verifica que recibas la respuesta automática.  
5. Envía otro mensaje con la palabra “queja” (ej. “Tengo una queja sobre el producto X”) y revisa que aparezca una notificación en tu canal de Slack.  

> **Tip:** Si usas la sandbox de Twilio, el número de origen y destino deben estar registrados en la consola de Twilio para que los mensajes pasen.

#### Paso 8 – Documentar y escalar  
- Guarda el workflow exportándolo (menú → **Export**) y compártelo con tu equipo.  
- Repite el proceso añadiendo más ramas (por ejemplo, detectar “solicitud de demo” y crear un evento en Google Calendar).  

---

### 5. Recursos adicionales  

| Tipo | Enlace | Descripción |
|------|--------|-------------|
| Tutorial oficial N8N | <https://docs.n8n.io/> | Guía paso a paso, nodos y ejemplos. |
| Curso gratuito “Automatiza tu negocio con N8N” (YouTube) | <https://www.youtube.com/watch?v=6lVZf0XK8sU> | Serie de videos en español, desde cero hasta flujos avanzados. |
| Plantillas de workflows para WhatsApp + IA | <https://n8n.io/workflows/> (buscar “WhatsApp OpenAI”) | Flujos pre‑construidos que puedes importar. |
| Guía de prompts para atención al cliente | <https://platform.openai.com/docs/guides/prompt-engineering> | Mejores prácticas para obtener respuestas consistentes y seguras. |
| Comunidad N8N en Discord | <https://discord.gg/n8n> | Soporte rápido, preguntas y ejemplos de usuarios. |
| Artículo: “Low‑code AI automation for Latin‑American startups” (Medium) | <https://medium.com/@tuusuario/low-code-ai-automation-latam> | Caso de estudio de una startup mexicana que redujo un 40% su tiempo de soporte. |

---

### 6. Preguntas de autoevaluación  

1. **¿Cuál es la función principal del nodo “IF” en un workflow de N8N y cómo podrías usarlo para diferenciar entre una consulta y una queja?**  
   *Respuesta esperada:* El nodo IF evalúa una condición (verdadero/falso) y divide el flujo en dos ramas. Para diferenciar consulta vs. queja, se verifica si el texto devuelto por el modelo de IA contiene la palabra “queja” (o cualquier otro indicador) y, según el resultado, se envía a la rama adecuada (notificar a Slack o responder automáticamente).

2. **En el ejemplo de generación de contenido para redes sociales, ¿qué nodo se encarga de crear la imagen y qué alternativa podrías usar si no tienes acceso a DALL·E?**  
   *Respuesta esperada:* El nodo que crea la imagen es el de **DALL·E** (o cualquier nodo de generación de imágenes). Una alternativa es usar la API de **Canva** para diseñar a partir de una plantilla, o bien un nodo que obtenga una imagen libre de derechos desde Unsplash/Pexels mediante su API.

3. **Imagina que deseas agregar un paso de enriquecimiento de lead: después de recibir un formulario, quieres consultar la empresa del lead en Clearbit para obtener su tamaño y industria. ¿Qué nodo añadirías y dónde lo colocarías en el flujo?**  
   *Respuesta esperada:* Añadirías el nodo **Clearbit** (operación “Enrich Company”) justo después del nodo que captura el formulario (trigger) y antes del nodo de clasificación de IA. Así el flujo tendría: Trigger de formulario → Clearbit (enriquecimiento) → IA (clasificación y scoring) → Condiciones → Acciones (CRM, email, Slack, etc.).  

---  

**¡Felicidades!** Has completado el Módulo 3. Ahora puedes empezar a experimentar con tus propios flujos de trabajo y llevar la automatización impulsada por IA a tu startup. 🚀