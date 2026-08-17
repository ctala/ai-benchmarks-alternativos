# Claude Sonnet 4.6 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.06 | quality: 8.4
- latency_total: 216.924s | tokens_per_second: 85.9
- input_tokens: 3 | output_tokens: 18625
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

## Respuesta completa

Aquí tienes el workflow completo listo para importar en N8N:

```json
{
  "name": "Clasificador de Mensajes → Slack",
  "nodes": [
    {
      "id": "wh-001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [180, 300],
      "webhookId": "11111111-1111-1111-1111-111111111111",
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "responseNode",
        "options": {}
      }
    },
    {
      "id": "ai-001",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.4,
      "position": [400, 300],
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de atención al cliente. Analiza el mensaje del usuario y responde ÚNICAMENTE con una de estas tres palabras en minúsculas:\n- soporte (problemas técnicos, errores, ayuda, quejas)\n- ventas (compras, precios, planes, upgrades, cotizaciones)\n- otro (cualquier otro tema)\n\nResponde SOLO con la palabra, nada más."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "simplify": true,
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZA_CON_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI API"
        }
      }
    },
    {
      "id": "code-001",
      "name": "Extraer Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [620, 300],
      "parameters": {
        "jsCode": "// Normaliza la clasificación del response de OpenAI\n// Compatible con distintas versiones del nodo OpenAI de n8n\nconst openaiJson = $input.item.json;\n\nlet rawText = '';\nif (typeof openaiJson.content === 'string') {\n  rawText = openaiJson.content;\n} else if (openaiJson.message && typeof openaiJson.message.content === 'string') {\n  rawText = openaiJson.message.content;\n} else if (Array.isArray(openaiJson.choices) && openaiJson.choices[0]?.message?.content) {\n  rawText = openaiJson.choices[0].message.content;\n}\n\nconst classification = rawText.trim().toLowerCase().replace(/[^a-záéíóú]/g, '');\nconst validClasses = ['soporte', 'ventas', 'otro'];\nconst finalClass = validClasses.includes(classification) ? classification : 'otro';\n\n// Recuperar campos del webhook original\nconst webhookBody = $('Webhook').item.json.body || {};\nconst email   = webhookBody.email   || '(sin email)';\nconst message = webhookBody.message || '(sin mensaje)';\n\nreturn [{ json: { email, message, classification: finalClass, rawClassification: rawText.trim() } }];"
      }
    },
    {
      "id": "sw-001",
      "name": "Enrutar por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [840, 300],
      "parameters": {
        "mode": "rules",
        "rules": {
          "values": [
            {
              "conditions": {
                "options": { "caseSensitive": false, "leftValue": "", "typeValidation": "strict" },
                "conditions": [
                  {
                    "id": "c1",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": { "type": "string", "operation": "equals" }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": { "caseSensitive": false, "leftValue": "", "typeValidation": "strict" },
                "conditions": [
                  {
                    "id": "c2",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": { "type": "string", "operation": "equals" }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      }
    },
    {
      "id": "sl-001",
      "name": "Slack → #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1060, 160],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "={{ `🔧 *Nuevo ticket de SOPORTE*\n\n📧 *Email:* ${$json.email}\n💬 *Mensaje:* ${$json.message}\n\n_Clasificado automáticamente por IA_` }}",
        "otherOptions": { "mrkdwn": true }
      },
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_ID_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "id": "sl-002",
      "name": "Slack → #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1060, 300],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "={{ `💰 *Nuevo lead de VENTAS*\n\n📧 *Email:* ${$json.email}\n💬 *Mensaje:* ${$json.message}\n\n_Clasificado automáticamente por IA_` }}",
        "otherOptions": { "mrkdwn": true }
      },
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_ID_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "id": "sl-003",
      "name": "Slack → #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1060, 440],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "={{ `📩 *Mensaje GENERAL*\n\n📧 *Email:* ${$json.email}\n💬 *Mensaje:* ${$json.message}\n\n_Clasificado automáticamente por IA_` }}",
        "otherOptions": { "mrkdwn": true }
      },
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_ID_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "id": "rw-001",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1280, 300],
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ { success: true, email: $('Extraer Clasificación').item.json.email, classification: $('Extraer Clasificación').item.json.classification, channel: $('Extraer Clasificación').item.json.classification === 'soporte' ? '#support' : ($('Extraer Clasificación').item.json.classification === 'ventas' ? '#sales' : '#general') } }}",
        "options": { "responseCode": 200 }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [[{ "node": "Clasificar con OpenAI", "type": "main", "index": 0 }]]
    },
    "Clasificar con OpenAI": {
      "main": [[{ "node": "Extraer Clasificación", "type": "main", "index": 0 }]]
    },
    "Extraer Clasificación": {
      "main": [[{ "node": "Enrutar por Clasificación", "type": "main", "index": 0 }]]
    },
    "Enrutar por Clasificación": {
      "main": [
        [{ "node": "Slack → #support", "type": "main", "index": 0 }],
        [{ "node": "Slack → #sales",   "type": "main", "index": 0 }],
        [{ "node": "Slack → #general", "type": "main", "index": 0 }]
      ]
    },
    "Slack → #support": {
      "main": [[{ "node": "Responder Webhook", "type": "main", "index": 0 }]]
    },
    "Slack → #sales": {
      "main": [[{ "node": "Responder Webhook", "type": "main", "index": 0 }]]
    },
    "Slack → #general": {
      "main": [[{ "node": "Responder Webhook", "type": "main", "index": 0 }]]
    }
  },
  "active": false,
  "settings": { "executionOrder": "v1" },
  "versionId": "22222222-2222-2222-2222-222222222222",
  "meta": { "templateCredsSetupCompleted": false },
  "id": "clasificador-mensajes-slack",
  "tags": []
}
```

---

## Arquitectura del flujo

```
POST /webhook/classify-message
        │
        ▼
[Webhook]  ← recibe { email, message }
        │
        ▼
[OpenAI gpt-4o-mini]  ← system prompt determinístico, temp=0, max 10 tokens
        │  responde: "soporte" | "ventas" | "otro"
        ▼
[Code: Extraer Clasificación]  ← normaliza + recupera email/message del webhook
        │
        ▼
[Switch: Enrutar por Clasificación]
   ┌────┴────┬──────────────┐
   ▼         ▼              ▼ (fallback)
[#support] [#sales]     [#general]
   └────┬────┴──────────────┘
        ▼
[Responder Webhook]  ← { success, email, classification, channel }
```

## Setup en 3 pasos

| Paso | Qué hacer |
|------|-----------|
| **1. Credencial OpenAI** | En N8N → Credentials → New → OpenAI. Reemplaza `REEMPLAZA_CON_ID_CREDENCIAL_OPENAI` con el ID generado. |
| **2. Credencial Slack** | En N8N → Credentials → New → Slack API (OAuth2). Reemplaza `REEMPLAZA_CON_ID_CREDENCIAL_SLACK` en los 3 nodos. |
| **3. Activar** | Cambia `"active": false` a `true`, o actívalo desde la UI. |

## Ejemplo de request

```bash
curl -X POST https://tu-n8n.com/webhook/classify-message \
  -H "Content-Type: application/json" \
  -d '{ "email": "cliente@empresa.com", "message": "No puedo acceder a mi cuenta" }'
```

**Response:**
```json
{
  "success": true,
  "email": "cliente@empresa.com",
  "classification": "soporte",
  "channel": "#support"
}
```

## Notas de diseño

- **Nodo Code** en el medio: hace el workflow robusto ante cambios en `typeVersion` del nodo OpenAI (la estructura del response varía entre versiones)
- **`temperature: 0` + `maxTokens: 10`**: maximiza determinismo y ahorra tokens — para clasificación pura no necesitas más
- **Switch con fallbackOutput**: cualquier respuesta inesperada del modelo cae siempre a `#general`, nunca falla silenciosamente
- **`responseMode: responseNode`**: el webhook no responde hasta que Slack confirma el envío, garantizando que no pierdas mensajes sin notificar