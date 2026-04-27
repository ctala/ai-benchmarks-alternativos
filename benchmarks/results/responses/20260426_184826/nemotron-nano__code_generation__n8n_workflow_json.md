# Nemotron 3 Nano 30B — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.31 | quality: 8.6
- latency_total: 66.954s | tokens_per_second: 95.3
- input_tokens: 133 | output_tokens: 6383
- judge_score: 4.0 | justificación: 

## Respuesta completa

Aquí tienes el **workflow completo de n8n** en formato JSON que cumple con los requisitos que describiste.  
Puedes importarlo directamente en tu instancia de n8n ( *Importar → Pegar JSON* ).

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "",
        "responseMode": "onReceived"
      },
      "name": "Webhook Trigger",
      "type": "n8n-n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "email_classifier_webhook"
    },
    {
      "parameters": {
        "values": {
          "email": "={{ $json[\"email\"] }}",
          "message": "={{ $json[\"message\"] }}"
        }
      },
      "name": "Extract Email & Message",
      "type": "n8n-n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [400, 300],
      "inputs": 1
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": "Classify the following message into one of the following categories: soporte, ventas, otro. Return only the category name (no extra text).\n\nMessage: {{ $json[\"message\"] }}\n",
        "temperature": 0,
        "max_tokens": 10,
        "stop": []
      },
      "name": "Classify Message",
      "type": "n8n-n8n-nodes-base.openai",
      "typeVersion": 1,
      "position": [550, 300],
      "inputs": 1,
      "credentials": {
        "openaiApi": "OpenAI Credentials"
      }
    },
    {
      "parameters": {
        "mode": "standard",
        "options": [
          {
            "name": "Soporte",
            "value": "soporte"
          },
          {
            "name": "Ventas",
            "value": "ventas"
          },
          {
            "name": "Otro",
            "value": "otro"
          }
        ]
      },
      "name": "Switch: Category",
      "type": "n8n-n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [700, 300],
      "input": [
        {
          "node": "Classify Message",
          "type": "n8n-n8n-nodes-base.openai",
          "index": 0
        }
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "📨 New support ticket from email: {{ $json[\"email\"] }}\nMessage: {{ $json[\"message\"] }}"
      },
      "name": "Post to Slack #support",
      "type": "n8n-n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 150],
      "credentials": {
        "slackApi": "Slack API Credentials"
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "🚀 New sales prospect from email: {{ $json[\"email\"] }}\nMessage: {{ $json[\"message\"] }}"
      },
      "name": "Post to Slack #sales",
      "type": "n8n-n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 350],
      "credentials": {
        "slackApi": "Slack API Credentials"
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "ℹ️ New other message from email: {{ $json[\"email\"] }}\nMessage: {{ $json[\"message\"] }}"
      },
      "name": "Post to Slack #general",
      "type": "n8n-n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [850, 550],
      "credentials": {
        "slackApi": "Slack API Credentials"
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Extract Email & Message",
            "type": "n8n-n8n-nodes-base.set",
            "index": 0
          }
        ]
      ]
    },
    "Extract Email & Message": {
      "main": [
        [
          {
            "node": "Classify Message",
            "type": "n8n-n8n-nodes-base.openai",
            "index": 0
          }
        ]
      ]
    },
    "Classify Message": {
      "main": [
        [
          {
            "node": "Switch: Category",
            "type": "n8n-n8n-nodes-base.switch",
            "index": 0
          }
        ]
      ]
    },
    "Switch: Category": {
      "main": [
        [
          {
            "node": "Post to Slack #support",
            "type": "n8n-n8n-nodes-base.slack",
            "index": 0
          }
        ],
        [
          {
            "node": "Post to Slack #sales",
            "type": "n8n-n8n-nodes-base.slack",
            "index": 1
          }
        ],
        [
          {
            "node": "Post to Slack #general",
            "type": "n8n-n8n-nodes-base.slack",
            "index": 2
          }
        ]
      ]
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
| **Webhook Trigger** | Espera una petición `POST` en la URL que generes (p.ej. `https://tu-dominio.com/webhook`). |
| **Extract Email & Message** | Extrae los campos `email` y `message` del cuerpo JSON recibido. |
| **Classify Message** | Usa la API de OpenAI (`gpt‑3.5‑turbo`) con un prompt que devuelve **únicamente** la categoría (`soporte`, `ventas` o `otro`). |
| **Switch: Category** | Distribuye el mensaje al siguiente nodo según el valor devuelto por la IA. |
| **Post to Slack #\*** | Envía el correo y el mensaje a la zona correspondiente de Slack (`#support`, `#sales` o `#general`). |

### Cómo usarlo

1. **Importa** el JSON en n8n.  
2. **Crea** los credenciales necesarios:  
   - `OpenAI Credentials` (tu clave API de OpenAI).  
   - `Slack API Credentials` (token de bot o token de usuario con permisos para publicar en los canales).  
3. **Activa** el workflow y copia la URL del webhook que n8n genera.  
4. **Envía** una petición `POST` a esa URL con un cuerpo JSON, por ejemplo:

```json
{
  "email": "cliente@example.com",
  "message": "Quiero cambiar mi plan de precios."
}
```

5. Dependiendo del contenido del `message`, el mensaje se publicará en `#support`, `#sales` o `#general`.

¡Listo! Con este workflow tendrás una clasificación automática y una ruta de notificación directa a los canales de Slack correspondientes. 🚀