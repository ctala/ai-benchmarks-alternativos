# Ling 3.0 Flash — code_generation/n8n_workflow_json

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 6.71 | quality: 6.92
- latency_total: 164.071s | tokens_per_second: 47.1
- input_tokens: 149 | output_tokens: 7722
- judge_score: 2.8 | justificación: 

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

Aquí tienes el JSON completo del workflow de N8N:

```json
{
  "name": "Email Classifier and Router",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "email-classifier",
        "responseMode": "responseNode"
      },
      "id": "b4e5f6a7-1111-4000-9000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        240,
        300
      ]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o"
        },
        "text": "=Eres un clasificador de mensajes de atención al cliente. Clasifica el siguiente mensaje en UNA SOLA de estas categorías: 'soporte', 'ventas', 'otro'. Responde únicamente con la palabra correspondiente, sin explicaciones ni texto adicional.\n\nMensaje a clasificar: {{ $json.message }}"
      },
      "id": "b4e5f6a7-2222-4000-9000-000000000002",
      "name": "Clasificar Mensaje",
      "type": "@n8n/n8n-nodes-langchain.openAiChatModel",
      "typeVersion": 1.1,
      "position": [
        480,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_API_CREDENTIAL",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "r": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "errorOutput": "nearestError"
                },
                "conditions": [
                  {
                    "id": "rule-soporte",
                    "leftValue": "={{ $json.text }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "errorOutput": "nearestError"
                },
                "conditions": [
                  {
                    "id": "rule-ventas",
                    "leftValue": "={{ $json.text }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "errorOutput": "nearestError"
                },
                "conditions": [
                  {
                    "id": "rule-otro",
                    "leftValue": "={{ $json.text }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "b4e5f6a7-3333-4000-9000-000000000003",
      "name": "Router por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        720,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=📧 *Nuevo mensaje de SOPORTE*\n👤 *De:* {{ $json.email }}\n📝 *Mensaje:* {{ $json.message }}\n🕐 *Hora:* {{ $now.format('yyyy-MM-dd HH:mm:ss') }}"
      },
      "id": "b4e5f6a7-4444-4000-9000-000000000004",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        980,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_API_CREDENTIAL",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=📧 *Nuevo mensaje de VENTAS*\n👤 *De:* {{ $json.email }}\n📝 *Mensaje:* {{ $json.message }}\n🕐 *Hora:* {{ $now.format('yyyy-MM-dd HH:mm:ss') }}"
      },
      "id": "b4e5f6a7-5555-4000-9000-000000000005",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        980,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_API_CREDENTIAL",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=📧 *Nuevo mensaje (OTRO)*\n👤 *De:* {{ $json.email }}\n📝 *Mensaje:* {{ $json.message }}\n🕐 *Hora:* {{ $now.format('yyyy-MM-dd HH:mm:ss') }}"
      },
      "id": "b4e5f6a7-6666-4000-9000-000000000006",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        980,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_API_CREDENTIAL",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Mensaje": {
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
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
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
  "pinData": {},
  "tags": []
}
```

---

### 📋 Resumen del flujo

| Paso | Nodo | Descripción |
|------|------|-------------|
| 1 | **Webhook** | Escucha peticiones POST en `/email-classifier` |
| 2 | **Clasificar Mensaje** (OpenAI Chat) | Envía el campo `message` a GPT-4o con un prompt para clasificarlo como `soporte`, `ventas` o `otro` |
| 3 | **Router por Categoría** (Switch) | Evalúa la respuesta de OpenAI y enruta a la rama correspondiente |
| 4a | **Slack - Soporte** | Envía a `#support` si la categoría es `soporte` |
| 4b | **Slack - Ventas** | Envía a `#sales` si la categoría es `ventas` |
| 4c | **Slack - General** | Envía a `#general` si la categoría es `otro` |

---

### ⚙️ Configuración necesaria antes de importar

1. **Credenciales OpenAI**: Crea una credencial de tipo *OpenAI API* en N8N con tu API key y asígnala al nodo "Clasificar Mensaje".
2. **Credenciales Slack**: Crea una credencial de tipo *Slack API* (con OAuth o token de bot) y asígnala a los tres nodos Slack.
3. **Canales de Slack**: Asegúrate de que los canales `#support`, `#sales` y `#general` existan y que el bot de Slack tenga permisos para publicar en ellos.
4. **Importante**: El campo `text` del nodo OpenAI usa `{{ $json.text }}` en el Switch. Si en tu versión de N8N la salida del Chat Model se almacena en otra ruta (por ejemplo `{{ $json.output }}`), ajusta la `leftValue` del Switch en consecuencia.