# Grok 4.6 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.6`
- success: True  | final: 5.88 | quality: 6.6
- latency_total: 57.625s | tokens_per_second: 65.0
- input_tokens: 319 | output_tokens: 3746
- judge_score: 3.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow.


## Respuesta completa

```json
{
  "name": "Clasificar mensaje y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 400],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body?.email ?? $json.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body?.message ?? $json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 400]
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
              "content": "Eres un clasificador. Debes clasificar el mensaje del usuario en EXACTAMENTE una de estas categorías: soporte, ventas, otro.\n\nReglas:\n- soporte: incidencias, errores, ayuda técnica, tickets, problemas de producto.\n- ventas: precios, presupuestos, contrataciones, demos, compras.\n- otro: cualquier cosa que no encaje en las anteriores.\n\nResponde ÚNICAMENTE con una palabra: soporte, ventas u otro. Sin comillas, sin puntuación y sin explicación."
            },
            {
              "content": "=Email del remitente: {{ $json.email }}\nMensaje:\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [680, 400],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "cat-field",
              "name": "categoria",
              "value": "={{ ($json.message?.content ?? $json.text ?? $json.choices?.[0]?.message?.content ?? '').toString().toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "email-keep",
              "name": "email",
              "value": "={{ $('Extraer campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "msg-keep",
              "name": "message",
              "value": "={{ $('Extraer campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "d4e5f6a7-b8c9-0123-def0-234567890123",
      "name": "Normalizar clasificacion",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
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
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
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
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
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
          "fallbackOutput": "extra"
        }
      },
      "id": "e5f6a7b8-c9d0-1234-ef01-345678901234",
      "name": "Enrutar por categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 400]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#support"
        },
        "text": "=*Nuevo ticket de soporte*\n• Email: {{ $json.email }}\n• Clasificación: soporte\n\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-d0e1-2345-f012-456789012345",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1400, 160],
      "webhookId": "slack-support",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#sales"
        },
        "text": "=*Nuevo lead / consulta de ventas*\n• Email: {{ $json.email }}\n• Clasificación: ventas\n\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a7b8c9d0-e1f2-3456-0123-567890123456",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1400, 360],
      "webhookId": "slack-sales",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId