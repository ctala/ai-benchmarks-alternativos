# Nemotron 3 Super — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.48 | quality: 8.6
- latency_total: 224.553s | tokens_per_second: 43.9
- input_tokens: 133 | output_tokens: 9858
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un JSON bien estructurado, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos.

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

Aquí tienes el JSON completo del workflow listo para importar en n8n.  
Solo debes configurar las credenciales de **OpenAI** y **Slack** (reemplaza los IDs placeholder por los reales de tu instancia).

```json
{
  "name": "Clasificador de Mensajes con OpenAI y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        200,
        300
      ],
      "webhookId": "webhook-clasificador-001"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": [
          {
            "name": "email",
            "value": "={{ $json.email }}"
          },
          {
            "name": "message",
            "value": "={{ $json.message }}"
          }
        ],
        "options": {}
      },
      "id": "extract-data",
      "name": "Extraer email y message",
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
        "operation": "chat",
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario estrictamente como 'soporte', 'ventas' o 'otro'. Responde solo con una de esas tres palabras, sin explicaciones adicionales."
          },
          {
            "role": "user",
            "content": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
          }
        ],
        "options": {}
      },
      "id": "openai-classify",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        640,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "credential-openai-id"
        }
      }
    },
    {
      "parameters": {
        "keepOnlySet": false,
        "values": [
          {
            "name": "classification",
            "value": "={{ $json.choices[0].message.content.trim().toLowerCase() }}"
          }
        ],
        "options": {}
      },
      "id": "extract-classification",
      "name": "Extraer clasificación",
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        860,
        300
      ]
    },
    {
      "parameters": {
        "property": "={{ $json.classification }}",
        "rules": [
          {
            "value": "soporte",
            "output": 0
          },
          {
            "value": "ventas",
            "output": 1
          },
          {
            "value": "otro",
            "output": 2
          }
        ],
        "options": {}
      },
      "id": "route-classification",
      "name": "Enrutar por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1080,
        300
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje clasificado como *soporte*\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-support",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1320,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "credential-slack-id"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje clasificado como *ventas*\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-sales",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1320,
        400
      ],
      "credentials": {
        "slackApi": {
          "id": "credential-slack-id"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje clasificado como *otro*\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Slack - Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1320,
        600
      ],
      "credentials": {
        "slackApi": {
          "id": "credential-slack-id"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Extraer clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer clasificación": {
      "main": [
        [
          {
            "node": "Enrutar por Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por Clasificación": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Otro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "workflow-clasificador-slack-001"
}
```

### Notas importantes
1. **Credenciales**: Reemplaza `"credential-openai-id"` y `"credential-slack-id"` por los IDs reales de las credenciales configuradas en tu n8n.
2. **Webhook**: La URL del webhook será algo como `https://tu-n8n.com/webhook/clasificar-mensaje`.
3. **Entrada esperada**: El webhook espera un JSON con los campos `email` y `message`, por ejemplo:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Necesito ayuda con mi factura"
   }
   ```
4. **Clasificación**: El nodo de OpenAI responde con una de las tres palabras exactas (`soporte`, `ventas`, `otro`) y el nodo Switch envía el mensaje al canal de Slack correspondiente.