# Inkling Small — code_generation/n8n_workflow_json

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 6.6 | quality: 7.2
- latency_total: 24.576s | tokens_per_second: 357.2
- input_tokens: 126 | output_tokens: 8779
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de profundidad en la configuración del nodo de Slack y no especifica cómo se manejan los canales de Slack, lo que limita su utilidad práctica.

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

Aquí tienes el workflow completo de n8n (JSON). Solo tienes que importar el archivo, configurar las **credenciales de OpenAI** y **Slack**, y activar el webhook.

```json
{
  "name": "Clasificación IA → Slack por Canal",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "node-webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "node-webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-1",
              "name": "email",
              "value": "={{ $json.body.email || $json.email }}",
              "type": "string"
            },
            {
              "id": "assign-2",
              "name": "message",
              "value": "={{ $json.body.message || $json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "node-set",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [450, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "messages": [
            {
              "role": "system",
              "content": "Clasifica el mensaje del usuario exclusivamente como 'soporte', 'ventas' u 'otro'. Responde SOLO con una de esas tres palabras, sin explicaciones ni puntuación extra."
            },
            {
              "role": "user",
              "content": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "node-openai",
      "name": "Clasificar IA",
      "type": "n8n-nodes-langchain.openAiChat",
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
        "rules": {
          "rules": [
            {
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "operation": "equals",
              "value2": "soporte"
            },
            {
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "operation": "equals",
              "value2": "ventas"
            },
            {
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "operation": "equals",
              "value2": "otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": 0
        }
      },
      "id": "node-switch",
      "name": "Switch Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [850, 300]
    },
    {
      "parameters": {
        "operation": "postMessage",
        "channel": "#support",
        "text": "📩 *Nueva consulta: soporte*\n*Email:* {{ $node['Extraer Datos'].json.email }}\n*Mensaje:* {{ $node['Extraer Datos'].json.message }}",
        "options": {}
      },
      "id": "node-slack-soporte",
      "name": "Slack Soporte",
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
        "operation": "postMessage",
        "channel": "#sales",
        "text": "📩 *Nueva consulta: ventas*\n*Email:* {{ $node['Extraer Datos'].json.email }}\n*Mensaje:* {{ $node['Extraer Datos'].json.message }}",
        "options": {}
      },
      "id": "node-slack-ventas",
      "name": "Slack Ventas",
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
        "operation": "postMessage",
        "channel": "#general",
        "text": "📩 *Nueva consulta: otro*\n*Email:* {{ $node['Extraer Datos'].json.email }}\n*Mensaje:* {{ $node['Extraer Datos'].json.message }}",
        "options": {}
      },
      "id": "node-slack-general",
      "name": "Slack General",
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
            "node": "Clasificar IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar IA": {
      "main": [
        [
          {
            "node": "Switch Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoría": {
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
            "node": "Slack Ventas",
            "type": "main",
            "index": 1
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 2
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "tags": []
}
```

### Cómo usarlo
1. **Importa** el JSON en n8n (Menú → Importar → pegar JSON).
2. **Configura credenciales**:
   - **OpenAI** (en el nodo *Clasificar IA*): tu API Key.
   - **Slack** (en los 3 nodos finales): tu token de Slack con permisos `chat:write`.
3. **Activa** el workflow.
4. Envía un `POST` al webhook (ej. `https://tun8n.com/webhook/webhook`) con body JSON:
   ```json
   {
     "email": "cliente@email.com",
     "message": "Quiero comprar el plan pro"
   }
   ```

El flujo hará:
- Extraer `email` y `message`
- Consultar a OpenAI para clasificar
- Enviar a `#support`, `#sales` o `#general` según corresponda (usando los datos originales del nodo *Extraer Datos* para que siempre lleguen completos al Slack).