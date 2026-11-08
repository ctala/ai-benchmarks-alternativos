# Llama 3.3 70B — code_generation/n8n_workflow_json

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 6.66 | quality: 6.6
- latency_total: 14.422s | tokens_per_second: 90.5
- input_tokens: 125 | output_tokens: 1305
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

Aquí te dejo el JSON del workflow de N8N que cumple con tus requisitos:
```json
{
  "name": "Clasificar y enviar mensaje a Slack",
  "nodes": [
    {
      "parameters": {},
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        100,
        100
      ],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json.body.email}}"
            },
            {
              "name": "message",
              "value": "={{$json.body.message}}"
            }
          ]
        }
      },
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        250,
        100
      ]
    },
    {
      "parameters": {
        "apiVersion": "2022-06-15",
        "model": "text-davinci-002",
        "prompt": "Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\": {{message}}",
        "temperature": 0.7,
        "maxTokens": 2048
      },
      "name": "Clasificar mensaje",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        400,
        100
      ],
      "credentials": {
        "openai": {
          "id": "tu-id-de-openai",
          "apiKey": "tu-api-key-de-openai"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.clasificacion}}",
              "operator": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "name": "Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        550,
        50
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.clasificacion}}",
              "operator": "equals",
              "value2": "ventas"
            }
          ]
        }
      },
      "name": "Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        550,
        200
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.clasificacion}}",
              "operator": "equals",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "Otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        550,
        350
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Mensaje de soporte de {{email}}: {{message}}"
      },
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        750,
        50
      ],
      "credentials": {
        "slack": {
          "id": "tu-id-de-slack",
          "accessToken": "tu-access-token-de-slack"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Mensaje de ventas de {{email}}: {{message}}"
      },
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        750,
        200
      ],
      "credentials": {
        "slack": {
          "id": "tu-id-de-slack",
          "accessToken": "tu-access-token-de-slack"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Mensaje de {{email}}: {{message}}"
      },
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        750,
        350
      ],
      "credentials": {
        "slack": {
          "id": "tu-id-de-slack",
          "accessToken": "tu-access-token-de-slack"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        "Extraer campos"
      ]
    },
    "Extraer campos": {
      "main": [
        "Clasificar mensaje"
      ]
    },
    "Clasificar mensaje": {
      "main": [
        "Soporte",
        "Ventas",
        "Otro"
      ]
    },
    "Soporte": {
      "main": [
        "Enviar a #support"
      ]
    },
    "Ventas": {
      "main": [
        "Enviar a #sales"
      ]
    },
    "Otro": {
      "main": [
        "Enviar a #general"
      ]
    }
  }
}
```
Recuerda que debes reemplazar los valores de `tu-id-de-openai`, `tu-api-key-de-openai`, `tu-id-de-slack` y `tu-access-token-de-slack` con tus propios valores de API.

Este workflow se activa con un webhook POST, extrae los campos "email" y "message" del body, clasifica el mensaje usando OpenAI y envía el mensaje a un canal de Slack diferente según la clasificación.