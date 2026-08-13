# Claude Sonnet 5 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-sonnet-5`
- success: True  | final: 6.87 | quality: 8.4
- latency_total: 92.386s | tokens_per_second: 99.9
- input_tokens: 2 | output_tokens: 9232
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un workflow JSON bien estructurado que cumple con los requisitos especificados, aunque carece de detalles adicionales que podrían profundizar en la configuración o manejo de errores.

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

Acá tienes el workflow completo. Después del JSON dejo las notas de setup que necesitas para que corra sin sorpresas.

```json
{
  "name": "Clasificador de Mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-200, 0],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "mode": "manual",
        "duplicateItem": false,
        "assignments": {
          "assignments": [
            {
              "id": "e1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "e2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [20, 0]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes entrantes de atención al cliente. Clasifica el mensaje del usuario en EXACTAMENTE una de estas tres categorías: soporte, ventas, otro. Responde ÚNICAMENTE con la palabra de la categoría en minúsculas, sin puntuación ni explicaciones."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.3,
      "position": [240, 0],
      "credentials": {
        "openAiApi": {
          "id": "REPLACE_WITH_YOUR_CREDENTIAL_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const source = $('Extraer Campos').item.json;\nconst raw = $input.item.json;\n\nlet text = '';\nif (raw.message && raw.message.content) {\n  text = raw.message.content;\n} else if (raw.choices && raw.choices[0] && raw.choices[0].message) {\n  text = raw.choices[0].message.content;\n} else if (raw.content) {\n  text = raw.content;\n} else if (raw.text) {\n  text = raw.text;\n}\n\nconst classification = text.toString().trim().toLowerCase();\n\nreturn {\n  json: {\n    email: source.email,\n    message: source.message,\n    classification\n  }\n};"
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Normalizar Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [460, 0]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c1",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c2",
                    "leftValue": "={{ $json.classification }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "Ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Enrutar por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [680, 0]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "support",
          "mode": "name"
        },
        "text": "=📩 Nuevo mensaje clasificado como *SOPORTE*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [920, -160],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "sales",
          "mode": "name"
        },
        "text": "=💰 Nuevo mensaje clasificado como *VENTAS*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [920, 0],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "general",
          "mode": "name"
        },
        "text": "=📨 Nuevo mensaje clasificado como *OTRO*\n\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack - Otro",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [920, 160],
      "credentials": {
        "slackApi": {
          "id": "REPLACE_WITH_YOUR_CREDENTIAL_ID",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          { "node": "Extraer Campos", "type": "main", "index": 0 }
        ]
      ]
    },
    "Extraer Campos": {
      "main": [
        [
          { "node": "Clasificar con OpenAI", "type": "main", "index": 0 }
        ]
      ]
    },
    "Clasificar con OpenAI": {
      "main": [
        [
          { "node": "Normalizar Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Normalizar Clasificación": {
      "main": [
        [
          { "node": "Enrutar por Clasificación", "type": "main", "index": 0 }
        ]
      ]
    },
    "Enrutar por Clasificación": {
      "main": [
        [
          { "node": "Slack - Soporte", "type": "main", "index": 0 }
        ],
        [
          { "node": "Slack - Ventas", "type": "main", "index": 0 }
        ],
        [
          { "node": "Slack - Otro", "type": "main", "index": 0 }
        ]
      ]
    }
  },
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "active": false,
  "versionId": "1"
}
```

**Setup necesario antes de importarlo:**

1. **Credenciales** — hay 2 placeholders (`REPLACE_WITH_YOUR_CREDENTIAL_ID`): OpenAI API y Slack API. Al importar, n8n te va a pedir que las asignes a tus credenciales reales (o vincula por nombre si ya tienes una "OpenAI account" / "Slack account" creada).

2. **URL del webhook** — queda en `https://tu-instancia-n8n.com/webhook/clasificar-mensaje`. El body esperado:
```json
{ "email": "usuario@ejemplo.com", "message": "No puedo iniciar sesión en mi cuenta" }
```

3. **Nombres de canal Slack** — el nodo Slack está configurado con `mode: "name"` y valores `support`, `sales`, `general` (sin el `#`). Si tu bot de Slack no tiene el nombre exacto del canal o prefieres usar el ID del canal, cambia `mode` a `"id"` y pon el ID en `value` (más confiable si el canal se renombra).

4. **Nodo "Normalizar Clasificación"** — es un Code node que resuelve el output del nodo OpenAI sin importar exactamente cómo lo formatee tu versión de n8n (`message.content`, `choices[0].message.content`, etc.). Es la parte más frágil del pipeline si actualizas n8n — si algo falla ahí primero, revisa qué shape trae el JSON de salida del nodo OpenAI con "Execute step" y ajusta.

5. **Fallback del Switch** — configuré solo 2 reglas explícitas (soporte, ventas) + `fallbackOutput: "extra"` como tercer output. Esto significa que "otro" Y cualquier respuesta inesperada del modelo (typos, idioma distinto, etc.) caen en `#general` — es el comportamiento seguro por defecto, no necesitas una tercera regla exacta.

6. **`responseMode: "onReceived"`** — el webhook responde 200 inmediato sin esperar a que termine todo el flujo. Si necesitas que quien llama al webhook espere confirmación real, cambia a `"lastNode"`.