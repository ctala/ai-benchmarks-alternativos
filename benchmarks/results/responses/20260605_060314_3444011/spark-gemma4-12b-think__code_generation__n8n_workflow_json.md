# Gemma 4 12B (Spark llama-server, reasoning) — code_generation/n8n_workflow_json

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.41 | quality: 8.6
- latency_total: 108.18s | tokens_per_second: 25.5
- input_tokens: 131 | output_tokens: 2760
- judge_score: 4.0 | justificación: 

## Respuesta completa

Para usar este workflow, copia el código JSON de abajo y pégalo directamente en tu lienzo de n8n (Ctrl+V o Cmd+V).

### Notas previas antes de importar:
1.  **Credenciales:** Deberás configurar tus credenciales de **OpenAI** y **Slack** en los nodos correspondientes.
2.  **Slack Channels:** Asegúrate de que el bot de Slack tenga permisos para escribir en los canales `#support`, `#sales` y `#general`.
3.  **Prompt:** He configurado el prompt para que la IA responda **únicamente** con una palabra para facilitar la lógica del nodo *Switch*.

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "19e47d64-8f4e-4955-9982-0e7897961334",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        380,
        460
      ],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": {
          "messages": [
            {
              "content": "Clasifica el siguiente mensaje de un usuario en una de estas tres categorías: \"soporte\", \"ventas\" o \"otro\". \n\nRegla estricta: Responde ÚNICAMENTE con la palabra de la categoría, sin puntos, sin explicaciones y sin comillas.\n\nMensaje: {{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "28f5e832-6932-487c-9d96-671972973862",
      "name": "OpenAI - Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        840,
        460
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_DE_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "value": "soporte",
              "output": 1
            },
            {
              "value": "ventas",
              "output": 2
            }
          ],
          "fallbackOutput": 3
        }
      },
      "id": "0e799334-7871-4262-8899-7f018722b5d9",
      "name": "Switch - Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1200,
        460
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🚨 *Nuevo Ticket de Soporte*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "d8d97523-7764-4894-978c-776908829410",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1540,
        320
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nueva Oportunidad de Ventas*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "f4e7a98b-7f3e-490c-8d9c-1234567890ab",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1540,
        460
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📩 *Otro Mensaje*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-e5f6-4789-9012-34567890abcd",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1540,
        600
      ],
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
            "node": "OpenAI - Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI - Clasificar": {
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
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Explicación del Workflow:

1.  **Webhook:** Escucha una petición POST. Espera un JSON como este:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, mi producto no funciona y necesito ayuda urgente."
    }
    ```
2.  **OpenAI Node:** Utiliza el modelo `gpt-4o-mini` (que es muy barato y rápido) para analizar el texto. El prompt le ordena ser estricto y devolver solo una palabra para que el siguiente nodo no falle.
3.  **Switch Node:** Evalúa el texto de la IA:
    *   Si dice "soporte", va a la salida 1.
    *   Si dice "ventas", va a la salida 2.
    *   Cualquier otra cosa (o "otro") va a la salida 3 (fallback).
4.  **Slack Nodes:** Hay tres nodos de Slack independientes. Cada uno envía el mensaje formateado con el email y el contenido original al canal correspondiente.