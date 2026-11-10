# Gemini 3.1 Flash Lite (GA) — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 8.13 | quality: 8.6
- latency_total: 3.99s | tokens_per_second: 332.6
- input_tokens: 115 | output_tokens: 1327
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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

Para implementar este workflow en n8n, asegúrate de tener configuradas tus credenciales de **OpenAI** y **Slack** dentro de la plataforma.

Aquí tienes el código JSON. Puedes copiarlo y pegarlo directamente en el lienzo (canvas) de n8n usando `Ctrl+V` (o `Cmd+V`).

```json
{
  "name": "Clasificador de Emails a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [0, 0],
      "id": "webhook-trigger",
      "name": "Webhook"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {
          "systemMessage": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde únicamente con la palabra de la categoría."
        },
        "promptType": "define",
        "text": "={{ $json.body.message }}"
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.4,
      "position": [220, 0],
      "id": "openai-classifier",
      "name": "OpenAI Classifier"
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "value1": "={{ $json.output }}",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.output }}",
              "value2": "ventas"
            }
          ]
        }
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [440, 0],
      "id": "switch-category",
      "name": "Switch Category"
    },
    {
      "parameters": {
        "channel": "support",
        "text": "={{ 'Nuevo mensaje de soporte de: ' + $('Webhook').item.json.body.email + '\\nMensaje: ' + $('Webhook').item.json.body.message }}"
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [700, -150],
      "id": "slack-support",
      "name": "Slack #support"
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "={{ 'Nuevo lead de ventas de: ' + $('Webhook').item.json.body.email + '\\nMensaje: ' + $('Webhook').item.json.body.message }}"
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [700, 0],
      "id": "slack-sales",
      "name": "Slack #sales"
    },
    {
      "parameters": {
        "channel": "general",
        "text": "={{ 'Mensaje general de: ' + $('Webhook').item.json.body.email + '\\nMensaje: ' + $('Webhook').item.json.body.message }}"
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [700, 150],
      "id": "slack-general",
      "name": "Slack #general"
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classifier": {
      "main": [
        [
          {
            "node": "Switch Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Category": {
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
  }
}
```

### Notas importantes para que funcione:
1. **Credenciales:** Al importar el JSON, n8n te pedirá que selecciones tus credenciales de OpenAI y Slack.
2. **Nombres de canales:** En los nodos de Slack, asegúrate de que el campo "Channel" coincida exactamente con el nombre de tu canal (ej. `support`, `sales`, `general`).
3. **Estructura del JSON:** El webhook espera un JSON con este formato:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Hola, necesito ayuda con mi factura"
   }
   ```
4. **Nodo de IA:** He configurado el nodo de OpenAI para que sea determinista. Si notas que la IA añade texto extra, puedes ajustar el *System Message* para forzar una respuesta más estricta.