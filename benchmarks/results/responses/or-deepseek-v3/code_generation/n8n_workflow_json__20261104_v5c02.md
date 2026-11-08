# DeepSeek V3 — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 6.47 | quality: 6.72
- latency_total: 50.14s | tokens_per_second: 39.6
- input_tokens: 126 | output_tokens: 1985
- judge_score: 2.8 | justificación: 

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

```json
{
  "name": "Clasificación de mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {},
      "id": "start",
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "path": "webhook",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [450, 300],
      "webhookId": "clasificador-mensajes"
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "respondToWebhook",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "jsCode": "// Extraer email y message del body\nconst { email, message } = $input.first().json.body;\n\nif (!email) {\n  throw new Error('Email no encontrado en el body');\n}\n\nif (!message) {\n  throw new Error('Mensaje no encontrado en el body');\n}\n\nreturn [\n  {\n    json: {\n      email,\n      message,\n      timestamp: new Date().toISOString()\n    }\n  }\n];"
      },
      "id": "extractData",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [650, 300]
    },
    {
      "parameters": {
        "options": {},
        "text": "={{ $json.message }}\n\nClasifica este mensaje en exactamente una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde solo con la categoría, sin explicaciones ni texto adicional."
      },
      "id": "openai",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [850, 200],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIALS_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "create",
        "channel": "={{ $json.classification === 'soporte' ? '#support' : $json.classification === 'ventas' ? '#sales' : '#general' }}",
        "text": "Nuevo mensaje recibido:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json.classification }}\n*Timestamp:* {{ $json.timestamp }}",
        "options": {}
      },
      "id": "slack",
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "setClassification",
      "name": "Asignar clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [1050, 200],
      "webhookId": "clasificador-mensajes"
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        },
        "options": {}
      },
      "id": "ifSoporte",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [1250, 150]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        },
        "options": {}
      },
      "id": "ifVentas",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [1250, 250]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equals",
              "value2": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "ifOtro",
      "name": "¿Es otro?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [1250, 350]
    }
  ],
  "connections": {
    "Start": {
      "main": [
        [
          {
            "node": "Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer datos": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          },
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Asignar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Asignar clasificación": {
      "main": [
        [
          {
            "node": "Enviar a Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enviar a Slack": {
      "main": [
        [
          {
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es otro?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "pinData": {},
  "versionId": "1",
  "triggerCount": 1
}
```

**Notas importantes:**

1. **Credenciales**: Necesitarás configurar las credenciales para:
   - OpenAI API (en el nodo "Clasificar con OpenAI")
   - Slack API (en el nodo "Enviar a Slack")

2. **Configuración del webhook**:
   - El webhook se activa en la ruta `/webhook/clasificador-mensajes`
   - Acepta solicitudes POST
   - Debes exponer tu instancia de n8n para recibir webhooks externos

3. **Estructura del body esperado**:
   ```json
   {
     "email": "usuario@ejemplo.com",
     "message": "Mi mensaje aquí"
   }
   ```

4. **Canales de Slack**: Asegúrate de que existan los canales `#support`, `#sales` y `#general` en tu workspace de Slack.

5. **Respuesta del webhook**: El workflow responde inmediatamente después de recibir el webhook, mientras el procesamiento continúa en segundo plano.

Para importar este workflow en n8n:
1. Copia el JSON completo
2. Ve a n8n → Workflows → "Import from URL"
3. Pega el JSON en la opción de importar desde texto
4. Configura las credenciales necesarias
5. Activa el workflow