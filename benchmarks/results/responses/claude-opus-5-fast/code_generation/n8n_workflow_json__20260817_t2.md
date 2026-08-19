# Claude Opus 5 Fast — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.87 | quality: 8.6
- latency_total: 28.327s | tokens_per_second: 281.8
- input_tokens: 175 | output_tokens: 7982
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del flujo de trabajo con un enfoque claro y estructurado, aunque carece de profundidad adicional más allá de la implementación básica.

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

Aquí tienes el workflow completo, listo para importar en n8n (**Workflows → ⋯ → Import from File / Paste JSON**).

## JSON del workflow

```json
{
  "name": "Clasificador de Mensajes con IA → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "11111111-1111-4111-8111-111111111111",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-220, 300],
      "webhookId": "a7c3f9e2-4b1d-4f2a-9c8e-1d2b3a4c5d6e"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "a2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "22222222-2222-4222-8222-222222222222",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [0, 300]
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
              "content": "Eres un clasificador de mensajes de clientes. Clasifica el mensaje en UNA de estas categorías:\n- \"soporte\": problemas técnicos, errores, bugs, dudas sobre el uso del producto, incidencias, reclamaciones de servicio.\n- \"ventas\": precios, planes, presupuestos, demos, contratación, upgrades, facturación comercial, interés en comprar.\n- \"otro\": cualquier cosa que no encaje claramente en las anteriores (spam, saludos, prensa, empleo, etc.).\n\nResponde ÚNICAMENTE con un JSON válido con esta forma exacta:\n{\"categoria\": \"soporte\", \"confianza\": 0.95, \"resumen\": \"resumen en una frase\"}\n\nEl campo \"categoria\" solo puede valer: soporte, ventas u otro.",
              "role": "system"
            },
            {
              "content": "=Email del remitente: {{ $json.email }}\n\nMensaje:\n\"\"\"\n{{ $json.message }}\n\"\"\"",
              "role": "user"
            }
          ]
        },
        "jsonOutput": true,
        "options": {
          "temperature": 0
        }
      },
      "id": "33333333-3333-4333-8333-333333333333",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [220, 300],
      "credentials": {
        "openAiApi": {
          "id": "OPENAI_CRED_ID",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "mode": "runOnceForEachItem",
        "jsCode": "// Normaliza la respuesta del modelo pase lo que pase\nconst raw = $json.message?.content ?? $json.content ?? $json.text ?? $json;\n\nlet parsed = raw;\nif (typeof raw === 'string') {\n  try {\n    parsed = JSON.parse(raw.replace(/```json|```/g, '').trim());\n  } catch (e) {\n    parsed = { categoria: raw.trim().toLowerCase() };\n  }\n}\n\nconst validas = ['soporte', 'ventas', 'otro'];\nlet categoria = String(parsed?.categoria ?? 'otro').toLowerCase().trim();\nif (!validas.includes(categoria)) categoria = 'otro';\n\nconst datos = $('Extraer Datos').item.json;\n\nreturn {\n  json: {\n    email: datos.email,\n    mensaje: datos.message,\n    categoria,\n    confianza: parsed?.confianza ?? null,\n    resumen: parsed?.resumen ?? ''\n  }\n};"
      },
      "id": "44444444-4444-4444-8444-444444444444",
      "name": "Normalizar Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [440, 300]
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c1",
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
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c2",
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
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "otro"
        }
      },
      "id": "55555555-5555-4555-8555-555555555555",
      "name": "Router por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [660, 300]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:tools: *Nuevo mensaje de SOPORTE*\n*Email:* {{ $json.email }}\n*Resumen:* {{ $json.resumen }}\n*Confianza:* {{ $json.confianza }}\n\n>>> {{ $json.mensaje }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "66666666-6666-4666-8666-666666666666",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [920, 100],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nuevo mensaje de VENTAS*\n*Email:* {{ $json.email }}\n*Resumen:* {{ $json.resumen }}\n*Confianza:* {{ $json.confianza }}\n\n>>> {{ $json.mensaje }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "77777777-7777-4777-8777-777777777777",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [920, 300],
      "credentials": {
        "slackApi": {
          "id": "SLACK_CRED_ID",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:inbox_tray: *Nuevo mensaje (OTRO)*\n*Email:* {{ $json.email }}\n*Resumen:* {{ $json.resumen }}\n*Confianza:* {{ $json.confianza }}\n\n>>> {{ $json.mensaje }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "88888888-8888-4888-8888-888888888888",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [920, 500],
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
        "responseBody": "={{ JSON.stringify({ ok: true, categoria: $('Normalizar Clasificación').item.json.categoria, email: $('Normalizar Clasificación').item.json.email }) }}",
        "options": {}
      },
      "id": "99999999-9999-4999-8999-999999999999",
      "name": "Responder Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1180, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer Datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer Datos": {
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
            "node": "Normalizar Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar Clasificación": {
      "main": [
        [
          {
            "node": "Router por Categoría",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Router por Categoría": {
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
            "node": "Responder Webhook",
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
            "node": "Responder Webhook",
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
            "node": "Responder Webhook",
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
  "pinData": {},
  "active": false,
  "tags": []
}
```

## Notas para ponerlo en marcha

1. **Credenciales**: tras importar, abre los nodos `Clasificar con OpenAI` y los tres `Slack #...` y selecciona tus credenciales (los IDs `OPENAI_CRED_ID` / `SLACK_CRED_ID` son placeholders y aparecerán en rojo).
2. **Slack**: el bot necesita el scope `chat:write` y estar invitado a los canales (`/invite @tu-bot` en `#support`, `#sales`, `#general`). Si prefieres seleccionar el canal por ID, cambia `"mode": "name"` por `"mode": "list"` y pon el `C0xxxxxxx` en `value`.
3. **Prueba** (URL de test que te da el nodo Webhook):

```bash
curl -X POST https://TU-N8N/webhook-test/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"ana@empresa.com","message":"La app me da error 500 al iniciar sesión"}'
```

4. **Por qué el nodo Code**: la salida del nodo OpenAI puede llegar como objeto o como string (a veces envuelto en ``` ```json ```). El nodo `Normalizar Clasificación` fuerza siempre una categoría válida (`otro` como fallback), evitando que el Switch se quede sin ruta.
5. **Alternativa más corta**: puedes sustituir OpenAI + Code + Switch por el nodo `@n8n/n8n-nodes-langchain.textClassifier` con un sub-nodo `lmChatOpenAi`, que ya expone una salida por categoría. Lo he hecho con Switch porque te da control total sobre el prompt, la confianza y el fallback.