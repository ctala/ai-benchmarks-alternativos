# Qwen 3-Next 80B Thinking (NIM) — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 18.582s | tokens_per_second: 110.2
- input_tokens: 253 | output_tokens: 2048
- judge_score: 4.2 | justificación: 

## Respuesta completa

Okay, I need to design Module 3 for the "IA Practica para Emprendedores" course. The title is "Automatización con IA: De la idea al flujo de trabajo". Let me break down the requirements.

First, the objective. It should be one paragraph. It needs to state what the module aims to achieve. Since it's for Latin American entrepreneurs, focus on practical, hands-on skills. Maybe something like enabling them to automate workflows using AI tools without technical expertise, improving efficiency, reducing costs, etc.

Next, theoretical content. Explain automation with AI, mentioning tools like n8n. Need to keep it simple, non-technical. Define what automation is, how AI enhances it, maybe compare traditional automation vs AI-driven. Tools like n8n as a no-code platform, maybe mention other tools briefly but focus on n8n since specified.

Then three practical examples for startups: customer service automation, social media content generation, lead scoring. Each example should be specific. For customer service: chatbots using tools like Dialogflow or n8n integrating with WhatsApp. Social media: using AI to generate posts, maybe using Canva or Jasper, but need to tie into n8n workflows. Lead scoring: using AI to analyze leads from forms, maybe integrating with CRM.

Exercise step-by-step. The student should follow along. Maybe a simple n8n workflow. Let's see. For example, setting up a workflow that takes a new lead from a Google Form, processes it with AI (maybe sentiment analysis), then sends a personalized response via email. But the user is non-technical, so need to make sure steps are clear, maybe screenshots would help but since it's markdown, describe the steps clearly.

Resources: links to n8n docs, free tools, maybe some templates. Also maybe YouTube tutorials for Latin American audience.

Self-evaluation questions: 3 questions. Should test understanding of concepts, maybe one on benefits of AI automation, one on a tool mentioned, one on steps in the exercise.

Wait, the user specified "herramientas como N8N", so focus on n8n for the examples and exercise. Maybe the exercise uses n8n to create a workflow. Let's outline each section.

Let me structure each part.

Objective: One paragraph. "En este módulo, aprenderás a implementar soluciones de automatización con IA para optimizar procesos clave de tu startup. Sin necesidad de conocimientos técnicos, entenderás cómo integrar herramientas como n8n para crear flujos de trabajo que ahorren tiempo, reduzcan errores y mejoren la atención al cliente, la generación de contenido y la gestión de leads. Al finalizar, tendrás un flujo de trabajo automatizado listo para aplicar en tu negocio."

Theoretical content: Start by explaining automation with AI. Traditional automation is rule-based, but AI adds learning and adaptability. For example, not just sending a fixed response but analyzing context. Mention n8n as a no-code tool that connects apps via workflows. Maybe a simple diagram description: "n8n funciona como un 'cableado' entre apps: cuando un evento ocurre en una herramienta (ej. nuevo formulario), activa acciones en otras (ej. enviar email, guardar en base de datos)."

Then three examples:

1. Atención al cliente automatizada: Usar n8n para conectar WhatsApp Business con un chatbot de IA (como Dialogflow). Cuando un cliente envía un mensaje, el chatbot responde con información predefinida o deriva a un humano si es complejo. Ejemplo: una tienda online recibe preguntas sobre envíos, el chatbot responde con tiempos de entrega y enlaces a políticas.

2. Generación de contenido para redes sociales: n8n toma datos de un CRM o Google Sheet con temas de productos, usa una herramienta de IA como Jasper para generar posts, y publica en redes via API de Facebook/Instagram. Ejemplo: un café genera posts diarios con descripciones de promociones basadas en ingredientes del día.

3. Calificación automática de leads: Formulario de contacto en sitio web → n8n recibe datos → IA analiza (ej. si es empresa grande, presupuesto, etc.) y asigna puntaje. Si puntaje alto, notifica al equipo de ventas via Slack; si bajo, envía contenido educativo.

Exercise: Step-by-step for one of these. Let's pick the lead scoring example since it's a common need. Steps:

1. Crear un formulario en Google Forms (ej. para captar leads en sitio web).

2. Configurar n8n: create a new workflow.

- Trigger: Google Forms new response.

- Then use a node to process data. Maybe use a "Function" node in n8n to add logic. But since non-technical, maybe use a pre-built template or simpler.

Wait, but n8n might not have built-in AI scoring, so perhaps integrate with another tool like a simple rule-based scoring. Or use a tool like Make.com which has AI nodes, but the user specified n8n. Maybe n8n can connect to an AI API, but that might be too technical.

Alternative: Maybe for the exercise, use a simple rule-based scoring first. For example, if the lead's industry is "tech" and budget > $10k, score high. But the user said "calificacion automatica de leads" using AI. Hmm. Maybe use a simple AI service like a free API for sentiment analysis or something. But perhaps for simplicity, use n8n to route leads based on keywords.

Wait, but the user said "calificacion automatica de leads" with AI. So maybe the exercise should use a tool like a simple AI model. But non-technical, so perhaps use a pre-trained model via an API. For example, using a service like MonkeyLearn for sentiment analysis, but that might be complex.

Alternatively, in the exercise steps, maybe use a simple rule-based approach but explain it as a basic AI automation. Or use n8n's "Webhook" node to send data to an AI service. But maybe for simplicity, the exercise is a basic workflow without actual AI, but the explanation says it's using AI. Maybe the AI part is handled by another tool integrated into n8n.

Wait, the example says "Calificacion automatica de leads" with AI. So perhaps the lead scoring uses an AI model. For example, using a service like Zoho Flow or something, but maybe in the exercise, the steps are:

1. Create a Google Form with fields like industry, budget, company size.

2. In n8n, set up a workflow that triggers on new form response.

3. Use a "HTTP Request" node to send the data to a simple AI API (like a mock API for simplicity) that returns a score.

But since the user is non-technical, maybe the exercise uses a pre-built n8n template that uses an AI service, but the steps would be to copy the template and configure it.

Alternatively, maybe use a service like Zapier with AI actions, but the module is focused on n8n. Hmm.

Alternatively, maybe the exercise uses n8n to connect Google Forms to a spreadsheet, then uses a simple formula to score leads. But that's not AI. Need to tie it to AI.

Wait, maybe in the theoretical part, explain that AI can analyze text for intent, so for example, if the lead's message contains words like "investment" or "partnership", it's a high priority. So in the exercise, the step is to use n8n to check keywords in the lead's response and assign score.

For example:

- When a new form response comes in, check the "message" field for keywords.

- If "investment" or "partner", score 10; else, score 5.

Then send to sales team if score >=8.

So in n8n, the steps would be:

1. Trigger: Google Forms new response.

2. Use a "Function" node to write a simple JavaScript to check keywords.

But for non-technical users, maybe use a "Condition" node in n8n to check for keywords.

Wait, n8n has a "IF" node where you can set conditions. So steps could be:

- After getting the form data, use an IF node to check if the message contains "investment" or "partner".

- If yes, set score to 10; else 5.

Then use another node to send to Slack or email.

But the user is non-technical, so need to describe the steps clearly with screenshots (but since markdown, maybe just describe the steps in simple terms).

Alternatively, use a template from n8n's gallery. But maybe the exercise is to create a simple workflow with n8n using their UI.

Let me outline the exercise steps:

Ejercicio Practico Paso a Paso:

1. Configura un formulario de Google Forms con campos: Nombre, Empresa, Email, Mensaje (para captar leads).

2. Ve a n8n.io y crea una cuenta gratuita.

3. Crea un nuevo flujo (workflow) y selecciona "Google Forms" como trigger. Conecta tu cuenta de Google.

4. En el nodo de Google Forms, selecciona tu formulario recién creado.

5. Añade un nodo "Function" para procesar el mensaje. En el código, escribir algo como:

   if (item.json.message.includes("inversión") || item.json.message.includes("socio")) {
     item.json.score = 10;
   } else {
     item.json.score = 5;
   }

   But since non-technical, maybe use a simpler condition. Alternatively, use