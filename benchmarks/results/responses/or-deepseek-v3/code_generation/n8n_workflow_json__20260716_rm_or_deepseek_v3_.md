# DeepSeek V3 — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 7.04 | quality: 7.0
- latency_total: 14.25s | tokens_per_second: 113.2
- input_tokens: 126 | output_tokens: 1613
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de detalles completos y profundidad, como la configuración completa del nodo 'if' y la falta de un nodo 'Slack #general'.

## Respuesta completa

```json
{
  "name": "Clasificación de mensajes con IA y envío a Slack",
  "nodes": [
    {
      "parameters": {},
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "mensaje-clasificacion",
      "notes": "Recibe POST request con email y mensaje"
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "set-node",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.set",
      "typeVersion":", 1,
      "position": [
        450,
        300
      ],
      "notes": "Extrae email y message del body"
    },
    {
      "parameters": {
        "options": {},
        "resource": "chat",
        "operation": "complete",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde SOLO con la palabra de la categoría, sin explicaciones ni puntuación."
            },
            {
              "role": "user",
              "content": "= \"{{$json.message}}\""
            }
          ]
        }
      },
      "id": "openai-node",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "notes": "Clasifica el mensaje en soporte, ventas u otro"
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "if-node",
      "name": "Router por categoría",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        850,
        300
      ],
      "notes": "Dirige según la clasificación de OpenAI"
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "accessToken": "={{$credentials.slackToken}}",
        "resource": "message",
        "operation": "post",
        "channelId": "C1234567890",
        "text": "Nuevo mensaje de **{{$json.email}}**:\n{{$json.message}}\n\n*Categoría: Soporte*"
      },
      "id": "slack-support-node",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        200
      ],
      "notes": "Envía a canal de soporte"
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "accessToken": "={{$credentials.slackToken}}",
        "resource": "message",
        "operation": "post",
        "channelId": "C0987654321",
        "text": "Nuevo mensaje de **{{$json.email}}**:\n{{$json.message}}\n\n*Categoría: Ventas*"
      },
      "id": "slack-sales-node",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "notes": "Envía a canal de ventas"
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "accessToken": "={{$credentials.slackToken}}",
        "resource": "message",
        "operation": "post",
        "channelId": "C1122334455",
        "text": "Nuevo mensaje de **{{$json.email}}**:\n{{$json.message}}\n\n*Categoría: Otro*"
      },
      "id": "slack-general-node",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        400
      ],
      "notes": "Envía a canal general"
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
            "node": "Router por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por categoría": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": .0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 1
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 2
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "triggerCount": 1
}
```

**Notas importantes:**

1. **Configuración del nodo "Extraer datos":** Debes configurar este nodo para asignar:
   - `email`: `{{$json.body.email}}`
   - `message`: `{{$json.body.message}}`

2. **Configuración del nodo "Router por categoría":** Configura las condiciones:
   - **Soporte:** `{{$json.aiResponse}} = "soporte"`
   - **Ventas:** `{{$json.aiResponse}} = "ventas"`
   - **Otro:** `{{$json.aiResponse}} = "otro"`

3. **Credenciales necesarias:**
   - OpenAI: API Key
   - Slack: Access Token (con permisos para enviar mensajes)

4. **IDs de canales de Slack:** Reemplaza `C1234567890`, `C0987654321` y `C1122334455` con los IDs reales de tus canales (#support, #sales, #general).

5. **Webhook URL:** Una vez desplegado, obtendrás una URL única para enviar POST requests con JSON como:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Mi producto no funciona correctamente"
   }
   ```

Este workflow procesa automáticamente los mensajes, los clasifica con IA y los dirige al canal de Slack correspondiente.