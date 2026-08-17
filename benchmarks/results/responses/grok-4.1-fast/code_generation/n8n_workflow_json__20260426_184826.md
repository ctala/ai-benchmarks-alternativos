# Grok 4.1 Fast — code_generation/n8n_workflow_json

- model_id: `x-ai/grok-4.1-fast`
- success: True  | final: 7.02 | quality: 7.48
- latency_total: 22.682s | tokens_per_second: 173.7
- input_tokens: 270 | output_tokens: 3940
- judge_score: 3.2 | justificación: 

## Respuesta completa

```json
{
  "name": "Clasificador de Emails a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "email-classifier",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        240,
        300
      ],
      "webhookId": "random-webhook-id"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario como exactamente una de estas opciones: 'soporte', 'ventas' o 'otro'. Responde SOLO con esa palabra, sin texto adicional, explicaciones ni comillas."
            },
            {
              "role": "user",
              "content": "=Mensaje a clasificar: {{$json.body.message}}"
            }
          ]
        },
        "options": {}
      },
      "id": "2",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        460,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "clasificacion",
              "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
            },
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "3",
      "name": "Set Clasificacion",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        680,
        300
      ]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.clasificacion }}",
        "rules": {
          "values": [
            {
              "value2": "soporte",
              "output": 0
            },
            {
              "value2": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "4",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        900,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🆘 *SOPORTE*\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}",
        "otherOptions": {}
      },
      "id": "5",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1120,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💼 *VENTAS*\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}",
        "otherOptions": {}
      },
      "id": "6",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1120,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📩 *OTRO*\n\n**Email:** {{$json.email}}\n\n**Mensaje:** {{$json.message}}\n\n**Clasificación:** {{$json.clasificacion}}",
        "otherOptions": {}
      },
      "id": "7",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1120,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "text",
        "responseBody": "Mensaje clasificado y enviado a Slack correctamente.",
        "options": {}
      },
      "id": "8",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1340,
        300
      ]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Set Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Clasificacion": {
      "main": [
        [
          {
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
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
    },
    "Slack Support": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack Sales": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack General": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
  "triggerCount": 0,
  "updatedAt": "2024-01-01T00:00:00.000Z",
  "versionId": "1"
}
```

### Instrucciones para usar este JSON:
1. **Importa el JSON** en N8N (Workflows > Import from JSON).
2. **Configura credenciales**:
   - **OpenAI**: Crea una credencial "OpenAI API" con tu API key y reemplaza `YOUR_OPENAI_CREDENTIAL_ID`.
   - **Slack**: Crea una credencial "Slack API" (OAuth2 o Bot Token) y reemplaza `YOUR_SLACK_CREDENTIAL_ID`. Asegúrate de que el bot tenga permisos para postear en `#support`, `#sales` y `#general`.
3. **Activa el workflow**. El webhook estará disponible en `https://tu-n8n-instance/webhook/email-classifier`.
4. **Prueba**: Envía un POST con body `{ "email": "test@example.com", "message": "Quiero ayuda con mi cuenta" }`. Debería clasificarlo y enviarlo al canal correcto.
5. **Notas**:
   - El nodo Switch usa modo "Expression" con fallback para "otro".
   - Agregué un "Respond to Webhook" para cerrar la respuesta HTTP.
   - El prompt de OpenAI fuerza una respuesta exacta para robustez.
   - Ajusta canales, prompts o emojis según necesites.