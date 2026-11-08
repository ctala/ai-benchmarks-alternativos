# Kimi K2.5 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.15 | quality: 8.6
- latency_total: 300.389s | tokens_per_second: 31.2
- input_tokens: 132 | output_tokens: 9374
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del workflow de N8N, y está claramente organizada y fácil de entender, lo que la hace útil para un emprendedor.

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

Aquí tienes el workflow completo en formato JSON listo para importar en N8N. 

**Importante:** Recuerda configurar tus credenciales de **OpenAI** y **Slack** después de importarlo (el workflow usa placeholders).

```json
{
  "name": "Clasificador IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasifica-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "11111111-1111-1111-1111-111111111111",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "clasifica-mensaje"
    },
    {
      "parameters": {
        "mode": "manual",
        "fields": {
          "values": [
            {
              "name": "email",
              "type": "string",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "type": "string",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "22222222-2222-2222-2222-222222222222",
      "name": "Extract Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [
        450,
        300
      ]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "modelId": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el texto del usuario en exactamente una palabra: soporte, ventas u otro. Responde únicamente la palabra, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "simplify": true
        }
      },
      "id": "33333333-3333-3333-3333-333333333333",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CRED_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "manual",
        "fields": {
          "values": [
            {
              "name": "email",
              "type": "string",
              "value": "={{ $('Extract Data').item.json.email }}"
            },
            {
              "name": "message",
              "type": "string",
              "value": "={{ $('Extract Data').item.json.message }}"
            },
            {
              "name": "category",
              "type": "string",
              "value": "={{ $json.content.trim().toLowerCase() }}"
            }
          ]
        },
        "options": {}
      },
      "id": "44444444-4444-4444-4444-444444444444",
      "name": "Parse Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "rules": [
            {
              "conditions": [
                {
                  "id": "cond-soporte",
                  "leftValue": "={{ $json.category }}",
                  "operator": {
                    "type": "string",
                    "operation": "equals"
                  },
                  "rightValue": "soporte"
                }
              ],
              "output": 0
            },
            {
              "conditions": [
                {
                  "id": "cond-ventas",
                  "leftValue": "={{ $json.category }}",
                  "operator": {
                    "type": "string",
                    "operation": "equals"
                  },
                  "rightValue": "ventas"
                }
              ],
              "output": 1
            },
            {
              "conditions": [
                {
                  "id": "cond-otro",
                  "leftValue": "={{ $json.category }}",
                  "operator": {
                    "type": "string",
                    "operation": "equals"
                  },
                  "rightValue": "otro"
                }
              ],
              "output": 2
            }
          ]
        },
        "options": {}
      },
      "id": "55555555-5555-5555-5555-555555555555",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#support",
        "text": "🛠️ *Nuevo ticket de Soporte*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "66666666-6666-6666-6666-666666666666",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#sales",
        "text": "💰 *Nuevo lead de Ventas*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "77777777-7777-7777-7777-777777777777",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channel": "#general",
        "text": "📧 *Nuevo mensaje (Otro)*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {}
      },
      "id": "88888888-8888-8888-8888-888888888888",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CRED_ID",
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
            "node": "Extract Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Data": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
      "main": [
        [
          {
            "node": "Parse Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Classification": {
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
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": []
}
```

### Cómo funciona:
1. **Webhook**: Escucha peticiones `POST` en `/webhook/clasifica-mensaje` esperando un JSON con `email` y `message`.
2. **Extract Data**: Normaliza los datos del body para usarlos fácilmente en los siguientes nodos.
3. **OpenAI**: Envía el mensaje a GPT con un prompt de sistema que fuerza a responder **solo** una palabra (`soporte`, `ventas` u `otro`). Con `simplify: true` obtenemos solo el texto plano.
4. **Parse Classification**: Limpia la respuesta de la IA (trim + lowercase) y la guarda en `category`, manteniendo también los datos originales.
5. **Switch**: Evalúa el campo `category` y deriva el flujo hacia una de las tres ramas.
6. **Slack**: Cada rama envía el mensaje al canal correspondiente con formato enriquecido.

### Prueba rápida (cURL):
```bash
curl -X POST https://TU-N8N/webhook/clasifica-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"Hola, mi factura tiene un error"}'
```

¡Listo para importar! 🚀