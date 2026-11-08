# GPT-6 Luna — code_generation/n8n_workflow_json

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.41 | quality: 8.0
- latency_total: 50.732s | tokens_per_second: 120.7
- input_tokens: 118 | output_tokens: 6123
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un uso adecuado de los nodos de N8N. La profundidad es aceptable, proporcionando un enfoque estructurado pero sin insights adicionales. La claridad es buena, con una estructura organizada y fácil de entender, y es prácticamente útil para un emprendedor.

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
  "name": "Clasificar consultas y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-consulta",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1f2c3d4-1111-4444-8888-123456789001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        240,
        300
      ],
      "webhookId": "clasificar-consulta"
    },
    {
      "parameters": {
        "jsCode": "const input = $input.first().json;\nconst body = input.body ?? input;\nreturn [{ json: { email: String(body.email ?? ''), message: String(body.message ?? '') } }];"
      },
      "id": "a1f2c3d4-2222-4444-8888-123456789002",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        460,
        300
      ]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/chat/completions",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer REEMPLAZA_CON_TU_OPENAI_API_KEY"
            },
            {
              "name": "Content-Type",
              "value": "application/json"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={{ { model: 'gpt-4o-mini', response_format: { type: 'json_object' }, messages: [ { role: 'system', content: 'Clasifica el mensaje en exactamente una categoría: soporte, ventas u otro. Responde únicamente con un objeto JSON con la clave \"classification\" y una de esas tres categorías como valor.' }, { role: 'user', content: 'Email: ' + $json.email + '\\nMensaje: ' + $json.message } ] } }}",
        "options": {}
      },
      "id": "a1f2c3d4-3333-4444-8888-123456789003",
      "name": "OpenAI - clasificar",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        700,
        300
      ]
    },
    {
      "parameters": {
        "jsCode": "const result = $input.first().json;\nconst source = $('Extraer email y message').first().json;\nconst content = result.choices?.[0]?.message?.content ?? result.body?.choices?.[0]?.message?.content ?? '';\nlet parsed;\ntry {\n  parsed = typeof content === 'string' ? JSON.parse(content) : content;\n} catch {\n  parsed = { classification: String(content).toLowerCase().trim() };\n}\nlet classification = String(parsed?.classification ?? '').toLowerCase().trim();\nif (!['soporte', 'ventas', 'otro'].includes(classification)) classification = 'otro';\nreturn [{ json: { email: source.email, message: source.message, classification } }];"
      },
      "id": "a1f2c3d4-4444-4444-8888-123456789004",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        940,
        300
      ]
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
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
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
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
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
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
      "id": "a1f2c3d4-5555-4444-8888-123456789005",
      "name": "Enrutar por clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        1180,
        300
      ]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://slack.com/api/chat.postMessage",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer REEMPLAZA_CON_TU_SLACK_BOT_TOKEN"
            },
            {
              "name": "Content-Type",
              "value": "application/json; charset=utf-8"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={{ { channel: '#support', text: 'Clasificación: soporte\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message } }}",
        "options": {}
      },
      "id": "a1f2c3d4-6666-4444-8888-123456789006",
      "name": "Slack - support",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        1450,
        160
      ]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://slack.com/api/chat.postMessage",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer REEMPLAZA_CON_TU_SLACK_BOT_TOKEN"
            },
            {
              "name": "Content-Type",
              "value": "application/json; charset=utf-8"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={{ { channel: '#sales', text: 'Clasificación: ventas\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message } }}",
        "options": {}
      },
      "id": "a1f2c3d4-7777-4444-8888-123456789007",
      "name": "Slack - sales",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        1450,
        300
      ]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://slack.com/api/chat.postMessage",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Authorization",
              "value": "Bearer REEMPLAZA_CON_TU_SLACK_BOT_TOKEN"
            },
            {
              "name": "Content-Type",
              "value": "application/json; charset=utf-8"
            }
          ]
        },
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={{ { channel: '#general', text: 'Clasificación: otro\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message } }}",
        "options": {}
      },
      "id": "a1f2c3d4-8888-4444-8888-123456789008",
      "name": "Slack - general",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.2,
      "position": [
        1450,
        440
      ]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "OpenAI - clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - clasificar": {
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
            "node": "Enrutar por clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por clasificación": {
      "main": [
        [
          {
            "node": "Slack - support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - general",
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
  "versionId": "a1f2c3d4-9999-4444-8888-123456789009"
}
```

Antes de activarlo, reemplaza las claves API indicadas. Slack puede requerir los IDs de canal (`C…`) en lugar de nombres como `#support`; si es así, cambia esos valores por los IDs correspondientes.