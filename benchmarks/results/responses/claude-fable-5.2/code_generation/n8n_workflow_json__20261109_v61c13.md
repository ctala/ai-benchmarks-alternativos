# Claude Fable 5.2 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 6.03 | quality: 7.2
- latency_total: 40.875s | tokens_per_second: 119.7
- input_tokens: 177 | output_tokens: 4892
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

```json
{
  "name": "Clasificar mensajes y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 300],
      "webhookId": "a1b2c3d4-aaaa-4000-8000-00000000abcd"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "b1b2c3d4-0001-4000-8000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "b1b2c3d4-0002-4000-8000-000000000002",
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
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "GPT-4O-MINI"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en una de estas tres categorías: \"soporte\" (problemas técnicos, errores, ayuda con el producto), \"ventas\" (precios, compras, planes, cotizaciones) u \"otro\" (cualquier otra cosa). Responde ÚNICAMENTE con una palabra en minúsculas: soporte, ventas u otro. No añadas explicaciones ni puntuación.",
              "role": "system"
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
      "typeVersion": 1.8,
      "position": [440, 300]
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
                    "id": "c1b2c3d4-0001-4000-8000-000000000001",
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
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
                    "id": "c1b2c3d4-0002-4000-8000-000000000002",
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
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
          "ignoreCase": true
        }
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Switch clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [800, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo mensaje de SOPORTE*\n*Email:* {{ $('Extraer campos').item.json.email }}\n*Mensaje:* {{ $('Extraer campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1060, 100]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*Email:* {{ $('Extraer campos').item.json.email }}\n*Mensaje:* {{ $('Extraer campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1060, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📩 *Nuevo mensaje (OTRO)*\n*Email:* {{ $('Extraer campos').item.json.email }}\n*Mensaje:* {{ $('Extraer campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1060, 500]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer campos": {
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
            "node": "Switch clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch clasificación": {
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
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "active": false
}
```

## Antes de usarlo

No he podido ejecutarlo en una instancia de n8n, así que haz una prueba tras importarlo. Si tu versión de n8n es antigua, puede que tengas que actualizarla o recrear algún nodo.

1. **Importar:** en n8n, crea un workflow nuevo y elige "Import from File", o pega el JSON directamente en el canvas.
2. **Credenciales:** el JSON no las incluye, así que debes asignarlas a mano:
   - En "Clasificar con OpenAI", tu credencial de OpenAI (API key).
   - En los tres nodos de Slack, tu credencial de Slack (el bot necesita el scope `chat:write` y estar invitado a los tres canales).
3. **Probar:** pulsa "Test workflow" y lanza una petición a la URL de prueba:

```bash
curl -X POST https://TU-INSTANCIA-N8N/webhook-test/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email": "cliente@ejemplo.com", "message": "No puedo iniciar sesión en mi cuenta"}'
```

4. **Activar:** al activar el workflow, la URL de producción pasa a ser `/webhook/clasificar-mensaje`.

## Cómo funciona

- **Ruta por defecto:** el Switch envía a `#general` todo lo que no contenga "soporte" ni "ventas". Así, si el modelo responde algo inesperado, el mensaje no se pierde.
- **Clasificación:** el modelo es `gpt-4o-mini` con temperatura 0 para que las respuestas sean consistentes. Puedes cambiarlo en el nodo.
- **Respuesta del webhook:** responde de inmediato al recibir la petición, sin esperar a que termine la clasificación.