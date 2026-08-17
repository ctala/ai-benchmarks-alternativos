# Gemini 3.6 Flash — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 7.51 | quality: 8.6
- latency_total: 18.495s | tokens_per_second: 226.3
- input_tokens: 115 | output_tokens: 4185
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para el workflow de n8n que cumple con los requisitos especificados. La estructura es clara y organizada, y un emprendedor podría usarla directamente con algunas configuraciones adicionales. Sin embargo, la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores.

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

Aquí tienes el JSON completo del workflow para n8n. 

### ¿Cómo importarlo en n8n?
1. Copia todo el código JSON de abajo.
2. Ve a tu instancia de n8n.
3. Crea un nuevo Workflow.
4. Haz clic en el menú de tres puntos (arriba a la derecha) y selecciona **"Import from JSON"** (o presiona `Ctrl + V` / `Cmd + V` directamente sobre el lienzo).
5. Configura tus credenciales de **OpenAI** y **Slack** en los nodos correspondientes.

```json
{
  "name": "Clasificador de Mensajes con IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "118b62fa-3e61-4fa3-a9d0-1c05d9b73648",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "messages": {
          "message": [
            {
              "role": "system",
              "content": "Eres un asistente de clasificación. Tu única tarea es clasificar el mensaje del usuario en una de las siguientes tres categorías estrictas:\n- soporte\n- ventas\n- otro\n\nResponde ÚNICAMENTE con una de esas tres palabras en minúsculas, sin puntos, sin comillas y sin texto adicional."
            },
            {
              "content": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "62d5832a-e8d1-4a4f-808d-8a9d18b6a1e1",
      "name": "Clasificador OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        470,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "REPLACE_WITH_YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "7a3e811b-0a7b-4029-9e8c-3e6181f21a99",
      "name": "Switch Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        690,
        300
      ]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:sos: *Nuevo ticket de Soporte*\n*De:* {{ $('Webhook POST').item.json.body.email }}\n*Mensaje:* {{ $('Webhook POST').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-111111111111",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        950,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nueva oportunidad de Ventas*\n*De:* {{ $('Webhook POST').item.json.body.email }}\n*Mensaje:* {{ $('Webhook POST').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-222222222222",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        950,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:speech_balloon: *Nuevo mensaje General*\n*De:* {{ $('Webhook POST').item.json.body.email }}\n*Mensaje:* {{ $('Webhook POST').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-333333333333",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        950,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Clasificador OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador OpenAI": {
      "main": [
        [
          {
            "node": "Switch Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoria": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

### Estructura del JSON de entrada (Webhook Payload):
Para probar tu Webhook, debes enviar una petición `POST` con la siguiente estructura en el **Body** (JSON):

```json
{
  "email": "cliente@ejemplo.com",
  "message": "Hola, necesito ayuda porque la plataforma no me deja iniciar sesión."
}
```

### Configuración requerida tras importar:
1. **OpenAI Node**: Vincula tu API Key de OpenAI.
2. **Slack Nodes**: Vincula tu cuenta/token de Slack y asegúrate de que el bot tenga acceso a los canales `#support`, `#sales` y `#general` (o cámbialos por los nombres/IDs de tus canales reales).