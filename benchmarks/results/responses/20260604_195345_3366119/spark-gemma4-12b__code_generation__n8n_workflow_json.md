# Gemma 4 12B (Spark llama-server Q4_K_M) — code_generation/n8n_workflow_json

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.32 | quality: 8.32
- latency_total: 80.838s | tokens_per_second: 25.2
- input_tokens: 128 | output_tokens: 2038
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para usar este JSON en n8n, simplemente cópialo y pégalo directamente en tu lienzo de n8n (o impórtalo mediante el menú de "Import from JSON").

**Nota importante:** Necesitarás configurar tus propias credenciales en los nodos de **OpenAI** y **Slack**.

```json
{
  "name": "Clasificador de Emails a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook-email-classifier",
        "options": {}
      },
      "id": "d7698c6d-3c71-4e8a-9b7d-9a891f2c3d4e",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        400,
        400
      ]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un asistente que clasifica correos electrónicos. Responde ÚNICAMENTE con una de estas tres palabras: soporte, ventas, o otro. No añadas explicaciones."
            },
            {
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "e8798c6d-3c71-4e8a-9b7d-9a891f2c3d4f",
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        820,
        400
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_DE_CREDENCIAL_AQUI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "operation": "convertToText",
              "value1": "={{ $json.message.content.toLowerCase() }}",
              "value2": "soporte",
              "output": "soporte"
            },
            {
              "operation": "convertToText",
              "value1": "={{ $json.message.content.toLowerCase() }}",
              "value2": "ventas",
              "output": "ventas"
            }
          ]
        },
        "fallbackOutput": "otro"
      },
      "id": "f9898c6d-3c71-4e8a-9b7d-9a891f2c3d5e",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1040,
        400
      ]
    },
    {
      "parameters": {
        "channel": "soporte",
        "text": "=📧 *Nuevo Ticket de Soporte*\n*De:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "options": {}
      },
      "id": "a1098c6d-3c71-4e8a-9b7d-9a891f2c3d6f",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1300,
        280
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_AQUI",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "ventas",
        "text": "=💰 *Nueva Oportunidad de Venta*\n*De:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "options": {}
      },
      "id": "b2098c6d-3c71-4e8a-9b7d-9a891f2c3d7f",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1300,
        400
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_AQUI",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "general",
        "text": "=📩 *Otro Mensaje*\n*De:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "options": {}
      },
      "id": "c3098c6d-3c71-4e8a-9b7d-9a891f2c3d8f",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1300,
        520
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_AQUI",
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
  }
}
```

### Explicación del funcionamiento:

1.  **Webhook**: Escucha una petición POST. Espera un JSON como este:
    `{"email": "usuario@ejemplo.com", "message": "Mi producto no funciona"}`.
2.  **OpenAI Classifier**: Envía el contenido del mensaje a GPT. He configurado el *System Prompt* para que la IA solo responda una palabra clave, evitando que incluya texto innecesario que rompería el flujo.
3.  **Switch**: Evalúa la respuesta de la IA.
    *   Si dice "soporte" $\rightarrow$ va al primer canal de Slack.
    *   Si dice "ventas" $\rightarrow$ va al segundo.
    *   Cualquier otra respuesta (o "otro") $\rightarrow$ va al canal general.
4.  **Slack Nodes**: Envían el mensaje formateado incluyendo el email del remitente y el cuerpo del mensaje original.

### Cómo configurarlo:
1.  Copia el JSON y pégalo en n8n.
2.  En el nodo **OpenAI**, selecciona tus credenciales y asegúrate de que el modelo sea `gpt-3.5-turbo` o `gpt-4o`.
3.  En los 3 nodos de **Slack**, selecciona tus credenciales y asegúrate de que los nombres de los canales (`#soporte`, `#ventas`, `#general`) coincidan exactamente con los de tu espacio de trabajo.
4.  Pulsa en "Execute Workflow" para probarlo o "Activate" para dejarlo corriendo.