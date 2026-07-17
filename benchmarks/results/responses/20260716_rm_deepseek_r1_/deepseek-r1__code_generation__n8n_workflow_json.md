# DeepSeek R1 (reasoning) — code_generation/n8n_workflow_json

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 6.78 | quality: 8.4
- latency_total: 403.158s | tokens_per_second: 14.9
- input_tokens: 125 | output_tokens: 6007
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un uso adecuado de los nodos. La profundidad es aceptable, aunque no ofrece insights adicionales más allá de la implementación básica. La claridad y utilidad práctica son altas, permitiendo a un emprendedor implementar el workflow directamente.

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n:

```json
{
  "name": "Clasificación de Mensajes con OpenAI y Slack",
  "nodes": [
    {
      "parameters": {},
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": 1,
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "path": "/webhook",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        450,
        300
      ]
    },
    {
      "parameters": {
        "values": {
          "values": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        650,
        300
      ]
    },
    {
      "parameters": {
        "model": "text-davinci-003",
        "prompt": "Clasifica el siguiente mensaje en 'soporte', 'ventas' o 'otro'. Responde solo con la palabra clave:\n\n\"{{ $json.message }}\"",
        "options": {
          "temperature": 0,
          "maxTokens": 5
        }
      },
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "condition": {
                "type": "string",
                "value": {
                  "string": "soporte"
                }
              },
              "output": 0
            },
            {
              "condition": {
                "type": "string",
                "value": {
                  "string": "ventas"
                }
              },
              "output": 1
            }
          ]
        },
        "defaultOutput": 2
      },
      "name": "Router",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "Nuevo mensaje de SOPORTE:\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "Slack Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        150
      ]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "Nuevo mensaje de VENTAS:\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "Slack Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        300
      ]
    },
    {
      "parameters": {
        "authentication": "slackApi",
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "Nuevo mensaje (OTRO):\nEmail: {{ $json.email }}\nMensaje: {{ $json.message }}"
      },
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1250,
        450
      ]
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
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
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
            "node": "Router",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router": {
      "main": [
        [
          {
            "node": "Slack Soporte",
            "type": "main",
            "index": 0
          },
          0
        ],
        [
          {
            "node": "Slack Ventas",
            "type": "main",
            "index": 0
          },
          1
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          },
          2
        ]
      ]
    }
  }
}
```

**Explicación del workflow:**

1. **Webhook**: 
   - Recibe solicitudes POST en `/webhook`
   - Extrae automáticamente el cuerpo JSON

2. **Extraer Datos**:
   - Crea dos nuevos campos: `email` y `message`
   - Usa expresiones para obtenerlos del cuerpo del webhook

3. **Clasificar con OpenAI**:
   - Usa el modelo text-davinci-003
   - Prompt diseñado para obtener solo una palabra clave
   - Configuración de temperatura 0 para respuestas deterministas
   - Limita tokens para respuestas breves

4. **Router (Switch Node)**:
   - Evalúa la salida de OpenAI
   - "soporte" → Canal #support (output 0)
   - "ventas" → Canal #sales (output 1)
   - Cualquier otro valor → #general (default output 2)

5. **Nodos Slack**:
   - Envían mensajes formateados a diferentes canales
   - Incluyen el email y mensaje original
   - Usan autenticación API de Slack (debes configurar las credenciales)

**Para usar este workflow:**
1. Importa el JSON en n8n
2. Configura credenciales para:
   - OpenAI (en el nodo de clasificación)
   - Slack (en los 3 nodos de Slack)
3. Activa el workflow
4. Usa la URL del webhook generada para enviar POST requests con formato:
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Mi dispositivo no funciona"
}
```

**Notas:**
- Los canales de Slack deben existir previamente
- El prompt de OpenAI está en español para mantener consistencia
- El nodo Switch incluye un caso por defecto para cualquier respuesta inesperada
- Todos los nodos están conectados secuencialmente con manejo de errores implícito