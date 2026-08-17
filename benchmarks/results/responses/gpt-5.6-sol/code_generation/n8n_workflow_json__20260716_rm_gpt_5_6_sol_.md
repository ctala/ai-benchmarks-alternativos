# GPT-5.6 Sol — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 5.52 | quality: 6.6
- latency_total: 76.651s | tokens_per_second: 64.8
- input_tokens: 118 | output_tokens: 4967
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de profundidad en la explicación y no completa el JSON, lo que limita su utilidad práctica.

## Respuesta completa

```json
{
  "name": "Clasificar mensajes y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "4b4fd687-df88-42bd-a59b-054590dd5b18",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2.1,
      "position": [
        -800,
        300
      ],
      "webhookId": "1c29d834-75bc-473d-b579-7d8c03baac91"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "3b2e25fc-c883-4d33-956f-9ff81a1b3ce8",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "47ed6a71-51de-45aa-8c61-2722d655c1a2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "includeOtherFields": false,
        "options": {}
      },
      "id": "b9e14617-21d6-4a26-b540-285f8593e487",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -580,
        300
      ]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "GPT-4O-MINI"
        },
        "messages": {
          "values": [
            {
              "content": "=Clasifica el siguiente mensaje en exactamente una de estas categorías: soporte, ventas u otro.\n\nReglas:\n- soporte: problemas técnicos, errores, incidencias, ayuda con un producto o servicio.\n- ventas: consultas de precios, planes, compras, demostraciones o contratación.\n- otro: cualquier mensaje que no corresponda a soporte ni ventas.\n\nResponde únicamente con una palabra: soporte, ventas u otro.\n\nMensaje:\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "e53c4675-4742-4bcd-bbf2-3d7ccf65a47a",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        -340,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const original = $items('Extraer campos')[0].json;\n\nconst raw =\n  $json.message?.content ??\n  $json.choices?.[0]?.message?.content ??\n  $json.content ??\n  $json.text ??\n  '';\n\nconst match = String(raw)\n  .trim()\n  .toLowerCase()\n  .match(/\\b(soporte|ventas|otro)\\b/);\n\nconst classification = match ? match[1] : 'otro';\n\nreturn [\n  {\n    json: {\n      email: original.email,\n      message: original.message,\n      classification\n    }\n  }\n];"
      },
      "id": "a2100b64-c895-4c6e-b1da-70fda9f9812c",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        -100,
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
                  "caseSensitive": false,
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
                  "caseSensitive": false,
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
                  "caseSensitive": false,
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
      "id": "c03e047f-9ffc-4589-bfca-d44d944534dd",
      "name": "Enrutar clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        140,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "={{ '*Nuevo mensaje de soporte*\\n*Email:* ' + $json.email + '\\n*Mensaje:* ' + $json.message + '\\n*Clasificación:* ' + $json.classification }}",
        "attachments": [],
        "otherOptions": {}
      },
      "id": "f6fb4ef2-c6bd-482e-849b-b398f112b0b9",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        440,
        140
      ],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "={{ '*Nuevo mensaje de ventas*\\n*Email:* ' + $json.email + '\\n*Mensaje:* ' + $json.message + '\\n*Clasificación:* ' + $json.classification }}",
        "attachments": [],
        "otherOptions": {}
      },
      "id": "17cb69c8-349a-4088-a6dd-9a0ef441d52e",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        440,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "={{ '*Nuevo mensaje general*\\n*Email:* ' + $json.email + '\\n*Mensaje:* ' + $json.message + '\\n*Clasificación:* ' + $json.classification }}",
        "attachments": [],
        "otherOptions": {}
      },
      "id": "10d0491b-94c0-47cb-98db-9d27673c098e",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        440,
        460
      ],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_SLACK_CREDENTIAL_ID",
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
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
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
  "pinData": {},
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "3104fe02-032d-4288-a63d-026fe9075877",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```