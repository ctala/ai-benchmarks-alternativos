# DeepSeek V4 Pro — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 42.236s | tokens_per_second: 72.1
- input_tokens: 126 | output_tokens: 3044
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un uso adecuado de los nodos de N8N. La claridad y utilidad práctica son altas, aunque la profundidad podría mejorarse con más detalles sobre la configuración o posibles ajustes.

## Respuesta completa

```json
{
  "name": "Clasificar y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "keep": true,
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "set-extract-fields",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Responde solo con la palabra correspondiente."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-classify",
      "name": "Clasificar con IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "keep": true,
        "values": {
          "string": [
            {
              "name": "classification",
              "value": "={{ $json.choices[0].message.content }}"
            }
          ]
        }
      },
      "id": "set-extract-classification",
      "name": "Extraer clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ],
          "fallbackOutput": "extra"
        }
      },
      "id": "switch-channel",
      "name": "Enrutar por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [1050, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 100],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 300],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 500],
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
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Extraer clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer clasificación": {
      "main": [
        [
          {
            "node": "Enrutar por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por categoría": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```