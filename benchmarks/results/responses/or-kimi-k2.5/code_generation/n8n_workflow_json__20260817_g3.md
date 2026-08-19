# Kimi K2.5 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.5 | quality: 8.6
- latency_total: 42.238s | tokens_per_second: 61.7
- input_tokens: 141 | output_tokens: 2604
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un workflow JSON funcional para el escenario descrito, con claridad y utilidad práctica para su implementación.

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

Aquí tienes el workflow completo en formato JSON para N8N. Copia y pega esto directamente en el canvas de N8N (Settings > Import from File o pegar como JSON):

```json
{
  "name": "Clasificación IA y Envío a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-inquiry",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger-001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "classify-inquiry"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {},
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el mensaje del usuario y clasifícalo EXACTAMENTE como una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin explicaciones adicionales."
            },
            {
              "role": "user",
              "content": "Mensaje: {{ $json.body.message }}\nEmail: {{ $json.body.email }}"
            }
          ]
        }
      },
      "id": "openai-classifier-002",
      "name": "OpenAI - Clasificador",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
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
            },
            {
              "value": "otro",
              "output": 2
            }
          ]
        },
        "options": {}
      },
      "id": "switch-router-003",
      "name": "Switch - Tipo de Mensaje",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 *Nuevo mensaje de Soporte*\n\n*De:* {{ $('Webhook').first().json.body.email }}\n*Mensaje:* {{ $('Webhook').first().json.body.message }}\n\n_Clasificado automáticamente por IA_",
        "otherOptions": {},
        "attachments": []
      },
      "id": "slack-support-004",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1000,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nueva consulta de Ventas*\n\n*De:* {{ $('Webhook').first().json.body.email }}\n*Mensaje:* {{ $('Webhook').first().json.body.message }}\n\n_Clasificado automáticamente por IA_",
        "otherOptions": {},
        "attachments": []
      },
      "id": "slack-sales-005",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1000,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📨 *Nuevo mensaje General*\n\n*De:* {{ $('Webhook').first().json.body.email }}\n*Mensaje:* {{ $('Webhook').first().json.body.message }}\n\n_Clasificado automáticamente por IA_",
        "otherOptions": {},
        "attachments": []
      },
      "id": "slack-general-006",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1000,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "options": {},
        "respondWith": "json",
        "json": "{\n  \"status\": \"success\",\n  \"classification\": \"{{ $('OpenAI - Clasificador').first().json.content }}\",\n  \"message\": \"Mensaje procesado y enviado al canal correspondiente\"\n}"
      },
      "id": "respond-to-webhook-007",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Switch - Tipo de Mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Tipo de Mensaje": {
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
    },
    "Slack - Soporte": {
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
    "Slack - Ventas": {
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
    "Slack - General": {
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
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": []
}
```

## Configuración necesaria:

1. **Credenciales**: Reemplaza `YOUR_OPENAI_CREDENTIAL_ID` y `YOUR_SLACK_CREDENTIAL_ID` con tus credenciales configuradas en N8N, o configúralas después de importar.

2. **Webhook URL**: Una vez activado, el endpoint será: `POST https://tun8ndominio.com/webhook/classify-inquiry`

3. **Body esperado**:
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Necesito ayuda con mi factura del mes pasado"
}
```

4. **Switch Node**: El nodo Switch compara la salida de OpenAI (que debe ser exactamente "soporte", "ventas" o "otro") y enruta al canal correspondiente.

5. **Respuesta**: El workflow responde al webhook con la clasificación realizada por la IA.

**Nota**: Asegúrate de tener configuradas las credenciales de OpenAI (API Key) y Slack (Bot Token) en tu instancia de N8N antes de ejecutar el workflow.