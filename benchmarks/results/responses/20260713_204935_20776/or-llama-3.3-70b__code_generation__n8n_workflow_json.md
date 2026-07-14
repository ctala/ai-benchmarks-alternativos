# Llama 3.3 70B — code_generation/n8n_workflow_json

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 5.17 | quality: 5.2
- latency_total: 136.486s | tokens_per_second: 12.9
- input_tokens: 125 | output_tokens: 1754
- judge_score: 2.0 | justificación: El JSON tiene errores significativos, como la falta de lógica de enrutamiento para los canales de Slack y la ausencia de condiciones para los nodos de Slack, lo que afecta la precisión y relevancia. La profundidad es baja ya que no se abordan las complejidades de la lógica de flujo de trabajo. Sin embargo, la claridad es aceptable, y la utilidad práctica es limitada debido a los errores.

## Respuesta completa

Aquí te dejo el JSON del workflow de N8N que solicitaste:

```json
{
  "name": "Clasificador de mensajes",
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
      "webhookId": "clasificador-de-mensajes"
    },
    {
      "parameters": {
        "function": "={{$json[\"body\"][\"email\"]}}"
      },
      "name": "Extraer email",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        300,
        100
      ]
    },
    {
      "parameters": {
        "function": "={{$json[\"body\"][\"message\"]}}"
      },
      "name": "Extraer mensaje",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        300,
        200
      ]
    },
    {
      "parameters": {
        "apiEndpoint": "https://api.openai.com/v1/",
        "apiVersion": "v1",
        "authentication": "apiKey",
        "apiKey": "YOUR_OPENAI_API_KEY",
        "model": "text-davinci-003",
        "prompt": "={{\"Clasifica el siguiente mensaje: \" + $node[\"Extraer mensaje\"].json[\"message\"] + \" como soporte, ventas u otro\"}}",
        "maxTokens": "256",
        "temperature": "0"
      },
      "name": "Clasificar mensaje",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        500,
        150
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "={{\"Soporte: \" + $node[\"Extraer mensaje\"].json[\"message\"] + \" de \" + $node[\"Extraer email\"].json[\"email\"]}}"
      },
      "name": "Enviar a soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        800,
        50
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "={{\"Ventas: \" + $node[\"Extraer mensaje\"].json[\"message\"] + \" de \" + $node[\"Extraer email\"].json[\"email\"]}}"
      },
      "name": "Enviar a ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        800,
        200
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "={{\"Otro: \" + $node[\"Extraer mensaje\"].json[\"message\"] + \" de \" + $node[\"Extraer email\"].json[\"email\"]}}"
      },
      "name": "Enviar a general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        800,
        350
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Clasificar mensaje\"].json.choices[0].text}}",
              "value2": "soporte",
              "operation": "equals"
            }
          ]
        }
      },
      "name": "Condicional soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        50
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Clasificar mensaje\"].json.choices[0].text}}",
              "value2": "ventas",
              "operation": "equals"
            }
          ]
        }
      },
      "name": "Condicional ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        200
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$node[\"Clasificar mensaje\"].json.choices[0].text}}",
              "value2": "otro",
              "operation": "equals"
            }
          ]
        }
      },
      "name": "Condicional otro",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        650,
        350
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          "Extraer email",
          {
            "id": "Extraer email",
            "type": "main",
            "index": 0
          }
        ],
        [
          "Extraer mensaje",
          {
            "id": "Extraer mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email": {
      "main": [
        [
          "Clasificar mensaje",
          {
            "id": "Clasificar mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer mensaje": {
      "main": [
        [
          "Clasificar mensaje",
          {
            "id": "Clasificar mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar mensaje": {
      "main": [
        [
          "Condicional soporte",
          {
            "id": "Condicional soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          "Condicional ventas",
          {
            "id": "Condicional ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          "Condicional otro",
          {
            "id": "Condicional otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Condicional soporte": {
      "main": [
        [
          "Enviar a soporte",
          {
            "id": "Enviar a soporte",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Condicional ventas": {
      "main": [
        [
          "Enviar a ventas",
          {
            "id": "Enviar a ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Condicional otro": {
      "main": [
        [
          "Enviar a general",
          {
            "id": "Enviar a general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

Recuerda que debes reemplazar `YOUR_OPENAI_API_KEY` con tu propia API key de OpenAI.

Este workflow se activa con un webhook POST, extrae el campo "email" y "message" del body, clasifica el mensaje como "soporte", "ventas" o "otro" utilizando un nodo de IA de OpenAI, y según la clasificación, envía el email a un canal de Slack diferente.

Ten en cuenta que este workflow utiliza la versión 1 de los nodos, por lo que si estás utilizando una versión más reciente de N8N, es posible que debas adaptar el workflow a la versión que estás utilizando.