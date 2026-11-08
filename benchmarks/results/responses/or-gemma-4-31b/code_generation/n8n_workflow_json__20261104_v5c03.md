# Gemma 4 31B — code_generation/n8n_workflow_json

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 6.98 | quality: 7.2
- latency_total: 21.746s | tokens_per_second: 96.3
- input_tokens: 128 | output_tokens: 2094
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero carece de profundidad en la explicación de la configuración del modelo y la lógica de los nodos, lo que podría dificultar su implementación directa por un emprendedor.

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

Para implementar este workflow, necesitas tener configuradas tus credenciales de **OpenAI** y **Slack** en n8n.

He diseñado el flujo utilizando el nodo **AI Agent** con un **Output Parser** (o instrucciones estrictas) para asegurar que la IA solo responda con una de las tres palabras clave, permitiendo que el nodo **Switch** funcione correctamente.

Aquí tienes el JSON completo. Para usarlo, simplemente **cópialo y pégalo directamente en el lienzo de n8n**.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "6f4d8a2b-1234-4abc-8def-1234567890ab",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [400, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. \n\nRegla estricta: Responde ÚNICAMENTE con la palabra de la categoría, sin puntos, sin explicaciones y en minúsculas.\n\nMensaje: {{ $json.body.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
      "name": "AI Classifier",
      "type": "n8n-nodes-base.aiAgent",
      "typeVersion": 1,
      "position": [620, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "name": "OpenAI Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [600, 520],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.output }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte"
            },
            {
              "value2": "ventas",
              "output": 1
            },
            {
              "value2": "otro",
              "output": 2
            }
          ]
        }
      },
      "id": "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f",
      "name": "Switch Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [880, 300]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "=🚨 *Nuevo Ticket de Soporte*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1120, 180],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "=💰 *Nuevo Lead de Ventas*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1120, 300],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "general",
        "text": "=📩 *Mensaje General*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-d0e1-4f2a-3b4c-5d6e7f8a9b0c",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1120, 420],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
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
            "node": "Switch Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Model": {
      "ai_languageModel": [
        [
          {
            "node": "AI Classifier",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Switch Category": {
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
  }
}
```

### Notas para la configuración:

1.  **Credenciales**: Después de importar el JSON, haz clic en los nodos de **OpenAI** y **Slack** para seleccionar tus propias credenciales guardadas en n8n.
2.  **Canales de Slack**: Asegúrate de que el bot de Slack haya sido invitado a los canales `#support`, `#sales` y `#general` (usa `/invite @NombreDeTuBot` en Slack).
3.  **Prueba el Webhook**: Puedes enviar una prueba usando `curl` o Postman con el siguiente cuerpo:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, mi pedido no ha llegado y quiero saber dónde está."
    }
    ```
4.  **Lógica de IA**: He configurado el prompt para que sea "estricto". Esto evita que la IA responda cosas como *"La categoría es soporte"*, obligándola a responder solo *"soporte"*, lo cual es crítico para que el nodo **Switch** no falle.