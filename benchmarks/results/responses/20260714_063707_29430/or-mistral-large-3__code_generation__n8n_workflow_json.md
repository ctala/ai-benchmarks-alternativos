# Mistral Large 3 675B — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.78 | quality: 8.6
- latency_total: 16.277s | tokens_per_second: 69.9
- input_tokens: 120 | output_tokens: 1137
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos especificados, y está claramente organizada, lo que la hace útil para un emprendedor, aunque carece de profundidad adicional más allá de la funcionalidad básica.

## Respuesta completa

Aquí tienes el JSON completo de un workflow de n8n que cumple con tus requisitos:

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "=Clasifica el siguiente mensaje en una de estas categorías: \"soporte\", \"ventas\" o \"otro\".\n\nMensaje: {{ $json[\"message\"] }}\n\nResponde únicamente con una de estas palabras: soporte, ventas u otro. No añadas explicaciones ni puntuación.",
        "options": {
          "temperature": 0.7
        }
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "1",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "channel": "={{ $json[\"category\"] === 'soporte' ? '#support' : $json[\"category\"] === 'ventas' ? '#sales' : '#general' }}",
        "text": "=Nuevo mensaje de: {{ $json[\"email\"] }}\n\nMensaje:\n{{ $json[\"message\"] }}\n\nCategoría: {{ $json[\"category\"] }}",
        "attachments": [],
        "otherOptions": {}
      },
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "2",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "let category = $input.all()[0].json.choices[0].message.content.trim().toLowerCase();\n\nif (!['soporte', 'ventas', 'otro'].includes(category)) {\n  category = 'otro';\n}\n\nreturn {\n  email: $input.all()[0].json.email,\n  message: $input.all()[0].json.message,\n  category: category\n};"
      },
      "name": "Code",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
      "main": [
        [
          {
            "node": "Code",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Code": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {
    "executionOrder": "v1"
  },
  "id": "1"
}
```

### Notas importantes:

1. **Webhook**: Necesitarás reemplazar el `webhookId` con uno generado por n8n cuando crees el workflow.

2. **Credenciales**:
   - Debes configurar tus credenciales de OpenAI (nodo "OpenAI account")
   - Debes configurar tus credenciales de Slack (nodo "Slack account")

3. **Canales de Slack**: Asegúrate de que los canales #support, #sales y #general existan en tu espacio de Slack.

4. **Código**: El nodo Code procesa la respuesta de OpenAI para asegurarse de que siempre devuelva una de las tres categorías válidas.

5. **Modelo de OpenAI**: Puedes cambiar el modelo a "gpt-4" si lo prefieres, aunque gpt-3.5-turbo es más económico.

Para usar este workflow:
1. Cópialo en el editor de n8n (en la vista de código)
2. Configura las credenciales necesarias
3. Actívalo
4. Usa la URL del webhook que n8n te proporcione para enviar tus solicitudes POST