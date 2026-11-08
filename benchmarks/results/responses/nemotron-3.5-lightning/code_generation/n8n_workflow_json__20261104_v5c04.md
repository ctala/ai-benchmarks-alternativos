# Nemotron 3.5 Lightning — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 7.51 | quality: 7.2
- latency_total: 3.837s | tokens_per_second: 412.1
- input_tokens: 133 | output_tokens: 1581
- judge_score: 3.0 | justificación: 

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

Aquí tienes el workflow completo de N8N en formato JSON.

Este workflow está diseñado para recibir un POST con un cuerpo JSON (ej. `{"email": "test@test.com", "message": "Hola"}`), clasificar el mensaje usando OpenAI y enrutar el correo al canal de Slack correspondiente.

### Instrucciones de configuración:
1.  **Webhook**: Copia la URL generada y úsala para enviar tus POST requests.
2.  **OpenAI**: Asegúrate de tener una clave de API configurada en las credenciales del nodo "OpenAI" y selecciona el modelo deseado (ej. `gpt-3.5-turbo`).
3.  **Slack**: Configura las credenciales de Slack y asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu workspace.

```json
{
  "name": "Clasificar y Enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "path": "mensaje",
        "method": "POST",
        "responseMode": "onReceived",
        "responseCode": 200,
        "responseBody": "Mensaje recibido y procesado"
      },
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "operation": "chatCompletion",
        "systemMessage": "Clasifica el siguiente mensaje de cliente en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Responde SOLO con el nombre de la categoría, sin explicaciones adicionales.",
        "userMessage": "Mensaje: {{ $json.message }}\nEmail: {{ $json.email }}"
      },
      "name": "Clasificar Mensaje (OpenAI)",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "credentials": {
        "openAiApi": "OpenAI Credentials"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.category}}",
              "operation": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "name": "Ruteo Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        750,
        100
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📥 **Nuevo ticket de soporte**\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}"
      },
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        50
      ],
      "credentials": {
        "slackApi": "Slack Credentials"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.category}}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "name": "Ruteo Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        750,
        250
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📈 **Nueva consulta de ventas**\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}"
      },
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        200
      ],
      "credentials": {
        "slackApi": "Slack Credentials"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.category}}",
              "operation": "equal",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "Ruteo Otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        750,
        450
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📝 **Mensaje general**\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}"
      },
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        400
      ],
      "credentials": {
        "slackApi": "Slack Credentials"
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje (OpenAI)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Mensaje (OpenAI)": {
      "main": [
        [
          {
            "node": "Ruteo Soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "Ruteo Ventas",
            "type": "main",
            "index": 0
          },
          {
            "node": "Ruteo Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ruteo Soporte": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ruteo Ventas": {
      "main": [
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ruteo Otro": {
      "main": [
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  }
}
```