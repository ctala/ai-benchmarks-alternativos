# Claude Sonnet 5.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.26 | quality: 8.6
- latency_total: 32.666s | tokens_per_second: 172.1
- input_tokens: 177 | output_tokens: 5623
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

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

## JSON completo

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
              "id": "f1000000-0000-4000-8000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f1000000-0000-4000-8000-000000000002",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer email y message",
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
              "content": "Eres un clasificador de mensajes de clientes. Clasifica el mensaje del usuario en UNA sola de estas categorías: soporte, ventas, otro.\n\n- soporte: problemas técnicos, errores, fallos, ayuda con un producto o servicio ya adquirido, facturación o incidencias.\n- ventas: interés en comprar, precios, presupuestos, demos, planes o contratación.\n- otro: cualquier cosa que no encaje en las anteriores.\n\nResponde ÚNICAMENTE con una palabra en minúsculas: soporte, ventas u otro. Sin puntuación ni explicaciones."
            },
            {
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
      "typeVersion": 1.1,
      "position": [440, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "runOnceForEachItem",
        "language": "javaScript",
        "jsCode": "const raw = String($json.message?.content ?? $json.text ?? '').toLowerCase().trim();\n\nlet categoria = 'otro';\nif (raw.includes('soporte')) categoria = 'soporte';\nelse if (raw.includes('ventas')) categoria = 'ventas';\n\nconst original = $('Extraer email y message').item.json;\n\nreturn {\n  json: {\n    email: original.email,\n    message: original.message,\n    categoria\n  }\n};"
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
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
                    "id": "c1000000-0000-4000-8000-000000000001",
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
                    "id": "c1000000-0000-4000-8000-000000000002",
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
      "webhookId": "slack-support-0001",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID",
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
      "webhookId": "slack-sales-0002",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID",
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
      "webhookId": "slack-general-0003",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          { "node": "Extraer email y message", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer email y message": {
      "main": [
        [
          { "node": "Clasificar con OpenAI", "type": "main", "index": 0 }
        ]
      ]
    },
    "Clasificar con OpenAI": {
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
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {}
}
```

## Cómo funciona

| Nodo | Función |
|---|---|
| **Webhook** | Recibe un `POST` en `/webhook/clasificar-mensaje` (o `/webhook-test/...` en modo prueba). |
| **Extraer email y message** | Toma `body.email` y `body.message` del request. |
| **Clasificar con OpenAI** | Usa `gpt-4o-mini` con temperatura 0 para devolver solo `soporte`, `ventas` u `otro`. |
| **Normalizar clasificación** | Limpia la respuesta de la IA y fuerza `otro` si no reconoce la categoría. También recupera `email` y `message`. |
| **Switch por categoría** | Enruta a la salida `soporte`, `ventas` o `otro` (fallback). |
| **Slack ×3** | Publica en `#support`, `#sales` o `#general`. |

## Pasos para usarlo

1. En n8n, ve a **Workflows → Import from File / URL** (o pega el JSON con `Ctrl+V` en el canvas).
2. Configura las credenciales:
   - **OpenAI API** (API key).
   - **Slack API** (OAuth2 o Access Token). El bot necesita el scope `chat:write` y estar invitado a los canales (`/invite @tu-bot`).
3. Activa el workflow.
4. Pruébalo con:

```bash
curl -X POST https://TU-INSTANCIA/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"Hola, me gustaría saber el precio del plan empresarial"}'
```

## Notas

- **Versión del nodo OpenAI:** uso `typeVersion 1.1`, que devuelve el texto en `$json.message.content`. Si tu instancia usa una versión más reciente (1.8 o superior) y el nodo da error, el código de "Normalizar clasificación" ya contempla `$json.text` como alternativa. Si la salida cambia, ajusta esa línea según la estructura que veas en la ejecución.
- **Validación:** si el webhook puede recibir datos incompletos, añade un nodo **IF** tras el Webhook para comprobar que `email` y `message` existen.
- **Respuesta HTTP:** ahora responde de inmediato (`onReceived`). Si quieres devolver la categoría al cliente, cambia `responseMode` a `lastNode` o añade un nodo **Respond to Webhook**.