# Kimi K2.6 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.23 | quality: 8.6
- latency_total: 92.44s | tokens_per_second: 81.8
- input_tokens: 132 | output_tokens: 7564
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado. Aunque la profundidad es adecuada, podría incluir más detalles sobre la configuración de credenciales o manejo de errores para mejorar la utilidad práctica.

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

 Aquí tienes el workflow completo para **n8n**. Al importarlo, solo necesitarás configurar tus credenciales de **OpenAI** y **Slack**.

```json
{
  "name": "Webhook Clasificador IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasifica-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-trigger-01",
      "name": "Webhook",
      "type": "@n8n/nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "clasifica-mensaje"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el siguiente mensaje en una de estas categorías exactas: soporte, ventas, otro. Responde ÚNICAMENTE con una de esas tres palabras en minúsculas, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "=Email: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "openai-01",
      "name": "OpenAI",
      "type": "@n8n/nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": null,
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const input = items[0].json;\nlet classification = '';\n\nif (input.message && input.message.content) {\n  classification = input.message.content.toLowerCase().trim();\n} else if (input.content) {\n  classification = input.content.toLowerCase().trim();\n} else {\n  classification = 'otro';\n}\n\nreturn [{\n  json: {\n    email: input.body?.email || input.email,\n    message: input.body?.message || input.message,\n    classification: classification\n  }\n}];"
      },
      "id": "code-01",
      "name": "Normalize",
      "type": "@n8n/nodes-base.code",
      "typeVersion": 2,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "mode": "rules",
        "outputs": 3,
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "output": 0,
              "operation": "equal"
            },
            {
              "value": "ventas",
              "output": 1,
              "operation": "equal"
            }
          ]
        },
        "dataType": "string",
        "value1": "={{ $json.classification }}",
        "fallbackOutput": 2
      },
      "id": "switch-01",
      "name": "Switch",
      "type": "@n8n/nodes-base.switch",
      "typeVersion": 2.1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=*Nuevo mensaje clasificado* 🛠️\n• *Email:* {{ $json.email }}\n• *Categoría:* {{ $json.classification }}\n• *Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support-01",
      "name": "Slack Support",
      "type": "@n8n/nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": null,
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=*Nuevo mensaje clasificado* 💰\n• *Email:* {{ $json.email }}\n• *Categoría:* {{ $json.classification }}\n• *Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales-01",
      "name": "Slack Sales",
      "type": "@n8n/nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": null,
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=*Nuevo mensaje clasificado* 📌\n• *Email:* {{ $json.email }}\n• *Categoría:* {{ $json.classification }}\n• *Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general-01",
      "name": "Slack General",
      "type": "@n8n/nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": null,
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
            "node": "Normalize",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
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
  "staticData": null,
  "tags": []
}
```

### Instrucciones de uso

1. **Importa** el JSON en n8n (Workflows → Import from file).
2. **Conecta tus credenciales**:
   - OpenAI: en el nodo "OpenAI".
   - Slack: en los tres nodos de Slack (puedes usar la misma credencial).
3. **Activa el workflow** y obtén la URL del webhook (ej: `https://tun8n.app/webhook/clasifica-mensaje`).
4. **Envía un POST** con este body de ejemplo:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Hola, quiero comprar una licencia enterprise"
   }
   ```

El flujo clasificará el mensaje con OpenAI y lo enviará al canal de Slack correspondiente.