# Grok 4.3 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.3 | quality: 8.0
- latency_total: 11.669s | tokens_per_second: 170.8
- input_tokens: 305 | output_tokens: 1993
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del flujo de trabajo, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores.

## Respuesta completa

```json
{
  "name": "Clasificador Webhook → OpenAI → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook-clasificador",
        "responseMode": "responseNode"
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu única tarea es devolver exactamente una de estas tres palabras: soporte, ventas u otro. No agregues explicaciones ni texto adicional."
            },
            {
              "role": "user",
              "content": "Clasifica el siguiente mensaje:\n\n{{ $('Webhook').item.json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openai",
      "typeVersion": 1.1,
      "position": [480, 300],
      "credentials": {
        "openAiApi": {
          "id": "your-openai-credential-id",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
      },
      "id": "extract-class",
      "name": "Extraer Clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [700, 300]
    },
    {
      "parameters": {
        "rules": {
          "string": [
            {
              "value": "soporte",
              "output": 0
            },
            {
              "value": "ventas",
              "output": 1
            },
            {
              "value": "otro",
              "output": 2
            }
          ]
        }
      },
      "id": "switch",
      "name": "Switch por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [920, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 *Nuevo mensaje de soporte*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1160, 180],
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nuevo mensaje de ventas*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1160, 300],
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📬 *Mensaje sin clasificar*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1160, 420],
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack"
        }
      }
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
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1",
  "meta": {
    "instanceId": "n8n-workflow"
  }
}
```