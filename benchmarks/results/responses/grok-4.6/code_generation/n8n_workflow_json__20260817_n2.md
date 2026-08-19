# Grok 4.6 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.6`
- success: True  | final: 5.89 | quality: 6.72
- latency_total: 87.764s | tokens_per_second: 63.3
- input_tokens: 319 | output_tokens: 5556
- judge_score: 2.8 | justificación: 

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

```json
{
  "name": "Clasificador de Mensajes Webhook → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 400],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 400]
    },
    {
      "parameters": {
        "inputText": "={{ $json.message }}",
        "categories": {
          "categories": [
            {
              "category": "soporte",
              "description": "Problemas técnicos, incidencias, errores, tickets, ayuda o soporte al cliente"
            },
            {
              "category": "ventas",
              "description": "Precios, compras, cotizaciones, productos, contrataciones o consultas comerciales"
            },
            {
              "category": "otro",
              "description": "Cualquier mensaje que no sea de soporte ni de ventas"
            }
          ]
        },
        "options": {}
      },
      "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
      "name": "Clasificar Mensaje",
      "type": "@n8n/n8n-nodes-langchain.textClassifier",
      "typeVersion": 1,
      "position": [680, 400]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "d4e5f6a7-b8c9-0123-def0-234567890123",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [680, 620],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje de SOPORTE*\n*Email:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-c9d0-1234-ef01-345678901234",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 200],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje de VENTAS*\n*Email:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-d0e1-2345-f012-456789012345",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 400],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje (OTRO)*\n*Email:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a7b8c9d0-e1f2-3456-0123-567890123456",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [960, 600],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Clasificar Mensaje",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Mensaje": {
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
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1a2b3c4d-5e6f-7890-abcd-ef1234567890",
  "meta": {
    "templateCredsSetupCompleted": false,
    "instanceId": "n8n-instance"
  },
  "id": "wf-clasificador-mensajes",
  "tags": []
}
```

**Cómo usarlo**

1. En n8n: **Workflows → Import from File / URL / JSON** y pega este JSON.
2. Configura credenciales:
   - **OpenAI** en el nodo `OpenAI Chat Model`.
   - **Slack** (Bot Token) en los 3 nodos Slack. El bot necesita `chat:write` y estar invitado a `#support`, `#sales` y `#general`.
3. Activa el workflow. El webhook queda en:  
   `POST https://<tu-n8n>/webhook/clasificar-mensaje`

**Body de ejemplo**

```json
{
  "email": "cliente@ejemplo.com",
  "message": "No puedo iniciar sesión en la plataforma"
}
```

Flujo: Webhook → extrae `email`/`message