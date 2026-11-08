# Kimi K2.7 Code — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.17 | quality: 8.6
- latency_total: 109.303s | tokens_per_second: 48.9
- input_tokens: 131 | output_tokens: 5340
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los pasos necesarios para el flujo de trabajo de N8N, aunque carece de detalles adicionales sobre la configuración de credenciales y manejo de errores.

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

Aquí tienes un workflow de **n8n** en formato JSON. Solo cópialo, impórtalo en n8n y conecta tus credenciales de **OpenAI** y **Slack**.

```json
{
  "name": "Clasificar mensaje con IA y enviar a Slack",
  "nodes": [
    {
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje",
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      }
    },
    {
      "id": "extraer-campos",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [440, 300],
      "parameters": {
        "mode": "manual",
        "assignments": {
          "assignments": [
            {
              "id": "asg-email",
              "name": "email",
              "type": "string",
              "value": "={{ $json.body.email }}"
            },
            {
              "id": "asg-message",
              "name": "message",
              "type": "string",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "id": "openai-clasificar",
      "name": "OpenAI - Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [640, 300],
      "parameters": {
        "resource": "chatMessage",
        "operation": "create",
        "modelId": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Responde ÚNICAMENTE con una de estas palabras en minúsculas: soporte, ventas, otro."
            },
            {
              "role": "user",
              "content": "={{ \"Email: \" + $json.email + \"\\nMensaje: \" + $json.message }}"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "id": "normalizar-categoria",
      "name": "Normalizar categoría",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [840, 300],
      "parameters": {
        "mode": "manual",
        "assignments": {
          "assignments": [
            {
              "id": "asg-category",
              "name": "category",
              "type": "string",
              "value": "={{ $json.output.toLowerCase().trim() }}"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "id": "switch-categoria",
      "name": "Switch por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2.1,
      "position": [1040, 300],
      "parameters": {
        "mode": "rules",
        "dataType": "string",
        "value1": "={{ $json.category }}",
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "output": 0
            },
            {
              "value": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": 2
      }
    },
    {
      "id": "slack-soporte",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1280, 100],
      "parameters": {
        "operation": "post",
        "channel": "#support",
        "text": "={{ \"Nuevo mensaje clasificado como *\" + $json.category + \"*\\n*Email:* \" + $json.email + \"\\n*Mensaje:* \" + $json.message }}"
      }
    },
    {
      "id": "slack-ventas",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1280, 300],
      "parameters": {
        "operation": "post",
        "channel": "#sales",
        "text": "={{ \"Nuevo mensaje clasificado como *\" + $json.category + \"*\\n*Email:* \" + $json.email + \"\\n*Mensaje:* \" + $json.message }}"
      }
    },
    {
      "id": "slack-otro",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1280, 500],
      "parameters": {
        "operation": "post",
        "channel": "#general",
        "text": "={{ \"Nuevo mensaje clasificado como *\" + $json.category + \"*\\n*Email:* \" + $json.email + \"\\n*Mensaje:* \" + $json.message }}"
      }
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
            "node": "OpenAI - Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificar": {
      "main": [
        [
          {
            "node": "Normalizar categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar categoría": {
      "main": [
        [
          {
            "node": "Switch por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por categoría": {
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
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": []
}
```

### Cómo usarlo

1. **Importa** el JSON en n8n.
2. **Conecta credenciales**:
   - OpenAI
   - Slack
3. **Activa el workflow**.
4. Envía un POST al webhook generado con este body JSON:

```json
{
  "email": "usuario@ejemplo.com",
  "message": "Quiero saber los precios de sus planes"
}
```

El workflow clasificará el mensaje y lo enviará al canal de Slack correspondiente:
- `soporte` → `#support`
- `ventas` → `#sales`
- `otro` → `#general`