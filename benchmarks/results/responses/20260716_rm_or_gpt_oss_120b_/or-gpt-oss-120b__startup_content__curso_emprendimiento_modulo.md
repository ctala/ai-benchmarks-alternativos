# GPT-OSS 120B — startup_content/curso_emprendimiento_modulo

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 31.062s | tokens_per_second: 63.7
- input_tokens: 279 | output_tokens: 1980
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando información detallada y ejemplos prácticos que un emprendedor puede aplicar directamente.

## Respuesta completa

# Módulo 3 – Automatización con IA: De la idea al flujo de trabajo  

---

## 1. Objetivo del módulo  

Al finalizar este módulo, el emprendedor será capaz de identificar procesos repetitivos susceptibles de ser automatizados con IA, seleccionar la herramienta adecuada (n8n) y diseñar, probar y poner en marcha su propio flujo de trabajo automatizado que le ahorre tiempo, mejore la experiencia del cliente y aumente la generación de oportunidades de negocio.

---

## 2. Contenido teórico  

| Tema | Qué aprenderás | Por qué es importante |
|------|----------------|----------------------|
| **¿Qué es la automatización con IA?** | Concepto de “workflow” + IA vs. automatización tradicional. | Te permite combinar decisiones inteligentes (IA) con tareas repetitivas (automatización). |
| **Ventajas para startups** | Reducción de costos, velocidad de ejecución, escalabilidad y mejora de la experiencia del cliente. | Cada minuto que ahorras se traduce en tiempo para crear valor y crecer. |
| **Componentes de un flujo de trabajo con IA** | 1️⃣ Trigger (evento que inicia el proceso) 2️⃣ Acción (tarea que se ejecuta) 3️⃣ Condición/branch (decisión basada en IA) 4️⃣ Salida (resultado o notificación). | Entender la lógica te ayuda a armar flujos claros y mantenibles. |
| **Herramientas low‑code: n8n** | - Qué es n8n (plataforma open‑source de automatización). <br>- Principales bloques (Node, Trigger, Function, AI Integration). <br>- Por qué n8n es ideal para emprendedores no‑técnicos (interfaz visual, comunidad, hosting gratuito). | No necesitas saber programar; con “arrastrar‑y‑soltar” puedes conectar APIs de IA (OpenAI, Cohere, etc.). |
| **Buenas prácticas** | • Diseña flujos sencillos → prueba cada paso. <br>• Usa “logging” para detectar errores. <br>• Guarda versiones (exporta JSON). <br>• Cuida la privacidad de datos (GDPR, LGPD). | Evita sorpresas y mantén la confianza de tus clientes. |

> **Tip:** En n8n, cada nodo tiene una **documentación integrada** (ícono “?!”). Usa esa herramienta mientras construyes tus flujos.

---

## 3. 3 ejemplos prácticos de automatización para startups  

### 3.1. Atención al cliente automatizada  
- **Trigger:** Un mensaje nuevo llega a WhatsApp Business (Webhooks).  
- **AI:** ChatGPT (OpenAI) genera una respuesta basada en una base de preguntas frecuentes.  
- **Acción:** Se envía la respuesta al cliente vía WhatsApp y se guarda el ticket en Airtable.  

### 3.2. Generación de contenido para redes sociales  
- **Trigger:** Cada vez que el equipo sube una idea de post a Google Sheets.  
- **AI:** El modelo de lenguaje elabora 3 versiones de copy + hashtags.  
- **Acción:** Publícalas directamente en Buffer (o programa su publicación) y notifica al equipo por Slack.  

### 3.3. Calificación automática de leads  
- **Trigger:** Un nuevo formulario de captura (Typeform) se completa.  
- **AI:** Un modelo de clasificación (OpenAI) evalúa el texto del formulario y asigna un “score” 1‑10.  
- **Condición:** Si el score ≥ 7 → el lead se envía a HubSpot como “Calificado”. Si < 7 → se archiva o se envía a nurture email vía Mailchimp.  

---  

## 4. Ejercicio práctico paso a paso  

> **Objetivo:** Crear un flujo que reciba consultas por email, genere una respuesta automática usando IA y la archive en Google Drive.  
> **Tiempo estimado:** 45 min  

### Paso 1 – Preparar cuentas  
1. Regístrate (gratuita) en **n8n.cloud** o instala n8n en tu PC.  
2. Crea una cuenta en **OpenAI** (API key) y **Google Cloud** (para Google Drive).  
3. Configura un alias de correo (p.ej. consultas@tusitio.com) que reenvíe los mensajes a una dirección que n8n pueda leer vía IMAP.

### Paso 2 – Crear el workflow en n8n  
1. En el dashboard de n8n, haz clic en **“New Workflow”**.  
2. **Añade el trigger “IMAP Email”**  
   - Host: `imap.gmail.com` (o tu proveedor).  
   - Usuario / contraseña: credenciales del alias.  
   - Marca **“Only unread”** para no procesar dos veces.  
3. **Añade un nodo “OpenAI”** (Search “ChatGPT”)  
   - Conecta el nodo al trigger.  
   - En “Prompt” escribe:  
     ```
     Responde de forma cordial y profesional a la siguiente consulta del cliente, utilizando la siguiente política de respuesta: {{ $json.body }}
     ```  
   - Configura **model** (e.g., `gpt-4o-mini`) y **temperature 0.5**.  
4. **Añade un nodo “Gmail – Send Email”** (o “SMTP”)  
   - Conecta la salida del nodo OpenAI.  
   - Configura “To” con `{{$json.from}}` (el cliente); asunto “Re: {{$json.subject}}”; cuerpo con `{{$node["OpenAI"].json.choices[0].message.content}}`.  
5. **Añade un nodo “Google Drive – Upload”**  
   - Conecta también a la salida del nodo OpenAI.  
   - Ruta: `/Consultas Automáticas/` (crea la carpeta).  
   - Nombre de archivo: `consulta_{{$json.id}}_{{ $now.format("YYYYMMDD_HHmm") }}.txt`.  
   - Contenido: `{{$node["OpenAI"].json.choices[0].message.content}}`.  

### Paso 3 – Probar el flujo  
1. Envía un email de prueba a tu alias con cualquier pregunta (“¿Cuáles son sus planes de precios?”).  
2. En n8n, pulsa **“Execute Workflow”** → observa los logs.  
3. Verifica:  
   - Recibiste la respuesta automática en tu bandeja.  
   - En Google Drive apareció el archivo `.txt` con la respuesta.  

### Paso 4 – Publicar y activar  
1. Cambia el botón **“Execute Workflow”** a **“Active”** (interruptor).  
2. Opcional: Añade un **“Error Trigger”** que notifique a Slack si alguna petición falla.  

### Paso 5 – Documentar y versionar  
1. Exporta el workflow (menú → Export → JSON).  
2. Guarda el archivo en tu repositorio interno o en Notion para referencia futura.  

> **Consejo:** Repite este proceso con los otros dos ejemplos (social media y leads) adaptando los nodos de trigger y AI.  

---  

## 5. Recursos adicionales  

| Tipo | Enlace | Comentario |
|------|--------|------------|
| **Documentación oficial n8n** | <https://docs.n8n.io/> | Guías paso a paso y ejemplos de IA. |
| **Plantilla de flujo de atención al cliente** | <https://n8n.io/workflows/1234> | Importa directamente a tu cuenta. |
| **OpenAI API Quickstart** | <https://platform.openai.com/docs/quickstart> | Cómo obtener tu clave y probar la API. |
| **Curso corto: “No‑code AI for Startups”** | Udemy / Coursera (buscar “AI no‑code”) | Video tutorial de 2 h. |
| **Comunidad latinoamericana n8n** | <https://discord.com/invite/n8n> (canal “es‑latam”) | Soporte en español y casos de uso locales. |
| **Guía legal de IA** | <https://www.dataprivacylaws.org/latam> | Buenas prácticas de privacidad y uso de datos. |

---  

## 6. Preguntas de autoevaluación  

1. **¿Cuál es la diferencia entre un “trigger” y una “acción” en un flujo de trabajo automatizado?**  
2. **Menciona al menos dos ventajas de usar n8n frente a escribir código a mano para integrar una IA.**  
3. **En el ejemplo de calificación automática de leads, ¿qué ocurre si el “score” asignado por la IA es menor a 7?**  

*Responde en tu cuaderno de notas o en la plataforma del curso y revisa el feedback automático.*  