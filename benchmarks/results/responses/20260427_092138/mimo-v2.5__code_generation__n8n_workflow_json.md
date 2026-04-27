# MiMo V2.5 (Xiaomi) — code_generation/n8n_workflow_json

- model_id: `mimo-v2.5`
- success: True  | final: 7.18 | quality: 7.08
- latency_total: 17.839s | tokens_per_second: 114.8
- input_tokens: 362 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

# Workflow N8N: Clasificación de Mensajes con IA

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificador de Mensajes con IA",
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
        "jsCode": "// Extraer email y message del body del webhook\nconst body = $input.first().json.body;\n\nif (!body || !body.email || !body.message) {\n  throw new Error('Faltan campos requeridos: email y message');\n}\n\nreturn [{\n  json: {\n    email: body.email,\n    message: body.message,\n    timestamp: new Date().toISOString()\n  }\n}];"
      },
      "id": "extract-data",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [460, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes. Clasifica el siguiente mensaje en UNA sola categoría exacta. Responde SOLO con una de estas palabras exactas (sin comillas, sin puntos, sin texto adicional): soporte, ventas, otro.\n\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0.1,
          "maxTokens": 10
        }
      },
      "id": "openai-classify",
      "name": "OpenAI Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.2,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Obtener la clasificación de la respuesta de OpenAI\nconst openaiResponse = $input.first().json;\nlet clasificacion = '';\n\n// Extraer el texto de la respuesta\nif (openaiResponse.data && openaiResponse.data.choices) {\n  clasificacion = openaiResponse.data.choices[0].message.content.trim().toLowerCase();\n} else if (openaiResponse.text) {\n  clasificacion = openaiResponse.text.trim().toLowerCase();\n} else {\n  clasificacion = JSON.stringify(openaiResponse).trim().toLowerCase();\n}\n\n// Limpiar la clasificación\nclasificacion = clasificacion.replace(/[\"'.,;:!?]/g, '').trim();\n\n// Mapear variantes comunes\nlet categoria = 'otro';\nif (clasificacion.includes('soporte') || clasificacion.includes('support')) {\n  categoria = 'soporte';\n} else if (clasificacion.includes('ventas') || clasificacion.includes('sales')) {\n  categoria = 'ventas';\n} else {\n  categoria = 'otro';\n}\n\n// Obtener datos originales del webhook\nconst originalData = $('Extraer Datos').first().json;\n\nreturn [{\n  json: {\n    email: originalData.email,\n    message: originalData.message,\n    timestamp: originalData.timestamp,\n    clasificacion: categoria,\n    clasificacion_raw: clasificacion\n  }\n}];"
      },
      "id": "parse-classification",
      "name": "Parsear Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [900, 300]
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
              "renameOutput": "Soporte"
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
              "renameOutput": "Ventas"
            }
          ]
        },
        "fallbackOutput": "extra",
        "options": {}
      },
      "id": "switch-routing",
      "name": "Routing",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "🎫 *Nuevo ticket de Soporte*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.clasificacion }}\n*Fecha:* {{ $json.timestamp }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 160],
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
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "💰 *Nuevo lead de Ventas*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.clasificacion }}\n*Fecha:* {{ $json.timestamp }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 300],
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
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "📩 *Mensaje Clasificado como Otro*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.clasificacion }}\n*Fecha:* {{ $json.timestamp }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 440],
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
        "responseBody": "={{ JSON.stringify({ success: true, clasificacion: $json.clasificacion, email: $json.email, message: 'Mensaje clasificado y enviado correctamente' }) }}",
        "options": {
          "responseCode": 200
        }
      },
      "id": "respond-webhook",
      "name":