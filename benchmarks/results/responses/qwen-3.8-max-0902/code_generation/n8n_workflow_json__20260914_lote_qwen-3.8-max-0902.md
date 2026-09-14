# Qwen 3.8 Max 0902 — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.03 | quality: 8.6
- latency_total: 253.717s | tokens_per_second: 55.6
- input_tokens: 176 | output_tokens: 14113
- judge_score: 4.0 | justificación: La respuesta proporciona un workflow de N8N preciso y relevante que cumple con los requisitos especificados, con una estructura clara y utilidad práctica, aunque carece de profundidad adicional más allá de la implementación básica.

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

Aquí tienes el workflow completo. Cópialo y pégalo en N8N mediante **Workflows → ⋯ → Import from File** (guárdalo como `.json`) o con **Paste from URL/JSON**.

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "contact-form",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "f9e8d7c6-b5a4-4f3e-2d1c-0b9a8f7e6d5c"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 0]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de una empresa. Tu única tarea es clasificar mensajes en exactamente una de tres categorías: soporte, ventas u otro."
            },
            {
              "content": "=Clasifica el siguiente mensaje en exactamente una de estas categorías: \"soporte\", \"ventas\" u \"otro\". Responde únicamente con la categoría, sin explicaciones ni puntuación adicional.\n\nMensaje:\n\"{{ $json.message }}\""
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 0]
    },
    {
      "parameters": {
        "mode": "runOnceForAllItems",
        "jsCode": "const ai = $input.first().json;\n\n// Extraer el texto de la respuesta de OpenAI (compatible con varios formatos de salida)\nlet raw = '';\nif (ai.message && typeof ai.message.content === 'string') {\n  raw = ai.message.content;\n} else if (ai.choices && ai.choices[0] && ai.choices[0].message && ai.choices[0].message.content) {\n  raw = ai.choices[0].message.content;\n} else if (typeof ai.content === 'string') {\n  raw = ai.content;\n} else if (typeof ai.output === 'string') {\n  raw = ai.output;\n}\n\nraw = raw.toLowerCase().trim();\n\nlet category = 'otro';\nif (raw.includes('soporte')) {\n  category = 'soporte';\n} else if (raw.includes('venta')) {\n  category = 'ventas';\n}\n\nconst original = $('Extraer Datos').first().json;\n\nreturn [{\n  json: {\n    email: original.email,\n    message: original.message,\n    category: category\n  }\n}];"
      },
      "id": "f6a7b8c9-d0e1-4f2a-3b4c-5d6e7f8a9b0c",
      "name": "Normalizar Categoria",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [660, 0]
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
                    "id": "11111111-0000-4000-8000-000000000001",
                    "leftValue": "={{ $json.category }}",
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
                    "id": "11111111-0000-4000-8000-000000000002",
                    "leftValue": "={{ $json.category }}",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "11111111-0000-4000-8000-000000000003",
                    "leftValue": "={{ $json.category }}",
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
        "options": {}
      },
      "id": "07b8c9d0-e1f2-4a3b-4c5d-6e7f8a9b0c1d",
      "name": "Enrutar por Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#support"
        },
        "text": "=🎫 *Nuevo mensaje de soporte*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "18c9d0e1-f2a3-4b4c-5d6e-7f8a9b0c1d2e",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1140, -200]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#sales"
        },
        "text": "=💼 *Nuevo mensaje de ventas*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "29d0e1f2-a3b4-4c5d-6e7f-8a9b0c1d2e3f",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1140, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#general"
        },
        "text": "=📬 *Nuevo mensaje (sin clasificar)*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "3ae1f2a3-b4c5-4d6e-7f8a-9b0c1d2e3f4a",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1140, 200]
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
            "node": "Normalizar Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Categoria": {
      "main": [
        [
          {
            "node": "Enrutar por Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por Categoria": {
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
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

## Cómo funciona

1. **Webhook (POST)** → recibe el payload en `/webhook/contact-form`
2. **Extraer Datos** (Set) → normaliza `email` y `message` del body
3. **Clasificar con IA** (OpenAI) → usa `gpt-4o-mini` con `temperature: 0` para clasificar de forma determinista
4. **Normalizar Categoria** (Code) → limpia la respuesta de la IA y garantiza que la categoría sea siempre `soporte`, `ventas` u `otro` (cualquier respuesta inesperada cae en `otro`)
5. **Enrutar por Categoria** (Switch) → 3 salidas, una por categoría
6. **Slack** → 3 nodos, uno por canal

## Antes de activarlo

- **Credenciales**: configura tu credencial de **OpenAI** en el nodo "Clasificar con IA" y tu credencial de **Slack** en los 3 nodos de Slack.
- **Canales**: los canales `#support`, `#sales` y `#general` deben existir y el bot de Slack debe ser miembro de ellos.
- **Modelo**: puedes cambiar `gpt-4o-mini` por el que prefieras en el nodo de OpenAI.

## Prueba rápida

```bash
curl -X POST https://TU-INSTANCIA-N8N.com/webhook/contact-form \
  -H "Content-Type: application/json" \
  -d '{"email": "cliente@ejemplo.com", "message": "No puedo iniciar sesión en mi cuenta"}'
```

> Nota: mientras pruebas con el botón "Execute Workflow", usa la URL de test (`/webhook-test/contact-form`). La URL de producción solo funciona con el workflow activado.