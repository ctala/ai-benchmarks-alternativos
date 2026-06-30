# Grok 4.3 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.3`
- success: True  | final: 7.3 | quality: 8.0
- latency_total: 14.615s | tokens_per_second: 138.3
- input_tokens: 244 | output_tokens: 2021

## Respuesta completa

```json
{
  "name": "Clasificador Mensajes Webhook → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
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
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en exactamente una de estas tres categorías: soporte, ventas u otro. Responde SOLO con una de esas tres palabras en minúsculas, sin ningún texto adicional."
            },
            {
              "role": "user",
              "content": "Email: {{$json.email}}\nMensaje: {{$json.message}}"
            }
          ]
        }
      },
      "id": "openai-classifier",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.1,
      "position": [480, 300],
      "credentials": {
        "openAiApi": {
          "id": "openai-credential",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.choices[0].message.content.trim() }}",
                    "operation": "equals",
                    "value2": "soporte"
                  }
                ]
              }
            },
            {
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.choices[0].message.content.trim() }}",
                    "operation": "equals",
                    "value2": "ventas"
                  }
                ]
              }
            },
            {
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.choices[0].message.content.trim() }}",
                    "operation": "equals",
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
      "typeVersion": 3.2,
      "position": [720, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 Nuevo mensaje de soporte\n\n*Email:* {{$json.email}}\n*Mensaje:* {{$json.message}}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 140],
      "credentials": {
        "slackApi": {
          "id": "slack-credential",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📩 Nuevo mensaje de ventas\n\n*Email:* {{$json.email}}\n*Mensaje:* {{$json.message}}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 300],
      "credentials": {
        "slackApi": {
          "id": "slack-credential",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📩 Nuevo mensaje\n\n*Email:* {{$json.email}}\n*Mensaje:* {{$json.message}}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 460],
      "credentials": {
        "slackApi": {
          "id": "slack-credential",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "text",
        "options": {
          "responseData": "Mensaje recibido y clasificado correctamente"
        }
      },
      "id": "respond-webhook",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [720, 500]
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
        ],
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
  }
}
```