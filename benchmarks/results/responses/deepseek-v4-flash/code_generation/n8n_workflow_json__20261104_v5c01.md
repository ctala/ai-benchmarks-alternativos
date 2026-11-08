# DeepSeek V4 Flash (OpenRouter) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.68 | quality: 8.0
- latency_total: 29.468s | tokens_per_second: 63.4
- input_tokens: 126 | output_tokens: 1869
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un uso adecuado de los nodos. Aunque la profundidad es moderada, la claridad y utilidad práctica son altas, lo que permite a un emprendedor implementar el workflow directamente.

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
  "name": "Classify and Route to Slack",
  "nodes": [
    {
      "parameters": {
        "path": "classify-message",
        "responseMode": "onReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "user",
              "content": "Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\". Mensaje: {{ $json.message }}"
            }
          ]
        },
        "options": {
          "maxTokens": 10,
          "temperature": 0
        }
      },
      "id": "openai",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "dataType": "json",
        "fieldName": "classification",
        "expression": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
      },
      "id": "extractClassification",
      "name": "Extract Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [650, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.classification }}",
              "operation": "equal",
              "value2": "soporte"
            }
          ]
        }
      },
      "id": "switch",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [850, 300],
      "parameters": {
        "dataType": "string",
        "outputs": ["soporte", "ventas", "otro"],
        "fallbackOutput": "otro"
      }
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slackSupport",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 200],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slackSales",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 400],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje (sin clasificar):\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slackGeneral",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1050, 600],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
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
    }
  }
}
```