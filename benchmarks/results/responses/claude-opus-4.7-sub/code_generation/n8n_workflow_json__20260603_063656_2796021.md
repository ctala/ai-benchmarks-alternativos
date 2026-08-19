# Claude Opus 4.7 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-opus-4-7`
- success: True  | final: 6.58 | quality: 8.6
- latency_total: 58.376s | tokens_per_second: 88.6
- input_tokens: 6 | output_tokens: 5172
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un JSON bien estructurado. Aunque la profundidad es moderada, la claridad y utilidad práctica son altas, lo que permite a un emprendedor usarla directamente.

## Respuesta completa

# Workflow N8N: Clasificación de Mensajes con IA

Aquí tenés el JSON completo del workflow. Lo podés importar directo en N8N desde `Workflows > Import from File` o pegándolo en `Import from Clipboard`.

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 400],
      "webhookId": "clasificar-mensaje-webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-assign",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-assign",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-4b5c-9d0e-1f2a3b4c5d6e",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 400]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "complete",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Sos un clasificador de mensajes de clientes. Analizá el mensaje y respondé ÚNICAMENTE con una de estas tres palabras en minúsculas, sin puntuación ni explicaciones adicionales:\n\n- soporte: si el mensaje es sobre problemas técnicos, bugs, errores, dudas de uso del producto, reclamos o solicitudes de ayuda\n- ventas: si el mensaje es sobre precios, planes, compras, cotizaciones, demos, o interés comercial\n- otro: si el mensaje no encaja en las categorías anteriores (saludos, feedback general, consultas misceláneas)\n\nRespondé SOLO la palabra. Nada más."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0,
          "maxTokens": 10
        }
      },
      "id": "c3d4e5f6-a7b8-4c5d-0e1f-2a3b4c5d6e7f",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.6,
      "position": [680, 400],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CRED_ID",
          "name": "OpenAI API"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "categoria-assign",
              "name": "categoria",
              "value": "={{ $json.message.content.toLowerCase().trim() }}",
              "type": "string"
            },
            {
              "id": "email-passthrough",
              "name": "email",
              "value": "={{ $('Extraer Campos').item.json.email }}",
              "type": "string"
            },
            {
              "id": "message-passthrough",
              "name": "message",
              "value": "={{ $('Extraer Campos').item.json.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "d4e5f6a7-b8c9-4d5e-1f2a-3b4c5d6e7f8a",
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
                    "id": "cond-soporte",
                    "leftValue": "={{ $json.categoria }}",
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
                    "id": "cond-ventas",
                    "leftValue": "={{ $json.categoria }}",
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
              "outputKey": "ventas"
            }
          ]
        },
        "fallbackOutput": "extra",
        "options": {
          "renameFallbackOutput": "otro"
        }
      },
      "id": "e5f6a7b8-c9d0-4e5f-2a3b-4c5d6e7f8a9b",
      "name": "Switch por Categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [1120, 400]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:rotating_light: *Nuevo mensaje de SOPORTE*\n\n*De:* {{ $json.email }}\n*Mensaje:*\n```\n{{ $json.message }}\n```",
        "otherOptions": {}
      },
      "id": "f6a7b8c9-d0e1-4f5a-3b4c-5d6e7f8a9b0c",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 200],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nueva oportunidad de VENTAS*\n\n*De:* {{ $json.email }}\n*Mensaje:*\n```\n{{ $json.message }}\n```",
        "otherOptions": {}
      },
      "id": "a7b8c9d0-e1f2-4a5b-4c5d-6e7f8a9b0c1d",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 400],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:speech_balloon: *Mensaje sin categorizar*\n\n*De:* {{ $json.email }}\n*Mensaje:*\n```\n{{ $json.message }}\n```",
        "otherOptions": {}
      },
      "id": "b8c9d0e1-f2a3-4b5c-5d6e-7f8a9b0c1d2e",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1380, 600],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack API"
        }
      }
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={\n  \"status\": \"ok\",\n  \"categoria\": \"{{ $('Normalizar Categoria').item.json.categoria }}\",\n  \"email\": \"{{ $('Normalizar Categoria').item.json.email }}\"\n}",
        "options": {}
      },
      "id": "c9d0e1f2-a3b4-4c5d-6e7f-8a9b0c1d2e3f",
      "name": "Respond Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1640, 400]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Campos": {
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
            "node": "Normalizar Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Categoria": {
      "main": [
        [
          {
            "node": "Switch por Categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch por Categoria": {
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
    },
    "Slack #support": {
      "main": [
        [
          {
            "node": "Respond Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #sales": {
      "main": [
        [
          {
            "node": "Respond Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Slack #general": {
      "main": [
        [
          {
            "node": "Respond Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "pinData": {},
  "versionId": "1.0.0",
  "triggerCount": 1,
  "tags": []
}
```

## Flujo del workflow

```
Webhook (POST) → Extraer Campos → Clasificar con OpenAI → Normalizar Categoria → Switch
                                                                                   ├── soporte → Slack #support ─┐
                                                                                   ├── ventas  → Slack #sales   ─┼→ Respond
                                                                                   └── otro    → Slack #general ─┘
```

## Pasos para importarlo

1. **En N8N**: `Workflows > Add workflow > Import from Clipboard` → pegar el JSON
2. **Configurar credenciales** (reemplazar los placeholders):
   - **OpenAI API**: cambiar `OPENAI_CRED_ID` por tu credential real desde la UI (clic en el nodo → seleccionar credential)
   - **Slack API**: cambiar `SLACK_CRED_ID` por tu credential de Slack (OAuth2 o Access Token con scopes `chat:write`)
3. **Activar el workflow** con el toggle arriba a la derecha
4. **Copiar la URL del webhook** (en el nodo Webhook → Production URL)

## Probarlo con curl

```bash
curl -X POST https://tu-n8n.com/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@ejemplo.com",
    "message": "Hola, no me deja loguear en la app, me tira error 500"
  }'
```

## Decisiones de diseño

- **`gpt-4o-mini`** como clasificador: rápido, barato (~$0.15/M input), suficiente para clasificación de 3 clases. Si querés algo más barato podés cambiarlo por `deepseek-chat` o `gemini-2.0-flash-lite` (el ranking 4 de tu benchmark — 165 tok/s).
- **`temperature: 0` + `maxTokens: 10`**: clasificación determinística, evita que el modelo divague.
- **Nodo "Normalizar Categoria"**: aplica `toLowerCase().trim()` para que el switch no falle si el LLM responde con `"Soporte"` o `" ventas\n"`.
- **Fallback `otro`** en el switch: si el LLM responde algo inesperado (ej. `"reclamo"`), cae automáticamente a `#general` en lugar de romper el flujo.
- **Respond to Webhook** al final: devuelve confirmación al cliente con la categoría asignada (útil para debugging y para que el frontend que llame al webhook sepa qué pasó).

## Mejoras opcionales

- **Reemplazar OpenAI por modelo local** (alineado con tu setup): cambiar el nodo OpenAI por un HTTP Request a `http://localhost:11434/api/chat` con `qwen3.5:397b-cloud` o `devstral-small` (tu top 1 del benchmark, $0.10/$0.30).
- **Agregar logging**: insertar un nodo Google Sheets o Postgres entre "Normalizar Categoria" y "Switch" para auditar todas las clasificaciones.
- **Manejo de errores**: agregar un nodo Error Trigger que mande a `#general` con tag `[ERROR]` si OpenAI falla.