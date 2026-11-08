# Claude Sonnet 5.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.26 | quality: 8.6
- latency_total: 31.889s | tokens_per_second: 176.5
- input_tokens: 177 | output_tokens: 5629
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro en la clasificación de mensajes y el envío a Slack. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack o la gestión de errores.

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

# Workflow de n8n: clasificación de mensajes con IA y envío a Slack

```json
{
  "name": "Clasificador de mensajes con IA -> Slack",
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
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1000001-0000-4000-8000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f1000001-0000-4000-8000-000000000002",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 300]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "GPT-4O-MINI"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes de clientes. Clasifica el mensaje del usuario en UNA sola categoría: \"soporte\" (problemas técnicos, errores, ayuda con un producto o servicio ya contratado), \"ventas\" (precios, cotizaciones, compras, demos, información comercial) u \"otro\" (cualquier otra cosa). Responde ÚNICAMENTE con una palabra en minúsculas: soporte, ventas u otro. Sin puntuación ni explicaciones.",
              "role": "system"
            },
            {
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "OpenAI - Clasificar",
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
              "id": "f1000003-0000-4000-8000-000000000001",
              "name": "categoria",
              "value": "={{ (() => { const raw = ($json.message?.content || $json.output?.[0]?.content?.[0]?.text || $json.text || '').toString().trim().toLowerCase(); if (raw.includes('soporte')) return 'soporte'; if (raw.includes('ventas')) return 'ventas'; return 'otro'; })() }}",
              "type": "string"
            },
            {
              "id": "f1000003-0000-4000-8000-000000000002",
              "name": "email",
              "value": "={{ $('Extraer campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "f1000003-0000-4000-8000-000000000003",
              "name": "message",
              "value": "={{ $('Extraer campos').item.json.message }}",
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
      "position": [660, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "c0000001-0000-4000-8000-000000000002",
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
      "name": "Switch por categoría",
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
        "text": "=🛠️ *Nuevo mensaje de SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 160],
      "webhookId": "slack-support-node",
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
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 320],
      "webhookId": "slack-sales-node",
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
        "text": "=📩 *Nuevo mensaje (OTRO)*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 480],
      "webhookId": "slack-general-node",
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
          { "node": "Extraer campos", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer campos": {
      "main": [
        [
          { "node": "OpenAI - Clasificar", "type": "main", "index": 0 }
        ]
      ]
    },
    "OpenAI - Clasificar": {
      "main": [
        [
          { "node": "Normalizar clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Normalizar clasificación": {
      "main": [
        [
          { "node": "Switch por categoría", "type": "main", "index": 0 }
        ]
      ]
    },
    "Switch por categoría": {
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
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "active": false,
  "tags": []
}
```

## Cómo funciona

| Nodo | Función |
|---|---|
| **Webhook** | Recibe un `POST` en `/webhook/clasificar-mensaje` (o `/webhook-test/...` en modo prueba). |
| **Extraer campos** | Toma `email` y `message` de `body`. |
| **OpenAI - Clasificar** | Con `temperature: 0`, devuelve una sola palabra: `soporte`, `ventas` u `otro`. |
| **Normalizar clasificación** | Limpia la respuesta de la IA. Si no coincide con soporte o ventas, la marca como `otro`. También recupera `email` y `message`, porque la salida de OpenAI no los conserva. |
| **Switch por categoría** | Tiene 3 salidas: `soporte`, `ventas` y `otro` (la de fallback). |
| **Slack (x3)** | Envía el mensaje a `#support`, `#sales` o `#general`. |

## Antes de usarlo

1. **Importar:** en n8n ve a *Workflows → Import from File/URL*, o pega el JSON con `Ctrl+V` en el canvas.
2. **Credenciales:** asigna tus credenciales de **OpenAI** y de **Slack** en los nodos correspondientes. Los IDs `REEMPLAZAR_...` son placeholders.
3. **Slack:** el bot necesita el scope `chat:write` y debe estar invitado a los canales (`/invite @tu-bot`). Para canales públicos sin invitar, añade `chat:write.public`.
4. **Versión de n8n:** el JSON está pensado para versiones recientes de n8n (1.x). Si el nodo de OpenAI da error de parámetros, vuelve a seleccionar el modelo en la interfaz. El resto del flujo no cambia.

## Prueba rápida

```bash
curl -X POST https://TU-INSTANCIA/webhook-test/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"Hola, quiero saber el precio del plan empresarial"}'
```

Este ejemplo debería ir a `#sales`.

Si quieres, puedo añadir un nodo **Respond to Webhook** para devolver la categoría al cliente, o un manejo de errores por si falla OpenAI.