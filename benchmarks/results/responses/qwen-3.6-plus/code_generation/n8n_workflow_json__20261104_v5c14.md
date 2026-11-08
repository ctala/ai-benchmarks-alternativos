# Qwen 3.6 Plus — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 6.54 | quality: 7.2
- latency_total: 61.873s | tokens_per_second: 57.5
- input_tokens: 125 | output_tokens: 3555
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

# Workflow n8n: Clasificación de Mensajes con IA → Slack

Aquí tienes el JSON completo listo para importar en n8n:

```json
{
  "name": "Clasificador de Mensajes → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
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
      "id": "extract-fields",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [470, 300]
    },
    {
      "parameters": {
        "model": {
          "model": {
            "id": "gpt-4o-mini",
            "name": "gpt-4o-mini"
          }
        },
        "messages": {
          "values": [
            {
              "content": "=Eres un clasificador de mensajes. Tu ÚNICA tarea es analizar el siguiente mensaje y clasificarlo en EXACTAMENTE UNA de estas tres categorías:\n\n- **soporte** → Si el mensaje trata sobre problemas técnicos, bugs, errores, preguntas sobre funcionalidad, ayuda con la plataforma, quejas de servicio.\n- **ventas** → Si el mensaje trata sobre precios, planes, descuentos, demos, cotizaciones, propuestas comerciales, partnerships.\n- **otro** → Si no encaja en ninguna de las dos anteriores.\n\nIMPORTANTE: Responde SOLO con la palabra exacta de la categoría, sin explicaciones ni texto adicional.\n\n---\n\nMensaje a clasificar:\n{{ $json.message }}",
              "role": "system"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "openai-classify",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.6,
      "position": [690, 300],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI account"
        }
      }
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
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "soporte",
                    "operator": { "type": "string", "operation": "equals" }
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
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "ventas",
                    "operator": { "type": "string", "operation": "equals" }
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
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "otro",
                    "operator": { "type": "string", "operation": "equals" }
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
      "id": "switch-node",
      "name": "Rutar por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [910, 300]
    },
    {
      "parameters": {
        "operation": "post",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=📧 *Nuevo mensaje de soporte*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Clasificación:* Soporte\n\n*Mensaje:*\n{{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "slack-support",
      "name": "Slack → #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1130, 100],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=💰 *Nuevo lead de ventas*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Clasificación:* Ventas\n\n*Mensaje:*\n{{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "slack-sales",
      "name": "Slack → #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1130, 300],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "operation": "post",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=📨 *Nuevo mensaje*\n\n*De:* {{ $('Extraer Campos').item.json.email }}\n*Clasificación:* Otro\n\n*Mensaje:*\n{{ $('Extraer Campos').item.json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "slack-general",
      "name": "Slack → #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1130, 500],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
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
            "node": "Rutar por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Rutar por Categoría": {
      "main": [
        [
          {
            "node": "Slack → #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack → #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack → #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "templateCredsSetupCompleted": false,
    "instanceId": ""
  }
}
```

## 📋 Diagrama del flujo

```
[Webhook POST] → [Extraer Campos] → [Clasificar con OpenAI] → [Switch/Ruta]
                                                              ├─→ Slack #support
                                                              ├─→ Slack #sales
                                                              └─→ Slack #general
```

## 🔧 Pasos para usarlo

1. **Importar**: En n8n → `Settings` → `Import from File` y pega el JSON
2. **Configurar credenciales**:
   - 🔑 **OpenAI**: Crea una credencial `OpenAI account` con tu API key
   - 🔑 **Slack**: Crea una credencial `Slack account` con un bot token (`xoxb-...`)
3. **Ajustar canales**: Verifica que los nombres `#support`, `#sales`, `#general` coincidan con tus canales reales de Slack
4. **Probar**: Envía un POST a `https://TU-INSTANCIA.n8n.cloud/webhook/clasificar-mensaje` con:

```json
{
  "body": {
    "email": "cliente@ejemplo.com",
    "message": "Mi cuenta no me permite iniciar sesión desde ayer"
  }
}
```

## ⚙️ Notas de configuración

| Aspecto | Detalle |
|---|---|
| **Modelo IA** | `gpt-4o-mini` (bajo costo, suficiente para clasificación) |
| **Temperature** | `0` (determinístico, siempre la misma respuesta) |
| **Max tokens** | `10` (solo necesita devolver una palabra) |
| **Webhook URL** | `/webhook/clasificar-mensaje` |
| **Método** | `POST` |