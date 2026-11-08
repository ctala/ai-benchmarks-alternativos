# Seed 2.0 Code — code_generation/n8n_workflow_json

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 65.084s | tokens_per_second: 73.9
- input_tokens: 153 | output_tokens: 4810
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un workflow JSON completo que cumple con los requisitos especificados, incluyendo optimizaciones útiles para un emprendedor.

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

### Workflow N8N JSON (Compatible con N8N ≥1.20.0)
Este workflow cumple **todos tus requisitos** y incluye optimizaciones (ej: respuesta determinista de OpenAI, formato Markdown en Slack, manejo de espacios en la clasificación):

```json
{
  "id": "clasificador-mensajes-slack-openai",
  "name": "Clasificador de Mensajes → Slack",
  "active": true,
  "settings": {},
  "version": 1,
  "n8nVersion": "1.40.0",
  "nodes": [
    {
      "id": "webhook-trigger",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 0],
      "parameters": {
        "httpMethod": "POST",
        "path": "/clasificar-mensaje",
        "responseMode": "onReceived",
        "responseData": "ok"
      }
    },
    {
      "id": "extraer-campos",
      "name": "Extraer Email/Mensaje",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [280, 0],
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json.body.email }}"
            },
            {
              "name": "message",
              "value": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "setAll": false,
          "includeOtherFields": false
        }
      }
    },
    {
      "id": "clasificar-openai",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 4,
      "position": [560, 0],
      "credentials": {
        "openAiApi": {
          "id": "placeholder-openai-cred",
          "name": "OpenAI API"
        }
      },
      "parameters": {
        "operation": "chat",
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Clasifica el siguiente mensaje del usuario en EXACTAMENTE UNA de estas categorías: 'soporte', 'ventas', 'otro'. NO AGREGUES TEXTO ADICIONAL, SOLO LA CATEGORÍA."
          },
          {
            "role": "user",
            "content": "={{ $json.message }}"
          }
        ],
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      }
    },
    {
      "id": "enrutar-categoria",
      "name": "Enrutar por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [840, 0],
      "parameters": {
        "rules": [
          {
            "value1": "={{ $trim($json.choices[0].message.content) }}",
            "operation": "equal",
            "value2": "soporte"
          },
          {
            "value1": "={{ $trim($json.choices[0].message.content) }}",
            "operation": "equal",
            "value2": "ventas"
          }
        ],
        "fallbackRule": true
      }
    },
    {
      "id": "slack-support",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 3,
      "position": [1120, -180],
      "credentials": {
        "slackApi": {
          "id": "placeholder-slack-cred",
          "name": "Slack API"
        }
      },
      "parameters": {
        "operation": "postMessage",
        "channel": "#support",
        "text": "*NUEVO MENSAJE DE SOPORTE*\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n📂 Categoría: {{ $trim($json.choices[0].message.content) }}",
        "options": {
          "markdown": true
        }
      }
    },
    {
      "id": "slack-sales",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 3,
      "position": [1120, 0],
      "credentials": {
        "slackApi": {
          "id": "placeholder-slack-cred",
          "name": "Slack API"
        }
      },
      "parameters": {
        "operation": "postMessage",
        "channel": "#sales",
        "text": "*NUEVO MENSAJE DE VENTAS*\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n📂 Categoría: {{ $trim($json.choices[0].message.content) }}",
        "options": {
          "markdown": true
        }
      }
    },
    {
      "id": "slack-general",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 3,
      "position": [1120, 180],
      "credentials": {
        "slackApi": {
          "id": "placeholder-slack-cred",
          "name": "Slack API"
        }
      },
      "parameters": {
        "operation": "postMessage",
        "channel": "#general",
        "text": "*NUEVO MENSAJE (OTRO)*\n👤 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}\n📂 Categoría: {{ $trim($json.choices[0].message.content) }}",
        "options": {
          "markdown": true
        }
      }
    }
  ],
  "connections": {
    "webhook-trigger": {
      "main": [
        [
          {
            "node": "extraer-campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "extraer-campos": {
      "main": [
        [
          {
            "node": "clasificar-openai",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "clasificar-openai": {
      "main": [
        [
          {
            "node": "enrutar-categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "enrutar-categoria": {
      "main": [
        [
          {
            "node": "slack-support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "slack-sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "slack-general",
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

### Pasos para Configurar y Usar
#### 1. Importar el Workflow en N8N
- Abre tu instancia de N8N
- Ve a **Workflows → Import Workflow**
- Pega el JSON anterior y haz clic en **Import**

#### 2. Configurar Credenciales (Requerido)
El workflow usa **placeholders** para credenciales, debes reemplazarlos:
##### Credencial OpenAI
- Haz clic en el nodo **"Clasificar con OpenAI"**
- En el campo *Credentials*, selecciona **"Create New"** o usa una credencial existente de OpenAI (necesitas una API Key de OpenAI)
- **Recomendación**: Usa `gpt-3.5-turbo` (barato y suficiente para clasificación)

##### Credencial Slack
- Haz clic en **cualquier nodo de Slack** (ej: *"Enviar a #support"*)
- Crea una credencial de Slack:
  1. Ve a [Slack API Apps](https://api.slack.com/apps)
  2. Crea una app **From Scratch**
  3. Habilita **Bot Token Scopes** con el permiso `chat:write`
  4. Instala la app en tu workspace Slack
  5. Copia el **Bot User OAuth Token** y pegalo en la credencial de N8N
  6. **Importante**: Agrega el bot de Slack a los canales `#support`, `#sales` y `#general` (para que pueda enviar mensajes)

#### 3. Probar el Workflow
- Activa el workflow (botón **Active** en la esquina superior derecha)
- Copia la URL del webhook (nodo *"Webhook POST"* → campo *Webhook URL*)
- Envía una petición **POST** con un body JSON como este (puedes usar Postman, cURL o Insomnia):
  ```json
  {
    "email": "usuario@ejemplo.com",
    "message": "Hola, necesito ayuda con mi factura de suscripción"
  }
  ```
- El mensaje se clasificará como **soporte** y se enviará a `#support`

---

### Características Clave del Workflow
1. **Trigger Webhook POST**: Responde inmediatamente al cliente (no bloquea la petición)
2. **Extracción Segura**: Usa un nodo `Set` para normalizar los campos `email` y `message`
3. **Clasificación Determinista**: OpenAI usa `temperature: 0` para evitar respuestas aleatorias, y un prompt estricto para que solo devuelva la categoría
4. **Enrutamiento Inteligente**: Usa un nodo `Switch` para enviar a cada canal de Slack según la clasificación
5. **Formato en Slack**: Usa Markdown para mensajes legibles (negrita, emojis)
6. **Manejo de Errores**: El nodo `Switch` limpia espacios en la clasificación (por si OpenAI agrega espacios accidentales)

Si necesitas modificar algo (ej: cambiar el modelo de OpenAI, agregar más categorías), avísame!