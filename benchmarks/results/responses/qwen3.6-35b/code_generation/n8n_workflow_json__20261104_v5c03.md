# Qwen 3.6 35B base (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 7.52 | quality: 8.6
- latency_total: 103.375s | tokens_per_second: 72.2
- input_tokens: 101 | output_tokens: 7463
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los pasos necesarios para el flujo de trabajo de N8N. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales y manejo de errores.

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



Aquí tienes el workflow completo en formato JSON listo para importar en n8n. Solo debes copiarlo, guardarlo como `workflow.json` e importarlo desde la interfaz de n8n (`⋮` → `Import from File`).

```json
{
  "name": "Webhook AI Classification to Slack",
  "nodes": [
    {
      "parameters": {
        "path": "classify-message",
        "httpMethod": "POST",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "webhook-123",
      "triggerWhenEmpty": true
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "resource": "chat",
        "messages": "={{ [ { \"role\": \"system\", \"content\": \"Classify the following message into one of these three categories: soporte, ventas, otro. Return ONLY the category name in lowercase.\" }, { \"role\": \"user\", \"content\": $json.message } ] }}"
      },
      "id": "openai-classifier",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 4,
      "position": [470, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CRED_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const content = $input.item.json.choices?.[0]?.message?.content || \"\";\nreturn { json: { ...$input.item.json, classification: content.trim().toLowerCase() } };"
      },
      "id": "code-extract",
      "name": "Extract Classification",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [690, 300]
    },
    {
      "parameters": {
        "rules": {
          "conditions": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "string",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.classification }}",
              "operation": "string",
              "value2": "ventas"
            },
            {
              "value1": "={{ $json.classification }}",
              "operation": "string",
              "value2": "otro"
            }
          ],
          "otherOutput": "other"
        }
      },
      "id": "switch-route",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [910, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "channel": "#support",
        "message": "={{ \"📧 Email: \" + $json.email + \"\\n📝 Message: \" + $json.message + \"\\n🤖 Clasificación: \" + $json.classification }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1130, 150],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CRED_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "channel": "#sales",
        "message": "={{ \"📧 Email: \" + $json.email + \"\\n📝 Message: \" + $json.message + \"\\n🤖 Clasificación: \" + $json.classification }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1130, 300],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CRED_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "channel": "#general",
        "message": "={{ \"📧 Email: \" + $json.email + \"\\n📝 Message: \" + $json.message + \"\\n🤖 Clasificación: \" + $json.classification }}",
        "otherOptions": {}
      },
      "id": "slack-otro",
      "name": "Slack - Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1130, 450],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CRED_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "OpenAI Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classifier": {
      "main": [
        [
          {
            "node": "Extract Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Classification": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "saveDataErrorExecution": "all",
    "saveDataSuccessExecution": "all",
    "executionTimeout": 3600,
    "timezone": "Europe/Madrid"
  },
  "id": "workflow-ai-slack-route",
  "active": false,
  "versionId": "1",
  "meta": {
    "instanceId": "your-instance-id"
  },
  "tags": []
}
```

### 📋 Pasos para activarlo:
1. **Importar**: Ve a tu n8n → `⋮` → `Import from File