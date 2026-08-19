# Kimi K2.6 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.02 | quality: 7.48
- latency_total: 139.702s | tokens_per_second: 53.8
- input_tokens: 132 | output_tokens: 7519
- judge_score: 3.2 | justificación: 

## Respuesta completa

 Aquí tienes el workflow completo en JSON. Al importarlo en N8N solo necesitarás:

1. Configurar tu **credencial de OpenAI**.
2. Configurar tu **credencial de Slack**.
3. Asegurarte de que los canales `#support`, `#sales` y `#general` existen en tu workspace.

```json
{
  "name": "Clasificador OpenAI a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasifica-email",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "a1b2c3d4-0001-0000-0000-000000000000",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ],
      "webhookId": "clasifica-email"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "modelId": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en UNA sola palabra: soporte, ventas, u otro. Responde solo la palabra, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-0000-0000-000000000000",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.message.content.trim().toLowerCase() }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "a1b2c3d4-0003-0000-0000-000000000000",
      "name": "¿Es Soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": ":ticket: *Nuevo mensaje de Soporte*\n*De:* {{ $('Webhook').first().json.email }}\n*Mensaje:* {{ $('Webhook').first().json.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-0004-0000-0000-000000000000",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        900,
        150
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.message.content.trim().toLowerCase() }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "a1b2c3d4-0005-0000-0000-000000000000",
      "name": "¿Es Ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [
        900,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": ":moneybag: *Nuevo mensaje de Ventas*\n*De:* {{ $('Webhook').first().json.email }}\n*Mensaje:* {{ $('Webhook').first().json.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-0006-0000-0000-000000000000",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1150,
        250
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": ":speech_balloon: *Nuevo mensaje (Otros)*\n*De:* {{ $('Webhook').first().json.email }}\n*Mensaje:* {{ $('Webhook').first().json.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-0007-0000-0000-000000000000",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1150,
        450
      ]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "¿Es Soporte?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es Soporte?": {
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
            "node": "¿Es Ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es Ventas?": {
      "main": [
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
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": []
}
```

### Cómo funciona:
1. **Webhook**: escucha en `POST /webhook/clasifica-email`. Espera un JSON como:
   ```json
   {
     "email": "usuario@ejemplo.com",
     "message": "No puedo iniciar sesión en mi cuenta"
   }
   ```
2. **OpenAI**: envía el `message` a GPT con un prompt de sistema que fuerza a responder **solo una palabra**: `soporte`, `ventas` u `otro`.
3. **IF ¿Es Soporte?**: verifica si la respuesta de la IA contiene `soporte`. Si es **true**, envía a `#support`. Si es **false**, continúa al siguiente IF.
4. **IF ¿Es Ventas?**: verifica si la respuesta es `ventas`. Si es **true**, envía a `#sales`. Si es **false**, cae en `#general`.
5. **Slack**: cada nodo de Slack recupera el `email` y `message` originales del nodo Webhook usando `$('Webhook').first().json` y publica la notificación en el canal correspondiente.