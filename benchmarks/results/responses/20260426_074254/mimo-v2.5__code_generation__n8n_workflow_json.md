# MiMo-V2.5 (omnimodal) — code_generation/n8n_workflow_json

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 6.58 | quality: 7.08
- latency_total: 13.869s | tokens_per_second: 147.7
- input_tokens: 362 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

# Workflow N8N - Clasificación de Mensajes con IA

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificación de Mensajes con IA",
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
      "position": [240, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "cond-email",
              "leftValue": "={{ $json.body.email }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "exists"
              }
            },
            {
              "id": "cond-message",
              "leftValue": "={{ $json.body.message }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "exists"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "validar-campos",
      "name": "Validar Campos",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [460, 300]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "extraer-campos",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [680, 200]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes de clientes. Clasifica el siguiente mensaje en UNA de estas categorías exactas: \"soporte\", \"ventas\" o \"otro\".\n\nResponde ÚNICAMENTE con la categoría, sin explicaciones ni texto adicional.\n\nMensaje del cliente:\n\"{{ $json.message }}\"",
              "role": "system"
            }
          ]
        },
        "options": {
          "temperature": 0.1,
          "maxTokens": 20
        }
      },
      "id": "openai-clasificar",
      "name": "OpenAI Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [900, 200],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": false,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "cond-soporte",
              "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            },
            {
              "id": "cond-ventas",
              "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
              "rightValue": "ventas",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "or"
        },
        "options": {}
      },
      "id": "switch-clasificacion",
      "name": "Switch Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1140, 200]
    },
    {
      "parameters": {
        "resource": "message",
        "channel": "#support",
        "text": "📩 *Nuevo mensaje clasificado como SOPORTE*\n\n*Email:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:*\n> {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1400, 80],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "channel": "#sales",
        "text": "📩 *Nuevo mensaje clasificado como VENTAS*\n\n*Email:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:*\n> {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1400, 260],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "channel": "#general",
        "text": "📩 *Nuevo mensaje clasificado como OTRO*\n\n*Email:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:*\n> {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1400, 440],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ JSON.stringify({ success: false, error: 'Faltan campos requeridos: email y message' }) }}",
        "options": {
          "responseCode": 400
        }
      },
      "id": "responder-error",
      "name": "Respuesta Error",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [680, 420]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ JSON.stringify({ success: true, classification: $json.message.content.trim() }) }}",
        "options": {
          "responseCode": 200
        }
      },
      "id": "responder-exito",
      "name": "Respuesta Éxito",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1400, 620]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Validar Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Validar Campos": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Respuesta Error",
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
            "node":