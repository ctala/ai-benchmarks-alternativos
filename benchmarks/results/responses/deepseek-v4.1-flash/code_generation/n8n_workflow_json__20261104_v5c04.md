# DeepSeek V4.1 Flash — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 6.9 | quality: 7.2
- latency_total: 24.966s | tokens_per_second: 154.7
- input_tokens: 152 | output_tokens: 3862
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

```json
{
  "name": "Clasificador de mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [220, 400],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "field-2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [440, 400]
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
              "content": "=Eres un clasificador de mensajes. Clasifica el siguiente mensaje en UNA de estas tres categorías: \"soporte\", \"ventas\" o \"otro\".\n\nReglas:\n- \"soporte\": problemas técnicos, errores, incidencias, ayuda con el producto.\n- \"ventas\": consultas sobre precios, planes, compras, demos.\n- \"otro\": cualquier otra cosa.\n\nResponde ÚNICAMENTE con la palabra exacta de la categoría, en minúsculas, sin comillas ni texto adicional.\n\nMensaje: {{ $json.message }}",
              "role": "user"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [660, 400]
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
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
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Router por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 400]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=📩 *Nuevo mensaje de SOPORTE*\n*De:* {{ $('Extraer email y message').item.json.email }}\n*Mensaje:* {{ $('Extraer email y message').item.json.message }}\n*Clasificación IA:* {{ $json.message.content.trim() }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 240],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENTIAL_ID",
          "name": "Slack - Cuenta principal"
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
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*De:* {{ $('Extraer email y message').item.json.email }}\n*Mensaje:* {{ $('Extraer email y message').item.json.message }}\n*Clasificación IA:* {{ $json.message.content.trim() }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 400],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENTIAL_ID",
          "name": "Slack - Cuenta principal"
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
        "text": "=📬 *Nuevo mensaje OTRO*\n*De:* {{ $('Extraer email y message').item.json.email }}\n*Mensaje:* {{ $('Extraer email y message').item.json.message }}\n*Clasificación IA:* {{ $json.message.content.trim() }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 560],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_CREDENTIAL_ID",
          "name": "Slack - Cuenta principal"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
      "main": [
        [
          {
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Router por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por categoría": {
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
  "pinData": {},
  "meta": {
    "instanceId": "workflow-clasificador-ia"
  },
  "tags": []
}
```

## Cómo usarlo

1. **Importa el JSON** en n8n: `Workflows → Import from File` (o pega el JSON).
2. **Configura las credenciales**:
   - **OpenAI**: en el nodo `Clasificar con IA` selecciona tu credencial de OpenAI (o crea una nueva).
   - **Slack**: en los tres nodos de Slack, reemplaza `REEMPLAZA_CON_TU_CREDENTIAL_ID` por el ID real de tu credencial, o simplemente ábrelos y selecciona la credencial desde el dropdown.
3. **Ajusta los canales** (`#support`, `#sales`, `#general`) al nombre real de tus canales de Slack. Si tu workspace requiere IDs en vez de nombres, cambia `"mode": "name"` a `"mode": "id"` y pon el ID del canal.
4. **Activa el workflow** y haz un POST de prueba:

```bash
curl -X POST https://TU-INSTANCIA.n8n.cloud/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"No puedo iniciar sesión en mi cuenta"}'
```

## Notas técnicas

- **Webhook**: la ruta `clasificar-mensaje` la puedes cambiar; el body llega en `$json.body`.
- **Clasificación**: el prompt fuerza al modelo a devolver **solo** la palabra (`soporte`/`ventas`/`otro`). El Switch hace `contains` en minúsculas para ser tolerante a variaciones.
- **Fallback**: cualquier respuesta no reconocida cae en la salida "extra" (tercera salida del Switch), que va a `#general`.
- Los nodos de Slack usan `$('Extraer email y message').item.json` para recuperar los datos originales, porque el nodo de OpenAI devuelve su propia estructura (`message.content`).