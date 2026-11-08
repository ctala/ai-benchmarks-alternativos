# Claude Fable 5.1 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.93 | quality: 8.6
- latency_total: 59.075s | tokens_per_second: 103.0
- input_tokens: 177 | output_tokens: 6082
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un JSON bien estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack o manejo de errores.

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

Aquí tienes el workflow completo, listo para importar en n8n (**Workflows → Import from file / Paste JSON**):

```json
{
  "name": "Clasificador de mensajes con IA → Slack",
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
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1e2d3c4-0001-4000-8000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f1e2d3c4-0002-4000-8000-000000000002",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer datos",
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
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en exactamente UNA de estas categorías: soporte, ventas, otro.\n\n- soporte: problemas técnicos, errores, dudas de uso, incidencias con el producto o servicio.\n- ventas: interés en comprar, precios, planes, presupuestos, demos, contratación.\n- otro: cualquier cosa que no encaje en las anteriores.\n\nResponde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "simplify": true,
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "OpenAI - Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1e2d3c4-0003-4000-8000-000000000003",
              "name": "categoria",
              "value": "={{ ['soporte','ventas','otro'].includes($json.message.content.trim().toLowerCase()) ? $json.message.content.trim().toLowerCase() : 'otro' }}",
              "type": "string"
            },
            {
              "id": "f1e2d3c4-0004-4000-8000-000000000004",
              "name": "email",
              "value": "={{ $('Extraer datos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "f1e2d3c4-0005-4000-8000-000000000005",
              "name": "message",
              "value": "={{ $('Extraer datos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [800, 300]
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c0000001-0000-4000-8000-000000000001",
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c0000002-0000-4000-8000-000000000002",
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
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c0000003-0000-4000-8000-000000000003",
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
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
          "fallbackOutput": 2
        }
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Switch por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1020, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo mensaje de SOPORTE*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack - #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1300, 100],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL",
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
        "text": "=💰 *Nuevo mensaje de VENTAS*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack - #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1300, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL",
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
        "text": "=📩 *Nuevo mensaje (OTRO)*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack - #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1300, 500],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL",
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
            "node": "Extraer datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer datos": {
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
            "node": "Normalizar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificación": {
      "main": [
        [
          {
            "node": "Switch por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por categoría": {
      "main": [
        [
          {
            "node": "Slack - #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - #general",
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
  "pinData": {},
  "tags": []
}
```

## Cómo funciona

| Nodo | Función |
|---|---|
| **Webhook** | Recibe `POST` en `/webhook/clasificar-mensaje` |
| **Extraer datos** | Saca `email` y `message` de `$json.body` |
| **OpenAI - Clasificar** | Prompt con `temperature: 0` que devuelve solo `soporte`, `ventas` u `otro` |
| **Normalizar clasificación** | Limpia la respuesta (trim + lowercase) y fuerza `otro` si el modelo devuelve algo inesperado. Recupera email/message del nodo anterior |
| **Switch por categoría** | 3 salidas; el fallback va a `otro` (índice 2) |
| **Slack - #support / #sales / #general** | Publica el mensaje formateado en el canal correspondiente |

## Pasos tras importar

1. **Credenciales**: abre los nodos de OpenAI y Slack y selecciona tus credenciales (los IDs `REEMPLAZAR_ID_CREDENCIAL` son placeholders).
2. **Slack**: el bot debe estar invitado a `#support`, `#sales` y `#general` y tener el scope `chat:write`. Si prefieres evitar resolver por nombre, cambia `mode` a `"id"` y pon el ID del canal (ej. `C0123ABCD`).
3. **Modelo**: puedes cambiar `gpt-4o-mini` por el que prefieras en el nodo de OpenAI.
4. **Activa** el workflow y prueba:

```bash
curl -X POST https://TU_N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"No puedo iniciar sesión, me da error 500"}'
```

Eso debería terminar en `#support`.