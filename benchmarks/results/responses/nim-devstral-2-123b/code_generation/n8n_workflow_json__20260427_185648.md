# Devstral 2 123B (NIM) — code_generation/n8n_workflow_json

- model_id: `mistralai/devstral-2-123b-instruct-2512`
- success: True  | final: 6.52 | quality: 7.48
- latency_total: 39.353s | tokens_per_second: 43.7
- input_tokens: 120 | output_tokens: 1719
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n que cumple con tus requisitos. Este workflow utiliza un webhook para recibir datos, extrae el email y mensaje, clasifica el mensaje con OpenAI y luego envía el mensaje al canal de Slack correspondiente:

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde solo con la categoría, sin explicaciones."
          },
          {
            "role": "user",
            "content": "={{$node[\"Webhook\"].json[\"message\"]}}"
          }
        ],
        "options": {}
      },
      "id": "2",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIALS_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "3",
      "name": "IF: Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        200
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "4",
      "name": "IF: Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\nEmail: {{\($node[\"Webhook\"].json[\"email\"]\\)}}\nMensaje: {{\($node[\"Webhook\"].json[\"message\"]\\)}}"
      },
      "id": "5",
      "name": "Slack: Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\nEmail: {{\($node[\"Webhook\"].json[\"email\"]\\)}}\nMensaje: {{\($node[\"Webhook\"].json[\"message\"]\\)}}"
      },
      "id": "6",
      "name": "Slack: Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje general:\nEmail: {{\($node[\"Webhook\"].json[\"email\"]\\)}}\nMensaje: {{\($node[\"Webhook\"].json[\"message\"]\\)}}"
      },
      "id": "7",
      "name": "Slack: General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        400
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      }
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
            "node": "IF: Soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "IF: Ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF: Soporte": {
      "main": [
        [
          {
            "node": "Slack: Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: General",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "IF: Ventas": {
      "main": [
        [
          {
            "node": "Slack: Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: General",
            "type": "main",
            "index": 1
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {},
  "id": "YOUR_WORKFLOW_ID"
}
```

### Notas importantes:
1. **Credenciales**: Debes reemplazar `YOUR_OPENAI_CREDENTIALS_ID` y `YOUR_SLACK_CREDENTIALS_ID` con los IDs reales de tus credenciales configuradas en n8n.
2. **Canales de Slack**: Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu espacio de trabajo de Slack.
3. **Modelo OpenAI**: El workflow usa `gpt-3.5-turbo`, pero puedes cambiarlo a otro modelo si lo prefieres.
4. **Estructura del webhook**: El workflow espera un JSON con los campos `email` y `message` en el body del POST.

Para usar este workflow:
1. Copia el JSON completo
2. En n8n, ve a "Workflows" y haz clic en "Import"
3. Pega el JSON y guarda el workflow
4. Activa el webhook y configura tus credenciales