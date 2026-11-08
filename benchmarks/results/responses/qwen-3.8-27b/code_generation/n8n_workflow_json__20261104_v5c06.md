# Qwen 3.8 27B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 6.37 | quality: 8.0
- latency_total: 1282.249s | tokens_per_second: 18.4
- input_tokens: 167 | output_tokens: 23550
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un JSON bien estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o manejo de errores.

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



Aquí tienes el JSON completo del workflow para n8n:

```json
{
  "name": "Clasificar mensaje con OpenAI y enviar a Slack",
  "nodes": [
    {
      "id": "webhook-start",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [220, 300],
      "parameters": {
        "httpMethod": "POST",
        "path": "mensajes",
        "options": {}
      }
    },
    {
      "id": "extract-fields",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [440, 300],
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body && $json.body.email ? $json.body.email : '' }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body && $json.body.message ? $json.body.message : '' }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      }
    },
    {
      "id": "openai-classifier",
      "name": "OpenAI Classifier",
      "type": "@n8n/n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [660, 300],
      "credentials": {
        "openAiApi": {
          "name": "OpenAI account"
        }
      },
      "parameters": {
        "resource": "text",
        "operation": "create",
        "modelId": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "content": "Clasifica el mensaje del usuario como exactamente una de estas palabras: soporte, ventas o otro. Responde solo con la palabra, sin puntos ni explicaciones.",
              "type": "system"
            },
            {
              "content": "=Clasifica este mensaje: {{ $json.message }}",
              "type": "user"
            }
          ]
        },
        "options": {
          "maxTokens": 10,
          "temperature": 0
        }
      }
    },
    {
      "id": "parse-classification",
      "name": "Parse Classification",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [880, 300],
      "parameters": {
        "jsCode": "const source = $('Extract Fields').first().json;\nlet raw = $input.first().json;\nlet text = '';\n\nif (typeof raw === 'string') {\n  text = raw;\n} else if (raw && raw.message && typeof raw.message.content === 'string') {\n  text = raw.message.content;\n} else if (raw && raw.choices && Array.isArray(raw.choices) && raw.choices[0] && raw.choices[0].message && typeof raw.choices[0].message.content === 'string') {\n  text = raw.choices[0].message.content;\n} else if (raw && typeof raw.content === 'string') {\n  text = raw.content;\n}\n\nlet classification = 'otro';\nconst normalized = text.toLowerCase();\n\nif (normalized.includes('soporte')) {\n  classification = 'soporte';\n} else if (normalized.includes('ventas')) {\n  classification = 'ventas';\n} else if (normalized.includes('otro')) {\n  classification = 'otro';\n}\n\nreturn [\n  {\n    json: {\n      email: source.email || '',\n      message: source.message || '',\n      classification\n    }\n  }\n];"
      }
    },
    {
      "id": "route-by-classification",
      "name": "Route by Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.1,
      "position": [1100, 300],
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "rule-support",
                    "leftValue": "={{ $json.classification }}",
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "rule-sales",
                    "leftValue": "={{ $json.classification }}",
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "rule-other",
                    "leftValue": "={{ $json.classification }}",
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
        "fallbackOutput": "2",
        "options": {}
      }
    },
    {
      "id": "slack-support",
      "name": "Slack Support",
      "type": "@n8n/n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1320, 180],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      },
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#support",
        "text": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}\n\nClasificación: {{ $json.classification }}",
        "options": {}
      }
    },
    {
      "id": "slack-sales",
      "name": "Slack Sales",
      "type": "@n8n/n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1320, 300],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      },
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#sales",
        "text": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}\n\nClasificación: {{ $json.classification }}",
        "options": {}
      }
    },
    {
      "id": "slack-general",
      "name": "Slack General",
      "type": "@n8n/n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1320, 420],
      "credentials": {
        "slackApi": {
          "name": "Slack account"
        }
      },
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channelId": "#general",
        "text": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}\n\nClasificación: {{ $json.classification }}",
        "options": {}
      }
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Parse Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parse Classification": {
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {}
}
```

Notas importantes:

- Importa este JSON en n8n.
- Selecciona o crea las credenciales:
  - OpenAI para el nodo `OpenAI Classifier`.
  - Slack para los nodos `Slack Support`, `Slack Sales` y `Slack General`.
- El webhook recibirá payloads tipo:

```json
{
  "email": "persona@ejemplo.com",
  "message": "Tengo un problema con mi cuenta"
}
```

- El bot de Slack debe estar invitado a los canales:
  - `#support`
  - `#sales`
  - `#general`