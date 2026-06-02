# DeepSeek V4 Flash (OpenRouter) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.91 | quality: 8.6
- latency_total: 28.219s | tokens_per_second: 57.9
- input_tokens: 126 | output_tokens: 1635
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos.

## Respuesta completa

Aquí tienes el workflow completo de n8n en formato JSON:

```json
{
  "name": "Clasificador de mensajes por IA",
  "nodes": [
    {
      "parameters": {},
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "clasificador-mensajes"
    },
    {
      "parameters": {
        "jsCode": "const body = $input.first().json.body;\nreturn [\n  {\n    email: body.email,\n    message: body.message\n  }\n];"
      },
      "id": "extractData",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "options": {},
        "promptType": "define",
        "text": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Responde solo con una palabra.\n\nMensaje: {{ $json.message }}",
        "model": "gpt-3.5-turbo",
        "temperature": 0.3
      },
      "id": "openai",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.text }}",
              "operation": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "ifSoporte",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.text }}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "ifVentas",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 400]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\n\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "username": "Bot Clasificador",
        "iconEmoji": ":robot_face:"
      },
      "id": "slackSupport",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 100]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\n\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "username": "Bot Clasificador",
        "iconEmoji": ":moneybag:"
      },
      "id": "slackSales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 300]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje (sin clasificar):\n\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "username": "Bot Clasificador",
        "iconEmoji": ":grey_question:"
      },
      "id": "slackGeneral",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 500]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer datos": {
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
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es soporte?": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es ventas?": {
      "main": [
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
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
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "pinData": {},
  "versionId": "workflow-version-1"
}
```

## Configuración necesaria:

1. **Credenciales de OpenAI**: Configura tu API key de OpenAI en las credenciales del nodo "Clasificar con OpenAI"

2. **Credenciales de Slack**: Configura tu token de bot de Slack en los nodos de Slack

3. **Webhook URL**: Cuando actives el workflow, obtendrás una URL de webhook (ej: `https://tu-n8n.com/webhook/clasificador-mensajes`)

## Uso:

Envía un POST a la URL del webhook con este formato:
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Necesito ayuda con mi cuenta"
}
```

## Flujo del workflow:

1. **Webhook** recibe el POST
2. **Extraer datos** extrae `email` y `message`
3. **Clasificar con OpenAI** clasifica el mensaje
4. **¿Es soporte?** y **¿Es ventas?** verifican la clasificación
5. Según el resultado, se envía al canal correspondiente:
   - "soporte" → #support
   - "ventas" → #sales
   - cualquier otro → #general