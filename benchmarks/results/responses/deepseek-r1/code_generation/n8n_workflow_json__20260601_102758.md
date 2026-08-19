# DeepSeek R1 (reasoning) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 6.51 | quality: 8.4
- latency_total: 238.356s | tokens_per_second: 25.9
- input_tokens: 127 | output_tokens: 6175
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos especificados, aunque la profundidad podría mejorarse con más detalles sobre la configuración de credenciales o manejo de errores.

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n:

```json
{
  "name": "Clasificar Mensajes y Enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "/webhook-receptor"
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "webhookId": "clasificador-mensajes",
      "id": "1"
    },
    {
      "parameters": {
        "functionCode": "return {\n  email: $json.body.email,\n  message: $json.body.message\n};"
      },
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "id": "2"
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "options": {},
        "prompt": "Clasifica este mensaje en una sola palabra: 'soporte', 'ventas' o 'otro'. Mensaje: \"{{$json.message}}\"\nRespuesta:",
        "temperature": 0
      },
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "credentials": {
        "openAiApi": "openai-credentials"
      },
      "id": "3"
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "conditions": [
                {
                  "leftValue": "={{$json.response}}",
                  "operation": "contains",
                  "rightValue": "soporte"
                }
              ]
            },
            {
              "conditions": [
                {
                  "leftValue": "={{$json.response}}",
                  "operation": "contains",
                  "rightValue": "ventas"
                }
              ]
            }
          ]
        }
      },
      "name": "Router por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "id": "4"
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de SOPORTE:\nEmail: {{$json.email}}\nMensaje: {{$json.message}}"
      },
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "credentials": {
        "slackApi": "slack-credentials"
      },
      "id": "5"
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de VENTAS:\nEmail: {{$json.email}}\nMensaje: {{$json.message}}"
      },
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "credentials": {
        "slackApi": "slack-credentials"
      },
      "id": "6"
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje (OTRO):\nEmail: {{$json.email}}\nMensaje: {{$json.message}}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "credentials": {
        "slackApi": "slack-credentials"
      },
      "id": "7"
    }
  ],
  "connections": {
    "1": {
      "main": [
        [
          {
            "node": "2",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "2": {
      "main": [
        [
          {
            "node": "3",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "3": {
      "main": [
        [
          {
            "node": "4",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "4": {
      "main": [
        [
          {
            "node": "5",
            "type": "main",
            "index": 0
          }
        ],
        [],
        [
          {
            "node": "6",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "7",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {},
  "tags": [],
  "pinData": {}
}
```

**Explicación del workflow:**

1. **Webhook (nodo 1):**
   - Recibe peticiones POST en `/webhook-receptor`
   - Activa el workflow con cualquier payload JSON que contenga `email` y `message`

2. **Función (nodo 2):**
   - Extrae los campos del body:
   ```javascript
   return {
     email: $json.body.email,
     message: $json.body.message
   };
   ```

3. **OpenAI (nodo 3):**
   - Usa GPT-3.5-turbo para clasificación
   - Prompt: *"Clasifica este mensaje en una sola palabra: 'soporte', 'ventas' o 'otro'..."*
   - Temperatura 0 para respuestas deterministas
   - Devuelve la categoría en `$json.response`

4. **Switch Router (nodo 4):**
   - Rutea según la clasificación:
     - Si contiene "soporte" → nodo 5
     - Si contiene "ventas" → nodo 6
     - Cualquier otro caso → nodo 7

5. **Nodos Slack (5, 6, 7):**
   - Envían a diferentes canales con formato:
   ```
   Nuevo mensaje de [CATEGORÍA]:
   Email: [email]
   Mensaje: [mensaje]
   ```

**Para usar este workflow:**

1. Importa el JSON en n8n
2. Configura credenciales para:
   - OpenAI (API Key)
   - Slack (OAuth2)
3. Activa el workflow
4. Configura el webhook:
   - Usa la URL generada por n8n
   - Envía payloads JSON con formato:
   ```json
   {
     "email": "usuario@ejemplo.com",
     "message": "Texto a clasificar"
   }
   ```

**Notas:**
- Los nombres de los canales de Slack (#support, #sales, #general) deben existir
- El webhookId se genera automáticamente al activar el workflow
- Ajusta el modelo de OpenAI si es necesario (ej: gpt-4)
- Agrega manejo de errores según necesidades específicas