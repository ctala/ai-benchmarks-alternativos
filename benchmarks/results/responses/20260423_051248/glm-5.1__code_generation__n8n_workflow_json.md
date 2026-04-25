# GLM-5.1 — code_generation/n8n_workflow_json

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.31 | quality: 8.32
- latency_total: 383.21s | tokens_per_second: 10.1
- input_tokens: 119 | output_tokens: 3856
- judge_score: 3.8 | justificación: 

## Respuesta completa

Aquí tienes el workflow completo de n8n en formato JSON. 

Este flujo utiliza un Webhook para recibir los datos, un nodo de OpenAI con un *prompt* estricto para asegurar que solo devuelva la categoría exacta, un nodo Switch para enrutar el resultado, y nodos de Slack para enviar el mensaje al canal correspondiente.

```json
{
  "name": "Clasificación de Emails con IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [220, 300],
      "webhookId": "generated-id-webhook"
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "options": {
          "temperature": 0
        },
        "messages": {
          "messageValues": [
            {
              "content": "Eres un asistente de clasificación. Tu ÚNICA función es leer el mensaje del usuario y clasificarlo en una de estas tres categorías exactas: 'soporte', 'ventas' o 'otro'. \n\nReglas:\n- Si el mensaje habla de problemas técnicos, errores, o ayuda con el producto, responde: soporte\n- Si el mensaje habla de precios, contratación, demo, o compra, responde: ventas\n- Si no encaja en nada de lo anterior, responde: otro\n\nIMPORTANTE: Tu respuesta debe ser SOLO la palabra de la categoría, sin puntos, sin comas, sin explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        }
      },
      "id": "openai-node",
      "name": "OpenAI (Clasificador)",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.2,
      "position": [460, 300],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENTIAL_ID_OPENAI",
          "name": "OpenAI Api"
        }
      }
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.toLowerCase().trim() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte",
              "output": 0
            },
            {
              "value2": "ventas",
              "output": 1
            },
            {
              "value2": "otro",
              "output": 2
            }
          ]
        },
        "fallbackOutput": 2,
        "options": {}
      },
      "id": "switch-node",
      "name": "Switch (Enrutador)",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [700, 300]
    },
    {
      "parameters": {
        "operation": "sendMessage",
        "channel": "#support",
        "text": "📬 *Nuevo mensaje de Soporte*\n\n📧 *Email:* {{ $('Webhook').item.json.body.email }}\n💬 *Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack (#support)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [940, 140],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack Api"
        }
      }
    },
    {
      "parameters": {
        "operation": "sendMessage",
        "channel": "#sales",
        "text": "💰 *Nuevo mensaje de Ventas*\n\n📧 *Email:* {{ $('Webhook').item.json.body.email }}\n💬 *Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack (#sales)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [940, 340],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack Api"
        }
      }
    },
    {
      "parameters": {
        "operation": "sendMessage",
        "channel": "#general",
        "text": "📌 *Nuevo mensaje General*\n\n📧 *Email:* {{ $('Webhook').item.json.body.email }}\n💬 *Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack (#general)",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [940, 540],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENTIAL_ID_SLACK",
          "name": "Slack Api"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI (Clasificador)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI (Clasificador)": {
      "main": [
        [
          {
            "node": "Switch (Enrutador)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch (Enrutador)": {
      "main": [
        [
          {
            "node": "Slack (#support)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#sales)",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack (#general)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {}
}
```

### 🛠️ Instrucciones para ponerlo en marcha:

1. **Importar el workflow:** Ve a tu instancia de n8n, haz clic en el menú (tres puntos arriba a la derecha) y selecciona "Import from File" o pega el JSON directamente en "Import from Clipboard".
2. **Credenciales:** 
   * Abre los nodos de **OpenAI** y **Slack** y configura tus credenciales (API Keys). En el JSON dejé el marcador `TU_CREDENTIAL_ID_OPENAI` y `TU_CREDENTIAL_ID_SLACK` que se reemplazarán automáticamente al seleccionar tu cuenta en la interfaz.
3. **Canales de Slack:** Asegúrate de que el bot de Slack tenga permisos para escribir en `#support`, `#sales` y `#general`, y que los nombres en minúsculas coincidan exactamente con los de tu espacio de trabajo.
4. **Activar el Workflow:** Enciende el switch "Active" en la esquina superior derecha para que el Webhook empiece a escuchar.

### 🧪 Cómo probarlo:

Puedes enviar un POST a la URL del webhook (la encontrarás en el nodo Webhook) usando `curl` o Postman:

```bash
curl -X POST https://TU-INSTANCIA-N8N.com/webhook/clasificar-email \
-H "Content-Type: application/json" \
-d '{
  "email": "cliente@empresa.com",
  "message": "Hola, me interesa conocer los precios de su plan empresarial para mi equipo."
}'
```

**¿Qué hace el flujo por dentro?**
1. El Webhook recibe el JSON y lo pasa a OpenAI.
2. OpenAI recibe el *message* ("Hola, me interesa conocer los precios..."), aplica el prompt de sistema que le obliga a responder **solo** con la categoría, y devuelve `ventas`.
3. El nodo Switch toma la respuesta de OpenAI, la pasa a minúsculas y elimina espacios (`toLowerCase().trim()`), y la compara.
4. Al ser "ventas", dirige el flujo por la segunda salida del Switch hacia el nodo `Slack (#sales)`.
5. El nodo de Slack extrae el email y el mensaje originales directamente del nodo Webhook (`$('Webhook').item.json.body`) y publica el formato enriquecido en el canal correspondiente.