# Mistral Large 3 675B (NIM) — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 7.01 | quality: 8.6
- latency_total: 86.945s | tokens_per_second: 11.7
- input_tokens: 115 | output_tokens: 1013
- judge_score: 4.0 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo de un workflow de n8n que cumple con tus requisitos:

```json
{
  "name": "Clasificación de mensajes y envío a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "webhook",
        "responseMode": "onReceived",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "your-webhook-id"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "=Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\". Responde únicamente con una de estas tres palabras:\n\nMensaje: {{$json[\"message\"]}}",
        "options": {
          "temperature": 0.7,
          "top_p": 1,
          "presence_penalty": 0,
          "frequency_penalty": 0
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
          "id": "your-openai-credentials-id",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "channel": "={{$node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"] === \"soporte\" ? \"#support\" : ($node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"] === \"ventas\" ? \"#sales\" : \"#general\")}}",
        "text": "=Nuevo mensaje de: {{$json[\"email\"]}}\n\nMensaje:\n{{$json[\"message\"]}}",
        "as_user": false,
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
          "id": "your-slack-credentials-id",
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
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "your-workflow-id"
}
```

### Instrucciones para configurar el workflow:

1. **Webhook**:
   - El nodo webhook se activará con cualquier POST que envíes a la URL que te proporcione n8n.

2. **OpenAI**:
   - Necesitarás configurar tus credenciales de OpenAI (API Key).
   - El prompt está diseñado para que la IA solo responda con una de las tres palabras ("soporte", "ventas" o "otro").

3. **Slack**:
   - Necesitarás configurar tus credenciales de Slack (OAuth o Token).
   - El canal se selecciona dinámicamente basado en la respuesta de OpenAI.
   - El mensaje incluirá el email y el contenido del mensaje original.

4. **Configuración adicional**:
   - Reemplaza `your-webhook-id`, `your-openai-credentials-id`, `your-slack-credentials-id` y `your-workflow-id` con los IDs correspondientes de tu instancia de n8n.
   - Asegúrate de tener instalados y configurados los nodos de OpenAI y Slack en tu instancia de n8n.

### Ejemplo de payload esperado:
```json
{
  "email": "usuario@example.com",
  "message": "Tengo problemas para iniciar sesión en mi cuenta"
}
```

Este workflow procesará el payload, clasificará el mensaje y lo enviará al canal correspondiente de Slack.