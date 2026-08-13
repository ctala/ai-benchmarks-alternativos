# DeepSeek V4 Flash 0731 — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 7.49 | quality: 8.0
- latency_total: 97.323s | tokens_per_second: 51.7
- input_tokens: 126 | output_tokens: 5033
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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

```json
{
  "name": "Clasificar mensaje y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [0, 0]
    },
    {
      "parameters": {
        "assign": [
          {
            "name": "email",
            "value": "={{ $json.body.email }}",
            "type": "string"
          },
          {
            "name": "message",
            "value": "={{ $json.body.message }}",
            "type": "string"
          }
        ],
        "options": {}
      },
      "id": "set-extract",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [200, 0]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde solo con la palabra exacta."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "passThrough": true
        }
      },
      "id": "openai-node",
      "name": "Clasificar con IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [400, 0]
    },
    {
      "parameters": {
        "assign": [
          {
            "name": "classification",
            "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
            "type": "string"
          }
        ],
        "options": {}
      },
      "id": "set-classification",
      "name": "Extraer clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [600, 0]
    },
    {
      "parameters": {
        "dataPropertyName": "classification",
        "rules": [
          {
            "type": "string",
            "value1": "soporte",
            "value2": ""
          },
          {
            "type": "string",
            "value1": "ventas",
            "value2": ""
          },
          {
            "type": "string",
            "value1": "otro",
            "value2": ""
          }
        ],
        "outputType": "single",
        "options": {}
      },
      "id": "switch-node",
      "name": "Enrutar por clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [800, 0]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 Email: {{ $json.email }}\n📝 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1000, -200]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📧 Email: {{ $json.email }}\n📝 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1000, 0]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📧 Email: {{ $json.email }}\n📝 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1000, 200]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
      "main": [
        [
          {
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Extraer clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer clasificación": {
      "main": [
        [
          {
            "node": "Enrutar por clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por clasificación": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```