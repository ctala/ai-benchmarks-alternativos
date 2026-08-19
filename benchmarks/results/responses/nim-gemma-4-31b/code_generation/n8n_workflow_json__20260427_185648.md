# Gemma 4 31B (NIM) — code_generation/n8n_workflow_json

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.01 | quality: 8.32
- latency_total: 85.764s | tokens_per_second: 23.0
- input_tokens: 121 | output_tokens: 1969
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para implementar este workflow, necesitas tener configuradas tus credenciales de **OpenAI** y **Slack** en n8n.

He diseñado el flujo utilizando un **AI Agent** con un **Output Parser** (aunque para simplicidad en el JSON, he usado un prompt estructurado que devuelve solo la palabra clave) y un nodo **Switch** para el enrutamiento.

Aquí tienes el JSON completo. Para usarlo, simplemente **cópialo y pégalo directamente en el lienzo (canvas) de n8n**.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificador-mensajes",
        "options": {}
      },
      "id": "3f8a6c1a-7b2d-4e5f-8a1b-c2d3e4f5a6b7",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [400, 300]
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. \n\nRegla estricta: Responde ÚNICAMENTE con una de esas tres palabras, sin puntos, sin mayúsculas y sin explicaciones.\n\nMensaje: {{ $json.body.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [620, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_DE_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.text }}",
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
      "id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "name": "Switch Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [840, 300]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "=📩 *Nuevo Ticket de Soporte*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1100, 180],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "=💰 *Nueva Oportunidad de Ventas*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1100, 300],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "general",
        "text": "=📦 *Mensaje General*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1100, 420],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
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
            "node": "Switch Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Classification": {
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

### Instrucciones para ponerlo en marcha:

1.  **Importar:** Copia el código anterior, ve a tu n8n y presiona `Ctrl+V` (o `Cmd+V`) en el editor.
2.  **Credenciales:**
    *   Haz clic en el nodo **OpenAI Classifier** y selecciona/crea tu credencial de OpenAI API.
    *   Haz clic en los nodos de **Slack** y selecciona/crea tu credencial de Slack.
3.  **Canales de Slack:** Asegúrate de que el Bot de Slack haya sido invitado a los canales `#support`, `#sales` y `#general` (comando `/invite @NombreDelBot` en Slack).
4.  **Prueba:** Envía un POST al URL del webhook con el siguiente formato JSON:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, mi pedido no ha llegado y quiero saber dónde está"
    }
    ```

### Detalles técnicos del flujo:
*   **Webhook:** Recibe los datos.
*   **OpenAI:** He utilizado un "System Prompt" implícito en el texto para forzar que la IA solo responda una palabra. Esto evita que el nodo Switch falle por recibir frases largas como *"Este mensaje pertenece a la categoría de soporte"*.
*   **Switch:** Compara la respuesta de la IA y redirige el flujo al camino 0, 1 o 2.
*   **Slack:** Utiliza expresiones para recuperar el email y el mensaje original desde el nodo Webhook inicial.