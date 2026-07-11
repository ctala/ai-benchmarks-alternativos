# GPT-5.6 Sol — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 4.53 | quality: 5.2
- latency_total: 56.522s | tokens_per_second: 91.5
- input_tokens: 118 | output_tokens: 5171
- judge_score: 2.0 | justificación: La respuesta es parcialmente correcta pero carece de completitud y contiene errores significativos, como la falta de un nodo para enviar mensajes a Slack y la inclusión de un nodo OpenAI innecesario.

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
      "id": "dca92407-00af-43c5-935e-bf0617cac0cb",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        300
      ],
      "webhookId": "7fbc9db9-f2ca-414b-8662-1d555489a125"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "48807286-168c-4cd1-9744-f061590a6646",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "35b781d9-2881-48ee-abef-4b99e62b287b",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "d2b1ce61-eb9e-46ae-b81f-84fb65f03218",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        220,
        300
      ]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "={{ 'Clasifica el siguiente mensaje en una sola categoría: soporte, ventas u otro.\\n\\nMensaje:\\n' + $json.message }}",
        "messages": {
          "messageValues": [
            {
              "message": "Eres un clasificador de mensajes. Responde exclusivamente con una de estas palabras en minúsculas: soporte, ventas, otro. Usa soporte para problemas técnicos, incidencias, errores, ayuda o reclamaciones. Usa ventas para precios, presupuestos, demostraciones, compras o información comercial. Usa otro para cualquier mensaje que no corresponda a las categorías anteriores."
            }
          ]
        }
      },
      "id": "739c5120-e3b7-4cbb-9098-e0168aa9c928",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.4,
      "position": [
        460,
        300
      ]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "04cd740a-36a7-49bd-b80a-e9fb41117209",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [
        460,
        520
      ]
    },
    {
      "parameters": {
        "jsCode": "const raw = String($json.text ?? $json.output ?? $json.response ?? '')\n  .toLowerCase()\n  .trim();\n\nconst match = raw.match(/\\b(soporte|ventas|otro)\\b/);\nconst classification = match ? match[1] : 'otro';\n\nconst input = $('Extraer campos').item.json;\n\nreturn [\n  {\n    json: {\n      email: input.email,\n      message: input.message,\n      classification,\n      aiRawResponse: raw\n    }\n  }\n];"
      },
      "id": "565309ac-a547-4eef-83c6-ad61a23973c1",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        700,
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
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "aa672f54-75e4-4519-974f-d039a36652c2",
      "name": "Enrutar clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        940,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "SUPPORT_CHANNEL_ID",
          "mode": "id"
        },
        "text": "={{ '📩 Nuevo mensaje de *soporte*\\n\\n*Email:* ' + $json.email + '\\n*Mensaje:*\\n' + $json.message }}",
        "otherOptions": {}
      },
      "id": "00bf07e2-6c3f-435e-a7fd-19e5dcb43d5e",
      "name": "Slack - support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1220,
        140
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "SALES_CHANNEL_ID",
          "mode": "id"
        },
        "text": "={{ '💰 Nuevo mensaje de *ventas*\\n\\n*Email:* ' + $json.email + '\\n*Mensaje:*\\n' + $json.message }}",
        "otherOptions": {}
      },
      "id": "26f8ea20-a230-49ee-a039-fcf5e10d2841",
      "name": "Slack - sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1220,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "GENERAL_CHANNEL_ID",
          "mode": "id"
        },
        "text": "={{ '📨 Nuevo mensaje clasificado como *otro*\\n\\n*Email:* ' + $json.email + '\\n*Mensaje:*\\n' + $json.message }}",
        "otherOptions": {}
      },
      "id": "0ae0999b-3ea4-4aa7-8a09-dbf0af8d06f5",
      "name": "Slack - general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1220,
        460
      ]
    }
  ],
  "connections": {
    "Webhook POST": {
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
            "node": "Clasificar con IA",
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
            "node": "Clasificar con IA",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
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
            "node": "Enrutar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar clasificación": {
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
  "pinData": {},
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "32ef8385-abfb-40d0-a340-2d01420922af",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```

Después de importarlo, selecciona las credenciales de OpenAI y Slack. Sustituye `SUPPORT_CHANNEL_ID`, `SALES_CHANNEL_ID` y `GENERAL_CHANNEL_ID` por los IDs reales de `#support`, `#sales` y `#general`, respectivamente.