# Gemini 3.8 Flash — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 6.56 | quality: 7.2
- latency_total: 22.076s | tokens_per_second: 158.9
- input_tokens: 115 | output_tokens: 3509
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

Aquí tienes el JSON completo del workflow listo para importar directamente en n8n (puedes copiar el código y pegarlo directamente sobre el lienzo de n8n con `Ctrl + V` o `Cmd + V`).

### JSON del Workflow

```json
{
  "name": "Clasificador de Mensajes con OpenAI y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-message",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "id": "webhook-trigger",
      "name": "Webhook"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu tarea es responder ÚNICAMENTE con una de las siguientes tres palabras exactas: 'soporte', 'ventas' u 'otro'. No agregues puntuación, explicaciones ni formato adicional."
            },
            {
              "role": "user",
              "content": "=Clasifica el siguiente mensaje:\n{{ $json.body.message }}"
            }
          ]
        }
      },
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.4,
      "position": [460, 300],
      "id": "openai-classifier",
      "name": "OpenAI - Clasificar",
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_DE_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.toLowerCase().trim() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "output": 0
            },
            {
              "value2": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": 2
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [680, 300],
      "id": "switch-routing",
      "name": "Switch por Categoría"
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo ticket de Soporte*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [940, 160],
      "id": "slack-support",
      "name": "Slack (#support)",
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nueva oportunidad de Ventas*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [940, 300],
      "id": "slack-sales",
      "name": "Slack (#sales)",
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📩 *Nuevo mensaje general (Otro)*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [940, 440],
      "id": "slack-general",
      "name": "Slack (#general)",
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI - Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificar": {
      "main": [
        [
          {
            "node": "Switch por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por Categoría": {
      "main": [
        [
          {
            "node": "Slack (#support)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#sales)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#general)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

---

### Pasos para configurarlo:

1. **Importar**: En n8n, pulsa `Ctrl + V` (o ve al menú superior de tres puntos `...` -> **Import from clipboard**).
2. **Credenciales**:
   - Asigna tu credencial de **OpenAI** al nodo `OpenAI - Clasificar`.
   - Asigna tu credencial de **Slack** a los tres nodos de Slack.
3. **Probar el Webhook**:
   Envía una petición POST al endpoint de prueba que te da el nodo Webhook:
   ```bash
   curl -X POST "https://TU-INSTANCIA-N8N/webhook-test/incoming-message" \
     -H "Content-Type: application/json" \
     -d '{
       "email": "cliente@example.com",
       "message": "Hola, el sistema no me deja iniciar sesión y da error 500."
     }'
   ```