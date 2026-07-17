# Mistral Large 3 675B — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.79 | quality: 8.6
- latency_total: 14.945s | tokens_per_second: 74.5
- input_tokens: 120 | output_tokens: 1114
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos especificados, y está claramente estructurada para su implementación, aunque carece de profundidad adicional más allá de la funcionalidad básica.

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
        "prompt": "=Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\" según su contenido. Solo responde con una de estas tres palabras:\n\nMensaje: {{$json[\"message\"]}}",
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
        "channel": "={{$json[\"category\"] === 'soporte' ? '#support' : ($json[\"category\"] === 'ventas' ? '#sales' : '#general')}}",
        "text": "=Nuevo mensaje de: {{$json[\"email\"]}}\n\nMensaje:\n{{$json[\"message\"]}}",
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
        "jsCode": "const category = $input.all()[0].json.choices[0].message.content.trim().toLowerCase();\n\nreturn {\n  email: $input.all()[0].json.email,\n  message: $input.all()[0].json.message,\n  category: category\n};"
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
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "id": "1"
}
```

### Instrucciones para configurar el workflow:

1. **Webhook**:
   - El nodo webhook recibirá las peticiones POST con el cuerpo que contenga `email` y `message`.

2. **OpenAI**:
   - Necesitarás configurar tus credenciales de OpenAI en n8n.
   - El prompt está diseñado para que la IA solo responda con una de las tres categorías.

3. **Code**:
   - Este nodo procesa la respuesta de OpenAI para extraer la categoría y mantener los datos originales.
   - Asegúrate de que la respuesta de OpenAI sea consistente (solo una palabra en minúsculas).

4. **Slack**:
   - Configura tus credenciales de Slack en n8n.
   - El nodo enviará el mensaje al canal correspondiente según la categoría.

5. **Activación**:
   - Activa el workflow en n8n para que el webhook esté disponible.

### Notas importantes:
- Reemplaza los IDs de las credenciales (`"id": "1"` y `"id": "2"`) con los IDs reales de tus credenciales en n8n.
- El `webhookId` es un ejemplo, n8n generará uno nuevo cuando actives el workflow.
- Asegúrate de que los canales de Slack (`#support`, `#sales`, `#general`) existan en tu espacio de trabajo.