# MiniMax M3.1 Flash — code_generation/n8n_workflow_json

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 7.4 | quality: 8.2
- latency_total: 77.428s | tokens_per_second: 278.9
- input_tokens: 318 | output_tokens: 21596
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un JSON bien estructurado. Aunque carece de profundidad en términos de explicaciones adicionales o optimizaciones, es clara y prácticamente útil para un emprendedor.

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

El workflow sigue este flujo: **Webhook POST → extracción de campos → OpenAI → normalización de clasificación → Switch → Slack**.

```json
{
  "name": "Clasificar mensajes y enviarlos a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "11111111-1111-4111-8111-111111111111",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        -1000,
        0
      ],
      "webhookId": "99999999-9999-4999-8999-999999999999"
    },
    {
      "parameters": {
        "jsCode": "const body = $input.first().json.body ?? {};\nconst email = typeof body.email === 'string' ? body.email.trim() : '';\nconst message = typeof body.message === 'string' ? body.message.trim() : '';\n\nif (!email) throw new Error('El campo \"email\" es obligatorio');\nif (!message) throw new Error('El campo \"message\" es obligatorio');\n\nreturn [{ json: { email, message } }];"
      },
      "id": "22222222-2222-4222-8222-222222222222",
      "name": "Extraer email y mensaje",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        -780,
        0
      ]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "cachedResultName": "gpt-4o-mini"
        },
        "promptType": "define",
        "text": "={{ 'Email: ' + $json.email + '\\nMensaje: ' + $json.message }}",
        "options": {
          "systemMessage": "Eres un clasificador de mensajes. Clasifica el mensaje únicamente como soporte, ventas u otro. Soporte corresponde a dudas, problemas técnicos o assistance. Ventas corresponde a precios, compras, contrataciones o interés comercial. Otro corresponde a cualquier categoría no relacionada. Devuelve exclusivamente una de estas tres palabras en minúsculas, sin explicaciones ni comillas."
        }
      },
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI API"
        }
      },
      "id": "33333333-3333-4333-8333-333333333333",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        -540,
        0
      ]
    },
    {
      "parameters": {
        "jsCode": "const ai = $input.first().json;\nconst candidate = ai.text ?? ai.output ?? ai.response ?? ai.content ?? ai.message ?? '';\nconst raw = typeof candidate === 'string' ? candidate : JSON.stringify(candidate);\nconst allowed = ['soporte', 'ventas', 'otro'];\nlet detected = '';\n\ntry {\n  const parsed = JSON.parse(raw);\n  const value = typeof parsed === 'string' ? parsed : (parsed.category ?? parsed.categoria ?? parsed.classification);\n  if (typeof value === 'string') detected = value.toLowerCase().trim();\n} catch {}\n\nif (!allowed.includes(detected)) {\n  const match = raw.toLowerCase().match(/\\b(soporte|ventas|otro)\\b/);\n  detected = match ? match[1] : 'otro';\n}\n\nconst category = allowed.includes(detected) ? detected : 'otro';\nconst original = $('Extraer email y mensaje').first().json;\n\nreturn [{ json: { ...original, category, aiResponse: raw } }];"
      },
      "id": "44444444-4444-4444-8444-444444444444",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        -300,
        0
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
                    "id": "a1111111-1111-4111-8111-111111111111",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "b2222222-2222-4222-8222-222222222222",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c3333333-3333-4333-8333-333333333333",
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
      "id": "55555555-5555-4555-8555-555555555555",
      "name": "Enrutar por clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        -40,
        0
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "support",
          "cachedResultName": "#support"
        },
        "text": "={{ '*Email:* ' + $json.email + '\\n*Mensaje:* ' + $json.message + '\\n*Clasificación:* soporte' }}",
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      },
      "id": "66666666-6666-4666-8666-666666666666",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        220,
        -160
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "sales",
          "cachedResultName": "#sales"
        },
        "text": "={{ '*Email:* ' + $json.email + '\\n*Mensaje:* ' + $json.message + '\\n*Clasificación:* ventas' }}",
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      },
      "id": "77777777-7777-4777-8777-777777777777",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        220,
        0
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "general",
          "cachedResultName": "#general"
        },
        "text": "={{ '*Email:* ' + $json.email + '\\n*Mensaje:* ' + $json.message + '\\n*Clasificación:* otro' }}",
        "otherOptions": {}
      },
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      },
      "id": "88888888-8888-4888-8888-888888888888",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        220,
        160
      ]
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extraer email y mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y mensaje": {
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
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "tags": []
}
```

Después de importarlo:

- Sustituye o selecciona las credenciales de **OpenAI** y **Slack**.
- Si Slack requiere IDs internos, reemplaza `support`, `sales` y `general` por los valores `C...` correspondientes.
- El webhook de producción quedará en:

```text
POST https://TU-N8N/webhook/clasificar-mensaje
```

Con un body como:

```json
{
  "email": "cliente@example.com",
  "message": "Necesito ayuda para configurar mi cuenta"
}
```