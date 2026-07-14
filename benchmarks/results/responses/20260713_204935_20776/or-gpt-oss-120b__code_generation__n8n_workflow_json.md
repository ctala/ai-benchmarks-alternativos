# GPT-OSS 120B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.57 | quality: 8.4
- latency_total: 145.931s | tokens_per_second: 21.3
- input_tokens: 179 | output_tokens: 3103
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado, aunque carece de profundidad en términos de insights adicionales.

## Respuesta completa

```json
{
  "name": "Clasificador y envío a Slack",
  "id": "1",
  "active": false,
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming",
        "responseMode": "onReceived",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "c1f7a3d2-9c7b-4e12-bd5e-7f6c5b2a1e4f"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "set": [
          {
            "name": "email",
            "value": "={{$json[\"body\"][\"email\"]}}"
          },
          {
            "name": "message",
            "value": "={{$json[\"body\"][\"message\"]}}"
          }
        ]
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
        "maxTokens": 50,
        "systemMessage": "Eres un clasificador de mensajes. Recibe el mensaje del usuario y devuelve únicamente una de las siguientes palabras: \"soporte\", \"ventas\" o \"otro\".",
        "userMessage": "={{$json[\"message\"]}}"
      },
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        750,
        300
      ],
      "credentials": {
        "openAiApi": "OpenAI API"
      }
    },
    {
      "parameters": {
        "rules": [
          {
            "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}",
            "operation": "equal",
            "value2": "soporte"
          },
          {
            "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}",
            "operation": "equal",
            "value2": "ventas"
          },
          {
            "value1": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}",
            "operation": "equal",
            "value2": "otro"
          }
        ]
      },
      "name": "Switch on classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1000,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 **Nuevo mensaje de soporte**\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        200
      ],
      "credentials": {
        "slackApi": "Slack API"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📩 **Nuevo mensaje de ventas**\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "slackApi": "Slack API"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📩 **Nuevo mensaje**\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        400
      ],
      "credentials": {
        "slackApi": "Slack API"
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
            "node": "Classify with OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify with OpenAI": {
      "main": [
        [
          {
            "node": "Switch on classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch on classification": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          },
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 1
          },
          {
            "node": "Slack General",
            "type": "main",
            "index": 2
          }
        ]
      ]
    }
  },
  "settings": {}
}
``` 

**Descripción rápida del flujo**

1. **Webhook** – recibe peticiones `POST` en `/incoming`.  
2. **Extract fields** – extrae `email` y `message` del cuerpo JSON.  
3. **Classify with OpenAI** – envía el mensaje a GPT‑3.5‑turbo con un prompt que devuelve únicamente `soporte`, `ventas` o `otro`.  
4. **Switch on classification** – evalúa la respuesta de OpenAI y dirige el flujo a la rama correspondiente.  
5. **Slack Support / Slack Sales / Slack General** – envían un mensaje formateado al canal de Slack indicado (`#support`, `#sales` o `#general`).  

Solo necesitas crear/seleccionar las credenciales **OpenAI API** y **Slack API** en n8n y activar el workflow. ¡Listo!