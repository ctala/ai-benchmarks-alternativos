# Nemotron 3 Super — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.44 | quality: 8.0
- latency_total: 30.704s | tokens_per_second: 97.7
- input_tokens: 133 | output_tokens: 3000
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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
      "parameters": {},
      "name": "Webhook",
      "type": "webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "email-classifier"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "set": {
          "email": {
            "value": "={{$json[\"email\"]}}",
            "name": "email"
          },
          "message": {
            "value": "={{$json[\"message\"]}}",
            "name": "message"
          }
        }
      },
      "name": "Set",
      "type": "set",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "operation": "chat",
        "model": "gpt-3.5-turbo",
        "systemMessage": "Classify the user message into one of: soporte, ventas, otro. Respond with only the word.",
        "userMessage": "={{$json[\"message\"]}}",
        "responseFormat": "text"
      },
      "name": "OpenAI",
      "type": "openai",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openaiApi": "openai_credential_id"
      }
    },
    {
      "parameters": {
        "value": "={{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
        "rules": {
          "string": [
            { "value": "soporte", "name": "Soporte" },
            { "value": "ventas",  "name": "Ventas" },
            { "value": "otro",    "name": "Otro" }
          ]
        }
      },
      "name": "Switch",
      "type": "switch",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo email de soporte: {{$json[\"email\"]}}\nMensaje: {{$json[\"message\"]}}"
      },
      "name": "Slack Support",
      "type": "slack",
      "typeVersion": 2,
      "position": [1050, 200],
      "credentials": {
        "slackApi": "slack_credential_id"
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo email de ventas: {{$json[\"email\"]}}\nMensaje: {{$json[\"message\"]}}"
      },
      "name": "Slack Sales",
      "type": "slack",
      "typeVersion": 2,
      "position": [1050, 300],
      "credentials": {
        "slackApi": "slack_credential_id"
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo email otro: {{$json[\"email\"]}}\nMensaje: {{$json[\"message\"]}}"
      },
      "name": "Slack General",
      "type": "slack",
      "typeVersion": 2,
      "position": [1050, 400],
      "credentials": {
        "slackApi": "slack_credential_id"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
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
  "active": false,
  "settings": {},
  "id": "1"
}
```