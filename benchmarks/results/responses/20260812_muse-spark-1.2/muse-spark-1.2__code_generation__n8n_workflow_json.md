# Muse Spark 1.2 — code_generation/n8n_workflow_json

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 7.52 | quality: 8.6
- latency_total: 13.066s | tokens_per_second: 257.5
- input_tokens: 121 | output_tokens: 3365
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para un workflow de N8N que cumple con los requisitos especificados. La estructura es clara y organizada, lo que la hace útil para un emprendedor. Sin embargo, carece de profundidad adicional más allá de la implementación básica.

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

Aquí tienes el workflow completo listo para importar en n8n. Solo tienes que crear las credenciales de `OpenAI` y `Slack` y asignarlas a los nodos.

> **Cómo importarlo:** En n8n ve a `Workflows` > `Import from File` o `Import from Clipboard` y pega este JSON.

```json
{
  "name": "Clasificador IA Webhook a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificador-mensajes",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a5b-8c9d-1234567890ab",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        0,
        0
      ],
      "webhookId": "clasificador-mensajes-webhook-id"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-4b5c-9d0e-2345678901bc",
      "name": "Extraer email y message",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        220,
        0
      ]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Tu tarea es clasificar el mensaje del usuario en UNA sola palabra: soporte, ventas u otro. Responde ÚNICAMENTE con una de esas tres palabras en minúsculas, sin punto ni explicación.\n- soporte: si el usuario pide ayuda, tiene un problema, error, bug, no funciona algo.\n- ventas: si el usuario quiere comprar, pregunta por precios, planes, demos, contratar servicios.\n- otro: para cualquier otro caso."
            },
            {
              "role": "user",
              "content": "=Clasifica este mensaje: \"{{ $json.message }}\""
            }
          ]
        },
        "simplify": false,
        "responseFormat": "text"
      },
      "id": "c3d4e5f6-a7b8-4c5d-8e0f-3456789012cd",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.3,
      "position": [
        440,
        0
      ],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZA_CON_TU_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "categoria",
              "value": "={{ $json.message.content.trim().toLowerCase() }}",
              "type": "string"
            },
            {
              "id": "2",
              "name": "email",
              "value": "={{ $('Extraer email y message').item.json.email }}",
              "type": "string"
            },
            {
              "id": "3",
              "name": "message",
              "value": "={{ $('Extraer email y message').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "d4e5f6a7-b8c9-4d5e-9f0a-4567890123de",
      "name": "Normalizar Clasificacion",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        660,
        0
      ]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "value1": "={{ $json.categoria }}",
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.categoria }}",
              "operation": "equal",
              "value2": "ventas"
            },
            {
              "value1": "={{ $json.categoria }}",
              "operation": "equal",
              "value2": "otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra",
          "allMatchingOutputs": false
        }
      },
      "id": "e5f6a7b8-c9d0-4e5f-8a1b-5678901234ef",
      "name": "Switch por Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        880,
        0
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=📩 *Nuevo mensaje clasificado como SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.categoria }}",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-d0e1-4f5a-9b2c-6789012345fa",
      "name": "Slack - #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1100,
        -200
      ],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje clasificado como VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.categoria }}",
        "otherOptions": {}
      },
      "id": "a7b8c9d0-e1f2-4a5b-8c3d-7890123456ab",
      "name": "Slack - #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1100,
        0
      ],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=💬 *Nuevo mensaje clasificado como OTRO*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.categoria }}",
        "otherOptions": {}
      },
      "id": "b8c9d0e1-f2a3-4b5c-9d4e-8901234567bc",
      "name": "Slack - #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [
        1100,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZA_CON_TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          {
            "node": "Normalizar Clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Clasificacion": {
      "main": [
        [
          {
            "node": "Switch por Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por Categoria": {
      "main": [
        [
          {
            "node": "Slack - #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "instanceId": "workflow-clasificador-slack"
  }
}
```

### Qué hace cada nodo:

1.  **Webhook POST:** Se activa en `POST https://tu-n8n.com/webhook/clasificador-mensajes`. Espera un body JSON como este:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, quiero saber el precio del plan pro"
    }
    ```
2.  **Extraer email y message:** Normaliza el body y deja solo esos dos campos.
3.  **Clasificar con OpenAI:** Usa `gpt-4o-mini` para clasificar. Devuelve solo `soporte`, `ventas` u `otro`.
4.  **Normalizar Clasificacion:** Limpia la respuesta de la IA `.trim().toLowerCase()` para evitar errores de mayúsculas/espacios.
5.  **Switch por Categoria:** Enruta a 3 salidas diferentes según la categoría.
6.  **Slack - #support / #sales / #general:** Envía un mensaje formateado al canal correspondiente.

**Importante:** Después de importar, abre los nodos `Clasificar con OpenAI` y `Slack` y selecciona tus credenciales reales de OpenAI y Slack.