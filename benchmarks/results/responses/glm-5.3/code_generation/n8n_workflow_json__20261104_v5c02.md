# GLM 5.3 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.01 | quality: 7.2
- latency_total: 270.111s | tokens_per_second: 85.8
- input_tokens: 126 | output_tokens: 23188
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

Aquí tienes el workflow completo. Cópialo e impórtalo en n8n (**Workflow → Import from Clipboard**):

```json
{
  "name": "Clasificador de mensajes IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "9f8b1c2d-3e4f-4a5b-8c6d-1a2b3c4d5e6f",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-560, -20],
      "webhookId": "7c8d9e0f-1a2b-4c3d-9e0f-6a7b8c9d0e1f"
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "1a2b3c4d-0001-4a01-9b01-aaaaaaaaaaaa",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "1a2b3c4d-0002-4a02-9b02-bbbbbbbbbbbb",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "8a7b6c5d-4e3f-4b2a-9c1d-2b3c4d5e6f7a",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [-340, -20]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes entrantes para una empresa. Clasifica cada mensaje del usuario en EXACTAMENTE una de estas tres categorías:\n- soporte: problemas técnicos, errores, bugs, incidencias o dudas sobre el uso del producto.\n- ventas: interés en comprar, precios, planes, descuentos, demos o información comercial.\n- otro: cualquier otro tipo de mensaje (agradecimientos, spam, consultas generales, etc.).\n\nResponde ÚNICAMENTE con una de estas tres palabras en minúsculas y sin puntuación: soporte, ventas u otro.\nNo añadas explicaciones, comillas ni puntos finales.",
              "role": "system"
            },
            {
              "content": "=Email del remitente: {{ $json.email }}\n\nMensaje a clasificar:\n\"\"\"\n{{ $json.message }}\n\"\"\"",
              "role": "user"
            }
          ]
        },
        "options": {}
      },
      "id": "7b6c5d4e-3f2a-4c1b-8d0c-3c4d5e6f7a8b",
      "name": "Clasificar mensaje (OpenAI)",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [-120, -20]
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "2b3c4d5e-0003-4a03-9b03-cccccccccccc",
              "name": "email",
              "value": "={{ $('Extraer campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "2b3c4d5e-0004-4a04-9b04-dddddddddddd",
              "name": "message",
              "value": "={{ $('Extraer campos').item.json.message }}",
              "type": "string"
            },
            {
              "id": "2b3c4d5e-0005-4a05-9b05-eeeeeeeeeeee",
              "name": "category",
              "value": "={{ (($json.message && $json.message.content) || $json.output || $json.text || '').trim().toLowerCase() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "6c5d4e3f-2a1b-4d0c-9e2d-4d5e6f7a8b9c",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [100, -20]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "3c4d5e6f-0006-4a06-9b06-ffffffffffff",
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "4d5e6f7a-0007-4a07-9b07-121212121212",
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "5e6f7a8b-0008-4a08-9b08-232323232323",
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "5d4e3f2a-1b0c-4c2d-8f3e-5e6f7a8b9c0d",
      "name": "Enrutar por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [320, -20]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:rotating_light: *Nuevo mensaje de SOPORTE*\n\n:email: *Email:* {{ $json.email }}\n:label: *Clasificación:* {{ $json.category }}\n\n:memo: *Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "4e3f2a1b-0c9d-4d3e-8a4f-6f7a8b9c0d1e",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [580, -240]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n\n:email: *Email:* {{ $json.email }}\n:label: *Clasificación:* {{ $json.category }}\n\n:memo: *Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "3f2a1b0c-9d8e-4e4f-8b5a-7a8b9c0d1e2f",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [580, -20]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:speech_balloon: *Nuevo mensaje clasificado como OTRO*\n\n:email: *Email:* {{ $json.email }}\n:label: *Clasificación:* {{ $json.category }}\n\n:memo: *Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "2a1b0c9d-8e7f-4f5a-8c6b-8b9c0d1e2f3a",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [580, 200]
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [[{ "node": "Extraer campos", "type": "main", "index": 0 }]]
    },
    "Extraer campos": {
      "main": [[{ "node": "Clasificar mensaje (OpenAI)", "type": "main", "index": 0 }]]
    },
    "Clasificar mensaje (OpenAI)": {
      "main": [[{ "node": "Normalizar clasificación", "type": "main", "index": 0 }]]
    },
    "Normalizar clasificación": {
      "main": [[{ "node": "Enrutar por categoría", "type": "main", "index": 0 }]]
    },
    "Enrutar por categoría": {
      "main": [
        [{ "node": "Slack #support", "type": "main", "index": 0 }],
        [{ "node": "Slack #sales", "type": "main", "index": 0 }],
        [{ "node": "Slack #general", "type": "main", "index": 0 }],
        [{ "node": "Slack #general", "type": "main", "index": 0 }]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "active": false,
  "tags": []
}
```

## Notas de configuración

1. **Credenciales**: al importar, asigna tus credenciales en el nodo de OpenAI (API key) y en los 3 nodos de Slack (bot token con scope `chat:write`). El bot debe ser miembro de los canales `#support`, `#sales` y `#general` (o reemplaza los nombres por los IDs de canal).

2. **Flujo**: `Webhook POST` → `Extraer campos` (email/message del body) → `OpenAI` (clasifica con prompt estricto) → `Normalizar` (minúsculas + fallback por si cambia el formato de salida del nodo) → `Switch` → Slack según categoría.

3. **Robustez**: el Switch usa `contains` (tolera "Soporte.", "es soporte", etc.) y tiene una salida *fallback* extra conectada también a `#general`, así ningún mensaje se pierde aunque el modelo devuelva algo inesperado.

4. **Prueba**:
```bash
curl -X POST https://TU-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email": "cliente@ejemplo.com", "message": "No puedo iniciar sesión en mi cuenta"}'
```

5. **Si tu versión de n8n es antigua** y el nodo OpenAI retorna el texto en otro campo (p. ej. `$json.text` en vez de `$json.message.content`), la expresión del nodo "Normalizar clasificación" ya contempla ambos formatos, así que no deberías necesitar cambios.