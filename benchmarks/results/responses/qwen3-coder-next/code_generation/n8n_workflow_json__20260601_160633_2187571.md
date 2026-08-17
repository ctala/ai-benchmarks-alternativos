# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.05 | quality: 8.4
- latency_total: 30.416s | tokens_per_second: 66.2
- input_tokens: 123 | output_tokens: 2012
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del workflow de N8N. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o posibles errores comunes.

## Respuesta completa

Aquí tienes un workflow completo de **n8n** en formato JSON que cumple con todos tus requisitos:

- Se activa con un webhook POST
- Extrae `email` y `message` del body
- Usa el nodo de **OpenAI (Chat Completion)** para clasificar el mensaje
- Rutea el mensaje a canales de Slack según la clasificación (`soporte`, `ventas`, `otro`)

> ⚠️ **Requisitos previos**:
> - Tener configurada una credencial de **OpenAI** con una API key válida.
> - Tener configurada una credencial de **Slack Webhook** (o usar el nodo "Slack" con token bot).
> - Asegurarte de que los canales `#support`, `#sales`, y `#general` existan en tu workspace de Slack (o ajustar los nombres si es necesario).

---

```json
{
  "name": "Email Classifier to Slack",
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "path": "classify-email",
        "responseMode": "lastNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 200]
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            { "name": "email", "value": "={{ $json.email }}" },
            { "name": "message", "value": "={{ $json.message }}" }
          ]
        }
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [450, 200]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas', o 'otro'. Responde solo con la categoría en minúsculas y sin puntos ni comillas."
          },
          {
            "role": "user",
            "content": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
          }
        ],
        "options": {}
      },
      "name": "OpenAI Chat",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [650, 200],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "My OpenAI"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "combinator": "and",
                "conditions": [
                  {
                    "id": "classification",
                    "leftValue": "={{ $json[0].text }}",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "rightValue": "soporte"
                    }
                  }
                ],
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                }
              },
              "name": "soporte",
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "combinator": "and",
                "conditions": [
                  {
                    "id": "classification",
                    "leftValue": "={{ $json[0].text }}",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "rightValue": "ventas"
                    }
                  }
                ],
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                }
              },
              "name": "ventas",
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "combinator": "and",
                "conditions": [
                  {
                    "id": "classification",
                    "leftValue": "={{ $json[0].text }}",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "rightValue": "otro"
                    }
                  }
                ],
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                }
              },
              "name": "otro",
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [850, 200]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📧 Nuevo mensaje de soporte:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "name": "Slack - Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 100],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "My Slack"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📧 Nuevo mensaje de ventas:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 200],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "My Slack"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📧 Nuevo mensaje no clasificado:\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 300],
      "credentials": {
        "slackApi": {
          "id": "1",
          "name": "My Slack"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
      "main": [
        [
          {
            "node": "OpenAI Chat",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat": {
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
      "soporte": [
        [
          {
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "ventas": [
        [
          {
            "node": "Slack - Sales",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "otro": [
        [
          {
            "node": "Slack - General",
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

### 🔧 Notas técnicas:

- **Nodo `OpenAI Chat`**: Usa `gpt-3.5-turbo` (puedes cambiarlo a `gpt-4` si tienes acceso).
- **Salida del modelo**: Se espera que el modelo devuelva **solo** una palabra: `"soporte"`, `"ventas"` o `"otro"` (sin comillas ni puntos). Esto es crítico para que el Switch funcione.
- **Credenciales**: Debes reemplazar `"id": "1"` y `"name": "My OpenAI"` / `"My Slack"` con las IDs reales de tus credenciales guardadas en n8n.
- **Manejo de errores**: Si el modelo falla o devuelve texto no válido, puedes añadir un nodo `IF` o `Function Item` para validar la salida antes del Switch.

¿Quieres que le añada un nodo de validación o manejo de errores (por ejemplo, si OpenAI falla)?