# Ministral 14B (NIM) — code_generation/n8n_workflow_json

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 6.12 | quality: 6.64
- latency_total: 117.466s | tokens_per_second: 17.4
- input_tokens: 120 | output_tokens: 2048
- judge_score: 2.6 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n que cumple con tus requisitos. Este workflow incluye:
- Un webhook para recibir la petición POST
- Extracción de los campos `email` y `message` del cuerpo de la petición
- Clasificación con OpenAI (usando el nodo OpenAI)
- Envío al canal de Slack correspondiente según la clasificación

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "webhook",
        "path": "webhook-incoming",
        "responseCode": 200,
        "responseBody": "{\"status\":\"success\",\"message\":\"Mensaje recibido\"}",
        "responseHeaders": {}
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
        "authentication": "none",
        "additionalHeaders": {},
        "options": {}
      },
      "name": "Set Email and Message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {}
    },
    {
      "parameters": {
        "resource": "chatCompletions",
        "options": {
          "model": "gpt-3.5-turbo",
          "messages": [
            {
              "role": "system",
              "content": "Clasifica el siguiente mensaje en una de las siguientes categorías: soporte, ventas u otro. Responde solo con la categoría. Ejemplo: 'soporte'"
            },
            {
              "role": "user",
              "content": "{{$node["Set Email and Message"].json["message"]}}"
            }
          ],
          "temperature": 0,
          "maxTokens": 50
        }
      },
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-openai.api",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openaiApi": "openai-API"
      }
    },
    {
      "parameters": {
        "text": "New message received:\n\nEmail: {{$node[\"Set Email and Message\"].json[\"email\"]}}\nMessage: {{$node[\"Set Email and Message\"].json[\"message\"]}}\nCategory: {{$node[\"Classify with OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
        "channel": "",
        "username": "n8n Bot"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        400
      ],
      "credentials": {
        "slackApi": "slack-API"
      }
    },
    {
      "parameters": {
        "text": "New message received:\n\nEmail: {{$node[\"Set Email and Message\"].json[\"email\"]}}\nMessage: {{$node[\"Set Email and Message\"].json[\"message\"]}}\nCategory: {{$node[\"Classify with OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
        "channel": "sales",
        "username": "n8n Bot"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        500
      ],
      "credentials": {
        "slackApi": "slack-API"
      }
    },
    {
      "parameters": {
        "text": "New message received:\n\nEmail: {{$node[\"Set Email and Message\"].json[\"email\"]}}\nMessage: {{$node[\"Set Email and Message\"].json[\"message\"]}}\nCategory: {{$node[\"Classify with OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
        "channel": "general",
        "username": "n8n Bot"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        600
      ],
      "credentials": {
        "slackApi": "slack-API"
      }
    },
    {
      "parameters": {
        "conditions": {
          "number1": "{{$node[\"Classify with OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
          "string1": "soporte",
          "comparator": "isEqualTo"
        }
      },
      "name": "Check if Support",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "number1": "{{$node[\"Classify with OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"]}}",
          "string1": "ventas",
          "comparator": "isEqualTo"
        }
      },
      "name": "Check if Sales",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        850,
        350
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set Email and Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Email and Message": {
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
            "node": "Check if Support",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check if Support": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "false": [
        [
          {
            "node": "Check if Sales",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check if Sales": {
      "main": [
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "false": [
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### **Cómo configurar el workflow en n8n:**

1. **Webhook**: Debes configurar el webhook en n8n para que acepte peticiones POST al endpoint `/webhook-incoming` (o el que tú definas).

2. **Credenciales de OpenAI**: Crea una credencial de tipo `OpenAI` en n8n con tu clave API de OpenAI.

3. **Credenciales de Slack**:
   - Crea una credencial de tipo `Slack` en n8n con tu token de autenticación de Slack (se genera cuando creas una app en Slack).
   - Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu espacio de trabajo de Slack.

4. **Configuración del Nodo "Set Email and Message"**:
   - Este nodo extrae los campos `email` y `message` del cuerpo del webhook. Si el formato de la petición es JSON, el nodo deberá estar configurado para extraer esos campos del JSON.

### **Ejemplo de petición POST que debe recibir el webhook:**
```json
{
  "email": "usuario@example.com",
  "message": "Tengo problemas para acceder a mi cuenta."
}
```

### **Notas importantes:**
- La lógica de OpenAI clasifica el mensaje en tres categorías: `soporte`, `ventas` o `otro`. Si OpenAI responde con un texto diferente al esperado (por ejemplo, "soporte técnico"), deberás ajustar los nodos `Check if Support` y `Check if Sales` para que sean más robustos.
- Para mejorar la clasificación, podrías personalizar el prompt de OpenAI para que sea más específico.
- Este workflow asume que la respuesta de OpenAI será exactamente igual a las opciones (`soporte`, `ventas`, `otro`). Si OpenAI responde con algo como "soporte técnico", deberás ajustar los comparadores en los nodos `Check if Support` y `Check if Sales`.

Si necesitas ajustar la lógica