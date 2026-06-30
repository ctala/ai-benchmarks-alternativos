# Nemotron 3 Ultra 550B (NIM) — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 143.433s | tokens_per_second: 27.6
- input_tokens: 133 | output_tokens: 3964

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n.

**Notas importantes antes de importar:**
1.  **Nodo OpenAI:** He utilizado el nodo **Legacy `n8n-nodes-base.openAi`** (operación `chatCompletion`) porque es autocontenido (no requiere nodos LangChain adicionales como `Chain` o `Agent`) y funciona en la mayoría de instalaciones estándar de n8n sin configuración extra.
2.  **Credenciales:** Debes configurar las credenciales `OpenAI Api` y `Slack Api` en n8n y seleccionarlas en los nodos correspondientes (los placeholders `"credentials": { ... }` están vacíos).
3.  **Webhook URL:** Al activar el workflow, la URL de producción será algo como `https://tu-dominio.com/webhook/classify-message`.
4.  **Salida OpenAI:** El prompt fuerza a la IA a devolver **solo un JSON válido** (`{"categoria": "..."}`) para que el nodo `Switch` pueda leer el campo `categoria` correctamente.

```json
{
  "name": "Clasificar y Enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "responseData": {
          "options": {}
        },
        "options": {}
      },
      "id": "1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "webhookId": "classify-message-webhook"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0,
          "maxTokens": 50
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el email y el mensaje del usuario y devuelve ÚNICAMENTE un objeto JSON válido con la clave 'categoria'. Los valores permitidos son: 'soporte', 'ventas', 'otro'. No añadas texto extra, ni markdown, ni explicaciones.\n\nEjemplos:\n- \"Mi factura tiene un error\" -> {\"categoria\": \"soporte\"}\n- \"Quiero comprar 10 licencias\" -> {\"categoria\": \"ventas\"}\n- \"Hola, ¿cómo están?\" -> {\"categoria\": \"otro\"}"
            },
            {
              "role": "user",
              "content": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        }
      },
      "id": "2",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "credentials": {
        "openAiApi": "TU_CREDENCIAL_OPENAI_AQUI"
      }
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
      "id": "3",
      "name": "Switch: Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        750,
        300
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "🎫 *Nuevo ticket de SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "parseMode": "markdown"
        }
      },
      "id": "4",
      "name": "Slack: Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        100
      ],
      "credentials": {
        "slackApi": "TU_CREDENCIAL_SLACK_AQUI"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "💰 *Nueva oportunidad de VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "parseMode": "markdown"
        }
      },
      "id": "5",
      "name": "Slack: Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        300
      ],
      "credentials": {
        "slackApi": "TU_CREDENCIAL_SLACK_AQUI"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "📥 *Mensaje GENERAL*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "options": {
          "parseMode": "markdown"
        }
      },
      "id": "6",
      "name": "Slack: General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1000,
        500
      ],
      "credentials": {
        "slackApi": "TU_CREDENCIAL_SLACK_AQUI"
      }
    },
    {
      "parameters": {
        "options": {},
        "respondWith": "json",
        "responseCode": 200,
        "responseData": {
          "options": {}
        }
      },
      "id": "7",
      "name": "Responder OK",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ]
    }
  ],
  "connections": {
    "Webhook": {
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
            "node": "Switch: Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch: Categoría": {
      "main": [
        [
          {
            "node": "Slack: Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack: Soporte": {
      "main": [
        [
          {
            "node": "Responder OK",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack: Ventas": {
      "main": [
        [
          {
            "node": "Responder OK",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack: General": {
      "main": [
        [
          {
            "node": "Responder OK",
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
  "id": "1"
}
```

### Cómo importarlo:
1.  Copia el JSON de arriba.
2.  En n8n, ve a **Workflows** → **Import** (arriba a la derecha).
3.  Pega el JSON y dale a **Import**.
4.  Abre el workflow.
5.  Haz clic en el nodo **"Clasificar con OpenAI"** → Credentials → Selecciona tu credencial de **OpenAI Api**.
6.  Haz clic en los tres nodos **Slack** (Soporte, Ventas, General) → Credentials → Selecciona tu credencial de **Slack Api**.
6.  Guarda y haz clic en **Execute Workflow** (o **Test URL** para probar con el webhook de prueba).

### Ejemplo de Body para probar (POST):
```json
{
  "email": "cliente@ejemplo.com",
  "message": "Hola, mi factura del mes pasado tiene un importe incorrecto, necesito ayuda urgente."
}
```
*Debería clasificarse como `soporte` e ir a `#support`.*