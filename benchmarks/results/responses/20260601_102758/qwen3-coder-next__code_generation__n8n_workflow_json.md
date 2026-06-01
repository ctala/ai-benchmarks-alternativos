# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.92 | quality: 10.0
- latency_total: 21.58s | tokens_per_second: 72.0
- input_tokens: 123 | output_tokens: 1554
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un workflow JSON completo que cumple con los requisitos especificados, incluyendo configuraciones detalladas y consideraciones previas, lo que la hace altamente util para un emprendedor.

## Respuesta completa

Aquí tienes un workflow completo de **n8n** en formato JSON que cumple con todos los requisitos que solicitaste:

- Se activa con un **webhook POST**
- Extrae `email` y `message` del body
- Usa **OpenAI (GPT)** para clasificar el mensaje en: `"soporte"`, `"ventas"` o `"otro"`
- Envía el mensaje a un canal de **Slack** diferente según la clasificación

> ⚠️ **Requisitos previos para usar este workflow**:
> - Tener configurado un nodo de **OpenAI** con tu API key válida (model recomendado: `gpt-4o-mini` o `gpt-3.5-turbo`)
> - Tener configurado un nodo de **Slack** con token OAuth válido y permisos para enviar mensajes a `#support`, `#sales`, `#general`
> - Asegurarte de que los canales existen en tu workspace de Slack

---

### ✅ Workflow JSON (n8n v1.70+ compatible)

```json
{
  "name": "Email Classifier to Slack",
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "path": "classify-email",
        "httpMethod": "POST",
        "responseMode": "lastNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            { "name": "email", "value": "={{ $json.body.email }}" },
            { "name": "message", "value": "={{ $json.body.message }}" }
          ]
        }
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [650, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "systemMessage": "Eres un clasificador de correos. Solo responde con una sola palabra en minúsculas: 'soporte', 'ventas' o 'otro', según el tema del mensaje. No añadas nada más.",
        "messages": {
          "message": "={{ 'Clasifica este correo: \"' + $json.message + '\". Responde únicamente con: soporte, ventas u otro.' }}"
        }
      },
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAI",
      "typeVersion": 1,
      "position": [850, 300],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "My OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "functionCode": "return items.map(item => {\n  const response = item.json.response || '';\n  const classification = response.trim().toLowerCase();\n  \n  let channel = '#general';\n  if (classification.includes('soporte')) channel = '#support';\n  else if (classification.includes('ventas')) channel = '#sales';\n\n  return {\n    json: {\n      ...item.json,\n      classification,\n      channel,\n      email: item.json.email,\n      message: item.json.message\n    }\n  };\n});"
      },
      "name": "Classify Logic",
      "type": "n8n-nodes-base.functionItem",
      "typeVersion": 1,
      "position": [1050, 300]
    },
    {
      "parameters": {
        "channel": "={{ $json.channel }}",
        "text": "📩 Nuevo mensaje recibido:\n\n**Email:** {{ $json.email }}\n\n**Mensaje:**\n> {{ $json.message }}\n\n**Clasificación:** {{ $json.classification }}",
        "additionalFields": {}
      },
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1250, 300],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "My Slack workspace"
        }
      }
    }
  ],
  "connections": {
    "Start": {
      "main": [
        {
          "node": "Webhook",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Webhook": {
      "main": [
        {
          "node": "Set",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Set": {
      "main": [
        {
          "node": "OpenAI Chat Model",
          "type": "main",
          "index": 0
        }
      ]
    },
    "OpenAI Chat Model": {
      "main": [
        {
          "node": "Classify Logic",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Classify Logic": {
      "main": [
        {
          "node": "Slack",
          "type": "main",
          "index": 0
        }
      ]
    }
  }
}
```

---

### 🔧 Notas adicionales:

1. **Credenciales**:
   - En `OpenAI Chat Model` y `Slack`, debes reemplazar `"id": "1"` y `"name": "..."` por tus propias credenciales guardadas en n8n.
   - Para OpenAI: Usa `gpt-4o-mini` (barato y rápido) o `gpt-3.5-turbo`.
   - Para Slack: Asegúrate de que el bot tenga permiso `chat:write` y esté invitado a los canales `#support`, `#sales`, `#general`.

2. **Manejo de errores (opcional)**:
   - Puedes añadir un nodo `Error Trigger` y un `If` para manejar si la clasificación falla o no coincide con ninguno de los valores esperados.

3. **Prueba del webhook**:
   - Haz un POST a `https://tu-n8n-instance.com/webhook/classify-email` con:
     ```json
     {
       "email": "cliente@ejemplo.com",
       "message": "Quiero comprar un plan premium"
     }
     ```

¿Quieres que te ayude a exportarlo directamente a tu instancia de n8n o ajustar el prompt de clasificación para mayor precisión?