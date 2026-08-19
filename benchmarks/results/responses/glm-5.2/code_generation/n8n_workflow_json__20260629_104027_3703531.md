# GLM 5.2 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.2`
- success: True  | final: 6.86 | quality: 8.32
- latency_total: 193.422s | tokens_per_second: 26.9
- input_tokens: 126 | output_tokens: 5198
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow para n8n. Este flujo recibe los datos por webhook, usa la IA de OpenAI para clasificar, enruta el mensaje según la categoría y envía la notificación a los respectivos canales de Slack accediendo a los datos originales del body.

Para que funcione correctamente, solo tendrás que importarlo en tu instancia de n8n y configurar tus credenciales de **OpenAI** y **Slack** en sus respectivos nodos.

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhookId": "webhook-clasificador-mensajes"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-3.5-turbo",
        "messages": {
          "messageValues": [
            {
              "content": "=Clasifica el siguiente mensaje en una sola palabra: 'soporte', 'ventas' u 'otro'. Devuelve únicamente esa palabra en minúsculas sin signos de puntuación.\n\nMensaje: {{$json.body.message}}"
            }
          ]
        }
      },
      "id": "openai-node",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.1,
      "position": [460, 300]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.toLowerCase() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "operation": "contains"
            },
            {
              "value2": "ventas",
              "operation": "contains"
            },
            {
              "value2": "otro",
              "operation": "contains"
            }
          ]
        },
        "fallbackOutput": 3
      },
      "id": "switch-node",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [680, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": "#support",
        "text": "=Nuevo mensaje de: {{ $('Webhook').item.json.body.email }}\n\nMensaje: {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack (Soporte)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [920, 140]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": "#sales",
        "text": "=Nuevo mensaje de: {{ $('Webhook').item.json.body.email }}\n\nMensaje: {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack (Ventas)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [920, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": "#general",
        "text": "=Nuevo mensaje de: {{ $('Webhook').item.json.body.email }}\n\nMensaje: {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack (General)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [920, 460]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
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
            "node": "Slack (Soporte)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (Ventas)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (General)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Notas sobre el Workflow:
1. **Webhook**: Se activa mediante una petición `POST` a la ruta `/clasificar-mensaje`.
2. **Extracción de Datos**: En los nodos de Slack, se accede directamente a los datos originales del body usando la expresión `{{ $('Webhook').item.json.body.email }}` y `{{ $('Webhook').item.json.body.message }}` para asegurar que la información no se pierda al pasar por el nodo de IA.
3. **OpenAI**: El prompt está configurado para devolver estrictamente una sola palabra. En el nodo *Switch*, se usa `.toLowerCase()` y el operador `contains` para evitar problemas si la IA responde con mayúsculas o espacios extra.
4. **Slack**: Utiliza el nombre de los canales (`#support`, `#sales`, `#general`). Si tu bot requiere los IDs de los canales en lugar de los nombres, simplemente cambia el valor en el campo `channelId` de cada nodo de Slack.