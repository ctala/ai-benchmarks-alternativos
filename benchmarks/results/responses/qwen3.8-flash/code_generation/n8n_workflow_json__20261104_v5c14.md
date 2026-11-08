# Qwen 3.8 Flash — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 7.34 | quality: 8.2
- latency_total: 141.748s | tokens_per_second: 129.7
- input_tokens: 176 | output_tokens: 18381
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los pasos necesarios para el flujo de trabajo de N8N, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores.

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

Aquí tienes el workflow de n8n en JSON completo. Pégalo en n8n usando **Import from Clipboard**, luego asigna credenciales de **OpenAI** y **Slack**.

El webhook espera un `POST` con un body como este:

```json
{
  "email": "usuario@ejemplo.com",
  "message": "No puedo iniciar sesión"
}
```

```json
{
  "name": "Clasificar email con OpenAI y enviar a Slack",
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "nodes": [
    {
      "id": "webhook-post",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [260, 300],
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "options": {
          "rawBody": false,
          "responseCode": 200,
          "responseData": "noData"
        }
      }
    },
    {
      "id": "extract-email-message",
      "name": "Extract email and message",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [480, 300],
      "parameters": {
        "jsCode": "const body = $json.body ?? $json;\nconst email = body.email ?? '';\nconst message = body.message ?? '';\nconst messages = [\n  { role: 'system', content: 'Clasifica el siguiente mensaje en una sola palabra: soporte, ventas o otro. No agregues explicaciones.' },\n  { role: 'user', content: `Email: ${email}\\nMensaje: ${message}` }\n];\nreturn [{ json: { email, message, messages } }];"
      }
    },
    {
      "id": "openai-classify",
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2,
      "position": [700, 300],
      "parameters": {
        "resource": "chat",
        "operation": "messageCreate",
        "model": "gpt-4o-mini",
        "messagesJson": "={{ $json.messages }}",
        "options": {
          "temperature": 0
        }
      }
    },
    {
      "id": "parse-classification",
      "name": "Parse Classification",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [920, 300],
      "parameters": {
        "jsCode": "const item = $input.first().json;\nlet raw = item.output?.text ?? item.output?.classification ?? item.choices?.[0]?.message?.content ?? item.message?.content ?? item.text ?? item.result ?? '';\nif (typeof raw !== 'string') raw = JSON.stringify(raw);\nconst text = String(raw).toLowerCase();\nlet classification = 'otro';\nif (text.includes('soporte') || text.includes('support')) classification = 'soporte';\nelse if (text.includes('ventas') || text.includes('sales')) classification = 'ventas';\nconst previous = $('Extract email and message').first().json;\nreturn [{ json: { email: previous.email, message: previous.message, classification } }];"
      }
    },
    {
      "id": "switch-route",
      "name": "Route by classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1140, 300],
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-support",
                    "leftValue": "={{ $json.classification }}",
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
              "outputKey": "support"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-sales",
                    "leftValue": "={{ $json.classification }}",
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
              "outputKey": "sales"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-other",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "other"
            }
          ]
        }
      }
    },
    {
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 200],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": "#support",
        "text": "=Email: {{ $json.email }}\nClasificación: {{ $json.classification }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      }
    },
    {
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 300],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": "#sales",
        "text": "=Email: {{ $json.email }}\nClasificación: {{ $json.classification }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      }
    },
    {
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 400],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": "#general",
        "text": "=Email: {{ $json.email }}\nClasificación: {{ $json.classification }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extract email and message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract email and message": {
      "main": [
        [
          {
            "node": "OpenAI Classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "Parse Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Classification": {
      "main": [
        [
          {
            "node": "Route by classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by classification": {
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
  }
}
```

Notas rápidas:

- Si tu versión de n8n usa Slack con **channel ID** en lugar de nombre de canal, cambia `#support`, `#sales` y `#general` por los IDs reales de Slack.
- El nodo de OpenAI usa `gpt-4o-mini`; puedes cambiarlo por el modelo que tengas disponible.
- El nodo `Parse Classification` es defensivo: intenta leer la salida de OpenAI en varias estructuras posibles y siempre cae en `otro` si no reconoce `soporte` o `ventas`.