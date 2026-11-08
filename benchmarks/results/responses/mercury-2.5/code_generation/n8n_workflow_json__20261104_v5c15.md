# Mercury 2.5 — code_generation/n8n_workflow_json

- model_id: `inception/mercury-2.5`
- success: True  | final: 7.85 | quality: 8.0
- latency_total: 9.431s | tokens_per_second: 328.4
- input_tokens: 112 | output_tokens: 3097
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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



{
  "name": "Workflow Clasificacion Emails",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "email-input",
        "responseMode": "onReceived"
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "options": {
          "maxTokens": 10
        }
      },
      "id": "openai-node",
      "name": "AI Clasificador",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.1,
      "position": [
        470,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "openai-cred-id",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "name": "Soporte",
              "operation": "equals",
              "value1": "={{ $json.classification }}",
              "value2": "soporte"
            },
            {
              "name": "Ventas",
              "operation": "equals",
              "value1": "={{ $json.classification }}",
              "value2": "ventas"
            },
            {
              "name": "Otro",
              "operation": "equals",
              "value1": "={{ $json.classification }}",
              "value2": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2.2,
      "position": [
        690,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "content": "Nuevo mensaje de soporte:\nEmail: {{$json.body.email}}\nMensaje: {{$json.body.message}}\nCategoría: soporte",
        "options": {}
      },
      "id": "slack-support-node",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        910,
        100
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "slack-cred-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "content": "Nuevo lead de ventas:\nEmail: {{$json.body.email}}\nMensaje: {{$json.body.message}}\nCategoría: ventas",
        "options": {}
      },
      "id": "slack-sales-node",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        910,
        300
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "slack-cred-id",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "content": "Mensaje general:\nEmail: {{$json.body.email}}\nMensaje: {{$json.body.message}}\nCategoría: otro",
        "options": {}
      },
      "id": "slack-general-node",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        910,
        500
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "slack-cred-id",
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
            "node": "AI Clasificador",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Clasificador": {
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
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}