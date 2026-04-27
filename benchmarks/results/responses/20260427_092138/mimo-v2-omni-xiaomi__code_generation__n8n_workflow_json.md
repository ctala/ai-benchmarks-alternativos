# MiMo V2-Omni (Xiaomi direct) — code_generation/n8n_workflow_json

- model_id: `mimo-v2-omni`
- success: True  | final: 7.54 | quality: 8.12
- latency_total: 12.382s | tokens_per_second: 152.8
- input_tokens: 365 | output_tokens: 1892
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "name": "Email Classification Workflow",
  "nodes": [
    {
      "parameters": {},
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhook": "classify-email"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json[\"email\"]}}"
            },
            {
              "name": "message",
              "value": "={{$json[\"message\"]}}"
            }
          ]
        }
      },
      "id": "set-fields",
      "name": "Set Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "You are a helpful assistant that classifies customer emails into exactly one of these three categories: 'soporte', 'ventas', or 'otro'. Respond with ONLY the category name, nothing else."
          },
          {
            "role": "user",
            "content": "={{$json[\"message\"]}}"
          }
        ],
        "options": {
          "temperature": 0
        }
      },
      "id": "ai-classify",
      "name": "AI Classification",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value": "={{$json[\"choices\"][0][\"message\"][\"content\"]}}",
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "outputIndex": 0
            },
            {
              "value": "ventas",
              "outputIndex": 1
            },
            {
              "value": "otro",
              "outputIndex": 2
            }
          ]
        }
      },
      "id": "switch-classification",
      "name": "Switch by Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [900, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo email de soporte:\n\n**De:** {{$node[\"Set Fields\"].json[\"email\"]}}\n\n**Mensaje:**\n{{$node[\"Set Fields\"].json[\"message\"]}}"
      },
      "id": "slack-support",
      "name": "Slack - Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 140],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo email de ventas:\n\n**De:** {{$node[\"Set Fields\"].json[\"email\"]}}\n\n**Mensaje:**\n{{$node[\"Set Fields\"].json[\"message\"]}}"
      },
      "id": "slack-sales",
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo email (clasificación: otro):\n\n**De:** {{$node[\"Set Fields\"].json[\"email\"]}}\n\n**Mensaje:**\n{{$node[\"Set Fields\"].json[\"message\"]}}"
      },
      "id": "slack-general",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 460],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
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
            "node": "Set Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Fields": {
      "main": [
        [
          {
            "node": "AI Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Classification": {
      "main": [
        [
          {
            "node": "Switch by Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch by Classification": {
      "main": [
        [
          {
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

**Notas importantes para usar este workflow:**

1. **Reemplaza los IDs de credenciales:**
   - `YOUR_OPENAI_CREDENTIAL_ID`: Necesitas configurar una credencial de OpenAI en N8N
   - `YOUR_SLACK_CREDENTIAL_ID`: Necesitas configurar una credencial de Slack en N8N

2. **Cómo funciona:**
   - El webhook se activará con POST a: `http://tu-servidor-n8n/webhook/classify-email`
   - El body del POST debe ser JSON con los campos `email` y `message`
   - La IA clasificará el mensaje y el Switch redirigirá al canal de Slack correspondiente

3. **Ejemplo de body para probar:**
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Necesito ayuda con mi pedido #12345, no ha llegado todavía."
}
```

4. **Asegúrate de que:**
   - Los canales de Slack (`#support`, `#sales`, `#general`) existan en tu workspace
   - La app de Slack tenga permisos para enviar mensajes a estos canales
   - El modelo de OpenAI tenga el prompt ajustado según tus necesidades específicas