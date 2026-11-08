# Muse Spark 1.3 — code_generation/n8n_workflow_json

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 7.15 | quality: 8.2
- latency_total: 33.162s | tokens_per_second: 167.6
- input_tokens: 122 | output_tokens: 5557
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los pasos necesarios para el flujo de trabajo de N8N. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores.

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

Aquí tienes un workflow completo y listo para importar en n8N (`Import from JSON`):

**Qué hace:**
`Webhook POST` > `Set (extrae email/message)` > `OpenAI (clasifica)` > `Code (normaliza)` > `Switch (soporte/ventas/otro)` > `3x Slack (#support, #sales, #general)` > `Respond`

> Solo tienes que crear y conectar las credenciales: **OpenAI** y **Slack**.

```json
{
  "name": "Webhook Clasificador IA -> Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "11111111-1111-4111-8111-111111111111",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "a1b2c3d4-e5f6-4a7b-8c9d-123456789000"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "assign-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "22222222-2222-4222-8222-222222222222",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 0]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de clientes. Clasifica el mensaje en UNA sola palabra: soporte, ventas u otro.\n- soporte: problemas técnicos, errores, ayuda, cuenta, contraseña\n- ventas: precios, planes, comprar, demo, contratación\n- otro: todo lo demás\nResponde ÚNICAMENTE con: soporte, ventas u otro. Sin puntos, sin explicaciones."
            },
            {
              "role": "user",
              "content": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}\n\nResponde ÚNICAMENTE con una palabra: soporte, ventas u otro."
            }
          ]
        },
        "options": {
          "maxTokens": 10,
          "temperature": 0
        }
      },
      "id": "33333333-3333-4333-8333-333333333333",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [440, 0],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "const data = $input.first().json;\nconst raw = data?.choices?.[0]?.message?.content || data?.text || data?.output || 'otro';\nconst categoriaRaw = raw.toString().toLowerCase().trim();\nconst categoria = ['soporte','ventas'].includes(categoriaRaw) ? categoriaRaw : 'otro';\nconst prev = $('Extraer email y message').first().json;\nreturn [{ json: { email: prev.email, message: prev.message, categoria, raw: raw.toString().trim() } }];"
      },
      "id": "44444444-4444-4444-8444-444444444444",
      "name": "Normalizar Clasificacion",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [660, 0]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.categoria }}",
        "rules": {
          "values": [
            {
              "id": "rule-soporte",
              "operation": "equals",
              "value2": "soporte",
              "outputKey": "soporte",
              "renameOutput": true
            },
            {
              "id": "rule-ventas",
              "operation": "equals",
              "value2": "ventas",
              "outputKey": "ventas",
              "renameOutput": true
            }
          ]
        },
        "fallbackOutput": "extra",
        "options": {
          "renameFallback": true,
          "fallbackOutputKey": "otro"
        }
      },
      "id": "55555555-5555-4555-8555-555555555555",
      "name": "Switch por Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#support",
        "text": "=📩 *Nuevo mensaje de SOPORTE* de {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "66666666-6666-4666-8666-666666666666",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1100, -200],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje de VENTAS* de {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "77777777-7777-4777-8777-777777777777",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1100, 0],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#general",
        "text": "=📝 *Nuevo mensaje (otro)* de {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "88888888-8888-4888-8888-888888888888",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1100, 200],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"success\": true,\n  \"email\": \"{{ $json.email }}\",\n  \"categoria\": \"{{ $json.categoria }}\",\n  \"canal\": \"{{ $json.categoria === 'soporte' ? '#support' : $json.categoria === 'ventas' ? '#sales' : '#general' }}\"\n}",
        "options": {}
      },
      "id": "99999999-9999-4999-8999-999999999999",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1320, 0]
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
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
            "node": "Normalizar Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Clasificacion": {
      "main": [
        [
          {
            "node": "Switch por Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por Categoria": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack Soporte": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack Ventas": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack General": {
      "main": [
        [
          {
            "node": "Responder Webhook",
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

**Para probarlo:**
```bash
curl -X POST https://tu-n8n.app/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@test.com","message":"Quiero saber el precio del plan pro"}'
```
Esto lo clasificará como `ventas` y lo enviará a `#sales`.
