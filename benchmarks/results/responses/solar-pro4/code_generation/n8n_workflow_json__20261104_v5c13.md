# Solar Pro 4 — code_generation/n8n_workflow_json

- model_id: `upstage/solar-pro4`
- success: True  | final: 7.96 | quality: 8.6
- latency_total: 26.633s | tokens_per_second: 71.5
- input_tokens: 174 | output_tokens: 1903
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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
  "name": "Webhook Classifier -> Slack Routing",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "tu_webhook_id_aqui"
    },
    {
      "parameters": {
        "operation": "execute",
        "model": {
          "authentication": "openaiApi",
          "resource": "chat"
        },
        "messages": {
          "message": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Devuelve SOLO la categoría.\n\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
        },
        "options": {
          "responseFormat": "text"
        }
      },
      "id": "ai-classifier",
      "name": "Classify with AI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openaiApi": {
          "id": "tu_credencial_openai",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.output }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "if-soporte",
      "name": "Si Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📩 Nuevo mensaje de Soporte\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-soporte",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "tu_credencial_slack",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.output }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "if-ventas",
      "name": "Si Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        450
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "📩 Nuevo mensaje de Ventas\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-ventas",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        350
      ],
      "credentials": {
        "slackApi": {
          "id": "tu_credencial_slack",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $json.output === 'soporte' }}",
              "operation": "not"
            },
            {
              "value1": "={{ $json.output === 'ventas' }}",
              "operation": "not"
            }
          ]
        }
      },
      "id": "if-otro",
      "name": "Si Otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        600
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📩 Nuevo mensaje General\nDe: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-otro",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        850,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "tu_credencial_slack",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Classify with AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify with AI": {
      "main": [
        [
          {
            "node": "Si Soporte",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Si Soporte": {
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
            "node": "Si Ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Si Ventas": {
      "main": [
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Si Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Si Otro": {
      "main": [
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
  "meta": {
    "templateId": "workflow-template-classifier"
  },
  "settings": {
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "executeInExistingProcess": false,
    "timeout": 30,
    "retryOnFail": false,
    "maxConcurrency": 1,
    "continueOnFail": false
  },
  "staticData": null,
  "tags": [],
  "updatedAt": "2024-01-15T12:00:00.000Z",
  "versionId": "version-1",
  "id": "workflow-id-aqui",
  "pinData": {}
}
```

### Notas para configurar este workflow:

1. **Webhook**: Después de importar, ve a los settings del nodo "Webhook Trigger" para obtener la URL real del webhook.

2. **Credenciales**:
   - Configura las credenciales de OpenAI en el nodo "Classify with AI"
   - Configura las credenciales de Slack en los 3 nodos de Slack

3. **Prompt de IA**: El prompt está diseñado para que la IA devuelva solo la categoría. Si necesitas ajustar el comportamiento, modifica el campo "message" del nodo de OpenAI.

4. **Estructura**: El workflow usa 3 nodos "If" encadenados para enrutar según la clasificación. Alternativamente, podrías usar un único nodo "Switch" si prefieres una estructura más compacta.

5. **Testing**: Puedes probar el webhook con curl:
```bash
curl -X POST https://tu-n8n-url/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email": "test@ejemplo.com", "message": "Tengo un problema con mi cuenta"}'
```