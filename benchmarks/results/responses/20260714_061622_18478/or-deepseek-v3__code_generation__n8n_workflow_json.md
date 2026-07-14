# DeepSeek V3 — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 7.69 | quality: 8.6
- latency_total: 66.555s | tokens_per_second: 27.8
- input_tokens: 132 | output_tokens: 1847
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300],
      "parameters": {
        "path": "clasificador-mensajes",
        "responseMode": "responseNode",
        "options": {}
      },
      "webhookId": "webhook-clasificador",
      "typeVersion": 1
    },
    {
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "position": [450, 300],
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "typeVersion": 3
    },
    {
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "position": [650, 300],
      "parameters": {
        "resource": "chat",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el siguiente mensaje y clasifícalo EXCLUSIVAMENTE como una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Devuelve SOLO la palabra de la categoría, sin explicaciones, puntos ni espacios adicionales."
            },
            {
              "role": "user",
              "content": "Mensaje del usuario: {{ $json.message }}\nEmail: {{ $json.email }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "typeVersion": 2
    },
    {
      "name": "Router por Categoría",
      "type": "n8n-nodes-base.if",
      "position": [850, 300],
      "parameters": {
        "conditions": {
          "conditions": [
            {
              "id": "soporte",
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.chatMessage.content }}",
                    "operation": "equals",
                    "value2": "soporte"
                  }
                ]
              }
            },
            {
              "id": "ventas",
              "conditions": {
                "string": [
                  {
                    "value1": "={{ $json.chatMessage.content }}",
                    "operation": "equals",
                    "value2": "ventas"
                  }
                ]
              }
            }
          ],
          "options": {}
        }
      },
      "typeVersion": 2
    },
    {
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "position": [1050, 200],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje de SOPORTE\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Clasificación: soporte"
      },
      "typeVersion": 2
    },
    {
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "position": [1050, 300],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje de VENTAS\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Clasificación: ventas"
      },
      "typeVersion": 2
    },
    {
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "position": [1050, 400],
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje - OTRAS\n📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🏷️ Clasificación: otro"
      },
      "typeVersion": 2
    },
    {
      "name": "Respuesta Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [1250, 300],
      "parameters": {
        "responseBody": {
          "data": {
            "status": "procesado",
            "categoria": "={{ $json.chatMessage.content }}"
          }
        }
      },
      "typeVersion": 1
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
            "node": "Router por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por Categoría": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 1
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 2
          }
        ]
      ]
    },
    "Slack - Soporte": {
      "main": [
        [
          {
            "node": "Respuesta Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - Ventas": {
      "main": [
        [
          {
            "node": "Respuesta Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack - General": {
      "main": [
        [
          {
            "node": "Respuesta Webhook",
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
  "staticData": null,
  "triggerCount": 1
}
```

## Instrucciones de uso:

1. **Configurar nodo Slack**: Necesitarás configurar las credenciales de Slack en cada nodo de Slack (soporte, ventas, general).

2. **Configurar nodo OpenAI**: Necesitarás añadir tus credenciales de OpenAI API.

3. **Webhook URL**: Una vez importado el workflow, obtendrás una URL de webhook que podrás usar para enviar POST requests.

4. **Formato del request**:
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Mi mensaje aquí"
}
```

5. **Canales de Slack**: Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu workspace de Slack.

Para importar este workflow en N8N:
1. Ve a la sección de workflows
2. Haz clic en "Import from file" o "Import from URL"
3. Pega este JSON o guárdalo como archivo .json e impórtalo