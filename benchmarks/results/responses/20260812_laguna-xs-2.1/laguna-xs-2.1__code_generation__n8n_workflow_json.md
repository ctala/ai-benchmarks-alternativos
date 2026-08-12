# Poolside Laguna XS 2.1 — code_generation/n8n_workflow_json

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 7.9 | quality: 8.0
- latency_total: 10.787s | tokens_per_second: 187.2
- input_tokens: 140 | output_tokens: 2019
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, siguiendo las instrucciones para crear un flujo de trabajo de N8N. La estructura es clara y útil para un emprendedor, aunque la profundidad podría mejorarse con más detalles sobre la configuración o manejo de errores.

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
  "name": "Classify and Route Messages",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST"
      },
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
              "value": "={{ $json.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.message }}"
            }
          ]
        }
      },
      "name": "Extract Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "model": "gpt-4",
        "messages": [
          {
            "role": "user",
            "content": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro' según su contenido:\n\n{{ $json.message }}"
          }
        ],
        "options": {
          "response_format": {
            "type": "json_schema",
            "json_schema": {
              "name": "classification",
              "strict": true,
              "schema": {
                "type": "object",
                "properties": {
                  "category": {
                    "type": "string",
                    "enum": ["soporte", "ventas", "otro"]
                  }
                },
                "required": ["category"]
              }
            }
          }
        }
      },
      "name": "Classify Message",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openaiApi": "OpenAI API Key"
      }
    },
    {
      "parameters": {
        "rules": [
          {
            "value1": "={{ $json.category }}",
            "operation": "equals",
            "value2": "soporte"
          },
          {
            "value1": "={{ $json.category }}",
            "operation": "equals",
            "value2": "ventas"
          },
          {
            "value1": "={{ $json.category }}",
            "operation": "equals",
            "value2": "otro"
          }
        ]
      },
      "name": "Route to Slack Channel",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Email: {{ $json.email }}\nMessage: {{ $json.message }}"
      },
      "name": "Send to Support Channel",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 150],
      "credentials": {
        "slackApi": "Slack API Token"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Email: {{ $json.email }}\nMessage: {{ $json.message }}"
      },
      "name": "Send to Sales Channel",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 300],
      "credentials": {
        "slackApi": "Slack API Token"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Email: {{ $json.email }}\nMessage: {{ $json.message }}"
      },
      "name": "Send to General Channel",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 450],
      "credentials": {
        "slackApi": "Slack API Token"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Data": {
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
            "node": "Route to Slack Channel",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route to Slack Channel": {
      "main": [
        [
          {
            "node": "Send to Support Channel",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to Sales Channel",
            "type": "main",
            "index": 1
          }
        ],
        [
          {
            "node": "Send to General Channel",
            "type": "main",
            "index": 2
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {
    "timezone": "America/New_York"
  }
}
```