# DeepSeek V4 Pro (0813) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 6.86 | quality: 8.2
- latency_total: 210.805s | tokens_per_second: 76.2
- input_tokens: 205 | output_tokens: 16072
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado. Aunque la profundidad es moderada, la utilidad práctica es alta para un emprendedor que busca implementar este flujo de trabajo.

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

Aquí tienes el workflow completo en JSON para n8n. Recuerda configurar tus credenciales de **OpenAI** y **Slack** después de importarlo.

```json
{
  "name": "Clasificador de mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [0, 0]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "complete",
        "model": "gpt-3.5-turbo-instruct",
        "prompt": "=Clasifica el siguiente mensaje en una de estas categorías exactas: \"soporte\", \"ventas\" o \"otro\". Responde únicamente con la categoría.\n\nMensaje: {{ $json.body.message }}\nEmail: {{ $json.body.email }}",
        "options": {
          "temperature": 0
        }
      },
      "id": "openai-node",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [220, 0]
    },
    {
      "parameters": {
        "functionCode": "let text = '';\nconst call = $json;\nif (call.choices && call.choices[0]) {\n  if (call.choices[0].message && call.choices[0].message.content) text = call.choices[0].message.content;\n  else if (call.choices[0].text) text = call.choices[0].text;\n} else if (call.text) {\n  text = call.text;\n} else if (call.content) {\n  text = call.content;\n} else {\n  text = JSON.stringify(call);\n}\ntext = text.trim().toLowerCase();\nlet category = 'otro';\nif (text.includes('soporte')) category = 'soporte';\nelse if (text.includes('ventas')) category = 'ventas';\nreturn { json: { category, raw_text: text } };"
      },
      "id": "normalize-node",
      "name": "Normalize Category",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [440, 0]
    },
    {
      "parameters": {
        "conditions": [
          {
            "value1": "={{ $json.category }}",
            "operation": "equal",
            "value2": "soporte"
          },
          {
            "value1": "={{ $json.category }}",
            "operation": "equal",
            "value2": "ventas"
          },
          {
            "value1": "={{ $json.category }}",
            "operation": "equal",
            "value2": "otro"
          }
        ],
        "options": {}
      },
      "id": "switch-node",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [660, 0]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "channel": "#support",
        "text": "=Nuevo mensaje de {{ $('Webhook').item.json.body.email }}:\n{{ $('Webhook').item.json.body.message }}"
      },
      "id": "slack-support-node",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [880, -100]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "channel": "#sales",
        "text": "=Nuevo mensaje de {{ $('Webhook').item.json.body.email }}:\n{{ $('Webhook').item.json.body.message }}"
      },
      "id": "slack-sales-node",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [880, 0]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "channel": "#general",
        "text": "=Nuevo mensaje de {{ $('Webhook').item.json.body.email }}:\n{{ $('Webhook').item.json.body.message }}"
      },
      "id": "slack-general-node",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [880, 100]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Normalize Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize Category": {
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
  },
  "settings": {}
}
```