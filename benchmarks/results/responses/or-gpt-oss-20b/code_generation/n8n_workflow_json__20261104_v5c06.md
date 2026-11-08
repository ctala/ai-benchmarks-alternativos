# GPT-OSS 20B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.76 | quality: 8.0
- latency_total: 32.015s | tokens_per_second: 113.5
- input_tokens: 166 | output_tokens: 3635
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los pasos necesarios para el flujo de trabajo de N8N, aunque carece de detalles adicionales sobre la configuración de credenciales y manejo de errores, lo cual podría mejorar la profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow.


## Respuesta completa

```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming"
      }
    },
    {
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "parameters": {
        "values": {
          "email": {
            "value": "={{$json[\"email\"]}}"
          },
          "message": {
            "value": "={{$json[\"message\"]}}"
          }
        },
        "options": {}
      }
    },
    {
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAI",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "Please classify the following message into one of the categories: soporte, ventas, otro. Respond with only the category.\n\nMessage: {{$node[\"Extract Fields\"].json.message}}",
        "maxTokens": 10,
        "temperature": 0
      },
      "credentials": {
        "openAIApiKey": "YOUR_OPENAI_API_KEY"
      }
    },
    {
      "name": "Extract Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        850,
        300
      ],
      "parameters": {
        "values": {
          "classification": {
            "value": "={{$node[\"Classify Message\"].json.choices[0].message.content.trim()}}"
          }
        },
        "options": {}
      }
    },
    {
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "parameters": {
        "value": "={{$node[\"Extract Classification\"].json.classification}}",
        "switchValue": {
          "soporte": {
            "value": "soporte"
          },
          "ventas": {
            "value": "ventas"
          },
          "otro": {
            "value": "otro"
          }
        }
      }
    },
    {
      "name": "Send to Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        150
      ],
      "parameters": {
        "channel": "#support",
        "message": "Nuevo mensaje de soporte de {{$node[\"Extract Fields\"].json.email}}:\n{{$node[\"Extract Fields\"].json.message}}"
      },
      "credentials": {
        "slackApi": "YOUR_SLACK_API_KEY"
      }
    },
    {
      "name": "Send to Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ],
      "parameters": {
        "channel": "#sales",
        "message": "Nuevo mensaje de ventas de {{$node[\"Extract Fields\"].json.email}}:\n{{$node[\"Extract Fields\"].json.message}}"
      },
      "credentials": {
        "slackApi": "YOUR_SLACK_API_KEY"
      }
    },
    {
      "name": "Send to Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        450
      ],
      "parameters": {
        "channel": "#general",
        "message": "Nuevo mensaje de otro de {{$node[\"Extract Fields\"].json.email}}:\n{{$node[\"Extract Fields\"].json.message}}"
      },
      "credentials": {
        "slackApi": "YOUR_SLACK_API_KEY"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
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
            "node": "Extract Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Classification": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Send to Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```