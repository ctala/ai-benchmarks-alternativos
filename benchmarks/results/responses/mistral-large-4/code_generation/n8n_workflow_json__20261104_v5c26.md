# Mistral Large 4.0 — code_generation/n8n_workflow_json

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 7.35 | quality: 8.6
- latency_total: 76.012s | tokens_per_second: 99.2
- input_tokens: 130 | output_tokens: 7540
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo de N8N con un enfoque claro y estructurado. Aunque la profundidad es adecuada, podría beneficiarse de más detalles sobre la configuración de Slack o la gestión de errores.

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

Aquí tienes el workflow completo de **n8n** en formato JSON. Guárdalo como `clasificar-slack.json` e impórtalo en n8n desde **Workflows → Import from File**.

```json
{
  "name": "Clasificar mensaje con IA y enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "lastNode",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 300],
      "id": "webhook-001",
      "name": "Webhook POST"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "email",
              "value": "={{ $json.body?.email || '' }}",
              "type": "string"
            },
            {
              "name": "message",
              "value": "={{ $json.body?.message || '' }}",
              "type": "string"
            }
          ]
        },
        "options": {
          "keepOnlySet": true
        }
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [220, 300],
      "id": "set-001",
      "name": "Extraer email y message"
    },
    {
      "parameters": {
        "operation": "message",
        "model": {
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes de clientes. Clasifica el mensaje en exactamente una de estas categorías: \"soporte\", \"ventas\" o \"otro\". Responde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin puntuación, sin comillas y sin ninguna explicación adicional."
            },
            {
              "role": "user",
              "content": "=Email del remitente: {{ $json.email }}\nMensaje:\n{{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.3,
      "position": [440, 300],
      "id": "openai-001",
      "name": "Clasificar con OpenAI",
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "name": "categoria",
              "value": "={{ ($json.choices[0].message.content || 'otro').toLowerCase().trim().replace(/[^a-zñáéíóú]/g, '') }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [660, 300],
      "id": "set-002",
      "name": "Normalizar categoría"
    },
    {
      "parameters": {
        "mode": "rules",
        "rules": {
          "values": [
            {
              "operation": "equal",
              "value1": "={{ $json.categoria }}",
              "value2": "soporte"
            },
            {
              "operation": "equal",
              "value1": "={{ $json.categoria }}",
              "value2": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "last"
        }
      },
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [880, 300],
      "id": "switch-001",
      "name": "Switch por categoría"
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=🛠️ *Nuevo mensaje — SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 180],
      "id": "slack-support",
      "name": "Slack #support",
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje — VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 300],
      "id": "slack-sales",
      "name": "Slack #sales",
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=📥 *Nuevo mensaje — OTRO*\n*Email:* {{ $json.email }}\n*Mensaje:*\n{{ $json.message }}",
        "otherOptions": {}
      },
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 420],
      "id": "slack-general",
      "name": "Slack #general",
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook POST": {
      "main": [
        [
          {
            "node": "Extraer email y message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer email y message": {
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
            "node": "Normalizar categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar categoría": {
      "main": [
        [
          {
            "node": "Switch por categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por categoría": {
      "main": [
        [
          {
            "node": "Slack #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "version": 1,
  "id": "wf-clasificar-slack-001",
  "meta": {
    "instanceId": "TU_INSTANCE_ID"
  },
  "tags": []
}
```

## Cómo usarlo

1. **Importa** el JSON en n8n (**Workflows → ⋮ → Import from File**).
2. **Configura las credenciales**:
   - En el nodo **Clasificar con OpenAI** → selecciona tu credencial de **OpenAI API** (reemplaza `TU_CREDENCIAL_OPENAI_ID`).
   - En los 3 nodos **Slack** → selecciona tu credencial de **Slack Bot Token** con permisos `chat:write` y acceso a los canales `#support`, `#sales`, `#general` (reemplaza `TU_CREDENCIAL_SLACK_ID`).
3. **Activa** el workflow. La URL productiva será:
   ```
   https://<tu-instancia-n8n>/webhook/clasificar-mensaje
   ```
   (en modo edición/test usa `/webhook-test/clasificar-mensaje`).

## Prueba con curl

```bash
curl -X POST https://<tu-instancia>/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"cliente@ejemplo.com","message":"No puedo iniciar sesión en mi cuenta, me da error 500"}'
```
Ese mensaje debería clasificarse como **soporte** y aparecer en `#support`. Prueba con `"Quiero saber precios del plan enterprise"` → `#sales`, y con cualquier otro texto → `#general`.

## Notas

- El webhook usa `responseMode: "lastNode"`, así que responde `200` con el resultado del nodo de Slack al finalizar.
- El nodo **Switch** usa `fallbackOutput: "last"`: si la IA devuelve cualquier cosa distinta de `soporte`/`ventas` (incluido "otro"), cae en la tercera salida → `#general`.
- Si prefieres forzar siempre una de las 3 categorías, el prompt del sistema ya lo indica; el nodo **Normalizar categoría** limpia mayúsculas y puntuación por si acaso.