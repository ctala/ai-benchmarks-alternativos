# GPT-5.5 — code_generation/n8n_workflow_json

- model_id: `gpt-5.5`
- success: True  | final: 6.1 | quality: 7.72
- latency_total: 53.955s | tokens_per_second: 92.2
- input_tokens: 118 | output_tokens: 4977
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "name": "Clasificar email y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {
          "responseCode": 200
        }
      },
      "id": "1f0f1b9e-1111-4a11-9f11-111111111111",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        0
      ],
      "webhookId": "clasificar-email-webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "2f0f1b9e-2222-4a22-9f22-222222222222",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        260,
        0
      ]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Debes responder únicamente con una de estas tres palabras exactas: soporte, ventas u otro. No agregues explicación."
            },
            {
              "role": "user",
              "content": "=Clasifica el siguiente mensaje:\n\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "3f0f1b9e-3333-4a33-9f33-333333333333",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        560,
        0
      ],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const raw = $json.output || $json.text || $json.content || $json.message?.content || $json.choices?.[0]?.message?.content || $json.data?.choices?.[0]?.message?.content || '';\nconst normalized = String(raw).toLowerCase().trim();\nconst match = normalized.match(/\\b(soporte|ventas|otro)\\b/);\nconst classification = match ? match[1] : 'otro';\n\nreturn [\n  {\n    json: {\n      email: $node['Extraer campos'].json.email,\n      message: $node['Extraer campos'].json.message,\n      classification,\n      ai_raw: raw\n    }\n  }\n];"
      },
      "id": "4f0f1b9e-4444-4a44-9f44-444444444444",
      "name": "Normalizar clasificacion",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        840,
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "soporte-condition",
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
                    "id": "ventas-condition",
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
                    "id": "otro-condition",
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
      "id": "5f0f1b9e-5555-4a55-9f55-555555555555",
      "name": "Segun clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        1120,
        0
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=Nuevo mensaje clasificado como *soporte*:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "6f0f1b9e-6666-4a66-9f66-666666666666",
      "name": "Slack soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1420,
        -220
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "REEMPLAZAR_CREDENCIAL_SLACK",
          "name": "Slack OAuth2 account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=Nuevo mensaje clasificado como *ventas*:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "7f0f1b9e-7777-4a77-9f77-777777777777",
      "name": "Slack ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1420,
        0
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "REEMPLAZAR_CREDENCIAL_SLACK",
          "name": "Slack OAuth2 account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=Nuevo mensaje clasificado como *otro*:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "8f0f1b9e-8888-4a88-9f88-888888888888",
      "name": "Slack otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1420,
        220
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "REEMPLAZAR_CREDENCIAL_SLACK",
          "name": "Slack OAuth2 account"
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
            "node": "Normalizar clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificacion": {
      "main": [
        [
          {
            "node": "Segun clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Segun clasificacion": {
      "main": [
        [
          {
            "node": "Slack soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack otro",
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
  "staticData": null,
  "tags": [],
  "triggerCount": 1,
  "updatedAt": "2026-04-25T00:00:00.000Z",
  "versionId": "workflow-clasificar-email-slack"
}
```