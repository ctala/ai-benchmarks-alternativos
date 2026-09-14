# Gemini 3.8 Flash — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.55 | quality: 8.6
- latency_total: 19.644s | tokens_per_second: 167.4
- input_tokens: 115 | output_tokens: 3289
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para un flujo de trabajo de N8N que cumple con los requisitos especificados. La estructura es clara y organizada, facilitando su implementación. Aunque la profundidad es adecuada, podría haber incluido más detalles sobre la configuración de credenciales o manejo de errores para mejorar la utilidad práctica.

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

Aquí tienes el flujo completo en formato JSON listo para importar en N8N.

### Pasos para usarlo:
1. En N8N, crea un nuevo workflow, haz clic en los tres puntos (`...`) arriba a la derecha y selecciona **"Import from JSON"**.
2. Pega el JSON que está abajo.
3. Configura tus credenciales para los nodos de **OpenAI** y **Slack**.
4. Activa el workflow.

```json
{
  "name": "Clasificador de Mensajes con OpenAI a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-message",
        "responseMode": "onReceived",
        "responseData": "OK",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        0
      ],
      "id": "webhook-trigger",
      "name": "Webhook"
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador estricto de mensajes. Clasifica el mensaje del usuario exactamente en una de las siguientes tres categorías:\n- soporte\n- ventas\n- otro\n\nResponde ÚNICAMENTE con una de esas tres palabras en minúsculas, sin comillas, signos de puntuación ni texto adicional.",
              "role": "system"
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
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.4,
      "position": [
        240,
        0
      ],
      "id": "openai-classifier",
      "name": "Clasificador OpenAI",
      "credentials": {
        "openAiApi": {
          "id": "TUS_CREDENCIALES_OPENAI",
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
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
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
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        480,
        0
      ],
      "id": "switch-node",
      "name": "Switch Categoria"
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=🛠️ *Nuevo ticket de Soporte*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        780,
        -160
      ],
      "id": "slack-support",
      "name": "Slack #support",
      "credentials": {
        "slackApi": {
          "id": "TUS_CREDENCIALES_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo Lead de Ventas*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        780,
        0
      ],
      "id": "slack-sales",
      "name": "Slack #sales",
      "credentials": {
        "slackApi": {
          "id": "TUS_CREDENCIALES_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=💬 *Nuevo Mensaje General*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        780,
        160
      ],
      "id": "slack-general",
      "name": "Slack #general",
      "credentials": {
        "slackApi": {
          "id": "TUS_CREDENCIALES_SLACK",
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
            "node": "Clasificador OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador OpenAI": {
      "main": [
        [
          {
            "node": "Switch Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoria": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

### Ejemplo de Payload para enviar al Webhook (POST):
```json
{
  "email": "cliente@example.com",
  "message": "Hola, la aplicación me da un error 500 al intentar iniciar sesión."
}
```