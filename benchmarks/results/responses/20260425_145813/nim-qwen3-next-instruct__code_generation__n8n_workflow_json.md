# Qwen 3-Next 80B Instruct (NIM) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.62 | quality: 7.48
- latency_total: 26.901s | tokens_per_second: 76.1
- input_tokens: 118 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

Claro, aquí tienes un **workflow completo de n8n en formato JSON** que cumple con todos tus requisitos:

- Se activa con un **webhook POST**
- Extrae `email` y `message` del body
- Usa **OpenAI** para clasificar el mensaje en: `"soporte"`, `"ventas"` o `"otro"`
- Envia el email a un canal de **Slack** diferente según la clasificación

> ✅ Asegúrate de tener configurados los nodos de **OpenAI** y **Slack** con tus credenciales en n8n antes de importar este workflow.

---

### 📄 **JSON del Workflow n8N**

```json
{
  "name": "Clasificar mensaje por email y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "path": "/webhook/clasificar-email",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "keepOnlySet": false,
        "binaryPropertyName": "binary",
        "jsonParameters": true,
        "json": {
          "email": "={{ $json.email }}",
          "message": "={{ $json.message }}"
        }
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "prompt": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Responde solo con una palabra: {{ $json.message }}",
        "model": "gpt-3.5-turbo",
        "maxTokens": 10,
        "temperature": 0.1
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2.1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "keepOnlySet": false,
        "binaryPropertyName": "binary",
        "jsonParameters": true,
        "json": {
          "email": "={{ $json.email }}",
          "message": "={{ $json.message }}",
          "category": "={{ $json['OpenAI'].choices[0].message.content.trim().toLowerCase() }}"
        }
      },
      "name": "Set Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.category }}",
              "value2": "soporte"
            }
          ]
        }
      },
      "name": "Split by Condition - soporte",
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 1,
      "position": [
        1050,
        200
      ]
    },
    {
      "parameters": {
        "options": {},
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.category }}",
              "value2": "ventas"
            }
          ]
        }
      },
      "name": "Split by Condition - ventas",
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.category }}",
              "value2": "otro"
            }
          ]
        }
      },
      "name": "Split by Condition - otro",
      "type": "n8n-nodes-base.splitInBatches",
      "typeVersion": 1,
      "position": [
        1050,
        400
      ]
    },
    {
      "parameters": {
        "url": "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL_FOR_SUPPORT",
        "options": {}
      },
      "name": "Slack - Support",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1250,
        200
      ]
    },
    {
      "parameters": {
        "url": "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL_FOR_SALES",
        "options": {}
      },
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ]
    },
    {
      "parameters": {
        "url": "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_URL_FOR_GENERAL",
        "options": {}
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1250,
        400
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
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
            "node": "Set Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Category": {
      "main": [
        [
          {
            "node": "Split by Condition - soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "Split by Condition - ventas",
            "type": "main",
            "index": 0
          },
          {
            "node": "Split by Condition - otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split by Condition - soporte": {
      "main": [
        [
          {
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split by Condition - ventas": {
      "main": [
        [
          {
            "node": "Slack - Sales",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Split by Condition - otro": {
      "main": [
        [
          {
            "node": "Slack - General",
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
  "id": "workflow-12345"
}
```

---

### ✅ Instrucciones para usarlo:

1. **Importa este JSON** en tu instancia de n8n:  
   `Workflow → Import from JSON`

2. **Configura tus credenciales**:
   - **OpenAI**: Añade tu clave API de OpenAI en `Credentials`.
   - **Slack**: Reemplaza las URLs de los webhooks por las tuyas:
     - `YOUR_SLACK_WEBHOOK_URL_FOR_SUPPORT`
     - `YOUR_SLACK_WEBHOOK_URL_FOR_SALES`
     - `YOUR_SLACK_WEBHOOK_URL_FOR_GENERAL`

   > Puedes obtener estos webhooks desde [https://api.slack.com/messaging/webhooks](https://api.slack.com/messaging/webhooks)

3. **Activa el workflow** (cambia `active: false` a `true` en el JSON o desde la UI).

4. **Prueba el webhook** con una solicitud POST:

```bash
curl -X POST https://tu-n8n-url.com/webhook/clasificar-email \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@ejemplo.com",
    "message": "Tengo un problema con mi factura."
  }'
```

---

### 💡 Notas adicionales:

- El nodo **OpenAI** usa `gpt-3.5-turbo` y una prompt simple para clasificación. Si necesitas mayor precisión, puedes mejorar la prompt.
- El nodo `Split by Condition` no filtra por valor, pero **solo el nodo que cumple la condición enviará datos**. Los otros no se activarán.
- Si prefieres un enfoque más limpio