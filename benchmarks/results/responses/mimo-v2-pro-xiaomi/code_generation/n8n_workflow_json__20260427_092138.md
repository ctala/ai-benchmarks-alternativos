# MiMo V2-Pro (Xiaomi direct) — code_generation/n8n_workflow_json

- model_id: `mimo-v2-pro`
- success: True  | final: 7.37 | quality: 7.92
- latency_total: 31.06s | tokens_per_second: 65.9
- input_tokens: 364 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

# Workflow N8N: Clasificación de Mensajes con IA y Slack

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificación de Mensajes con IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "assign-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "extract-fields",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [470, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el mensaje del usuario y responde ÚNICAMENTO con una de estas tres palabras (sin puntuación, sin explicación):\n\n- soporte → si el mensaje es una queja, problema técnico, error, bug, o solicitud de ayuda técnica\n- ventas → si el mensaje es una consulta de precios, compra, licencia, demo, o interés comercial\n- otro → si no encaja en las categorías anteriores"
            },
            {
              "role": "user",
              "content": "=Clasifica este mensaje:\n\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-classify",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [690, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENTIAL_ID",
          "name": "OpenAI API"
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
                  "typeValidation": "strict"
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
                  "typeValidation": "strict"
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
                  "typeValidation": "strict"
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
        "options": {
          "fallbackOutput": "extra",
          "allMatchingOutputs": false
        }
      },
      "id": "switch-router",
      "name": "Router por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [910, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🎫 *Nuevo mensaje de SOPORTE*\n\n📧 *Email:* {{ $('Extraer Campos').item.json.email }}\n💬 *Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1150, 140],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo mensaje de VENTAS*\n\n📧 *Email:* {{ $('Extraer Campos').item.json.email }}\n💬 *Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1150, 300],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📬 *Nuevo mensaje GENERAL*\n\n📧 *Email:* {{ $('Extraer Campos').item.json.email }}\n💬 *Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1150, 460],
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
        "responseBody": "={{ JSON.stringify({ status: 'ok', clasificacion: $('Clasificar con OpenAI').item.json.message.content }) }}"
      },
      "id": "respond-webhook",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1370, 300]
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