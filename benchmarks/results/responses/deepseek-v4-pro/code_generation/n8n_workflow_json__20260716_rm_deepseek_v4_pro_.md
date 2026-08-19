# DeepSeek V4 Pro — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.06 | quality: 6.6
- latency_total: 101.304s | tokens_per_second: 48.3
- input_tokens: 126 | output_tokens: 4893
- judge_score: 3.0 | justificación: 

## Respuesta completa

```json
{
  "name": "Email Classifier to Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "keepOnlySet": false,
        "values": {},
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "name": "Set original",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "authentication": "openAiApi",
        "resource": "chat",
        "operation": "message",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "user",
              "content": "=Classify the following message into one of these categories: soporte, ventas, otro. Only respond with the category.\n\nMessage: {{ $json.message }}\n\nCategory:"
            }
          ]
        },
        "options": {}
      },
      "id": "c3d4e5f6-a789-012b-cdef-123456789012",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [450, 500],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "combine",
        "combinationMode": "mergeByIndex",
        "options": {}
      },
      "id": "d4e5f6a7-8901-23cd-ef01-234567890123",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "typeVersion": 2,
      "position": [650, 400]
    },
    {
      "parameters": {
        "functionCode": "const classification = $input.first().json.choices[0].message.content.trim().toLowerCase();\nreturn [{\n  json: {\n    email: $input.first().json.email,\n    message: $input.first().json.message,\n    classification: classification\n  }\n}];"
      },
      "id": "e5f6a789-0123-4def-0123-456789012345",
      "name": "Extract classification",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [850, 400]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": "equals"
                  }
                ],
                "combinator": "and"
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": "equals"
                  }
                ],
                "combinator": "and"
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": "equals"
                  }
                ],
                "combinator": "and"
              }
            }
          ]
        },
        "options": {}
      },
      "id": "f6a78901-2345-6ef0-1234-567890123456",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [1050, 400]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=New message from {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "a7890123-4567-8f01-2345-678901234567",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 200],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=New message from {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "b8901234-5678-9f01-3456-789012345678",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 400],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=New message from {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "c9012345-6789-0f12-4567-890123456789",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 600],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set original",
            "type": "main",
            "index": 0
          },
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set original": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 1
          }
        ]
      ]
    },
    "OpenAI": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge": {
      "main": [
        [
          {
            "node": "Extract classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract classification": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```