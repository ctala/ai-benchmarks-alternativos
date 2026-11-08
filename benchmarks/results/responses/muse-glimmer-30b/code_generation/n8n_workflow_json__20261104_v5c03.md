# Muse Glimmer 30B — code_generation/n8n_workflow_json

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.58 | quality: 8.4
- latency_total: 21.01s | tokens_per_second: 166.7
- input_tokens: 170 | output_tokens: 3502
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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

Aquí tienes un workflow completo de n8n listo para importar. Hace POST -> extrae email/message -> clasifica con OpenAI -> envía a Slack según la clasificación.

```json
{
  "name": "Clasificador Email -> Slack",
  "nodes": [
    {
      "parameters": {
        "path": "classify",
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "id": "webhook-1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.message }}"
            }
          ]
        }
      },
      "id": "set-extract",
      "name": "Extract Data",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "chatCompletion",
        "operation": "create",
        "model": "gpt-4o-mini",
        "messages": {
          "values": {
            "string": [
              {
                "role": "system",
                "content": "Eres un clasificador. Clasifica el mensaje como soporte, ventas u otro. Responde solo con una de esas tres palabras en minúsculas."
              },
              {
                "role": "user",
                "content": "Mensaje: {{ $json.message }}"
              }
            ]
          },
          "options": {}
        }
      },
      "id": "openai-classify",
      "name": "Classify Message",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [680, 300]
    },
    {
      "parameters": {
        "keepExisting": true,
        "values": {
          "string": [
            {
              "name": "classification",
              "value": "={{ $json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase() }}"
            }
          ]
        }
      },
      "id": "set-normalize",
      "name": "Normalize Classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [900, 300]
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "rules": [
            {
              "value1": "soporte",
              "value2": "soporte"
            },
            {
              "value1": "ventas",
              "value2": "ventas"
            },
            {
              "value1": "otro",
              "value2": "otro"
            }
          ]
        },
        "value": "={{ $json.classification }}"
      },
      "id": "switch-route",
      "name": "Route by Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.1,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje de *soporte*\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "id": "slack-support",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1340, 200]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje de *ventas*\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "id": "slack-sales",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1340, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje de *otro*\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "id": "slack-general",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1340, 400]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Data": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Normalize Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize Classification": {
      "main": [
        [
          {
            "node": "Route by Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Classification": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    }
  }
}
```

**Cómo usarlo**
1. Importa el JSON en n8n.
2. Crea las credenciales de OpenAI y Slack.
3. El webhook quedará disponible en `https://<tu-dominio>/webhook/classify` con POST.
4. Envía `{"email":"...","message":"..."}` y el workflow clasificará y publicará en `#support`, `#sales` o `#general`.

Puedes cambiar el modelo de OpenAI o los textos de Slack según necesites.