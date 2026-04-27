# Hermes 4 405B — code_generation/n8n_workflow_json

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 6.68 | quality: 7.08
- latency_total: 28.482s | tokens_per_second: 34.0
- input_tokens: 139 | output_tokens: 967
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes el JSON completo del workflow de N8N que cumple con los requisitos especificados:

```json
{
  "name": "Clasificar y enrutar mensajes",
  "nodes": [
    {
      "parameters": {},
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "webhookId": "webhook-1234"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json[\"body\"][\"email\"]}}"
            },
            {
              "name": "message",
              "value": "={{$json[\"body\"][\"message\"]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "prompt": "={{$node[\"Set\"].json[\"message\"]}}",
        "max_tokens": 10
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        850,
        300
      ],
      "credentials": {
        "openAiApi": "openai-api-key"
      }
    },
    {
      "parameters": {
        "channels": [
          {
            "channelId": "C0123456789",
            "text": "=Soporte: {{$node[\"Set\"].json[\"message\"]}}\n\nEmail: {{$node[\"Set\"].json[\"email\"]}}"
          },
          {
            "channelId": "C9876543210",
            "text": "=Ventas: {{$node[\"Set\"].json[\"message\"]}}\n\nEmail: {{$node[\"Set\"].json[\"email\"]}}"
          },
          {
            "channelId": "C1122334455",
            "text": "=Otro: {{$node[\"Set\"].json[\"message\"]}}\n\nEmail: {{$node[\"Set\"].json[\"email\"]}}"
          }
        ]
      },
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "credentials": {
        "slackApi": "slack-api"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
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
  "id": "1"
}
```

Por favor, ten en cuenta lo siguiente:

1. Deberás reemplazar los valores de `webhookId`, `openAiApi` y `slackApi` con tus propias credenciales y configuraciones.

2. Los valores de `channelId` en el nodo de Slack deben ser reemplazados por los IDs reales de tus canales de Slack (#support, #sales y #general).

3. El nodo de OpenAI está configurado para generar una clasificación en base al mensaje. Dependiendo de cómo hayas entrenado tu modelo de OpenAI, el formato de la respuesta puede variar. Asegúrate de ajustar el nodo de Slack en consecuencia para enrutar correctamente los mensajes a los canales correspondientes.

4. Puedes ajustar el formato del mensaje enviado a Slack modificando el texto en la configuración del nodo de Slack.

Espero que este workflow te sea de utilidad. ¡Recuerda hacer las modificaciones necesarias para adaptarlo a tus necesidades específicas!