# Gemini 3.1 Flash Lite — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.17 | quality: 7.48
- latency_total: 4.721s | tokens_per_second: 316.9
- input_tokens: 116 | output_tokens: 1496
- judge_score: 3.2 | justificación: 

## Respuesta completa

Para importar este workflow en **n8n**, simplemente copia el código JSON a continuación, ve a tu instancia de n8n, crea un nuevo workflow y pega el código (`Ctrl+V` o `Cmd+V`).

### Consideraciones previas:
1. **Credenciales**: Necesitarás configurar tus credenciales de **OpenAI** (API Key) y de **Slack** (Token de bot) dentro de los nodos correspondientes.
2. **Canales**: Asegúrate de que el bot de Slack tenga permisos para escribir en los canales `#support`, `#sales` y `#general`.

```json
{
  "name": "Clasificador de Emails a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [0, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {
          "systemMessage": "Eres un asistente clasificador. Clasifica el mensaje recibido en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Responde únicamente con la palabra de la categoría."
        },
        "promptType": "define",
        "text": "={{ $json.body.message }}"
      },
      "id": "openai-node",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.4,
      "position": [220, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": false
          },
          "conditions": [
            {
              "leftValue": "={{ $json.output }}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            },
            {
              "leftValue": "={{ $json.output }}",
              "rightValue": "ventas",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "or"
        },
        "looseTypeValidation": false
      },
      "id": "switch-node",
      "name": "Switch Canal",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [440, 300]
    },
    {
      "parameters": {
        "channel": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "={{ 'Nuevo ticket de soporte de: ' + $('Webhook').item.json.body.email + '\\nMensaje: ' + $('Webhook').item.json.body.message }}"
      },
      "id": "slack-support",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [700, 100]
    },
    {
      "parameters": {
        "channel": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "={{ 'Nueva consulta de ventas de: ' + $('Webhook').item.json.body.email + '\\nMensaje: ' + $('Webhook').item.json.body.message }}"
      },
      "id": "slack-sales",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [700, 300]
    },
    {
      "parameters": {
        "channel": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "={{ 'Mensaje general de: ' + $('Webhook').item.json.body.email + '\\nMensaje: ' + $('Webhook').item.json.body.message }}"
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [700, 500]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
      "main": [
        [
          {
            "node": "Switch Canal",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Canal": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Cómo probarlo:
1. **Webhook**: Usa la URL de "Test URL" que te da el nodo Webhook.
2. **Payload de prueba**: Envía un POST (usando Postman o Insomnia) con este formato JSON:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Quiero comprar su producto más caro."
   }
   ```
3. El nodo **OpenAI** clasificará el texto, el **Switch** lo enviará a `#sales` y recibirás el mensaje en Slack.