# Qwen 3.5 397B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.4 | quality: 8.6
- latency_total: 80.353s | tokens_per_second: 63.5
- input_tokens: 125 | output_tokens: 5100
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para un workflow de N8N que cumple con los requisitos especificados. Aunque la profundidad es adecuada, podría haber incluido más detalles sobre la configuración de credenciales o manejo de errores. La claridad y utilidad práctica son altas, ya que un emprendedor podría usar esta respuesta directamente.

## Respuesta completa

Aquí tienes el código JSON completo para importar en n8n.

### Instrucciones previas:
1.  **Importar:** Copia el JSON, ve a tu instancia de n8n, haz clic en el menú (tres puntos) o en "Add workflow" -> "Import from File" (o pega el JSON directamente en el canvas con `Ctrl+V` / `Cmd+V`).
2.  **Credenciales:** Este workflow requiere que tengas configuradas dos credenciales en n8n:
    *   **OpenAI API:** Para el nodo de IA.
    *   **Slack OAuth2 API:** Para enviar los mensajes.
    *   *Nota:* Si tus credenciales tienen otro nombre, edítalos en los nodos correspondientes después de importar.
3.  **Canales de Slack:** Asegúrate de que los canales `support`, `sales` y `general` existen en tu Slack. La API de Slack suele requerir el nombre del canal **sin** el símbolo `#`.
4.  **Webhook:** Una vez importado, copia la URL del nodo "Webhook" (en modo Test o Production) para probarlo.

### Workflow JSON

```json
{
  "name": "Clasificador Email a Slack con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-message",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ],
      "webhookId": "webhook-incoming-message"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu única tarea es analizar el mensaje y responder EXACTAMENTE con una de estas tres palabras en minúsculas: soporte, ventas, otro. No añadas explicaciones ni puntuación."
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
      "name": "Clasificador IA",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "rule1",
                    "leftValue": "={{ $json.output }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "rule2",
                    "leftValue": "={{ $json.output }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "rule3",
                    "leftValue": "={{ $json.output }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              }
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node",
      "name": "Router Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "🔴 *Nuevo Mensaje de SOPORTE*\n📧 De: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-support",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        900,
        150
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "2",
          "name": "Slack OAuth2 API"
        }
      }
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "🟢 *Nuevo Mensaje de VENTAS*\n📧 De: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-sales",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        900,
        300
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "2",
          "name": "Slack OAuth2 API"
        }
      }
    },
    {
      "parameters": {
        "channel": "general",
        "text": "⚪ *Nuevo Mensaje GENERAL*\n📧 De: {{ $json.body.email }}\n💬 Mensaje: {{ $json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        900,
        450
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "2",
          "name": "Slack OAuth2 API"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificador IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador IA": {
      "main": [
        [
          {
            "node": "Router Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router Clasificación": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
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
  "settings": {},
  "versionId": "workflow-version-id-placeholder",
  "meta": {
    "instanceId": "instance-id-placeholder"
  },
  "tags": []
}
```

### Notas sobre la implementación:
1.  **Nodo OpenAI:** He utilizado