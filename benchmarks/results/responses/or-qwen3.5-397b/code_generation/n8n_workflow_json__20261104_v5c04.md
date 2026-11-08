# Qwen 3.5 397B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.31 | quality: 8.6
- latency_total: 94.452s | tokens_per_second: 61.6
- input_tokens: 125 | output_tokens: 5821
- judge_score: 4.0 | justificación: La respuesta proporciona un JSON preciso y relevante para el workflow de N8N, cubriendo todos los pasos requeridos, aunque carece de detalles adicionales sobre la configuración de credenciales y manejo de errores.

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

Aquí tienes el JSON completo del workflow para n8n. 

**Instrucciones previas:**
1. Copia el código JSON.
2. En tu instancia de n8n, ve a **Workflows** -> **Add Workflow** -> **Import from File** (o pega el código en el editor JSON).
3. **Credenciales:** Deberás configurar las credenciales para los nodos:
   - **OpenAI API:** Para el nodo de IA.
   - **Slack OAuth2 API:** Para los nodos de Slack.
4. **Canales de Slack:** Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu workspace, o cambia los nombres en los nodos de Slack por los IDs de canal (ej. `C0123456`) si es necesario.
5. **Webhook:** Activa el workflow y usa la URL del webhook (POST) para probarlo.

```json
{
  "name": "Clasificador Email a Slack con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ],
      "webhookId": "clasificar-email"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un asistente clasificador. Tu única tarea es clasificar el siguiente mensaje en una de estas tres categorías exactas: 'soporte', 'ventas' u 'otro'. No devuelvas nada más, solo la palabra de la categoría en minúsculas."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "categoria",
              "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "edit-fields-node",
      "name": "Normalizar IA",
      "type": "n8n-nodes-base.editFields",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "operation": "equal"
            },
            {
              "value": "ventas",
              "operation": "equal"
            }
          ]
        },
        "dataPropertyName": "categoria",
        "fallbackOutput": "otro"
      },
      "id": "switch-node",
      "name": "Clasificador",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🔴 *Nuevo Mensaje de Soporte*\n📧 Email: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        150
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack OAuth2 API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "🟢 *Nuevo Mensaje de Ventas*\n📧 Email: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        300
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack OAuth2 API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "⚪ *Nuevo Mensaje General*\n📧 Email: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1100,
        450
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack OAuth2 API"
        }
      }
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
            "node": "Normalizar IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar IA": {
      "main": [
        [
          {
            "node": "Clasificador",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador": {
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
  "versionId": "workflow-version-id-placeholder",
  "meta": {
    "instanceId": "placeholder"
  },
  "id": "workflow-id-placeholder",
  "tags": []
}
```

### Notas Importantes para la Importación:

1.  **Credenciales:** En el JSON verás campos como `"id": "YOUR_OPENAI_CREDENTIAL_ID"`. Al importar en n8n, el sistema te pedirá que selecciones o crees las credenciales reales para **OpenAI** y **Slack**. No funcionará hasta que las asignes.
2.  **Nodo Normalizar IA:** He añadido un nodo intermedio (`Edit Fields`) después de OpenAI. Esto es crucial porque la IA a veces devuelve espacios en blanco o mayúsculas (" Soporte "). Este nodo limpia el texto (`trim` + `toLowerCase`) para que el nodo `Switch` funcione perfectamente.
3.  **Webhook:** El webhook está configurado en `POST`. Para probarlo, usa herramientas como Postman o cURL:
    ```bash
    curl -X POST https://TU-INSTANCIA-N8N/webhook/clasificar-email \
      -H "Content-Type: application/json" \
      -d '{"email": "cliente@ejemplo.com", "message": "Mi producto no funciona, necesito ayuda"}'
    ```
4.  **Canales Slack:** Si tu bot de Slack no tiene permiso para escribir en esos canales, debes invitarlo primero (`/invite @tu-bot`) dentro de cada canal en Slack.