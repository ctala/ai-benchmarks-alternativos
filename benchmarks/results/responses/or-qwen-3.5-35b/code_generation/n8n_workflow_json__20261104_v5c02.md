# Qwen 3.5 35B — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 7.78 | quality: 8.6
- latency_total: 19.478s | tokens_per_second: 155.4
- input_tokens: 125 | output_tokens: 3027
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del flujo de trabajo especificados. La estructura es clara y organizada, facilitando la comprensión y la implementación. Aunque la profundidad es adecuada, podría haber incluido más detalles sobre la configuración de credenciales o manejo de errores para mejorar la utilidad práctica.

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

Aquí tienes el workflow completo en formato JSON listo para importar en n8n.

Este flujo sigue una arquitectura lineal y eficiente:
1.  **Webhook**: Recibe los datos.
2.  **LLM (OpenAI)**: Clasifica el texto.
3.  **Code (JavaScript)**: Convierte la clasificación de texto en el nombre del canal de Slack correspondiente.
4.  **Slack**: Envía el mensaje al canal dinámico.

### Instrucciones previas:
1.  Copia el código JSON de abajo.
2.  En tu instancia de n8n, ve a **Importar** (flecha hacia arriba en la barra lateral izquierda) y pega el contenido.
3.  **Importante**: Deberás configurar las credenciales manualmente:
    *   En el nodo **OpenAI**, conecta tu cuenta de OpenAI.
    *   En el nodo **Slack**, conecta tu cuenta de Slack.

```json
{
  "name": "Workflow de Clasificación de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        260,
        300
      ],
      "webhookId": "webhook-id-placeholder"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "content": "Clasifica el siguiente mensaje en una de estas tres categorías exactamente: 'soporte', 'ventas' o 'otro'. No devuelvas nada más que la palabra clave.",
              "role": "systemMessage"
            },
            {
              "content": "={{ $json.message }}",
              "role": "userMessage"
            }
          ]
        }
      },
      "id": "x9y8z7w6-v5u4-3210-zabc-def987654321",
      "name": "Clasificador IA (OpenAI)",
      "type": "n8n-nodes-base.chatPrompt",
      "typeVersion": 1.4,
      "position": [
        460,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "cred-openai-placeholder",
          "name": "Mi cuenta de OpenAI"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "// Obtenemos el resultado de la IA\nconst aiResponse = items[0].json.output;\n\n// Normalizamos la respuesta (quitar comillas si las trae)\nlet category = aiResponse.replace(/['\"]+/g, '').toLowerCase().trim();\n\nlet slackChannel = '';\n\nif (category === 'soporte') {\n  slackChannel = '#support';\n} else if (category === 'ventas') {\n  slackChannel = '#sales';\n} else {\n  slackChannel = '#general';\n}\n\n// Retornamos el objeto original añadiendo el canal calculado\nreturn [\n  {\n    json: {\n      email: items[0].json.email,\n      message: items[0].json.message,\n      slack_channel: slackChannel,\n      classification: category\n    }\n  }\n];",
        "inputFields": ""
      },
      "id": "p0o9i8u7-y6t5-4321-qwer-asdfghjklmno",
      "name": "Determinar Canal Slack",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        660,
        300
      ]
    },
    {
      "parameters": {
        "channel": "={{ $json.slack_channel }}",
        "text": "📩 *Nuevo Ticket*\n\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n\n🏷️ *Clasificado como:* {{ $json.classification }}",
        "otherOptions": {}
      },
      "id": "l1k2j3h4-g5f6-7890-dcba-zyxwvutsrqponm",
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        860,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "cred-slack-placeholder",
          "name": "Mi cuenta de Slack"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificador IA (OpenAI)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador IA (OpenAI)": {
      "main": [
        [
          {
            "node": "Determinar Canal Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Determinar Canal Slack": {
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
  },
  "active": false,
  "settings": {},
  "versionId": "workfow-version-id",
  "meta": {
    "instanceId": "instance-id-placeholder"
  },
  "tags": []
}
```