# GPT-5.6 Terra Pro — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.52 | quality: 7.72
- latency_total: 65.037s | tokens_per_second: 234.9
- input_tokens: 15712 | output_tokens: 15280
- judge_score: 3.8 | justificación: 

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
      "id": "1",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        -900,
        300
      ],
      "webhookId": "a1f5c05d-6e28-4baf-ae68-2f3c4e4e0010"
    },
    {
      "parameters": {
        "mode": "manual",
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "includeOtherFields": false,
        "options": {}
      },
      "id": "2",
      "name": "Extraer email y mensaje",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -680,
        300
      ]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Email del remitente: {{ $json.email }}\n\nMensaje:\n{{ $json.message }}",
        "options": {
          "systemMessage": "Clasifica el mensaje recibido en una sola categoría: soporte, ventas u otro.\n\nReglas:\n- \"soporte\": problemas técnicos, incidencias, errores, ayuda con un producto o cuenta.\n- \"ventas\": interés en comprar, precios, presupuesto, demo, contratación o planes.\n- \"otro\": cualquier mensaje que no encaje claramente en soporte o ventas.\n\nResponde únicamente con una de estas palabras, sin puntuación ni explicaciones: soporte, ventas u otro."
        }
      },
      "id": "3",
      "name": "Clasificar mensaje con IA",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.7,
      "position": [
        -400,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        }
      },
      "id": "4",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [
        -400,
        520
      ],
      "credentials": {
        "openAiApi": {
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "return $input.all().map((item) => {\n  const raw = String(item.json.output ?? item.json.response ?? '').toLowerCase();\n  const match = raw.match(/\\b(soporte|ventas|otro)\\b/);\n\n  return {\n    json: {\n      ...item.json,\n      classification: match ? match[1] : 'otro'\n    }\n  };\n});"
      },
      "id": "5",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        -130,
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
              "leftValue": "={{ $json.classification }}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        },
        "options": {}
      },
      "id": "6",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        100,
        120
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
              "leftValue": "={{ $json.classification }}",
              "rightValue": "ventas",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        },
        "options": {}
      },
      "id": "7",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        100,
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
              "leftValue": "={{ $json.classification }}",
              "rightValue": "otro",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ]
        },
        "options": {}
      },
      "id": "8",
      "name": "¿Es otro?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        100,
        480
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#support",
        "text": "=Nuevo mensaje clasificado como *soporte*\\n\\n*Email:* {{ $json.email }}\\n*Mensaje:* {{ $json.message }}"
      },
      "id": "9",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        390,
        120
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#sales",
        "text": "=Nuevo mensaje clasificado como *ventas*\\n\\n*Email:* {{ $json.email }}\\n*Mensaje:* {{ $json.message }}"
      },
      "id": "10",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        390,
        300
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#general",
        "text": "=Nuevo mensaje clasificado como *otro*\\n\\n*Email:* {{ $json.email }}\\n*Mensaje:* {{ $json.message }}"
      },
      "id": "11",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        390,
        480
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      }
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
            "node": "Clasificar mensaje con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Clasificar mensaje con IA",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar mensaje con IA": {
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
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es otro?",
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
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "¿Es ventas?": {
      "main": [
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "¿Es otro?": {
      "main": [
        [
          {
            "node": "Enviar a #general",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1"
}
```

Tras importarlo, asigna tus credenciales de OpenAI y Slack. Si tu integración de Slack requiere IDs de canal en lugar de nombres, sustituye `#support`, `#sales` y `#general` por los IDs correspondientes.