# Ministral 14B — code_generation/n8n_workflow_json

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 6.93 | quality: 7.2
- latency_total: 42.11s | tokens_per_second: 48.6
- input_tokens: 120 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo para un workflow de **n8n** que cumple con tus requisitos. Este workflow incluye un **webhook**, extracción de datos, clasificación con OpenAI y envío a canales de Slack según la categoría:

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "webhook",
        "specification": {
          "type": "object",
          "properties": {
            "email": {
              "type": "string"
            },
            "message": {
              "type": "string"
            }
          },
          "required": ["email", "message"]
        }
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
        "resource": "openai",
        "operation": "chatCompletion",
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas o otro. Responde solo con la categoría sin explicación."
          },
          {
            "role": "user",
            "content": "={{$json["message"]}}"
          }
        ],
        "maxTokens": 10,
        "temperature": 0,
        "authentication": "openAiApiKey"
      },
      "name": "Clasificar Mensaje (OpenAI)",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApiKey": "YOUR_OPENAI_API_KEY"
      }
    },
    {
      "parameters": {
        "resource": "slack",
        "operation": "sendMessage",
        "options": {
          "channel": "#support",
          "text": "Nuevo mensaje de soporte:\n\nEmail: {{$json[\"email\"]}}\nMensaje: {{json[\"message\"]}}",
          "username": "n8n Bot"
        }
      },
      "name": "Enviar a Soporte (Slack)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        650,
        100
      ],
      "credentials": {
        "slackApi": "YOUR_SLACK_API_KEY"
      }
    },
    {
      "parameters": {
        "resource": "slack",
        "operation": "sendMessage",
        "options": {
          "channel": "#sales",
          "text": "Nuevo mensaje de ventas:\n\nEmail: {{$json[\"email\"]}}\nMensaje: {{json[\"message\"]}}",
          "username": "n8n Bot"
        }
      },
      "name": "Enviar a Ventas (Slack)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "slackApi": "YOUR_SLACK_API_KEY"
      }
    },
    {
      "parameters": {
        "resource": "slack",
        "operation": "sendMessage",
        "options": {
          "channel": "#general",
          "text": "Nuevo mensaje genérico:\n\nEmail: {{$json[\"email\"]}}\nMensaje: {{json[\"message\"]}}",
          "username": "n8n Bot"
        }
      },
      "name": "Enviar a General (Slack)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        650,
        500
      ],
      "credentials": {
        "slackApi": "YOUR_SLACK_API_KEY"
      }
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "category",
              "value": "={{$node["Clasificar Mensaje (OpenAI)"].json[\"choices\"][0][\"message\"][\"content\"].trim()}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        500
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"category\"]}}",
              "value2": "soporte",
              "operation": "equals"
            }
          ]
        },
        "otherwise": {}
      },
      "name": "If Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        400
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"category\"]}}",
              "value2": "ventas",
              "operation": "equals"
            }
          ]
        },
        "otherwise": {}
      },
      "name": "If Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        450
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json[\"category\"]}}",
              "value2": "otro",
              "operation": "equals"
            }
          ]
        },
        "otherwise": {}
      },
      "name": "If Otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        550
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje (OpenAI)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Mensaje (OpenAI)": {
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
            "node": "If Soporte",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If Soporte": {
      "main": [
        [
          {
            "node": "Enviar a Soporte (Slack)",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "otherwise": [
        [
          {
            "node": "If Ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If Ventas": {
      "main": [
        [
          {
            "node": "Enviar a Ventas (Slack)",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "otherwise": [
        [
          {
            "node": "If Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If Otro": {
      "main": [
        [
          {
            "node": "Enviar a General (Slack)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

---

### **Explicación del Workflow**:
1. **Webhook POST**:
   - Escucha solicitudes POST en `/webhook` y extrae los campos `email` y `message` del cuerpo (`body`).

2. **Clasificación con OpenAI**:
   - Usa el modelo `gpt-3.5-turbo` para clasificar el mensaje en `soporte`, `ventas` o `otro`.
   - El prompt está configurado para que responda **solo con la categoría** (sin explicación).

3. **Nodos `If` para rutas condicionales**:
   - **`If Soporte`**: Si la categoría es `soporte`, envía el mensaje a `#support` en Slack.
   - **`If Ventas`**: Si es `ventas`, lo envía a `#sales`.
   - **`If Otro`**: Si es `otro`, lo envía a `#general`.

4. **Slack**:
   - Cada nodo de Slack incluye el `email` y el `message` en el formato:
     ```
     Nuevo mensaje de [categoría]:
     Email: {{email}}
     Mensaje: {{message}}
     ```

---

### **Configuración Requerida**:
1. **