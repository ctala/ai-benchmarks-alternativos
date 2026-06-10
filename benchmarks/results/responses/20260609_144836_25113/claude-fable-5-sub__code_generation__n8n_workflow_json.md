# Claude Fable 5 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-fable-5`
- success: True  | final: 7.04 | quality: 9.34
- latency_total: 35.835s | tokens_per_second: 104.7
- input_tokens: 2 | output_tokens: 3753

## Respuesta completa

Aquí está el workflow completo. Webhook → extracción → clasificación con OpenAI → Switch → 3 canales Slack:

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
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
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en exactamente una de estas tres categorías: soporte, ventas, otro. Responde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin puntuación ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "c1",
              "name": "classification",
              "value": "={{ $json.message.content.toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "c2",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "c3",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Normalizar Clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [900, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "r1",
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
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "r2",
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
              "outputKey": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "otro"
        }
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Switch Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo mensaje de SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1380, 120],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CREDENTIAL_ID",
          "name": "Slack account"
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
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1380, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CREDENTIAL_ID",
          "name": "Slack account"
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
        "text": "=📩 *Nuevo mensaje (OTRO)*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1380, 480],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CREDENTIAL_ID",
          "name": "Slack account"
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
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Normalizar Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Clasificación": {
      "main": [
        [
          {
            "node": "Switch Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Clasificación": {
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
  },
  "settings": {
    "executionOrder": "v1"
  },
  "active": false
}
```

**Notas para importarlo:**

1. **Credenciales**: reemplaza los `REEMPLAZAR_CREDENTIAL_ID` por tus credenciales reales de OpenAI y Slack después de importar (n8n las pide al abrir cada nodo).
2. **Robustez de clasificación**: el system prompt fuerza respuesta de una sola palabra + `temperature: 0` + el nodo "Normalizar Clasificación" hace `toLowerCase().trim()`. Cualquier respuesta inesperada del modelo cae al fallback → `#general` (no se pierde nada).
3. **Path del webhook**: `POST https://tu-n8n.com/webhook/clasificar-mensaje` con body `{"email": "...", "message": "..."}`.
4. **Modelo**: usa `gpt-4o-mini` (barato y suficiente para clasificación de 3 categorías). Cámbialo si prefieres otro.
5. Siguiendo tu regla #4 del repo (cambios incrementales en PROD): impórtalo primero en DEV, valida con un par de POSTs de prueba por categoría, y recién ahí pásalo a PROD.