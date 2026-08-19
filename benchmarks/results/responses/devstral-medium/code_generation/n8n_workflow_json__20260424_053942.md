# Devstral Medium — code_generation/n8n_workflow_json

- model_id: `mistralai/devstral-medium`
- success: True  | final: 6.81 | quality: 6.88
- latency_total: 11.195s | tokens_per_second: 135.9
- input_tokens: 120 | output_tokens: 1521
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n que cumple con los requisitos que has especificado:

```json
{
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [
        240,
        300
      ]
    },
    {
      "parameters": {
        "path": "webhook",
        "httpMethod": "POST",
        "responseMode": "onReceived",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        440,
        300
      ]
    },
    {
      "parameters": {
        "functionCode": "const email = $json.email;\nconst message = $json.message;\n\nreturn [\n  {\n    json: {\n      email,\n      message\n    }\n  }\n];"
      },
      "name": "Extract Email and Message",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        640,
        300
      ]
    },
    {
      "parameters": {
        "model": "text-davinci-003",
        "prompt": "Classify the following message as 'soporte', 'ventas', or 'otro':\n\nMessage: {{ $json.message }}\n\nClassification:",
        "temperature": 0.7,
        "maxTokens": 5,
        "topP": 1,
        "frequencyPenalty": 0,
        "presencePenalty": 0,
        "stop": [
          "\n"
        ]
      },
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        840,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "New support message from {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1040,
        200
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "New sales message from {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1040,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "New message from {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1040,
        400
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{ $json.classification }}",
              "operation": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "name": "IF Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        1240,
        200
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{ $json.classification }}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "name": "IF Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        1240,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "{{ $json.classification }}",
              "operation": "equal",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "IF Otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        1240,
        400
      ]
    }
  ],
  "connections": {
    "Start": {
      "main": [
        [
          {
            "node": "Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Email and Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Email and Message": {
      "main": [
        [
          {
            "node": "OpenAI Classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "IF Soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "IF Ventas",
            "type": "main",
            "index": 0
          },
          {
            "node": "IF Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Soporte": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Ventas": {
      "main": [
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Otro": {
      "main": [
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

Este workflow de n8n se activa con un webhook POST, extrae el campo "email" y "message" del body, usa un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro", y según la clasificación, envía el email a un canal de Slack diferente.