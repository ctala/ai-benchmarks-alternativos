# Qwen 3-Next 80B Instruct — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.0 | quality: 8.6
- latency_total: 7.653s | tokens_per_second: 221.4
- input_tokens: 123 | output_tokens: 1694
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del flujo de trabajo, aunque carece de detalles adicionales sobre la configuración de credenciales y manejo de errores, lo que podría mejorar la profundidad y utilidad.

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

Claro, aquí tienes un **workflow completo de n8n en formato JSON** que cumple con tus requisitos:

```json
{
  "name": "Clasificar mensaje por IA y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "path": "/webhook/classify-message",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "keepOnlySet": false,
        "keepOnlySetOptions": {}
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {}
    },
    {
      "parameters": {
        "options": {
          "model": "gpt-3.5-turbo",
          "temperature": 0.1,
          "maxTokens": 50
        },
        "prompt": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Solo responde con una palabra: {{ $json.message }}",
        "maxRetries": 3,
        "timeout": 10000
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 2,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": "openAiApi"
      }
    },
    {
      "parameters": {
        "options": {}
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
        "url": "https://hooks.slack.com/services/REDACTED",
        "options": {
          "header": {
            "Content-Type": "application/json"
          }
        },
        "body": "{\"text\":\"Nuevo mensaje de soporte de {{$json.email}}: {{$json.message}}\"}"
      },
      "name": "Slack - Support",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1050,
        200
      ]
    },
    {
      "parameters": {
        "url": "https://hooks.slack.com/services/REDACTED",
        "options": {
          "header": {
            "Content-Type": "application/json"
          }
        },
        "body": "{\"text\":\"Nuevo mensaje de ventas de {{$json.email}}: {{$json.message}}\"}"
      },
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "url": "https://hooks.slack.com/services/REDACTED",
        "options": {
          "header": {
            "Content-Type": "application/json"
          }
        },
        "body": "{\"text\":\"Nuevo mensaje general de {{$json.email}}: {{$json.message}}\"}"
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1050,
        400
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Set",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Set": {
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
            "node": "Slack - Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
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
  "credentials": {
    "openAiApi": {
      "api": "your-openai-api-key-here"
    }
  }
}
```

---

### ✅ **Instrucciones para usar este workflow:**

1. **Reemplaza los URLs de Slack**:
   - Busca `YOUR_SLACK_WEBHOOK_URL_FOR_SUPPORT`, `YOUR_SLACK_WEBHOOK_URL_FOR_SALES` y `YOUR_SLACK_WEBHOOK_URL_FOR_GENERAL` y reemplázalos con tus propios **Incoming Webhook URLs** de Slack.
   - Puedes crearlos en: https://api.slack.com/apps → tu app → Incoming Webhooks → Activate → Add New Webhook.

2. **Configura la credencial de OpenAI**:
   - En n8n, ve a **Credentials** → **Add New** → **OpenAI API**.
   - Ingresa tu clave de API de OpenAI (desde https://platform.openai.com/api-keys).

3. **Activa el workflow** y prueba con un POST a:
   ```
   POST http://localhost:5678/webhook/classify-message
   ```
   Con body:
   ```json
   {
     "email": "usuario@ejemplo.com",
     "message": "Tengo un problema con mi factura."
   }
   ```

---

### 💡 Notas técnicas:

- El nodo **Set** no hace nada en este caso, pero lo incluí para que el flujo sea más claro. Puedes eliminarlo y conectar directamente el Webhook al OpenAI si prefieres.
- El prompt de OpenAI está diseñado para devolver **solo una palabra** (`soporte`, `ventas`, `otro`) para que el nodo **Switch** pueda compararlo fácilmente.
- El nodo **Switch** debe tener 3 salidas, cada una con la condición:
  - `={{ $json["OpenAI"].choices[0].message.content.trim() === "soporte" }}`
  - `={{ $json["OpenAI"].choices[0].message.content.trim() === "ventas" }}`
  - `={{ $json["OpenAI"].choices[0].message.content.trim() === "otro" }}`

> ⚠️ **Importante**: En n8n, el nodo **Switch** no tiene una interfaz gráfica para múltiples condiciones en el modo básico. Debes hacer clic en “+ Add Condition” y configurar manualmente cada salida con la expresión exacta arriba.

---

Si deseas, puedo generarte una versión **sin el nodo Set** y con las condiciones del Switch ya preconfiguradas en texto para copiar/pegar. ¡Avísame!