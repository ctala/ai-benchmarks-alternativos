# Claude Haiku 4.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 7.38 | quality: 8.2
- latency_total: 9.662s | tokens_per_second: 212.0
- input_tokens: 133 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

```json
{
  "name": "Email Classification to Slack",
  "nodes": [
    {
      "parameters": {
        "path": "email-classifier",
        "responseMode": "onReceived",
        "responseData": "{\n  \"success\": true,\n  \"message\": \"Email received and processing\"\n}"
      },
      "id": "webhook_trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "functionCode": "// Extraer email y message del body\nconst email = $input.body.email;\nconst message = $input.body.message;\n\nif (!email || !message) {\n  throw new Error('Missing email or message field');\n}\n\nreturn {\n  email: email,\n  message: message\n};"
      },
      "id": "extract_fields",
      "name": "Extract Email & Message",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": []
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "create",
        "model": "gpt-3.5-turbo",
        "messages": {
          "messageValues": [
            {
              "content": "You are a message classifier. Classify the following message into exactly ONE of these categories: 'soporte', 'ventas', or 'otro'. Respond with ONLY the category name, nothing else.\n\nMessage: {{$node[\"extract_fields\"].json.message}}"
            }
          ]
        }
      },
      "id": "openai_classifier",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": "openAiApi"
      }
    },
    {
      "parameters": {
        "functionCode": "// Extraer la clasificación de OpenAI\nconst response = $input.json.choices[0].message.content.trim().toLowerCase();\n\n// Validar que sea una clasificación válida\nconst validCategories = ['soporte', 'ventas', 'otro'];\nconst category = validCategories.includes(response) ? response : 'otro';\n\nreturn {\n  category: category,\n  email: $node[\"extract_fields\"].json.email,\n  message: $node[\"extract_fields\"].json.message\n};"
      },
      "id": "parse_classification",
      "name": "Parse Classification",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [850, 300],
      "credentials": []
    },
    {
      "parameters": {
        "conditions": {
          "conditions": [
            {
              "value1": "={{$node[\"parse_classification\"].json.category}}",
              "condition": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "if_soporte",
      "name": "If Support",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [1050, 200]
    },
    {
      "parameters": {
        "conditions": {
          "conditions": [
            {
              "value1": "={{$node[\"parse_classification\"].json.category}}",
              "condition": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "if_ventas",
      "name": "If Sales",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [1050, 400]
    },
    {
      "parameters": {
        "conditions": {
          "conditions": [
            {
              "value1": "={{$node[\"parse_classification\"].json.category}}",
              "condition": "equal",
              "value2": "otro"
            }
          ]
        }
      },
      "id": "if_other",
      "name": "If Other",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [1050, 600]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 **New Support Email**\n\n**From:** {{$node[\"parse_classification\"].json.email}}\n\n**Message:**\n{{$node[\"parse_classification\"].json.message}}"
      },
      "id": "slack_support",
      "name": "Send to #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 150],
      "credentials": {
        "slackApi": "slackApi"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💼 **New Sales Email**\n\n**From:** {{$node[\"parse_classification\"].json.email}}\n\n**Message:**\n{{$node[\"parse_classification\"].json.message}}"
      },
      "id": "slack_sales",
      "name": "Send to #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 350],
      "credentials": {
        "slackApi": "slackApi"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📬 **New General Email**\n\n**From:** {{$node[\"parse_classification\"].json.email}}\n\n**Message:**\n{{$node[\"parse_classification\"].json.message}}"
      },
      "id": "slack_general",
      "name": "Send to #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 550],
      "credentials": {
        "slackApi": "slackApi"
      }
    }
  ],
  "connections": {
    "webhook_trigger": {
      "main": [
        [
          {
            "node": "extract_fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "extract_fields": {
      "main": [
        [
          {
            "node": "openai_classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "openai_classifier": {
      "main": [
        [
          {
            "node": "parse_classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "parse_classification": {
      "main": [
        [
          {
            "node": "if_soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "if_ventas",
            "type": "main",
            "index": 0
          },
          {
            "node": "if_other",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "if_soporte": {
      "main": [
        [
          {
            "node": "slack_support",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "if_ventas": {
      "main": [
        [
          {
            "node": "slack_sales