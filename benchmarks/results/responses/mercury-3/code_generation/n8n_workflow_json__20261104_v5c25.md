# Mercury 3 — code_generation/n8n_workflow_json

- model_id: `inception/mercury-3`
- success: True  | final: 7.0 | quality: 7.2
- latency_total: 6.58s | tokens_per_second: 869.2
- input_tokens: 116 | output_tokens: 5719
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

Aquí tienes el workflow completo de n8n en JSON. Incluye un webhook POST, extracción de `email` y `message`, clasificación con OpenAI y envío a Slack según la categoría.

```json
{
  "name": "Classify and Route to Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-uuid",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "webhook-id"
    },
    {
      "parameters": {
        "mode": "manual",
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-uuid",
      "name": "Extract Email and Message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [140, 0]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "You are a classifier. Given a customer message and their email, classify the message into one of these categories: 'soporte', 'ventas', or 'otro'. Respond with only one word: soporte, ventas, or otro."
            },
            {
              "role": "user",
              "content": "Email: {{ $json.email }}\nMessage: {{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-uuid",
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2,
      "position": [280, 0],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "dataPropertyName": "output",
        "rules": {
          "values": [
            {
              "condition": {
                "leftValue": "={{ $json.output }}",
                "rightValue": "soporte",
                "operator": "equals"
              },
              "output": 0
            },
            {
              "condition": {
                "leftValue": "={{ $json.output }}",
                "rightValue": "ventas",
                "operator": "equals"
              },
              "output": 1
            }
          ]
        },
        "options": {}
      },
      "id": "switch-uuid",
      "name": "Route by Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [420, 0]
    },
    {
      "parameters": {
        "operation": "message",
        "channel": "#support",
        "text": "New support request from {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-support-uuid",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [560, -120],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "operation": "message",
        "channel": "#sales",
        "text": "New sales inquiry from {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales-uuid",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [560, 120],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "operation": "message",
        "channel": "#general",
        "text": "New message from {{ $json.email }}:\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general-uuid",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [560, 240],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
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
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Route by Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Classification": {
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
  "settings": {
    "executionOrder": "v1"
  },
  "active": false,
  "tags": [],
  "pinData": {},
  "versionId": "1",
  "meta": {}
}
```

### Cómo usarlo
1. **Importa el JSON** en n8n (New Workflow → ⋯ → Import from File).
2. **Configura las credenciales**:
   - Reemplaza `YOUR_OPENAI_CREDENTIAL_ID` por tu credencial real de OpenAI.
   - Reemplaza `YOUR_SLACK_CREDENTIAL_ID` por tu credencial real de Slack.
3. **Ajusta los canales** si tus canales tienen otros nombres.
4. **Activa el workflow** y usa la URL del webhook (aparece al hacer clic en el nodo Webhook) para enviar un POST con un body como:
   ```json
   {
     "email": "cliente@example.com",
     "message": "Necesito ayuda con mi pedido"
   }
   ```

### Flujo
- **Webhook** recibe el POST.
- **Set** extrae `email` y `message`.
- **OpenAI** clasifica el mensaje devolviendo `soporte`, `ventas` o `otro`.
- **Switch** enruta a la rama correspondiente.
- **Slack** envía el mensaje al canal adecuado (`#support`, `#sales` o `#general`).