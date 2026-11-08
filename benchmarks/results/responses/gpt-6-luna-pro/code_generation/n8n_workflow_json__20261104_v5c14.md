# GPT-6 Luna Pro — code_generation/n8n_workflow_json

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.27 | quality: 8.0
- latency_total: 54.855s | tokens_per_second: 188.9
- input_tokens: 11114 | output_tokens: 10364
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del workflow de N8N, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos de Slack.

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

```json
{
  "name": "Clasificar mensajes y enviar a Slack",
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
      "position": [
        240,
        300
      ],
      "webhookId": "a1b2c3d4-0001-4000-8000-000000000001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1b2c3d4-0002-4000-8000-000000000002",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "a1b2c3d4-0003-4000-8000-000000000003",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        460,
        300
      ]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": "gpt-4o-mini",
        "prompt": {
          "messages": {
            "values": [
              {
                "role": "system",
                "content": "Clasifica el mensaje recibido en exactamente una categoría: soporte, ventas u otro. Responde únicamente con la categoría, sin signos ni explicaciones."
              },
              {
                "role": "user",
                "content": "={{ 'Email: ' + $json.email + '\\nMensaje: ' + $json.message }}"
              }
            ]
          }
        },
        "options": {}
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [
        700,
        300
      ]
    },
    {
      "parameters": {
        "mode": "runOnceForAllItems",
        "jsCode": "const response = $input.first().json;\nconst raw = response.choices?.[0]?.message?.content ?? response.message?.content ?? response.text ?? '';\nconst match = String(raw).toLowerCase().match(/\\b(soporte|ventas|otro)\\b/);\nconst { email, message } = $('Extraer datos').first().json;\nreturn [{ json: { email, message, classification: match?.[1] ?? 'otro' } }];"
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Preparar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        940,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "a1b2c3d4-0007-4000-8000-000000000007",
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
        "options": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1180,
        300
      ]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "support",
          "mode": "name"
        },
        "text": "={{ 'Nuevo mensaje de ' + $json.email + ':\\n' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0009-4000-8000-000000000009",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1420,
        180
      ]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict",
            "version": 2
          },
          "conditions": [
            {
              "id": "a1b2c3d4-0010-4000-8000-000000000010",
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
        "options": {}
      },
      "id": "a1b2c3d4-0011-4000-8000-000000000011",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1420,
        420
      ]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "sales",
          "mode": "name"
        },
        "text": "={{ 'Nuevo mensaje de ' + $json.email + ':\\n' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0012-4000-8000-000000000012",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1660,
        360
      ]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "general",
          "mode": "name"
        },
        "text": "={{ 'Nuevo mensaje de ' + $json.email + ':\\n' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0013-4000-8000-000000000013",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1660,
        500
      ]
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
            "node": "Preparar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar clasificación": {
      "main": [
        [
          {
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es soporte?": {
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
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es ventas?": {
      "main": [
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a1b2c3d4-0014-4000-8000-000000000014"
}
```

Tras importarlo, configura las credenciales de OpenAI y Slack. Si n8n no encuentra los canales por nombre, selecciónalos en cada nodo de Slack usando el selector de canales.