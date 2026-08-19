# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — code_generation/n8n_workflow_json

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.5 | quality: 7.72
- latency_total: 155.925s | tokens_per_second: 18.5
- input_tokens: 133 | output_tokens: 2881
- judge_score: 3.8 | justificación: 

## Respuesta completa

{
  "name": "Clasificar y enrutar mensaje a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify",
        "responseMode": "onReceived",
        "responseData": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        0,
        0
      ],
      "id": "1"
    },
    {
      "parameters": {
        "values": [
          {
            "name": "email",
            "value": "={{ $json[\"email\"] }}"
          },
          {
            "name": "message",
            "value": "={{ $json[\"message\"] }}"
          }
        ],
        "options": {}
      },
      "name": "Set Email & Message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        200,
        0
      ],
      "id": "2"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "Classify the following message into one of the categories: soporte, ventas, otro. Return only the category name.\n\nMessage: {{$json[\"message\"]}}",
        "temperature": 0,
        "maxTokens": 10
      },
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        400,
        0
      ],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI Account"
        }
      },
      "id": "3"
    },
    {
      "parameters": {
        "property": "value",
        "rules": [
          {
            "value": "soporte",
            "type": "string"
          },
          {
            "value": "ventas",
            "type": "string"
          },
          {
            "value": "otro",
            "type": "string"
          }
        ],
        "value": "={{ $json[\"text\"] }}"
      },
      "name": "Router por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        600,
        0
      ],
      "id": "4"
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje de soporte\\nEmail: {{$json[\"email\"]}}\\nMensaje: {{$json[\"message\"]}}"
      },
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        800,
        -100
      ],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "Slack Account"
        }
      },
      "id": "5"
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas\\nEmail: {{$json[\"email\"]}}\\nMensaje: {{$json[\"message\"]}}"
      },
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        800,
        0
      ],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "Slack Account"
        }
      },
      "id": "6"
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje (otro)\\nEmail: {{$json[\"email\"]}}\\nMensaje: {{$json[\"message\"]}}"
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        800,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "Slack Account"
        }
      },
      "id": "7"
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set Email & Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Email & Message": {
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
            "node": "Router por Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por Clasificación": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "workflow-classify-slack"
}