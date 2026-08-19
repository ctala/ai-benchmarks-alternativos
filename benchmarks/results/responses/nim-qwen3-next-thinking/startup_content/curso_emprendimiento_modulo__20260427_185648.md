# Qwen 3-Next 80B Thinking (NIM) — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.44 | quality: 6.96
- latency_total: 21.325s | tokens_per_second: 96.0
- input_tokens: 253 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

Okay, I need to design Module 3 for the "IA Práctica para Emprendedores" course. The title is "Automatización con IA: De la idea al flujo de trabajo". Let me break down the requirements.

First, the objective of the module should be one paragraph. It needs to state what the module aims to teach. Since it's for non-technical entrepreneurs, the objective should focus on practical skills, how automation with AI can save time, reduce errors, and scale operations. Maybe mention tools like n8n, Zapier, etc., but the main tool here is n8n as per the example.

Next, theoretical content. Explain what AI automation is, how it works, maybe differentiate between simple automation and AI-driven automation. Mention tools like n8n, but also perhaps others like Zapier or Make (formerly Integromat), but the example specifies n8n. So explain n8n as a no-code tool, open-source, connects apps, workflows, maybe some basics of how it works with triggers and actions.

Then three practical examples for startups:

1. Automated customer service: Maybe using chatbots for FAQs, integrating with WhatsApp or email, using something like n8n to route messages to a chatbot, then if it's a complex issue, escalate to human. But need to be specific. Maybe a workflow where incoming messages on social media are checked by a chatbot, if it's a common question, answer directly, else send to a human team.

2. Social media content generation: Using AI to generate posts, maybe using tools like Canva or Copy.ai, but integrating with n8n. For example, when a new product is added to a database, n8n triggers an AI tool to create a social media post, then schedules it via Buffer or Hootsuite.

3. Automatic lead qualification: When a lead fills out a form, n8n checks their answers against criteria (like budget, company size), scores them, then sends high-scoring leads to sales team, low to nurture campaigns. Maybe using a simple scoring system based on form responses.

Then a step-by-step exercise. The user should follow along. Let's pick one of the examples, maybe the customer service one. Steps: sign up for n8n, connect a messaging platform (like WhatsApp via Twilio), set up a chatbot using an AI service like Dialogflow or a simple rule-based bot. But wait, n8n might not directly integrate with Dialogflow, but maybe use an API. Alternatively, for simplicity, use a basic rule-based system where if the message contains certain keywords, reply with a predefined answer.

But the user is non-technical, so maybe use n8n with a simple HTTP request to a chatbot API, but perhaps that's too complex. Alternatively, use a no-code tool that's simpler. Wait, the module is about n8n, so the exercise should use n8n.

Let me think of a step-by-step for customer service automation. For example, using n8n to monitor a Google Form or a WhatsApp number, then if the message is about "hours", reply with business hours. Steps: create a n8n account, set up a webhook trigger (for incoming messages), then check the message content, if it contains certain words, send a response.

But how to handle incoming messages? Maybe using Twilio for WhatsApp, but that might require a paid account. Alternatively, use a simple form submission. Maybe the exercise uses Google Forms and n8n to respond automatically. But maybe better to use a social media platform. Alternatively, use a simple email trigger.

Alternatively, use a free service like Google Sheets as a trigger. For example, when a new row is added to a Google Sheet (simulating a new message), n8n checks the message and replies. But for a customer service example, perhaps using a tool like Airtable or a simple form.

Wait, maybe the exercise is to set up a basic workflow where when someone submits a form (like via Typeform or Google Forms), n8n checks the response and sends an automated reply. But that's more of a form response, not customer service. Maybe better to use a real-time chat.

Alternatively, for simplicity, the exercise could be: set up n8n to send a welcome message when a new subscriber joins a mailing list (Mailchimp). But that's more basic automation. But the example should be about customer service.

Hmm. Let's see. Let's say the exercise is: Automate the process where when a customer sends a message via WhatsApp to your business number, n8n checks if the message is "hours" and replies with business hours. Steps:

1. Sign up for n8n.cloud (free tier).

2. Connect Twilio to n8n for WhatsApp.

3. Create a workflow: Trigger when a new message comes in via Twilio.

4. Add a node to check the message content. If it contains "hours", then send a reply with business hours.

But the user might not have a Twilio account, but maybe the exercise can use a free alternative. Alternatively, use a mock trigger in n8n, like a manual trigger, but that's not real-world. Maybe the exercise uses a Google Sheets trigger where a new row is added, and then n8n processes it. But for customer service, perhaps using a Google Form submission.

Alternatively, use a free tool like Zapiet or something else, but the module is supposed to use n8n. Let's proceed with Twilio, but note that the user needs a Twilio account, which has costs. Maybe the exercise uses a free trial, but that's a bit of a hurdle. Alternatively, for simplicity, use a webhook that can be triggered by a simple HTTP request, and simulate the message input.

But for a non-technical entrepreneur, the steps need to be very clear. Maybe the exercise is to set up a basic workflow using n8n's built-in triggers and actions, like using the "Webhook" node to receive data, then a "Function" node to check the content, then send a response via email or another webhook.

Wait, the exercise should be something that can be done without complex integrations. Maybe using Google Sheets and n8n to automate a simple response. Let's outline:

Exercise: Automate responses to customer inquiries via email.

Steps:

1. Create a new workflow in n8n.

2. Add a trigger node: "HTTP Request" (Webhook) to receive email submissions. Wait, but how to get emails into n8n? Maybe use a service like Gmail via Zapier, but that complicates. Alternatively, use a Google Form that sends responses to a Google Sheet, then n8n monitors the sheet.

Alternative plan for the exercise:

Step 1: Create a Google Sheet with columns for "Email", "Query", "Response".

Step 2: Set up a Google Form that submits to the sheet.

Step 3: In n8n, create a workflow that triggers when a new row is added to the Google Sheet.

Step 4: Check the "Query" column for keywords like "hours", "price", etc.

Step 5: If "hours", set response to business hours; if "price", set to product prices.

Step 6: Send the response via email using Gmail node.

But to do this, the user needs to set up Google Sheets and Gmail in n8n.

But the user is non-technical, so instructions need to be very clear, step-by-step, with screenshots or references to where to click.

But since this is a text-based markdown, we can't include screenshots, but we can describe the steps clearly.

So for the exercise:

- Create a Google Sheet with columns for Email, Query, Response.

- Set up a Google Form linked to the sheet.

- In n8n, create a new workflow.

- Add a Google Sheets node as trigger for "New Row" in the sheet.

- Then add a "Function" node to check the Query.

- If Query contains "hours", set Response to "Our hours are 9 AM - 6 PM".

- Then add a Gmail node to send the response to the Email address.

But how to configure the Gmail node? Maybe use OAuth, but that's a bit technical. Alternatively, use a service like SMTP.

But maybe the exercise is simpler: using a basic automation where when a new entry is added to a sheet, it sends a predefined response. But perhaps for simplicity, the exercise could be about social media content generation using n8n and an AI tool like Copy.ai.

For example:

1. When a new product is added to a Google Sheet, trigger n8n to use Copy.ai to generate a social media post.

But again, requires integrating Copy.ai API.

Alternatively, use a simpler method. Maybe the exercise is to create a workflow where n8n takes a prompt from a Google Form, sends it to an AI service (like OpenAI via API), and then posts the result to Twitter.

But the user needs to have API keys for OpenAI, which might be a barrier. However, the module could mention that they need to sign up for those services, but keep the steps simple.

Alternatively, for the exercise, use n8n's built-in nodes to create a simple workflow without external services. But n8n requires integrations to do much.

Hmm. Maybe the best approach is to outline the steps for a customer service automation using Twilio and a simple rule-based response, even if it requires signing up for Twilio. The steps would be:

1. Sign up for a Twilio account and get a WhatsApp number.

2. In n8n, add the Twilio node and authenticate with your Twilio credentials.

3. Create a workflow with a Twilio trigger for incoming messages.

4. Add a "Function" node to check if the message