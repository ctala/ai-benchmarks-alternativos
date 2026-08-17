# GLM 5 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5`
- success: True  | final: 7.13 | quality: 8.32
- latency_total: 112.494s | tokens_per_second: 39.9
- input_tokens: 119 | output_tokens: 4483
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el código JSON completo para importar directamente en N8N. Este flujo implementa la lógica que solicitaste: recibe un webhook, clasifica con IA y enruta a Slack.

### Instrucciones previas:
1.  Copia el código de abajo.
2.  En N8N, haz clic en el menú de los tres puntos (esquina superior derecha) -> **Import from File** (o pegar el código).
3.  **Importante:** Deberás configurar tus credenciales de **OpenAI** y **Slack** en los nodos correspondientes después de importar el flujo, ya que por seguridad no se incluyen en el JSON.

### Código JSON del Workflow

```json
{
  "name": "Clasificacion IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook-clasificador",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000001",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        380,
        240
      ],
      "webhookId": "b1c1e1c1-0000-4000-8000-000000000001"
    },
    {
      "parameters": {
        "mode": "raw",
        "jsonOutput": "={\n  \"email\": \"{{ $json.body.email }}\",\n  \"message\": \"{{ $json.body.message }}\"\n}",
        "options": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000002",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [
        600,
        240
      ]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un asistente de clasificación. Tu trabajo es leer un mensaje y clasificarlo en una de tres categorías: 'soporte', 'ventas' o 'otro'. Responde UNICAMENTE con la palabra de la categoría en minúsculas, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000003",
      "name": "OpenAI - Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        820,
        240
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_DE_CREDENCIAL_OPENAI",
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "type": "string"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "type": "string"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": true,
              "outputKey": "ventas"
            }
          ],
          "fallbackOutput": {
            "type": "extra",
            "outputName": "otro"
          }
        },
        "options": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000004",
      "name": "Switch - Ruta",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        1040,
        240
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=Nuevo ticket de SOPORTE:\nDe: {{ $('Extraer Datos').item.json.email }}\nMensaje: {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000005",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1280,
        120
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=Nuevo lead de VENTAS:\nDe: {{ $('Extraer Datos').item.json.email }}\nMensaje: {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000006",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1280,
        240
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=Mensaje genérico recibido:\nDe: {{ $('Extraer Datos').item.json.email }}\nMensaje: {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000007",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1280,
        360
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={ \"status\": \"ok\", \"classification\": \"{{ $('OpenAI - Clasificar').item.json.message.content }}\" }",
        "options": {}
      },
      "id": "b1c1e1c1-0000-4000-8000-000000000008",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [
        1500,
        240
      ]
    }
  ],
  "connections": {
    "Webhook POST": {
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
            "node": "OpenAI - Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificar": {
      "main": [
        [
          {
            "node": "Switch - Ruta",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Ruta": {
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
    },
    "Slack - Soporte": {
      "main": [
        [
          {
            "node": "Responder Webhook",
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
            "node": "Responder Webhook",
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
            "node": "Responder Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Cómo funciona el flujo:

1.  **Webhook POST**: Escucha en la ruta `/webhook-clasificador`. Espera un JSON con `email` y `message`.
2.  **Extraer Datos**: Aísla los campos del body para usarlos fácilmente en los pasos siguientes.
3.  **OpenAI - Clasificar**: Envía el mensaje a GPT-3.5 con un "System Prompt" estricto que le ordena responder solo con una de las tres categorías (`soporte`, `ventas`, `otro`).
4.  **Switch - Ruta**: Evalúa la respuesta de la IA.
    *   Si el texto es "soporte" -> Sale por la salida 0.
    *   Si el texto es "ventas" -> Sale por la salida 1.
    *   Si no coincide con ninguna (o es "otro") -> Sale por la salida "Fallback" (otro).
5.  **Slack Nodes**: Cada nodo envía el mensaje al canal correspondiente (`#support`, `#sales`, `#general`) recuperando los datos originales del nodo "Extraer Datos".
6.  **Responder Webhook**: Devuelve un status 200 OK al cliente que hizo la petición inicial para confirmar que todo funcionó.