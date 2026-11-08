# MiniMax M2.5 — code_generation/n8n_workflow_json

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.79 | quality: 8.6
- latency_total: 24.056s | tokens_per_second: 137.6
- input_tokens: 154 | output_tokens: 3309
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo que cumple con los requisitos del workflow de N8N. La estructura es clara y organizada, lo que la hace útil para un emprendedor. Sin embargo, la profundidad podría mejorarse con más detalles sobre la configuración o posibles errores.

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

Aquí tienes el JSON completo del workflow. Para usarlo, sigue estos pasos:

1.  Copia el código de abajo.
2.  En tu instancia de N8N, ve a **Workflows** -> **Import from File** (o pega el JSON en el editor de código).
3.  **Importante:** Necesitarás configurar las credenciales para **Slack** y **OpenAI** en los nodos correspondientes, ya que el JSON solo guarda la referencia, no las claves privadas.

```json
{
  "name": "Clasificador de Mensajes Webhook + AI + Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "clasificador"
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "complete",
        "model": "gpt-3.5-turbo",
        "prompt": "Clasifica el siguiente mensaje en una sola palabra en minúsculas: \"soporte\", \"ventas\" u \"otro\". \n\nMensaje: {{ $json.message }}\n\nResponde únicamente con la palabra de clasificación.",
        "options": {
          "maxTokens": 50,
          "temperature": 0
        }
      },
      "id": "ai-classify",
      "name": "Clasificar con IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "openAiApi": "openai_creds"
      }
    },
    {
      "parameters": {
        "data1": "={{ $json.text }}",
        "rules": {
          "rules": [
            {
              "value1": "soporte",
              "operation": "equal",
              "value2": ""
            },
            {
              "value1": "ventas",
              "operation": "equal",
              "value2": ""
            },
            {
              "value1": "otro",
              "operation": "equal",
              "value2": ""
            }
          ]
        },
        "fallbackRoute": 2
      },
      "id": "switch-routing",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [650, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo ticket de *Soporte*:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 3,
      "position": [850, 150],
      "credentials": {
        "slackApi": "slack_creds"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo lead de *Ventas*:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 3,
      "position": [850, 300],
      "credentials": {
        "slackApi": "slack_creds"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje *General*:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 3,
      "position": [850, 450],
      "credentials": {
        "slackApi": "slack_creds"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
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
  "active": false,
  "settings": {},
  "id": "workflow-clasificador"
}
```

### Explicación del flujo:

1.  **Webhook:** Quedará a la espera de una llamada POST. Se espera que el cuerpo (body) del JSON enviado contenga los campos `email` y `message`.
2.  **Clasificar con IA (OpenAI):** Envía el texto recibido a GPT. Le pide que devuelva una sola palabra ("soporte", "ventas" u "otro") en minúsculas para facilitar la comparación.
3.  **Route by Category (Switch):** Lee la respuesta de la IA. Dependiendo de si la respuesta es "soporte", "ventas" u "otro", enruta el flujo por una rama diferente.
4.  **Nodos Slack:** Hay 3 nodos de Slack. Cada uno está conectado a una salida diferente del Switch y envía el mensaje al canal correspondiente (#support, #sales o #general).

### Cómo probarlo:

Una vez importado el workflow y configuradas las credenciales, activa el workflow. Luego, usa Postman o cURL para enviar datos:

```bash
curl -X POST https://tu-url-de-n8n/webhook/clasificar-mensaje \
   -H "Content-Type: application/json" \
   -d '{"email": "cliente@ejemplo.com", "message": "Tengo un problema con mi servidor"}'
```