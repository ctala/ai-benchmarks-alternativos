# Tencent Hy3 — startup_content/curso_emprendimiento_modulo

- model_id: `tencent/hy3`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 58.62s | tokens_per_second: 94.2
- input_tokens: 288 | output_tokens: 5522
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando ejemplos prácticos y explicaciones detalladas que un emprendedor podría aplicar directamente.

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

## 1. Objetivo del Módulo
En este módulo, aprenderás a identificar tareas repetitivas en tu día a día empresarial y transformarlas en flujos de trabajo automatizados utilizando Inteligencia Artificial, sin necesidad de saber programar. El objetivo es que al finalizar, seas capaz de diseñar tu primer "robot" interno que ahorre tiempo, reduzca errores humanos y permita que tu startup opere de manera más eficiente y escalable, usando herramientas accesibles y de bajo costo, ideales para la realidad del mercado latinoamericano.

---

## 2. Contenido Teórico: Automatización con IA al alcance de todos

### ¿Qué es la automatización con IA?
Imagina que tienes un asistente virtual que nunca duerme. La **automatización** es simplemente conectar dos o más aplicaciones para que "hablen" entre sí y realicen una tarea solas. Por ejemplo: *cuando llegue un correo, guárdalo en una hoja de cálculo*. 
La **IA (Inteligencia Artificial)** le da "cerebro" a esa automatización. Ya no solo sigues reglas fijas, sino que la IA puede *entender* el texto, *clasificarlo* o *redactar* una respuesta. 

### Herramientas No-Code: Conoce N8N
Para lograr esto sin escribir una línea de código, usamos plataformas de automatización visual. Existen opciones como Zapier o Make, pero en este curso nos enfocamos en **N8N** (pronunciado "n-eight-n"). 
N8N es una herramienta donde arrastras y sueltas bloques (llamados *nodos*) para crear un diagrama de flujo. Es de código abierto (*open-source*), lo que significa que tiene un costo mucho menor que sus competidores, perfecto para emprendedores latinos que buscan maximizar su presupuesto. Con N8N puedes conectar tu WhatsApp Business, Google Sheets, tu correo y la API de ChatGPT para crear soluciones a la medida.

---

## 3. 3 Ejemplos Prácticos de Automatización para Startups

### Ejemplo 1: Atención al cliente automatizada (WhatsApp + IA)
* **El problema:** Recibes decenas de mensajes por WhatsApp y tardas horas en responder preguntas frecuentes, perdiendo ventas.
* **La solución:** Un flujo en N8N que recibe el mensaje de WhatsApp, lo envía a la IA para que identifique la intención (ej. "quiere precio", "tiene una queja"). Si es una pregunta frecuente, la IA responde sola. Si es complejo, la IA crea un ticket en Trello o Notion y te avisa en tu canal de Slack o Telegram.

### Ejemplo 2: Generación de contenido para redes sociales
* **El problema:** Sabes que debes estar en Instagram y LinkedIn, pero te falta tiempo para crear posts constantes.
* **La solución:** Un flujo que toma palabras clave que escribiste en un Google Sheet, le pide a ChatGPT que redacte 3 variantes de posts con tu "tono de voz" (ej. divertido, profesional), y las guarda en una base de datos para que solo tengas que dar "click a publicar".

### Ejemplo 3: Calificación automática de leads (Lead Scoring)
* **El problema:** Llenan tu formulario de contacto, pero no sabes quién es un cliente real con presupuesto y quién solo curiosea.
* **La solución:** Cuando alguien llena el formulario, N8N toma sus respuestas, se las pasa a la IA con la instrucción: *"Califica este lead del 1 al 10 según el presupuesto y la urgencia"*. Luego, la IA escribe "Caliente" o "Fría" en tu hoja de cálculo de CRM, permitiéndote enfocarte solo en los clientes que cierran ventas.

---

## 4. Ejercicio Práctico Paso a Paso: Crea tu "Robot Calificador de Leads"

Vamos a construir el **Ejemplo 3** usando N8N Cloud (tiene un periodo de prueba gratis y no requiere instalación en tu computadora).

**Paso 1: Preparación (10 min)**
1. Crea una cuenta gratis en [N8N Cloud](https://n8n.io/).
2. Crea una cuenta en [OpenAI](https://platform.openai.com/) y genera una "API Key" (piensa en esto como una contraseña que le das a N8N para que hable con ChatGPT).
3. Abre Google Sheets y crea una hoja llamada "Leads" con las columnas: `Nombre`, `Mensaje`, `Calificacion_IA`.

**Paso 2: Inicia el flujo en N8N**
1. En N8N, haz clic en "+ Nuevo Flujo" y nómbralo "Calificador de Leads".
2. Arrastra el nodo **Manual Trigger** (para probar el flujo a mano sin esperar datos reales).
3. Añade un nodo **Google Sheets** (acción: "Get Row" o "Obtener fila") para leer los datos de tu hoja.

**Paso 3: Conecta el "Cerebro" (OpenAI)**
1. Arrastra un nodo **OpenAI** (Chat Model) y conéctalo al nodo anterior.
2. Pega tu API Key en las credenciales.
3. En el campo "Prompt" (instrucción), escribe: 
   > *"Analiza el siguiente mensaje de un lead: {{ $json.Mensaje }}. Responde solo con la palabra 'Caliente' si tiene intención de compra, o 'Fría' si es spam o duda general."*

**Paso 4: Guarda el resultado**
1. Añade otro nodo **Google Sheets** (acción: "Update Row" o "Actualizar fila").
2. Configúralo para que escriba la respuesta de la IA en la columna `Calificacion_IA` de la fila correspondiente.

**Paso 5: ¡Pruébalo!**
1. Haz clic en **"Execute Workflow"** (Ejecutar flujo). 
2. Revisa tu Google Sheet: ¡La columna de calificación se habrá llenado sola con la decisión de la IA!

---

## 5. Recursos Adicionales
* **Plantillas Gratis de N8N:** Explora la [biblioteca de plantillas](https://n8n.io/workflows/) (busca "AI" y "WhatsApp" para inspirarte).
* **Comunidad:** Únete a grupos de Facebook o Discord de "No-Code Latam" para ver cómo otros emprendedores resuelven problemas similares.
* **Guía de Prompts:** Descarga nuestra hoja de cálculo "Prompts listos para automatizar tu startup" (disponible en el aula).
* **Video Tutorial:** "Cómo conectar WhatsApp Business a N8N paso a paso" (Enlace en la barra lateral del curso).

---

## 6. Preguntas de Autoevaluación
1. **Comprensión:** ¿Qué diferencia hay entre una automatización tradicional (reglas fijas) y una automatización potenciada con IA en el contexto de una startup?
2. **Aplicación:** Menciona 2 tareas repetitivas específicas de *tu* emprendimiento que podrías automatizar hoy usando los ejemplos vistos en este módulo.
3. **Análisis:** Si tuvieras un presupuesto muy limitado, ¿por qué N8N sería una mejor opción que herramientas de pago mensual fijo como Zapier para un emprendedor latinoamericano?