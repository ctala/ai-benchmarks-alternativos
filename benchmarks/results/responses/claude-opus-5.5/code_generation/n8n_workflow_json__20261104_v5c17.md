# Claude Opus 5.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.14 | quality: 7.2
- latency_total: 42.894s | tokens_per_second: 128.6
- input_tokens: 177 | output_tokens: 5515
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

# Workflow de n8n: clasificación de mensajes con OpenAI y envío a Slack

## JSON del workflow

```json
{
  "name": "Clasificador de Mensajes con IA → Slack",
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
      "position": [0, 300],
      "webhookId": "b7e4f6a2-1c3d-4e5f-9a8b-clasificador01"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1a1b1c1-0001-4000-8000-000000000101",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f1a1b1c1-0002-4000-8000-000000000102",
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
      "position": [220, 300]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "GPT-4O-MINI"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes de clientes. Debes clasificar el mensaje en UNA de estas categorías:\n\n- soporte: problemas técnicos, errores, incidencias, dudas sobre el uso del producto, cuentas, accesos.\n- ventas: precios, presupuestos, compras, planes, demos, información comercial, interés en contratar.\n- otro: cualquier cosa que no encaje en las anteriores.\n\nResponde ÚNICAMENTE con una de estas palabras exactas, en minúsculas y sin puntuación: soporte, ventas, otro",
              "role": "system"
            },
            {
              "content": "=Mensaje a clasificar:\n\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 5
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f2a2b2c2-0001-4000-8000-000000000201",
              "name": "categoria",
              "value": "={{ (() => { const c = ($json.message?.content || '').toString().trim().toLowerCase().replace(/[^a-z]/g, ''); return ['soporte', 'ventas'].includes(c) ? c : 'otro'; })() }}",
              "type": "string"
            },
            {
              "id": "f2a2b2c2-0002-4000-8000-000000000202",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "f2a2b2c2-0003-4000-8000-000000000203",
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
      "position": [660, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "c1c1c1c1-0001-4000-8000-000000000301",
                    "leftValue": "={{ $json.categoria }}",
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
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "c1c1c1c1-0002-4000-8000-000000000302",
                    "leftValue": "={{ $json.categoria }}",
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
      "name": "Enrutar por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:wrench: *Nuevo mensaje de SOPORTE*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 100],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
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
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
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
        "text": "=:envelope: *Nuevo mensaje (OTRO)*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 500],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          { "node": "Extraer Campos", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          { "node": "Clasificar con OpenAI", "type": "main", "index": 0 }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          { "node": "Normalizar Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Normalizar Clasificación": {
      "main": [
        [
          { "node": "Enrutar por Categoría", "type": "main", "index": 0 }
        ]
      ]
    },
    "Enrutar por Categoría": {
      "main": [
        [
          { "node": "Slack #support", "type": "main", "index": 0 }
        ],
        [
          { "node": "Slack #sales", "type": "main", "index": 0 }
        ],
        [
          { "node": "Slack #general", "type": "main", "index": 0 }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```

## Flujo

```
Webhook (POST) → Extraer Campos → Clasificar con OpenAI → Normalizar Clasificación → Switch
                                                                                      ├─ soporte → Slack #support
                                                                                      ├─ ventas  → Slack #sales
                                                                                      └─ otro    → Slack #general
```

## Cómo importarlo

1. En n8n, crea un workflow nuevo, pulsa los tres puntos (⋯) y elige **Import from File**, o simplemente pega el JSON con `Ctrl+V` en el lienzo.
2. Configura las credenciales:
   - **OpenAI:** abre el nodo "Clasificar con OpenAI" y selecciona o crea tu credencial con tu API key.
   - **Slack:** abre cada nodo de Slack y selecciona tu credencial (Bot Token con el permiso `chat:write`).
3. Invita al bot de Slack a los canales `#support`, `#sales` y `#general` con `/invite @tu-bot`.
4. Activa el workflow.

## Prueba con curl

```bash
curl -X POST https://TU-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@ejemplo.com",
    "message": "Hola, quisiera saber el precio del plan empresarial para 50 usuarios"
  }'
```

Este mensaje debería llegar a **#sales**.

Mientras pruebas, usa la URL de test (`/webhook-test/clasificar-mensaje`) con el botón "Listen for test event" activo.

## Detalles del diseño

- **Temperature 0 y maxTokens 5:** hacen que la respuesta de la IA sea determinista y corta.
- **Nodo "Normalizar Clasificación":** limpia la respuesta (espacios, mayúsculas, puntuación). Si la IA devuelve algo inesperado, lo clasifica como `otro`, así que el mensaje nunca se pierde.
- **Salida fallback del Switch:** cualquier valor que no sea `soporte` ni `ventas` va a `#general`.