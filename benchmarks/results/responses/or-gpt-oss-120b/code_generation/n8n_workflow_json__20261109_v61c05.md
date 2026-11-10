# GPT-OSS 120B — code_generation/n8n_workflow_json

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.09 | quality: 8.6
- latency_total: 29.222s | tokens_per_second: 149.4
- input_tokens: 179 | output_tokens: 4365
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del workflow de N8N. La estructura es clara y organizada, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o posibles errores. Es práctica y útil para un emprendedor.

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

Aquí tienes el **workflow completo de n8n** en formato JSON.  
Cumple con los requisitos que pediste:

1. Se activa con un **webhook POST**.  
2. Extrae los campos **email** y **message** del cuerpo de la petición.  
3. Usa el nodo **OpenAI** para clasificar el mensaje como **soporte**, **ventas** o **otro**.  
4. Según la clasificación, envía un mensaje a un **canal de Slack** distinto.

```json
{
  "name": "Clasificador y envío a Slack",
  "id": "1",
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "parameters": {
        "httpMethod": "POST",
        "path": "receive"
      },
      "webhookId": "webhook-1"
    },
    {
      "name": "Extract fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        450,
        300
      ],
      "parameters": {
        "keepOnlySet": true,
        "values": [
          {
            "name": "email",
            "type": "json",
            "value": "={{$json[\"email\"]}}"
          },
          {
            "name": "message",
            "type": "json",
            "value": "={{$json[\"message\"]}}"
          }
        ]
      }
    },
    {
      "name": "Classify with OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "openAiCredentials",
          "name": "OpenAI API"
        }
      },
      "parameters": {
        "operation": "chatCompletion",
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "systemMessage": "Eres un clasificador. Debes leer el mensaje provisto y devolver solo una palabra: \"soporte\", \"ventas\" o \"otro\" según corresponda.",
        "userMessage": "={{$json[\"message\"]}}"
      }
    },
    {
      "name": "Extract classification",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        850,
        300
      ],
      "parameters": {
        "keepOnlySet": false,
        "values": [
          {
            "name": "category",
            "type": "json",
            "value": "={{$json[\"choices\"][0][\"message\"][\"content\"].trim().toLowerCase()}}"
          }
        ]
      }
    },
    {
      "name": "Switch by category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ],
      "parameters": {
        "value": "={{$json[\"category\"]}}",
        "rules": [
          {
            "value": "soporte",
            "output": "soporte"
          },
          {
            "value": "ventas",
            "output": "ventas"
          },
          {
            "value": "otro",
            "output": "otro"
          }
        ]
      }
    },
    {
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        150
      ],
      "credentials": {
        "slackApi": {
          "id": "slackCredentials",
          "name": "Slack API"
        }
      },
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje de **soporte** recibido:\n\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      }
    },
    {
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "slackCredentials",
          "name": "Slack API"
        }
      },
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje de **ventas** recibido:\n\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      }
    },
    {
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "slackCredentials",
          "name": "Slack API"
        }
      },
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje clasificado como **otro**:\n\n*Email:* {{$json[\"email\"]}}\n*Mensaje:* {{$json[\"message\"]}}"
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract fields": {
      "main": [
        [
          {
            "node": "Classify with OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify with OpenAI": {
      "main": [
        [
          {
            "node": "Extract classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract classification": {
      "main": [
        [
          {
            "node": "Switch by category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch by category": {
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
  },
  "settings": {},
  "active": false,
  "tags": [],
  "createdAt": "2026-11-10T00:00:00.000Z",
  "updatedAt": "2026-11-10T00:00:00.000Z",
  "versionId": "1"
}
```

### Qué hace cada nodo

| Nodo | Acción |
|------|--------|
| **Webhook** | Recibe una petición `POST` en `/webhook/receive`. |
| **Extract fields** | Saca `email` y `message` del cuerpo JSON y los deja disponibles para los siguientes nodos. |
| **Classify with OpenAI** | Envía el `message` a OpenAI (modelo *gpt‑3.5‑turbo*) con un prompt que obliga a devolver solo `soporte`, `ventas` o `otro`. |
| **Extract classification** | Toma la respuesta de OpenAI, la normaliza a minúsculas y la guarda en `category`. |
| **Switch by category** | Según el valor de `category` dirige el flujo a uno de los tres nodos de Slack. |
| **Slack Support / Slack Sales / Slack General** | Publican en los canales `#support`, `#sales` o `#general` respectivamente, incluyendo el email y el mensaje original. |

Solo debes añadir tus credenciales de **OpenAI** (`openAiCredentials`) y **Slack** (`slackCredentials`) en n8n y el workflow quedará listo para usar. ¡Éxitos!