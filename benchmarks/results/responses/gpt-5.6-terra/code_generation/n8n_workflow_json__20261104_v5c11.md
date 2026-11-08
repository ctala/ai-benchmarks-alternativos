# GPT-5.6 Terra — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 5.7 | quality: 6.32
- latency_total: 29.126s | tokens_per_second: 132.8
- input_tokens: 118 | output_tokens: 3868
- judge_score: 2.8 | justificación: 

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
  "name": "Clasificar emails y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2.1,
      "position": [
        0,
        300
      ],
      "webhookId": "clasificar-email-webhook"
    },
    {
      "parameters": {
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
        "options": {}
      },
      "id": "2",
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
        "text": "=Clasifica el siguiente mensaje de correo en exactamente una de estas categorías: soporte, ventas u otro.\\n\\nReglas:\\n- \"soporte\": problemas técnicos, incidencias, ayuda con productos o servicios existentes.\\n- \"ventas\": interés comercial, precios, demos, presupuestos o compra.\\n- \"otro\": cualquier caso que no sea soporte ni ventas.\\n\\nResponde únicamente con una palabra en minúsculas: soporte, ventas u otro.\\n\\nEmail: {{ $json.email }}\\nMensaje: {{ $json.message }}",
        "hasOutputParser": false,
        "options": {}
      },
      "id": "3",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.7,
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
      "id": "4",
      "name": "Modelo OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [
        430,
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
        "jsCode": "const original = $('Extraer campos').item.json;\\n\\n// El nodo de cadena puede devolver el resultado bajo diferentes propiedades\\nconst aiResponse = String(\\n  $json.text ?? $json.response ?? $json.output ?? $json.content ?? ''\\n).toLowerCase().trim();\\n\\nlet classification = 'otro';\\n\\nif (aiResponse.includes('soporte')) {\\n  classification = 'soporte';\\n} else if (aiResponse.includes('ventas')) {\\n  classification = 'ventas';\\n}\\n\\nreturn [\\n  {\\n    json: {\\n      email: original.email,\\n      message: original.message,\\n      classification\\n    }\\n  }\\n];"
      },
      "id": "5",
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
                  "typeValidation": "strict"
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
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
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
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
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
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "6",
      "name": "Enrutar por clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        920,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=📩 *Nuevo email de soporte*\\n\\n*Email:* {{ $json.email }}\\n*Mensaje:*\\n{{ $json.message }}"
      },
      "id": "7",
      "name": "Slack - Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1180,
        160
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
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💼 *Nuevo email de ventas*\\n\\n*Email:* {{ $json.email }}\\n*Mensaje:*\\n{{ $json.message }}"
      },
      "id": "8",
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1180,
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
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📬 *Nuevo email clasificado como otro*\\n\\n*Email:* {{ $json.email }}\\n*Mensaje:*\\n{{ $json.message }}"
      },
      "id": "9",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1180,
        440
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      }
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
    "Modelo OpenAI": {
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
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Sales",
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
  "pinData": {},
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```