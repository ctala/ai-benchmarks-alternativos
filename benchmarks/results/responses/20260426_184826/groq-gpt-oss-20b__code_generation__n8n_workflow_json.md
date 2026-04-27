# GPT-OSS 20B (Groq) — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.65 | quality: 8.0
- latency_total: 2.317s | tokens_per_second: 820.0
- input_tokens: 183 | output_tokens: 1900
- judge_score: 4.0 | justificación: 

## Respuesta completa

```json
{
  "name": "Webhook Email Classifier",
  "active": true,
  "nodes": [
    {
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [200, 200],
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook",
        "responseMode": "onReceived"
      }
    },
    {
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [400, 200],
      "parameters": {
        "values": {
          "set": [
            {
              "name": "email",
              "value": "={{ $json.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [600, 200],
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant."
          },
          {
            "role": "user",
            "content": "Classify the following message into one of the categories: soporte, ventas, otro. Just output the category. Message: {{ $json.message }}"
          }
        ],
        "maxTokens": 10,
        "temperature": 0
      }
    },
    {
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [800, 200],
      "parameters": {
        "value": "={{ $json.choices[0].message.content.trim() }}",
        "rules": [
          {
            "value": "soporte",
            "nextNode": "Send to Support"
          },
          {
            "value": "ventas",
            "nextNode": "Send to Sales"
          },
          {
            "value": "otro",
            "nextNode": "Send to General"
          }
        ],
        "options": {}
      }
    },
    {
      "name": "Send to Support",
      "type": "n8n-nodes-base.slackSendMessage",
      "typeVersion": 1,
      "position": [1000, 100],
      "parameters": {
        "channel": "#support",
        "text": "New support request:\nEmail: {{ $json.email }}\nMessage: {{ $json.message }}"
      }
    },
    {
      "name": "Send to Sales",
      "type": "n8n-nodes-base.slackSendMessage",
      "typeVersion": 1,
      "position": [1000, 200],
      "parameters": {
        "channel": "#sales",
        "text": "New sales inquiry:\nEmail: {{ $json.email }}\nMessage: {{ $json.message }}"
      }
    },
    {
      "name": "Send to General",
      "type": "n8n-nodes-base.slackSendMessage",
      "typeVersion": 1,
      "position": [1000, 300],
      "parameters": {
        "channel": "#general",
        "text": "New general message:\nEmail: {{ $json.email }}\nMessage: {{ $json.message }}"
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main"
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main"
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main"
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Send to Support",
            "type": "main"
          },
          {
            "node": "Send to Sales",
            "type": "main"
          },
          {
            "node": "Send to General",
            "type": "main"
          }
        ]
      ]
    }
  }
}
```