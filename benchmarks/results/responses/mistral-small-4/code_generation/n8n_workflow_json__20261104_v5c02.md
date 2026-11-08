# Mistral Small 4 — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 6.37 | quality: 6.08
- latency_total: 8.613s | tokens_per_second: 175.9
- input_tokens: 132 | output_tokens: 1515
- judge_score: 2.2 | justificación: 

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

Aquí tienes el JSON completo del workflow de N8N que cumple con los requisitos que especificaste:

```json
{
  "name": "Clasificación de mensajes con IA y envío a Slack",
  "nodes": [
    {
      "parameters": {},
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "message-classification-webhook",
      "onTrigger": true
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"message\"]}}",
              "operation": "contains",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "classification-soporte",
      "name": "Es Soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [450, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"message\"]}}",
              "operation": "contains",
              "value2": "venta"
            }
          ]
        }
      },
      "id": "classification-ventas",
      "name": "Es Ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [450, 400]
    },
    {
      "parameters": {
        "functionCode": "// Clasifica el mensaje usando OpenAI\nconst message = items[0].json.message;\n\nconst classification = await this.helpers.httpRequest({\n  url: 'https://api.openai.com/v1/chat/completions',\n  method: 'POST',\n  headers: {\n    'Authorization': `Bearer {{ $credentials.apiKey }}`,\n    'Content-Type': 'application/json'\n  },\n  body: {\n    model: 'gpt-3.5-turbo',\n    messages: [\n      {\n        role: 'system',\n        content: 'Clasifica el siguiente mensaje como una de estas categorías: soporte, ventas o otro. Solo responde con la categoría sin explicaciones.'\n      },\n      {\n        role: 'user',\n        content: message\n      }\n    ],\n    max_tokens: 10\n  }\n});\n\nconst classificationResult = JSON.parse(classification).choices[0].message.content.trim().toLowerCase();\n\nreturn [{ json: { email: items[0].json.email, message: items[0].json.message, classification: classificationResult } }];"
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "={{ $json.classification === 'soporte' ? '#support' : ($json.classification === 'ventas' ? '#sales' : '#general') }}",
        "text": "Nuevo mensaje recibido:\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}\n\n**Clasificación:** {{$json.classification}}"
      },
      "id": "slack-message",
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [850, 300],
      "credentials": {
        "slackApi": {
          "id": "slack-credentials",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "openai-credentials",
      "name": "OpenAI API",
      "type": "n8n-nodes-base.credentials",
      "typeVersion": 1,
      "position": [650, 200],
      "credentials": {
        "openAiApi": {
          "id": "openai-credentials",
          "name": "OpenAI API"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Es Soporte?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Es Soporte?": {
      "main": [
        [
          {
            "node": "Es Ventas?",
            "type": "main",
            "index": 0
          },
          {
            "node": "Clasificación con IA",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Clasificación con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Es Ventas?": {
      "main": [
        [
          {
            "node": "Clasificación con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificación con IA": {
      "main": [
        [
          {
            "node": "Enviar a Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1.0.0",
  "meta": {
    "templateCredsSetupCompleted": true
  }
}
```

### Instrucciones para su uso:

1. **Credenciales necesarias**:
   - Configura una credencial para Slack (necesitarás un token de bot de Slack con permisos para enviar mensajes)
   - Configura una credencial para OpenAI (necesitarás una API key de OpenAI)

2. **Cómo funciona**:
   - El webhook recibe un POST con body que debe contener `email` y `message`
   - Primero verifica si el mensaje contiene "soporte" o "venta" para casos simples
   - Si no es claro, usa OpenAI para clasificar el mensaje en "soporte", "ventas" o "otro"
   - Envía el mensaje a Slack según la clasificación:
     - soporte → #support
     - ventas → #sales
     - otro → #general

3. **Mejoras posibles**:
   - Podrías ajustar el prompt de OpenAI para mejorar la clasificación
   - Añadir manejo de errores en caso de que OpenAI falle
   - Guardar los mensajes clasificados en una base de datos

El workflow está diseñado para ser robusto pero puedes modificarlo según tus necesidades específicas.