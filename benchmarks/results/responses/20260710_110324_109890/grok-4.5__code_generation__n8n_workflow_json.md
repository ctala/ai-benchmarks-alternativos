# Grok 4.5 — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.5`
- success: True  | final: 7.42 | quality: 8.6
- latency_total: 35.588s | tokens_per_second: 112.6
- input_tokens: 319 | output_tokens: 4006
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

```json
{
  "name": "Webhook Email Classifier to Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "message-classifier",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "message-classifier"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Debes clasificar el mensaje del usuario en EXACTAMENTE UNA de estas tres categorías: soporte, ventas, otro.\n\nReglas:\n- soporte: problemas técnicos, bugs, ayuda con producto, reclamaciones, tickets.\n- ventas: precios, demos, cotizaciones, interés comercial, compras.\n- otro: cualquier otra cosa (saludos, spam, preguntas generales, etc.).\n\nResponde ÚNICAMENTE con la palabra de la categoría en minúsculas y sin comillas, sin explicación ni puntuación. Ejemplo de respuesta válida: soporte"
            },
            {
              "role": "user",
              "content": "Email del remitente: {{ $json.body.email }}\n\nMensaje:\n{{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0.1,
          "maxTokens": 10
        },
        "requestOptions": {}
      },
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "name": "OpenAI Classify",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [500, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.trim().toLowerCase() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte"
            },
            {
              "value2": "ventas"
            },
            {
              "value2": "otro"
            }
          ]
        },
        "fallbackOutput": 3
      },
      "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
      "name": "Switch Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [760, 300]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=?📩 *Nuevo mensaje de Soporte*\n\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:*\n{{ $('Webhook').item.json.body.message }}\n\n_Clasificación: soporte_",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "d4e5f6a7-b8c9-0123-defa-234567890123",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1040, 120],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
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
        "text": "=?💰 *Nuevo mensaje de Ventas*\n\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:*\n{{ $('Webhook').item.json.body.message }}\n\n_Clasificación: ventas_",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "e5f6a7b8-c9d0-1234-efab-345678901234",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1040, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
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
        "text": "=?📝 *Nuevo mensaje (Otro)*\n\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:*\n{{ $('Webhook').item.json.body.message }}\n\n_Clasificación: otro_",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "f6a7b8c9-d0e1-2345-fabc-456789012345",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1040, 480],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
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
            "node": "OpenAI Classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classify": {
      "main": [
        [
          {
            "node": "Switch Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Classification": {
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
  "versionId": "1a2b3c4d-5e6f-7890-abcd-ef1234567890",
  "meta": {
    "templateCredsSetupCompleted": false,
    "instanceId": "n8n-instance"
  },
  "id": "workflow-email-classifier-slack",
  "tags": []
}
```

### Instrucciones de uso e importación

1. **Importar en n8n**:
   - Ve a *Workflows* → *Import from File* o pega el JSON (Ctrl+V en el editor).

2. **Configurar credenciales** (obligatorio):
   - **OpenAI**: Crea/selecciona una credencial de OpenAI API y asígnala al nodo `OpenAI Classify`.
   - **Slack**: Crea una credencial de Slack (Bot Token con scopes `chat:write` y acceso a los canales) y asígnala a los 3 nodos de Slack.

3. **Canales de Slack**:
   - Asegúrate de que el bot esté invitado a `#support`, `#sales` y `#general`.
   - Si prefieres IDs de canal en lugar de nombres, cambia el modo de `channelId` a “ID” y pon el ID real (ej. `C0123456789`).

4. **Activar el