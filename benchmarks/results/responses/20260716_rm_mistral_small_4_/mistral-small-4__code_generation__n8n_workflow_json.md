# Mistral Small 4 — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 8.01 | quality: 8.6
- latency_total: 10.213s | tokens_per_second: 196.4
- input_tokens: 132 | output_tokens: 2006
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un uso adecuado de los nodos de N8N y la API de OpenAI, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

## Respuesta completa

Aquí tienes el workflow completo en JSON para n8n que cumple con los requisitos que mencionas:

```json
{
  "name": "Clasificación de mensajes con IA y envío a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook-clasificacion",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    {
      "parameters": {
        "functionCode": "const { email, message } = items[0].json;\n\nreturn [\n  {\n    json: {\n      email,\n      message,\n      classification: null\n    }\n  }\n];"
      },
      "id": "extract-data-node",
      "name": "Extraer email y mensaje",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "functionCode": "const { message } = items[0].json;\n\n// Usamos OpenAI para clasificar el mensaje\nconst classification = await this.helpers.httpRequest({\n  method: 'POST',\n  url: 'https://api.openai.com/v1/chat/completions',\n  headers: {\n    'Authorization': `Bearer ${$credentials.apiKey}`,\n    'Content-Type': 'application/json'\n  },\n  body: {\n    model: 'gpt-3.5-turbo',\n    messages: [\n      {\n        role: 'system',\n        content: 'Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\". Solo responde con una de estas tres opciones. No añadas nada más.'\n      },\n      {\n        role: 'user',\n        content: message\n      }\n    ]\n  }\n});\n\nconst response = JSON.parse(classification.body);\nconst classificationResult = response.choices[0].message.content.trim().toLowerCase();\n\nreturn [\n  {\n    json: {\n      ...items[0].json,\n      classification: classificationResult\n    }\n  }\n];"
      },
      "id": "ai-classification-node",
      "name": "Clasificar con IA",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": {
          "id": "openai-credentials",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "support-condition-node",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "sales-condition-node",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 400]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}",
        "additionalFields": {}
      },
      "id": "support-slack-node",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 100],
      "credentials": {
        "slackApi": {
          "id": "slack-credentials",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}",
        "additionalFields": {}
      },
      "id": "sales-slack-node",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 300],
      "credentials": {
        "slackApi": {
          "id": "slack-credentials",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje no clasificado:\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}\n\n**Clasificación:** {{$json.classification}}",
        "additionalFields": {}
      },
      "id": "general-slack-node",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 500],
      "credentials": {
        "slackApi": {
          "id": "slack-credentials",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer email y mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y mensaje": {
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
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es soporte?": {
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
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es ventas?": {
      "main": [
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1.0.0",
  "meta": {
    "templateCredsSetupCompleted": false
  }
}
```

### Instrucciones importantes:

1. **Credenciales necesarias**:
   - Debes configurar las credenciales de OpenAI (API Key) en n8n
   - Debes configurar las credenciales de Slack (Token de API) en n8n

2. **Personalización**:
   - Asegúrate de que los canales de Slack (#support, #sales, #general) existan en tu workspace
   - Puedes ajustar el mensaje que se envía a Slack modificando el texto en los nodos de Slack

3. **Clasificación con IA**:
   - El nodo de IA usa GPT-3.5-turbo para clasificar los mensajes
   - El prompt está configurado para responder solo con "soporte", "ventas" o "otro"

4. **Webhook**:
   - El endpoint del webhook será `https://tu-instancia.n8n.cloud/webhook/webhook-clasificacion`
   - Puedes cambiar el path (`webhook-clasificacion`) si lo deseas

5. **Activación**:
   - El workflow está configurado como `active: false` por defecto, así que debes activarlo manualmente en n8n

Este workflow sigue el flujo que solicitaste: webhook → extracción de datos → clasificación con IA → enrutamiento a Slack según la clasificación.