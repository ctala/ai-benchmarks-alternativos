# Gemma 4 26B MoE (3.8B activos) — code_generation/n8n_workflow_json

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.98 | quality: 8.6
- latency_total: 36.142s | tokens_per_second: 60.0
- input_tokens: 128 | output_tokens: 2168
- judge_score: 4.0 | justificación: La respuesta proporciona un JSON preciso y relevante para el workflow de N8N, cubriendo los requisitos especificados, aunque carece de detalles adicionales sobre la configuración de credenciales y la finalización de nodos de Slack.

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

Para que este workflow funcione, necesitarás tener configuradas tus credenciales de **OpenAI** y **Slack** en n8n.

Aquí tienes el JSON completo. Para usarlo, simplemente copia el código de abajo, ve a tu n8n, crea un nuevo workflow y **pégalo directamente (Ctrl+V / Cmd+V)** en el lienzo.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificador-mensajes",
        "options": {}
      },
      "id": "56f8806c-8c8e-4e5d-9f7a-8e8e8e8e8e8e",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        400,
        400
      ]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "prompt": "={{ 'Clasifica el siguiente mensaje de un cliente en una de estas tres categorías: \"soporte\", \"ventas\" o \"otro\". \n\nSolo responde con una de esas tres palabras, sin puntos ni explicaciones.\n\nMensaje: ' + $json.body.message }}",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d",
      "name": "AI Classifier",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        620,
        400
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENTIAL_ID_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.text.toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.text.toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "ventas"
            }
          ]
        },
        "fallbackOutput": "otro"
      },
      "id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "name": "Switch Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        840,
        400
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🚨 *Nuevo Ticket de Soporte*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1100,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nueva Oportunidad de Ventas*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1100,
        400
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📩 *Nuevo Mensaje (Sin clasificar)*\n*Email:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [
        1100,
        600
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
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
            "node": "AI Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Classifier": {
      "main": [
        [
          {
            "node": "Switch Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Classification": {
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

### Explicación técnica del Workflow:

1.  **Webhook Node**: Escucha peticiones `POST`. El endpoint lo genera n8n automáticamente. Debes enviar un JSON como este:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, no puedo entrar a mi cuenta, necesito ayuda técnica."
    }
    ```
2.  **AI Classifier (OpenAI)**: Utiliza el modelo `gpt-4o-mini` (económico y rápido). Le pasamos el mensaje y le damos una instrucción estricta (*System Prompt*) para que **solo** devuelva una palabra: "soporte", "ventas" o "otro". Esto es crucial para que el siguiente nodo no falle.
3.  **Switch Classification**: Este nodo actúa como un router.
    *   Si el texto es "soporte" $\rightarrow$ Ruta 1.
    *   Si el texto es "ventas" $\rightarrow$ Ruta 2.
    *   Si no coincide con nada (Fallback) $\rightarrow$ Ruta 3 ("otro").
4.  **Slack Nodes**: Tres nodos independientes que envían el mensaje al canal correspondiente. He configurado el texto para que use expresiones que recuperan el `email` y el `message` original directamente desde el primer nodo (`Webhook`), asegurando que la información sea legible en Slack.

### Pasos para activar:
1.  **Credenciales**: Haz clic en los nodos de OpenAI y Slack para seleccionar tus propias cuentas.
2.  **Canales**: En los nodos de Slack, asegúrate de que los nombres de los canales (`#support`, `#sales`, `#general`) existan en tu workspace.
3.  **Test**: Haz clic en "Execute Workflow" y envía un comando `curl` o usa Postman para probar el webhook.