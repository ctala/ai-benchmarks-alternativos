# Nemotron 3 Ultra 550B — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.68 | quality: 8.6
- latency_total: 17.032s | tokens_per_second: 169.3
- input_tokens: 133 | output_tokens: 2884
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con claridad y utilidad práctica, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores.

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n. 

**Notas importantes antes de importar:**
1.  **Credenciales:** Debes configurar tus credenciales de **OpenAI** (nombre interno: `openAiApi`) y **Slack** (nombre interno: `slackApi`) en n8n antes de activar el workflow.
2.  **Modelo OpenAI:** Usa `gpt-4o-mini` o `gpt-3.5-turbo` (configurado en el nodo) para respuestas rápidas y baratas. Asegúrate de que tu clave de API tenga acceso.
3.  **Formato de salida IA:** El nodo de OpenAI usa `response_format: { "type": "json_object" }` para garantizar que la clasificación sea parseable por el nodo Switch.
4.  **Webhook URL:** Al activar el workflow, la URL de prueba será `https://TU_DOMINIO_N8N/webhook/classify-message` (o `/webhook-test/...` en modo test).

```json
{
  "name": "Clasificar y Enviar a Slack",
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
      "name": "Webhook Recibido",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0,
          "responseFormat": "json_object"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de negocio. Analiza el mensaje del usuario y clasifícalo EXCLUSIVAMENTE en una de estas tres categorías: 'soporte', 'ventas', 'otro'.\n\nReglas:\n- 'soporte': Problemas técnicos, errores, dudas de uso, bugs, accesos, facturación técnica.\n- 'ventas': Consultas de precios, demos, planes, contratos, renovaciones comerciales, upselling.\n- 'otro': Spam, saludos sin contexto, consultas irrelevantes, recursos humanos, proveedores.\n\nResponde ÚNICAMENTE con un objeto JSON válido con la clave 'category'. Ejemplo: {\"category\": \"soporte\"}"
            },
            {
              "role": "user",
              "content": "Email del remitente: {{ $json.email }}\n\nMensaje:\n{{ $json.message }}"
            }
          ]
        }
      },
      "id": "2",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [
        500,
        300
      ],
      "credentials": {
        "openAiApi": "openAiApi"
      }
    },
    {
      "parameters": {
        "mode": "strict",
        "rules": {
          "values": [
            {
              "value": "={{ $json.category }}",
              "operation": "equal",
              "key": "soporte"
            },
            {
              "value": "={{ $json.category }}",
              "operation": "equal",
              "key": "ventas"
            }
          ]
        }
      },
      "id": "3",
      "name": "Switch: Ruta por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🎫 *Nuevo Ticket de SOPORTE*\n*Email:* {{ $('Webhook Recibido').item.json.email }}\n*Mensaje:* {{ $('Webhook Recibido').item.json.message }}",
        "options": {
          "blockFields": {}
        }
      },
      "id": "4",
      "name": "Slack: Soporte (#support)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1000,
        150
      ],
      "credentials": {
        "slackApi": "slackApi"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nueva Oportunidad de VENTAS*\n*Email:* {{ $('Webhook Recibido').item.json.email }}\n*Mensaje:* {{ $('Webhook Recibido').item.json.message }}",
        "options": {
          "blockFields": {}
        }
      },
      "id": "5",
      "name": "Slack: Ventas (#sales)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1000,
        300
      ],
      "credentials": {
        "slackApi": "slackApi"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📥 *Mensaje CLASIFICADO COMO 'OTRO'*\n*Email:* {{ $('Webhook Recibido').item.json.email }}\n*Mensaje:* {{ $('Webhook Recibido').item.json.message }}\n*Categoría IA:* {{ $('Clasificar con OpenAI').item.json.category }}",
        "options": {
          "blockFields": {}
        }
      },
      "id": "6",
      "name": "Slack: General (#general)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1000,
        450
      ],
      "credentials": {
        "slackApi": "slackApi"
      }
    }
  ],
  "connections": {
    "Webhook Recibido": {
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
            "node": "Switch: Ruta por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch: Ruta por Categoría": {
      "main": [
        [
          {
            "node": "Slack: Soporte (#support)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: Ventas (#sales)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: General (#general)",
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
  "id": "workflow-clasificador-slack-01"
}
```

### Cómo importarlo:
1.  En n8n, ve a **Workflows** → **Import**.
2.  Pega el JSON en un archivo `.json` o directamente en el modal de importación (según tu versión de n8n).
3.  Abre el workflow.
4.  Haz clic en el nodo **"Clasificar con OpenAI"** → Credenciales → Selecciona tu credencial de OpenAI.
5.  Haz clic en los 3 nodos **Slack** → Credenciales → Selecciona tu credencial de Slack (Bot Token con permisos `chat:write`, `channels:read`, `groups:read`).
6.  Guarda y haz clic en **"Execute Workflow"** (para probar) o **"Activate"** (para producción).

### Estructura del Body para probar (POST a `/webhook/classify-message`):
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Hola, mi factura del mes pasado tiene un error en el IVA, ¿pueden revisarlo?"
}
```
*Debería ir a `#support`.*