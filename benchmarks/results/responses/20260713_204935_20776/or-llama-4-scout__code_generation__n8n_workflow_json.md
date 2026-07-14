# Llama 4 Scout 17B — code_generation/n8n_workflow_json

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 6.53 | quality: 6.6
- latency_total: 30.001s | tokens_per_second: 42.1
- input_tokens: 124 | output_tokens: 1264
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de profundidad en la configuración del nodo de Slack y no completa el JSON, lo que afecta su utilidad práctica.

## Respuesta completa

Aquí te dejo el JSON del workflow de N8N que cumple con tus requisitos:
```json
{
  "name": "Clasificación de mensajes y envío a Slack",
  "nodes": [
    {
      "parameters": {
        "path": "/webhook"
      },
      "name": "Webhook",
      "type": "n8n-webhook",
      "typeVersion": 1,
      "position": 0
    },
    {
      "parameters": {
        "operation": "extract",
        "keys": [
          "email",
          "message"
        ]
      },
      "name": "Extraer campos",
      "type": "n8n-function",
      "typeVersion": 1,
      "position": 1,
      "inputs": {
        "main": [
          {
            "parameters": {
              "bodyParametersUi": {
                "parameter": [
                  {
                    "name": "body"
                  }
                ]
              }
            },
            "node": "Webhook",
            "type": "Webhook",
            "typeVersion": 1
          }
        ]
      }
    },
    {
      "parameters": {
        "model": "text-classification",
        "prompt": "Clasifica el mensaje como soporte, ventas o otro",
        "inputs": [
          {
            "text": "=$message"
          }
        ],
        "credentialType": "oai-user",
        "credentials": {
          "token": "YOUR_OPENAI_TOKEN"
        }
      },
      "name": "Clasificar mensaje",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": 2,
      "inputs": {
        "main": [
          {
            "parameters": {},
            "node": "Extraer campos",
            "type": "Function",
            "typeVersion": 1
          }
        ]
      }
    },
    {
      "parameters": {
        "channel": "",
        "message": "=$email: $message"
      },
      "name": "Enviar a Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": 3,
      "inputs": {
        "main": []
      },
      "outputs": {
        "main": []
      },
      "credentials": {
        "token": "YOUR_SLACK_TOKEN",
        "channel": "#support"
      },
      "conditions": {
        "json": [
          {
            "key": "classification",
            "operation": "equals",
            "value": "soporte"
          }
        ]
      }
    },
    {
      "parameters": {
        "channel": "",
        "message": "=$email: $message"
      },
      "name": "Enviar a Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": 4,
      "inputs": {
        "main": []
      },
      "outputs": {
        "main": []
      },
      "credentials": {
        "token": "YOUR_SLACK_TOKEN",
        "channel": "#sales"
      },
      "conditions": {
        "json": [
          {
            "key": "classification",
            "operation": "equals",
            "value": "ventas"
          }
        ]
      }
    },
    {
      "parameters": {
        "channel": "",
        "message": "=$email: $message"
      },
      "name": "Enviar a Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": 5,
      "inputs": {
        "main": []
      },
      "outputs": {
        "main": []
      },
      "credentials": {
        "token": "YOUR_SLACK_TOKEN",
        "channel": "#general"
      },
      "conditions": {
        "json": [
          {
            "key": "classification",
            "operation": "equals",
            "value": "otro"
          }
        ]
      }
    },
    {
      "parameters": {
        "classification": "={{ $classification }}"
      },
      "name": "Unir clasificación",
      "type": "n8n-function",
      "typeVersion": 1,
      "position": 6,
      "inputs": {
        "main": [
          {
            "parameters": {},
            "node": "Clasificar mensaje",
            "type": "OpenAI",
            "typeVersion": 1
          }
        ]
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        {
          "node": "Extraer campos",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Extraer campos": {
      "main": [
        {
          "node": "Clasificar mensaje",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Clasificar mensaje": {
      "main": [
        {
          "node": "Unir clasificación",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Unir clasificación": {
      "main": [
        {
          "node": "Enviar a Slack #support",
          "type": "main",
          "index": 0
        },
        {
          "node": "Enviar a Slack #sales",
          "type": "main",
          "index": 0
        },
        {
          "node": "Enviar a Slack #general",
          "type": "main",
          "index": 0
        }
      ]
    }
  }
}
```
Ten en cuenta que debes reemplazar `YOUR_OPENAI_TOKEN` y `YOUR_SLACK_TOKEN` con tus tokens de OpenAI y Slack respectivamente.

Espero que esto te ayude. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!