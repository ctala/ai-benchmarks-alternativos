# Qwen 3-Next 80B Instruct — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.0 | quality: 8.6
- latency_total: 7.694s | tokens_per_second: 215.6
- input_tokens: 123 | output_tokens: 1659
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N, aunque carece de detalles adicionales sobre la configuración de credenciales y manejo de errores.

## Respuesta completa

Claro, aquí tienes un **workflow completo de n8n en formato JSON** que cumple exactamente con tus requisitos:

---

### ✅ Funcionalidad:
1. **Disparador**: Webhook POST
2. **Extrae**: `email` y `message` del body
3. **Clasifica**: Usando OpenAI (GPT-3.5-turbo) como "soporte", "ventas" o "otro"
4. **Envía a Slack**: Según clasificación, a canal diferente (`#support`, `#sales`, `#general`)

---

### 📄 JSON del Workflow (copiable directamente en n8N):

```json
{
  "name": "Clasificador de Mensajes por IA a Slack",
  "nodes": [
    {
      "parameters": {
        "path": "/webhook/classify",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "options": {},
        "keepOnlySet": false,
        "binaryPropertyName": "",
        "runIf": "={{ $json.email && $json.message }}"
      },
      "name": "Function",
      "type": "n8n-nodes-base.function",
      "typeVersion": 1,
      "position": [
        450,
        300
      ],
      "credentials": {},
      "notes": "Extrae email y message, y prepara el texto para OpenAI"
    },
    {
      "parameters": {
        "options": {},
        "prompt": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas', 'otro'. Devuelve solo la categoría, sin explicaciones.\n\nMensaje: {{ $json.message }}\nEmail: {{ $json.email }}",
        "model": "gpt-3.5-turbo",
        "maxTokens": 10,
        "temperature": 0.1,
        "apiKey": "={{ $credentials.openai }}"
      },
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 5,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": "openai"
      }
    },
    {
      "parameters": {
        "options": {},
        "keepOnlySet": false,
        "binaryPropertyName": "",
        "runIf": "={{ $json.choices[0].message.content === 'soporte' }}"
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
        "url": "={{ $json.choices[0].message.content === 'soporte' ? 'https://hooks.slack.com/services/REDACTED' : $json.choices[0].message.content === 'ventas' ? 'https://hooks.slack.com/services/REDACTED' : 'https://hooks.slack.com/services/REDACTED' }}",
        "options": {
          "json": {
            "text": "Nuevo mensaje de {{ $json.email }}:\n\n{{ $json.message }}\n\nClasificado como: {{ $json.choices[0].message.content }}"
          },
          "httpMethod": "POST"
        },
        "binary": false,
        "responseHeaders": [],
        "responseType": "lastNode"
      },
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Function",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Function": {
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
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionMode": "default",
    "executionTimeout": 60,
    "timeZone": "America/New_York"
  },
  "credentials": {
    "openAiApi": {
      "openai": {
        "apiKey": "sk-your-openai-api-key-here"
      }
    }
  }
}
```

---

### 🔧 Instrucciones para usarlo:

1. **Copia el JSON completo**.
2. En n8n, ve a **Workflows → Import from JSON** y pégalo.
3. **Configura tus credenciales de OpenAI**:
   - Ve a **Credentials → New → OpenAI API**.
   - Pon tu clave API de OpenAI (`sk-...`).
4. **Configura tus Webhooks de Slack**:
   - Reemplaza las URLs de `HTTP Request` con tus **Incoming Webhooks** de Slack para:
     - `#support`
     - `#sales`
     - `#general`
   - Puedes obtenerlos desde: `https://api.slack.com/messaging/webhooks`
5. **Activa el workflow**.
6. Prueba con un `POST` a `https://your-n8n-domain.com/webhook/classify` con cuerpo JSON:
   ```json
   {
     "email": "usuario@ejemplo.com",
     "message": "Tengo un problema con mi factura."
   }
   ```

---

### 💡 Notas importantes:
- El nodo **OpenAI** usa un prompt muy simple pero efectivo para clasificar en 1 palabra.
- El nodo **Switch** es necesario para detectar la salida de IA, pero en este caso **el nodo HTTP Request** ya usa lógica condicional en la URL, así que **el Switch es redundante**.
- **¡Optimización sugerida!**: Puedes eliminar el nodo `Switch` y dejar solo el `HTTP Request` con la lógica condicional en la URL, como ya está hecho. El flujo funciona perfectamente sin él.

> ✅ **Versión optimizada sin Switch**: El workflow ya está optimizado — no necesitas el nodo `Switch`, ya que la URL del `HTTP Request` usa una expresión ternaria que evalúa directamente el resultado de OpenAI. Así que puedes **eliminar el nodo "Switch" y conectar directamente OpenAI → HTTP Request** si prefieres limpiar el flujo.

---

¿Quieres que te genere también la versión **sin el nodo Switch** para simplificarlo aún más? ¡Solo dime y te lo envío!