# Kimi K3 — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 5.8 | quality: 7.2
- latency_total: 232.921s | tokens_per_second: 44.6
- input_tokens: 209 | output_tokens: 10380
- judge_score: 3.0 | justificación: 

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

Aquí tienes el workflow completo, listo para importar en n8n (Workflows → Import from Clipboard):

```json
{
  "name": "Clasificador de Mensajes IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "f7a3c2d1-4b5e-4c6a-9d8e-1f2a3b4c5d6e",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "c1d2e3f4-a5b6-4c7d-8e9f-0a1b2c3d4e5f"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "GPT-4O-MINI"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de una empresa. Clasifica el mensaje del usuario en UNA de estas categorías:\n- soporte: problemas técnicos, errores, ayuda con el producto\n- ventas: preguntas sobre precios, planes, contratación, demos\n- otro: cualquier otro tema\n\nResponde ÚNICAMENTE con una palabra: soporte, ventas u otro. Sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "=Email del remitente: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [700, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ ($json.message.content || '').toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "name": "filter.operator.equals"
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ ($json.message.content || '').toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "name": "filter.operator.equals"
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
          "fallbackOutput": "extra",
          "renameFallbackOutput": "otro"
        }
      },
      "id": "a5b6c7d8-e9f0-1a2b-3c4d-5e6f7a8b9c0d",
      "name": "Switch Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [940, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "messageType": "text",
        "text": "=🆘 *Nuevo mensaje de SOPORTE*\n*De:* {{ $('Extraer Datos').item.json.email }}\n*Mensaje:* {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "6d7e8f9a-0b1c-2d3e-4f5a-6b7c8d9e0f1a",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1200, 140],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL",
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
        "messageType": "text",
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*De:* {{ $('Extraer Datos').item.json.email }}\n*Mensaje:* {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1200, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL",
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
        "messageType": "text",
        "text": "=📨 *Nuevo mensaje (OTRO)*\n*De:* {{ $('Extraer Datos').item.json.email }}\n*Mensaje:* {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "9a0b1c2d-e3f4-5a6b-7c8d-9e0f1a2b3c4d",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1200, 460],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENCIAL",
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
            "node": "Switch Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Clasificación": {
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
  },
  "staticData": null,
  "pinData": {}
}
```

## Pasos después de importar

1. **Credenciales**: Asigna tu credencial de OpenAI en el nodo "Clasificar con OpenAI" y tu credencial de Slack en los 3 nodos de Slack.
2. **Canales de Slack**: Verifica que los canales `#support`, `#sales` y `#general` existan (o selecciónalos desde el dropdown de cada nodo).
3. **Activar** el workflow para que el webhook pase a modo producción.

## Cómo probarlo

```bash
curl -X POST https://tu-instancia-n8n.com/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email": "cliente@ejemplo.com", "message": "No puedo iniciar sesión en mi cuenta"}'
```

## Notas clave

- **El Switch usa fallback para "otro"**: si la IA devuelve algo inesperado, el mensaje cae en `#general` en lugar de perderse.
- **`temperature: 0` y `maxTokens: 10`**: fuerzan respuestas deterministas de una sola palabra, manteniendo el costo mínimo.
- Los nodos de Slack leen `email`/`message` desde el nodo "Extraer Datos" (`$('Extraer Datos').item.json...`), porque el nodo de OpenAI no preserva los campos de entrada en su output.
- Si quieres devolver una respuesta personalizada al llamador del webhook, cambia `responseMode` a `"responseNode"` y añade un nodo "Respond to Webhook" al final de cada rama.