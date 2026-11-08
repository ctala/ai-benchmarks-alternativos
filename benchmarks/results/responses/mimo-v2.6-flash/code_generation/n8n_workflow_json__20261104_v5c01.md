# MiMo V2.6 Flash — code_generation/n8n_workflow_json

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.51 | quality: 8.4
- latency_total: 135.02s | tokens_per_second: 93.9
- input_tokens: 122 | output_tokens: 12682
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro en la clasificación y el enrutamiento. La profundidad es adecuada, pero podría beneficiarse de más detalles sobre la configuración de Slack. La claridad y utilidad son altas, haciendo que el flujo de trabajo sea comprensible y aplicable para un emprendedor.

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

# Workflow n8n: Clasificador de Email con Enrutamiento a Slack

```json
{
  "name": "Classify Email & Route to Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "options": {}
      },
      "id": "f1a1e001-0001-4001-8001-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-240, 300],
      "webhookId": "classify-email"
    },
    {
      "parameters": {
        "mode": "manual",
        "assignments": {
          "assignments": [
            {
              "id": "ext-email",
              "name": "email",
              "type": "string",
              "value": "={{ $json.body.email }}"
            },
            {
              "id": "ext-message",
              "name": "message",
              "type": "string",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "f1a1e001-0002-4002-8002-000000000002",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [0, 300]
    },
    {
      "parameters": {
        "method": "chat",
        "modelId": "gpt-4o-mini",
        "messages": {
          "systemMessage": "Eres un clasificador de mensajes. Tu ÚNICA tarea es determinar si un mensaje pertenece a la categoría 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con una de esas tres palabras, sin nada más.",
          "messageValues": [
            {
              "role": "user",
              "content": "Clasifica el siguiente mensaje:\n\n{{ $json.message }}\n\nCategorías: soporte | ventas | otro\nResponde solo con la categoría."
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "f1a1e001-0003-4003-8003-000000000003",
      "name": "Classify with AI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.7,
      "position": [240, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Parsear respuesta de OpenAI (multi-formato para compatibilidad)\nconst aiOutput = $input.first().json;\nlet content = '';\n\nif (aiOutput.message && aiOutput.message.content) {\n  content = aiOutput.message.content;\n} else if (aiOutput.output) {\n  content = aiOutput.output;\n} else if (aiOutput.choices && aiOutput.choices[0] && aiOutput.choices[0].message) {\n  content = aiOutput.choices[0].message.content;\n}\n\nconst normalized = content.trim().toLowerCase();\nconst classification = ['soporte', 'ventas'].includes(normalized) ? normalized : 'otro';\n\n// Recuperar datos originales del nodo Set\nconst original = $('Extract Fields').first().json;\n\nreturn [{\n  json: {\n    email: original.email,\n    message: original.message,\n    classification: classification\n  }\n}];"
      },
      "id": "f1a1e001-0004-4004-8004-000000000004",
      "name": "Parse Classification",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [480, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "renameOutput": true,
              "outputKey": "soporte",
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              }
            },
            {
              "renameOutput": true,
              "outputKey": "ventas",
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "combinator": "and",
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              }
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "f1a1e001-0005-4005-8005-000000000005",
      "name": "Route by Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [720, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=📬 *Mensaje recibido — Soporte*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.classification }}",
        "otherOptions": {}
      },
      "id": "f1a1e001-0006-4006-8006-000000000006",
      "name": "Slack - Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1000, 80],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💼 *Mensaje recibido — Ventas*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.classification }}",
        "otherOptions": {}
      },
      "id": "f1a1e001-0007-4007-8007-000000000007",
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1000, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📋 *Mensaje recibido — Otro*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.classification }}",
        "otherOptions": {}
      },
      "id": "f1a1e001-0008-4008-8008-000000000008",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1000, 520],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
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
            "node": "Classify with AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify with AI": {
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
            "node": "Route by Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Classification": {
      "main": [
        [
          {
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Sales",
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
    "executionOrder": "v1"
  },
  "active": false,
  "pinData": {}
}
```

---

## 📊 Diagrama del flujo

```
POST /classify-email
        │
        ▼
 ┌──────────────┐     ┌────────────────┐     ┌─────────────────┐
 │   Webhook    │────▶│ Extract Fields │────▶│ Classify with   │
 │   (POST)     │     │  email+message │     │ AI (OpenAI)     │
 └──────────────┘     └────────────────┘     └────────┬────────┘
                                                       │
                                                       ▼
                                             ┌──────────────────┐
                                             │Parse Classification│
                                             │(normaliza salida)  │
                                             └────────┬───────────┘
                                                      │
                                                      ▼
                                            ┌──────────────────┐
                                            │  Switch           │
                                            │  Route by         │
                                            │  Classification   │
                                            └──┬─────┬─────┬────┘
                                               │     │     │
                                    ┌──────────┘     │     └──────────┐
                                    ▼                ▼                ▼
                              ┌──────────┐    ┌──────────┐    ┌──────────┐
                              │  Slack   │    │  Slack   │    │  Slack   │
                              │#support  │    │#sales    │    │#general  │
                              └──────────┘    └──────────┘    └──────────┘
```

## 📋 Estructura de los nodos

| # | Nodo | Tipo | Función |
|---|------|------|---------|
| 1 | **Webhook** | `n8n-nodes-base.webhook` | Escucha POST en `/classify-email` |
| 2 | **Extract Fields** | `n8n-nodes-base.set` | Extrae `email` y `message` del body |
| 3 | **Classify with AI** | `n8n-nodes-base.openAi` | GPT-4o-mini clasifica el mensaje |
| 4 | **Parse Classification** | `n8n-nodes-base.code` | Normaliza respuesta y unifica datos |
| 5 | **Route by Classification** | `n8n-nodes-base.switch` | Enruta según clasificación |
| 6 | **Slack - Support** | `n8n-nodes-base.slack` | Envía a `#support` |
| 7 | **Slack - Sales** | `n8n-nodes-base.slack` | Envía a `#sales` |
| 8 | **Slack - General** | `n8n-nodes-base.slack` | Envía a `#general` (fallback) |

## 🔧 Antes de importar, reemplaza estos placeholders

| Placeholder | Qué poner |
|---|---|
| `YOUR_OPENAI_CREDENTIAL_ID` | Tu credencial de OpenAI en n8n |
| `YOUR_SLACK_CREDENTIAL_ID` | Tu credencial de Slack en n8n |

## 🧪 Ejemplo de prueba (curl)

```bash
curl -X POST https://TU_N8N.com/webhook/classify-email \
  -H "Content-Type: application/json" \
  -d '{
    "email": "juan@empresa.com",
    "message": "Tengo un problema con la facturación, no puedo descargar mi factura"
  }'
```

> **Resultado esperado:** GPT clasifica como `"soporte"` → el mensaje llega al canal **#support** de Slack.