# KAT Coder Air v2.5 — code_generation/n8n_workflow_json

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.72 | quality: 8.2
- latency_total: 12.0s | tokens_per_second: 170.7
- input_tokens: 125 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un workflow de N8N detallado que cumple con los requisitos especificados. La estructura es clara y organizada, lo que facilita su comprensión e implementación. Aunque la profundidad es adecuada, podría haberse beneficiado de más detalles sobre la configuración de los nodos de Slack o la gestión de errores.

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



# Workflow n8n — Clasificación de Mensajes con IA

```json
{
  "name": "Clasificador de Mensajes con IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "authentication": "headerAuth",
        "responseMode": "responseNode",
        "options": {
          "response": {
            "statusCode": 200,
            "body": "={{JSON.stringify({status: 'recibido', email: $json.email, clasificacion: $json.clasificacion, canal: $json.canal})}}"
          }
        }
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-260, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "jsCode": "// Extraer campos del body\nconst body = $json.body || {};\nconst email = body.email || '';\nconst message = body.message || '';\n\nreturn [{\n  json: {\n    email,\n    message,\n    webhookResponse: {}\n  }\n}];"
      },
      "id": "extraer-campos",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [-40, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": "=Clasifica el siguiente mensaje del usuario en una de estas tres categorías: soporte, ventas, otro.\n\nMensaje: {{ $json.message }}\n\nDevuelve ÚNICAMENTE una de estas tres palabras, sin explicaciones adicionales: soporte, ventas o otro.",
        "options": {
          "maxTokens": 20,
          "temperature": 0.2
        }
      },
      "id": "clasificacion-ia",
      "name": "Clasificación IA",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [160, 300],
      "credentials": {
        "openAiApi": {
          "type": "openAiApi",
          "id": "openai-credentials-id"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Limpiar la respuesta de la IA (quitar comillas, espacios, etc.)\nlet categoria = $json.completion || '';\ncategoria = categoria.trim().toLowerCase();\n\n// Normalizar\nif (categoria.includes('soporte')) {\n  categoria = 'soporte';\n} else if (categoria.includes('ventas')) {\n  categoria = 'ventas';\n} else {\n  categoria = 'otro';\n}\n\nreturn [{\n  json: {\n    email: $json.email,\n    message: $json.message,\n    clasificacion: categoria\n  }\n}];"
      },
      "id": "normalizar-categoria",
      "name": "Normalizar Categoría",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [360, 300]
    },
    {
      "parameters": {
        "rule": {
          "interval": [
            { "field": "combination", "matching": "any", "conditions": [] }
          ],
          "conditions": {
            "options": { "caseSensitive": true, "leftValue": "", "typeValidation": "strict" },
            "conditions": [
              {
                "id": "cond-soporte",
                "leftValue": "={{ $json.clasificacion }}",
                "rightValue": "soporte",
                "operator": { "type": "string", "operation": "equals" }
              }
            ],
            "combinator": "and"
          }
        },
        "options": {}
      },
      "id": "router",
      "name": "Router",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [560, 300]
    },
    {
      "parameters": {
        "channelId": "#support",
        "text": "=📧 *Nuevo mensaje de Soporte*\n\n👤 *Email:* {{ $json.email }}\n💬 *Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-soporte",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [760, 180],
      "credentials": {
        "slackApi": {
          "type": "slackApi",
          "id": "slack-credentials-id"
        }
      }
    },
    {
      "parameters": {
        "channelId": "#sales",
        "text": "=📧 *Nuevo mensaje de Ventas*\n\n👤 *Email:* {{ $json.email }}\n💬 *Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-ventas",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [760, 300],
      "credentials": {
        "slackApi": {
          "type": "slackApi",
          "id": "slack-credentials-id"
        }
      }
    },
    {
      "parameters": {
        "channelId": "#general",
        "text": "=📧 *Nuevo mensaje (Otro)*\n\n👤 *Email:* {{ $json.email }}\n💬 *Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [760, 420],
      "credentials": {
        "slackApi": {
          "type": "slackApi",
          "id": "slack-credentials-id"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          {
            "node": "Clasificación IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificación IA": {
      "main": [
        [
          {
            "node": "Normalizar Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Categoría": {
      "main": [
        [
          {
            "node": "Router",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "callerPolicy":