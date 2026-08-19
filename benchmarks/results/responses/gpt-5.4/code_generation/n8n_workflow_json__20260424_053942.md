# GPT-5.4 — code_generation/n8n_workflow_json

- model_id: `gpt-5.4`
- success: True  | final: 7.07 | quality: 7.92
- latency_total: 14.701s | tokens_per_second: 86.6
- input_tokens: 118 | output_tokens: 1273
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "name": "Clasificar mensajes y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        240,
        300
      ],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "2",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        460,
        300
      ]
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
              "content": "Clasifica el siguiente mensaje en una sola palabra, usando exclusivamente una de estas opciones: soporte, ventas, otro. No agregues explicación."
            },
            {
              "role": "user",
              "content": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "3",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [
        700,
        300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const categoria = ($json.choices?.[0]?.message?.content || '').trim().toLowerCase();\nconst email = $items('Extraer Datos', 0, 0)[0].json.email;\nconst message = $items('Extraer Datos', 0, 0)[0].json.message;\n\nlet channel = '#general';\nif (categoria === 'soporte') {\n  channel = '#support';\n} else if (categoria === 'ventas') {\n  channel = '#sales';\n}\n\nreturn [{\n  json: {\n    email,\n    message,\n    categoria,\n    channel\n  }\n}];"
      },
      "id": "4",
      "name": "Preparar Canal",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        940,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "={{ $json.channel }}",
        "text": "Nuevo mensaje recibido\n\n*Clasificación:* {{ $json.categoria }}\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "5",
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1180,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Preparar Canal",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar Canal": {
      "main": [
        [
          {
            "node": "Enviar a Slack",
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
  },
  "versionId": "1",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "pinData": {}
}
```

Notas rápidas:
- Debes reemplazar:
  - `OPENAI_CREDENTIAL_ID`
  - `SLACK_CREDENTIAL_ID`
- El webhook espera un `POST` con body tipo:
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Necesito ayuda con mi cuenta"
}
```

Si quieres, también te puedo generar una versión:
1. con nodos `Switch` en vez de un solo canal dinámico, o
2. compatible con el formato exacto de exportación de tu versión de n8n.