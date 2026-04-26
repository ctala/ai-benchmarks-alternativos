# GPT-OSS 120B (Ollama Cloud) — code_generation/n8n_workflow_json

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.3 | quality: 7.28
- latency_total: 21.533s | tokens_per_second: 88.7
- input_tokens: 179 | output_tokens: 1911
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "name": "Clasificador de mensajes → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming",
        "responseMode": "onReceived",
        "responseContentType": "json",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "{{$node[\"Webhook\"].webhookId}}"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json[\"email\"]}}"
            },
            {
              "name": "message",
              "value": "={{$json[\"message\"]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Extract fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "maxTokens": 10,
        "systemMessage": "",
        "messages": [
          {
            "role": "system",
            "content": "You are a classifier. Classify the supplied message into ONE of the following categories exactly as written: soporte, ventas, otro. Respond only with the category word."
          },
          {
            "role": "user",
            "content": "Message: {{ $json.message }}"
          }
        ],
        "options": {}
      },
      "name": "OpenAI - Classify",
      "type": "n8n-nodes-openai.openAi",
      "typeVersion": 1,
      "position": [
        750,
        300
      ],
      "credentials": {
        "openAiApi": "OpenAI_API"
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}",
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        }
      },
      "name": "Switch - Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1000,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        150
      ],
      "credentials": {
        "slackApi": "Slack_API"
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "slackApi": "Slack_API"
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje (otro):\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación:* {{ $json[\"choices\"][0][\"message\"][\"content\"].trim() }}",
        "options": {}
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        450
      ],
      "credentials": {
        "slackApi": "Slack_API"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract fields": {
      "main": [
        [
          {
            "node": "OpenAI - Classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Classify": {
      "main": [
        [
          {
            "node": "Switch - Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Category": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          },
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 1
          },
          {
            "node": "Slack - General",
            "type": "main",
            "index": 2
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "1"
}
```

**Instrucciones rápidas**

1. Copia todo el bloque JSON anterior.  
2. En tu instancia de n8n, ve a **Workflows → Import** y pega el JSON.  
3. Configura las credenciales:  
   - `OpenAI_API` → tu clave de API de OpenAI.  
   - `Slack_API` → token de Slack con permisos para publicar en los canales `#support`, `#sales` y `#general`.  
4. (Opcional) Cambia el **path** del webhook (`incoming`) si deseas otro endpoint.  
5. Activa el workflow y prueba enviando un `POST` a `https://TU_INSTANCIA/n8n/webhook/incoming` con un cuerpo JSON como:

```json
{
  "email": "usuario@ejemplo.com",
  "message": "Necesito ayuda con mi cuenta"
}
```

El mensaje será clasificado y enviado al canal de Slack correspondiente. ¡Listo!