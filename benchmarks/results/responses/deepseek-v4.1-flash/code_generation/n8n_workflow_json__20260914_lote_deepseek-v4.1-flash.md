# DeepSeek V4.1 Flash — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.81 | quality: 8.6
- latency_total: 25.843s | tokens_per_second: 96.7
- input_tokens: 152 | output_tokens: 2500
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un workflow JSON adecuado para la tarea especificada, con claridad y utilidad práctica para un emprendedor.

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

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "1a2b3c4d-0001-0000-0000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [200, 300],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "1a2b3c4d-0002-0000-0000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [420, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el mensaje del usuario y responde ÚNICAMENTE con una de estas tres palabras en minúsculas: \"soporte\", \"ventas\" o \"otro\". No agregues explicaciones ni puntuación.\n\nReglas:\n- \"soporte\": problemas técnicos, errores, bugs, ayuda con el producto, incidencias.\n- \"ventas\": consultas de precios, planes, demos, compras, cotizaciones.\n- \"otro\": cualquier otro tema (feedback, saludos, spam, etc.)."
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
      "id": "1a2b3c4d-0003-0000-0000-000000000003",
      "name": "OpenAI - Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [640, 300],
      "credentials": {
        "openAiApi": {
          "id": "REPLACE_WITH_OPENAI_CREDENTIAL_ID",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
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
      "id": "1a2b3c4d-0004-0000-0000-000000000004",
      "name": "Switch - Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:rotating_light: *Nuevo mensaje de SOPORTE*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "1a2b3c4d-0005-0000-0000-000000000005",
      "name": "Slack - #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1140, 140],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_SLACK_CREDENTIAL_ID",
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
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "1a2b3c4d-0006-0000-0000-000000000006",
      "name": "Slack - #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1140, 300],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_SLACK_CREDENTIAL_ID",
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
        "text": "=:inbox_tray: *Nuevo mensaje OTRO*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Mensaje:* {{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "1a2b3c4d-0007-0000-0000-000000000007",
      "name": "Slack - #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1140, 460],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_SLACK_CREDENTIAL_ID",
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
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
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
            "node": "Switch - Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Clasificación": {
      "main": [
        [
          {
            "node": "Slack - #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - #general",
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
  "active": false,
  "versionId": "1",
  "tags": []
}
```

### Notas de uso

1. **Webhook**: Escucha en `POST /webhook/clasificar-mensaje`. El body esperado es:
   ```json
   { "email": "user@example.com", "message": "Tengo un error al iniciar sesión" }
   ```

2. **Credenciales a reemplazar**:
   - `REPLACE_WITH_OPENAI_CREDENTIAL_ID` → tu credencial de OpenAI.
   - `REPLACE_WITH_SLACK_CREDENTIAL_ID` → tu credencial de Slack (con permisos `chat:write` y acceso a los canales `#support`, `#sales`, `#general`).

3. **Nodo de IA**: Usa el nodo **OpenAI (LangChain)** con `gpt-4o-mini` y `temperature: 0` para que la clasificación sea determinista. El prompt del sistema fuerza a responder solo con una palabra.

4. **Switch**: Tres salidas — `soporte`, `ventas` y la salida *fallback* (`extra`) que captura todo lo demás (incluido "otro") y lo envía a `#general`.

5. **Canales de Slack**: Si tu workspace usa IDs en lugar de nombres, cambia `mode: "name"` por `mode: "id"` y pon los IDs (ej: `C01234ABCDE`).

6. **Importar**: En n8n → *Workflows* → *Import from clipboard* y pega el JSON.