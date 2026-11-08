# Qwen 3.8 Max 0902 — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 5.55 | quality: 6.8
- latency_total: 446.954s | tokens_per_second: 45.0
- input_tokens: 176 | output_tokens: 20113
- judge_score: 3.0 | justificación: 

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

Aquí tienes el workflow completo de N8N en JSON. Después de importarlo, solo tendrás que configurar las credenciales de **OpenAI** y **Slack** en los nodos correspondientes.

```json
{
  "name": "Clasificar mensajes con OpenAI y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000001",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-460, 0],
      "webhookId": "7c9f2b4c-aaaa-4bbb-8ccc-000000000001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "b8f7a2d0-1111-4aaa-8aaa-000000000010",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "b8f7a2d0-1111-4aaa-8aaa-000000000011",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000002",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [-240, 0]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en exactamente una de estas palabras: soporte, ventas, otro. No agregues explicaciones, puntuación ni comillas.\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000003",
      "name": "Clasificar mensaje",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.7,
      "position": [-20, 0]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini",
          "cachedResultName": "gpt-4o-mini"
        },
        "options": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000004",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1.2,
      "position": [-20, 220]
    },
    {
      "parameters": {
        "jsCode": "const original = $('Extraer email y message').first().json;\nconst llm = $input.first().json;\nconst raw = (llm.text ?? llm.response ?? llm.output ?? llm.message?.content ?? llm.content ?? '').toString().trim().toLowerCase();\nlet category = 'otro';\nif (raw.includes('soporte') || raw.includes('support')) {\n  category = 'soporte';\n} else if (raw.includes('ventas') || raw.includes('venta') || raw.includes('sales')) {\n  category = 'ventas';\n} else if (raw.includes('otro') || raw.includes('other')) {\n  category = 'otro';\n}\nreturn [{ json: { email: original.email ?? '', message: original.message ?? '', category } }];"
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000005",
      "name": "Normalizar categoria",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [200, 0]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-soporte",
                    "leftValue": "={{ $json.category }}",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-ventas",
                    "leftValue": "={{ $json.category }}",
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
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-otro",
                    "leftValue": "={{ $json.category }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000006",
      "name": "Route by category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [420, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "mode": "name",
          "value": "#support",
          "cachedResultName": "#support"
        },
        "messageType": "text",
        "text": "=Nuevo mensaje de soporte\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000007",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [660, -180]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "mode": "name",
          "value": "#sales",
          "cachedResultName": "#sales"
        },
        "messageType": "text",
        "text": "=Nuevo mensaje de ventas\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000008",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [660, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": {
          "__rl": true,
          "mode": "name",
          "value": "#general",
          "cachedResultName": "#general"
        },
        "messageType": "text",
        "text": "=Nuevo mensaje clasificado como otro\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "6f1e2f3a-1111-4aaa-8aaa-000000000009",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [660, 180]
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
      "main": [
        [
          {
            "node": "Clasificar mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Chat Model": {
      "ai_languageModel": [
        [
          {
            "node": "Clasificar mensaje",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar mensaje": {
      "main": [
        [
          {
            "node": "Normalizar categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar categoria": {
      "main": [
        [
          {
            "node": "Route by category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by category": {
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
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {}
}
```