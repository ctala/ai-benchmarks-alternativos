# GLM 5.3 Flash — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.34 | quality: 8.4
- latency_total: 178.205s | tokens_per_second: 94.5
- input_tokens: 126 | output_tokens: 16839
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un JSON bien estructurado. Aunque la profundidad es moderada, la claridad y utilidad práctica son altas, lo que permite a un emprendedor implementar el flujo de trabajo directamente.

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

Aquí tienes el workflow completo. Cópialo y pégalo en n8n con **Ctrl+V** sobre el canvas (o usa "Import from File/Clipboard"):

```json
{
  "name": "Webhook → Clasificador IA → Slack",
  "nodes": [
    {
      "parameters": {
        "content": "## 📬 Clasificador de mensajes\n\n**1.** Configura las credenciales de **OpenAI** y **Slack** en cada nodo.\n**2.** Invita al bot de Slack a los canales (#support, #sales, #general).\n**3.** Activa el workflow y haz POST al webhook.\n\n**Body esperado:**\n```\n{ \"email\": \"...\", \"message\": \"...\" }\n```\n\nCategorías: soporte / ventas / otro (cualquier respuesta inválida cae en #general).",
        "height": 320,
        "width": 340
      },
      "id": "9a1f2b3c-0000-4a1b-8c2d-000000000000",
      "name": "Sticky Note",
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [-400, -280]
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "e1a2b3c4-1111-4a2b-8c3d-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "f7c8d9e0-aaaa-4bbb-8ccc-000000000001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1b2c3d4-0001-4e5f-8a6b-0000000000a1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "a1b2c3d4-0002-4e5f-8a6b-0000000000a2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "e1a2b3c4-2222-4a2b-8c3d-000000000002",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [240, 0]
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
              "content": "=Eres un clasificador de mensajes de clientes. Tu única tarea es clasificar el mensaje del usuario en EXACTAMENTE una de estas categorías:\n\n- soporte: problemas técnicos, errores, bugs, ayuda con el producto\n- ventas: precios, cotizaciones, compras, planes, demos\n- otro: cualquier cosa que no encaje en las anteriores\n\nReglas:\n- Responde ÚNICAMENTE con la palabra de la categoría, en minúsculas.\n- Sin puntuación, sin explicaciones, sin texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "e1a2b3c4-3333-4a2b-8c3d-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [480, 0]
    },
    {
      "parameters": {
        "jsCode": "// Normaliza la respuesta del modelo y vuelve a exponer los datos originales\nconst raw = ($json.message?.content ?? $json.text ?? '').toString();\n\n// Busca la primera categoría válida (tolera mayúsculas, puntos, comillas, etc.)\nconst match = raw.toLowerCase().match(/\\b(soporte|ventas|otro)\\b/);\nconst categoria = match ? match[1] : 'otro';\n\nreturn [{\n  json: {\n    categoria,\n    respuesta_modelo: raw.trim(),\n    email: $('Extraer Datos').first().json.email,\n    mensaje: $('Extraer Datos').first().json.message,\n  },\n}];"
      },
      "id": "e1a2b3c4-4444-4a2b-8c3d-000000000004",
      "name": "Normalizar Categoría",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [720, 0]
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-soporte-0001",
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
              "outputKey": "Soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-ventas-0002",
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
              "outputKey": "Ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-otro-0003",
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
              "outputKey": "Otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "e1a2b3c4-5555-4a2b-8c3d-000000000005",
      "name": "Router por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [960, 0]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo mensaje → SOPORTE*\n\n*De:* {{ $json.email }}\n\n*Mensaje:*\n{{ $json.mensaje }}",
        "otherOptions": {}
      },
      "id": "e1a2b3c4-6666-4a2b-8c3d-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1240, -240]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo mensaje → VENTAS*\n\n*De:* {{ $json.email }}\n\n*Mensaje:*\n{{ $json.mensaje }}",
        "otherOptions": {}
      },
      "id": "e1a2b3c4-7777-4a2b-8c3d-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1240, 0]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=💬 *Nuevo mensaje → GENERAL*\n\n*De:* {{ $json.email }}\n\n*Mensaje:*\n{{ $json.mensaje }}",
        "otherOptions": {}
      },
      "id": "e1a2b3c4-8888-4a2b-8c3d-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1240, 240]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
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
            "node": "Normalizar Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Categoría": {
      "main": [
        [
          {
            "node": "Router por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por Categoría": {
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {}
}
```

### Cómo funciona

**Webhook → Extraer Datos → Clasificar con OpenAI → Normalizar Categoría → Router (Switch) → Slack (#support / #sales / #general)**

Incluí un nodo Code ("Normalizar Categoría") que limpia la respuesta del modelo (mayúsculas, puntos, frases extra) y convierte cualquier salida inválida en `otro`, para que el Switch nunca falle.

### Antes de activarlo

- Configura las credenciales en los nodos: **OpenAI API** (o credential `openAiApi`) y **Slack OAuth2**.
- Invita al bot de Slack a los 3 canales (`/invite @tu-bot`). Si la búsqueda por nombre falla, cambia `mode: "name"` por `mode: "id"` y usa el ID del canal (`C0123456789`).
- El webhook responde cuando termina el flujo (`lastNode`). Si prefieres respuesta instantánea, cambia `responseMode` a `"onReceived"`.

### Prueba rápida

```bash
curl -X POST https://TU-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"La app no me deja iniciar sesión desde ayer"}'
```

Nota: usa el nodo OpenAI moderno (LangChain). Si tu versión de n8n no lo tiene, avísame y te doy una variante con HTTP Request directa a la API de OpenAI.