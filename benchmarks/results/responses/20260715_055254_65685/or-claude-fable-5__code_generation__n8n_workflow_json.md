# Claude Fable 5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 5.88 | quality: 7.2
- latency_total: 39.227s | tokens_per_second: 99.5
- input_tokens: 175 | output_tokens: 3905
- judge_score: 3.0 | justificación: 

## Respuesta completa

# Workflow N8N: Clasificador de Mensajes con IA

Aquí tienes el JSON completo del workflow. Puedes importarlo directamente en n8n con **Import from File/Clipboard**:

```json
{
  "name": "Clasificador de Mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "webhookId": "clasificar-mensaje"
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
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 0]
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
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en una de estas tres categorias exactas: soporte, ventas, otro. Responde UNICAMENTE con una de esas tres palabras en minusculas, sin puntuacion ni texto adicional."
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
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 0],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENTIAL_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "field-classification",
              "name": "classification",
              "value": "={{ $json.message.content.toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "field-email-pass",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "field-message-pass",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Preparar Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [660, 0]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict",
                  "version": 2
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
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict",
                  "version": 2
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
              "outputKey": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "otro"
        }
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Switch Clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [880, 0]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:wrench: *Nuevo mensaje de SOPORTE*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack - Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, -160],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENTIAL_ID",
          "name": "Slack Account"
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
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 0],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENTIAL_ID",
          "name": "Slack Account"
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
        "text": "=:speech_balloon: *Nuevo mensaje (OTRO)*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1120, 160],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENTIAL_ID",
          "name": "Slack Account"
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
            "node": "Preparar Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar Datos": {
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
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
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

## Notas de configuración

1. **Credenciales**: Reemplaza `REEMPLAZAR_CON_TU_CREDENTIAL_ID` con tus credenciales reales de OpenAI y Slack (o simplemente selecciónalas desde la UI de n8n tras importar).

2. **Webhook URL**: Una vez activo, el endpoint será:
   ```
   POST https://tu-instancia-n8n.com/webhook/clasificar-mensaje
   ```

3. **Payload de prueba**:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Mi aplicación no carga desde ayer, necesito ayuda urgente"
   }
   ```

4. **Robustez**: El nodo "Preparar Datos" aplica `.toLowerCase().trim()` a la respuesta de OpenAI y el Switch tiene un **fallback a #general**, así que si el modelo responde algo inesperado, el mensaje nunca se pierde.

5. **Temperatura 0**: Configurada en el nodo OpenAI para que la clasificación sea determinista y consistente.

6. **Slack Bot**: Asegúrate de que tu bot de Slack esté invitado a los tres canales (`#support`, `#sales`, `#general`) con el scope `chat:write`.