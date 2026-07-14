# Qwen 3-Next 80B Thinking — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.24 | quality: 8.0
- latency_total: 48.593s | tokens_per_second: 187.6
- input_tokens: 123 | output_tokens: 9118
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

```json
{
  "name": "Email Classification Workflow",
  "active": true,
  "nodes": [
    {
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "parameters": {
        "path": "/webhook",
        "httpMethod": "POST",
        "responseMode": "onFinish",
        "responseStatusCode": 200,
        "responseBody": "success",
        "options": {}
      }
    },
    {
      "id": "2",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "openAiApi": "OpenAI"
      },
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "Classify the following message into one of the categories: soporte, ventas, otro. Only respond with the category name. Message: {{ $json.message }}",
        "responseFormat": "string"
      }
    },
    {
      "id": "3",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [650, 300],
      "parameters": {
        "conditions": [
          {
            "value1": "={{ $json.response }}",
            "operation": "equal",
            "value2": "soporte"
          },
          {
            "value1": "={{ $json.response }}",
            "operation": "equal",
            "value2": "ventas"
          },
          {
            "value1": "={{ $json.response }}",
            "operation": "equal",
            "value2": "otro"
          }
        ]
      }
    },
    {
      "id": "4",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 200],
      "credentials": {
        "slackApi": "Slack"
      },
      "parameters": {
        "channel": "#support",
        "text": "New message from {{ $json.email }}: {{ $json.message }}"
      }
    },
    {
      "id": "5",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 300],
      "credentials": {
        "slackApi": "Slack"
      },
      "parameters": {
        "channel": "#sales",
        "text": "New message from {{ $json.email }}: {{ $json.message }}"
      }
    },
    {
      "id": "6",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 400],
      "credentials": {
        "slackApi": "Slack"
      },
      "parameters": {
        "channel": "#general",
        "text": "New message from {{ $json.email }}: {{ $json.message }}"
      }
    }
  ],
  "connections": {
    "1": [
      {
        "main": [
          [
            {
              "node": "2",
              "type": "main",
              "index": 0
            }
          ]
        ]
      }
    ],
    "2": [
      {
        "main": [
          [
            {
              "node": "3",
              "type": "main",
              "index": 0
            }
          ]
        ]
      }
    ],
    "3": [
      {
        "main": [
          [
            {
              "node": "4",
              "type": "main",
              "index": 0
            }
          ],
          [
            {
              "node": "5",
              "type": "main",
              "index": 1
            }
          ],
          [
            {
              "node": "6",
              "type": "main",
              "index": 2
            }
          ]
        ]
      }
    ]
  }
}
```