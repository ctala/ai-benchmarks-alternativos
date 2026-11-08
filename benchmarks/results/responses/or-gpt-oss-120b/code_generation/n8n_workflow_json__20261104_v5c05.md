# GPT-OSS 120B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.55 | quality: 8.12
- latency_total: 68.378s | tokens_per_second: 39.9
- input_tokens: 166 | output_tokens: 2726
- judge_score: 3.8 | justificación: 

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

Aquí tienes el workflow completo en formato **JSON** para n8n.  
Cumple con los requisitos:

1. Se activa con un **Webhook POST**.  
2. Extrae los campos **email** y **message** del body.  
3. Usa el nodo **OpenAI** para clasificar el mensaje como **“soporte”, “ventas” o “otro”**.  
4. Según la clasificación envía el mensaje a un **canal de Slack** diferente.

```json
{
  "name": "Email to Slack Router",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "email",
        "responseMode": "onReceived"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "PLACEHOLDER_WEBHOOK_ID"
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
        },
        "options": {}
      },
      "name": "Set Extract",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Eres un clasificador de mensajes. Responde solo con una palabra: 'soporte', 'ventas' o 'otro'."
          },
          {
            "role": "user",
            "content": "Clasifica el siguiente mensaje:\n\n{{ $json[\"message\"] }}"
          }
        ],
        "options": {}
      },
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "classification",
              "value": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        1000,
        300
      ]
    },
    {
      "parameters": {
        "value": "={{$json[\"classification\"]}}",
        "rules": [
          {
            "value": "soporte",
            "output": 0
          },
          {
            "value": "ventas",
            "output": 1
          },
          {
            "value": "otro",
            "output": 2
          }
        ]
      },
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 *Nuevo mensaje de soporte*\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1500,
        150
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📩 *Nuevo mensaje de ventas*\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1500,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📩 *Nuevo mensaje general*\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1500,
        450
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set Extract",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Extract": {
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
            "node": "Set Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Classification": {
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
  "settings": {}
}
```

**Cómo usarlo**

1. Copia todo el JSON anterior.  
2. En n8n ve a **Workflows → Import** y pega el contenido.  
3. Reemplaza `PLACEHOLDER_WEBHOOK_ID` por el ID que n8n genere automáticamente (puedes volver a guardar el workflow y el ID se completará).  
4. Configura las credenciales de **OpenAI** y **Slack** en n8n.  
5. Activa el workflow y envía un `POST` al endpoint `{{your-n8n-domain}}/webhook/email` con un cuerpo JSON que incluya los campos `email` y `message`.

¡Listo! El mensaje será clasificado y enviado al canal de Slack correspondiente. 🚀