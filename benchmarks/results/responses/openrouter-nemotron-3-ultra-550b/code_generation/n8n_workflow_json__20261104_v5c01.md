# Nemotron 3 Ultra 550B — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.26 | quality: 8.32
- latency_total: 59.316s | tokens_per_second: 65.9
- input_tokens: 133 | output_tokens: 3911
- judge_score: 3.8 | justificación: 

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

**Notas importantes antes de importar:**
1.  **Credenciales:** Debes configurar tus credenciales de **OpenAI** y **Slack** en n8n y seleccionarlas en los nodos correspondientes (marcados como `YOUR_OPENAI_CREDENTIAL_ID` y `YOUR_SLACK_CREDENTIAL_ID`).
2.  **Estructura de datos:** Se incluye un nodo **Set (Combinar Datos)** crucial para no perder el `email` y `message` original tras la clasificación de la IA.
3.  **Modelo IA:** Usa `gpt-4o-mini` (rápido y barato) con `response_format: json_object` para garantizar una salida parsable.
4.  **Webhook URL:** Al activar el workflow, la URL será `https://TU_DOMINIO_N8N/webhook/classify-message`.

```json
{
  "name": "Clasificador Mensajes -> Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "options": {
          "rawBody": false
        }
      },
      "id": "1",
      "name": "Webhook Recibir Mensaje",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "classify-message"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "options": {
          "responseFormat": "json_object"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un sistema de clasificación automática. Analiza el mensaje del usuario y clasifícalo EXCLUSIVAMENTE en una de estas tres categorías: 'soporte', 'ventas', 'otro'.\n\nCriterios:\n- 'soporte': Dudas técnicas, errores, bugs, accesos, problemas con producto/servicio.\n- 'ventas': Consultas de precios, planes, demos, facturación, contratos, upgrades.\n- 'otro': Spam, saludos sin contexto, consultas irrelevantes, errores de envío.\n\nResponde ÚNICAMENTE con un objeto JSON válido con la clave 'clasificacion'. Ejemplo: {\"clasificacion\": \"soporte\"}"
            },
            {
              "role": "user",
              "content": "Email: {{ $json.body.email }}\nMensaje: {{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "2",
      "name": "OpenAI Clasificar",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [
        500,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email",
              "name": "email",
              "value": "={{ $('Webhook Recibir Mensaje').item.json.body.email }}",
              "type": "string"
            },
            {
              "id": "message",
              "name": "message",
              "value": "={{ $('Webhook Recibir Mensaje').item.json.body.message }}",
              "type": "string"
            },
            {
              "id": "clasificacion",
              "name": "clasificacion",
              "value": "={{ $json.clasificacion }}",
              "type": "string"
            }
          ]
        },
        "options": {
          "keepOnlySet": false
        }
      },
      "id": "3",
      "name": "Combinar Datos (Set)",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "id": "soporte",
              "value1": "={{ $json.clasificacion }}",
              "operation": "equals",
              "value2": "soporte"
            },
            {
              "id": "ventas",
              "value1": "={{ $json.clasificacion }}",
              "operation": "equals",
              "value2": "ventas"
            }
          ]
        },
        "options": {
          "caseSensitive": false
        }
      },
      "id": "4",
      "name": "Switch Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        1000,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "*🔔 Nuevo ticket de SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "blockBuilder": {
            "blocks": []
          }
        }
      },
      "id": "5",
      "name": "Slack -> #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "*💰 Nueva oportunidad de VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "blockBuilder": {
            "blocks": []
          }
        }
      },
      "id": "6",
      "name": "Slack -> #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "*📥 Mensaje OTRO/General*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Clasificación IA:* {{ $json.clasificacion }}",
        "options": {
          "blockBuilder": {
            "blocks": []
          }
        }
      },
      "id": "7",
      "name": "Slack -> #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook Recibir Mensaje": {
      "main": [
        [
          {
            "node": "OpenAI Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Clasificar": {
      "main": [
        [
          {
            "node": "Combinar Datos (Set)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Combinar Datos (Set)": {
      "main": [
        [
          {
            "node": "Switch Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Clasificación": {
      "main": [
        [
          {
            "node": "Slack -> #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack -> #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack -> #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "meta": {
    "templateCredsSetupCompleted": true
  },
  "id": "1"
}
```

### Cómo importar y configurar:

1.  Copia el JSON anterior.
2.  En n8n, ve a **Workflows** → **Import** → pega el JSON → **Import**.
3.  Abre el workflow importado.
4.  **Nodo "OpenAI Clasificar"**: Haz clic en *Credentials* → Selecciona tu credencial de OpenAI.
5.  **Nodos Slack (x3)**: Haz clic en *Credentials* → Selecciona tu credencial de Slack (Bot Token con permisos `chat:write`, `channels:read`, `groups:read`).
6.  Verifica que los canales **#support**, **#sales** y **#general** existan en tu Slack y que el bot haya sido invitado a ellos (`/invite @TuBot`).
7.  Guarda y haz clic en **Execute Workflow** (o **Activate** para producción).
8.  Prueba con un `POST` a la URL del webhook (ej: `https://tu-n8n.com/webhook/classify-message`) con body:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Mi factura del mes pasado tiene un error en el IVA"
    }
    ```