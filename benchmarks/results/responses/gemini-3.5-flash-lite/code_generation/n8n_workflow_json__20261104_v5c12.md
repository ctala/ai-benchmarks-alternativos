# Gemini 3.5 Flash Lite — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.73 | quality: 8.6
- latency_total: 7.279s | tokens_per_second: 400.2
- input_tokens: 115 | output_tokens: 2913
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con nodos apropiados y configuraciones. Aunque la profundidad es moderada, proporciona una estructura clara y utilidad práctica para implementar el flujo de trabajo.

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

Aquí tienes el código JSON completo para importar directamente en n8n. 

Este flujo utiliza:
1. **Webhook** para recibir los datos POST.
2. **Advanced AI (OpenAI Chat Model + Structured Output Parser)** para garantizar que la IA devuelva exactamente una de las tres categorías requeridas ("soporte", "ventas", "otro").
3. **Switch** para enrutar el mensaje según la categoría.
4. **Slack** para enviar el mensaje al canal correspondiente.

> **Nota importante:** Para que funcione, debes configurar una credencial de **OpenAI** y una credencial de **Slack** en tu instancia de n8n, y asegurarte de que los nombres de los nodos coincidan con los IDs si editas las conexiones (en este JSON ya están pre-conectados).

```json
{
  "name": "Clasificador de Leads y Soporte con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        0
      ],
      "id": "webhook-01",
      "name": "Webhook POST",
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje de un cliente:\n\nEmail: {{$json.body.email}}\nMensaje: {{$json.body.message}}",
        "options": {
          "systemMessage": "Eres un asistente de atención al cliente experto en clasificación. Debes clasificar el mensaje recibido estrictamente en una de estas tres categorías: 'soporte', 'ventas', u 'otro'."
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.7,
      "position": [
        220,
        0
      ],
      "id": "ai-agent-01",
      "name": "AI Agent"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {}
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        220,
        220
      ],
      "id": "openai-model-01",
      "name": "OpenAI Chat Model",
      "credentials": {
        "openAiApi": {
          "id": "CONFIGURA_TU_ID_DE_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsonSchema": "{\n  \"type\": \"object\",\n  \"properties\": {\n    \"categoria\": {\n      \"type\": \"string\",\n      \"enum\": [\"soporte\", \"ventas\", \"otro\"]\n    }\n  },\n  \"required\": [\"categoria\"]\n}"
      },
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "typeVersion": 1.2,
      "position": [
        380,
        220
      ],
      "id": "output-parser-01",
      "name": "Structured Output Parser"
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
                    "leftValue": "={{ $json.output.categoria }}",
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
                    "leftValue": "={{ $json.output.categoria }}",
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
                    "leftValue": "={{ $json.output.categoria }}",
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
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        600,
        0
      ],
      "id": "switch-01",
      "name": "Switch Categoria"
    },
    {
      "parameters": {
        "resource": "message",
        "select": "channel",
        "channelId": "support",
        "text": "=Nuevo mensaje de SOPORTE:\n📧 Email: {{$node[\"Webhook POST\"].json.body.email}}\n💬 Mensaje: {{$node[\"Webhook POST\"].json.body.message}}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        840,
        -120
      ],
      "id": "slack-support",
      "name": "Slack #support",
      "credentials": {
        "slackApi": {
          "id": "CONFIGURA_TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "select": "channel",
        "channelId": "sales",
        "text": "=Nuevo mensaje de VENTAS:\n📧 Email: {{$node[\"Webhook POST\"].json.body.email}}\n💬 Mensaje: {{$node[\"Webhook POST\"].json.body.message}}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        840,
        60
      ],
      "id": "slack-sales",
      "name": "Slack #sales",
      "credentials": {
        "slackApi": {
          "id": "CONFIGURA_TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "select": "channel",
        "channelId": "general",
        "text": "=Nuevo mensaje GENERAL:\n📧 Email: {{$node[\"Webhook POST\"].json.body.email}}\n💬 Mensaje: {{$node[\"Webhook POST\"].json.body.message}}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        840,
        240
      ],
      "id": "slack-general",
      "name": "Slack #general",
      "credentials": {
        "slackApi": {
          "id": "CONFIGURA_TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"status\": \"success\",\n  \"message\": \"Mensaje recibido y clasificado correctamente\"\n}",
        "options": {}
      },
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1100,
        60
      ],
      "id": "respond-webhook",
      "name": "Respond to Webhook"
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "AI Agent",
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
            "node": "AI Agent",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Structured Output Parser": {
      "ai_outputParser": [
        [
          {
            "node": "AI Agent",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Switch Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoria": {
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
            "node": "Respond to Webhook",
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
            "node": "Respond to Webhook",
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
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {}
}
```

### Instrucciones para probarlo:
1. Copia el JSON anterior.
2. En tu panel de n8n, crea un nuevo workflow, haz clic en el menú superior (tres puntos) y selecciona **Import from JSON**, pegando el código.
3. Conecta tus credenciales de **OpenAI** y **Slack**.
4. En los nodos de Slack, asegúrate de colocar los nombres correctos de tus canales (por ejemplo, `support`, `sales`, `general` o sus IDs correspondientes).
5. Activa el workflow y haz una petición POST a la URL del Webhook con un cuerpo JSON como este:
   ```json
   {
     "email": "cliente@example.com",
     "message": "Hola, tengo un problema con mi factura de este mes."
   }
   ```