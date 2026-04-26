# Llama 3.3 70B (Groq) — code_generation/n8n_workflow_json

- model_id: `llama-3.3-70b-versatile`
- success: True  | final: 7.03 | quality: 7.08
- latency_total: 3.842s | tokens_per_second: 363.4
- input_tokens: 150 | output_tokens: 1396
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí te dejo el JSON del workflow de N8N que cumple con los requisitos solicitados:
```json
{
  "name": "Clasificación de mensajes",
  "nodes": [
    {
      "parameters": {},
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        100,
        100
      ],
      "webhookId": "clasificacion-mensajes"
    },
    {
      "parameters": {
        "function": "return { email: $json.body.email, message: $json.body.message };"
      },
      "name": "Extraer campos",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        300,
        100
      ]
    },
    {
      "parameters": {
        "function": "return { text: $input.message };"
      },
      "name": "Preparar texto para IA",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        500,
        100
      ]
    },
    {
      "parameters": {
        "modelName": "text-classification",
        "apiVersion": "2022-06-01",
        "modelId": "text-classification",
        "apiKey": "TU_API_KEY_DE_OPENAI",
        "text": "={{$json.text}}"
      },
      "name": "Clasificar mensaje con OpenAI",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        700,
        100
      ]
    },
    {
      "parameters": {
        "conditions": {
          "any": [
            {
              "value1": "={{$json.label}}",
              "value2": "soporte",
              "operation": {
                "type": "string",
                "value": "equals"
              }
            }
          ]
        }
      },
      "name": "Condición soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        900,
        100
      ]
    },
    {
      "parameters": {
        "conditions": {
          "any": [
            {
              "value1": "={{$json.label}}",
              "value2": "ventas",
              "operation": {
                "type": "string",
                "value": "equals"
              }
            }
          ]
        }
      },
      "name": "Condición ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        900,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "any": [
            {
              "value1": "={{$json.label}}",
              "value2": "otro",
              "operation": {
                "type": "string",
                "value": "equals"
              }
            }
          ]
        }
      },
      "name": "Condición otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        900,
        500
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Mensaje de soporte de {{=$json.email}}: {{=$json.message}}"
      },
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1200,
        100
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Mensaje de ventas de {{=$json.email}}: {{=$json.message}}"
      },
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1200,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Mensaje de {{=$json.email}}: {{=$json.message}}"
      },
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1200,
        500
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        "Extraer campos"
      ]
    },
    "Extraer campos": {
      "main": [
        "Preparar texto para IA"
      ]
    },
    "Preparar texto para IA": {
      "main": [
        "Clasificar mensaje con OpenAI"
      ]
    },
    "Clasificar mensaje con OpenAI": {
      "main": [
        "Condición soporte",
        "Condición ventas",
        "Condición otro"
      ]
    },
    "Condición soporte": {
      "main": [
        "Enviar a #support"
      ]
    },
    "Condición ventas": {
      "main": [
        "Enviar a #sales"
      ]
    },
    "Condición otro": {
      "main": [
        "Enviar a #general"
      ]
    }
  }
}
```
Recuerda reemplazar `TU_API_KEY_DE_OPENAI` con tu API key real de OpenAI.

Este workflow utiliza los siguientes nodos:

1. Webhook: recibe el mensaje POST y extrae el campo "email" y "message" del body.
2. Extraer campos: extrae el campo "email" y "message" del body del mensaje.
3. Preparar texto para IA: prepara el texto para ser enviado a la API de OpenAI.
4. Clasificar mensaje con OpenAI: clasifica el mensaje utilizando la API de OpenAI.
5. Condición soporte, Condición ventas, Condición otro: comprueban la clasificación del mensaje y envían el mensaje a un canal de Slack diferente según la clasificación.
6. Enviar a #support, Enviar a #sales, Enviar a #general: envían el mensaje a un canal de Slack diferente según la clasificación.

Espero que esto te ayude. ¡Si tienes alguna pregunta, no dudes en preguntar!