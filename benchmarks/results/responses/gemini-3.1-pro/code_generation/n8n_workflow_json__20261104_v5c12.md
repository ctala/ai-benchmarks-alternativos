# Gemini 3.1 Pro — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 7.25 | quality: 8.6
- latency_total: 47.117s | tokens_per_second: 100.8
- input_tokens: 115 | output_tokens: 4748
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del flujo de trabajo. La estructura es clara y organizada, facilitando la implementación. Aunque la profundidad es adecuada, podría incluir más detalles sobre la configuración de los nodos o manejo de errores para mejorar la utilidad práctica.

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

Aquí tienes el workflow de n8n en formato JSON. 

Este flujo hace exactamente lo que pides: recibe el webhook, usa OpenAI para clasificar el texto (asegurándose de limpiar la respuesta para evitar errores por mayúsculas o espacios), lo pasa por un nodo *Switch* y finalmente lo envía al canal de Slack correspondiente.

### Cómo importarlo en n8n:
1. Copia todo el bloque de código JSON a continuación.
2. Abre tu instancia de n8n.
3. Ve a un workflow nuevo y presiona `Ctrl + V` (o `Cmd + V` en Mac) directamente sobre el lienzo (canvas).

```json
{
  "name": "Clasificador de Tickets con IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-ticket",
        "options": {}
      },
      "id": "e1a9c3b2-7d4f-4b1a-8c9e-1234567890ab",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        180,
        240
      ],
      "webhookId": "clasificador-ia-webhook"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-3.5-turbo",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un asistente de clasificación. Tu único objetivo es leer el mensaje del usuario y clasificarlo en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con la palabra exacta de la categoría en minúsculas. No agregues puntos, comillas ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "f2b8d4c3-8e5g-5c2b-9d0f-2345678901bc",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        400,
        240
      ]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.toLowerCase().trim() }}",
        "rules": {
          "rules": [
            {
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "operation": "equal",
              "value2": "ventas"
            },
            {
              "operation": "equal",
              "value2": "otro"
            }
          ]
        }
      },
      "id": "a3c9e5d4-9f6h-6d3c-0e1g-3456789012cd",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        620,
        240
      ]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "=🛠️ *Nuevo mensaje de Soporte*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "b4d0f6e5-0g7i-7e4d-1f2h-4567890123de",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        880,
        60
      ]
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "=💰 *Nuevo mensaje de Ventas*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "c5e1g7f6-1h8j-8f5e-2g3i-5678901234ef",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        880,
        240
      ]
    },
    {
      "parameters": {
        "channel": "general",
        "text": "=📫 *Nuevo mensaje (Otro)*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "d6f2h8g7-2i9k-9g6f-3h4j-6789012345fg",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        880,
        420
      ]
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
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1"
}
```

### ⚙️ Pasos adicionales tras importar:
1. **Credenciales:** Tendrás que abrir el nodo de **OpenAI** y los nodos de **Slack** para seleccionar o crear tus credenciales (API Key de OpenAI y Token de Slack).
2. **Prueba del Webhook:** Para probarlo, envía una petición POST a la URL de prueba del Webhook con este formato JSON en el Body:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Hola, mi tarjeta de crédito fue rechazada al intentar comprar el plan premium."
   }
   ```
3. **Variables:** Notarás que en los nodos de Slack uso la expresión `{{ $('Webhook').item.json.body.email }}`. Esto es una función nativa de n8n que permite "recordar" los datos del nodo inicial (Webhook) aunque el nodo anterior inmediato haya sido el de OpenAI.