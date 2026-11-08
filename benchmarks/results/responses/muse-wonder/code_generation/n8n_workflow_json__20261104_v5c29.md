# Muse Wonder — code_generation/n8n_workflow_json

- model_id: `meta/muse-wonder`
- success: True  | final: 6.19 | quality: 7.2
- latency_total: 21.599s | tokens_per_second: 205.7
- input_tokens: 122 | output_tokens: 4444
- judge_score: 3.0 | justificación: La respuesta proporciona un workflow básico que cumple con los requisitos, pero carece de detalles completos para la configuración de Slack y no incluye la lógica para enviar mensajes a diferentes canales basados en la clasificación.

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

Aquí tienes un workflow de n8n completo e importable. Solo tendrás que configurar tus credenciales de OpenAI y Slack después de importarlo.

### JSON del Workflow

```json
{
  "name": "Clasificador de Mensajes - Webhook + OpenAI + Slack",
  "nodes": [
    {
      "parameters": {
        "content": "## 1. Webhook POST\nRecibe un JSON con:\n```json\n{\n  \"email\": \"usuario@ejemplo.com\",\n  \"message\": \"Necesito ayuda con mi cuenta\"\n}\n```",
        "height": 220,
        "width": 320,
        "color": 4
      },
      "id": "sticky-webhook",
      "name": "Nota Webhook",
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        -80,
        180
      ]
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "a1b2c3d4-1111-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        420
      ],
      "webhookId": "a1b2c3d4-1111-4000-8000-000000000099"
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
      "id": "a1b2c3d4-2222-4000-8000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        240,
        420
      ]
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
              "content": "Clasifica el mensaje en una sola palabra: soporte, ventas u otro.\n\n- soporte: problemas técnicos, errores, ayuda, acceso, bugs.\n- ventas: precios, planes, comprar, contratar, cotización, información comercial.\n- otro: cualquier otro tema.\n\nResponde SOLO con la palabra en minúsculas, sin puntuación ni explicación."
            },
            {
              "role": "user",
              "content": "=Mensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "a1b2c3d4-3333-4000-8000-000000000003",
      "name": "OpenAI - Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2,
      "position": [
        480,
        420
      ],
      "credentials": {
        "openAiApi": {
          "id": null,
          "name": "OpenAi account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "assign-classification",
              "name": "classification",
              "value": "={{ ($json.message.content || $json.text || '').toLowerCase().trim().replace(/[^a-z]/g, '') }}",
              "type": "string"
            },
            {
              "id": "assign-email-2",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "assign-message-2",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-4444-4000-8000-000000000004",
      "name": "Normalizar Clasificacion",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        720,
        420
      ]
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
                    "leftValue": "={{ $json.classification }}",
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
                    "leftValue": "={{ $json.classification }}",
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
                    "id": "cond-otro",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
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
              "outputKey": "otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "a1b2c3d4-5555-4000-8000-000000000005",
      "name": "Switch por Clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        960,
        420
      ]
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
        "text": "=🛠️ *Nuevo mensaje de SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-6666-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1220,
        240
      ],
      "credentials": {
        "slackApi": {
          "id": null,
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
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-7777-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1220,
        420
      ],
      "credentials": {
        "slackApi": {
          "id": null,
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
        "text": "=📌 *Nuevo mensaje - OTRO*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-8888-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        1220,
        600
      ],
      "credentials": {
        "slackApi": {
          "id": null,
          "name": "Slack account"
        }
      }
    }
  ],
  "pinData": {},
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
            "node": "Normalizar Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Clasificacion": {
      "main": [
        [
          {
            "node": "Switch por Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por Clasificacion": {
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "a1b2c3d4-9999-4000-8000-000000000009",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```

### Cómo usarlo

1.  En n8n ve a **Workflows > Import from File** (o pega el JSON con `Ctrl+V` en el canvas).
2.  Configura las credenciales:
    *   **OpenAI - Clasificar:** selecciona tu API Key de OpenAI.
    *   **Slack #support / #sales / #general:** selecciona tu credencial de Slack (el bot debe estar invitado a los 3 canales).
3.  Activa el workflow.

### Prueba con cURL

```bash
curl -X POST https://TU-N8N/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"No puedo iniciar sesión, me da error 500"}'
```

Ese ejemplo se clasifica como `soporte` y llegará a **#support**.