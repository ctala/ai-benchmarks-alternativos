# GPT-5.6 Luna — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.06 | quality: 8.0
- latency_total: 14.386s | tokens_per_second: 207.0
- input_tokens: 118 | output_tokens: 2978
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

## Respuesta completa

```json
{
  "name": "Clasificación de mensajes y enrutamiento a Slack",
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
        260,
        300
      ],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "content": "=Clasifica el siguiente mensaje únicamente con una de estas categorías: soporte, ventas u otro.\n\nReglas:\n- soporte: problemas técnicos, errores, incidencias, ayuda o consultas sobre el funcionamiento del producto.\n- ventas: precios, compras, contratación, demos, planes o interés comercial.\n- otro: cualquier mensaje que no encaje en soporte o ventas.\n\nResponde únicamente con una palabra, en minúsculas: soporte, ventas u otro.\n\nMensaje:\n{{$json.body.message}}",
              "role": "user"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "2",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        520,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const webhookData = $('Webhook POST').first().json;\nconst body = webhookData.body || webhookData;\n\nconst rawClassification =\n  $json.content ??\n  $json.text ??\n  $json.message?.content ??\n  $json.choices?.[0]?.message?.content ??\n  $json.data?.[0]?.content ??\n  '';\n\nconst normalized = String(rawClassification).toLowerCase().trim();\n\nlet classification = 'otro';\nif (normalized.includes('soporte')) {\n  classification = 'soporte';\n} else if (normalized.includes('ventas')) {\n  classification = 'ventas';\n}\n\nreturn [\n  {\n    json: {\n      email: body.email || '',\n      message: body.message || '',\n      classification\n    }\n  }\n];"
      },
      "id": "3",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        780,
        300
      ]
    },
    {
      "parameters": {
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
              "leftValue": "={{$json.classification}}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "4",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1040,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#support",
        "text": "=📩 Nuevo mensaje clasificado como *soporte*\n\n*Email:* {{$json.email}}\n*Mensaje:*\n{{$json.message}}",
        "otherOptions": {}
      },
      "id": "5",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1300,
        180
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
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
              "leftValue": "={{$json.classification}}",
              "rightValue": "ventas",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "6",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1300,
        420
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#sales",
        "text": "=📩 Nuevo mensaje clasificado como *ventas*\n\n*Email:* {{$json.email}}\n*Mensaje:*\n{{$json.message}}",
        "otherOptions": {}
      },
      "id": "7",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1560,
        340
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#general",
        "text": "=📩 Nuevo mensaje clasificado como *otro*\n\n*Email:* {{$json.email}}\n*Mensaje:*\n{{$json.message}}",
        "otherOptions": {}
      },
      "id": "8",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1560,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
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
            "node": "¿Es soporte?",
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
        [
          {
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          }
        ]
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "workflow-version-1",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```