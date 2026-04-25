# Gemini 2.5 Flash — code_generation/n8n_workflow_json

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 6.94 | quality: 8.12
- latency_total: 10.231s | tokens_per_second: 196.8
- input_tokens: 116 | output_tokens: 2013
- judge_score: 3.8 | justificación: 

## Respuesta completa

```json
{
  "name": "Clasificador de Mensajes con IA a Slack",
  "nodes": [
    {
      "id": "webhookTrigger",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        240,
        300
      ],
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message"
      },
      "credentials": {}
    },
    {
      "id": "extractData",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [
        480,
        300
      ],
      "parameters": {
        "values": [
          {
            "name": "email",
            "value": "={{$json.body.email}}"
          },
          {
            "name": "message",
            "value": "={{$json.body.message}}"
          }
        ]
      }
    },
    {
      "id": "classifyMessage",
      "name": "Clasificar Mensaje (OpenAI)",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [
        720,
        300
      ],
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "user",
            "content": "Clasifica el siguiente mensaje en una de las siguientes categorías: \"soporte\", \"ventas\", \"otro\". Responde únicamente con la categoría. \n\nMensaje: \"{{$json.message}}\""
          }
        ],
        "temperature": 0
      },
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "resolve": true
        }
      }
    },
    {
      "id": "routeByClassification",
      "name": "Ruta por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [
        960,
        300
      ],
      "parameters": {
        "mode": "string",
        "value": "={{$json.choices[0].message.content.trim().toLowerCase()}}",
        "conditions": [
          {
            "value": "soporte",
            "type": "string",
            "operator": "equalTo"
          },
          {
            "value": "ventas",
            "type": "string",
            "operator": "equalTo"
          },
          {
            "value": "otro",
            "type": "string",
            "operator": "equalTo"
          }
        ]
      }
    },
    {
      "id": "sendToSupportSlack",
      "name": "Enviar a Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1200,
        180
      ],
      "parameters": {
        "channel": "#support",
        "text": "Nuevo mensaje de soporte de: {{$json.email}}\n\n*Mensaje:*\n{{$json.message}}"
      },
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "resolve": true
        }
      }
    },
    {
      "id": "sendToSalesSlack",
      "name": "Enviar a Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1200,
        300
      ],
      "parameters": {
        "channel": "#sales",
        "text": "Nuevo mensaje de ventas de: {{$json.email}}\n\n*Mensaje:*\n{{$json.message}}"
      },
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "resolve": true
        }
      }
    },
    {
      "id": "sendToGeneralSlack",
      "name": "Enviar a Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        1200,
        420
      ],
      "parameters": {
        "channel": "#general",
        "text": "Nuevo mensaje general de: {{$json.email}}\n\n*Mensaje:*\n{{$json.message}}"
      },
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "resolve": true
        }
      }
    }
  ],
  "connections": {
    "webhookTrigger": {
      "main": [
        [
          {
            "node": "extractData",
            "input": 0
          }
        ]
      ]
    },
    "extractData": {
      "main": [
        [
          {
            "node": "classifyMessage",
            "input": 0
          }
        ]
      ]
    },
    "classifyMessage": {
      "main": [
        [
          {
            "node": "routeByClassification",
            "input": 0
          }
        ]
      ]
    },
    "routeByClassification": {
      "main": [
        [
          {
            "node": "sendToSupportSlack",
            "input": 0
          }
        ],
        [
          {
            "node": "sendToSalesSlack",
            "input": 0
          }
        ],
        [
          {
            "node": "sendToGeneralSlack",
            "input": 0
          }
        ]
      ]
    }
  }
}
```

---

**Cómo usar este workflow en N8N:**

1.  **Copia el JSON:** Copia todo el contenido del JSON de arriba.
2.  **Importa en n8n:**
    *   Abre tu instancia de n8n.
    *   Haz clic en "Workflows" en la barra lateral izquierda.
    *   Haz clic en "New Workflow" o en el botón de "Add Workflow".
    *   Haz clic en el icono de "Import from JSON" (generalmente es un icono de flecha hacia arriba o de documento con flecha).
    *   Pega el JSON copiado en el campo de texto y haz clic en "Import".
3.  **Configura las Credenciales:**
    *   **OpenAI:**
        *   Haz clic en el nodo "Clasificar Mensaje (OpenAI)".
        *   En la sección "Credentials", verás un campo "OpenAI API". Haz clic en "Create New" si no tienes una configurada, o selecciona una existente.
        *   Si creas una nueva, necesitarás tu `API Key` de OpenAI.
    *   **Slack:**
        *   Haz clic en cada uno de los nodos "Enviar a Slack #support", "Enviar a Slack #sales", "Enviar a Slack #general".
        *   En la sección "Credentials", verás un campo "Slack API". Haz clic en "Create New" o selecciona una existente.
        *   Si creas una nueva, necesitarás un "OAuth Access Token" para tu espacio de trabajo de Slack. Asegúrate de que la aplicación de Slack asociada al token tenga los permisos para enviar mensajes a los canales especificados (`#support`, `#sales`, `#general`).
4.  **Activa el Workflow:** Después de configurar las credenciales, activa el workflow haciendo clic en el botón "Active" en la parte superior derecha de la pantalla del workflow.
5.  **Obtén la URL del Webhook:**
    *   Haz clic en el nodo "Webhook".
    *   Verás un campo "Webhook URL". Copia esta URL. Esta es la URL a la que debes enviar tus solicitudes POST.

**Cómo probar el workflow:**

Puedes usar `curl`, Postman, Insomnia o cualquier otra herramienta para enviar una solicitud POST a la URL del webhook.

**Ejemplo de solicitud POST (usando `curl`):**

```bash
curl -X POST \
  YOUR_WEBHOOK_URL \
  -H 'Content-Type: application/json' \
  -d '{
    "email": "juan.perez@ejemplo.com",
    