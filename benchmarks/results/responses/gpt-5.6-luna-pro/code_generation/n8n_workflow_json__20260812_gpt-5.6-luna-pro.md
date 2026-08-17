# GPT-5.6 Luna Pro — code_generation/n8n_workflow_json

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 7.2 | quality: 8.0
- latency_total: 41.224s | tokens_per_second: 294.2
- input_tokens: 13167 | output_tokens: 12129
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un flujo de trabajo JSON adecuado para N8N que cumple con los requisitos especificados, aunque carece de profundidad en la explicación de la lógica de clasificación.

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
  "name": "Clasificación de mensajes y enrutamiento a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        260,
        300
      ],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "jsCode": "const body = $json.body ?? $json;\n\nconst email = String(body.email ?? '').trim();\nconst message = String(body.message ?? '').trim();\n\nif (!email || !message) {\n  throw new Error('Los campos \"email\" y \"message\" son obligatorios');\n}\n\nreturn [\n  {\n    json: {\n      email,\n      message\n    }\n  }\n];"
      },
      "id": "2",
      "name": "Preparar datos",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        480,
        300
      ]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "content": "={{ 'Clasifica el siguiente mensaje en exactamente una de estas categorías: soporte, ventas u otro.\\n\\nReglas:\\n- soporte: problemas técnicos, errores, incidencias o solicitudes de ayuda.\\n- ventas: precios, cotizaciones, compras, planes o interés comercial.\\n- otro: cualquier mensaje que no corresponda a las categorías anteriores.\\n\\nResponde únicamente con JSON válido, sin markdown, usando exactamente este formato:\\n{\"classification\":\"soporte\"}\\n\\nEmail del remitente: ' + $json.email + '\\nMensaje: ' + $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 50
        }
      },
      "id": "3",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [
        720,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const original = $('Preparar datos').first().json;\n\nlet raw = $json.output ?? $json.text ?? $json.content ?? $json.response ?? $json.message?.content ?? $json;\n\nif (typeof raw === 'object' && raw !== null) {\n  raw = raw.classification ?? raw.category ?? JSON.stringify(raw);\n}\n\nlet classification = '';\n\nif (typeof raw === 'string') {\n  const cleaned = raw\n    .replace(/```json/gi, '')\n    .replace(/```/g, '')\n    .trim();\n\n  try {\n    const parsed = JSON.parse(cleaned);\n    classification = parsed.classification ?? parsed.category ?? '';\n  } catch {\n    classification = cleaned;\n  }\n}\n\nclassification = String(classification)\n  .toLowerCase()\n  .normalize('NFD')\n  .replace(/[\\u0300-\\u036f]/g, '')\n  .trim();\n\nif (classification.includes('soporte')) {\n  classification = 'soporte';\n} else if (classification.includes('venta')) {\n  classification = 'ventas';\n} else {\n  classification = 'otro';\n}\n\nreturn [\n  {\n    json: {\n      ...original,\n      classification\n    }\n  }\n];"
      },
      "id": "4",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        960,
        300
      ]
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
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
        "options": {}
      },
      "id": "5",
      "name": "Enrutar por clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        1200,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "={{ '📩 Nuevo mensaje clasificado como SOPORTE\\n\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "6",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1480,
        160
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "={{ '📩 Nuevo mensaje clasificado como VENTAS\\n\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "7",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1480,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "={{ '📩 Nuevo mensaje clasificado como OTRO\\n\\nEmail: ' + $json.email + '\\nMensaje: ' + $json.message }}",
        "otherOptions": {}
      },
      "id": "8",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1480,
        440
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\"success\":true,\"classification\":\"mensaje recibido y enviado a Slack\"}",
        "options": {}
      },
      "id": "9",
      "name": "Responder al webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1740,
        300
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Preparar datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar datos": {
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
            "node": "Normalizar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificación": {
      "main": [
        [
          {
            "node": "Enrutar por clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por clasificación": {
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
    },
    "Slack #support": {
      "main": [
        [
          {
            "node": "Responder al webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #sales": {
      "main": [
        [
          {
            "node": "Responder al webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #general": {
      "main": [
        [
          {
            "node": "Responder al webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "workflow-clasificacion-slack-v1",
  "meta": {
    "templateCredsSetupCompleted": false
  },
  "tags": []
}
```

Sustituye `OPENAI_CREDENTIAL_ID` y `SLACK_CREDENTIAL_ID` por las credenciales correspondientes en tu instancia de n8n. El webhook quedará disponible en:

```text
POST /webhook/clasificar-mensaje
```

con un body como:

```json
{
  "email": "cliente@example.com",
  "message": "Necesito ayuda con un error en mi cuenta"
}
```