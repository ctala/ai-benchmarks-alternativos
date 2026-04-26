# Mistral Small 4 — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 7.41 | quality: 8.6
- latency_total: 12.534s | tokens_per_second: 150.2
- input_tokens: 132 | output_tokens: 1883
- judge_score: 4.0 | justificación: 

## Respuesta completa

Aquí tienes el workflow completo en JSON para **n8n** que cumple con todos los requisitos que mencionaste:

```json
{
  "name": "Clasificación de mensajes con IA y envío a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook-clasificacion"
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300]
    },
    {
      "parameters": {
        "functionCode": "// Extrae email y message del body\nconst body = items[0].json.body || {};\nconst email = body.email;\nconst message = body.message;\n\n// Devuelve los datos para los siguientes nodos\nreturn [\n  {\n    json: {\n      email: email,\n      message: message\n    }\n  }\n];"
      },
      "id": "extract-data",
      "name": "Extraer email y mensaje",
      "type": "n8n-nodes-base.function",
      "position": [450, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "Clasifica el siguiente mensaje como una de estas tres opciones: 'soporte', 'ventas' o 'otro'. Solo responde con la categoría sin explicaciones.\n\nMensaje: \"{{ $('Extraer email y mensaje').item.json.message }}\"",
        "temperature": 0.7
      },
      "id": "ia-classification",
      "name": "Clasificar con IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": "openai-api"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $('Clasificar con IA').item.json.choices[0].message.content }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "if-soporte",
      "name": "¿Es soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 200]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\n\n**Email:** {{ $('Extraer email y mensaje').item.json.email }}\n\n**Mensaje:** {{ $('Extraer email y mensaje').item.json.message }}"
      },
      "id": "slack-soporte",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 100],
      "credentials": {
        "slackApi": "slack-api"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $('Clasificar con IA').item.json.choices[0].message.content }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "if-ventas",
      "name": "¿Es ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 400]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\n\n**Email:** {{ $('Extraer email y mensaje').item.json.email }}\n\n**Mensaje:** {{ $('Extraer email y mensaje').item.json.message }}"
      },
      "id": "slack-ventas",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 300],
      "credentials": {
        "slackApi": "slack-api"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje (otro):\n\n**Email:** {{ $('Extraer email y mensaje').item.json.email }}\n\n**Mensaje:** {{ $('Extraer email y mensaje').item.json.message }}"
      },
      "id": "slack-otro",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 500],
      "credentials": {
        "slackApi": "slack-api"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer email y mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y mensaje": {
      "main": [
        [
          {
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "¿Es soporte?",
            "type": "main",
            "index": 0
          },
          {
            "node": "¿Es ventas?",
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
            "node": "Enviar a #support",
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
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enviar a #support": {
      "main": [
        []
      ]
    },
    "Enviar a #sales": {
      "main": [
        []
      ]
    },
    "Enviar a #general": {
      "main": [
        []
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1.0.0"
}
```

### 🔧 **Requisitos previos (antes de importar):**
1. **Credenciales necesarias**:
   - Configura una **credencial de OpenAI** (API key) en n8n.
   - Configura una **credencial de Slack** (token de bot) que tenga acceso a los canales `#support`, `#sales` y `#general`.

2. **Canales de Slack**:
   - Asegúrate de que el bot de Slack esté añadido a los canales correspondientes.

3. **Modelo de OpenAI**:
   - El workflow usa `gpt-3.5-turbo`. Si quieres usar otro modelo (como `gpt-4`), cambia el parámetro `model` en el nodo "Clasificar con IA".

---

### 📌 **Cómo probar el workflow:**
1. **Actívalo** en n8n.
2. **Envía un POST** a la URL del webhook (ejemplo con `curl`):
   ```bash
   curl -X POST \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "message": "Tengo un problema con mi pedido"}' \
     https://<TU-DOMINIO>.app/webhook-clasificacion
   ```
3. El mensaje se clasificará y enviará al canal correcto de Slack.

---

### 🛠 **Posibles mejoras**:
- Añadir manejo de errores (ej: si el mensaje no es reconocible por la IA).
- Usar un **nodo de Switch** en lugar de múltiples nodos `if` para simplificar el flujo.
- Guardar los datos en una base de datos o CRM si es necesario.