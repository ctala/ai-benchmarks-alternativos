# Muse Glimmer 30B — code_generation/n8n_workflow_json

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.25 | quality: 8.4
- latency_total: 93.738s | tokens_per_second: 44.5
- input_tokens: 170 | output_tokens: 4173
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una estructura clara y utilidad práctica para implementar el flujo de trabajo en n8n, aunque carece de profundidad en términos de insights adicionales.

## Respuesta completa

Aquí tienes un workflow completo de n8n listo para importar. Activa con POST, clasifica con OpenAI y envía a Slack según la categoría.

```json
{
  "name": "Clasificador Email -> Slack",
  "nodes": [
    {
      "parameters": {
        "path": "classify-message",
        "httpMethod": "POST",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "webhook1",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            { "name": "email", "value": "={{$json.email}}" },
            { "name": "message", "value": "={{$json.message}}" }
          ]
        }
      },
      "id": "set1",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "model": "gpt-4o-mini",
        "messages": {
          "messages": [
            {
              "role": "system",
              "content": "Eres un clasificador. Clasifica el mensaje del usuario como soporte, ventas u otro. Responde únicamente con una de esas tres palabras."
            },
            {
              "role": "user",
              "content": "Email: {{$json.email}}\nMensaje: {{$json.message}}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai1",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [680, 300]
    },
    {
      "parameters": {
        "jsCode": "const content = items[0].json.choices?.[0]?.message?.content?.trim().toLowerCase() || 'otro';\nconst email = $items('Extraer Datos', 0, 0).json.email;\nconst message = $items('Extraer Datos', 0, 0).json.message;\nreturn [{ json: { classification: content, email, message } }];"
      },
      "id": "code1",
      "name": "Extraer Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [900, 300]
    },
    {
      "parameters": {
        "ruleSet": {
          "rules": {
            "string": [
              { "operation": "equal", "value": "soporte" },
              { "operation": "equal", "value": "ventas" },
              { "operation": "equal", "value": "otro" }
            ]
          }
        },
        "value1": "={{$json.classification}}"
      },
      "id": "switch1",
      "name": "Switch por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "create",
        "channel": "#support",
        "text": "Nuevo mensaje clasificado como **soporte**\nEmail: {{$json.email}}\nMensaje: {{$json.message}}"
      },
      "id": "slack1",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1340, 200]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "create",
        "channel": "#sales",
        "text": "Nuevo mensaje clasificado como **ventas**\nEmail: {{$json.email}}\nMensaje: {{$json.message}}"
      },
      "id": "slack2",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1340, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "create",
        "channel": "#general",
        "text": "Nuevo mensaje clasificado como **otro**\nEmail: {{$json.email}}\nMensaje: {{$json.message}}"
      },
      "id": "slack3",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1340, 400]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          { "node": "Extraer Datos", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer Datos": {
      "main": [
        [
          { "node": "Clasificar con OpenAI", "type": "main", "index": 0 }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          { "node": "Extraer Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer Clasificación": {
      "main": [
        [
          { "node": "Switch por Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Switch por Clasificación": {
      "main": [
        [
          { "node": "Slack #support", "type": "main", "index": 0 }
        ],
        [
          { "node": "Slack #sales", "type": "main", "index": 0 }
        ],
        [
          { "node": "Slack #general", "type": "main", "index": 0 }
        ]
      ]
    }
  },
  "pinData": {},
  "meta": {
    "instanceId": ""
  }
}
```

**Cómo usarlo**

1. Importa el JSON en n8n.
2. Configura las credenciales de OpenAI y Slack.
3. El webhook estará disponible en `https://<tu-dominio>/webhook/classify-message`.
4. Envía POST con body JSON: `{ "email": "usuario@ejemplo.com", "message": "texto..." }`

El workflow extrae los campos, clasifica con OpenAI y envía el mensaje al canal correspondiente.