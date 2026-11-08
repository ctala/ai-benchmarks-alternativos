# Step 3.5 Flash — code_generation/n8n_workflow_json

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.55 | quality: 8.4
- latency_total: 103.271s | tokens_per_second: 93.4
- input_tokens: 134 | output_tokens: 9648
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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
  "name": "Workflow Clasificación de Mensajes",
  "nodes": [
    {
      "parameters": {
        "path": "/webhook",
        "httpMethod": "POST",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "values": {
          "json": {
            "email": "={{ $json.body.email }}",
            "message": "={{ $json.body.message }}"
          }
        },
        "options": {}
      },
      "id": "extractData",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [460, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "user",
              "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Mensaje: {{ $json.message }}. Responde solo con la categoría."
            }
          ]
        },
        "options": {},
        "combineInputData": true
      },
      "id": "openai",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [680, 300],
      "credentials": {
        "openAiApi": "OpenAI API"
      }
    },
    {
      "parameters": {
        "values": {
          "json": {
            "classification": "={{ $json.choices[0].message.content.toLowerCase().trim() }}"
          }
        },
        "options": {}
      },
      "id": "normalize",
      "name": "Normalizar Clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [820, 300]
    },
    {
      "parameters": {
        "property": "={{ $json.classification }}",
        "cases": [
          {
            "value": "soporte"
          },
          {
            "value": "ventas"
          },
          {
            "value": "otro"
          }
        ],
        "options": {}
      },
      "id": "switch",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [980, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "value": "#support",
          "type": "string"
        },
        "text": "={{ 'Nuevo mensaje de ' + $json.email + ': ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "slackSupport",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1140, 200],
      "credentials": {
        "slackApi": "Slack API"
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "value": "#sales",
          "type": "string"
        },
        "text": "={{ 'Nuevo mensaje de ' + $json.email + ': ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "slackSales",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1140, 300],
      "credentials": {
        "slackApi": "Slack API"
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "value": "#general",
          "type": "string"
        },
        "text": "={{ 'Nuevo mensaje de ' + $json.email + ': ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "slackGeneral",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1140, 400],
      "credentials": {
        "slackApi": "Slack API"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
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
            "node": "Normalizar Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Clasificación": {
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
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
  "triggerCount": 0,
  "updatedAt": "2023-10-05T12:00:00.000Z",
  "versionId": "1"
}
```

**Instrucciones de uso:**
1. Crea una nueva credencial en n8n llamada **"OpenAI API"** con tu clave de API de OpenAI.
2. Crea otra credencial llamada **"Slack API"** con tu token de bot de Slack (con permisos para publicar en los canales).
3. Importa este JSON en n8n.
4. Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu workspace de Slack.
5. El webhook estará disponible en `https://tu-n8n-instance.com/webhook` (ajusta la URL según tu despliegue).
6. Envía una solicitud POST al webhook con un JSON como:
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Necesito ayuda con mi cuenta"
}
```

**Notas:**
- El prompt de OpenAI está diseñado para devolver solo la categoría (ej: `soporte`). Si el modelo devuelve texto adicional, el nodo "Normalizar Clasificación" limpiará espacios y convertirá a minúsculas.
- Si necesitas ajustar el modelo de OpenAI, cambia `"gpt-3.5-turbo"` en el nodo correspondiente.
- Los mensajes en Slack se formatean como: `"Nuevo mensaje de [email]: [mensaje]"`.