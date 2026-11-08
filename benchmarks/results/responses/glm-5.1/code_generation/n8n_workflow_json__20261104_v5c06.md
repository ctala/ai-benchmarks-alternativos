# GLM-5.1 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.31 | quality: 8.6
- latency_total: 74.852s | tokens_per_second: 85.1
- input_tokens: 126 | output_tokens: 6370
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de Slack.

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

Aquí tienes el JSON completo del workflow de n8n. 

Este workflow incluye:
1. Un **Webhook** configurado para recibir peticiones POST.
2. Un nodo de **OpenAI** que actúa como clasificador.
3. Un nodo **Switch** que enruta el flujo según la respuesta de la IA.
4. Tres nodos de **Slack** configurados para enviar mensajes a `#support`, `#sales` y `#general`.

```json
{
  "name": "Clasificador IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1-webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        0,
        0
      ],
      "webhookId": "webhook-clasificador"
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un asistente que clasifica mensajes. Dado el mensaje del usuario, debes responder SOLO con una de estas tres palabras: 'soporte', 'ventas' u 'otro'. No añadas signos de puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "2-openai",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.4,
      "position": [
        220,
        0
      ]
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
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": "Soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": "Ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.trim().toLowerCase() }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": "Otro"
            }
          ]
        },
        "options": {}
      },
      "id": "3-switch",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        440,
        0
      ]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "operation": "postMessage",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "support",
          "mode": "name"
        },
        "text": "=Nuevo mensaje de Soporte:\nEmail: {{$node[\"Webhook\"].json.body.email}}\nMensaje: {{$node[\"Webhook\"].json.body.message}}",
        "otherOptions": {}
      },
      "id": "4-slack-soporte",
      "name": "Slack: Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        660,
        -200
      ]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "operation": "postMessage",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "sales",
          "mode": "name"
        },
        "text": "=Nuevo mensaje de Ventas:\nEmail: {{$node[\"Webhook\"].json.body.email}}\nMensaje: {{$node[\"Webhook\"].json.body.message}}",
        "otherOptions": {}
      },
      "id": "5-slack-ventas",
      "name": "Slack: Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        660,
        0
      ]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "operation": "postMessage",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "general",
          "mode": "name"
        },
        "text": "=Nuevo mensaje General:\nEmail: {{$node[\"Webhook\"].json.body.email}}\nMensaje: {{$node[\"Webhook\"].json.body.message}}",
        "otherOptions": {}
      },
      "id": "6-slack-otro",
      "name": "Slack: Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        660,
        200
      ]
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
            "node": "Slack: Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: Otro",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Instrucciones de uso:
1. Copia el bloque JSON de arriba.
2. Ve a tu instancia de n8n, haz clic en el botón de añadir workflow (`...` o clic derecho en el lienzo) y selecciona **"Import from Clipboard"** (Importar del portapapeles).
3. **Configura las credenciales**:
   - Haz doble clic en el nodo **OpenAI** y añade tu API Key de OpenAI.
   - Haz doble clic en cada nodo de **Slack** y configura tus credenciales OAuth2 de Slack (asegúrate de que el bot de Slack tenga permisos para escribir en esos canales).
4. Activa el workflow. Puedes probarlo enviando una petición POST a tu URL de webhook (ej. `https://tu-n8n.com/webhook/clasificar-mensaje`) con un body JSON como este:
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Hola, quiero comprar 10 licencias de su software"
}
```