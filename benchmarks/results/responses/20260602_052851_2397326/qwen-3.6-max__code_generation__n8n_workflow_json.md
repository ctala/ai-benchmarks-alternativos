# Qwen 3.6 Max — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 6.39 | quality: 8.6
- latency_total: 222.05s | tokens_per_second: 45.6
- input_tokens: 125 | output_tokens: 10121
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un JSON bien estructurado. Aunque la profundidad es adecuada, podría haber incluido más detalles sobre la configuración de Slack o manejo de errores. La claridad y utilidad práctica son altas, facilitando la implementación directa.

## Respuesta completa

Aquí tienes el JSON completo del workflow listo para importar en n8n. Está diseñado con las versiones de nodos actuales (n8n v1.0+) y sigue buenas prácticas de manejo de datos y expresiones.

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "lastNode",
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
        "operation": "chat",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en exactamente una de estas tres categorías: soporte, ventas, otro. Responde ÚNICAMENTE con la palabra en minúsculas, sin puntuación, sin explicaciones y sin texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node",
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "openAiApi": {
          "id": "PLACEHOLDER_OPENAI_CRED_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "category",
              "name": "category",
              "value": "={{ ($json.content || $json.message?.content || '').trim().toLowerCase() }}",
              "type": "string"
            },
            {
              "id": "email",
              "name": "email",
              "value": "={{ $node[\"Webhook\"].json.body.email }}",
              "type": "string"
            },
            {
              "id": "message",
              "name": "message",
              "value": "={{ $node[\"Webhook\"].json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-node",
      "name": "Extract & Format",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [650, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              }
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [850, 300]
    },
    {
      "parameters": {
        "operation": "sendMessage",
        "channel": "#support",
        "message": "🛠️ *Nuevo mensaje de SOPORTE*\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 150],
      "credentials": {
        "slackApi": {
          "id": "PLACEHOLDER_SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "sendMessage",
        "channel": "#sales",
        "message": "💰 *Nuevo mensaje de VENTAS*\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 300],
      "credentials": {
        "slackApi": {
          "id": "PLACEHOLDER_SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "sendMessage",
        "channel": "#general",
        "message": "📌 *Nuevo mensaje (OTRO)*\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 450],
      "credentials": {
        "slackApi": {
          "id": "PLACEHOLDER_SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI Classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "Extract & Format",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract & Format": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "pinData": {}
}
```

### 📌 Notas importantes para puesta en marcha:
1. **Importar**: En n8n ve a `Menu → Import from JSON` y