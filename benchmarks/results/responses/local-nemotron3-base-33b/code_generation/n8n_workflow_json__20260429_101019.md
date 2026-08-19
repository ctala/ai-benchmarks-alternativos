# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — code_generation/n8n_workflow_json

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 6.4 | quality: 7.72
- latency_total: 81.791s | tokens_per_second: 65.6
- input_tokens: 134 | output_tokens: 5365
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "request",
        "event": "post"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "id": "1"
    },
    {
      "parameters": {
        "functionCode": "const email = $json.email;\nconst message = $json.message;\nreturn [{$json: {email, message}}];"
      },
      "name": "Extract Email & Message",
      "type": "n8n-nodes-base.function",
      "typeVersion": 2,
      "position": [250, 0],
      "id": "2"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "operation": "complete",
        "prompt": "Classify the following message into one of the categories: soporte, ventas, otro. Return only the category name.\n\nMessage: {{ $json.message }}"
      },
      "name": "OpenAI Classification",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 2,
      "position": [500, 0],
      "id": "3"
    },
    {
      "parameters": {
        "values": {
          "classification": "={{ $json.choices[0].text }}"
        }
      },
      "name": "Set Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [750, 0],
      "id": "4"
    },
    {
      "parameters": {
        "rules": [
          {
            "value1": "={{ $node[\"Set Classification\"].json.classification}}",
            "comparison": "equals",
            "value2": "soporte",
            "nextNode": "Slack Support"
          },
          {
            "value1": "={{ $node[\"Set Classification\"].json.classification}}",
            "comparison": "equals",
            "value2": "ventas",
            "nextNode": "Slack Sales"
          },
          {
            "value1": "={{ $node[\"Set Classification\"].json.classification}}",
            "comparison": "equals",
            "value2": "otro",
            "nextNode": "Slack General"
          }
        ]
      },
      "name": "Switch Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [1000, 0],
      "id": "5"
    },
    {
      "parameters": {
        "channel": "#support",
        "message": "📧 Email: {{ $node[\"Extract Email & Message\"].json.email }}\n📝 Message: {{ $node[\"Extract Email & Message\"].json.message }}\n🔎 Classification: soporte",
        "authentication": {
          "slack": "mySlackCredentials"
        }
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 0],
      "id": "6"
    },
    {
      "parameters": {
        "channel": "#sales",
        "message": "📧 Email: {{ $node[\"Extract Email & Message\"].json.email }}\n📝 Message: {{ $node[\"Extract Email & Message\"].json.message }}\n🔎 Classification: ventas",
        "authentication": {
          "slack": "mySlackCredentials"
        }
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 200],
      "id": "7"
    },
    {
      "parameters": {
        "channel": "#general",
        "message": "📧 Email: {{ $node[\"Extract Email & Message\"].json.email }}\n📝 Message: {{ $node[\"Extract Email & Message\"].json.message }}\n🔎 Classification: otro",
        "authentication": {
          "slack": "mySlackCredentials"
        }
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 400],
      "id": "8"
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Email & Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Email & Message": {
      "main": [
        [
          {
            "node": "OpenAI Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classification": {
      "main": [
        [
          {
            "node": "Set Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Classification": {
      "main": [
        [
          {
            "node": "Switch Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Classification": {
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
          },
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
  "settings": {},
  "id": "workflow"
}
```