# Qwen 3.5 397B (Ollama Cloud) — code_generation/n8n_workflow_json

- model_id: `qwen3.5:397b-cloud`
- success: True  | final: 7.66 | quality: 8.32
- latency_total: 58.519s | tokens_per_second: 54.3
- input_tokens: 125 | output_tokens: 3178
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el código JSON completo para importar en tu instancia de N8N.

### Instrucciones previas:
1.  Copia el código de abajo.
2.  En N8N, ve al menú (tres puntos arriba a la derecha) -> **Import from File** o **Import from URL** (o simplemente pega el texto en el lienzo vacío con `Ctrl+V` / `Cmd+V`).
3.  **Importante:** Debes configurar las credenciales para los nodos de **OpenAI** y **Slack**, ya que el JSON contiene marcadores de posición para ellas.

### Workflow JSON

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ],
      "webhookId": "unique-webhook-id-123"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un asistente de clasificación. Tu única tarea es leer el mensaje del usuario y devolver EXACTAMENTE una de estas tres palabras en minúsculas: 'soporte', 'ventas' u 'otro'. No devuelvas nada más, ni explicaciones, ni puntuación."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_AQUI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "output": 0
            },
            {
              "value": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "switch-node",
      "name": "Clasificador (Switch)",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🆘 *Nuevo ticket de Soporte*\n\n*De:* {{ $json.body.email }}\n*Mensaje:* {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_AQUI",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nuevo Lead de Ventas*\n\n*De:* {{ $json.body.email }}\n*Mensaje:* {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_AQUI",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📩 *Mensaje General*\n\n*De:* {{ $json.body.email }}\n*Mensaje:* {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_AQUI",
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
            "node": "Clasificador (Switch)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador (Switch)": {
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
  "pinData": {}
}
```

### Cómo probarlo:

1.  Activa el workflow en N8N.
2.  Copia la URL del Webhook que se genera (ej: `https://tu-n8n.com/webhook/clasificar-mensaje`).
3.  Envía un POST usando Postman o curl:

```bash
curl -X POST https://tu-n8n.com/webhook/clasificar-mensaje \
   -H "Content-Type: application/json" \
   -d '{
     "email": "cliente@ejemplo.com",
     "message": "Hola, mi producto no enciende y necesito ayuda urgente."
   }'
```

*   Si el mensaje es sobre ayuda técnica, irá a `#support`.
*   Si es "Quiero comprar 100 licencias", irá a `#sales`.
*   Si es "Hola, ¿cómo están?", irá a `#general`.