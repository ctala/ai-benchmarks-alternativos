# Qwen 3.7 Flash — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.07 | quality: 7.2
- latency_total: 54.992s | tokens_per_second: 138.8
- input_tokens: 125 | output_tokens: 7632
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

Aquí tienes el workflow completo en formato JSON válido para n8n. Está estructurado para n8n v1.x y listo para importar directamente desde `Workflows > Import from File`.

```json
{
  "name": "Webhook → AI Classify → Slack Router",
  "nodes": [
    {
      "id": "webhook-trigger",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 300],
      "webhookId": "custom-classify-webhook",
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "respondNow",
        "responseData": "allEntries",
        "options": {}
      },
      "credentials": {}
    },
    {
      "id": "ai-classifier",
      "name": "AI Classifier",
      "type": "n8n-nodes-base.openai",
      "typeVersion": 4,
      "position": [460, 300],
      "parameters": {
        "operation": "chatModel",
        "model": "gpt-4o-mini",
        "systemPrompt": "Eres un clasificador empresarial. Analiza el mensaje y responde ÚNICAMENTE con una de estas tres palabras exactas: soporte, ventas, otro. No agregues explicaciones ni puntuación adicional.",
        "messages": "={{ $json.message }}"
      },
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "id": "route-switch",
      "name": "Route Classification",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [680, 300],
      "parameters": {
        "mode": "ruleBased",
        "rules": {
          "and": [
            {
              "conditions": {
                "operator": "eq",
                "value1": "={{ $json.output }}",
                "value2": "soporte"
              }
            },
            {
              "conditions": {
                "operator": "eq",
                "value1": "={{ $json.output }}",
                "value2": "ventas"
              }
            }
          ]
        }
      },
      "credentials": {}
    },
    {
      "id": "slack-support",
      "name": "Send to Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [900, 150],
      "parameters": {
        "resource": "channel",
        "operation": "send",
        "channel": "#support",
        "text": "📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🤖 Clasificación: {{ $json.output }}"
      },
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack Account"
        }
      }
    },
    {
      "id": "slack-sales",
      "name": "Send to Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [900, 300],
      "parameters": {
        "resource": "channel",
        "operation": "send",
        "channel": "#sales",
        "text": "📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🤖 Clasificación: {{ $json.output }}"
      },
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack Account"
        }
      }
    },
    {
      "id": "slack-general",
      "name": "Send to General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [900, 450],
      "parameters": {
        "resource": "channel",
        "operation": "send",
        "channel": "#general",
        "text": "📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n🤖 Clasificación: {{ $json.output }}"
      },
      "credentials": {
        "slackApi": {
          "id": "TU_ID_CREDENCIAL_SLACK",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "AI Classifier",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "AI Classifier": {
      "main": [
        [
          {
            "node": "Route Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route Classification": {
      "main": [
        [
          {
            "node": "Send to Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send to General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Send to Support": {},
    "Send to Sales": {},
    "Send to General": {}
  },
  "settings": {
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "saveDataErrorExecution": "all",
    "saveDataSuccessExecution": "all",
    "executionTimeout": 3600,
    "errorWorkflow": ""
  },
  "staticData": null,
  "meta": {
    "templateCredsSetupCompleted": false,
    "instanceId": "imported-template"
  },
  "pinData": {},
  "versionId": "1",
  "triggerCount": null,
  "tags": []
}
```

### 📋 Instrucciones de configuración post-importación:

1. **Credenciales**:
   - Abre cada nodo en el canvas. En `Credentials`, reemplaza `TU_ID_CREDENCIAL_OPENAI` y `TU_ID_CREDENCIAL_SLACK` por las credenciales creadas en tu instancia de n8n (`Settings > Credentials`).
   - Si no las tienes, créalas primero: `OpenAI API` (con tu API Key) y `Slack API` (OAuth token con permisos `chat:write`).

2. **Webhook URL**:
   - Activa el workflow (`Toggle On`).
   - Copia la URL que aparece arriba del nodo `Webhook Trigger` (ej: `https://tu-instancia.n8n.cloud/webhook/classify-message`).
   - Esta es la URL que recibirás los `POST`.

3. **Formato esperado del payload**:
   ```json
   {
     "email": "cliente@ejemplo.com",
     "message": "Necesito ayuda con mi factura pendiente"
   }
   ```

4. **Notas técnicas**:
   - El nodo `Webhook` parsea automáticamente el JSON entrante, por lo que `{{ $json.email }}` y `{{ $json.message }}` están disponibles sin nodos intermedios.
   - El nodo OpenAI devuelve la clasificación en `{{ $json.output }}`. Si usas una versión antigua de n8n y el campo se llama `text`, cambia las condiciones del nodo `Route Classification` a `={{ $json.text }}`.
   - Los canales de Slack aceptan tanto `#support` como `support`. Si ves errores de canal no encontrado, quita el `#` en los parámetros.

¿Necesitas que ajuste alguna variante (ej: agregar autenticación al webhook, cambiar modelo de IA, o incluir respuesta HTTP personalizada)?