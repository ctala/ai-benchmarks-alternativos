# GLM 5 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5`
- success: True  | final: 7.39 | quality: 8.6
- latency_total: 92.861s | tokens_per_second: 75.8
- input_tokens: 126 | output_tokens: 7038
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos especificados para el workflow de N8N. Aunque la profundidad es adecuada, podría haber incluido más detalles sobre la configuración de Slack o manejo de errores. La claridad y utilidad práctica son altas, permitiendo a un emprendedor implementar el workflow directamente.

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

Aquí tienes el JSON completo del workflow de n8n. Cumple con todos los requisitos que has especificado. 

Para utilizarlo, simplemente copia todo el código JSON, ve a tu instancia de n8n, haz clic en el lienzo (canvas) y pega (Ctrl+V / Cmd+V). 

```json
{
  "name": "Clasificar y Enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1-webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        0,
        0
      ],
      "webhookId": "webhook-unico-123"
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "create",
        "model": "gpt-4o-mini",
        "messages": {
          "messageValues": [
            {
              "role": "user",
              "content": "=Eres un asistente de clasificación. Lee el siguiente mensaje de un usuario y clasifícalo en una de las siguientes categorías: 'soporte', 'ventas', o 'otro'. Responde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin texto adicional.\n\nMensaje del usuario: {{$json.body.message}}"
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
        0
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $('Webhook').item.json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $('Webhook').item.json.body.message }}",
              "type": "string"
            },
            {
              "id": "classification-field",
              "name": "classification",
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "3-set",
      "name": "Extraer y Formatear",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.3,
      "position": [
        440,
        0
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
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "singleValue": false
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": "Soporte"
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
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "singleValue": false
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": "Ventas"
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
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals",
                      "singleValue": false
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": "Otro"
            }
          ]
        },
        "options": {}
      },
      "id": "4-switch",
      "name": "Clasificar Canal",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2.1,
      "position": [
        660,
        0
      ]
    },
    {
      "parameters": {
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje de Soporte*\n*Email:* {{$json.email}}\n*Mensaje:* {{$json.message}}",
        "otherOptions": {}
      },
      "id": "5-slack-soporte",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        880,
        -200
      ]
    },
    {
      "parameters": {
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje de Ventas*\n*Email:* {{$json.email}}\n*Mensaje:* {{$json.message}}",
        "otherOptions": {}
      },
      "id": "6-slack-ventas",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        880,
        0
      ]
    },
    {
      "parameters": {
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=*Nuevo mensaje General*\n*Email:* {{$json.email}}\n*Mensaje:* {{$json.message}}",
        "otherOptions": {}
      },
      "id": "7-slack-otro",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        880,
        200
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
            "node": "Extraer y Formatear",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer y Formatear": {
      "main": [
        [
          {
            "node": "Clasificar Canal",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Canal": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Notas importantes una vez lo importes:
1. **Credenciales**: Tendrás que abrir el nodo de *OpenAI* y el de *Slack* para configurar tus credenciales (API Keys) ya que n8n no importa credenciales sensibles por seguridad.
2. **Webhook**: El webhook estará activo en la ruta `https://tu-n8n.com/webhook/clasificar-mensaje`.
3. **Canales de Slack**: El workflow asume que tu bot de Slack ya está invitado a los canales `#support`, `#sales` y `#general`. Si el nombre exacto del canal difiere, puedes cambiarlo directamente en cada nodo de Slack.
4. **Prueba**: Puedes probar el webhook enviando un POST con un JSON así:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Hola, quiero comprar 100 licencias de su software"
   }
   ```