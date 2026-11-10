# GPT-OSS 20B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 6.61 | quality: 6.52
- latency_total: 46.482s | tokens_per_second: 136.5
- input_tokens: 179 | output_tokens: 6347
- judge_score: 2.8 | justificación: 

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
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming",
        "responseMode": "onReceived"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        100,
        300
      ]
    },
    {
      "parameters": {
        "values": [
          {
            "name": "email",
            "value": "={{$json.email}}"
          },
          {
            "name": "message",
            "value": "={{$json.message}}"
          }
        ],
        "options": {}
      },
      "name": "Set Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        300,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "user",
            "content": "={{'Please classify the following message as one of the following categories: soporte, ventas, otro. Message: ' + $json.email + ' - ' + $json.message}}"
          }
        ],
        "temperature": 0,
        "maxTokens": 10,
        "responseType": "text"
      },
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "credentials": {
        "openaiApiKey": "OpenAI API Key"
      },
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "values": [
          {
            "name": "category",
            "value": "={{$json.choices[0].message.content.trim()}}"
          }
        ],
        "options": {}
      },
      "name": "Set Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        700,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": {
            "category": [
              {
                "value": "soporte",
                "operationType": "matching"
              },
              {
                "value": "ventas",
                "operationType": "matching"
              },
              {
                "value": "otro",
                "operationType": "matching"
              }
            ]
          }
        }
      },
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        900,
        300
      ]
    },
    {
      "parameters": {
        "options": {
          "channel": "#support",
          "text": "Email: {{$json.email}}\nMessage: {{$json.message}}"
        }
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "credentials": {
        "slackApiV2": "Slack API"
      },
      "position": [
        1100,
        150
      ]
    },
    {
      "parameters": {
        "options": {
          "channel": "#sales",
          "text": "Email: {{$json.email}}\nMessage: {{$json.message}}"
        }
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "credentials": {
        "slackApiV2": "Slack API"
      },
      "position": [
        1100,
        300
      ]
    },
    {
      "parameters": {
        "options": {
          "channel": "#general",
          "text": "Email: {{$json.email}}\nMessage: {{$json.message}}"
        }
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "credentials": {
        "slackApiV2": "Slack API"
      },
      "position": [
        1100,
        450
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set Fields",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ]
    },
    "Set Fields": {
      "main": [
        [
          {
            "node": "OpenAI Classify",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "Set Category",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ]
    },
    "Set Category": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ]
    },
    "Switch": {
      "soporte": [
        [
          {
            "node": "Slack Support",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ],
      "ventas": [
        [
          {
            "node": "Slack Sales",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ],
      "otro": [
        [
          {
            "node": "Slack General",
            "type": "string",
            "index": 0,
            "position": 0
          }
        ]
      ]
    }
  }
}
```

> **Notas**  
> * Reemplaza `"OpenAI API Key"` y `"Slack API"` por los nombres de tus credenciales configuradas en n8n.  
> * El campo `email` y `message` se extraen directamente del cuerpo JSON del webhook (`$json.email`, `$json.message`).  
> * El nodo OpenAI devuelve el texto de la respuesta; luego el nodo *Set Category* extrae y limpia la categoría.  
> * El nodo *Switch* dirige la ejecución a uno de los tres nodos Slack según la categoría, enviando el mismo contenido de correo y mensaje.