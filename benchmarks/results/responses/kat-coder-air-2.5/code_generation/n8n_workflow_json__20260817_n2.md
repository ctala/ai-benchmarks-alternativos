# KAT Coder Air v2.5 — code_generation/n8n_workflow_json

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.86 | quality: 8.4
- latency_total: 10.495s | tokens_per_second: 195.1
- input_tokens: 125 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un webhook, extracción de campos y clasificación de IA. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores. Es práctica para un emprendedor, pero podría beneficiarse de más contexto o ejemplos.

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



# Workflow n8n — Clasificación de Mensajes por IA

Aquí tienes el JSON completo. Solo necesitas configurar las credenciales de **OpenAI** y **Slack** en n8n antes de importarlo.

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "responseData": "lastNode"
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-300, 0],
      "webhookId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "extract-fields",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [-100, 0]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "maxTokens": 50,
          "temperature": 0.1
        }
      },
      "id": "ai-classify",
      "name": "Classify Message",
      "type": "@n8n/n8n-nodes-langchain.llmChain",
      "typeVersion": 1.4,
      "position": [100, 0],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Account"
        }
      },
      "parameters": {
        "promptType": "text",
        "text": "={{ $json.message }}\n\nClasifica este mensaje en exactamente una de estas tres categorías: soporte, ventas, otro. Responde SOLO con la categoría, sin explicaciones.",
        "systemMessage": "Eres un clasificador de mensajes. Tu única función es clasificar mensajes en: soporte, ventas u otro. Responde ÚNICAMENTE con una de esas tres palabras."
      }
    },
    {
      "parameters": {
        "rules": {
          "options": {
            "upperCase": true
          },
          "conditions": [
            {
              "values": {
                "string": [
                  {
                    "name": "category",
                    "value": "SOPORTE"
                  }
                ]
              },
              "operations": {
                "operator": "equals"
              }
            },
            {
              "values": {
                "string": [
                  {
                    "name": "category",
                    "value": "VENTAS"
                  }
                ]
              },
              "operations": {
                "operator": "equals"
              }
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [300, 0]
    },
    {
      "parameters": {
        "channelId": "#support",
        "text": "📧 Nuevo ticket de SOPORTE\n\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Categoría: {{ $json.category }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [500, -100],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channelId": "#sales",
        "text": "💰 Nuevo lead de VENTAS\n\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Categoría: {{ $json.category }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [500, 100],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channelId": "#general",
        "text": "📋 Mensaje clasificado como OTRO\n\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Categoría: {{ $json.category }}",
        "otherOptions": {}
      },
      "id": "slack-otro",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [500, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
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
  "settings": {
    "executionOrder": "v1",
    "saveManualExecutions": true,
    "callerPolicy": "anyWorkflow"
  },
  "staticData": null,
  "tags": []
}
```

---

## 📐 Diagrama del flujo

```
POST /clasificar-mensaje
        │
        ▼
  ┌─────────────┐
  │  Webhook    │
  └──────┬──────┘
         │
         ▼
  ┌───────────────┐
  │Extract Fields │  ← Extrae email + message del body
  └───────┬───────┘
          │
          ▼
  ┌──────────────────┐
  │Classify Message  │  ← GPT-4o-mini clasifica el mensaje
  │   (OpenAI)       │
  └──────