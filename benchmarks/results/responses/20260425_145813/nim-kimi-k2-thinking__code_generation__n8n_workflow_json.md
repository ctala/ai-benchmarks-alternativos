# Kimi K2 Thinking (NIM) — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2-thinking`
- success: True  | final: 6.6 | quality: 7.72
- latency_total: 51.914s | tokens_per_second: 39.4
- input_tokens: 126 | output_tokens: 2043
- judge_score: 3.8 | justificación: 

## Respuesta completa

 ```json
{
  "name": "Clasificador de Mensajes IA",
  "nodes": [
    {
      "parameters": {
        "path": "webhook-clasificador",
        "httpMethod": "POST",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {},
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "text": "Eres un clasificador de mensajes. Clasifica el siguiente mensaje en EXACTAMENTE una de estas categorías: \"soporte\", \"ventas\" o \"otro\". Solo responde con la palabra de la categoría, sin explicaciones ni texto adicional."
            },
            {
              "role": "user",
              "text": "Email: {{$json.body.email}}\nMensaje: {{$json.body.message}}"
            }
          ]
        }
      },
      "id": "2b3c4d5e-6f7g-8h9i-0j1k-2l3m4n5o6p7q",
      "name": "OpenAI Clasificador",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [500, 300],
      "credentials": {
        "openAiApi": "OpenAI Account"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
              "value2": "soporte",
              "operation": "equal"
            },
            {
              "value1": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
              "value2": "ventas",
              "operation": "equal"
            },
            {
              "value1": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
              "value2": "otro",
              "operation": "equal"
            }
          ]
        },
        "output": 3
      },
      "id": "3c4d5e6f-7g8h-9i0j-1k2l-3m4n5o6p7q8r",
      "name": "IF Clasificación",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [750, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 *Nuevo mensaje de soporte*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "options": {}
      },
      "id": "4d5e6f7g-8h9i-0j1k-2l3m-4n5o6p7q8r9s",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1000, 150],
      "credentials": {
        "slackApi": "Slack Account"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nuevo mensaje de ventas*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "options": {}
      },
      "id": "5e6f7g8h-9i0j-1k2l-3m4n-5o6p7q8r9s0t",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1000, 300],
      "credentials": {
        "slackApi": "Slack Account"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📨 *Nuevo mensaje general*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "options": {}
      },
      "id": "6f7g8h9i-0j1k-2l3m-4n5o-6p7q8r9s0t1u",
      "name": "Slack Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1000, 450],
      "credentials": {
        "slackApi": "Slack Account"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI Clasificador",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Clasificador": {
      "main": [
        [
          {
            "node": "IF Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Clasificación": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Otro",
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
  "id": "7g8h9i0j-1k2l-3m4n-5o6p-7q8r9s0t1u2v",
  "meta": {
    "instanceId": "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
  }
}
```