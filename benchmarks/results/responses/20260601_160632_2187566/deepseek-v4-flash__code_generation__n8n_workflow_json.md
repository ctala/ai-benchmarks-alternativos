# DeepSeek V4 Flash (OpenRouter) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.84 | quality: 8.6
- latency_total: 22.748s | tokens_per_second: 95.3
- input_tokens: 126 | output_tokens: 2168
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack o manejo de errores.

## Respuesta completa

Aquí tienes el workflow completo de n8n en formato JSON que implementa exactamente lo que necesitas:

```json
{
  "name": "Clasificador de mensajes con IA",
  "nodes": [
    {
      "parameters": {},
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [250, 300],
      "webhookId": "tu-webhook-id",
      "options": {
        "responseMode": "onReceived"
      },
      "webhookMethods": {
        "POST": {
          "path": "clasificar-mensaje"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const body = $input.first().json.body;\nreturn {\n  email: body.email,\n  message: body.message\n};"
      },
      "id": "extraer-campos",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con una de estas palabras, sin ningún otro texto ni puntuación."
            },
            {
              "role": "user",
              "content": "=Mensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "clasificador-ia",
      "name": "Clasificador IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": {
          "id": "tu-credential-id",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const aiResponse = $input.first().json.message.content.trim().toLowerCase();\n\nlet classification = 'otro';\nif (aiResponse === 'soporte' || aiResponse === 'ventas') {\n  classification = aiResponse;\n}\n\nreturn {\n  email: $json.email,\n  message: $json.message,\n  classification: classification\n};"
      },
      "id": "procesar-clasificacion",
      "name": "Procesar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "router-soporte",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [1050, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "router-ventas",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [1050, 400]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "={{ `Nuevo mensaje de soporte de ${$json.email}:\n\n${$json.message}` }}"
      },
      "id": "slack-soporte",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 200],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credential-id",
          "name": "Slack API"
        }
      },
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "={{ `Nuevo mensaje de ventas de ${$json.email}:\n\n${$json.message}` }}"
      },
      "id": "slack-ventas",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 350],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credential-id",
          "name": "Slack API"
        }
      },
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "={{ `Nuevo mensaje (clasificado como otro) de ${$json.email}:\n\n${$json.message}` }}"
      },
      "id": "slack-otro",
      "name": "Slack Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 500],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credential-id",
          "name": "Slack API"
        }
      },
      "onError": "continueRegularOutput"
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer campos": {
      "main": [
        [
          {
            "node": "Clasificador IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador IA": {
      "main": [
        [
          {
            "node": "Procesar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Procesar clasificación": {
      "main": [
        [
          {
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es soporte?": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "¿Es ventas?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "¿Es ventas?": {
      "main": [
        [
          {
            "node": "Slack Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "versionId": "workflow-v1",
  "active": true,
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": []
}
```

## Cómo usar este workflow:

1. **Importa el JSON** en n8n (Workflows → Add Workflow → Import)

2. **Configura las credenciales**:
   - Haz clic en el nodo "Clasificador IA" y configura tu API Key de OpenAI
   - Haz clic en cada nodo de Slack y configura las credenciales de tu workspace de Slack

3. **Webhook URL**: Una vez activado el workflow, verás el webhook URL en la configuración del nodo "Webhook". La ruta será algo como: `https://tu-n8n-instancia/webhook/clasificar-mensaje`

4. **Prueba** con un POST request:
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Necesito ayuda con mi cuenta, no puedo iniciar sesión"
}
```

## Flujo del workflow:

1. **Webhook** → Recibe POST con body JSON
2. **Extraer campos** → Extrae `email` y `message` del body
3. **Clasificador IA** → Envía el mensaje a GPT-3.5 para clasificarlo
4. **Procesar clasificación** → Normaliza la respuesta de la IA
5. **Router** → Usa nodos IF para redirigir según la clasificación
6. **Slack** → Envía el mensaje al canal correspondiente

## Notas importantes:

- El workflow responderá con el código HTTP 200 inmediatamente después de recibir el webhook
- Si la clasificación no es exactamente "soporte" o "ventas", automáticamente se envía a #general
- Los canales de Slack deben existir en tu workspace
- Puedes cambiar el modelo de OpenAI a GPT-4 si prefieres mayor precisión