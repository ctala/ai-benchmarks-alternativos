# Fugu Max — code_generation/n8n_workflow_json

- model_id: `sakana/fugu-max`
- success: True  | final: 6.44 | quality: 7.2
- latency_total: 22.966s | tokens_per_second: 177.0
- input_tokens: 212 | output_tokens: 4065
- judge_score: 3.0 | justificación: 

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

Aquí tienes el JSON completo del workflow listo para importar directamente en n8n (puedes copiar el código y pegarlo directamente en el lienzo de n8n con `Ctrl + V` o mediante la opción **Import from Clipboard**).

### JSON del Workflow

```json
{
  "name": "Clasificación de Mensajes con OpenAI a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-lead",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ],
      "webhookId": "incoming-lead-webhook"
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "prompt": {
          "messages": [
            {
              "role": "system",
              "content": "Eres un asistente de clasificación. Clasifica el mensaje del usuario en exactamente una de las siguientes tres categorías: 'soporte', 'ventas' u 'otro'. Responde únicamente con una palabra (la categoría elegida), en minúsculas y sin signos de puntuación."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "2",
      "name": "Clasificador OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.4,
      "position": [
        470,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CREDENTIAL_ID",
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
                  "caseSensitive": false,
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              }
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content.toLowerCase().trim() }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              }
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "3",
      "name": "Switch Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [
        690,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🛠️ *Nuevo ticket de Soporte*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "4",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        930,
        180
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nueva oportunidad de Ventas*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "5",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        930,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=💬 *Mensaje General / Otro*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "6",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        930,
        420
      ],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CREDENTIAL_ID",
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
            "node": "Clasificador OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificador OpenAI": {
      "main": [
        [
          {
            "node": "Switch Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Categoria": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Ventas",
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
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

---

### Configuración requerida tras importar:

1. **Credenciales**:
   - En el nodo **Clasificador OpenAI**, asigna tu credencial de API de OpenAI.
   - En los 3 nodos de **Slack**, selecciona tu credencial (Token Bot / OAuth). Asegúrate de que el bot de Slack tenga permisos para escribir en `#support`, `#sales` y `#general`.
2. **Estructura del Payload HTTP POST**:
   El Webhook espera un cuerpo JSON como este:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Hola, necesito una cotización para 15 licencias de su software."
   }
   ```
3. **Lógica de enrutamiento**:
   - Salida 0 (Regla 1): Mensajes clasificados como `soporte` → canal `#support`.
   - Salida 1 (Regla 2): Mensajes clasificados como `ventas` → canal `#sales`.
   - Salida 2 (Fallback / Otro): Cualquier otro caso → canal `#general`.