# MiMo V2.6 Pro — code_generation/n8n_workflow_json

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 6.31 | quality: 7.0
- latency_total: 156.077s | tokens_per_second: 79.8
- input_tokens: 122 | output_tokens: 12452
- judge_score: 3.0 | justificación: 

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

# Workflow N8N — Clasificador de Mensajes → Slack

```json
{
  "name": "Clasificador de Mensajes → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "e1a00001-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 340],
      "webhookId": "classify-message"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "extract-email",
              "name": "email",
              "value": "={{ $json.body?.email || $json.email }}",
              "type": "string"
            },
            {
              "id": "extract-message",
              "name": "message",
              "value": "={{ $json.body?.message || $json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "e1a00002-0002-4000-8000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 340]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "modelId": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un clasificador experto de mensajes de clientes. Analiza el mensaje y clasifícalo en UNA de estas tres categorías exactas:\n\n- \"soporte\" → problemas técnicos, errores, bugs, reclamos, ayuda con el producto.\n- \"ventas\" → compras, precios, planes, cotizaciones, demos, interés de compra.\n- \"otro\"   → cualquier otra cosa.\n\nResponde ÚNICAMENTE con la palabra exacta de la categoría. Nada más."
            },
            {
              "role": "user",
              "content": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "e1a00003-0003-4000-8000-000000000003",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [680, 340],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_CON_TU_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// ==========================================================\n// Extraer la clasificación limpia de la respuesta de OpenAI\n// ==========================================================\nconst raw = $input.first().json;\nconst campos = $('Extraer Campos').first().json;\n\nlet texto = '';\n\n// El formato del output varía según la versión del nodo OpenAI\nif (raw.message?.content)            texto = raw.message.content;\nelse if (raw.choices?.[0]?.message?.content) texto = raw.choices[0].message.content;\nelse if (raw.text)                   texto = raw.text;\nelse if (raw.output)                 texto = raw.output;\nelse if (raw.content)                texto = raw.content;\nelse                                 texto = JSON.stringify(raw);\n\n// Normalizar: minúsculas, quitar signos y espacios extra\ntexto = texto.trim().toLowerCase().replace(/[^a-záéíóúñ]/g, '');\n\n// Validar que sea una categoría conocida\nconst validas = ['soporte', 'ventas', 'otro'];\nconst classification = validas.includes(texto) ? texto : 'otro';\n\nreturn [{\n  json: {\n    classification,\n    email:   campos.email,\n    message: campos.message\n  }\n}];"
      },
      "id": "e1a00004-0004-4000-8000-000000000004",
      "name": "Extraer Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [900, 340]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "version": 1
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "version": 1
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "version": 1
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": true,
          "fallbackOutputName": "fallback → #general"
        }
      },
      "id": "e1a00005-0005-4000-8000-000000000005",
      "name": "Enrutar por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 340]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🔔 *Nuevo mensaje de SOPORTE*\n━━━━━━━━━━━━━━━━━\n*📧 Email:* `{{ $json.email }}`\n*💬 Mensaje:*\n> {{ $json.message }}\n━━━━━━━━━━━━━━━━━",
        "otherOptions": {}
      },
      "id": "e1a00006-0006-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 120],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo mensaje de VENTAS*\n━━━━━━━━━━━━━━━━━\n*📧 Email:* `{{ $json.email }}`\n*💬 Mensaje:*\n> {{ $json.message }}\n━━━━━━━━━━━━━━━━━",
        "otherOptions": {}
      },
      "id": "e1a00007-0007-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 340],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📝 *Nuevo mensaje (general)*\n━━━━━━━━━━━━━━━━━\n*📧 Email:* `{{ $json.email }}`\n*💬 Mensaje:*\n> {{ $json.message }}\n━━━━━━━━━━━━━━━━━",
        "otherOptions": {}
      },
      "id": "e1a00008-0008-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 560],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_ID_SLACK",
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
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Extraer Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Clasificación": {
      "main": [
        [
          {
            "node": "Enrutar por Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por Clasificación": {
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
  },
  "settings": {
    "executionOrder": "v1"
  },
  "active": true
}
```

---

## Diagrama del flujo

```
  POST /webhook/classify-message
           │
           ▼
    ┌──────────────┐
    │   Webhook     │  Recibe {"email":"...","message":"..."}
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │Extraer Campos│  Extrae email + message
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │Clasificar IA │  OpenAI → "soporte" | "ventas" | "otro"
    │  (OpenAI)    │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │Extraer Clasif│  Limpia y normaliza la respuesta
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │   Switch     │── output 0 ──► Slack #support  🔔
    │ "Enrutar"    │── output 1 ──► Slack #sales    💰
    │              │── output 2 ──► Slack #general  📝
    │              │── fallback ──► Slack #general  📝
    └──────────────┘
```

---

## Qué necesitas configurar

| Elemento | Qué hacer |
|---|---|
| **OpenAI API** | Crear credencial en N8N con tu `sk-...` de OpenAI |
| **Slack API** | Crear credencial en N8N con un **Bot Token** (`xoxb-...`) que tenga permisos `chat:write` |
| **Canales** | Asegurarte de que `#support`, `#sales` y `#general` existan y que el bot esté invitado a ellos |
| **Modelo** | Por defecto usa `gpt-4o-mini` (barato y rápido). Puedes cambiarlo a `gpt-4o` para mayor precisión |

---

## Payload de prueba

```bash
curl -X POST https://TU_N8N/webhook/classify-message \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@ejemplo.com",
    "message": "Mi app se cierra solo cada vez que abro el módulo de reportes, es urgente!"
  }'
```

Esto clasificará como **`soporte`** → enviará a **#support**. ✅