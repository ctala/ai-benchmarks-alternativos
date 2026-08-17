# Claude Opus 4.6 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 6.77 | quality: 7.92
- latency_total: 25.731s | tokens_per_second: 79.6
- input_tokens: 133 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa



# Workflow de N8N - Clasificación de mensajes con IA

A continuación te presento el JSON completo del workflow:

```json
{
  "name": "Clasificación de Mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-entry",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [200, 400],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "jsCode": "// Extraer email y message del body\nconst body = $input.first().json.body;\n\nconst email = body.email || '';\nconst message = body.message || '';\n\nif (!email || !message) {\n  throw new Error('Faltan campos requeridos: email y/o message');\n}\n\nreturn [{\n  json: {\n    email: email,\n    message: message\n  }\n}];"
      },
      "id": "extract-fields",
      "name": "Extraer Email y Message",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [420, 400]
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
              "content": "Eres un clasificador de mensajes. Tu única tarea es clasificar el mensaje del usuario en exactamente UNA de estas tres categorías:\n\n- soporte: problemas técnicos, errores, bugs, solicitudes de ayuda con productos existentes, quejas, devoluciones, problemas con cuentas\n- ventas: consultas sobre precios, cotizaciones, interés en comprar, demos, planes, upgrades, información de productos nuevos\n- otro: cualquier mensaje que no encaje claramente en soporte ni ventas\n\nResponde ÚNICAMENTE con una sola palabra en minúsculas: soporte, ventas o otro. Sin puntuación, sin explicación, sin nada más."
            },
            {
              "role": "user",
              "content": "=Clasifica el siguiente mensaje:\n\n\"{{ $json.message }}\""
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
      "typeVersion": 1.4,
      "position": [640, 400],
      "credentials": {
        "openAiApi": {
          "id": "OPEN_AI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Limpiar y normalizar la respuesta de OpenAI\nconst input = $input.first().json;\n\n// Extraer el texto de la respuesta de OpenAI\nlet classification = (input.message?.content || input.choices?.[0]?.message?.content || '').trim().toLowerCase();\n\n// Normalizar: eliminar puntuación y espacios extra\nclassification = classification.replace(/[^a-záéíóúñ]/g, '');\n\n// Validar que sea una categoría válida\nconst validCategories = ['soporte', 'ventas', 'otro'];\nif (!validCategories.includes(classification)) {\n  classification = 'otro';\n}\n\n// Mapear categoría a canal de Slack\nconst channelMap = {\n  'soporte': '#support',\n  'ventas': '#sales',\n  'otro': '#general'\n};\n\nreturn [{\n  json: {\n    email: $('Extraer Email y Message').first().json.email,\n    message: $('Extraer Email y Message').first().json.message,\n    classification: classification,\n    slackChannel: channelMap[classification]\n  }\n}];"
      },
      "id": "process-classification",
      "name": "Procesar Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [860, 400]
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
              "leftValue": "={{ $json.classification }}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "switch-soporte",
      "name": "¿Es Soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [1080, 400]
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
              "id": "condition-ventas",
              "leftValue": "={{ $json.classification }}",
              "rightValue": "ventas",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "switch-ventas",
      "name": "¿Es Ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [1300, 520]
    },
    {
      "parameters": {
        "resource": "message",
        "channel": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:rotating_light: *Nuevo mensaje de SOPORTE*\n\n:email: *De:* {{ $('Procesar Clasificación').first().json.email }}\n:speech_balloon: *Mensaje:* {{ $('Procesar Clasificación').first().json.message }}\n:label: *Clasificación:* Soporte",
        "otherOptions": {
          "unfurl_links": false,
          "unfurl_media": false
        }
      },
      "id": "slack-support",
      "name": "Slack → #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1520, 280],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
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
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n\n:email: *De:* {{ $('Procesar Clasificación').first().json.email }}\n:speech_balloon: *Mensaje:* {{ $('Procesar Clasificación').first().json.message }}\n:label: