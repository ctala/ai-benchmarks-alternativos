# Grok 4.7 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.7`
- success: True  | final: 4.86 | quality: 5.2
- latency_total: 51.076s | tokens_per_second: 85.9
- input_tokens: 1355 | output_tokens: 4386
- judge_score: 2.0 | justificación: El JSON tiene errores en la configuración de los nodos, como el uso incorrecto del nodo de clasificación de texto y la falta de lógica para enviar mensajes a diferentes canales de Slack basados en la clasificación.

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

Workflow listo para importar en n8n (menú del workflow → Import from File, o pegar el JSON). Tras importarlo, asigna las credenciales de OpenAI y Slack en los nodos correspondientes.

```json
{
  "name": "Clasificar mensaje y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 300],
      "webhookId": "classify-message"
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email || $json.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message || $json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [260, 300]
    },
    {
      "parameters": {
        "inputText": "={{ $json.message }}",
        "categories": {
          "categories": [
            {
              "category": "soporte",
              "description": "Problemas técnicos, incidencias, errores, ayuda con el producto o solicitudes de soporte."
            },
            {
              "category": "ventas",
              "description": "Interés comercial, precios, demos, compras, contrataciones o consultas de ventas."
            },
            {
              "category": "otro",
              "description": "Cualquier mensaje que no sea claramente de soporte ni de ventas."
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar mensaje",
      "type": "@n8n/n8n-nodes-langchain.textClassifier",
      "typeVersion": 1,
      "position": [520, 300]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [520, 540]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "support",
          "mode": "name"
        },
        "text": "=Nuevo mensaje de *soporte*\nEmail: {{ $('Extraer email y message').item.json.email }}\nMensaje: {{ $('Extraer email y message').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [860, 120]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "sales",
          "mode": "name"
        },
        "text": "=Nuevo mensaje de *ventas*\nEmail: {{ $('Extraer email y message').item.json.email }}\nMensaje: {{ $('Extraer email y message').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [860, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "general",
          "mode": "name"
        },
        "text": "=Nuevo mensaje (*otro*)\nEmail: {{ $('Extraer email y message').item.json.email }}\nMensaje: {{ $('Extraer email y message').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [860, 480]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
      "main": [
        [
          {
            "node": "Clasificar mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Clasificar mensaje",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar mensaje": {
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
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```

El clasificador tiene tres salidas, en este orden: `soporte` → `#support`, `ventas` → `#sales`, `otro` → `#general`.

Ejemplo de body:

```json
{
  "email": "ana@example.com",
  "message": "No puedo iniciar sesión en la app"
}
```

Antes de activarlo: el bot de Slack debe estar en esos canales, y si el selector por nombre falla, cambia cada canal a su ID (`C...`). Activa el workflow y usa la URL de producción del webhook.