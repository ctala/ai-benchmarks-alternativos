# Claude Opus 4.8 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-opus-4-8`
- success: True  | final: 6.45 | quality: 8.6
- latency_total: 77.827s | tokens_per_second: 106.1
- input_tokens: 2028 | output_tokens: 8254
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un JSON bien estructurado. Aunque la profundidad es adecuada, no ofrece insights adicionales más allá de la implementación básica, pero es clara y prácticamente útil para un emprendedor.

## Respuesta completa

No pude guardar el archivo (falta permiso de escritura), así que te dejo el JSON directamente abajo. Está listo para importar en N8N (**Workflows → ⋮ → Import from File / Paste**).

## Estructura del flujo

```
Webhook (POST) → Extraer Campos → Clasificar (OpenAI) → Normalizar Categoría → Switch
                                                                                  ├─ soporte → Slack #support ─┐
                                                                                  ├─ ventas  → Slack #sales   ─┤→ Responder Webhook
                                                                                  └─ otro    → Slack #general ─┘
```

## JSON completo

```json
{
  "name": "Clasificador de Mensajes -> Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "b1a1e1d0-0001-4a00-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 400],
      "webhookId": "clasificar-mensaje"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f0000000-0000-0000-0000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "f0000000-0000-0000-0000-000000000002",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b1a1e1d0-0002-4a00-8000-000000000002",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 400]
    },
    {
      "parameters": {
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
              "content": "Eres un clasificador de mensajes. Lee el mensaje del usuario y responde con UNA sola palabra en minusculas, sin puntuacion ni explicacion: \"soporte\", \"ventas\" u \"otro\".\n- \"soporte\": problemas tecnicos, errores, ayuda con un producto/servicio ya adquirido, reclamos.\n- \"ventas\": interes en comprar, cotizaciones, precios, demos, informacion comercial.\n- \"otro\": cualquier cosa que no encaje en las anteriores."
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
      "id": "b1a1e1d0-0003-4a00-8000-000000000003",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [680, 400],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CRED_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f0000000-0000-0000-0000-000000000010",
              "name": "categoria",
              "value": "={{ $json.message.content.toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "f0000000-0000-0000-0000-000000000011",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "f0000000-0000-0000-0000-000000000012",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b1a1e1d0-0004-4a00-8000-000000000004",
      "name": "Normalizar Categoria",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [900, 400]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "c0000000-0000-0000-0000-000000000001",
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "id": "c0000000-0000-0000-0000-000000000002",
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "contains"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "ventas"
            }
          ]
        },
        "options": {
          "fallbackOutput": "extra"
        }
      },
      "id": "b1a1e1d0-0005-4a00-8000-000000000005",
      "name": "Switch Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 400]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:incoming_envelope: *Nuevo mensaje de SOPORTE*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "b1a1e1d0-0006-4a00-8000-000000000006",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1380, 200],
      "webhookId": "",
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "b1a1e1d0-0007-4a00-8000-000000000007",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1380, 400],
      "webhookId": "",
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:speech_balloon: *Nuevo mensaje (OTRO)*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "b1a1e1d0-0008-4a00-8000-000000000008",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1380, 600],
      "webhookId": "",
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ { \"status\": \"ok\", \"categoria\": $('Normalizar Categoria').item.json.categoria } }}",
        "options": {}
      },
      "id": "b1a1e1d0-0009-4a00-8000-000000000009",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1640, 400]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [[{ "node": "Extraer Campos", "type": "main", "index": 0 }]]
    },
    "Extraer Campos": {
      "main": [[{ "node": "Clasificar con OpenAI", "type": "main", "index": 0 }]]
    },
    "Clasificar con OpenAI": {
      "main": [[{ "node": "Normalizar Categoria", "type": "main", "index": 0 }]]
    },
    "Normalizar Categoria": {
      "main": [[{ "node": "Switch Categoria", "type": "main", "index": 0 }]]
    },
    "Switch Categoria": {
      "main": [
        [{ "node": "Slack #support", "type": "main", "index": 0 }],
        [{ "node": "Slack #sales", "type": "main", "index": 0 }],
        [{ "node": "Slack #general", "type": "main", "index": 0 }]
      ]
    },
    "Slack #support": {
      "main": [[{ "node": "Responder Webhook", "type": "main", "index": 0 }]]
    },
    "Slack #sales": {
      "main": [[{ "node": "Responder Webhook", "type": "main", "index": 0 }]]
    },
    "Slack #general": {
      "main": [[{ "node": "Responder Webhook", "type": "main", "index": 0 }]]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "active": false,
  "pinData": {},
  "tags": []
}
```

## Notas para que funcione

1. **Credenciales**: tras importar, abre los nodos *Clasificar con OpenAI* y los 3 *Slack* y selecciona tus credenciales reales. Los placeholders `OPENAI_CRED_ID` / `SLACK_CRED_ID` se reemplazan solos al elegirlas en el dropdown.
2. **Webhook URL**: el path es `/clasificar-mensaje`. Envía un POST con body JSON:
   ```json
   { "email": "cliente@ejemplo.com", "message": "Tengo un error al iniciar sesión" }
   ```
3. **El Switch usa `contains`** (no `equals`) como red de seguridad: si el modelo devuelve algo como `"soporte."` igual matchea. La salida fallback (`otro`) va a `#general`.
4. **Canales Slack en modo `name`**: si tu nodo Slack te exige ID en vez de nombre, cambia `"mode": "name"` por `"mode": "id"` y pon el ID del canal (`C0xxxx`). Recuerda invitar al bot a cada canal (`/invite @tu-bot`).
5. **Modelo**: usé `gpt-4o-mini` con `temperature: 0` (barato y determinista para clasificar). Cámbialo si prefieres otro.

¿Quieres que lo adapte para usar OpenRouter en vez de OpenAI directo, o que en lugar de `email`/`message` planos lo lea de otra estructura del body?