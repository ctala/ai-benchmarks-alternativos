# Tencent Hy3 — code_generation/n8n_workflow_json

- model_id: `tencent/hy3`
- success: True  | final: 7.52 | quality: 8.6
- latency_total: 207.412s | tokens_per_second: 61.7
- input_tokens: 139 | output_tokens: 12806
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los aspectos de la tarea con un JSON bien estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos de Slack.

## Entrada exacta (lo que recibió el modelo)

**user:**

Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow.


## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n. Este workflow incluye:

1. Un **Webhook** (POST) que recibe el JSON.
2. Un nodo **Set** para extraer `email` y `message`.
3. Un nodo de **OpenAI** que clasifica el mensaje.
4. Un nodo **Set** para limpiar la respuesta de la IA.
5. Un nodo **Switch** que enruta según la clasificación.
6. Tres nodos de **Slack** conectados a los canales correspondientes.

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "email",
              "type": "string",
              "value": "={{ $json.email }}"
            },
            {
              "id": "2",
              "name": "message",
              "type": "string",
              "value": "={{ $json.message }}"
            }
          ]
        }
      },
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [450, 300]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "model": "gpt-3.5-turbo",
        "prompt": "Clasifica el siguiente mensaje en una de estas tres categorías exactas: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con la palabra de la categoría, sin puntuación ni texto adicional.\n\nMensaje: {{ $json.message }}",
        "options": {
          "systemMessage": "Eres un clasificador de texto. Responde siempre con una sola palabra: 'soporte', 'ventas' o 'otro'."
        }
      },
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [650, 300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAi account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "category",
              "type": "string",
              "value": "={{ $json.choices[0].message.content.trim() }}"
            }
          ]
        }
      },
      "name": "Extract Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [850, 300]
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": false,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": false,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": false,
              "outputKey": "otro"
            }
          ]
        }
      },
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1050, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 150],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 300],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=📩 Nuevo mensaje de {{ $json.email }}:\n{{ $json.message }}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1250, 450],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
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
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "OpenAI Classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "Extract Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Category": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "versionId": "1"
}
```

### Notas importantes:
1. **Credenciales**: Antes de activar el workflow, debes configurar tus credenciales de OpenAI y Slack en n8n (reemplazando los IDs de credenciales si es necesario, o seleccionándolas desde la interfaz).
2. **Webhook**: El endpoint se generará en una URL similar a `https://tu-instancia-n8n.com/webhook/clasificar-mensaje`. Debes enviar un `POST` con `Content-Type: application/json` y un cuerpo como:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "No puedo acceder a mi cuenta"
   }
   ```
3. **Canales de Slack**: Asegúrate de que el bot de n8n tenga permisos para escribir en los canales `#support`, `#sales` y `#general`. Si usas IDs de canal en lugar de nombres, simplemente reemplaza el valor en el parámetro `channel` de los nodos de Slack.