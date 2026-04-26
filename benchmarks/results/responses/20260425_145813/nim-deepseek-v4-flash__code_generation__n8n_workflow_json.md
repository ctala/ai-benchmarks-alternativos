# DeepSeek V4 Flash (NIM) — code_generation/n8n_workflow_json

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 6.52 | quality: 7.48
- latency_total: 49.319s | tokens_per_second: 33.6
- input_tokens: 126 | output_tokens: 1658
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes el workflow de n8n en formato JSON que cumple con todos los requisitos:

```json
{
  "name": "Clasificador de mensajes con OpenAI y Slack",
  "nodes": [
    {
      "parameters": {},
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "mi-webhook-unico",
      "path": "clasificar-mensaje",
      "options": {
        "responseMode": "onReceived"
      }
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con una de estas tres palabras, sin explicación adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "openai",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "openAiApi": "tus-credenciales-openai"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.output }}",
              "operation": "contains",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "if-soporte",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [650, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.output }}",
              "operation": "contains",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "if-ventas",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [650, 400]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\nEmail: {{ $node[\"Webhook\"].json.body.email }}\nMensaje: {{ $node[\"Webhook\"].json.body.message }}"
      },
      "id": "slack-soporte",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 150],
      "credentials": {
        "slackApi": "tus-credenciales-slack"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\nEmail: {{ $node[\"Webhook\"].json.body.email }}\nMensaje: {{ $node[\"Webhook\"].json.body.message }}"
      },
      "id": "slack-ventas",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 350],
      "credentials": {
        "slackApi": "tus-credenciales-slack"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje (categoría: otro):\nEmail: {{ $node[\"Webhook\"].json.body.email }}\nMensaje: {{ $node[\"Webhook\"].json.body.message }}"
      },
      "id": "slack-otro",
      "name": "Slack - Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 500],
      "credentials": {
        "slackApi": "tus-credenciales-slack"
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
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es soporte?": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "¿Es ventas?": {
      "main": [
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "versionId": "1.0.0",
  "active": true,
  "settings": {
    "executionOrder": "v1"
  },
  "tags": [],
  "id": "workflow-clasificador-mensajes"
}
```

## Instrucciones de configuración:

1. **Credenciales**: Reemplaza `"tus-credenciales-openai"` y `"tus-credenciales-slack"` con tus credenciales reales.

2. **Webhook**: El workflow se activará en la URL: `http://tu-instancia-n8n/webhook/clasificar-mensaje`

3. **Formato del body**: Envía una petición POST con:
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Necesito ayuda con mi cuenta"
}
```

4. **Canales de Slack**: Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu workspace de Slack.

## Flujo del workflow:

1. **Webhook** recibe la petición POST
2. **OpenAI** clasifica el mensaje usando GPT-3.5-turbo
3. **¿Es soporte?** y **¿Es ventas?** determinan la categoría
4. Según la clasificación, se envía el mensaje al canal correspondiente:
   - Soporte → `#support`
   - Ventas → `#sales`
   - Otro → `#general` (por defecto si no es soporte ni ventas)

El workflow está optimizado para manejar respuestas de OpenAI que puedan contener texto adicional, usando `contains` en lugar de igualdad exacta.