# Devstral 2 (Dic 2025) — code_generation/n8n_workflow_json

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.31 | quality: 8.32
- latency_total: 16.396s | tokens_per_second: 123.0
- input_tokens: 120 | output_tokens: 2017
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n que cumple con tus requisitos:

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
            "content": "Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas, otro. Responde solo con la categoría elegida.\n\nMensaje: {{$node[\"Webhook\"].json[\"body\"][\"message\"]}}",
            "role": "user"
          }
        ],
        "temperature": 0.7,
        "topP": 1,
        "frequencyPenalty": 0,
        "presencePenalty": 0,
        "n": 1,
        "maxTokens": 50,
        "stop": [
          "\n"
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
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\nEmail: {{$node[\"Webhook\"].json[\"body\"][\"email\"]}}\nMensaje: {{$node[\"Webhook\"].json[\"body\"][\"message\"]}}",
        "options": {}
      },
      "id": "3",
      "name": "Slack (Soporte)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        650,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      },
      "display": true
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\nEmail: {{$node[\"Webhook\"].json[\"body\"][\"email\"]}}\nMensaje: {{$node[\"Webhook\"].json[\"body\"][\"message\"]}}",
        "options": {}
      },
      "id": "4",
      "name": "Slack (Ventas)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      },
      "display": true
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje general:\nEmail: {{$node[\"Webhook\"].json[\"body\"][\"email\"]}}\nMensaje: {{$node[\"Webhook\"].json[\"body\"][\"message\"]}}",
        "options": {}
      },
      "id": "5",
      "name": "Slack (General)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        650,
        400
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      },
      "display": true
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "contains",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "6",
      "name": "IF (Soporte)",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        450,
        200
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "contains",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "7",
      "name": "IF (Ventas)",
      "type": "n8n-nodes-base.if",
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
              "value1": "{{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
              "operation": "contains",
              "value2": "otro"
            }
          ]
        }
      },
      "id": "8",
      "name": "IF (Otro)",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        450,
        400
      ]
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
            "node": "IF (Soporte)",
            "type": "main",
            "index": 0
          },
          {
            "node": "IF (Ventas)",
            "type": "main",
            "index": 0
          },
          {
            "node": "IF (Otro)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF (Soporte)": {
      "main": [
        [
          {
            "node": "Slack (Soporte)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF (Ventas)": {
      "main": [
        [
          {
            "node": "Slack (Ventas)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF (Otro)": {
      "main": [
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
  "active": false,
  "settings": {},
  "id": "YOUR_WORKFLOW_ID"
}
```

### Notas importantes:

1. **Credenciales**: Debes reemplazar `YOUR_OPENAI_CREDENTIALS_ID` y `YOUR_SLACK_CREDENTIALS_ID` con los IDs de tus credenciales configuradas en n8n.

2. **Modelo de OpenAI**: El workflow usa `gpt-3.5-turbo` por defecto. Puedes cambiarlo a otro modelo si lo prefieres.

3. **Canales de Slack**: Asegúrate de que los canales (#support, #sales, #general) existan en tu espacio de trabajo de Slack.

4. **Webhook**: El webhook se configurará en la ruta `/webhook` con método POST. Puedes cambiar la ruta si lo necesitas.

5. **Activación**: El workflow está configurado como inactivo (`"active": false`). Debes activarlo en n8n para que funcione.

6. **Formato del body**: El workflow espera un JSON en el body del webhook con este formato:
   ```json
   {
     "email": "usuario@example.com",
     "message": "Mi mensaje de prueba"
   }
   ```

Para implementar este workflow:
1. Copia el JSON completo
2. Ve a n8n y crea un nuevo workflow
3. Selecciona "Import from JSON" y pega el contenido
4. Configura las credenciales necesarias
5. Activa el workflow