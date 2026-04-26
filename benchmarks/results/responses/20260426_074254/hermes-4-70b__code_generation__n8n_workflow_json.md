# Hermes 4 70B — code_generation/n8n_workflow_json

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 6.41 | quality: 6.04
- latency_total: 12.088s | tokens_per_second: 79.9
- input_tokens: 139 | output_tokens: 966
- judge_score: 2.6 | justificación: 

## Respuesta completa

{
  "name": "Webhook and Slack Classifier",
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "path": "webhook",
        "displayName": "Webhook",
        "multipleMessages": false,
        "responseData": "json"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        450,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[email]}}",
              "value2": "=?*",
              "operator": "notEmpty"
            }
          ]
        }
      },
      "name": "Email Check",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "apiVersion": "stable",
        "model": "text-classification",
        "choices": "1",
        "classificationModel": "classification",
        "classificationCategories": "support,ventas,otro",
        "classificationLabels": "soporte,ventas,otro",
        "classificationNullLabel": "otro",
        "text": "={{$json[message]}}"
      },
      "name": "OpenAI Classification",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Soporte: {{$json[email]}} - {{$json[message]}}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        150
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Ventas: {{$json[email]}} - {{$json[message]}}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Otro: {{$json[email]}} - {{$json[message]}}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        450
      ]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json[email]}}"
            },
            {
              "name": "message",
              "value": "={{$json[message]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    }
  ],
  "connections": {
    "Start": {
      "main": [
        [
          "Webhook",
          0
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          "Email Check",
          0
        ]
      ]
    },
    "Email Check": {
      "main": [
        [
          "OpenAI Classification",
          0
        ]
      ]
    },
    "OpenAI Classification": {
      "main": [
        [
          "Set",
          0
        ]
      ]
    },
    "Set": {
      "main": [
        [
          "Slack Support",
          0
        ],
        [
          "Slack Sales",
          0
        ],
        [
          "Slack General",
          0
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": 10
}