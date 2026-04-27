# MiMo V2.5-Pro (Xiaomi) — code_generation/n8n_workflow_json

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.08 | quality: 7.08
- latency_total: 28.557s | tokens_per_second: 71.7
- input_tokens: 366 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

# Workflow N8N: Clasificación de Mensajes con IA → Slack

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
      "id": "webhook-node",
      "name": "Webhook Recibir Mensaje",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje"
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
      "id": "extract-fields-node",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [480, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes de atención al cliente. Debes clasificar el mensaje en UNA de estas tres categorías exactas: \"soporte\", \"ventas\" o \"otro\".\n\nResponde SOLO con la categoría, sin explicaciones ni texto adicional.",
              "role": "system"
            },
            {
              "content": "={{ 'Clasifica el siguiente mensaje:\\n\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message }}",
              "role": "user"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 20
        }
      },
      "id": "openai-node",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.4,
      "position": [720, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENTIAL_OPENAI_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            },
            {
              "id": "field-clasificacion",
              "name": "clasificacion",
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "combine-data-node",
      "name": "Combinar Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [960, 300]
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
              "id": "condition-soporte",
              "leftValue": "={{ $json.clasificacion }}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            },
            {
              "id": "condition-ventas",
              "leftValue": "={{ $json.clasificacion }}",
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
      "id": "switch-node",
      "name": "Ruta por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1200, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=📬 *Nuevo mensaje de Soporte*\n\n*Email:* {{ $json.email }}\n*Clasificación:* {{ $json.clasificacion }}\n\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {
          "mrkdwn": true,
          "unfurl_links": false,
          "unfurl_media": false
        }
      },
      "id": "slack-soporte",
      "name": "Slack → #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1500, 120],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_SLACK_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje de Ventas*\n\n*Email:* {{ $json.email }}\n*Clasificación:* {{ $json.clasificacion }}\n\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {
          "mrkdwn": true,
          "unfurl_links": false,
          "unfurl_media": false
        }
      },
      "id": "slack-ventas",
      "name": "Slack → #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1500, 300],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_SLACK_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📋 *Nuevo mensaje General*\n\n*Email:* {{ $json.email }}\n*Clasificación:* {{ $json.clasificacion }}\n\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {
          "mrkdwn": true,
          "unfurl_links": false,
          "unfurl_media": false
        }
      },
      "id": "slack-otro",
      "name": "Slack → #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1500, 480],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_SLACK_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ JSON.stringify({ success: true, clasificacion: $json.clasificacion, enviado_a: $json.clasificacion === 'soporte' ? '#support' : $json.clasificacion === 'ventas' ? '#sales' : '#general' }) }}",
        "options": {}
      },
      "id": "response-node",
      "name": "Respuesta Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1800, 300]
    }
  ],
  "connections": {
    "Webhook Recibir Mensaje": {
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
            "