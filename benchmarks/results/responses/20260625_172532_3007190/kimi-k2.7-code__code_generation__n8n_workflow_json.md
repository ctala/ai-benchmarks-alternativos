# Kimi K2.7 Code — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 5.93 | quality: 7.48
- latency_total: 155.345s | tokens_per_second: 22.7
- input_tokens: 132 | output_tokens: 3522
- judge_score: 3.2 | justificación: 

## Respuesta completa

 Aquí tienes el workflow completo en JSON para N8N. Solo necesitas importarlo en N8N y configurar tus credenciales de **OpenAI** y **Slack**.

```json
{
  "name": "Clasificación de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "messages": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje recibido por un usuario en exactamente UNA de estas categorías: soporte, ventas, otro. Responde únicamente con la palabra de la categoría, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "Email del remitente: {{ $json.body.email }}\n\nMensaje:\n{{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-clasificar-2",
      "name": "OpenAI Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [500, 300]
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "value": "={{ $json.message.content.toLowerCase() }}",
              "output": 0,
              "conditions": [
                {
                  "value": "soporte",
                  "operator": "contains"
                }
              ]
            },
            {
              "value": "={{ $json.message.content.toLowerCase() }}",
              "output": 1,
              "conditions": [
                {
                  "value": "ventas",
                  "operator": "contains"
                }
              ]
            },
            {
              "value": "={{ $json.message.content.toLowerCase() }}",
              "output": 2,
              "conditions": [
                {
                  "value": "otro",
                  "operator": "contains"
                }
              ]
            }
          ]
        }
      },
      "id": "switch-categoria-3",
      "name": "Switch Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [750, 300]
    },
    {
      "parameters": {
        "channel": "=#support",
        "text": "📧 *Nuevo mensaje de soporte*\n\n*De:* {{ $json.body.email }}\n*Categoría:* {{ $json.message.content }}\n\n*Mensaje:*\n{{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-support-4",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1000, 100]
    },
    {
      "parameters": {
        "channel": "=#sales",
        "text": "📧 *Nuevo mensaje de ventas*\n\n*De:* {{ $json.body.email }}\n*Categoría:* {{ $json.message.content }}\n\n*Mensaje:*\n{{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales-5",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1000, 300]
    },
    {
      "parameters": {
        "channel": "=#general",
        "text": "📧 *Nuevo mensaje general*\n\n*De:* {{ $json.body.email }}\n*Categoría:* {{ $json.message.content }}\n\n*Mensaje:*\n{{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general-6",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1000, 500]
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "respond-webhook-7",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1250, 300]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Switch Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoría": {
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
    },
    "Slack Soporte": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack Ventas": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack General": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
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

### Instrucciones rápidas:

1. **Importa el JSON** en N8N: *Workflows → Add Workflow → Import from File*.
2. **Configura credenciales**:
   - En el nodo **OpenAI Clasificar**, añade tu API key de OpenAI.
   - En los nodos **Slack**, añade tu token de Slack.
3. **Activa el Webhook** y prueba con:

```bash
curl -X POST https://TU-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"usuario@ejemplo.com","message":"Necesito ayuda con mi factura"}'
```

El mensaje se clasificará como **soporte** y se enviará al canal `#support`.