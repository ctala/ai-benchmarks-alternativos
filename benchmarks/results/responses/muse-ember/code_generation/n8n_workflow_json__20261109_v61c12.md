# Muse Ember — code_generation/n8n_workflow_json

- model_id: `meta/muse-ember`
- success: True  | final: 6.59 | quality: 6.92
- latency_total: 10.82s | tokens_per_second: 755.4
- input_tokens: 122 | output_tokens: 8174
- judge_score: 2.8 | justificación: 

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

Aquí tienes el workflow completo y listo para importar en n8n:

**Flujo:** `Webhook POST` -> `Set (extrae email/message)` -> `Basic LLM Chain + OpenAI` -> `Code (normaliza)` -> `Switch` -> `Slack #support / #sales / #general`

```json
{
  "name": "Clasificar mensajes con IA y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "11111111-1111-4111-8111-111111111111",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1",
              "name": "email",
              "value": "={{ $json.body.email || $json.email }}",
              "type": "string"
            },
            {
              "id": "a2",
              "name": "message",
              "value": "={{ $json.body.message || $json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "22222222-2222-4222-8222-222222222222",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje como \"soporte\", \"ventas\" u \"otro\".\n\n- soporte: problemas técnicos, errores, ayuda con la cuenta.\n- ventas: precios, compra, cotización, planes, contratar.\n- otro: cualquier otro tema.\n\nResponde SOLO con una palabra en minúsculas, sin puntuación ni explicación.\n\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "33333333-3333-4333-8333-333333333333",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.basicLlmChain",
      "typeVersion": 1,
      "position": [680, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "44444444-4444-4444-8444-444444444444",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.2,
      "position": [680, 500],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_POR_TU_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "runOnceForAllItems",
        "jsCode": "const datos = $('Extraer email y message').first().json;\nconst ia = $('Clasificar con IA').first().json;\nconst raw = String(ia.response?.text ?? ia.text ?? ia.output ?? '').toLowerCase().trim();\n\nlet clasificacion = 'otro';\nif (raw.includes('soporte')) clasificacion = 'soporte';\nelse if (raw.includes('ventas')) clasificacion = 'ventas';\nelse if (raw.includes('otro')) clasificacion = 'otro';\n\nreturn [{ json: { email: datos.email, message: datos.message, clasificacion } }];"
      },
      "id": "55555555-5555-4555-8555-555555555555",
      "name": "Normalizar clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [900, 300]
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c1",
                    "leftValue": "={{ $json.clasificacion }}",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c2",
                    "leftValue": "={{ $json.clasificacion }}",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c3",
                    "leftValue": "={{ $json.clasificacion }}",
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
      "id": "66666666-6666-4666-8666-666666666666",
      "name": "Switch - Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=Nuevo mensaje clasificado como *soporte*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "additionalFields": {}
      },
      "id": "77777777-7777-4777-8777-777777777777",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 180],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_POR_TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=Nuevo mensaje clasificado como *ventas*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "additionalFields": {}
      },
      "id": "88888888-8888-4888-8888-888888888888",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_POR_TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=Nuevo mensaje clasificado como *otro*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "additionalFields": {}
      },
      "id": "99999999-9999-4999-8999-999999999999",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1360, 420],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_POR_TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Clasificar con IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA": {
      "main": [
        [
          {
            "node": "Normalizar clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ],
      "ai_languageModel": [
        [
          {
            "node": "OpenAI Chat Model",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificación": {
      "main": [
        [
          {
            "node": "Switch - Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch - Clasificación": {
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

### Cómo usarlo

1. En n8n: **Workflows > Import from File** y pega este JSON.
2. En el nodo **OpenAI Chat Model** selecciona tu credencial de OpenAI.
3. En los 3 nodos de **Slack** selecciona tu credencial de Slack (los canales `#support`, `#sales`, `#general` deben existir y la app debe estar invitada).
4. Activa el workflow y copia la URL del Webhook.

### Probar

```bash
curl -X POST https://TU_INSTANCIA/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"juan@example.com","message":"Quiero saber el precio del plan premium"}'
```

Ese ejemplo debería ir a `#sales`.