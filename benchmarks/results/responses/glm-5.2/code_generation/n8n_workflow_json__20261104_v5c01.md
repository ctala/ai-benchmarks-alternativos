# GLM 5.2 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.6 | quality: 8.6
- latency_total: 36.138s | tokens_per_second: 126.6
- input_tokens: 126 | output_tokens: 4575
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con nodos apropiados. La claridad es buena, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales y manejo de errores.

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

Aquí tienes el JSON completo del workflow de n8n. 

Este workflow incluye:
1. **Webhook**: Escucha peticiones POST.
2. **OpenAI**: Toma el mensaje del body y lo clasifica estrictamente en "soporte", "ventas" u "otro".
3. **Switch**: Enruta el flujo según la respuesta de la IA.
4. **Slack (x3)**: Envía el correo y el mensaje original a los canales `#support`, `#sales` o `#general`.

Para usarlo, simplemente copia este código, ve a tu instancia de n8n, haz clic en el lienzo (workspace) y pega (`Ctrl+V` o `Cmd+V`). Luego deberás configurar tus credenciales de OpenAI y Slack en los respectivos nodos.

```json
{
  "name": "Clasificador IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "1-webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        0,
        240
      ],
      "webhookId": "b9e1f2c3-1234-4567-890a-bcdef1234567"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "system",
              "content": "Eres un asistente que clasifica mensajes. Lee el siguiente mensaje y clasifícalo estrictamente como una de estas tres palabras: 'soporte', 'ventas' o 'otro'. Solo devuelve la palabra, sin puntuación ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "2-openai",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.4,
      "position": [
        220,
        240
      ]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "cond-otro",
                    "leftValue": "={{ $json.choices[0].message.content.trim().toLowerCase() }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {}
      },
      "id": "3-switch",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        440,
        240
      ]
    },
    {
      "parameters": {
        "select": "channelName",
        "channelId": "support",
        "text": "=🆕 *Nuevo mensaje de Soporte*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "4-slack-support",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        700,
        100
      ]
    },
    {
      "parameters": {
        "select": "channelName",
        "channelId": "sales",
        "text": "=💰 *Nuevo mensaje de Ventas*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "5-slack-sales",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        700,
        240
      ]
    },
    {
      "parameters": {
        "select": "channelName",
        "channelId": "general",
        "text": "=💬 *Nuevo mensaje General*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "6-slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        700,
        380
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
            "node": "Switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
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
1. **Credenciales**: Al importar el workflow, verás que los nodos de OpenAI y Slack tienen un aviso de que faltan credenciales. Haz clic en cada uno y selecciona o crea tus credenciales de OpenAI API y Slack Bot.
2. **Permisos de Slack**: Asegúrate de que tu App de Slack tenga los permisos `chat:write` y `channels:read` (o `groups:read` si son canales privados) y que esté invitada a los canales `#support`, `#sales` y `#general`.
3. **Prueba el Webhook**: El Webhook generará una URL de prueba. Puedes probarlo con un comando curl como este:
   ```bash
   curl -X POST https://TU_URL_DE_N8N/webhook/clasificar-mensaje \
   -H "Content-Type: application/json" \
   -d '{"email": "cliente@ejemplo.com", "message": "Hola, quiero comprar 100 licencias de su software"}'
   ```