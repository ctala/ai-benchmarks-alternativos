# Mistral Large 3 675B — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 7.85 | quality: 8.6
- latency_total: 12.898s | tokens_per_second: 136.7
- input_tokens: 120 | output_tokens: 1763
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del workflow de N8N, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o posibles errores. La claridad y utilidad práctica son altas, ya que el JSON es comprensible y útil para implementar el workflow.

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

Aquí tienes el JSON completo de un workflow de n8n que cumple con tus requisitos:

```json
{
  "name": "Clasificador de Mensajes con IA y Slack",
  "nodes": [
    {
      "parameters": {
        "path": "webhook",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "a1b2c3d4-5678-90ef-ghij-klmnopqrstuv"
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "resource": "channel",
        "operation": "post",
        "channelId": "={{ $node[\"Switch\"].json[\"channel\"] }}",
        "text": "=Nuevo mensaje recibido:\n\n*Email:* {{ $node[\"Webhook\"].json[\"body\"][\"email\"] }}\n*Mensaje:* {{ $node[\"Webhook\"].json[\"body\"][\"message\"] }}\n*Clasificación:* {{ $node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"] }}",
        "otherOptions": {
          "unfurlLinks": false,
          "unfurlMedia": false
        }
      },
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "credentials": {
        "slackOAuth2Api": {
          "id": "1",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "=Clasifica el siguiente mensaje como \"soporte\", \"ventas\" o \"otro\". Solo responde con una de estas tres palabras:\n\nMensaje: {{ $node[\"Webhook\"].json[\"body\"][\"message\"] }}",
        "options": {
          "temperature": 0.3,
          "topP": 1,
          "frequencyPenalty": 0,
          "presencePenalty": 0
        }
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "2",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"].toLowerCase().trim() }}",
              "operation": "equals",
              "value2": "soporte"
            },
            {
              "value1": "={{ $node[\"OpenAI\"].json[\"choices\"][0][\"message\"][\"content\"].toLowerCase().trim() }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        },
        "combinator": "any"
      },
      "name": "Switch",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "channel",
              "value": "#support"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Soporte",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        1050,
        100
      ]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "channel",
              "value": "#sales"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Ventas",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "channel",
              "value": "#general"
            }
          ]
        },
        "options": {}
      },
      "name": "Set Otro",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        1050,
        500
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
            "node": "Set Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Set Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set Soporte": {
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
    "Set Ventas": {
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
    "Set Otro": {
      "main": [
        [
          {
            "node": "Slack",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {
    "executionOrder": "v1"
  },
  "id": "1"
}
```

### Notas importantes:

1. **Credenciales**: Deberás configurar tus propias credenciales para:
   - Slack (OAuth2)
   - OpenAI (API Key)

2. **Webhook ID**: El ID del webhook (`a1b2c3d4-5678-90ef-ghij-klmnopqrstuv`) es un placeholder. Cuando crees el workflow en n8n, se generará automáticamente uno nuevo.

3. **Canales de Slack**: Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu espacio de Slack y que el bot tenga permisos para publicar en ellos.

4. **Modelo de OpenAI**: El workflow usa `gpt-3.5-turbo`, pero puedes cambiarlo por otro modelo si lo prefieres.

5. **Formato del webhook**: El webhook espera un JSON con la estructura:
   ```json
   {
     "email": "usuario@example.com",
     "message": "Este es mi mensaje de ejemplo"
   }
   ```

Para importar este workflow en n8n, copia el JSON completo y usa la opción "Import from File/Clipboard" en la interfaz de n8n.