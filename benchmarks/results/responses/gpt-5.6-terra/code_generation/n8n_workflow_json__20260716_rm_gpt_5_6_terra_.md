# GPT-5.6 Terra — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 5.66 | quality: 6.32
- latency_total: 26.734s | tokens_per_second: 138.1
- input_tokens: 118 | output_tokens: 3692
- judge_score: 2.8 | justificación: 

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
      "typeVersion": 2,
      "position": [
        -900,
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
        -680,
        300
      ]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "={{ $json.message }}",
        "options": {
          "systemMessage": "Clasifica el mensaje recibido en una de estas tres categorías: \"soporte\", \"ventas\" u \"otro\". Responde exclusivamente con una sola palabra en minúsculas: soporte, ventas u otro. No añadas explicaciones, puntuación ni texto adicional."
        }
      },
      "id": "3",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.7,
      "position": [
        -420,
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
        "options": {}
      },
      "id": "4",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.2,
      "position": [
        -420,
        100
      ],
      "credentials": {
        "openAiApi": {
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "categoria-field",
              "name": "categoria",
              "value": "={{ (($json.output || '').trim().toLowerCase() === 'soporte') ? 'soporte' : ((($json.output || '').trim().toLowerCase() === 'ventas') ? 'ventas' : 'otro') }}",
              "type": "string"
            }
          ]
        },
        "options": {
          "includeOtherFields": true
        }
      },
      "id": "5",
      "name": "Normalizar categoría",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -180,
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
                    "leftValue": "={{ $json.categoria }}",
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.categoria }}",
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.categoria }}",
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
      "name": "Enrutar por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        60,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=📩 *Nuevo email de SOPORTE*\n\n*Email:* {{ $('Extraer campos').item.json.email }}\n*Mensaje:* {{ $('Extraer campos').item.json.message }}"
      },
      "id": "7",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        340,
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
        "channel": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=📩 *Nuevo email de VENTAS*\n\n*Email:* {{ $('Extraer campos').item.json.email }}\n*Mensaje:* {{ $('Extraer campos').item.json.message }}"
      },
      "id": "8",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        340,
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
        "channel": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📩 *Nuevo email GENERAL*\n\n*Email:* {{ $('Extraer campos').item.json.email }}\n*Mensaje:* {{ $('Extraer campos').item.json.message }}"
      },
      "id": "9",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        340,
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
            "node": "Normalizar categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar categoría": {
      "main": [
        [
          {
            "node": "Enrutar por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por categoría": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #general",
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