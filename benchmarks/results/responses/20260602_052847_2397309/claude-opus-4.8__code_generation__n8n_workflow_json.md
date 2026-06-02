# Claude Opus 4.8 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 6.55 | quality: 8.2
- latency_total: 20.061s | tokens_per_second: 102.1
- input_tokens: 175 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

## Respuesta completa

# Workflow N8N: Clasificación de Mensajes con IA y Routing a Slack

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificacion IA y Routing a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 400],
      "webhookId": "clasificar-mensaje-webhook"
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
      "id": "extract-fields-node",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 400]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Debes clasificar el mensaje del usuario en EXACTAMENTE una de estas tres categorias: 'soporte', 'ventas' o 'otro'. Responde UNICAMENTE con la palabra de la categoria, sin explicaciones, sin puntuacion adicional, en minusculas."
            },
            {
              "role": "user",
              "content": "=Clasifica el siguiente mensaje:\n\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-node",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [680, 400],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-email-2",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "assign-message-2",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            },
            {
              "id": "assign-categoria",
              "name": "categoria",
              "value": "={{ $json.message.content.toLowerCase().trim() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "prepare-data-node",
      "name": "Preparar Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [900, 400]
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
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "switch-node",
      "name": "Switch Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 400]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "support",
          "mode": "name"
        },
        "text": "=:wrench: *Nuevo mensaje de SOPORTE*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support-node",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1400, 200],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "sales",
          "mode": "name"
        },
        "text": "=:moneybag: *N