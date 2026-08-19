# GPT-5.6 Terra — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.88 | quality: 8.0
- latency_total: 20.2s | tokens_per_second: 147.1
- input_tokens: 118 | output_tokens: 2972
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

## Respuesta completa

```json
{
  "name": "Clasificación de emails con OpenAI y envío a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        240,
        300
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
      "id": "2",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        460,
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
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de email. Clasifica cada mensaje exclusivamente en una de estas categorías: \"soporte\", \"ventas\" u \"otro\". Responde únicamente con un objeto JSON válido, sin Markdown ni texto adicional, usando exactamente este formato: {\"category\":\"soporte\"}. Usa \"soporte\" para incidencias, problemas técnicos, ayuda o consultas sobre productos existentes. Usa \"ventas\" para presupuestos, precios, demostraciones, contratación o intención de compra. Usa \"otro\" para cualquier otro caso."
            },
            {
              "role": "user",
              "content": "Clasifica este mensaje:\n\n{{ $json.message }}"
            }
          ]
        },
        "simplify": true,
        "options": {
          "responseFormat": "json_object"
        }
      },
      "id": "3",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        700,
        300
      ],
      "credentials": {
        "openAiApi": {
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const original = $('Extraer campos').item.json;\n\nconst rawResponse = $json.content ?? $json.text ?? $json.message?.content ?? $json.output ?? JSON.stringify($json);\n\nlet category = 'otro';\n\ntry {\n  const parsed = typeof rawResponse === 'string' ? JSON.parse(rawResponse) : rawResponse;\n  category = String(parsed.category ?? parsed.clasificacion ?? 'otro').toLowerCase().trim();\n} catch (error) {\n  const text = String(rawResponse).toLowerCase();\n  if (text.includes('soporte')) {\n    category = 'soporte';\n  } else if (text.includes('ventas')) {\n    category = 'ventas';\n  }\n}\n\nif (!['soporte', 'ventas', 'otro'].includes(category)) {\n  category = 'otro';\n}\n\nreturn [\n  {\n    json: {\n      email: original.email,\n      message: original.message,\n      category\n    }\n  }\n];"
      },
      "id": "4",
      "name": "Procesar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        940,
        300
      ]
    },
    {
      "parameters": {
        "value1": "={{ $json.category }}",
        "rules": [
          {
            "operation": "equal",
            "value2": "soporte"
          },
          {
            "operation": "equal",
            "value2": "ventas"
          },
          {
            "operation": "equal",
            "value2": "otro"
          }
        ],
        "options": {}
      },
      "id": "5",
      "name": "Enrutar por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1160,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=📩 *Nuevo email de soporte*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría:* {{ $json.category }}"
      },
      "id": "6",
      "name": "Enviar a Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1400,
        160
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=💼 *Nuevo email de ventas*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría:* {{ $json.category }}"
      },
      "id": "7",
      "name": "Enviar a Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1400,
        300
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=📬 *Nuevo email general*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría:* {{ $json.category }}"
      },
      "id": "8",
      "name": "Enviar a Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1400,
        440
      ],
      "credentials": {
        "slackApi": {
          "name": "Slack API"
        }
      }
    }
  ],
  "pinData": {},
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
            "node": "Procesar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Procesar clasificación": {
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
            "node": "Enviar a Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a Slack General",
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
  "versionId": "1",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```