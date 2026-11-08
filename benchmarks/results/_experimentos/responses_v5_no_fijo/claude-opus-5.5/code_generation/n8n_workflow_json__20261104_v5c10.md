# Claude Opus 5.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.13 | quality: 8.6
- latency_total: 44.172s | tokens_per_second: 123.1
- input_tokens: 177 | output_tokens: 5439
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro en la clasificación de mensajes y el envío a Slack. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o posibles errores. Es prácticamente útil para un emprendedor.

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

# Workflow de n8n: clasificador de mensajes con OpenAI y Slack

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
      "webhookId": "b7e1c2a0-1111-4abc-9def-clasificador01"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1a1-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f1a2-message",
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
              "content": "Eres un clasificador de mensajes de clientes. Debes clasificar cada mensaje en UNA de estas categorías:\n\n- soporte: problemas técnicos, errores, dudas de uso, incidencias, quejas sobre el funcionamiento del producto o servicio.\n- ventas: interés en comprar, precios, presupuestos, planes, demos, cotizaciones, descuentos o información comercial.\n- otro: cualquier mensaje que no encaje claramente en las anteriores.\n\nResponde ÚNICAMENTE con una de estas palabras en minúsculas, sin puntuación ni explicación: soporte, ventas, otro",
              "role": "system"
            },
            {
              "content": "=Mensaje a clasificar:\n\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 300]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "c1-categoria",
              "name": "categoria",
              "value": "={{ $json.message.content.toLowerCase().trim().replace(/[^a-z]/g, '') }}",
              "type": "string"
            },
            {
              "id": "c2-email",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "c3-message",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Preparar Datos",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "r1-soporte",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "r2-ventas",
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
        "text": "=:wrench: *Nuevo mensaje de SOPORTE*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n>{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 100]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n>{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:speech_balloon: *Nuevo mensaje (OTRO)*\n\n*Email:* {{ $json.email }}\n*Mensaje:*\n>{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 500]
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
          { "node": "Preparar Datos", "type": "main", "index": 0 }
        ]
      ]
    },
    "Preparar Datos": {
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
Webhook (POST) → Extraer Campos → Clasificar con OpenAI → Preparar Datos → Switch
                                                                            ├── soporte → Slack #support
                                                                            ├── ventas  → Slack #sales
                                                                            └── otro    → Slack #general
```

## Cómo usarlo

1. **Importar:** en n8n, ve a *Workflows → Import from File / Paste JSON* y pega el JSON.
2. **Credenciales de OpenAI:** abre el nodo *Clasificar con OpenAI* y selecciona o crea tu credencial con tu API Key.
3. **Credenciales de Slack:** en cada nodo de Slack, selecciona tu credencial (Bot Token u OAuth2). El bot necesita el permiso `chat:write` y debe estar invitado a los canales `#support`, `#sales` y `#general`.
4. **Activar:** guarda y activa el workflow.

## Prueba con curl

```bash
curl -X POST https://TU-INSTANCIA-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@ejemplo.com",
    "message": "Hola, quisiera saber el precio del plan empresarial para 50 usuarios"
  }'
```

Este mensaje debería llegar a **#sales**.

Para probar sin activar el workflow, usa la URL de test: `/webhook-test/clasificar-mensaje`, después de pulsar "Test workflow".

## Detalles del diseño

- **Temperatura 0 y `maxTokens: 10`:** la clasificación es determinista y la respuesta se limita a una sola palabra.
- **Normalización:** el nodo *Preparar Datos* pasa la respuesta a minúsculas y elimina espacios y signos. Así, respuestas como `"Soporte."` se enrutan correctamente.
- **Fallback:** si la IA devuelve algo inesperado, el mensaje va a **#general** en lugar de perderse.
- **Modelo:** usa `gpt-4o-mini`, que es rápido y barato para esta tarea. Puedes cambiarlo en el nodo de OpenAI.