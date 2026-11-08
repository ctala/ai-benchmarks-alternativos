# DeepSeek V4 Pro — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 95.241s | tokens_per_second: 76.9
- input_tokens: 126 | output_tokens: 7325
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un uso adecuado de los nodos de N8N. La estructura es clara y fácil de entender, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o la gestión de errores.

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

{
  "name": "Email Message Routing",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook",
        "responseMode": "lastNode"
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "keepOnlySet": true,
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
      "id": "set-email",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "send",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "user",
              "content": "Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\". Responde únicamente con la categoría sin explicación adicional.\n\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        },
        "includeInputData": true
      },
      "id": "openai-classify",
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2,
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
        "values": {
          "string": [
            {
              "name": "classification",
              "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
            }
          ]
        }
      },
      "id": "set-classification",
      "name": "Simplify Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": false,
            "type": "string",
            "value1": "={{ $json.classification }}"
          },
          "rules": [
            {
              "value1": "soporte",
              "output": 0
            },
            {
              "value1": "ventas",
              "output": 1
            },
            {
              "value1": "otro",
              "output": 2
            }
          ]
        },
        "options": {
          "fallbackOutput": 2
        }
      },
      "id": "switch-route",
      "name": "Route",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [1050, 300]
    },
    {
      "parameters": {
        "resource": "channel",
        "operation": "postMessage",
        "channel": "#support",
        "text": "Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "slack-support",
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
        "resource": "channel",
        "operation": "postMessage",
        "channel": "#sales",
        "text": "Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "slack-sales",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
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
        "resource": "channel",
        "operation": "postMessage",
        "channel": "#general",
        "text": "Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 400],
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
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Simplify Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Simplify Classification": {
      "main": [
        [
          {
            "node": "Route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route": {
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
  "settings": {}
}