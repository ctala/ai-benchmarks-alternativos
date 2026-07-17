# Nemotron 3 Nano Omni 30B-A3B Reasoning — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 7.24 | quality: 8.0
- latency_total: 88.066s | tokens_per_second: 92.2
- input_tokens: 133 | output_tokens: 8122
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado. Aunque no ofrece insights adicionales más allá de la implementación básica, es práctica y directamente utilizable por un emprendedor.

## Respuesta completa

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "receive"
      },
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "id": "1"
    },
    {
      "parameters": {
        "values": {
          "email": "={{ $json[\"email\"] }}",
          "message": "={{ $json[\"message\"] }}"
        },
        "option": "set"
      },
      "name": "Set Extract",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [500, 300],
      "id": "2"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "text": "Classify the following message into one of three categories: soporte, ventas, otro. Return only the category name.\nMessage: {{$json[\"message\"]}}"
      },
      "name": "OpenAI Classification",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 2,
      "position": [750, 300],
      "id": "3"
    },
    {
      "parameters": {
        "values": {
          "category": "={{ $json[\"text\"] }}"
        },
        "option": "set"
      },
      "name": "Set Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [1000, 300],
      "id": "4"
    },
    {
      "parameters": {
        "rules": [
          {
            "value1": "= $json[\"category\"]",
            "case": "soporte"
          },
          {
            "value1": "= $json[\"category\"]",
            "case": "ventas"
          },
          {
            "value1": "= $json[\"category\"]",
            "case": "otro"
          }
        ]
      },
      "name": "Switch by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [1250, 300],
      "id": "5"
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 {{$json[\"email\"]}}\n📝 {{$json[\"message\"]}}"
      },
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1500, 300],
      "id": "6"
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📧 {{$json[\"email\"]}}\n📝 {{$json[\"message\"]}}"
      },
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1500, 400],
      "id": "7"
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📧 {{$json[\"email\"]}}\n📝 {{$json[\"message\"]}}"
      },
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1500, 500],
      "id": "8"
    }
  ],
  "connections": {
    "main": [
      {
        "node": "1",
        "main": [
          {
            "node": "2",
            "type": "main",
            "index": 0,
            "from": { "node": "1", "index": 0 },
            "to": { "node": "2", "index": 0 }
          }
        ]
      },
      {
        "node": "2",
        "main": [
          {
            "node": "3",
            "type": "main",
            "index": 0,
            "from": { "node": "2", "index": 0 },
            "to": { "node": "3", "index": 0 }
          }
        ]
      },
      {
        "node": "3",
        "main": [
          {
            "node": "4",
            "type": "main",
            "index": 0,
            "from": { "node": "3", "index": 0 },
            "to": { "node": "4", "index": 0 }
          }
        ]
      },
      {
        "node": "4",
        "main": [
          {
            "node": "5",
            "type": "main",
            "index": 0,
            "from": { "node": "4", "index": 0 },
            "to": { "node": "5", "index": 0 }
          }
        ]
      },
      {
        "node": "5",
        "main": [
          {
            "node": "6",
            "type": "main",
            "index": 0,
            "from": { "node": "5", "index": 0 },
            "to": { "node": "6", "index": 0 }
          },
          {
            "node": "7",
            "type": "main",
            "index": 1,
            "from": { "node": "5", "index": 0 },
            "to": { "node": "7", "index": 0 }
          },
          {
            "node": "8",
            "type": "main",
            "index": 2,
            "from": { "node": "5", "index": 0 },
            "to": { "node": "8", "index": 0 }
          }
        ]
      }
    ]
  }
}
```