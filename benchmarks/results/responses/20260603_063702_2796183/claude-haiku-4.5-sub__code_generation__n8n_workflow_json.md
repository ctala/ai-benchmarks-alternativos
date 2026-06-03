# Claude Haiku 4.5 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-haiku-4-5`
- success: True  | final: 6.39 | quality: 6.72
- latency_total: 17.362s | tokens_per_second: 152.8
- input_tokens: 10 | output_tokens: 2653
- judge_score: 2.8 | justificación: 

## Respuesta completa

# Workflow N8N - Clasificación de Mensajes a Slack

Aquí está el workflow completo en JSON:

```json
{
  "name": "Email Classifier to Slack",
  "nodes": [
    {
      "parameters": {
        "path": "webhook",
        "httpMethod": "POST",
        "responseMode": "onReceived",
        "responseData": "{}",
        "options": {}
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 250]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "email",
              "value": "={{$json.body.email}}",
              "type": "string"
            },
            {
              "id": "2",
              "name": "message",
              "value": "={{$json.body.message}}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set_data",
      "name": "Set Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [450, 250]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "create",
        "model": "gpt-4-turbo",
        "messages": {
          "messageValues": [
            {
              "content": "Clasifica el siguiente mensaje en UNA de estas categorías: 'soporte', 'ventas' u 'otro'. Responde SOLO con la palabra de la categoría, sin explicación.\n\nMensaje: {{$node[\"set_data\"].json.message}}",
              "role": "user"
            }
          ]
        },
        "options": {
          "temperature": 0.3
        }
      },
      "id": "openai_classify",
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 3.2,
      "position": [650, 250]
    },
    {
      "parameters": {
        "conditions": {
          "stringConditions": [
            {
              "value1": "={{$node[\"openai_classify\"].json.choices[0].message.content}}",
              "operation": "contains",
              "value2": "soporte"
            }
          ],
          "combinator": "and"
        }
      },
      "id": "if_soporte",
      "name": "Is Support?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [850, 150]
    },
    {
      "parameters": {
        "conditions": {
          "stringConditions": [
            {
              "value1": "={{$node[\"openai_classify\"].json.choices[0].message.content}}",
              "operation": "contains",
              "value2": "ventas"
            }
          ],
          "combinator": "and"
        }
      },
      "id": "if_ventas",
      "name": "Is Sales?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [850, 350]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 *Nuevo mensaje de soporte*\n\n*Email:* {{$node[\"set_data\"].json.email}}\n*Mensaje:* {{$node[\"set_data\"].json.message}}\n\n_Clasificación: SOPORTE_"
      },
      "id": "slack_support",
      "name": "Send to Support Channel",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 100]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📧 *Nuevo mensaje de ventas*\n\n*Email:* {{$node[\"set_data\"].json.email}}\n*Mensaje:* {{$node[\"set_data\"].json.message}}\n\n_Clasificación: VENTAS_"
      },
      "id": "slack_sales",
      "name": "Send to Sales Channel",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 300]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📧 *Nuevo mensaje general*\n\n*Email:* {{$node[\"set_data\"].json.email}}\n*Mensaje:* {{$node[\"set_data\"].json.message}}\n\n_Clasificación: OTRO_"
      },
      "id": "slack_general",
      "name": "Send to General Channel",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 500]
    }
  ],
  "connections": {
    "webhook": {
      "main": [
        [
          {
            "node": "set_data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "set_data": {
      "main": [
        [
          {
            "node": "openai_classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "openai_classify": {
      "main": [
        [
          {
            "node": "if_soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "if_ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "if_soporte": {
      "main": [
        [
          {
            "node": "slack_support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "if_ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "if_ventas": {
      "main": [
        [
          {
            "node": "slack_sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "slack_general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "callerPolicy": "workflowsFromSameOwner"
  },
  "versionId": "1"
}
```

---

## ⚙️ **Pasos de Setup**

### 1️⃣ **Credenciales necesarias**
- **OpenAI API Key** → agrega en N8N Credentials
- **Slack Bot Token** → crea un app en Slack con permisos:
  ```
  chat:write
  channels:read
  ```

### 2️⃣ **Webhook URL**
Una vez creado el workflow, N8N te genera:
```
https://tu-instance.n8n.cloud/webhook/uuid
```

Usa esa URL en tu aplicación:
```bash
curl -X POST https://tu-instance.n8n.cloud/webhook/uuid \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@example.com",
    "message": "Tengo un problema con mi orden #123"
  }'
```

### 3️⃣ **Flujo del workflow**
```
Webhook → Extract Data → OpenAI Classify → Route (3 branches) → Send to Slack
```

---

## 📝 **Ejemplo de respuestas**

| Input | Clasificación | Canal |
|-------|---|---|
| "Mi cuenta no funciona" | soporte | #support |
| "Quiero contratar vuestro plan" | ventas | #sales |
| "Saludos!" | otro | #general |

---

## 🔧 **Customizaciones comunes**

**Si quieres 4 categorías en lugar de 3:**
```json
"content": "Clasifica en: 'soporte', 'ventas', 'billing' u 'otro'..."
```

**Si quieres más detalles en el mensaje:**
```json
"text": "📧 *Mensaje:*\n```{{$node[\"set_data\"].json.message}}```\n_Confianza: {{$node[\"openai_classify\"].json.usage.prompt_tokens}} tokens_"
```

**Para usar Claude en lugar de OpenAI:**
Reemplaza el nodo OpenAI por uno de Anthropic (si tu N8N lo soporta) o usa el nodo HTTP genérico.

¿Necesitas ajustes o integración con tu instancia de N8N?