# Grok 4.3 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.31 | quality: 8.0
- latency_total: 15.496s | tokens_per_second: 120.0
- input_tokens: 244 | output_tokens: 1860

## Respuesta completa

```json
{
  "name": "Clasificador de Emails con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "responseNode"
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de estas tres categorías: \"soporte\", \"ventas\" o \"otro\". Responde ÚNICAMENTE con una de esas tres palabras en minúsculas, sin ningún texto adicional."
            },
            {
              "role": "user",
              "content": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        }
      },
      "id": "openai-node",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openai",
      "typeVersion": 1,
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
        "rules": {
          "rules": [
            {
              "outputKey": "soporte",
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
                    "operation": "equal",
                    "value2": "soporte"
                  }
                ]
              }
            },
            {
              "outputKey": "ventas",
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
                    "operation": "equal",
                    "value2": "ventas"
                  }
                ]
              }
            },
            {
              "outputKey": "otro",
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
                    "operation": "equal",
                    "value2": "otro"
                  }
                ]
              }
            }
          ]
        },
        "fallbackOutput": 3
      },
      "id": "switch-node",
      "name": "Switch por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [720, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 Nuevo mensaje de soporte\n\n*Email:* {{ $('Webhook').item.json.email }}\n*Mensaje:* {{ $('Webhook').item.json.message }}"
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 180],
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 Nuevo mensaje de ventas\n\n*Email:* {{ $('Webhook').item.json.email }}\n*Mensaje:* {{ $('Webhook').item.json.message }}"
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 300],
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📬 Nuevo mensaje (otro)\n\n*Email:* {{ $('Webhook').item.json.email }}\n*Mensaje:* {{ $('Webhook').item.json.message }}"
      },
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 420],
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
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
    "templateCredsSetupCompleted": true
  }
}
```