# Gemini 4 Argon — code_generation/n8n_workflow_json

- model_id: `google/gemini-4-argon`
- success: True  | final: 7.28 | quality: 8.6
- latency_total: 29.06s | tokens_per_second: 77.5
- input_tokens: 144 | output_tokens: 2252
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del flujo de trabajo con un JSON bien estructurado. Aunque la profundidad es adecuada, no ofrece insights adicionales más allá de la implementación básica. La claridad y utilidad práctica son altas, lo que permite a un emprendedor implementar el flujo de trabajo directamente.

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

Este flujo incluye:
1. **Webhook**: Configurado en método `POST` en la ruta `/clasificar-mensaje`.
2. **Edit Fields (Set)**: Extrae limpiamente `body.email` y `body.message`.
3. **OpenAI**: Usa el modelo `gpt-4o-mini` con un prompt estricto para responder únicamente con una de las tres categorías.
4. **Switch**: Evalúa la respuesta de la IA (en minúsculas por seguridad) y dirige el flujo.
5. **Nodos de Slack**: Envían el mensaje formateado al canal correspondiente.

### Código JSON del Workflow

Copia este código y pégalo directamente en tu lienzo de n8n (usando `Ctrl+V` o `Cmd+V`):

```json
{
  "name": "Clasificador de Mensajes con IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        200,
        300
      ],
      "webhookId": "a1b2c3d4-e5f6-7890-1234-56789abcdef0"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000002",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        420,
        300
      ]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "prompt": {
          "messages": [
            {
              "role": "system",
              "content": "Eres un asistente clasificador de correos. Debes clasificar el mensaje del usuario exactamente en una de estas tres categorías: \"soporte\", \"ventas\" u \"otro\". Responde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin signos de puntuación ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000003",
      "name": "OpenAI Clasificador",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        640,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.trim().toLowerCase() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "output": 0
            },
            {
              "value2": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000004",
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        860,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🛠️ *Nuevo ticket de Soporte*\n*De:* {{ $('Extraer Datos').item.json.email }}\n*Mensaje:* {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000005",
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1120,
        140
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nueva oportunidad de Ventas*\n*De:* {{ $('Extraer Datos').item.json.email }}\n*Mensaje:* {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000006",
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1120,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📌 *Nuevo mensaje general*\n*De:* {{ $('Extraer Datos').item.json.email }}\n*Mensaje:* {{ $('Extraer Datos').item.json.message }}",
        "otherOptions": {}
      },
      "id": "e1b9a240-12c3-4e2a-8b9f-000000000007",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1120,
        460
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
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
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
      "main": [
        [
          {
            "node": "OpenAI Clasificador",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Clasificador": {
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
  "settings": {}
}
```

### Pasos después de importar:
1. **Credenciales:** Abre el nodo `OpenAI Clasificador` y los 3 nodos de `Slack` para seleccionar tus propias credenciales.
2. **Canales de Slack:** Asegúrate de que tu Bot de Slack esté invitado a los canales `#support`, `#sales` y `#general`.
3. **Prueba:** Puedes probar el webhook haciendo una petición POST (con Postman o cURL) a la URL de prueba que te da el primer nodo enviando este JSON en el Body:
   ```json
   {
     "email": "cliente@empresa.com",
     "message": "Hola, no puedo iniciar sesión en mi cuenta, me da error 500."
   }
   ```