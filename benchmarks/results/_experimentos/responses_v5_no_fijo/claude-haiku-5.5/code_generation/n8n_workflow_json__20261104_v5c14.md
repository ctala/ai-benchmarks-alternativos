# Claude Haiku 5.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.86 | quality: 7.2
- latency_total: 21.152s | tokens_per_second: 268.7
- input_tokens: 177 | output_tokens: 5684
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de profundidad en la configuración de reglas para la clasificación y envío a Slack, y no incluye el nodo de Slack, lo que limita su utilidad práctica.

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

Aquí tienes el workflow completo. Puedes copiarlo y pegarlo en n8n con **Ctrl+V** sobre el lienzo.

```json
{
  "name": "Clasificador de mensajes a Slack con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "responseCode": 200,
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-800, 300],
      "webhookId": "a1b2c3d4-0001-4000-8000-000000000101"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "b1000001-0000-4000-8000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "b1000001-0000-4000-8000-000000000002",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "includeOtherFields": false,
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [-560, 300]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en una de estas categorías: soporte, ventas u otro. Responde ÚNICAMENTE con una de estas tres palabras en minúsculas: soporte, ventas, otro. No añadas nada más."
            },
            {
              "role": "user",
              "content": "=Mensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [-320, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID",
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
                    "id": "c1000001-0000-4000-8000-000000000001",
                    "leftValue": "={{ ($json.message?.content ?? $json.content ?? $json.text ?? '').toString().trim().toLowerCase() }}",
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
                    "id": "c1000001-0000-4000-8000-000000000002",
                    "leftValue": "={{ ($json.message?.content ?? $json.content ?? $json.text ?? '').toString().trim().toLowerCase() }}",
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
                    "id": "c1000001-0000-4000-8000-000000000003",
                    "leftValue": "={{ ($json.message?.content ?? $json.content ?? $json.text ?? '').toString().trim().toLowerCase() }}",
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
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Switch por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [-80, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "support",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje de soporte*\n*Email:* {{ $('Extraer datos').item.json.email }}\n*Mensaje:* {{ $('Extraer datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [180, 100],
      "webhookId": "a1b2c3d4-0005-4000-8000-000000000105",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "sales",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje de ventas*\n*Email:* {{ $('Extraer datos').item.json.email }}\n*Mensaje:* {{ $('Extraer datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [180, 300],
      "webhookId": "a1b2c3d4-0006-4000-8000-000000000106",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "general",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje general*\n*Email:* {{ $('Extraer datos').item.json.email }}\n*Mensaje:* {{ $('Extraer datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [180, 500],
      "webhookId": "a1b2c3d4-0007-4000-8000-000000000107",
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID",
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
            "node": "Extraer datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer datos": {
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
            "node": "Switch por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por categoría": {
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
  "active": false
}
```

## Pasos para configurarlo

1. **Credenciales:**
   - En **OpenAI**, crea una credencial de tipo `OpenAI API` con tu API key y asígnala al nodo *Clasificar con OpenAI*.
   - En **Slack**, crea una credencial de tipo `Slack API` (token de bot con permisos `chat:write` y `channels:read`) y asígnala a los tres nodos de Slack.
2. **Canales:** Asegúrate de que existan los canales `#support`, `#sales` y `#general`, y que el bot esté invitado a ellos (`/invite @nombre_del_bot`). Si tus canales tienen otros nombres, cambia el campo `value` de `channelId` en cada nodo de Slack.
3. **Activar:** Pulsa **Active** en el workflow. La URL de producción del webhook será algo como:
   `https://tu-instancia.n8n.cloud/webhook/clasificar-mensaje`
4. **Probar:**
   ```bash
   curl -X POST https://tu-instancia.n8n.cloud/webhook/clasificar-mensaje \
     -H "Content-Type: application/json" \
     -d '{"email": "cliente@ejemplo.com", "message": "No puedo iniciar sesión en mi cuenta"}'
   ```

## Notas

- **Ruta del texto de la IA:** La expresión del nodo Switch busca la respuesta en `message.content`, `content` o `text`, para cubrir las variaciones de salida del nodo de OpenAI según su versión. Si en tu versión de n8n la salida tiene otra estructura, ajusta esa expresión.
- **Respuestas inesperadas:** Si la IA devuelve algo distinto de `soporte`, `ventas` u `otro`, el mensaje no se enviará a ningún canal. Para cubrirlo, puedes añadir una cuarta salida en el Switch con la opción *Fallback Output* que la envíe a `#general`.
- **Modelo:** Usa `gpt-4o-mini` por coste y velocidad, que son suficientes para esta clasificación.