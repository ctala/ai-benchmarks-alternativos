# Tencent Hy4 preview — code_generation/n8n_workflow_json

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.84 | quality: 8.2
- latency_total: 300.474s | tokens_per_second: 68.6
- input_tokens: 143 | output_tokens: 20611
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales y manejo de errores.

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

Aquí tienes el JSON completo del workflow para N8N. Después de importarlo, selecciona tus credenciales de **OpenAI** y **Slack**. Si tu Slack requiere IDs de canal, reemplaza `#support`, `#sales` y `#general` por IDs tipo `C123...`.

```json
{
  "name": "Clasificar mensaje y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "10000000-0000-4000-8000-000000000001",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-660, 300],
      "webhookId": "20000000-0000-4000-8000-000000000001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "10000000-0000-4000-8000-000000000002",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [-440, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
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
              "content": "Eres un clasificador de mensajes. Responde SOLO con un JSON válido: {\"classification\":\"soporte\"|\"ventas\"|\"otro\"}. No agregues texto adicional."
            },
            {
              "role": "user",
              "content": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}\n\nClasifica el mensaje en una de estas categorías exactas: soporte, ventas, otro."
            }
          ]
        },
        "simplify": true,
        "jsonOutput": true,
        "options": {
          "temperature": 0,
          "maxTokens": 50
        }
      },
      "id": "10000000-0000-4000-8000-000000000003",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [-220, 300]
    },
    {
      "parameters": {
        "mode": "runOnceForAllItems",
        "jsCode": "const extracted = $('Extract Fields').first().json;\nconst aiOutput = $input.first().json;\n\nlet rawContent =\n  aiOutput?.message?.content ??\n  aiOutput?.choices?.[0]?.message?.content ??\n  aiOutput?.response?.message?.content ??\n  aiOutput?.text ??\n  aiOutput?.output ??\n  JSON.stringify(aiOutput);\n\nif (Array.isArray(rawContent)) {\n  rawContent = rawContent.map(part => part?.text ?? part?.content ?? '').join('');\n}\n\nlet classification = 'otro';\n\ntry {\n  const parsed = typeof rawContent === 'string' ? JSON.parse(rawContent) : rawContent;\n  classification = parsed?.classification ?? parsed?.clasificacion ?? parsed?.category ?? parsed?.categoria ?? rawContent;\n} catch (error) {\n  classification = rawContent;\n}\n\nconst textToSearch = typeof classification === 'string' ? classification : JSON.stringify(classification);\nconst match = textToSearch.match(/(soporte|ventas|otro)/i);\n\nclassification = match ? match[1].toLowerCase() : 'otro';\n\nreturn [\n  {\n    json: {\n      email: extracted.email,\n      message: extracted.message,\n      classification\n    }\n  }\n];\n"
      },
      "id": "10000000-0000-4000-8000-000000000004",
      "name": "Normalize Classification",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [0, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-soporte",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "singleValue": true
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
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-ventas",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "singleValue": true
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "rule-otro",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "singleValue": true
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
        "looseTypeValidation": true,
        "options": {}
      },
      "id": "10000000-0000-4000-8000-000000000005",
      "name": "Route by Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [220, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name",
          "cachedResultName": "#support"
        },
        "text": "=:incoming_envelope: *Nuevo mensaje clasificado como* `{{ $json.classification }}`\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "10000000-0000-4000-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [460, 180]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name",
          "cachedResultName": "#sales"
        },
        "text": "=:incoming_envelope: *Nuevo mensaje clasificado como* `{{ $json.classification }}`\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "10000000-0000-4000-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name",
          "cachedResultName": "#general"
        },
        "text": "=:incoming_envelope: *Nuevo mensaje clasificado como* `{{ $json.classification }}`\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "10000000-0000-4000-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [460, 420]
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
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
            "node": "Normalize Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize Classification": {
      "main": [
        [
          {
            "node": "Route by Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Classification": {
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "30000000-0000-4000-8000-000000000001"
}
```