# GLM 5.1 (NIM) — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.42 | quality: 7.76
- latency_total: 263.16s | tokens_per_second: 10.1
- input_tokens: 114 | output_tokens: 2658
- judge_score: 3.4 | justificación: 

## Respuesta completa

Aquí tienes el flujo completo de n8n en formato JSON. 

He diseñado el flujo para que sea robusto y fácil de mantener. En lugar de crear 3 nodos de Slack separados (lo cual haría el flujo visualmente cargado y difícil de mantener), he utilizado un nodo **Switch** que inyecta el canal de Slack correspondiente en una variable, y un único nodo de Slack que lee esa variable. Además, el nodo de OpenAI está configurado para usar el *JSON mode* y devolver la clasificación de forma estructurada.

Copia y pega este JSON directamente en tu instancia de n8n:

```json
{
  "name": "Clasificación IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [0, 0],
      "webhookId": "mi-webhook-id"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-field",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-field",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "extract-fields",
      "name": "Extraer Email y Mensaje",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [220, 0]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "promptType": "define",
        "text": "=Clasifica el siguiente mensaje en una de estas tres categorías: 'soporte', 'ventas' o 'otro'.\n\nMensaje: {{ $json.message }}\n\nResponde ÚNICAMENTE con un objeto JSON válido con la clave 'clasificacion'. Ejemplo: {\"clasificacion\": \"ventas\"}"
      },
      "id": "openai-classify",
      "name": "OpenAI (Clasificador)",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [440, 0],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_ID",
          "name": "OpenAI API"
        }
      },
      "notes": "Asegúrate de configurar tu credencial de OpenAI aquí"
    },
    {
      "parameters": {
        "mode": "raw",
        "json": "={{ $json.text }}",
        "options": {}
      },
      "id": "parse-json",
      "name": "Parsear JSON de IA",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [660, 0],
      "notes": "Convierte el texto JSON de OpenAI en datos estructurados"
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.clasificacion }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "outputKey": "Soporte",
              "output": 0
            },
            {
              "value2": "ventas",
              "outputKey": "Ventas",
              "output": 1
            },
            {
              "value2": "otro",
              "outputKey": "Otro",
              "output": 2
            }
          ]
        },
        "fallbackOutput": 2,
        "options": {}
      },
      "id": "switch-node",
      "name": "Switch (Canal Slack)",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [880, 0]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "slack-channel",
              "name": "slackChannel",
              "value": "#support",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-soporte",
      "name": "Set #support",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [1100, -200]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "slack-channel",
              "name": "slackChannel",
              "value": "#sales",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-ventas",
      "name": "Set #sales",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [1100, 0]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "slack-channel",
              "name": "slackChannel",
              "value": "#general",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-otro",
      "name": "Set #general",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [1100, 200]
    },
    {
      "parameters": {
        "channel": "={{ $('Switch (Canal Slack)').item.json.slackChannel }}",
        "text": "=*:email: Nuevo mensaje clasificado*\n*De:* {{ $('Extraer Email y Mensaje').item.json.email }}\n*Clasificación:* {{ $('Parsear JSON de IA').item.json.clasificacion }}\n*Mensaje:* {{ $('Extraer Email y Mensaje').item.json.message }}",
        "otherOptions": {}
      },
      "id": "slack-send",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1320, 0],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack API"
        }
      },
      "notes": "Envía al canal dinámico definido en los nodos Set"
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={ \"status\": \"success\", \"classification\": \"{{ $('Parsear JSON de IA').item.json.clasificacion }}\" }",
        "options": {}
      },
      "id": "webhook-response",
      "name": "Respuesta al Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1540, 0]
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Extraer Email y Mensaje",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Email y Mensaje": {
      "main": [
        [
          {
            "node": "OpenAI (Clasificador)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI (Clasificador)": {
      "main": [
        [
          {
            "node": "Parsear JSON de IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parsear JSON de IA": {
      "main": [
        [
          {
            "node": "Switch (Canal Slack)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch (Canal Slack)": {
      "main": [
        [
          {
            "node": "Set #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set #support": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set #sales": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set #general": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack": {
      "main": [
        [
          {
            "node": "Respuesta al Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### ⚙️ Instrucciones de configuración una vez importado:

1. **Credenciales de OpenAI**: Abre el nodo `OpenAI (Clasificador)` y selecciona o crea una credencial de OpenAI. Te recomiendo usar el modelo `gpt-4o-mini` (ya puesto por defecto) porque es extremadamente barato y rápido para tareas de clasificación.
2. **Credenciales de Slack**: Abre el nodo `Slack` y conecta tu credencial de Slack (necesitarás un Bot Token con permisos `chat:write` y los canales deben estar invitados al bot en Slack).
3. **Nombres de los canales**: Revisa los nodos `Set #support`, `Set #sales` y `Set #general`. Si en Slack usas IDs en lugar de nombres de canales (ej. `C12345678`), cambia los valores `#support`, etc., por los IDs correspondientes.
4. **Formato del Body del Webhook**: Asegúrate de enviar el POST a tu webhook con este formato:
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Hola, quiero saber el precio de su licencia empresarial"
}
```

### 🧠 ¿Cómo funciona este flujo?
1. **Webhook**: Recibe el POST y captura el body.
2. **Set**: Extrae solo el `email` y `message` para pasarle a la IA solo lo que necesita.
3. **OpenAI**: Se le pide que clasifique y devuelva *estrictamente* un JSON `{"clasificacion": "ventas"}`.
4. **Code (Parsear)**: Convierte el texto que devuelve OpenAI en un objeto JSON para que n8n pueda leer la propiedad `clasificacion`.
5. **Switch**: Evalúa si la clasificación es soporte, ventas u otro.
6. **Nodos Set por rama**: Inyectan la variable `slackChannel` con el canal correspondiente (`#support`, `#sales`, `#general`).
7. **Slack**: Un único nodo Slack recoge el mensaje original y el canal dinámico para publicar el mensaje formateado con Markdown.
8. **Respond to Webhook**: Devuelve un código 200 con la clasificación realizada al sistema que hizo la petición POST.