# Claude Opus 4.8 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 6.84 | quality: 8.2
- latency_total: 21.019s | tokens_per_second: 97.4
- input_tokens: 175 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con claridad y estructura adecuada, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

# Workflow de N8N: Clasificación y Enrutamiento de Mensajes

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificacion de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
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
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes. Debes clasificar el mensaje del usuario en una de estas tres categorias EXACTAS: 'soporte', 'ventas' u 'otro'. Responde UNICAMENTE con una sola palabra en minusculas: soporte, ventas o otro. No agregues explicaciones ni puntuacion.",
              "role": "system"
            },
            {
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
          "id": "openai-credentials",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-clasificacion",
              "name": "clasificacion",
              "value": "={{ $json.message.content.toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "assign-email-final",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "assign-message-final",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
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
                    "leftValue": "={{ $json.clasificacion }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
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
                    "leftValue": "={{ $json.clasificacion }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
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
      "name": "Enrutar por Clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1120, 400]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo mensaje de SOPORTE*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support-node",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1400, 200],
      "credentials": {
        "slackApi": {
          "id": "slack-credentials",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text