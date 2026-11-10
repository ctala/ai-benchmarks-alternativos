# Qwen 3.7 Flash — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 8.08 | quality: 8.6
- latency_total: 58.149s | tokens_per_second: 110.9
- input_tokens: 125 | output_tokens: 6446
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del flujo de trabajo de N8N. La estructura es clara y bien organizada, lo que la hace útil para un emprendedor. Sin embargo, la profundidad es moderada ya que sigue de cerca las instrucciones sin ofrecer insights adicionales.

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

Aquí tienes el workflow completo en formato JSON válido para n8n. Copia y pega este contenido en un archivo `.json` o impórtalo directamente desde la interfaz de n8n (`Import from > JSON`).

```json
{
  "name": "Email Classifier to Slack",
  "nodes": [
    {
      "id": "webhook_1",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-email",
        "responseMode": "responseNode",
        "options": {}
      },
      "credentials": {},
      "alwaysActive": false
    },
    {
      "id": "ai_1",
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAiChatCompletion",
      "typeVersion": 2,
      "position": [220, 0],
      "parameters": {
        "model": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "promptType": "define",
        "text": "Classify the following message into exactly one of these categories: soporte, ventas, otro. Return ONLY the category name in lowercase without quotes or extra text.\n\nMessage: {{ $json.message }}",
        "systemMessage": "You are a strict classifier. Respond with ONLY the category name."
      },
      "credentials": {
        "openAiApi": {
          "id": "your-openai-credential-id",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "id": "switch_1",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [440, 0],
      "parameters": {
        "rules": {
          "values": [
            {
              "expression": "{{ ($json.text || '').toLowerCase().trim() === 'soporte' }}",
              "outputNodeId": "slack_support_1"
            },
            {
              "expression": "{{ ($json.text || '').toLowerCase().trim() === 'ventas' }}",
              "outputNodeId": "slack_sales_1"
            }
          ]
        },
        "fallbackOutputNodeId": "slack_general_1"
      }
    },
    {
      "id": "slack_support_1",
      "name": "Send to Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [660, -150],
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#support",
        "text": "📧 Email: {{ $('Webhook Trigger').item.json.email }}\n💬 Message: {{ $('Webhook Trigger').item.json.message }}"
      },
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "id": "slack_sales_1",
      "name": "Send to Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [660, 0],
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#sales",
        "text": "📧 Email: {{ $('Webhook Trigger').item.json.email }}\n💬 Message: {{ $('Webhook Trigger').item.json.message }}"
      },
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "id": "slack_general_1",
      "name": "Send to General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [660, 150],
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#general",
        "text": "📧 Email: {{ $('Webhook Trigger').item.json.email }}\n💬 Message: {{ $('Webhook Trigger').item.json.message }}"
      },
      "credentials": {
        "slackApi": {
          "id": "your-slack-credential-id",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "saveDataErrorExecution": "all",
    "saveDataSuccessExecution": "all",
    "executionTimeout": 120,
    "timezone": "UTC"
  },
  "tags": []
}
```

### 📋 Instrucciones de uso:

1. **Importar**: En tu instancia de n8n, ve a `Workflows` → `Import from` → `JSON` y pega el código.
2. **Credenciales**: 
   - Reemplaza `your-openai-credential-id` con el ID real de tu credencial de OpenAI en n8n.
   - Reemplaza `your-slack-credential-id` con el ID de tu credencial de Slack.
   - Si no las tienes, créalas en la pestaña `Credentials` antes de importar o edita el JSON después.
3. **Activar Webhook**: Guarda el workflow y activa el nodo `Webhook Trigger`. n8n te dará una URL única tipo `https://tu-n8n.com/webhook/...`.
4. **Prueba**: Envía un POST al webhook con este JSON:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Necesito ayuda con mi pedido #1234"
   }
   ```
5. **Lógica de enrutamiento**: 
   - El nodo OpenAI devuelve solo la categoría.
   - El nodo `Switch` evalúa expresiones JavaScript seguras (ignora mayúsculas/minúsculas y espacios extra).
   - Si no coincide con `soporte` ni `ventas`, cae por defecto en `#general`.

¿Necesitas que ajuste alguna versión de nodos o agregue manejo de errores?