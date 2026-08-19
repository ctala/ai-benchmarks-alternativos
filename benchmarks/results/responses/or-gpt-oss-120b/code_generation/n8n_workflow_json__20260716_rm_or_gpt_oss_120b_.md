# GPT-OSS 120B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.12 | quality: 7.0
- latency_total: 12.428s | tokens_per_second: 164.8
- input_tokens: 181 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de detalles sobre la configuración del nodo OpenAI y el nodo Slack, lo que limita su profundidad y utilidad práctica.

## Respuesta completa

Aquí tienes el workflow completo de **n8n** en formato JSON.  
Cumple con los requisitos pedidos:

1. Se activa con un **Webhook POST**.  
2. Extrae los campos `email` y `message` del body.  
3. Usa el nodo **OpenAI** para clasificar el mensaje en *soporte*, *ventas* o *otro*.  
4. Según la clasificación, envía un mensaje a Slack al canal correspondiente (`#support`, `#sales` o `#general`).

```json
{
  "name": "Webhook → OpenAI classification → Slack routing",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "receive"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "{{YOUR_WEBHOOK_ID}}"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json[\"email\"]}}"
            },
            {
              "name": "message",
              "value": "={{$json[\"message\"]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Extract fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2