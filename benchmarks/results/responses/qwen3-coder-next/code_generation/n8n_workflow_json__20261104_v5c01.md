# Qwen3-Coder-Next (OpenRouter FP8) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.83 | quality: 8.6
- latency_total: 17.655s | tokens_per_second: 96.2
- input_tokens: 123 | output_tokens: 1698
- judge_score: 4.0 | justificación: La respuesta es relevante y clara, proporcionando un workflow JSON que cumple con los requisitos, aunque carece de conexiones de nodos y podría mejorar en profundidad al explicar más sobre la configuración del webhook y la integración de Slack.

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

Aquí tienes un workflow completo en formato JSON para **n8n**, que cumple con todos los requisitos que solicitaste:

```json
{
  "name": "Email Classifier to Slack",
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "path": "classify-email",
        "httpMethod": "POST",
        "responseMode": "lastNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 200]
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            { "name": "email", "value": "={{ $json.body.email }}" },
            { "name": "message", "value": "={{ $json.body.message }}" }
          ]
        }
      },
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [450, 200]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "systemMessage": "Clasifica el siguiente mensaje como 'soporte', 'ventas' o 'otro'. Devuelve solo la palabra clave (sin comillas ni puntuación).",
        "prompt": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAI",
      "typeVersion": 1,
      "position": [650, 200]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            { "value1": "={{ $json.output }}", "value2": "soporte" }
          ],
          "number": [],
          "boolean": []
        }
      },
      "name": "If - Soporte",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 100]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            { "value1": "={{ $json.output }}", "value2": "ventas" }
          ],
          "number": [],
          "boolean": []
        }
      },
      "name": "If - Ventas",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 250]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 400]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "Slack - Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 100]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "Slack - Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1050, 250]
    }
  ],
  "connections": {
    "Start": {
      "main": [
        [
          {
            "node": "Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
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
            "node": "If - Soporte",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If - Soporte": {
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
            "node": "If - Ventas",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "If - Ventas": {
      "main": [
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
  }
}
```

---

### 📝 Notas importantes:

1. **Nodos de IA (OpenAI)**:  
   - Usa `@n8n/n8n-nodes-langchain.lmChatOpenAI`, disponible si tienes instalado el paquete `@n8n/n8n-nodes-langchain`.  
   - Si usas una versión más reciente de n8n (v1.30+), se recomienda usar el nodo **"AI Chain" > "AI Agent"** o el nuevo **"AI Node"** (`n8n-nodes-langchain.aiAgent`) para mejor soporte y flexibilidad.

2. **Alternativa con nodo "AI Agent" (recomendado para v1.30+)**:
   Si prefieres usar el nodo más moderno (nodo `AI Agent`), reemplaza el nodo `OpenAI` y `If` por un solo nodo **AI Agent** con un prompt estructurado y output JSON, y luego usar un nodo **Set** + **Switch** para ruteo. ¿Quieres esa versión alternativa?

3. **Configuración requerida**:
   - En el nodo **Slack**, debes configurar la **conexión OAuth** con tu workspace y permisos para enviar mensajes a `#support`, `#sales` y `#general`.
   - En el nodo **OpenAI**, debes tener configurada tu API key de OpenAI en las credenciales de n8n.

4. **Webhook URL**:  
   Al activar el workflow, n8n generará una URL tipo:  
   `https://your-n8n-instance.com/webhook/classify-email`

   Puedes probarlo con:
   ```bash
   curl -X POST https://your-n8n-instance.com/webhook/classify-email \
     -H "Content-Type: application/json" \
     -d '{"email":"cliente@ejemplo.com", "message":"Quiero comprar un plan premium"}'
   ```

¿Quieres que te genere también una versión optimizada con el nodo **AI Agent** (más robusto y actualizado)?