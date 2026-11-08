# Grok 4.6 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.6`
- success: True  | final: 4.83 | quality: 5.2
- latency_total: 60.917s | tokens_per_second: 88.5
- input_tokens: 319 | output_tokens: 5392
- judge_score: 2.0 | justificación: 

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
  "name": "Webhook AI Classifier to Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-message",
        "options": {}
      },
      "id": "c1a2b3c4-d5e6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "incoming-message-webhook"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "content": "Clasifica el siguiente mensaje de cliente en UNA SOLA de estas categorías: soporte, ventas, otro. Responde ÚNICAMENTE con la palabra de la categoría, en minúsculas, sin explicaciones ni puntuación extra.\n\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "d2b3c4d5-e6f7-8901-bcde-f23456789012",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [470, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
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
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true
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
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true
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
                    "id": "cond-otro",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "e3c4d5e6-f7a8-9012-cdef-345678901234",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [690, 300]
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#support",
        "text": "=Nuevo mensaje de SOPORTE\nEmail: {{ $('Webhook').item.json.email }}\nMensaje: {{ $('Webhook').item.json.message }}",
        "otherOptions": {}
      },
      "id": "f4d5e6f7-a8b9-0123-defa-456789012345",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [910, 180],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#sales",
        "text": "=Nuevo mensaje de VENTAS\nEmail: {{ $('Webhook').item.json.email }}\nMensaje: {{ $('Webhook').item.json.message }}",
        "otherOptions": {}
      },
      "id": "g5e6f7a8-b9c0-1234-efab-567890123456",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [910, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#general",
        "text": "=Nuevo mensaje (OTRO)\nEmail: {{ $('Webhook').item.json.email }}\nMensaje: {{ $('Webhook').item.json.message }}",
        "otherOptions": {}
      },
      "id": "h6f7a8b9-c0d1-2345-fabc-678901234567",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [910, 420],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
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
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "meta": {
    "instanceId": "your-n8n-instance-id"
  },
  "id": "workflow-classifier-slack",
  "tags": []
}
```