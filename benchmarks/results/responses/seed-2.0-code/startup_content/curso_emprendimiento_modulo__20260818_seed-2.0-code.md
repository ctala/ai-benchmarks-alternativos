# Seed 2.0 Code — startup_content/curso_emprendimiento_modulo

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.34 | quality: 8.32
- latency_total: 39.271s | tokens_per_second: 52.2
- input_tokens: 289 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

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


El usuario quiere el Módulo 3 de "IA Practica para Emprendedores" titulado "Automatizacion con IA: De la idea al flujo de trabajo", para emprendedores no técnicos. Primero, voy a estructurar todo en Markdown como pide.

Primero, el Objetivo del Módulo: tiene que ser un párrafo, enfocado en emprendedores no técnicos, no solo hablar de herramientas sino de resolver problemas concretos: que pasen de tener una idea de automatizar (ej: "quiero no responder whatsapp a las 2am") a armar un flujo funcional sin código, usando IA, con herramientas como N8N, y que valoren que no se trata de automatizar todo sino lo que ahorra tiempo valioso (que es lo que los emprendedores necesitan).

Luego, Contenido Teórico: Empezar por explicar AUTOMATIZACIÓN CON IA de forma sencilla, NO como código, sino como "hacer que la computadora haga tareas repetitivas que nosotros hacemos, pero con IA para que no sea solo reglas rígidas" (diferencia entre automatización tradicional: "si llega un correo con 'factura' guardar en carpeta" vs automatización con IA: "si llega un correo, leerlo, entender si es una queja, un lead o una factura, y actuar según"). Luego explicar N8N PERO para no técnicos: es una herramienta de "arrastrar y soltar" (llamada low-code/no-code) que conecta herramientas que ya usas (WhatsApp, Instagram, Gmail, HubSpot, ChatGPT) sin escribir código. Mencionar que es gratis para uso básico, hay alternativas como Make (Zapier es más conocido pero N8N es más flexible y gratis para autoalojar o plan free). También explicar términos clave sin jerga: Nodo = paso del flujo, Trigger = lo que activa el flujo (ej: "cuando llega un mensaje a WhatsApp"), Conexión = unir dos herramientas.

Luego, 3 Ejemplos Prácticos para Startups: cada uno tiene que ser CONCRETO, para emprendedores latinos (ej: usar WhatsApp Business, que es muy usado en LATAM, no herramientas que no usen), con herramientas específicas, sin jerga.

Primer ejemplo: Atención al Cliente Automatizada (para tiendas de ropa online, servicio de coaching, lo que sea). No es un bot rígido: es un flujo que usa IA para entender el mensaje, responder preguntas frecuentes, o derivar a humano si es complejo. Detalles: Trigger = Mensaje nuevo en WhatsApp Business. Paso 1: IA (ChatGPT 3.5 Turbo, que es barato) lee el mensaje, clasifica en: "Pregunta Frecuente" (ej: "horarios", "envíos"), "Queja", "Pedido Especial", "Otro". Paso 2: Si es Pregunta Frecuente, IA usa una base de conocimiento TUYA (ej: tus horarios, costos de envío a CDMX, Medellín) para responder automáticamente. Si es Queja, envía un mensaje de disculpa y crea un ticket en Trello (o Notion) para que el equipo de atención lo revise en el día. Si es Pedido Especial, envía un mensaje de "te contactaremos en 1 hora" y avisa por correo al jefe de ventas. Mencionar ejemplo real: una emprendedora de aretes en Bogotá que usó este flujo y redujo el tiempo de respuesta de 4 horas a 2 minutos, y ahorró 15 horas a la semana.

Segundo ejemplo: Generación de Contenido para Redes Sociales (para cualquier startup, especialmente las de contenido o e-commerce). No es generar contenido sin sentido: es un flujo que te ayuda a crear contenido PERSONALIZADO según tu audiencia, sin que tengas que pensar en ideas todo el día. Trigger: Cada lunes a las 9am (o cada vez que agregas un producto nuevo a tu Shopify). Paso 1: IA (ChatGPT 4o Mini o Claude 3 Haiku) revisa tus últimos 10 posts de Instagram para ver qué funcionó (ej: los posts de "detrás de cámara" tuvieron 3x más interacciones). Paso 2: IA genera 5 ideas de posts adaptadas a lo que funcionó, con tono de tu marca (ej: "informal, con emojis, enfocado en emprendedoras latinas"). Paso 3: Si es un producto nuevo, IA usa la descripción del producto de Shopify para generar el copy, hashtags relevantes (no los más genericos, sino los que usa tu audiencia: ej: #AretesDePlataBogota en vez de #Aretes). Paso 4: Envía las ideas a tu Notion para que las revises, o programa directamente en Buffer. Ejemplo real: Una startup de café sostenible en Perú que usó este flujo y aumentó su publicación de 2 posts a la semana a 5, sin invertir más de 30 minutos a la semana en crear ideas.

Tercer ejemplo: Calificación Automática de Leads (para startups de servicios, SaaS, asesorías). Los emprendedores pierden mucho tiempo hablando con leads que no son calificados (ej: alguien que pregunta por un servicio de $1000 pero solo tiene presupuesto de $100). Este flujo usa IA para calificar leads sin que tu hables con ellos. Trigger: Cuando un lead llena un formulario de contacto en tu página web (o envía un mensaje por LinkedIn). Paso 1: IA lee las respuestas del formulario (o el mensaje de LinkedIn) y extrae datos clave: Presupuesto, Necesidad (ej: "quiero automatizar atención al cliente"), Plazo, Tamaño de empresa. Paso 2: IA califica el lead como "Caliente" (presupuesto suficiente, necesidad clara, plazo inmediato), "Tibio" (necesidad clara pero presupuesto bajo), "Frío" (no es tu audiencia). Paso 3: Si es Caliente, envía un enlace de Calendly para agendar una llamada con el equipo de ventas, y envía un correo a tu jefe de ventas con los datos del lead. Si es Tibio, envía un correo con un contenido gratuito (ej: guía de automatización para emprendedores) para nutrirlo. Si es Frío, envía un mensaje de agradecimiento y lo agrega a tu lista de correos para newsletters ocasionales. Ejemplo real: Una startup de asesorías financieras para emprendedores en México que usó este flujo y redujo el tiempo de calificación de leads de 2 horas por lead a 0, y aumentó la tasa de cierre de 10% a 25% porque solo hablaban con leads calientes.

Luego, Ejercicio Práctico Paso a Paso: Tiene que ser PARA NO TÉCNICOS, SIN CÓDIGO, usando herramientas GRATUITAS, y que el emprendedor pueda hacer en 30 minutos. El objetivo del ejercicio: Crear un flujo de AUTOMATIZACIÓN DE ATENCIÓN AL CLIENTE BÁSICA para WhatsApp Business, usando N8N (plan free) y ChatGPT (plan free o $5/mes, pero se puede usar el API gratis con créditos iniciales). Pasos detallados, sin jerga:

Paso 1: Preparar las herramientas (gratis):
- Crear cuenta en N8N Cloud: https://n8n.io/cloud/ (plan free: 5 flujos, 1000 ejecuciones al mes, suficiente para emprendedores)
- Crear cuenta en OpenAI: https://platform.openai.com/ (obtener API Key: hay créditos gratuitos para nuevos usuarios por 3 meses)
- Tener WhatsApp Business (gratis, ya lo usan la mayoría de emprendedores latinos)

Paso 2: Configurar el TRIGGER (lo que activa el flujo) en N8N:
- Abrir N8N, hacer clic en "Crear Flujo Nuevo"
- Buscar el nodo "WhatsApp Business" (no es WhatsApp personal, es Business, pero es gratis)
- Seleccionar el Trigger: "Cuando llegue un mensaje nuevo"
- Conectar N8N con WhatsApp Business: seguir los pasos de N8N (escanear código QR con WhatsApp Business, como cuando conectas WhatsApp Web)

Paso 3: Agregar el nodo de IA (ChatGPT) para CLASIFICAR el mensaje:
- Hacer clic en el signo + después del nodo WhatsApp
- Buscar "OpenAI" → seleccionar nodo "ChatGPT"
- Configurar el nodo:
  - API Key: pegar la que obtuviste de OpenAI
  - Modelo: gpt-3.5-turbo (más barato, suficiente para esto)
  - Prompt (lo que