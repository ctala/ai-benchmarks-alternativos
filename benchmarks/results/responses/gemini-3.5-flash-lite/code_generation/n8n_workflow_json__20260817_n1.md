# Gemini 3.5 Flash Lite — code_generation/n8n_workflow_json

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.67 | quality: 8.4
- latency_total: 5.704s | tokens_per_second: 339.9
- input_tokens: 116 | output_tokens: 1939
- judge_score: 4.0 | justificación: La respuesta proporciona un JSON detallado que cumple con los requisitos especificados, incluyendo la configuración de un webhook, el uso de un modelo de IA para clasificación, y la lógica de enrutamiento a Slack. Aunque la respuesta es precisa y relevante, la profundidad es moderada ya que no explora configuraciones avanzadas o optimizaciones potenciales. La claridad y utilidad son altas, ya que el JSON está bien estructurado y un emprendedor podría usarlo directamente con las configuraciones necesarias.

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

Este workflow incluye:
1. **Webhook**: Configurado para recibir peticiones POST.
2. **OpenAI (Advanced AI / LLM Chain)**: Utiliza un modelo (gpt-4o-mini por defecto) con un prompt del sistema para clasificar estrictamente el mensaje en una de las tres categorías requeridas (`soporte`, `ventas`, `otro`).
3. **Switch**: Evalúa la categoría devuelta por la IA y enruta el flujo.
4. **Slack**: Tres nodos de Slack independientes que envían el mensaje y el correo del remitente al canal correspondiente (`#support`, `#sales`, `#general`).

> **Nota importante antes de usarlo:**
> - Debes configurar tus credenciales de **OpenAI** y **Slack** en n8n y reemplazar los IDs de credencial o seleccionarlos en la interfaz.
> - Asegúrate de que el bot de Slack tenga permisos para escribir en los canales `#support`, `#sales` y `#general`.

```json
{
  "name": "Clasificador de Mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "responseNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        0
      ],
      "id": "webhook-node",
      "name": "Webhook POST",
      "webhookId": "classify-message-webhook"
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje de un cliente. \n\nMensaje: {{$json.body.message}}\nEmail del remitente: {{$json.body.email}}\n\nResponde ÚNICAMENTE con una de estas tres palabras exactas, sin puntos ni texto adicional: soporte, ventas, otro.",
        "options": {
          "systemMessage": "Eres un asistente de IA experto en triaje de atención al cliente. Tu único trabajo es leer un mensaje y clasificarlo estrictamente en una de estas tres categorías: 'soporte', 'ventas', o 'otro'."
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1.7,
      "position": [
        220,
        0
      ],
      "id": "ai-agent-node",
      "name": "AI Agent (Clasificador)"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        }
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        220,
        200
      ],
      "id": "openai-model",
      "name": "OpenAI Chat Model",
      "credentials": {
        "openAiApi": {
          "id": "REPLACE_WITH_YOUR_OPENAI_CREDENTIAL_ID",
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
                    "leftValue": "={{ $json.output.toLowerCase() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
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
                    "leftValue": "={{ $json.output.toLowerCase() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            }
          ]
        },
        "fallbackOutput": "extraOutput",
        "options": {}
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        540,
        0
      ],
      "id": "switch-node",
      "name": "Switch Categoría"
    },
    {
      "parameters": {
        "select": "channel",
        "channel": "#support",
        "text": "=📩 Nuevo ticket de SOPORTE\n*Remitente:* {{$node[\"Webhook POST\"].json.body.email}}\n*Mensaje:* {{$node[\"Webhook POST\"].json.body.message}}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        800,
        -180
      ],
      "id": "slack-support",
      "name": "Slack #support",
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channel": "#sales",
        "text": "=💰 Nuevo lead de VENTAS\n*Remitente:* {{$node[\"Webhook POST\"].json.body.email}}\n*Mensaje:* {{$node[\"Webhook POST\"].json.body.message}}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        800,
        0
      ],
      "id": "slack-sales",
      "name": "Slack #sales",
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channel": "#general",
        "text": "=📌 Nuevo mensaje general\n*Remitente:* {{$node[\"Webhook POST\"].json.body.email}}\n*Mensaje:* {{$node[\"Webhook POST\"].json.body.message}}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        800,
        180
      ],
      "id": "slack-general",
      "name": "Slack #general",
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "{\n  \"status\": \"success\",\n  \"message\": \"Procesado correctamente\"\n}",
        "options": {}
      },
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        1100,
        0
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
            "node": "AI Agent (Clasificador)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent (Clasificador)": {
      "main": [
        [
          {
            "node": "