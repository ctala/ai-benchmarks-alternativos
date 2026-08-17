# Llama 4 Scout 17B (Groq preview) — code_generation/n8n_workflow_json

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 7.89 | quality: 8.68
- latency_total: 2.145s | tokens_per_second: 365.5
- input_tokens: 124 | output_tokens: 784
- judge_score: 4.2 | justificación: 

## Respuesta completa

Aquí te dejo el JSON del workflow de N8N que cumple con tus requisitos:
```json
{
  "name": "Clasificador de mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "path": "/webhook",
        "method": "POST",
        "bodyParametersUi": [],
        "option": "let-empty",
        "validateBody": true,
        "name": "Webhook",
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 1,
        "position": [
          100,
          100
        ]
      }
    },
    {
      "parameters": {
        "json": "={{$json}}"
      },
      "name": "Extraer datos",
      "type": "n8n-nodes-base.json",
      "typeVersion": 1,
      "position": [
        300,
        100
      ]
    },
    {
      "parameters": {
        "model": "text-davinci-003",
        "prompt": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro': {{$json["message"]}}",
        "maxTokens": 100,
        "temperature": 0.5,
        "topP": 1,
        "frequencyPenalty": 0,
        "presencePenalty": 0
      },
      "name": "Clasificador de IA (OpenAI)",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        500,
        100
      ],
      "credentials": {
        "apiKey": "TU_API_KEY_DE_OPENAI"
      }
    },
    {
      "parameters": {
        "channel": "={{ $json["classification"] === 'soporte' ? '#support' : $json["classification"] === 'ventas' ? '#sales' : '#general' }}",
        "token": "TU_TOKEN_DE_SLACK",
        "text": "Nuevo mensaje de {{$json["email"]}}: {{$json["message"]}}"
      },
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        700,
        100
      ],
      "credentials": {
        "token": "TU_TOKEN_DE_SLACK"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "Extraer datos": [
        {
          "index": 0
        }
      ]
    },
    "Extraer datos": {
      "Clasificador de IA (OpenAI)": [
        {
          "index": 0
        }
      ]
    },
    "Clasificador de IA (OpenAI)": {
      "Enviar a Slack": [
        {
          "index": 0
        }
      ]
    }
  }
}
```
Recuerda reemplazar `TU_API_KEY_DE_OPENAI` y `TU_TOKEN_DE_SLACK` con tus credenciales reales de OpenAI y Slack.

Este workflow consta de 4 nodos:

1. **Webhook**: activa el workflow con un webhook POST en `/webhook`.
2. **Extraer datos**: extrae los campos `email` y `message` del cuerpo del mensaje.
3. **Clasificador de IA (OpenAI)**: utiliza el modelo de lenguaje de OpenAI para clasificar el mensaje como "soporte", "ventas" o "otro".
4. **Enviar a Slack**: envía el email a un canal de Slack diferente según la clasificación.

Espero que esto te ayude. ¡Si tienes alguna pregunta o necesitas más ayuda, no dudes en preguntar!