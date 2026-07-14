# Ministral 14B — code_generation/n8n_workflow_json

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.3 | quality: 8.6
- latency_total: 11.35s | tokens_per_second: 109.1
- input_tokens: 120 | output_tokens: 1238
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

Aquí tienes el workflow completo en formato JSON para n8n que cumple con tus requisitos:

```json
{
  "nodes": [
    {
      "parameters": {
        "operation": "webhook",
        "specification": {
          "auth": "none",
          "headers": {
            "Content-Type": "application/json"
          },
          "body": {
            "mode": "raw",
            "raw": {
              "type": "json"
            }
          }
        }
      },
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "resource": "openai",
        "operation": "chatCompletion",
        "authentication": "openAiApi",
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas u otro. Responde solo con la categoría sin explicación."
          },
          {
            "role": "user",
            "content": "={{$json["message"]}}"
          }
        ],
        "temperature": 0,
        "maxTokens": 10
      },
      "name": "Clasificar Mensaje con OpenAI",
      "type": "n8n-nodes-openai.api",
      "typeVersion": 1,
      "position": [
        650,
        500
      ],
      "credentials": {
        "openAiApi": "YOUR_OPENAI_CREDENTIAL"
      }
    },
    {
      "parameters": {
        "resource": "slack",
        "operation": "sendMessage",
        "authentication": "slackApi",
        "channel": "={{$json["category"] === 'soporte' ? '#support' : $json["category"] === 'ventas' ? '#sales' : '#general'}}",
        "text": "Nuevo mensaje {{if $json[\"category\"] === 'soporte'}}🔧{{/if}}{{if $json[\"category\"] === 'ventas'}}💰{{/if}}:\n\nDe: {{ $json[\"email\"] }}\n\nMensaje:\n{{ $json[\"message\"] }}"
      },
      "name": "Enviar a Slack",
      "type": "n8n-nodes-slack.api",
      "typeVersion": 1,
      "position": [
        950,
        700
      ],
      "credentials": {
        "slackApi": "YOUR_SLACK_CREDENTIAL"
      }
    },
    {
      "parameters": {
        "keepOnlySet": true,
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
      "name": "Set Email y Message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        500
      ]
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Set Email y Message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Email y Message": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Mensaje con OpenAI": {
      "main": [
        [
          {
            "node": "Enviar a Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Notas importantes:

1. **Credenciales**:
   - Debes reemplazar `YOUR_OPENAI_CREDENTIAL` con el nombre de tu credencial de OpenAI configurada en n8n
   - Debes reemplazar `YOUR_SLACK_CREDENTIAL` con el nombre de tu credencial de Slack configurada en n8n

2. **Configuración del Webhook**:
   - Asegúrate de configurar correctamente el webhook en n8n (URL y método POST)
   - El webhook espera un JSON con estructura como: `{"email": "...", "message": "..."}`

3. **Lógica de clasificación**:
   - El nodo de OpenAI está configurado para responder solo con la categoría ("soporte", "ventas" o "otro")
   - El mensaje en Slack incluye emojis según la categoría para mejor visualización

4. **Alternativa para la clasificación**:
   Si prefieres una clasificación más determinista (sin depender de OpenAI), podrías usar un nodo "Function" con lógica condicional basada en palabras clave en el mensaje.

5. **Formato del mensaje en Slack**:
   El mensaje incluye el email del remitente y el contenido original, con formato visual diferente según la categoría.

Para implementar esto, primero crea los nodos en tu flujo de n8n y luego importa este JSON o configúralo manualmente siguiendo la estructura mostrada.