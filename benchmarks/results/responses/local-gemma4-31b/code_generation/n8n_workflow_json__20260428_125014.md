# Gemma 4 31B (DGX Spark Q4_K_M) — code_generation/n8n_workflow_json

- model_id: `gemma4:31b`
- success: True  | final: 6.27 | quality: 7.48
- latency_total: 625.914s | tokens_per_second: 4.8
- input_tokens: 131 | output_tokens: 3024
- judge_score: 3.2 | justificación: 

## Respuesta completa

Para implementar este workflow en n8n, necesitas tener configuradas las credenciales de **OpenAI** y **Slack**.

Aquí tienes el JSON completo. Para usarlo, simplemente **copia el código y pégalo directamente en el lienzo (canvas) de tu n8n**.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-messages",
        "options": {}
      },
      "id": "5f8e7d2a-1234-4abc-8def-1234567890ab",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        400,
        400
      ],
      "webhookId": "incoming-messages"
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. \n\nResponde ÚNICAMENTE con la palabra de la categoría, sin puntos, sin explicaciones y en minúsculas.\n\nMensaje: {{ $json.body.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4g7h-8i9j-k0l1m2n3o4p5",
      "name": "Clasificador AI",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.4,
      "position": [
        620,
        400
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        }
      },
      "id": "b2c3d4e5-f6g7-4h8i-9j0k-l1m2n3o4p5q6",
      "name": "OpenAI Chat Model",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        620,
        600
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI",
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
      "id": "c3d4e5f6-g7h8-4i9j-0k1l-m2n3o4p5q6r7",
      "name": "Switch Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        880,
        400
      ]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "=🚨 *Nuevo ticket de Soporte*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "d4e5f6g7-h8i9-4j0k-1l2m-n3o4p5q6r7s8",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1150,
        250
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "sales",
        "text": "=💰 *Nueva Oportunidad de Ventas*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6g7h8-i9j0-4k1l-2m3n-o4p5q6r7s8t9",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1150,
        400
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "general",
        "text": "=📩 *Mensaje General*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "f6g7h8i9-j0k1-4l2m-3n4o-p5q6r7s8t9u0",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1150,
        550
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK",
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
            "node": "Clasificador AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador AI": {
      "main": [
        [
          {
            "node": "Switch Categoría",
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
            "node": "Clasificador AI",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoría": {
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

### Explicación técnica del Workflow:

1.  **Webhook Node**: Configurado para recibir peticiones `POST`. Espera un cuerpo JSON como este:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, mi pedido no ha llegado y quiero reclamar"
    }
    ```
2.  **Clasificador AI (Basic LLM Chain)**: 
    *   Utiliza un prompt estricto para evitar que la IA escriba frases largas. Le ordenamos que responda **solo** con una de las tres palabras: `soporte`, `ventas` u `otro`.
    *   He configurado el modelo `gpt-4o-mini` por ser extremadamente rápido y económico para tareas de clasificación.
    *   **Temperatura 0**: Fundamental para que la respuesta sea determinista y no "invente" categorías.
3.  **Switch Node**: 
    *   Toma el resultado del texto de la IA.
    *   Si el texto es exactamente "soporte" $\rightarrow$ Salida 0.
    *   Si el texto es exactamente "ventas" $\rightarrow$ Salida 1.
    *   Si el texto es exactamente "otro" $\rightarrow$ Salida 2.
4.  **Slack Nodes**: 
    *   Hay tres nodos independientes. Cada uno apunta a un canal diferente.
    *   Utilizan expresiones para recuperar el `email` y el `message` originales desde el nodo Webhook (usando `$node["Webhook"].json.body...`).

### Pasos para activarlo:
1. Copia el JSON anterior.
2. Ve a n8n y crea un nuevo Workflow.
3. Pega el JSON (`Ctrl+V` o `Cmd+V`).
4. Haz clic en los nodos de **OpenAI Chat Model** y **Slack** para seleccionar tus credenciales guardadas.
5. Cambia los nombres de los canales de Slack (`#support`, `#sales`, `#general`) por los IDs reales de tus canales si es necesario.
6. Haz clic en **Execute Workflow** y prueba enviando un POST mediante Postman o Curl.