# Grok 4.20 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.20`
- success: True  | final: 7.11 | quality: 8.88
- latency_total: 13.764s | tokens_per_second: 80.3
- input_tokens: 236 | output_tokens: 1105
- judge_score: 4.2 | justificación: 

## Respuesta completa

**✅ Aquí tienes el workflow completo de n8n en JSON:**

```json
{
  "name": "Clasificador de Emails → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhookId": "clasificar-email"
    },
    {
      "parameters": {
        "functionCode": "const body = $json.body || {};\n\nreturn [{\n  json: {\n    email: body.email || body.from || '',\n    message: body.message || body.text || body.content || '',\n    raw: body\n  }\n}];"
      },
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [460, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": "=Clasifica el siguiente mensaje en una sola palabra: \"soporte\", \"ventas\" o \"otro\".\n\nEmail: {{$json.email}}\nMensaje: {{$json.message}}\n\nResponde SOLO con una de estas tres palabras en minúsculas, sin explicación adicional.",
        "options": {
          "temperature": 0.1,
          "maxTokens": 10
        }
      },
      "name": "Clasificar con IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "functionCode": "const classification = $json.choices[0].message.content.trim().toLowerCase();\nlet channel = '#general';\n\nif (classification.includes('soporte')) channel = '#support';\nelse if (classification.includes('ventas')) channel = '#sales';\n\nreturn [{\n  json: {\n    channel: channel,\n    email: $input.first().json.email,\n    message: $input.first().json.message,\n    classification: classification\n  }\n}];"
      },
      "name": "Determinar Canal",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [900, 300]
    },
    {
      "parameters": {
        "channel": "={{$json.channel}}",
        "text": "📧 *Nuevo mensaje recibido*\n\n*De:* {{$json.email}}\n*Clasificación:* `{{$json.classification}}`\n\n*Mensaje:*\n>{{$json.message}}",
        "options": {}
      },
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 300],
      "credentials": {
        "slackApi": {
          "id": "",
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
            "node": "Determinar Canal",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Determinar Canal": {
      "main": [
        [
          {
            "node": "Enviar a Slack",
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
  "versionId": "1",
  "id": "1",
  "meta": {
    "instanceId": ""
  },
  "tags": []
}
```

---

### Instrucciones de uso:

1. Copia todo el JSON
2. En n8n ve a **Workflows** → **Import from JSON**
3. Pega el JSON y haz clic en **Import**
4. Configura tus credenciales:
   - **OpenAI** (necesitas API Key)
   - **Slack** (necesitas OAuth o Webhook Token)
5. Activa el workflow

El webhook estará disponible en:
`https://tu-n8n.com/webhook/clasificar-email`

¿Quieres también una versión que incluya respuesta automática al usuario según la clasificación?