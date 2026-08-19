# Claude Opus 5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.51 | quality: 6.3
- latency_total: 23.942s | tokens_per_second: 85.5
- input_tokens: 175 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta describe adecuadamente los pasos para crear el flujo de trabajo, pero carece de un JSON específico y detallado, lo que limita su precisión y utilidad práctica.

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

I'm building a complete n8n workflow JSON that starts with a webhook to receive POST requests, then extracts the email and message data, passes it through OpenAI for classification, uses a switch node to route based on the classification result, and finally sends the output to different Slack channels depending on the category. Writing the OpenAI node configuration... I need to handle the different output shapes from n8n's OpenAI node depending on whether JSON output is enabled, so I'm adding a normalization step using a Code node that safely extracts the categoria field regardless of the structure, then validates it against the allowed values. Writing the switch node config...…