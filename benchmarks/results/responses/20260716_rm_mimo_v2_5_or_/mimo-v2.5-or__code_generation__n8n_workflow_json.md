# MiMo-V2.5 (omnimodal) — code_generation/n8n_workflow_json

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 6.36 | quality: 6.8
- latency_total: 21.656s | tokens_per_second: 94.6
- input_tokens: 139 | output_tokens: 2048
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de profundidad y no incluye todos los nodos necesarios para completar el flujo de trabajo, como los nodos de Slack.

## Respuesta completa

# Workflow N8N: Clasificación de Mensajes con IA

```json
{
  "name": "Clasificación de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "functionCode": "// Extraer email y message del body del webhook\nconst body = $input.first().json.body;\n\nconst email = body.email || '';\nconst message = body.message || '';\n\nif (!email || !message) {\n  throw new Error('Faltan campos requeridos: email y message');\n}\n\nreturn [{\n  json: {\n    email: email,\n    message: message\n  }\n}];"
      },
      "id": "extract-fields",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [460, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu tarea es clasificar el mensaje del usuario en UNA de estas tres categorías exactas: \"soporte\", \"ventas\" o \"otro\".\n\nResponde SOLO con la categoría, sin explicaciones ni texto adicional.\n\nReglas:\n- \"soporte\": Si el mensaje solicita ayuda técnica, reporta un problema, tiene una queja sobre un servicio o producto, o necesita asistencia.\n- \"ventas\": Si el mensaje pregunta sobre precios, productos, servicios, ofertas, o tiene intención de compra.\n- \"otro\": Si no encaja en las categorías anteriores."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "openai-classify",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENTIAL_ID_OPENAI",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.message.content.toLowerCase().trim() }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "if-soporte",
      "name": "¿Es Soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [900, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.message.content.toLowerCase().trim() }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "if-ventas",
      "name": "¿Es Ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [900, 440]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=*📧 Nuevo mensaje clasificado como SOPORTE*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1140, 100],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=*📧 Nuevo mensaje clasificado como VENTAS*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1140, 380],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=*📧 Nuevo mensaje clasificado como OTRO*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1140, 560],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ JSON.stringify({ status: 'ok', classification: $('Clasificar con OpenAI').item.json.message.content.trim(), email: $('Extraer Campos').item.json.email }) }}",
        "options": {}
      },
      "id": "respond-webhook",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1380, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
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
            "node": "¿Es Soporte?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es Ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es Soporte?": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    },
    "¿Es Ventas?": {
      "main": [
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #support": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #sales": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #general": {
      "main": [
        [
          {
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "