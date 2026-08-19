# MiMo-V2-Omni (multimodal) — code_generation/n8n_workflow_json

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.24 | quality: 8.12
- latency_total: 16.667s | tokens_per_second: 122.9
- input_tokens: 365 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

# Workflow de N8N - Clasificación de Mensajes con IA

Aquí tienes el JSON completo del workflow:

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-1",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-1",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [460, 300]
    },
    {
      "parameters": {
        "method": "POST",
        "url": "https://api.openai.com/v1/chat/completions",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendBody": true,
        "specifyBody": "json",
        "jsonBody": "={\n  \"model\": \"gpt-4o-mini\",\n  \"messages\": [\n    {\n      \"role\": \"system\",\n      \"content\": \"Eres un clasificador de mensajes. Responde ÚNICAMENTE con una sola palabra: 'soporte', 'ventas' o 'otro'.\\n\\nClasifica como 'soporte' si el mensaje trata sobre: problemas técnicos, errores, ayuda con el producto, garantías, devoluciones, o soporte general.\\n\\nClasifica como 'ventas' si el mensaje trata sobre: consultas de precios, compras, productos nuevos, ofertas, descuentos, o interés en adquirir productos/servicios.\\n\\nClasifica como 'otro' para cualquier otro tipo de mensaje que no encaje en las categorías anteriores.\"\n    },\n    {\n      \"role\": \"user\",\n      \"content\": \"{{ $json.message }}\"\n    }\n  ],\n  \"temperature\": 0,\n  \"max_tokens\": 10\n}",
        "options": {}
      },
      "id": "http-1",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 4.1,
      "position": [680, 300],
      "credentials": {
        "httpHeaderAuth": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API Key"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Extraer la clasificación de la respuesta de OpenAI\nconst response = $input.first().json;\nconst classification = response.choices[0].message.content.trim().toLowerCase();\n\n// Obtener datos originales\nconst originalData = $('Extraer Campos').first().json;\n\nlet channel;\n\nswitch (classification) {\n  case 'soporte':\n    channel = '#support';\n    break;\n  case 'ventas':\n    channel = '#sales';\n    break;\n  default:\n    channel = '#general';\n    break;\n}\n\nreturn [{\n  json: {\n    email: originalData.email,\n    message: originalData.message,\n    classification: classification,\n    channel: channel\n  }\n}];"
      },
      "id": "code-1",
      "name": "Determinar Canal",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [900, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "={{ $json.channel }}",
        "text": ":incoming_envelope: *Nuevo mensaje clasificado como: {{ $json.classification }}*\n\n*De:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-1",
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1120, 300],
      "credentials": {
        "slackOAuth2Api": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack OAuth2"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"success\": true,\n  \"classification\": \"{{ $('Determinar Canal').first().json.classification }}\",\n  \"channel\": \"{{ $('Determinar Canal').first().json.channel }}\"\n}",
        "options": {
          "responseCode": 200
        }
      },
      "id": "respond-1",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1340, 300]
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
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
          },
          {
            "node": "Responder Webhook",
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
  "tags": [
    {
      "name": "ia",
      "id": "1"
    },
    {
      "name": "clasificacion",
      "id": "2"
    }
  ]
}
```

---

## 📊 Diagrama del Flujo

```
┌─────────────────┐     ┌─────────────────┐     ┌──────────────────────┐
│  Webhook POST   │────▶│  Extraer Campos │────▶│  Clasificar con      │
│  /clasificar-   │     │  (email,        │     │  OpenAI (GPT-4o-mini)│
│  mensaje        │     │   message)      │     │                      │
└─────────────────┘     └─────────────────┘     └──────────┬───────────┘
                                                           │
                                                           ▼
┌─────────────────┐     ┌──────────────────────────────────────────────┐
│  Responder      │◀────│  Determinar Canal (Switch por clasificación) │
│  Webhook 200    │     │                                              │
└─────────────────┘     │  soporte → #support                          │
                        │  ventas  → #sales                            │
                        │  otro    → #general                          │
                        └──────────────────┬───────────────────────────┘
                                           │
                                           ▼
                                ┌─────────────────────┐
                                │    Enviar a Slack   │
                                └─────────────────────┘
```

---

## 🔧 Pasos de Configuración

### 1. **Credenciales OpenAI**
```
Settings → Credentials → Add Credential → Header Auth
  Name: OpenAI API Key
  Header Name: Authorization
  Header Value: Bearer sk-tu-api-key-aqui
```

### 2