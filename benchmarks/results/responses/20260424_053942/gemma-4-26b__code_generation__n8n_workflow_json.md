# Gemma 4 26B MoE (3.8B activos) — code_generation/n8n_workflow_json

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.91 | quality: 8.32
- latency_total: 32.903s | tokens_per_second: 62.2
- input_tokens: 128 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para que este workflow funcione, necesitarás tener configuradas tus credenciales de **OpenAI** y de **Slack** en tu instancia de n8n.

Aquí tienes el JSON completo. Puedes copiarlo y pegarlo directamente en tu lienzo de n8n.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificador-mensajes",
        "options": {}
      },
      "id": "7e4d3f1a-1234-4abc-8def-1234567890ab",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [400, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu única tarea es clasificar el mensaje del usuario en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Responde ÚNICAMENTE con la palabra de la categoría, sin puntos ni explicaciones."
            },
            {
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d",
      "name": "AI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [620, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENTIAL_ID_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.choices[0].message.content.toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.choices[0].message.content.toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            }
          ]
        },
        "fallbackOutput": "otro"
      },
      "id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "name": "Switch Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [840, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🚨 *Nuevo ticket de Soporte*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1100, 150],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nueva oportunidad de Ventas*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1100, 300],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📩 *Mensaje No Clasificado*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1100, 450],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
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
            "node": "AI Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Classifier": {
      "main": [
        [
          {
            "node": "Switch Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Classification": {
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
        ]
      ]
    }
  }
}
```

### Explicación del Workflow:

1.  **Webhook Node**: Configurado para recibir un `POST`. La URL que te proporcione n8n será donde debes enviar tus datos.
2.  **AI Classifier (OpenAI)**:
    *   Utiliza un "System Prompt" para forzar a la IA a que solo responda una palabra (`soporte`, `ventas` o `otro`). Esto es crucial para que el siguiente nodo no falle.
    *   Utiliza la temperatura `0` para que la respuesta sea determinista y no creativa.
3.  **Switch Classification**:
    *   Toma la respuesta de la IA.
    *   He aplicado `.toLowerCase().trim()` en la expresión para limpiar cualquier espacio en blanco o mayúsculas accidentales que la IA pudiera enviar.
    *   Tiene 3 salidas: si es "soporte", si es "ventas", y una salida por defecto (*fallback*) para "otro".
4.  **Slack Nodes**:
    *   He creado tres nodos de Slack independientes.
    *   Cada uno usa una expresión para recuperar los datos originales del Webhook (`$('Webhook').item.json.body.email`), permit