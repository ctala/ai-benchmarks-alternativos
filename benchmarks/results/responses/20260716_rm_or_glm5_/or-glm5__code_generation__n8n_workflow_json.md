# GLM 5 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5`
- success: True  | final: 7.51 | quality: 8.6
- latency_total: 42.525s | tokens_per_second: 86.1
- input_tokens: 119 | output_tokens: 3661
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON bien estructurado para el workflow de N8N. Ofrece claridad y utilidad práctica, aunque la profundidad podría mejorarse con más detalles sobre la configuración o posibles errores.

## Respuesta completa

Aquí tienes el código JSON completo para el workflow de N8N.

Este workflow incluye:
1.  **Webhook Node**: Escucha peticiones POST.
2.  **OpenAI Node**: Usa el modelo `gpt-3.5-turbo` (puedes cambiarlo a `gpt-4o` si lo prefieres) con una system prompt estricto para asegurar que solo devuelva la categoría.
3.  **Switch Node**: Evalúa el texto devuelto por la IA y enruta el flujo.
4.  **Slack Nodes**: Tres nodos configurados para enviar mensajes a canales específicos (`#support`, `#sales`, `#general`).

### Instrucciones de uso:
1.  Copia el JSON de abajo.
2.  En N8N, haz clic en el menú (tres puntos arriba a la derecha) y selecciona **"Import from File"** o pega el código directamente si tu interfaz lo permite (algunas versiones permiten pegar JSON en la pantalla de creación).
3.  **Configuración obligatoria**:
    *   Abre el nodo **"OpenAI Classifier"** y selecciona o crea tus credenciales de OpenAI (API Key).
    *   Abre los nodos de **Slack** y conecta tu cuenta de Slack. Asegúrate de que los nombres de los canales (`#support`, etc.) existan en tu espacio de trabajo o usa los IDs de los canales.

```json
{
  "name": "Clasificacion Email IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        460,
        300
      ],
      "webhookId": "webhook-id-123"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu única tarea es clasificar el mensaje del usuario en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Solo debes responder con la palabra exacta de la categoría, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        680,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "tu-openai-credential-id",
          "name": "OpenAI API"
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
                  "caseSensitive": false,
                  "leftValue": "",
                  "type": "string"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.choices[0].message.content }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "type": "string"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.choices[0].message.content }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ]
              },
              "renameOutput": true,
              "outputKey": "ventas"
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node",
      "name": "Router Clasificacion",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        900,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=Correo: {{ $('Webhook POST').item.json.body.email }}\nMensaje: {{ $('Webhook POST').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1120,
        180
      ],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credential-id",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=Correo: {{ $('Webhook POST').item.json.body.email }}\nMensaje: {{ $('Webhook POST').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1120,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credential-id",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=Correo: {{ $('Webhook POST').item.json.body.email }}\nMensaje: {{ $('Webhook POST').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-otro",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1120,
        420
      ],
      "credentials": {
        "slackApi": {
          "id": "tu-slack-credential-id",
          "name": "Slack API"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
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
            "node": "Router Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router Clasificacion": {
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
        []
      ]
    }
  },
  "settings": {},
  "staticData": null,
  "pinData": {}
}
```