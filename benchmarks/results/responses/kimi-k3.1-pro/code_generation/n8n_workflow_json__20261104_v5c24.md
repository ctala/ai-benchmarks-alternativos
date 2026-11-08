# Kimi K3.1 Pro — code_generation/n8n_workflow_json

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.67 | quality: 8.4
- latency_total: 370.25s | tokens_per_second: 32.9
- input_tokens: 209 | output_tokens: 12178
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro en la extracción de datos, clasificación y envío a Slack. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack o manejo de errores.

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

Importa este JSON en n8n mediante **Workflows → Import from File/Clipboard**:

```json
{
  "name": "Clasificar mensajes con OpenAI y enviarlos a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1e2d3c4b-0001-4000-8000-000000000001",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        -1000,
        300
      ],
      "webhookId": "a1b2c3d4-1000-4000-8000-000000000001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body.email ?? '' }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body.message ?? '' }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "1e2d3c4b-0002-4000-8000-000000000002",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        -760,
        300
      ]
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
              "content": "Eres un clasificador de mensajes. Responde únicamente con una de estas tres palabras, en minúsculas y sin puntuación: soporte, ventas, otro. Usa 'soporte' para incidencias, errores, ayuda técnica o problemas con productos y servicios. Usa 'ventas' para consultas sobre precios, presupuestos, compras, contratación, demos o propuestas comerciales. Usa 'otro' para cualquier otro tema. No añadas explicaciones."
            },
            {
              "role": "user",
              "content": "=Mensaje a clasificar:\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "1e2d3c4b-0003-4000-8000-000000000003",
      "name": "OpenAI - Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        -520,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI - Configurar credencial"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const original = $('Extraer datos').item.json;\n\nconst raw =\n  $json.message?.content ??\n  $json.content ??\n  $json.text ??\n  $json.output ??\n  $json.choices?.[0]?.message?.content ??\n  '';\n\nconst value = String(raw).trim().toLowerCase();\nlet classification = 'otro';\n\nif (/\\bsoporte\\b/.test(value)) {\n  classification = 'soporte';\n} else if (/\\bventas\\b/.test(value)) {\n  classification = 'ventas';\n}\n\nreturn {\n  json: {\n    email: original.email,\n    message: original.message,\n    classification\n  }\n};"
      },
      "id": "1e2d3c4b-0004-4000-8000-000000000004",
      "name": "Normalizar clasificacion",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        -280,
        300
      ]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.classification }}",
        "rules": {
          "rules": [
            {
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "operation": "equal",
              "value2": "ventas"
            },
            {
              "operation": "equal",
              "value2": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "1e2d3c4b-0005-4000-8000-000000000005",
      "name": "Switch clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        -40,
        300
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
        "text": "=Nuevo mensaje clasificado como *soporte*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "1e2d3c4b-0006-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        240,
        80
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack - Configurar credencial"
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
        "text": "=Nuevo mensaje clasificado como *ventas*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "1e2d3c4b-0007-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        240,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack - Configurar credencial"
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
        "text": "=Nuevo mensaje clasificado como *otro*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "1e2d3c4b-0008-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        240,
        520
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack - Configurar credencial"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook POST": {
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
            "node": "Normalizar clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificacion": {
      "main": [
        [
          {
            "node": "Switch clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch clasificacion": {
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": []
}
```

Antes de activarlo:

1. Vuelve a seleccionar tus credenciales de **OpenAI** y **Slack** en los nodos correspondientes.
2. La aplicación de Slack necesita el permiso `chat:write` y el bot debe estar invitado a `#support`, `#sales` y `#general`. Si n8n no resuelve los nombres, sustitúyelos por los IDs de los canales.
3. Activa el workflow. El endpoint de producción será `/webhook/clasificar-email` y esperará un body como:

```json
{
  "email": "cliente@example.com",
  "message": "Necesito ayuda porque no puedo acceder a mi cuenta"
}
```