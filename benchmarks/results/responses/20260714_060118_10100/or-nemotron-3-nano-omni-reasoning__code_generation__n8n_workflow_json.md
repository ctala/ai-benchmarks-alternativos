# Nemotron 3 Nano Omni 30B-A3B Reasoning — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 7.92 | quality: 8.0
- latency_total: 20.457s | tokens_per_second: 182.6
- input_tokens: 133 | output_tokens: 3735
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del flujo de trabajo de N8N, aunque carece de profundidad adicional más allá de la funcionalidad básica requerida.

## Respuesta completa

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "webhook",
        "operation": "post",
        "webhookId": "webhook_1"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "connections": {}
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "= $json[\"email\"]"
            },
            {
              "name": "message",
              "value": "= $json[\"message\"]"
            }
          ]
        },
        "option": "set"
      },
      "name": "Set Extract",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [425, 300],
      "connections": {
        "Webhook": {
          "main": [
            [
              {
                "node": "Set Extract",
                "type": "main"
              }
            ]
          ]
        }
      }
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "operation": "text",
        "prompt": "Classify the following message into one of the categories: soporte, ventas, otro. Return only the category name.\nMessage: {{ $json[\"message\"] }}",
        "temperature": 0.0,
        "maxTokens": 10,
        "responseFormat": "text"
      },
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [600, 300],
      "connections": {
        "Set Extract": {
          "main": [
            [
              {
                "node": "OpenAI Classify",
                "type": "main"
              }
            ]
          ]
        }
      }
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "classification",
              "value": "= $json[\"response\"]"
            },
            {
              "name": "channel",
              "value": "= $json[\"classification\"] == \"soporte\" ? \"#support\" : ($json[\"classification\"] == \"ventas\" ? \"#sales\" : \"#general\")"
            }
          ]
        },
        "option": "set"
      },
      "name": "Set Map",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [775, 300],
      "connections": {
        "OpenAI Classify": {
          "main": [
            [
              {
                "node": "Set Map",
                "type": "main"
              }
            ]
          ]
        }
      }
    },
    {
      "parameters": {
        "text": "From: {{ $json[\"email\"] }}\nMessage: {{ $json[\"message\"] }}",
        "channel": "= $json[\"channel\"]",
        "authentication": "slack"
      },
      "name": "Slack Post",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [950, 300],
      "connections": {
        "Set Map": {
          "main": [
            [
              {
                "node": "Slack Post",
                "type": "main"
              }
            ]
          ]
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set Extract",
            "type": "main"
          }
        ]
      ]
    },
    "Set Extract": {
      "main": [
        [
          {
            "node": "OpenAI Classify",
            "type": "main"
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "Set Map",
            "type": "main"
          }
        ]
      ]
    },
    "Set Map": {
      "main": [
        [
          {
            "node": "Slack Post",
            "type": "main"
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {}
}
```