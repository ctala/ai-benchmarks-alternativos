# Qwen 3.6 Max — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 5.95 | quality: 6.8
- latency_total: 58.793s | tokens_per_second: 41.5
- input_tokens: 125 | output_tokens: 2442
- judge_score: 3.0 | justificación: 

## Respuesta completa

# Workflow N8N — Clasificador de Mensajes con IA → Slack

A continuación tienes el JSON completo, listo para importar en n8n (v1.x):

```json
{
  "name": "Clasificador de Mensajes → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify",
        "options": {}
      },
      "id": "a1b2c3d4-1111-2222-3333-444455556666",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "wh-classify-001"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el mensaje del usuario y responde EXACTAMENTE con una sola palabra: \"soporte\", \"ventas\" u \"otro\". No añadas explicaciones ni texto adicional."
            },
            {
              "role": "user",
              "content": "=Clasifica el siguiente mensaje:\n\nEmail: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0.1
        }
      },
      "id": "b2c3d4e5-2222-3333-4444-555566667777",
      "name": "OpenAI Clasificador",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.6,
      "position": [460, 300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Account"
        }
      }
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
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
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
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
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
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
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
      "id": "c3d4e5f6-3333-4444-5555-666677778888",
      "name": "Router por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [680, 300]
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#support",
        "messageType": "text",
        "text": "=🔧 *Solicitud de Soporte*\n\n📧 Email: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}\n🤖 Clasificación: {{ $json.message.content }}",
        "otherOptions": {}
      },
      "id": "d4e5f6a7-4444-5555-6666-777788889999",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [900, 120],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID_1",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#sales",
        "messageType": "text",
        "text": "=💰 *Oportunidad de Ventas*\n\n📧 Email: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}\n🤖 Clasificación: {{ $json.message.content }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-5555-6666-7777-888899990000",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [900, 300],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID_2",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#general",
        "messageType": "text",
        "text": "=📋 *Mensaje General*\n\n📧 Email: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}\n🤖 Clasificación: {{ $json.message.content }}",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-6666-7777-8888-999900001111",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [900, 480],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID_3",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "OpenAI Clasificador",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Clasificador": {
      "main": [
        [
          {
            "node": "Router por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por Categoría": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
