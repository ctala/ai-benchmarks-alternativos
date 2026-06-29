# GLM 5.2 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.29 | quality: 8.32
- latency_total: 51.804s | tokens_per_second: 51.3
- input_tokens: 126 | output_tokens: 2660
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n. Para usarlo, simplemente copia el código, ve a tu instancia de n8n, haz clic en el botón de "Workflow" (o en el menú de los tres puntos en el lienzo vacío) y selecciona **"Import from File"** o pega el texto directamente con **"Paste to canvas"**.

```json
{
  "name": "Clasificacion de Mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        0,
        240
      ],
      "webhookId": "12345678-9abc-def0-1234-567890abcdef"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "content": "Eres un asistente que clasifica mensajes. Lee el siguiente mensaje y clasifícalo en EXACTAMENTE una de estas tres palabras: 'soporte', 'ventas' u 'otro'. Devuelve SOLO la palabra de la categoría, sin puntos ni comillas.\n\nMensaje: {{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-classify",
      "name": "OpenAI (Clasificar)",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        220,
        240
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.text.trim().toLowerCase() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "outputKey": "soporte"
            },
            {
              "value2": "ventas",
              "outputKey": "ventas"
            },
            {
              "value2": "otro",
              "outputKey": "otro"
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "switch-route",
      "name": "Switch (Ruta)",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        440,
        240
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
        "text": "=*Nuevo mensaje para SOPORTE*\n\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {
          "append": false
        }
      },
      "id": "slack-support",
      "name": "Slack (#support)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        680,
        0
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_SLACK_CREDENTIAL_ID",
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
        "text": "=*Nuevo mensaje para VENTAS*\n\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {
          "append": false
        }
      },
      "id": "slack-sales",
      "name": "Slack (#sales)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        680,
        240
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_SLACK_CREDENTIAL_ID",
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
        "text": "=*Nuevo mensaje GENERAL*\n\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {
          "append": false
        }
      },
      "id": "slack-general",
      "name": "Slack (#general)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        680,
        480
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "openai-classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI (Clasificar)": {
      "main": [
        [
          {
            "node": "switch-route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch (Ruta)": {
      "main": [
        [
          {
            "node": "slack-support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "slack-sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "slack-general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "active": false,
  "tags": []
}
```

### Notas para su funcionamiento:
1. **Credenciales**: Al importar el workflow, verás que los nodos de OpenAI y Slack te pedirán configurar las credenciales. Deberás crear una credencial de API Key de OpenAI y una de OAuth2 o Bot Token de Slack.
2. **Webhook**: El webhook estará esperando una petición POST en la ruta `https://[tu-url-de-n8n]/webhook/clasificar-mensaje`. El body del JSON debe contener los campos `email` y `message`.
   *Ejemplo de body:*
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Hola, quiero comprar 50 licencias de su software."
   }
   ```
3. **Canal de Slack**: Asegúrate de que el bot de Slack tenga permisos para publicar en los canales `#support`, `#sales` y `#general`.