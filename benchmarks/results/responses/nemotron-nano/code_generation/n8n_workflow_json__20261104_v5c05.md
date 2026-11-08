# Nemotron 3 Nano 30B — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.91 | quality: 8.4
- latency_total: 43.935s | tokens_per_second: 108.2
- input_tokens: 133 | output_tokens: 4752
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo todos los requisitos del flujo de trabajo, aunque la profundidad podría mejorarse con más detalles sobre la configuración de los nodos o manejo de errores.

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


**Workflow JSON para N8N**

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify",
        "responseMode": "onReceived"
      },
      "name": "Webhook",
      "type": "n8n-n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "id": "webhook"
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "email",
              "value": "={{ $json[\"email\"] }}"
            },
            {
              "name": "message",
              "value": "={{ $json[\"message\"] }}"
            }
          ]
        },
        "options": {}
      },
      "name": "Extract",
      "type": "n8n-n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [500, 300],
      "id": "extract"
    },
    {
      "parameters": {
        "operation": "openai",
        "model": "gpt-3.5-turbo",
        "prompt": "Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas, otro. Devuelve solo el nombre de la categoría sin ningún otro texto.",
        "responseFormat": "string"
      },
      "name": "Classify",
      "type": "n8n-n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [750, 300],
      "id": "classify"
    },
    {
      "parameters": {
        "conditions": [
          {
            "value1": "={{ $json[\"category\"] }}",
            "operation": "equal",
            "value2": "soporte",
            "sendTo": [
              "slackSupport"
            ]
          },
          {
            "value1": "={{ $json[\"category\"] }}",
            "operation": "equal",
            "value2": "ventas",
            "sendTo": [
              "slackSales"
            ]
          },
          {
            "value1": "={{ $json[\"category\"] }}",
            "operation": "equal",
            "value2": "otro",
            "sendTo": [
              "slackGeneral"
            ]
          }
        ]
      },
      "name": "Switch",
      "type": "n8n-n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [1000, 300],
      "id": "switch"
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Ticket de soporte recibido de {{ $json[\"email\"] }}: {{ $json[\"message\"] }}"
      },
      "name": "Slack Support",
      "type": "n8n-n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1300, 150],
      "id": "slackSupport",
      "credentials": {
        "slackApi": "slackApi1"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Oportunidad de venta de {{ $json[\"email\"] }}: {{ $json[\"message\"] }}"
      },
      "name": "Slack Sales",
      "type": "n8n-n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1300, 350],
      "id": "slackSales",
      "credentials": {
        "slackApi": "slackApi1"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Mensaje genérico recibido de {{ $json[\"email\"] }}: {{ $json[\"message\"] }}"
      },
      "name": "Slack General",
      "type": "n8n-n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1300, 550],
      "id": "slackGeneral",
      "credentials": {
        "slackApi": "slackApi1"
      }
    }
  ],
  "connections": {
    "webhook": {
      "main": [
        [
          {
            "node": "extract",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "extract": {
      "main": [
        [
          {
            "node": "classify",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "classify": {
      "main": [
        [
          {
            "node": "switch",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "switch": {
      "main": [
        [
          {
            "node": "slackSupport",
            "type": "main",
            "index": 0
          },
          {
            "node": "slackSales",
            "type": "main",
            "index": 0
          },
          {
            "node": "slackGeneral",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "slackSupport": {
      "main": []
    },
    "slackSales": {
      "main": []
    },
    "slackGeneral": {
      "main": []
    }
  },
  "active": false,
  "settings": {},
  "id": "1"
}
```

### Qué hace cada nodo

| Nodo | Función |
|------|---------|
| **Webhook** | Espera una petición `POST` en la ruta `/classify`. |
| **Extract** | Toma los campos `email` y `message` del cuerpo JSON recibido. |
| **Classify** | Envía `message` a la API de OpenAI (modelo `gpt‑3.5‑turbo`) y recibe como salida la categoría (`soporte`, `ventas` o `otro`). |
| **Switch** | Evalúa el valor de `category` y dirige el flujo al nodo Slack correspondiente. |
| **Slack Support / Slack Sales / Slack General** | Publica un mensaje en el canal de Slack indicado (`#support`, `#sales` o `#general`). |

> **Nota:**  
> - Reemplaza `slackApi1` por el nombre del nodo de credenciales de Slack que hayas configurado en tu instancia de n8n.  
> - Asegúrate de que la cuenta de OpenAI tenga acceso a la API y que la clave esté almacenada en las credenciales de n8n bajo el nombre `openaiApi`.  
> - Puedes activar el workflow (`active: true`) una vez que lo importes y pruebes la webhook con una petición `POST` que incluya `{"email":"...","message":"..."}`.  

¡Listo! Con este JSON puedes importar el workflow directamente a tu instalación de n8n y tendrás la automatización solicitada. 🚀