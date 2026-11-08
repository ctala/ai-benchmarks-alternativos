# Qwen 3.6 27B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.39 | quality: 8.4
- latency_total: 46.093s | tokens_per_second: 71.7
- input_tokens: 125 | output_tokens: 3303
- judge_score: 4.0 | justificación: La respuesta proporciona un workflow JSON preciso y relevante que cumple con los requisitos especificados, aunque carece de detalles sobre las rutas de Slack y podría profundizar más en la configuración de los nodos de Slack.

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

# Workflow n8n — Clasificación IA + Slack Routing

```json
{
  "name": "Clasificar Mensaje IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ],
      "webhookId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    },
    {
      "parameters": {
        "fieldsToSummarize": {
          "values": [
            {
              "operation": "set",
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "operation": "set",
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [
        470,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0,
          "maxTokens": 50
        },
        "hasOutputParser": false,
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una de estas tres categorías: \"soporte\", \"ventas\" o \"otro\".\n\nMensaje: {{ $json.message }}\n\nResponde SOLO con la categoría exacta, sin explicaciones ni texto adicional.",
        "schema": {
          "values": []
        }
      },
      "name": "OpenAI - Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.3,
      "position": [
        690,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "fieldsToSummarize": {
          "values": [
            {
              "operation": "set",
              "name": "clasificacion",
              "value": "={{ $json.output.trim().toLowerCase() }}"
            }
          ]
        },
        "options": {}
      },
      "name": "Limpiar Clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [
        910,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.clasificacion }}",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.clasificacion }}",
              "value2": "ventas"
            },
            {
              "value1": "={{ $json.clasificacion }}",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "Ruta por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.1,
      "position": [
        1130,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🔧 *Soporte*\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Clasificación: Soporte",
        "additionalFields": {}
      },
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1350,
        180
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Ventas*\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Clasificación: Ventas",
        "additionalFields": {}
      },
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1350,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📌 *Otro*\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Clasificación: Otro",
        "additionalFields": {}
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1350,
        420
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "responseBody": "={\n  \"status\": \"ok\",\n  \"clasificacion\": \"{{ $json.clasificacion }}\",\n  \"canal\": \"{{ $json.clasificacion === 'soporte' ? '#support' : $json.clasificacion === 'ventas' ? '#sales' : '#general' }}\"\n}",
        "options": {}
      },
      "name": "Respuesta Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1570,
        300
      ]
    }
  ],
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
            "node": "OpenAI - Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificar": {
      "main": [
        [
          {
            "node": "Limpiar Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Limpiar Clasificación": {
      "main": [
        [
          {
            "node": "Ruta por Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ruta por Clasificación": {
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
            "node": "Respuesta Webhook",
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
            "node": "Respuesta Webhook",
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
            "node": "Respuesta Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1",
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "saveDataErrorExecution": "all",
    "saveDataSuccessExecution": "all"
  },
  "staticData": null,
  "meta": {
    "instanceId": "n8n-instance"
  },
  "pinData": {},
  "versionId": "1"
}
```

---

## 📋 Flujo del Workflow

```
┌──────────────┐     ┌────────────────┐     ┌──────────────────────┐
│   Webhook    │────▶│  Extraer Campos │────▶│ OpenAI Clasificar    │
│  POST        │     │ email + message│     │ gpt-4o-mini          │
└──────────────┘     └────────────────┘     └──────────┬───────────┘
                                                       │
                                              ┌────────▼──────────┐
                                              │ Limpiar           │
                                              │ clasificación     │
                                              └────────┬──────────┘
                                                       │
                                              ┌────────▼──────────┐
                                              │ Switch (3 rutas)  │
                                              └───┬────┬────┬────┘
                              ┌─────────────────┐│    │    │    └──────────────────┐
                              │                 ▼    ▼    ▼                        │
                        ┌─────▼─────┐   ┌──────▼───┐ ┌───▼────┐           ┌───────▼──────┐
                        │Slack      │   │Slack     │ │Slack   │           │Respuesta     │
                        │#support   │   │#sales    │ │#general│           │Webhook JSON  │
                        └───────────┘   └──────────┘ └────────┘           └──────────────┘
```

## 🔧 Configuración previa requerida

| Credencial | Tipo | Descripción |
|---|---|---|
| `OpenAI Account` | OpenAI API | API Key con acceso a GPT-4o-mini |
| `Slack Account` | Slack (OAuth2) | Bot con permisos `chat:write` en los 3 canales |

## 🚀 Ejemplo de petición de prueba

```bash
curl -X POST https://tu-n8n.com/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@ejemplo.com",
    "message": "Mi pedido no ha llegado y necesito ayuda"
  }'
```

> **Nota:** Reemplaza `TU_CREDENCIAL_OPENAI` y `TU_CREDENCIAL_SLACK` con los IDs reales de tus credenciales en n8n. El nodo `OpenAI - Clasificar` usa `temperature: 0` para garantizar respuestas deterministas y consistentes.