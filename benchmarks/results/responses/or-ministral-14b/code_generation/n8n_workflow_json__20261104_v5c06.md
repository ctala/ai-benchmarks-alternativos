# Ministral 14B — code_generation/n8n_workflow_json

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 8.16 | quality: 8.6
- latency_total: 21.398s | tokens_per_second: 53.2
- input_tokens: 120 | output_tokens: 1139
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos especificados con un enfoque claro y estructurado, aunque podría beneficiarse de una explicación adicional sobre la configuración de credenciales.

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

Aquí tienes el workflow completo en formato JSON para n8n, que cumple con todos los requisitos que mencionas:

```json
{
  "nodes": [
    {
      "parameters": {
        "resource": "webhook",
        "operation": "webhook",
        "path": "",
        "httpMethod": "POST",
        "authentication": "none",
        "options": {}
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
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Eres un clasificador de mensajes. Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas u otro. Responde solo con la categoría sin explicación."
          },
          {
            "role": "user",
            "content": "={{$json["message"]}}"
          }
        ],
        "temperature": 0,
        "maxTokens": 1,
        "apiKeyParameterName": "openaiApiKey",
        "options": {}
      },
      "name": "Classify Message",
      "type": "n8n-nodes-openai.chatCompletion",
      "typeVersion": 1,
      "position": [
        650,
        500
      ],
      "credentials": {
        "openaiApi": "openaiApiKey"
      }
    },
    {
      "parameters": {
        "resource": "slack",
        "operation": "sendMessage",
        "message": "={{$json[\"email\"]}}: {{json[\"message\"]}}",
        "channel": "={{$node["Classify Message"].json[\"choices\"][0][\"message\"][\"content\"] === 'soporte' ? '#support' : $node[\"Classify Message\"].json[\"choices\"][0][\"message\"][\"content\"] === 'ventas' ? '#sales' : '#general'}}",
        "apiKeyParameterName": "slackApiKey",
        "options": {}
      },
      "name": "Send to Slack",
      "type": "n8n-nodes-slack.sendMessage",
      "typeVersion": 1,
      "position": [
        850,
        700
      ],
      "credentials": {
        "slackApi": "slackApiKey"
      }
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{$json[\"email\"]}}"
            },
            {
              "name": "message",
              "value": "={{$json[\"message\"]}}"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Variables",
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
            "node": "Set Variables",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Variables": {
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
            "node": "Send to Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Explicación del workflow:

1. **Webhook Trigger**: Escucha solicitudes POST en la URL configurada en n8n.
2. **Set Variables**: Extrae los campos "email" y "message" del cuerpo de la solicitud (body).
3. **Classify Message**: Usa OpenAI para clasificar el mensaje en "soporte", "ventas" o "otro".
   - El prompt está configurado para que solo devuelva la categoría sin explicación.
4. **Send to Slack**: Envía el mensaje al canal correspondiente en Slack según la clasificación.

### Requisitos previos:
- Debes tener configuradas las credenciales para OpenAI y Slack en n8n.
- El webhook debe estar configurado correctamente en la instancia de n8n.

### Notas:
- El mensaje en Slack incluye tanto el email como el mensaje original.
- La clasificación se basa en el contenido del mensaje ("message").
- Asegúrate de que los canales de Slack (#support, #sales, #general) existan o ajusta los nombres según sea necesario.

Si necesitas ajustar algún detalle, como el modelo de OpenAI o el formato del mensaje en Slack, puedes modificar los parámetros correspondientes.