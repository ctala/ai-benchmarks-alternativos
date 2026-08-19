# KAT Coder Pro v2.5 — code_generation/n8n_workflow_json

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 7.27 | quality: 8.0
- latency_total: 18.276s | tokens_per_second: 112.1
- input_tokens: 125 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, siguiendo las instrucciones para crear un flujo de trabajo de N8N con un webhook, clasificación de IA y notificación a Slack. La estructura es clara y práctica, aunque la profundidad podría mejorarse con más detalles sobre la configuración o manejo de errores.

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



{
  "name": "Clasificador de Mensajes con IA y Notificación a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {
          "temperature": 0
        },
        "prompt": "=Clasifica el siguiente mensaje de un cliente en una de estas categorías: \"soporte\", \"ventas\" o \"otro\". Responde SOLO con la categoría, sin explicaciones.\n\nEmail del cliente: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}"
      },
      "id": "openai-node",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "openai-cred-id",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "operation": "contains",
              "value1": "={{ $json.output }}",
              "value2": "soporte",
              "output": "soporte"
            },
            {
              "operation": "contains",
              "value1": "={{ $json.output }}",
              "value2": "ventas",
              "output": "ventas"
            }
          ]
        },
        "fallbackOutput": "otro"
      },
      "id": "switch-node",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=Nuevo mensaje de Soporte:\nDe: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack (Soporte)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1000,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "slack-cred-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=Nuevo mensaje de Ventas:\nDe: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack (Ventas)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1000,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "slack-cred-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=Nuevo mensaje General:\nDe: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack (General)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1000,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "slack-cred-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"status\": \"success\",\n  \"message\": \"Mensaje procesado y enviado a Slack\"\n}"
      },
      "id": "respond-node",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1250,
        300
      ]
    }
  ],
  "pinData": {},
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
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Slack (Soporte)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (Ventas)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (General)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack (Soporte)": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack (Ventas)": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack (General)": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "versionId": "unique-version-id-123",
  "meta": {
    "instanceId": "