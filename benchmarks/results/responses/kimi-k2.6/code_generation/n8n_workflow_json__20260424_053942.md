# Kimi K2.6 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 6.51 | quality: 8.32
- latency_total: 236.702s | tokens_per_second: 33.3
- input_tokens: 132 | output_tokens: 7875
- judge_score: 3.8 | justificación: 

## Respuesta completa

 Aquí tienes el workflow completo en JSON para **n8n**. Al importarlo, solo necesitarás conectar tus credenciales de **OpenAI** y **Slack**.

```json
{
  "name": "Webhook Clasificador IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "a1b2c3d4-1111-2222-3333-123456789abc",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [260, 340],
      "webhookId": "clasificar-mensaje-01"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-2222-3333-4444-123456789abc",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [520, 340]
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
              "content": "Eres un clasificador de mensajes. Responde ÚNICAMENTE con una palabra en minúsculas: soporte, ventas u otro."
            },
            {
              "role": "user",
              "content": "={{ 'Email: ' + $json.email + '\\nMensaje: ' + $json.message + '\\n\\nClasificación:' }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-3333-4444-5555-123456789abc",
      "name": "OpenAI Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [780, 340]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-category",
              "name": "category",
              "value": "={{ ($json.message?.content ?? $json.content ?? 'otro').toString().trim().toLowerCase() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-4444-5555-6666-123456789abc",
      "name": "Normalizar Categoria",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [1040, 340]
    },
    {
      "parameters": {
        "mode": "rules",
        "dataType": "string",
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "output": 0
            },
            {
              "value": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": "extra"
      },
      "id": "a1b2c3d4-5555-6666-7777-123456789abc",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [1300, 340]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "={{ '*📩 Nuevo mensaje de ' + $json.category.toUpperCase() + '*\\n\\n*De:* ' + $json.email + '\\n*Mensaje:* ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-6666-7777-8888-123456789abc",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1680, 140]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "={{ '*📩 Nuevo mensaje de ' + $json.category.toUpperCase() + '*\\n\\n*De:* ' + $json.email + '\\n*Mensaje:* ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-7777-8888-9999-123456789abc",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1680, 340]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "={{ '*📩 Nuevo mensaje de ' + $json.category.toUpperCase() + '*\\n\\n*De:* ' + $json.email + '\\n*Mensaje:* ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-8888-9999-aaaa-123456789abc",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1680, 540]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          {
            "node": "OpenAI Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Clasificar": {
      "main": [
        [
          {
            "node": "Normalizar Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Categoria": {
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
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
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
  "settings": {
    "executionOrder": "v1"
  },
  "tags": []
}
```

### Instrucciones rápidas:

1. **Importa** el JSON en n8n (**Workflows > Import from file** o copiar y pegar en el editor).
2. **Configura las credenciales** cuando te lo pida:
   - Una para **OpenAI** (API Key).
   - Una para **Slack** (OAuth2 o Access Token con permisos `chat:write`).
3. **Asegúrate de que los canales existan** en tu Slack (`#support`, `#sales`, `#general`). Si usas nombres diferentes, edítalos en cada nodo Slack.
4. **Activa el webhook** y prueba con:

```bash
curl -X POST https://TU-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"Necesito ayuda con mi factura"}'
```

El flujo clasificará el mensaje con OpenAI y lo enviará al canal correspondiente en Slack.