# Kimi K2 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.31 | quality: 8.4
- latency_total: 46.059s | tokens_per_second: 42.3
- input_tokens: 133 | output_tokens: 1950
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado. Aunque no profundiza en detalles avanzados, es práctica y útil para un emprendedor.

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

Aquí tienes el workflow completo en JSON para N8N:

```json
{
  "name": "Clasificación de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en UNA sola categoría: \"soporte\", \"ventas\" o \"otro\". Responde ÚNICAMENTE con la palabra de la categoría, sin explicaciones adicionales."
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
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Extraer la clasificación de la respuesta de OpenAI\nconst classification = $input.first().json.content.toLowerCase().trim();\n\n// Validar que sea una de las categorías permitidas\nconst validCategories = ['soporte', 'ventas', 'otro'];\nconst category = validCategories.includes(classification) ? classification : 'otro';\n\nreturn {\n  json: {\n    email: $input.first().json.body.email,\n    message: $input.first().json.body.message,\n    classification: category\n  }\n};"
      },
      "id": "code-node",
      "name": "Procesar Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        650,
        300
      ]
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
            },
            {
              "value": "otro",
              "output": 2
            }
          ]
        }
      },
      "id": "switch-node",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=📧 *Nuevo mensaje de soporte*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-support",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1050,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje de ventas*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-sales",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1050,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📨 *Nuevo mensaje general*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1050,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"success\": true,\n  \"email\": $json.email,\n  \"classification\": $json.classification,\n  \"message\": \"Mensaje enviado al canal correspondiente\"\n}"
      },
      "id": "respond-to-webhook",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ]
    }
  ],
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
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
            "node": "Procesar Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Procesar Clasificación": {
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
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
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
    },
    "Slack Soporte": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack Ventas": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack General": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

## Instrucciones de configuración:

### 1. **Credenciales necesarias:**
- Reemplaza `"TU_CREDENCIAL_OPENAI"` con el ID de tu credencial de OpenAI
- Reemplaza `"TU_CREDENCIAL_SLACK"` con el ID de tu credencial de Slack

### 2. **URL del Webhook:**
```
POST https://TU-INSTANCIA-N8N/webhook/clasificar-mensaje
```

### 3. **Body de ejemplo para probar:**
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Tengo un problema con mi factura, no me llegó el recibo"
}
```

### Flujo del workflow:
```
Webhook → OpenAI (clasifica) → Code (procesa) → Switch (rutea) → Slack → Respuesta
```

¿Necesitas que ajuste algo del workflow?