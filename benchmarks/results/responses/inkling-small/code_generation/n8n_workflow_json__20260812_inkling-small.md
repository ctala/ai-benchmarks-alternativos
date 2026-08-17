# Inkling Small — code_generation/n8n_workflow_json

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 7.02 | quality: 8.6
- latency_total: 966.628s | tokens_per_second: 7.4
- input_tokens: 126 | output_tokens: 7131
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON bien estructurado que cumple con los requisitos especificados, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

Aquí tienes el workflow completo en JSON (compatible con n8n). Usa un **Webhook POST**, un **Set** para extraer `email` y `message`, un nodo **OpenAI** para clasificar, un **Switch** para enrutar y tres nodos **Slack** para enviar a cada canal.

```json
{
  "name": "Clasificación IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "clasificar-webhook"
    },
    {
      "parameters": {
        "options": {},
        "assignments": {
          "assignments": [
            {
              "id": "email-id",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "msg-id",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        }
      },
      "id": "set-1",
      "name": "SetDatos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [450, 300]
    },
    {
      "parameters": {
        "operation": "complete",
        "modelId": "gpt-3.5-turbo-instruct",
        "prompt": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con una de esas tres palabras, sin explicaciones ni puntuación extra.\n\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "openai-1",
      "name": "ClasificarOpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": {
          "id": "cred-openai",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "expression",
        "outputs": 3,
        "conditions": {
          "rules": [
            {
              "value1": "={{ $json.choices[0].text.trim() }}",
              "operation": "equals",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.choices[0].text.trim() }}",
              "operation": "equals",
              "value2": "ventas"
            },
            {
              "value1": "={{ $json.choices[0].text.trim() }}",
              "operation": "equals",
              "value2": "otro"
            }
          ]
        }
      },
      "id": "switch-1",
      "name": "Enrutar",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 *Clasificación:* soporte\n*Email:* {{ $('SetDatos').item.json.email }}\n*Mensaje:* {{ $('SetDatos').item.json.message }}",
        "operation": "postMessage"
      },
      "id": "slack-1",
      "name": "SlackSoporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 200],
      "credentials": {
        "slackApi": {
          "id": "cred-slack",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📩 *Clasificación:* ventas\n*Email:* {{ $('SetDatos').item.json.email }}\n*Mensaje:* {{ $('SetDatos').item.json.message }}",
        "operation": "postMessage"
      },
      "id": "slack-2",
      "name": "SlackVentas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 300],
      "credentials": {
        "slackApi": {
          "id": "cred-slack",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📩 *Clasificación:* otro\n*Email:* {{ $('SetDatos').item.json.email }}\n*Mensaje:* {{ $('SetDatos').item.json.message }}",
        "operation": "postMessage"
      },
      "id": "slack-3",
      "name": "SlackOtro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 400],
      "credentials": {
        "slackApi": {
          "id": "cred-slack",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "SetDatos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "SetDatos": {
      "main": [
        [
          {
            "node": "ClasificarOpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "ClasificarOpenAI": {
      "main": [
        [
          {
            "node": "Enrutar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar": {
      "main": [
        [
          {
            "node": "SlackSoporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "SlackVentas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "SlackOtro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1",
    "saveExecutionProgress": true,
    "callerPolicy": "workflowsFromSameOwner"
  },
  "tags": []
}
```

### Cómo usarlo:
1. **Importa** el JSON en n8n (Import from file / Import from JSON).
2. **Configura credenciales**:
   - `OpenAI account` en `ClasificarOpenAI`.
   - `Slack account` en los tres nodos Slack.
3. **Ajusta los canales** (`#support`, `#sales`, `#general`) si usas nombres diferentes.
4. **Activa** el webhook y envía un POST a `https://<tu-n8n>/webhook/clasificar` con JSON:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Quiero comprar el plan premium, ¿tienen descuento?"
   }
   ```

El flujo extrae los datos, clasifica con IA y envía al canal correspondiente automáticamente.