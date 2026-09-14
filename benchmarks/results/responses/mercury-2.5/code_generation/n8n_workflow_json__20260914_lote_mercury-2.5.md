# Mercury 2.5 — code_generation/n8n_workflow_json

- model_id: `inception/mercury-2.5`
- success: True  | final: 7.84 | quality: 8.0
- latency_total: 5.378s | tokens_per_second: 598.2
- input_tokens: 108 | output_tokens: 3217
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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
  "name": "Clasificador de Mensajes AI",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "submit-message",
        "responseMode": "lastNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ],
      "id": "webhook-node-id",
      "name": "Webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-id",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-id",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [
        480,
        300
      ],
      "id": "extract-fields-id",
      "name": "Extraer Datos"
    },
    {
      "parameters": {
        "operation": "text",
        "model": "text-davinci-003",
        "prompt": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Responde solo con la palabra.",
        "options": {
          "temperature": 0
        }
      },
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.3,
      "position": [
        720,
        300
      ],
      "id": "ai-classify-id",
      "name": "Clasificar IA",
      "credentials": {
        "openAiApi": {
          "id": "12345",
          "name": "OpenAI Credentials"
        }
      }
    },
    {
      "parameters": {
        "destinationField": "classification",
        "valueField": "text"
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [
        950,
        300
      ],
      "id": "extract-classification-id",
      "name": "Extraer Clasificación"
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "operation": "equal",
              "value": "soporte"
            },
            {
              "operation": "equal",
              "value": "ventas"
            },
            {
              "operation": "equal",
              "value": "otro"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        1180,
        300
      ],
      "id": "router-id",
      "name": "Enrutar"
    },
    {
      "parameters": {
        "operation": "postMessage",
        "channel": "#support",
        "text": "Nuevo mensaje de soporte: {{ $json.message }}. Email: {{ $json.email }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1.3,
      "position": [
        1400,
        200
      ],
      "id": "slack-support-id",
      "name": "Slack Soporte",
      "credentials": {
        "slackOAuth2Api": {
          "id": "67890",
          "name": "Slack Credentials"
        }
      }
    },
    {
      "parameters": {
        "operation": "postMessage",
        "channel": "#sales",
        "text": "Nuevo lead de ventas: {{ $json.message }}. Email: {{ $json.email }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1.3,
      "position": [
        1400,
        300
      ],
      "id": "slack-sales-id",
      "name": "Slack Ventas",
      "credentials": {
        "slackOAuth2Api": {
          "id": "67890",
          "name": "Slack Credentials"
        }
      }
    },
    {
      "parameters": {
        "operation": "postMessage",
        "channel": "#general",
        "text": "Mensaje general: {{ $json.message }}. Email: {{ $json.email }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1.3,
      "position": [
        1400,
        400
      ],
      "id": "slack-general-id",
      "name": "Slack General",
      "credentials": {
        "slackOAuth2Api": {
          "id": "67890",
          "name": "Slack Credentials"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
      "main": [
        [
          {
            "node": "Clasificar IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar IA": {
      "main": [
        [
          {
            "node": "Extraer Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Clasificación": {
      "main": [
        [
          {
            "node": "Enrutar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
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
  },
  "settings": {
    "saveManualExecutions": true,
    "executionOrder": "parallel"
  }
}
```