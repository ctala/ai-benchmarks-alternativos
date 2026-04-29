# GLM 5 (NIM) — code_generation/n8n_workflow_json

- model_id: `z-ai/glm5`
- success: True  | final: 6.08 | quality: 6.8
- latency_total: 202.048s | tokens_per_second: 10.1
- input_tokens: 114 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

## Respuesta completa

Aquí tienes el workflow completo en formato JSON para n8n. 

Este workflow utiliza un nodo **Switch** para evaluar la clasificación devuelta por OpenAI y enrutar el mensaje al canal de Slack correspondiente. También incluye un manejo de errores básico por si la IA devuelve una categoría no esperada.

Copia el siguiente JSON y pégalo directamente en tu instancia de n8n (usando `Ctrl+V` o `Cmd+V` en el lienzo):

```json
{
  "name": "Clasificación y Enrutamiento a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        220,
        300
      ],
      "webhookId": "webhook-clasificar"
    },
    {
      "parameters": {
        "jsCode": "const items = $input.all();\nconst returnData = [];\n\nfor (const item of items) {\n  const email = item.json.body.email;\n  const message = item.json.body.message;\n  \n  if (!email || !message) {\n    throw new Error('El body debe contener los campos \"email\" y \"message\"');\n  }\n  \n  returnData.push({ json: { email, message } });\n}\n\nreturn returnData;"
      },
      "id": "extract-data",
      "name": "Extraer Email y Mensaje",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        440,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "promptType": "define",
        "text": "={{ $json.message }}"
      },
      "id": "openai-classify",
      "name": "OpenAI (Clasificar)",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.3,
      "position": [
        660,
        300
      ],
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "promptType": "define",
        "text": "={{ $json.message }}"
      }
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "Clasifica el siguiente mensaje en una de estas tres categorías exactas: 'soporte', 'ventas' o 'otro'.\n\nMensaje: {{ $json.message }}\n\nResponde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin puntos, sin comas ni explicaciones.",
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-llm-chain",
      "name": "Cadena de Clasificación",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.2,
      "position": [
        660,
        300
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "classification_assignment",
              "name": "classification",
              "value": "={{ $json.output.toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "email_assignment",
              "name": "email",
              "value": "={{ $('Extraer Email y Mensaje').item.json.email }}",
              "type": "string"
            },
            {
              "id": "message_assignment",
              "name": "message",
              "value": "={{ $('Extraer Email y Mensaje').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "prepare-switch",
      "name": "Preparar Datos para Switch",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [
        880,
        300
      ]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.classification }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "outputKey": "soporte"
            },
            {
              "value2": "ventas",
              "outputKey": "ventas"
            },
            {
              "value2": "otro",
              "outputKey": "otro"
            }
          ]
        },
        "fallbackOutput": 3
      },
      "id": "switch-routing",
      "name": "Switch (Enrutador)",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        1100,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🎫 *Nuevo ticket de Soporte*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack (#support)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1340,
        180
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nuevo lead de Ventas*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack (#sales)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1340,
        340
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "ℹ️ *Nuevo mensaje General*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-otro",
      "name": "Slack (#general)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1340,
        500
      ]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ JSON.stringify({ status: 'success', classification: $json.classification }) }}",
        "options": {}
      },
      "id": "webhook-response",
      "name": "Respuesta al Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [
        1560,
        300
      ]
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Extraer Email y Mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Email y Mensaje": {
      "main": [
        [
          {
            "node": "Cadena de Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Cadena de Clasificación": {
      "main": [
        [
          {
            "node": "Preparar Datos para Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar Datos para Switch": {
      "main": [
        [
          {
            "node": "Switch (Enrutador)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch (Enrutador)": {
      "main": [
        [
          {
            "node": "Slack (#support)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#sales)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#general)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#general)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack (#support)": {
      "main": [
        [
          {
            "node": "Respuesta al Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack (#sales)": {
      "main": [
        [
         