# Grok 4.3 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 20.804s | tokens_per_second: 105.3
- input_tokens: 244 | output_tokens: 2190

## Respuesta completa

```json
{
  "name": "Clasificador de Mensajes - Webhook a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de estas tres categorías: \"soporte\", \"ventas\" o \"otro\". Responde SOLO con una de estas tres palabras en minúsculas, sin texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-classifier",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openai",
      "typeVersion": 1,
      "position": [480, 300],
      "credentials": {
        "openAiApi": {
          "id": "openai-cred",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "value": "={{ $json.message.content.trim().toLowerCase() }}",
        "toJson": true
      },
      "id": "extract-category",
      "name": "Extraer Categoría",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [700, 300]
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "output": 0,
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.value }}",
                    "operation": "equals",
                    "value2": "soporte"
                  }
                ]
              }
            },
            {
              "output": 1,
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.value }}",
                    "operation": "equals",
                    "value2": "ventas"
                  }
                ]
              }
            },
            {
              "output": 2,
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.value }}",
                    "operation": "equals",
                    "value2": "otro"
                  }
                ]
              }
            }
          ]
        },
        "options": {}
      },
      "id": "switch-router",
      "name": "Switch por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [920, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 *Nuevo mensaje de soporte*\n*Email:* {{ $('Webhook').item.json.email }}\n*Mensaje:* {{ $('Webhook').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1160, 180],
      "credentials": {
        "slackApi": {
          "id": "slack-cred",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nuevo mensaje de ventas*\n*Email:* {{ $('Webhook').item.json.email }}\n*Mensaje:* {{ $('Webhook').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1160, 300],
      "credentials": {
        "slackApi": {
          "id": "slack-cred",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📬 *Mensaje general*\n*Email:* {{ $('Webhook').item.json.email }}\n*Mensaje:* {{ $('Webhook').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1160, 420],
      "credentials": {
        "slackApi": {
          "id": "slack-cred",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "options": {
          "responseData": "{\n  \"status\": \"ok\",\n  \"categoria\": \"{{ $('Extraer Categoría').item.json.value }}\"\n}"
        }
      },
      "id": "respond-webhook",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1160, 540]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Extraer Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Categoría": {
      "main": [
        [
          {
            "node": "Switch por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por Categoría": {
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
    },
    "Enviar a #support": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enviar a #sales": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enviar a #general": {
      "main": [
        [
          {
            "node": "Responder Webhook",
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
  "versionId": "1",
  "meta": {
    "templateCredsSetupCompleted": true
  },
  "id": "workflow-clasificador-mensajes"
}
```