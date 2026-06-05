# Gemma 4 31B (Spark llama-server Q4_K_M) — code_generation/n8n_workflow_json

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 6.46 | quality: 7.48
- latency_total: 210.757s | tokens_per_second: 9.7
- input_tokens: 128 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

Para implementar este flujo, necesitas tener configuradas tus credenciales de **OpenAI** y **Slack** en n8n.

He diseñado el workflow utilizando un **AI Agent** simplificado con un **Output Parser** para asegurar que la IA responda estrictamente con una de las tres palabras clave, evitando que el flujo se rompa por respuestas largas.

Aquí tienes el JSON completo. Para importarlo, simplemente cópialo y pégalo directamente en el lienzo de tu n8n.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "7d5e8a2b-1c3d-4e5f-8a9b-0c1d2e3f4g5h",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        400,
        300
      ]
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
      "name": "AI Agent",
      "type": "n8n-nodes-base.aiAgent",
      "typeVersion": 1,
      "position": [
        620,
        300
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        580,
        520
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una de estas tres categorías: 'soporte', 'ventas' o 'otro'.\n\nMensaje: {{ $json.body.message }}\n\nResponde ÚNICAMENTE con la palabra de la categoría, sin puntos ni texto adicional.",
        "options": {}
      },
      "id": "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f",
      "name": "Classifier Prompt",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1,
      "position": [
        750,
        520
      ]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "value1": "={{ $json.output }}",
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.output }}",
              "operation": "equal",
              "value2": "ventas"
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8g",
      "name": "Switch Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        880,
        300
      ]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "=🚨 *Nuevo Ticket de Soporte*\n📧 Email: {{ $node[\"Webhook\"].json.body.email }}\n💬 Mensaje: {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8g9h",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1100,
        180
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "=💰 *Nueva Oportunidad de Ventas*\n📧 Email: {{ $node[\"Webhook\"].json.body.email }}\n💬 Mensaje: {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-d0e1-4f2a-3b4c-5d6e7f8g9h0i",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1100,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "general",
        "text": "=📩 *Mensaje General*\n📧 Email: {{ $node[\"Webhook\"].json.body.email }}\n💬 Mensaje: {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "g7h8i9j0-k1l2-4m3n-4o5p-6q7r8s9t0u1v",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1100,
        420
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
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
            "node": "AI Agent",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Agent": {
      "main": [
        [
          {
            "node": "Switch Clasificación",
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
    "Classifier Prompt": {
      "ai_agent": [
        [
          {
            "node": "AI Agent",
            "type": "ai_agent",
            "index": 0
          }
        ]
      ]
    },
    "Switch Clasificación": {
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

### Instrucciones de configuración:

1.  **Importación**: Copia el código anterior,