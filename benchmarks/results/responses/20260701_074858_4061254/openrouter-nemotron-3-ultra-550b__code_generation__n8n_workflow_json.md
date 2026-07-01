# Nemotron 3 Ultra 550B — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 25.569s | tokens_per_second: 142.9
- input_tokens: 133 | output_tokens: 3655

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n listo para importar.

**Notas importantes antes de importar:**
1.  **Credenciales:** Debes configurar tus credenciales de **OpenAI** y **Slack** en n8n y seleccionarlas en los nodos correspondientes (marcados con `"credentials": { ... }`).
2.  **Canales de Slack:** En los nodos de Slack (`Post to #support`, `Post to #sales`, `Post to #general`), cambia el valor del campo `channel` (actualmente `#support`, `#sales`, `#general`) por el **ID real del canal** (ej: `C01234567`) o el nombre exacto si tu credencial de Slack tiene permisos para resolver nombres.
3.  **Modelo OpenAI:** Usa `gpt-4o-mini` (recomendado por costo/velocidad) o `gpt-3.5-turbo`.
4.  **Webhook URL:** Al activar el workflow, la URL de prueba será `https://TU_DOMINIO_N8N/webhook/classify` y la de producción `https://TU_DOMINIO_N8N/webhook-test/classify`.

```json
{
  "name": "Clasificador Email a Slack (IA)",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify",
        "options": {
          "rawBody": false
        }
      },
      "id": "1",
      "name": "Webhook Recibido",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ],
      "webhookId": "classify-webhook-unique-id"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1b2c3d4-e5f6-7890-g1h2-i3j4k5l6m7n8",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "b2c3d4e5-f6g7-8901-h2i3-j4k5l6m7n8o9",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            },
            {
              "id": "c3d4e5f6-g7h8-9012-i3j4-k5l6m7n8o9p0",
              "name": "prompt",
              "value": "=Clasifica el siguiente mensaje de un cliente en UNA SOLA CATEGORÍA: 'soporte', 'ventas' u 'otro'.\n\nReglas:\n- 'soporte': Problemas técnicos, errores, bugs, dudas de uso, acceso, facturación técnica.\n- 'ventas': Consultas de precios, planes, demos, contratos, upgrades, nuevas funcionalidades para comprar.\n- 'otro': Spam, saludos sin contexto, quejas generales sin acción, temas legales/RRHH.\n\nResponde ÚNICAMENTE con un objeto JSON válido con la clave 'category'. Ejemplo: {\"category\": \"soporte\"}\n\nEmail del cliente: {{ $json.email }}\nMensaje: {{ $json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "2",
      "name": "Preparar Datos y Prompt",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {
          "temperature": 0.1,
          "maxTokens": 50
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador experto de tickets de soporte/ventas. Respondes SIEMPRE en formato JSON válido con una sola clave 'category'."
            },
            {
              "role": "user",
              "content": "={{ $json.prompt }}"
            }
          ]
        }
      },
      "id": "3",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.7,
      "position": [
        750,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "mode": "runOnceForAllItems",
        "jsCode": "/* Parsear la respuesta de OpenAI que viene en 'message.content' */\nconst responseContent = items[0].json.message?.content || '{}';\n\ntry {\n  const parsed = JSON.parse(responseContent);\n  // Devolvemos los datos originales + la categoría limpia\n  return [{\n    json: {\n      email: items[0].json.email,\n      message: items[0].json.message,\n      category: parsed.category?.toLowerCase().trim() || 'otro'\n    }\n  }];\n} catch (e) {\n  console.error('Error parseando JSON de IA:', responseContent);\n  // Fallback seguro\n  return [{\n    json: {\n      email: items[0].json.email,\n      message: items[0].json.message,\n      category: 'otro'\n    }\n  }];\n}"
      },
      "id": "4",
      "name": "Parsear Respuesta IA",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [
        1000,
        300
      ]
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "id": "rule-soporte",
              "value1": "={{ $json.category }}",
              "operation": "equal",
              "value2": "soporte",
              "output": "soporte"
            },
            {
              "id": "rule-ventas",
              "value1": "={{ $json.category }}",
              "operation": "equal",
              "value2": "ventas",
              "output": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "otro"
        }
      },
      "id": "5",
      "name": "Router (Switch)",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        1250,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🎫 *Nuevo Ticket SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "parseMode": "mrkdwn"
        }
      },
      "id": "6",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1500,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nueva Oportunidad VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "parseMode": "mrkdwn"
        }
      },
      "id": "7",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1500,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📥 *Mensaje OTRO / GENERAL*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.category }}",
        "options": {
          "parseMode": "mrkdwn"
        }
      },
      "id": "8",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1500,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook Recibido": {
      "main": [
        [
          {
            "node": "Preparar Datos y Prompt",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Preparar Datos y Prompt": {
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
            "node": "Parsear Respuesta IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parsear Respuesta IA": {
      "main": [
        [
          {
            "node": "Router (Switch)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router (Switch)": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Enviar a #general",
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
  "versionId": "1.0.0",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "workflow-instance-id"
  },
  "id": "workflow-id-clasificador-slack"
}
```

### Cómo usar este JSON:

1.  Copia el bloque de código superior.
2.  En n8n, ve a **Workflows** → **Import** (o el menú `...` → **Import from JSON**).
3.  Pega el JSON y guarda.
4.  **Configura Credenciales:**
    *   Abre el nodo **"Clasificar con OpenAI"** → Selecciona tu credencial `OpenAI Account`.
    *   Abre los 3 nodos de **Slack** (`Enviar a #support`, `#sales`, `#general`) → Selecciona tu credencial `Slack Account`.
5.  **Ajusta Canales Slack:** En cada nodo de Slack, cambia el campo **Channel** (`#support`, `#sales`, `#general`) por el **ID del canal** (ej: `C05XXXXXX`) para mayor robustez, o deja el nombre si tu bot tiene permisos `channels:read` y `groups:read`.
6.  Haz clic en **Test URL** en el nodo Webhook para obtener la URL de prueba.
7.  Envía un `POST` a esa URL con body:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Hola, mi factura del mes pasado tiene un error en el IVA"
    }
    ```
8.  Verifica que el mensaje aparezca en el canal de Slack correspondiente.