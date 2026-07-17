# Qwen 3-Next 80B Thinking — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.27 | quality: 8.0
- latency_total: 45.374s | tokens_per_second: 171.2
- input_tokens: 123 | output_tokens: 7768
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un uso adecuado de los nodos de N8N, aunque carece de detalles adicionales sobre la configuración de seguridad y manejo de errores.

## Respuesta completa

```json
{
  "nodes": [
    {
      "parameters": {
        "path": "classify",
        "responseMode": "onReceived",
        "statusCode": 200,
        "responseHeaders": [],
        "responseBody": "json",
        "options": {
          "sendResponse": true
        }
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "id": "1",
      "webhookId": "webhook_1"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "Classify the following message into 'soporte', 'ventas', or 'otro'. Only respond with one of the three words. Message: {{ $json.message }}",
        "outputField": "category",
        "apiKey": "your_openai_api_key",
        "maxTokens": 10,
        "temperature": 0.1
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "id": "2"
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.category }}",
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.category }}",
              "operation": "equal",
              "value2": "ventas"
            },
            {
              "value1": "={{ $json.category }}",
              "operation": "equal",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "Branch",
      "type": "n8n-nodes-base.branch",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "id": "3"
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "New message from {{ $json.email }}: {{ $json.message }}",
        "authentication": "accessToken",
        "accessToken": "your_slack_token"
      },
      "name": "Slack (Support)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        200
      ],
      "id": "4"
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "New message from {{ $json.email }}: {{ $json.message }}",
        "authentication": "accessToken",
        "accessToken": "your_slack_token"
      },
      "name": "Slack (Sales)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        300
      ],
      "id": "5"
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "New message from {{ $json.email }}: {{ $json.message }}",
        "authentication": "accessToken",
        "accessToken": "your_slack_token"
      },
      "name": "Slack (General)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        400
      ],
      "id": "6"
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
            "node": "Branch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Branch": {
      "main": [
        [
          {
            "node": "Slack (Support)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (Sales)",
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
    }
  },
  "settings": {
    "executionTimeout": 300,
    "timeZone": "America/New_York"
  }
}
```