# Llama 3.1 8B Instant (Groq) — code_generation/n8n_workflow_json

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.06 | quality: 6.04
- latency_total: 1.879s | tokens_per_second: 710.4
- input_tokens: 150 | output_tokens: 1335
- judge_score: 2.6 | justificación: 

## Respuesta completa

A continuación, te proporciono un ejemplo de cómo podrías configurar un workflow en N8N utilizando un webhook POST, un nodo de IA (OpenAI) y Slack:

```json
{
  "name": "Workflow de Clasificación de Mensajes",
  "nodes": {
    "Webhook de Inicio": {
      "parameters": {
        "topic": "http://example.com/webhook"
      },
      "type": "n8n-nodes-base.webhook",
      "title": "Webhook de Inicio",
      "description": ""
    },
    "Extraer Campos": {
      "parameters": {
        "fields": {
          "email": {
            "value": "={{$json[\"email\"]}}"
          },
          "mensaje": {
            "value": "={{$json[\"message\"]}}"
          }
        },
        "options": {}
      },
      "type": "n8n-nodes-base.function",
      "title": "Extraer Campos",
      "description": ""
    },
    "Nodo de IA (OpenAI)": {
      "parameters": {
        "endpoint": "https://api.openai.com/v1/classify",
        "options": {
          "headers": {
            "Authorization": "Bearer TU_CLAVE_API_OPENAI"
          },
          "body": {
            "input": "={{$node[\"Extraer Campos\"].data.mensaje}}",
            "model": "text-classification",
            "max_tokens": 2048
          }
        },
        "body": {},
        "tags": [],
        "name": ""
      },
      "type": "n8n-nodes-base.httpRequest",
      "title": "Nodo de IA (OpenAI)",
      "description": ""
    },
    "Clasificar Mensaje": {
      "parameters": {
        "options": {
          "json": {
            "classification": "={{$node[\"Nodo de IA (OpenAI)\"].data.output.classifications[0].label }}"
          }
        },
        "function": "json"
      },
      "type": "n8n-nodes-base.function",
      "title": "Clasificar Mensaje",
      "description": ""
    },
    "Enviar a Slack (Soporte)": {
      "parameters": {
        "channel": "#support",
        "options": {
          "json": {
            "text": "Nuevo mensaje de soporte: {{=$node[\"Extraer Campos\"].data.email}}",
            "attachments": [
              {
                "fields": [
                  {
                    "title": "Mensaje",
                    "value": "{{=$node[\"Extraer Campos\"].data.mensaje}}",
                    "short": false
                  }
                ]
              }
            ]
          }
        },
        "function": "json"
      },
      "type": "n8n-nodes-base.slack",
      "title": "Enviar a Slack (Soporte)",
      "description": ""
    },
    "Enviar a Slack (Ventas)": {
      "parameters": {
        "channel": "#sales",
        "options": {
          "json": {
            "text": "Nuevo mensaje de ventas: {{=$node[\"Extraer Campos\"].data.email}}",
            "attachments": [
              {
                "fields": [
                  {
                    "title": "Mensaje",
                    "value": "{{=$node[\"Extraer Campos\"].data.mensaje}}",
                    "short": false
                  }
                ]
              }
            ]
          }
        },
        "function": "json"
      },
      "type": "n8n-nodes-base.slack",
      "title": "Enviar a Slack (Ventas)",
      "description": ""
    },
    "Enviar a Slack (General)": {
      "parameters": {
        "channel": "#general",
        "options": {
          "json": {
            "text": "Nuevo mensaje general: {{=$node[\"Extraer Campos\"].data.email}}",
            "attachments": [
              {
                "fields": [
                  {
                    "title": "Mensaje",
                    "value": "{{=$node[\"Extraer Campos\"].data.mensaje}}",
                    "short": false
                  }
                ]
              }
            ]
          }
        },
        "function": "json"
      },
      "type": "n8n-nodes-base.slack",
      "title": "Enviar a Slack (General)",
      "description": ""
    }
  },
  "connections": {
    "Webhook de Inicio": {
      "main": [
        {
          "node": "Extraer Campos",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Extraer Campos": {
      "main": [
        {
          "node": "Nodo de IA (OpenAI)",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Nodo de IA (OpenAI)": {
      "main": [
        {
          "node": "Clasificar Mensaje",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Clasificar Mensaje": {
      "main": [
        {
          "node": "Enviar a Slack (Soporte)",
          "type": "main",
          "index": 0
        },
        {
          "node": "Enviar a Slack (Ventas)",
          "type": "main",
          "index": 0
        },
        {
          "node": "Enviar a Slack (General)",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Enviar a Slack (Soporte)": {
      "main": []
    },
    "Enviar a Slack (Ventas)": {
      "main": []
    },
    "Enviar a Slack (General)": {
      "main": []
    }
  }
}
```

Ten en cuenta que debes reemplazar `TU_CLAVE_API_OPENAI` con tu clave API real de OpenAI. También debes configurar los canales de Slack (`#support`, `#sales` y `#general`) en tus configuraciones de Slack.

Espero que esto te ayude a configurar tu workflow en N8N. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!