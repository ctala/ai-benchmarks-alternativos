# MiniMax M2.7 (directo) — code_generation/n8n_workflow_json

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.24 | quality: 7.92
- latency_total: 22.602s | tokens_per_second: 90.6
- input_tokens: 157 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

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

# Workflow N8N - Clasificación de Mensajes con OpenAI y Slack

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificador de Mensajes - Webhook → OpenAI → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {
          "rawBody": false
        }
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "clasificador-mensajes"
    },
    {
      "parameters": {
        "jsCode": "// Extraer email y message del body\nconst body = $input.first().json.body;\n\nreturn {\n  json: {\n    email: body.email || '',\n    message: body.message || '',\n    timestamp: new Date().toISOString()\n  }\n};"
      },
      "id": "extract-data",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": {
          "values": {
            "name": "gpt-4o-mini"
          }
        },
        "prompt": {
          "values": {
            "messages": [
              {
                "role": "system",
                "content": "Eres un clasificador de mensajes. Analiza el siguiente mensaje y clasifícalo en UNA de estas tres categorías: \"soporte\", \"ventas\" u \"otro\".\n\nReglas:\n- \"soporte\": Para problemas técnicos, ayuda con productos/servicios, bugs, errores, configuración\n- \"ventas\": Para consultas de compra, precios, demos, licencias, planes, negociación\n- \"otro\": Para todo lo demás (feedback general, preguntas informativas, contactos, etc)\n\nResponde SOLO con la categoría en minúsculas: soporte, ventas u otro."
              },
              {
                "role": "user",
                "content": "={{ $json.message }}"
              }
            ]
          }
        },
        "options": {
          "maxTokens": 50,
          "temperature": 0
        }
      },
      "id": "openai-classify",
      "name": "OpenAI - Clasificador",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [650, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "mode": "name",
          "value": "={{ $json.categoria }}"
        },
        "text": {
          "values": {
            "text": "=📬 *Nuevo mensaje recibido*\n\n*Email:* {{ $('Extraer Datos').item.json.email }}\n*Categoría:* {{ $json.categoria.toUpperCase() }}\n*Mensaje:*\n{{ $('Extraer Datos').item.json.message }}"
          }
        },
        "options": {
          "username": "Bot Clasificador"
        }
      },
      "id": "slack-soporte",
      "name": "Slack - #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [850, 150],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credentials",
          "name": "Slack API"
        }
      },
      "continueOnFail": true
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "mode": "name",
          "value": "={{ $json.categoria }}"
        },
        "text": {
          "values": {
            "text": "=📬 *Nuevo mensaje recibido*\n\n*Email:* {{ $('Extraer Datos').item.json.email }}\n*Categoría:* {{ $json.categoria.toUpperCase() }}\n*Mensaje:*\n{{ $('Extraer Datos').item.json.message }}"
          }
        },
        "options": {
          "username": "Bot Clasificador"
        }
      },
      "id": "slack-ventas",
      "name": "Slack - #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [850, 300],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credentials",
          "name": "Slack API"
        }
      },
      "continueOnFail": true
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "mode": "name",
          "value": "={{ $json.categoria }}"
        },
        "text": {
          "values": {
            "text": "=📬 *Nuevo mensaje recibido*\n\n*Email:* {{ $('Extraer Datos').item.json.email }}\n*Categoría:* {{ $json.categoria.toUpperCase() }}\n*Mensaje:*\n{{ $('Extraer Datos').item.json.message }}"
          }
        },
        "options": {
          "username": "Bot Clasificador"
        }
      },
      "id": "slack-general",
      "name": "Slack - #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [850, 450],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credentials",
          "name": "Slack API"
        }
      },
      "continueOnFail": true
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": {
          "values": {
            "status": "success",
            "message": "Mensaje recibido y clasificado"
          }
        }
      },
      "id": "response",
      "name": "Responder",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1050, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
      "main": [
        [
          {
            "node": "OpenAI - Clasificador",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificador": {
      "main": [
        [
          {
            "node": "Slack - #support",
            "type": "main",
            "index": 0
          },
          {
            "node": "Slack - #sales",
            "type": "main",
            "index": 0
          },
          {
            "node": "Slack - #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - #support": {
      "main": [
        [
          {
            "node": "Responder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - #sales": {
      "main": [
        [
          {
            "node": "Responder",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - #general": {
      "main": [
        [
          {
            "node": "Responder",
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

## 📋 Flujo del Workflow

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│   Webhook   │────▶│Extraer Datos │────▶│OpenAI Clasifica │
│   (POST)    │     │  email+msg   │     │ soporte/ventas/ │
└─────────────┘     └──────────────┘     │     otro        │
                                          └────────┬────────┘
                                                   │
                    ┌──────────────────────────────