# Gemma 4 31B — code_generation/n8n_workflow_json

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.82 | quality: 8.6
- latency_total: 49.906s | tokens_per_second: 38.7
- input_tokens: 128 | output_tokens: 1929
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y clara, proporcionando un JSON estructurado que cumple con los requisitos del workflow de n8n, aunque carece de profundidad en la explicación de la lógica detrás de la clasificación y el manejo de errores.

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

Para que este workflow funcione, necesitarás tener configuradas tus credenciales de **OpenAI** y **Slack** en n8n.

Aquí tienes el JSON completo. Para importarlo, simplemente copia el código y pégalo directamente en el lienzo (canvas) de tu editor de n8n.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-messages",
        "options": {}
      },
      "id": "7e8b3a1a-4b5c-4d6e-8f9g-0h1i2j3k4l5m",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [400, 400]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": "={{ 'Clasifica el siguiente mensaje en una de estas tres categorías: \"soporte\", \"ventas\" o \"otro\". Solo responde con una palabra (la categoría). No añadas puntuación ni explicaciones.\\n\\nMensaje: ' + $json.body.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4g7h-8i9j-k0l1m2n3o4p5",
      "name": "AI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [620, 400],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "value1": "={{ $json.choices[0].message.content.toLowerCase().trim() }}",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.choices[0].message.content.toLowerCase().trim() }}",
              "value2": "ventas"
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "b2c3d4e5-f6g7-4h8i-9j0k-l1m2n3o4p5q6",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [840, 400]
    },
    {
      "parameters": {
        "channel": "support",
        "text": "={{ \"📩 *Nuevo ticket de soporte*\\n📧 Email: \" + $node[\"Webhook\"].json.body.email + \"\\n💬 Mensaje: \" + $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "c3d4e5f6-g7h8-4i9j-0k1l-m2n3o4p5q6r7",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1060, 300],
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
        "text": "={{ \"💰 *Nueva oportunidad de ventas*\\n📧 Email: \" + $node[\"Webhook\"].json.body.email + \"\\n💬 Mensaje: \" + $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "d4e5f6g7-h8i9-4j0k-1l2m-n3o4p5q6r7s8",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1060, 400],
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
        "text": "={{ \"📝 *Mensaje General*\\n📧 Email: \" + $node[\"Webhook\"].json.body.email + \"\\n💬 Mensaje: \" + $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6g7h8-i9j0-4k1l-2m3n-o4p5q6r7s8t9",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1060, 500],
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
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
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

### Detalles de la implementación:

1.  **Webhook**: Está configurado para escuchar en la ruta `/classify-messages`. Espera un JSON como este:
    ```json
    {
      "email": "usuario@ejemplo.com",
      "message": "Hola, mi cuenta no funciona y no puedo entrar"
    }
    ```
2.  **AI Classifier (OpenAI)**: Utiliza un prompt estrictamente definido para que la IA solo responda con una de las tres palabras clave. He usado el modelo `gpt-4o-mini` por ser rápido y económico.
3.  **Switch (Route by Category)**:
    - Salida 0 $\rightarrow$ Si la respuesta es "soporte".
    - Salida 1 $\rightarrow$ Si la respuesta es "ventas".
    - Salida 2 (Fallback) $\rightarrow$ Cualquier otra cosa (va a `#general`).
4.  **Slack**: Cada nodo de Slack utiliza expresiones para recuperar el `email` y el `message` originales desde el nodo del Webhook, asegurando que la información llegue completa aunque la IA solo haya devuelto la categoría.

### Pasos para activar:
1. Copia el JSON.
2. En n8n, crea un nuevo workflow y pega el código.
3. Haz clic en los nodos de **OpenAI** y **Slack** para seleccionar tus credenciales ya creadas.
4. Dale a **"Execute Workflow"** y envía una prueba mediante Postman o cURL al URL del webhook.