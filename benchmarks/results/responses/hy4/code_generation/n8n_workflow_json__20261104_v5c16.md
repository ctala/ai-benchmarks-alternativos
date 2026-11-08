# Tencent Hy4 — code_generation/n8n_workflow_json

- model_id: `tencent/hy4`
- success: True  | final: 7.6 | quality: 8.6
- latency_total: 64.491s | tokens_per_second: 120.0
- input_tokens: 143 | output_tokens: 7738
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack o la gestión de errores.

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

Aquí tienes el workflow completo, listo para copiar y pegar en n8n (**Import from File / Clipboard**). 

Está diseñado con nodos modernos (LangChain OpenAI + Switch v3) e incluye un pequeño nodo de normalización para blindar la respuesta de la IA y evitar fallos de enrutamiento.

```json
{
  "name": "Clasificador IA → Slack (Webhook)",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "responseData": "{\"status\":\"ok\"}",
        "options": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000001",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000002",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 0]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador estricto. Lee el mensaje y responde ÚNICAMENTE con una de estas tres palabras exactas: soporte, ventas, otro. Sin mayúsculas, sin puntuación y sin explicaciones. Ejemplos: 'no funciona mi cuenta' -> soporte | 'quiero contratar el plan pro' -> ventas | 'hola buenos días' -> otro."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000003",
      "name": "OpenAI (Clasificar)",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 0],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f3",
              "name": "categoria",
              "value": "={{ ($json.output?.content || $json.content || $json.text || 'otro').toString().trim().toLowerCase() }}",
              "type": "string"
            },
            {
              "id": "f4",
              "name": "email",
              "value": "={{ $('Extraer email y message').item.json.email }}",
              "type": "string"
            },
            {
              "id": "f5",
              "name": "message",
              "value": "={{ $('Extraer email y message').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000004",
      "name": "Normalizar respuesta IA",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [660, 0]
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": [
          {
            "conditions": {
              "options": { "caseSensitive": true, "typeValidation": "strict", "version": 2 },
              "combinator": "and",
              "conditions": [
                {
                  "leftValue": "={{ $json.categoria }}",
                  "rightValue": "soporte",
                  "operator": { "type": "string", "operation": "equals" }
                }
              ]
            },
            "renameOutput": true,
            "outputKey": "Soporte"
          },
          {
            "conditions": {
              "options": { "caseSensitive": true, "typeValidation": "strict", "version": 2 },
              "combinator": "and",
              "conditions": [
                {
                  "leftValue": "={{ $json.categoria }}",
                  "rightValue": "ventas",
                  "operator": { "type": "string", "operation": "equals" }
                }
              ]
            },
            "renameOutput": true,
            "outputKey": "Ventas"
          },
          {
            "conditions": {
              "options": { "caseSensitive": true, "typeValidation": "strict", "version": 2 },
              "combinator": "and",
              "conditions": [
                {
                  "leftValue": "={{ $json.categoria }}",
                  "rightValue": "otro",
                  "operator": { "type": "string", "operation": "equals" }
                }
              ]
            },
            "renameOutput": true,
            "outputKey": "Otro"
          }
        ],
        "options": {
          "fallbackOutput": 2
        }
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000005",
      "name": "Switch por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": { "__rl": true, "value": "#support", "mode": "name" },
        "text": "={{ '🛠️ *Soporte*\\n📧 Email: ' + $json.email + '\\n💬 Mensaje: ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, -200],
      "credentials": {
        "slackApi": { "id": "REEMPLAZAR_ID_SLACK", "name": "Slack account" }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": { "__rl": true, "value": "#sales", "mode": "name" },
        "text": "={{ '💼 *Ventas*\\n📧 Email: ' + $json.email + '\\n💬 Mensaje: ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 0],
      "credentials": {
        "slackApi": { "id": "REEMPLAZAR_ID_SLACK", "name": "Slack account" }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": { "__rl": true, "value": "#general", "mode": "name" },
        "text": "={{ '📥 *Otro / General*\\n📧 Email: ' + $json.email + '\\n💬 Mensaje: ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 200],
      "credentials": {
        "slackApi": { "id": "REEMPLAZAR_ID_SLACK", "name": "Slack account" }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [[{ "node": "Extraer email y message", "type": "main", "index": 0 }]]
    },
    "Extraer email y message": {
      "main": [[{ "node": "OpenAI (Clasificar)", "type": "main", "index": 0 }]]
    },
    "OpenAI (Clasificar)": {
      "main": [[{ "node": "Normalizar respuesta IA", "type": "main", "index": 0 }]]
    },
    "Normalizar respuesta IA": {
      "main": [[{ "node": "Switch por categoría", "type": "main", "index": 0 }]]
    },
    "Switch por categoría": {
      "main": [
        [{ "node": "Slack #support", "type": "main", "index": 0 }],
        [{ "node": "Slack #sales", "type": "main", "index": 0 }],
        [{ "node": "Slack #general", "type": "main", "index": 0 }]
      ]
    }
  },
  "active": false,
  "settings": { "executionOrder": "v1" },
  "pinData": {}
}
```

### 📌 Notas para dejarlo funcionando:

1. **Credenciales:** Al importar, n8n te pedirá que selecciones tu credencial de **OpenAI** y la de **Slack** en los nodos correspondientes (los IDs `REEMPLAZAR_...` son marcadores de posición). Asegúrate de que el bot de Slack tenga permiso `chat:write` y esté invitado a los 3 canales.
2. **Webhook:** Configuré `responseMode: "onReceived"` para que responda `{"status":"ok"}` al instante y procese la IA en segundo plano. Así evitas *timeouts* del cliente que hace el POST.
3. **Blindaje:** El nodo *"Normalizar respuesta IA"* limpia la salida (minúsculas + `trim`) y recupera el `email`/`message` originales. Además, el `Switch` tiene `fallbackOutput: 2`, por si la IA alucina algo distinto, el mensaje acabará en `#general` en lugar de perderse.

**Prueba rápida:**
```bash
curl -X POST https://TU-N8N/webhook-test/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@acme.com","message":"Quiero contratar el plan enterprise, ¿me llamáis?"}'
```