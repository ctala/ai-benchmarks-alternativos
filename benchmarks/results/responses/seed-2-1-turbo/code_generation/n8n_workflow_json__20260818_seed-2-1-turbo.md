# Seed 2.1 Turbo — code_generation/n8n_workflow_json

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.15 | quality: 8.0
- latency_total: 35.752s | tokens_per_second: 57.3
- input_tokens: 168 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow.


## Respuesta completa


El usuario pide un workflow de n8n en JSON que cumpla 4 requisitos: webhook POST, the remaining three requirements are extracting email and message, classifying via OpenAI, and routing to Slack by category. I'll first set up the POST webhook with an auto-200 response, then use gpt-3.5-turbo to return only the category for subsequent routing.

The prompt for the OpenAI node will be strictly defined to return only one of the three specified categories without extra text. A Switch node will be used for multi-path routing, with three corresponding Slack nodes set up to send categorized messages to relevant channels. I'll also add detailed configuration instructions for users to input their OpenAI and Slack credentials and set the correct webhook path.

It has been confirmed that the OpenAI node will reference the email and message fields from the webhook request body, and the Switch node will evaluate the trimmed content of the OpenAI response.

To ensure the Slack nodes can correctly access the original email and message data from the webhook, I've confirmed we can directly reference the webhook node's data in both the OpenAI prompt and Slack message templates, avoiding data loss risks from payload modifications or intermediate processing. I've also finalized the configuration of the first two workflow nodes: the webhook will use the path /mensaje-entrada, return 200 OK automatically, and the OpenAI node will adopt gpt-3.5-turbo with a strict classification prompt that only outputs one of the three specified categories without extra text.

The Switch node will evaluate the trimmed OpenAI response content to route requests to three corresponding Slack channels: support, sales, and general. All Slack messages will directly reference the original webhook data to ensure information accuracy. The workflow will follow n8n's standard JSON structure, and no additional webhook response configuration is needed by default.

I've added relevant configuration reminders: OpenAI and Slack credentials cannot be included in the workflow JSON, and users need to configure them in their n8n instance. I've also compiled five usage notes covering credential setup, request specifications, model adjustment, Slack message customization and workflow testing.

The connection logic between workflow nodes and the exact configuration of the Switch node's three routing paths have been confirmed, and the JSON will be built step by step.

I'm building the workflow JSON step by step. The basic structure of the n8n workflow has been confirmed, with the webhook node already defined with the specified path and POST method, and the OpenAI node configured with the required strict classification prompt. The content is truncated at the OpenAI node's message array definition.
