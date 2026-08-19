# Qwen 2.5 72B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 7.86 | quality: 8.6
- latency_total: 30.662s | tokens_per_second: 41.8
- input_tokens: 123 | output_tokens: 1282
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos y conexiones.

## Respuesta completa

Claro, a continuación te proporciono el JSON completo de un workflow de N8N que cumple con los requisitos que has mencionado:

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "url": "/webhook"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "jsonParameters": [
          {
            "name": "email",
            "value": "={{ $json['email'] }}"
          },
          {
            "name": "message",
            "value": "={{ $json['message'] }}"
          }
        ]
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "model": "text-davinci-003",
        "prompt": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro': {{ $json['message'] }}. Responde solo con una de estas palabras.",
        "maxTokens": 50
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json['return'] }}",
              "operation": "equals",
              "value2": "soporte"
            }
          ]
        }
      },
      "name": "If",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [
        1000,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte:\nEmail: {{ $json['email'] }}\nMensaje: {{ $json['message'] }}"
      },
      "name": "Slack1",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        250
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas:\nEmail: {{ $json['email'] }}\nMensaje: {{ $json['message'] }}"
      },
      "name": "Slack2",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        350
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje:\nEmail: {{ $json['email'] }}\nMensaje: {{ $json['message'] }}"
      },
      "name": "Slack3",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        450
      ]
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
            "node": "If",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If": {
      "main": [
        [
          {
            "node": "Slack1",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack2",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Explicación del Workflow:
1. **Webhook**: Este nodo se activa cuando se recibe una solicitud POST en el URL especificado.
2. **Set**: Este nodo extrae los campos "email" y "message" del cuerpo de la solicitud y los asigna a variables.
3. **OpenAI**: Este nodo utiliza la API de OpenAI para clasificar el mensaje como "soporte", "ventas" o "otro".
4. **If**: Este nodo evalúa la clasificación y dirige el flujo a uno de los nodos de Slack correspondientes.
5. **Slack1, Slack2, Slack3**: Estos nodos envían el mensaje a los canales de Slack correspondientes (#support, #sales, #general).

### Notas:
- Asegúrate de configurar las credenciales de OpenAI y Slack en la configuración de N8N.
- El nodo `OpenAI` utiliza el modelo `text-davinci-003` para la clasificación. Puedes ajustar el modelo según tus necesidades.
- El nodo `If` utiliza la salida de `OpenAI` para determinar a qué canal de Slack enviar el mensaje.

Este JSON debería ser importado en tu instancia de N8N para configurar el workflow.