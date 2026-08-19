# Claude Sonnet 5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.19 | quality: 8.6
- latency_total: 60.077s | tokens_per_second: 131.5
- input_tokens: 175 | output_tokens: 7898
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un JSON bien estructurado, aunque carece de detalles adicionales sobre la configuración de Slack y la gestión de errores.

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

Aquí tienes el workflow completo de n8n en formato JSON. Puedes importarlo directamente en n8n (menú **Import from File / Clipboard**).

```json
{
  "name": "Clasificación de mensajes con IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "1a111111-1111-1111-1111-111111111111",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "e1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "e2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "2a222222-2222-2222-2222-222222222222",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de atención al cliente. Clasifica el mensaje del usuario en UNA sola palabra: 'soporte', 'ventas' u 'otro'. Responde únicamente con esa palabra en minúsculas, sin puntuación ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "3a333333-3333-3333-3333-333333333333",
      "name": "Clasificar Mensaje con IA",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.6,
      "position": [680, 300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAi account"
        }
      }
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "p1",
              "name": "classification",
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "type": "string"
            },
            {
              "id": "p2",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "p3",
              "name": "originalMessage",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "4a444444-4444-4444-4444-444444444444",
      "name": "Procesar Clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [900, 300]
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
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
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
              "outputKey": "Soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
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
              "outputKey": "Ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": "2"
        }
      },
      "id": "5a555555-5555-5555-5555-555555555555",
      "name": "Enrutar por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=📩 *Nuevo mensaje - Soporte*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.originalMessage }}",
        "otherOptions": {}
      },
      "id": "6a666666-6666-6666-6666-666666666666",
      "name": "Enviar a Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 140],
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
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo mensaje - Ventas*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.originalMessage }}",
        "otherOptions": {}
      },
      "id": "7a777777-7777-7777-7777-777777777777",
      "name": "Enviar a Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 300],
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
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📨 *Nuevo mensaje - Otro*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.originalMessage }}",
        "otherOptions": {}
      },
      "id": "8a888888-8888-8888-8888-888888888888",
      "name": "Enviar a Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 460],
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
          { "node": "Extraer Campos", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          { "node": "Clasificar Mensaje con IA", "type": "main", "index": 0 }
        ]
      ]
    },
    "Clasificar Mensaje con IA": {
      "main": [
        [
          { "node": "Procesar Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Procesar Clasificación": {
      "main": [
        [
          { "node": "Enrutar por Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Enrutar por Clasificación": {
      "main": [
        [
          { "node": "Enviar a Soporte", "type": "main", "index": 0 }
        ],
        [
          { "node": "Enviar a Ventas", "type": "main", "index": 0 }
        ],
        [
          { "node": "Enviar a Otro", "type": "main", "index": 0 }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "versionId": "1"
}
```

### Notas importantes antes de usarlo

1. **Credenciales**: reemplaza `OPENAI_CREDENTIAL_ID` y `SLACK_CREDENTIAL_ID` con las credenciales reales que configures en tu instancia de n8n (o simplemente selecciónalas desde la UI después de importar).

2. **Body del webhook**: el nodo `Webhook` recibe el payload en `$json.body`, por eso `Extraer Campos` usa `$json.body.email` y `$json.body.message`. Si tu cliente envía el JSON en la raíz (sin wrapper `body`), ajusta a `$json.email` / `$json.message`.

3. **Respuesta de OpenAI**: el nodo `n8n-nodes-base.openAi` (resource `chat`) devuelve el texto en `$json.message.content`. Si usas la versión con `@n8n/n8n-nodes-langchain.openAi` o cambia la versión del nodo, verifica el path exacto del output y ajusta la expresión en `Procesar Clasificación`.

4. **Robustez de la clasificación**: como el modelo puede devolver texto inesperado, el `Switch` tiene un **fallback** (`Otro`) por si la respuesta no coincide exactamente con "soporte" o "ventas".

5. **Canales de Slack**: asegúrate de que el bot/token de Slack tenga permisos (`chat:write`) y esté invitado a los canales `#support`, `#sales` y `#general`.

¿Quieres que agregue también una respuesta HTTP personalizada al webhook (por ejemplo, confirmando recepción) o un manejo de errores (try/catch) para el nodo de OpenAI?