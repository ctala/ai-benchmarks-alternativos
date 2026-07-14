# Nemotron Super 49B v1.5 — code_generation/n8n_workflow_json

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 7.71 | quality: 8.4
- latency_total: 55.472s | tokens_per_second: 53.9
- input_tokens: 134 | output_tokens: 2991
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos especificados, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos y la gestión de errores.

## Respuesta completa

Aquí tienes el workflow completo en JSON para N8N que cumple con tus requisitos:

```json
{
  "nodes": [
    {
      "parameters": {
        "path": "webhook-classify",
        "method": "POST"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.Webhook",
      "typeVersion": 1,
      "position": [200, 100]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.email }}",
              "type": "string"
            },
            {
              "name": "message",
              "value": "={{ $json.message }}",
              "type": "string"
            }
          ]
        }
      },
      "name": "Extract Fields",
      "type": "n8n-nodes-base.Set",
      "typeVersion": 1,
      "position": [400, 100]
    },
    {
      "parameters": {
        "model": "text-davinci-003",
        "prompt": "Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas o otro.\nMensaje: {{ message }}\nCategoría:",
        "input": "message"
      },
      "name": "OpenAI Classifier",
      "type": "n8n-nodes-base.OpenAI",
      "typeVersion": 1,
      "credentials": {
        "OPENAI_API_KEY": "your-openai-credentials"
      },
      "position": [600, 100]
    },
    {
      "parameters": {
        "cases": [
          {
            "name": "soporte",
            "value": "soporte"
          },
          {
            "name": "ventas",
            "value": "ventas"
          },
          {
            "name": "otro",
            "value": "otro"
          }
        ],
        "mode": "structure"
      },
      "name": "Classify Router",
      "type": "n8n-nodes-base.Switch",
      "typeVersion": 1,
      "position": [800, 100]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Email: {{ email }}\nMensaje: {{ message }}"
      },
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.Slack",
      "typeVersion": 1,
      "credentials": {
        "slack": "your-slack-credentials"
      },
      "position": [1000, 100]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Email: {{ email }}\nMensaje: {{ message }}"
      },
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.Slack",
      "typeVersion": 1,
      "credentials": {
        "slack": "your-slack-credentials"
      },
      "position": [1000, 200]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Email: {{ email }}\nMensaje: {{ message }}"
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.Slack",
      "typeVersion": 1,
      "credentials": {
        "slack": "your-slack-credentials"
      },
      "position": [1000, 300]
    }
  ],
  "connections": {
    "Webhook": [
      {
        "node": "Extract Fields",
        "type": "main"
      }
    ],
    "Extract Fields": [
      {
        "node": "OpenAI Classifier",
        "type": "main"
      }
    ],
    "OpenAI Classifier": [
      {
        "node": "Classify Router",
        "type": "main"
      }
    ],
    "Classify Router": [
      {
        "node": "Slack - Soporte",
        "type": "main",
        "condition": [
          {
            "type": "equality",
            "parameter": "value",
            "value": "soporte"
          }
        ]
      },
      {
        "node": "Slack - Ventas",
        "type": "main",
        "condition": [
          {
            "type": "equality",
            "parameter": "value",
            "value": "ventas"
          }
        ]
      },
      {
        "node": "Slack - General",
        "type": "main",
        "condition": [
          {
            "type": "equality",
            "parameter": "value",
            "value": "otro"
          }
        ]
      }
    ]
  }
}
```

**Notas importantes:**

1. **Credenciales:**
   - Reemplaza `"your-openai-credentials"` con el nombre de tu credencial OpenAI configurada en N8N
   - Reemplaza `"your-slack-credentials"` con el nombre de tu credencial Slack configurada en N8N

2. **Funcionamiento:**
   - El webhook escucha en `/webhook-classify`
   - Extrae los campos `email` y `message` del body
   - Usa OpenAI para clasificar el mensaje
   - Enruta a diferentes canales de Slack según la clasificación

3. **Requisitos previos:**
   - Debes tener configuradas las credenciales para OpenAI y Slack en N8N
   - Asegúrate de tener los nodos correspondientes instalados

4. **Personalización:**
   - Puedes ajustar el prompt de OpenAI según tus necesidades
   - Modifica los mensajes de Slack según tu formato deseado

Para usar este workflow:
1. Copia el JSON
2. En N8N, crea un nuevo workflow
3. Usa el botón "Import" y pega el JSON
4. Configura las credenciales correspondientes
5. Active el webhook y pruebe el flujo