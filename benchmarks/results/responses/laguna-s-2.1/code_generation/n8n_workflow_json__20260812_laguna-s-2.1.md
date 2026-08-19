# Poolside Laguna S 2.1 — code_generation/n8n_workflow_json

- model_id: `poolside/laguna-s-2.1`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 17.704s | tokens_per_second: 96.1
- input_tokens: 169 | output_tokens: 1702
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado, aunque carece de profundidad en la explicación de la lógica de clasificación.

## Respuesta completa

```json
{
  "name": "Classify and Route Messages",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook/classify-message"
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"body\"][\"email\"]}}",
              "operation": "notEmpty"
            }
          ]
        }
      },
      "id": "check-email",
      "name": "Check Email",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1.1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"body\"][\"message\"]}}",
              "operation": "notEmpty"
            }
          ]
        }
      },
      "id": "check-message",
      "name": "Check Message",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1.1,
      "position": [450, 450]
    },
    {
      "parameters": {
        "authentication": "openAiApi",
        "operation": "chat",
        "model": "gpt-3.5-turbo",
        "options": {
          "systemMessage": "You are a helpful assistant that classifies customer messages into one of three categories: support, sales, or other. Classify the following message:",
          "messages": {
            "messageValues": [
              {
                "role": "user",
                "text": "={{$json[\"body\"][\"message\"]}}"
              }
            ]
          }
        }
      },
      "id": "openai-classifier",
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [650, 375]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "contains",
              "value2": "support"
            }
          ]
        }
      },
      "id": "is-support",
      "name": "Is Support?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1.1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "contains",
              "value2": "sales"
            }
          ]
        }
      },
      "id": "is-sales",
      "name": "Is Sales?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1.1,
      "position": [850, 450]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "operation": "post",
        "channel": "#support",
        "text": "={{$json[\"body\"][\"email\"]}} - {{$json[\"body\"][\"message\"]}}"
      },
      "id": "send-to-support",
      "name": "Send to Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 225]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "operation": "post",
        "channel": "#sales",
        "text": "={{$json[\"body\"][\"email\"]}} - {{$json[\"body\"][\"message\"]}}"
      },
      "id": "send-to-sales",
      "name": "Send to Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 375]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "operation": "post",
        "channel": "#general",
        "text": "={{$json[\"body\"][\"email\"]}} - {{$json[\"body\"][\"message\"]}}"
      },
      "id": "send-to-general",
      "name": "Send to General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 525]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Check Email",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Email": {
      "main": [
        [
          {
            "node": "Check Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Message": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Is Support?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Support?": {
      "main": [
        [
          {
            "node": "Send to Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Is Sales?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Is Sales?": {
      "main": [
        [
          {
            "node": "Send to Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "versionId": "1",
  "meta": {
    "templateCredsSetup": true
  }
}
```