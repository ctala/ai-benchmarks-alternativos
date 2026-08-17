# Nemotron 3 Ultra 550B — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 27.925s | tokens_per_second: 115.0
- input_tokens: 133 | output_tokens: 3211

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n. Está diseñado para la versión moderna de n8n (v1.0+) utilizando el nodo **OpenAI** con **Structured Output Parser** para garantizar una clasificación fiable en formato JSON, y un nodo **Switch** para el enrutamiento condicional.

```json
{
  "name": "Clasificación y Envío a Slack por IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook-trigger",
      "name": "Webhook Entrada",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-fields",
      "name": "Extraer Email y Mensaje",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [500, 300]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "options": {
          "temperature": 0.1
        },
        "promptType": "define",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de tickets de soporte. Analiza el mensaje del usuario y clasifícalo EXCLUSIVAMENTE en una de estas tres categorías: 'soporte', 'ventas', 'otro'.\n\nCriterios:\n- **soporte**: Problemas técnicos, errores, bugs, dudas de uso, accesos, facturación técnica.\n- **ventas**: Consultas de precios, planes, demos, upgrades, nuevos contratos, negociación.\n- **otro**: Spam, saludos genéricos sin consulta, quejas sin categoría clara, temas irrelevantes.\n\nResponde ÚNICAMENTE con el objeto JSON válido definido en el schema."
            },
            {
              "role": "user",
              "content": "Email del usuario: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "outputParser": "structured"
      },
      "id": "openai-classifier",
      "name": "Clasificar con IA (OpenAI)",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [750, 300],
      "credentials": {
        "openAiApi": "Tu_Credencial_OpenAI_Aqui"
      }
    },
    {
      "parameters": {
        "schemaType": "json",
        "jsonSchema": {
          "type": "object",
          "properties": {
            "categoria": {
              "type": "string",
              "enum": ["soporte", "ventas", "otro"],
              "description": "Categoría asignada al mensaje"
            },
            "confianza": {
              "type": "number",
              "minimum": 0,
              "maximum": 1,
              "description": "Nivel de confianza de la clasificación (0.0 a 1.0)"
            },
            "razon": {
              "type": "string",
              "description": "Breve explicación de por qué se eligió esta categoría"
            }
          },
          "required": ["categoria", "confianza", "razon"]
        }
      },
      "id": "structured-parser",
      "name": "Parser Salida Estructurada",
      "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
      "typeVersion": 1.1,
      "position": [750, 100]
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
        "options": {}
      },
      "id": "switch-routing",
      "name": "Switch: Enrutar por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [1000, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🎫 *Nuevo Ticket SOPORTE*\n*Email:* {{ $('Extraer Email y Mensaje').item.json.email }}\n*Mensaje:* {{ $('Extraer Email y Mensaje').item.json.message }}\n*Confianza IA:* {{ $json.confianza }}\n*Razón:* {{ $json.razon }}",
        "options": {}
      },
      "id": "slack-support",
      "name": "Slack: #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1250, 100],
      "credentials": {
        "slackApi": "Tu_Credencial_Slack_Aqui"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nueva Oportunidad VENTAS*\n*Email:* {{ $('Extraer Email y Mensaje').item.json.email }}\n*Mensaje:* {{ $('Extraer Email y Mensaje').item.json.message }}\n*Confianza IA:* {{ $json.confianza }}\n*Razón:* {{ $json.razon }}",
        "options": {}
      },
      "id": "slack-sales",
      "name": "Slack: #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1250, 300],
      "credentials": {
        "slackApi": "Tu_Credencial_Slack_Aqui"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📥 *Mensaje OTRO / GENERAL*\n*Email:* {{ $('Extraer Email y Mensaje').item.json.email }}\n*Mensaje:* {{ $('Extraer Email y Mensaje').item.json.message }}\n*Categoría IA:* {{ $json.categoria }}\n*Razón:* {{ $json.razon }}",
        "options": {}
      },
      "id": "slack-general",
      "name": "Slack: #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [1250, 500],
      "credentials": {
        "slackApi": "Tu_Credencial_Slack_Aqui"
      }
    },
    {
      "parameters": {
        "options": {},
        "respondWith": "json",
        "responseCode": 200,
        "responseData": {
          "success": true,
          "categoria": "={{ $json.categoria }}",
          "message": "Mensaje procesado y enviado a Slack correctamente"
        }
      },
      "id": "respond-webhook",
      "name": "Responder Webhook (OK)",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1500, 300]
    }
  ],
  "connections": {
    "Webhook Entrada": {
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
            "node": "Clasificar con IA (OpenAI)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parser Salida Estructurada": {
      "ai_outputParser": [
        [
          {
            "node": "Clasificar con IA (OpenAI)",
            "type": "ai_outputParser",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar con IA (OpenAI)": {
      "main": [
        [
          {
            "node": "Switch: Enrutar por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch: Enrutar por Categoría": {
      "main": [
        [
          {
            "node": "Slack: #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack: #support": {
      "main": [
        [
          {
            "node": "Responder Webhook (OK)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack: #sales": {
      "main": [
        [
          {
            "node": "Responder Webhook (OK)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack: #general": {
      "main": [
        [
          {
            "node": "Responder Webhook (OK)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "instanceId": "workflow-clasificacion-slack"
  }
}
```

### Instrucciones para usar este JSON:

1.  **Importar:** En n8n, ve a **Workflows** → **Import** → Selecciona el archivo `.json` o pega el contenido.
2.  **Credenciales (Obligatorio):**
    *   Abre el nodo **"Clasificar con IA (OpenAI)"** y selecciona/crea tu credencial **OpenAI API** en el campo `Credentials`.
    *   Abre los tres nodos de **Slack** (`#support`, `#sales`, `#general`) y selecciona/crea tu credencial **Slack API** (Bot Token con permisos `chat:write`, `channels:read`, `groups:read`).
3.  **Canales de Slack:** Asegúrate de que los canales `#support`, `#sales` y `#general` existan en tu workspace y que el Bot de Slack haya sido invitado a ellos (`/invite @TuBot`).
4.  **Modelo IA:** El workflow usa `gpt-4o-mini` (rápido y barato). Puedes cambiarlo a `gpt-4o` o `gpt-3.5-turbo` en el parámetro `model` del nodo OpenAI.
5.  **Activar:** Guarda el workflow y haz clic en **Execute Workflow** (para prueba manual) o **Activate** (para producción).
6.  **URL del Webhook:** Una vez activado, la URL pública será: `https://TU_DOMINIO_N8N/webhook/clasificar-mensaje`.

### Estructura del Body esperado (POST):
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Hola, mi factura del mes pasado tiene un error en el IVA."
}
```

### Respuesta del Webhook (JSON):
```json
{
  "success": true,
  "categoria": "soporte",
  "message": "Mensaje procesado y enviado a Slack correctamente"
}
```