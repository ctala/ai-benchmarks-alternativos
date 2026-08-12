# Solar Pro 4 — code_generation/n8n_workflow_json

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.19 | quality: 8.6
- latency_total: 18.504s | tokens_per_second: 95.2
- input_tokens: 174 | output_tokens: 1762
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para un flujo de trabajo de n8n que cumple con los requisitos especificados, aunque carece de detalles adicionales sobre la configuración de credenciales y la gestión de errores.

## Respuesta completa



Aquí tienes el JSON completo del workflow. Está diseñado para ser importado directamente en n8n (funciona tanto en n8n Cloud como en instalaciones self-hosted).

### Instrucciones antes de importar:
1.  **Credenciales:** Este JSON hace referencia a credenciales de **OpenAI** y **Slack**. Debes tenerlas configuradas en tu instancia de n8n o actualizarlas tras importar.
2.  **Webhook URL:** Una vez importado, activa el workflow y copia la URL del nodo Webhook para poder enviar las pruebas POST.
3.  **Slack:** Asegúrate de que el bot de Slack tenga permisos para escribir en los canales `#support`, `#sales` y `#general`.

```json
{
  "name": "AI Message Classifier to Slack",
  "nodes": [
    {
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "tu_webhook_id_aqui",
      "resource": "POST",
      "respondToWebhook": true,
      "options": {
        "responseData": "allEntries"
      }
    },
    {
      "id": "2",
      "name": "Extract Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        }
      }
    },
    {
      "id": "3",
      "name": "AI Classifier",
      "type": "n8n-nodes-base.openAiChat",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "parameters": {
        "model": {
          "options": {
            "model": "gpt-4o-mini"
          }
        },
        "messages": {
          "messages": [
            {
              "role": "user",
              "text": "Classify the following message into one of these categories: 'soporte', 'ventas', 'otro'. Only return the category name.\n\nMessage: {{ $json.message }}"
            }
          ]
        },
        "temperature": 0,
        "maxTokens": 10,
        "responseFormat": {
          "type": "text"
        }
      },
      "credentials": {
        "openaiApi": {
          "id": "tu_credencial_openai_id",
          "name": "OpenAI"
        }
      }
    },
    {
      "id": "4",
      "name": "Router",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        850,
        300
      ],
      "parameters": {
        "rules": {
          "rules": [
            {
              "label": "Soporte",
              "output": 1,
              "value1": "={{ $json.message }}",
              "operation": "contains",
              "value2": "soporte"
            },
            {
              "label": "Ventas",
              "output": 2,
              "value1": "={{ $json.message }}",
              "operation": "contains",
              "value2": "ventas"
            },
            {
              "label": "Otro",
              "output": 3,
              "value1": "={{ $json.message }}",
              "operation": "contains",
              "value2": "otro"
            }
          ]
        }
      }
    },
    {
      "id": "5",
      "name": "Send to Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        200
      ],
      "parameters": {
        "channel": "#support",
        "text": "Nuevo ticket de Soporte\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}\nClasificación: soporte",
        "options": {}
      },
      "credentials": {
        "slackApi": {
          "id": "tu_credencial_slack_id",
          "name": "Slack Bot"
        }
      }
    },
    {
      "id": "6",
      "name": "Send to Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo lead de Ventas\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}\nClasificación: ventas",
        "options": {}
      },
      "credentials": {
        "slackApi": {
          "id": "tu_credencial_slack_id",
          "name": "Slack Bot"
        }
      }
    },
    {
      "id": "7",
      "name": "Send to General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        400
      ],
      "parameters": {
        "channel": "#general",
        "text": "Mensaje General\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}\nClasificación: otro",
        "options": {}
      },
      "credentials": {
        "slackApi": {
          "id": "tu_credencial_slack_id",
          "name": "Slack Bot"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Data": {
      "main": [
        [
          {
            "node": "AI Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Classifier": {
      "main": [
        [
          {
            "node": "Router",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router": {
      "main": [
        [
          {
            "node": "Send to Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "saveManualExecutions": true,
    "saveExecutionProgress": true,
    "executionTimeout": 30,
    "timezone": "America/Mexico_City"
  },
  "versionId": "1",
  "id": "tu_workflow_id_aqui",
  "tags": [
    "ia",
    "slack",
    "clasificacion"
  ]
}
```

### Notas sobre la lógica del Router
He utilizado un nodo **Switch** simple que busca la palabra clave devuelta por la IA (`soporte`, `ventas`, `otro`) dentro del texto de la respuesta. Esto es más robusto que comparar la igualdad exacta (`equals`), ya que a veces los modelos de lenguaje pueden añadir puntuación o espacios extra.