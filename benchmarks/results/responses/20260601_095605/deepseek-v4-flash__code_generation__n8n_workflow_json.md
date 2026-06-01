# DeepSeek V4 Flash (OpenRouter) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.42 | quality: 7.72
- latency_total: 31.932s | tokens_per_second: 63.1
- input_tokens: 126 | output_tokens: 2016
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "name": "Workflow Clasificación y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "options": {},
        "responseMode": "lastNode",
        "responseData": "allEntries",
        "respondWithEmptyBody": false,
        "rawBody": false
      },
      "id": "webhook-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "values": {},
        "options": {}
      },
      "id": "set-1",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {}
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {},
        "promptType": "define",
        "text": "Clasifica el siguiente mensaje en una de estas categorías: \"soporte\", \"ventas\", \"otro\". Responde únicamente con un JSON en el siguiente formato: {\"category\": \"soporte\"}. Mensaje: {{$json.message}}",
        "responseFormat": "json_object",
        "temperature": 0.2,
        "maxTokens": 50
      },
      "id": "openai-1",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "dataType": "number",
        "value1": "={{ $json.category }}",
        "rules": [
          {
            "value2": "soporte",
            "output": 0
          },
          {
            "value2": "ventas",
            "output": 1
          },
          {
            "value2": "otro",
            "output": 2
          }
        ],
        "fallbackOutput": 2
      },
      "id": "switch-1",
      "name": "Switch por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\nEmail: {{$json.email}}\nMensaje: {{$json.message}}",
        "username": "Workflow Bot",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 150],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\nEmail: {{$json.email}}\nMensaje: {{$json.message}}",
        "username": "Workflow Bot",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 300],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje (sin clasificar):\nEmail: {{$json.email}}\nMensaje: {{$json.message}}",
        "username": "Workflow Bot",
        "otherOptions": {}
      },
      "id": "slack-other",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 450],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer campos": {
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
            "node": "Switch por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por categoría": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "versionId": "example-version",
  "active": false,
  "settings": {},
  "tags": [],
  "id": "workflow-1"
}
```