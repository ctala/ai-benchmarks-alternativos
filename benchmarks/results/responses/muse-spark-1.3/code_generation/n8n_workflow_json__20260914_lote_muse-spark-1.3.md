# Muse Spark 1.3 — code_generation/n8n_workflow_json

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 6.13 | quality: 6.72
- latency_total: 31.846s | tokens_per_second: 155.4
- input_tokens: 121 | output_tokens: 4948
- judge_score: 2.8 | justificación: 

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

Aquí tienes un workflow listo para importar en n8N (`Import from JSON`):

> Necesitarás configurar 2 credenciales después de importar:
> 1. **OpenAI account** en el nodo `OpenAI Chat Model`
> 2. **Slack OAuth / Access Token** en los 3 nodos de Slack

```json
{
  "name": "Webhook Clasificacion a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "contacto",
        "responseMode": "whenReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "a1b2c3d4-webhook-post",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "contacto-webhook-id"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "assign-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b2c3d4e5-extract-data",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 0]
    },
    {
      "parameters": {
        "model": {
          "__rl__": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "c3d4e5f6-openai-model",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [420, 200],
      "credentials": {
        "openAiApi": {
          "id": null,
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una sola palabra: \"soporte\", \"ventas\" u \"otro\".\n\nCriterios:\n- soporte: problemas, errores, ayuda técnica, bugs, cuenta bloqueada\n- ventas: precios, planes, comprar, demo, contratación, cotización\n- otro: cualquier otra cosa\n\nMensaje: {{ $json.message }}\n\nResponde ÚNICAMENTE con una palabra en minúsculas: soporte, ventas u otro.",
        "options": {}
      },
      "id": "d4e5f6g7-classify-llm",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.4,
      "position": [440, 0]
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
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.text.trim().toLowerCase() }}",
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
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.text.trim().toLowerCase() }}",
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
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-otro",
                    "leftValue": "={{ $json.text.trim().toLowerCase() }}",
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
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "general"
        }
      },
      "id": "e5f6g7h8-switch-router",
      "name": "Switch Clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [660, 0]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "channel": "#support",
        "text": "=📩 *Nuevo ticket de SOPORTE*\nEmail: {{ $('Extraer email y message').item.json.email }}\nMensaje: {{ $('Extraer email y message').item.json.message }}\nClasificación IA: {{ $json.text }}",
        "otherOptions": {}
      },
      "id": "f6g7h8i9-slack-support",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [880, -160],
      "webhookId": "",
      "credentials": {
        "slackApi": {
          "id": null,
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "channel": "#sales",
        "text": "=💰 *Nuevo lead de VENTAS*\nEmail: {{ $('Extraer email y message').item.json.email }}\nMensaje: {{ $('Extraer email y message').item.json.message }}\nClasificación IA: {{ $json.text }}",
        "otherOptions": {}
      },
      "id": "g7h8i9j0-slack-sales",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [880, 0],
      "credentials": {
        "slackApi": {
          "id": null,
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "channel": "#general",
        "text": "=💬 *Nuevo mensaje GENERAL*\nEmail: {{ $('Extraer email y message').item.json.email }}\nMensaje: {{ $('Extraer email y message').item.json.message }}\nClasificación IA: {{ $json.text }}",
        "otherOptions": {}
      },
      "id": "h8i9j0k1-slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [880, 160],
      "credentials": {
        "slackApi": {
          "id": null,
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
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
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Clasificar con IA",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Switch Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Clasificacion": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {}
}
```

**Cómo probarlo:**
1. Activa el workflow, copia la `Production URL` del nodo `Webhook POST` (ej: `.../webhook/contacto`)
2. Haz un POST:
```bash
curl -X POST https://tu-n8n.com/webhook/contacto \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@test.com", "message":"Quiero saber el precio del plan pro"}'
```
3. Debería llegar a `#sales`.