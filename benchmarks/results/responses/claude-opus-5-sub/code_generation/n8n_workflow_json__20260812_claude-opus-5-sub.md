# Claude Opus 5 (suscripción) — code_generation/n8n_workflow_json

- model_id: `claude-opus-5`
- success: True  | final: 5.82 | quality: 7.2
- latency_total: 125.128s | tokens_per_second: 84.6
- input_tokens: 2 | output_tokens: 10580
- judge_score: 3.0 | justificación: 

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

Acá va el workflow completo, listo para importar (Workflows → ⋯ → Import from Clipboard).

```json
{
  "name": "Clasificador de Mensajes → Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [-320, 340],
      "webhookId": "f7c2a1e0-3b44-4c9a-9f10-8c1d2e3f4a55"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "f-email",
              "name": "email",
              "value": "={{ $json.body.email || '' }}",
              "type": "string"
            },
            {
              "id": "f-message",
              "name": "message",
              "value": "={{ $json.body.message || '' }}",
              "type": "string"
            },
            {
              "id": "f-recibido",
              "name": "recibido_en",
              "value": "={{ $now.toISO() }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer Datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [-100, 340]
    },
    {
      "parameters": {
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list",
          "cachedResultName": "GPT-4O-MINI"
        },
        "messages": {
          "values": [
            {
              "content": "Eres un clasificador de mensajes de contacto. Devuelve SOLO un objeto JSON válido, sin texto extra.\n\nCategorías permitidas:\n- soporte: problemas técnicos, bugs, errores, no puedo entrar, dudas de uso, reclamos, incidencias de facturación.\n- ventas: interés en comprar, precios, planes, demo, cotización, upgrade, partnership comercial.\n- otro: cualquier otra cosa (spam, prensa, postulaciones, saludos, texto ilegible).\n\nFormato exacto de salida:\n{\"categoria\": \"soporte\", \"confianza\": 0.93, \"razon\": \"reporta error de login\"}\n\nReglas:\n- categoria debe ser exactamente soporte, ventas u otro, en minúsculas.\n- Si dudas o el mensaje es ambiguo, usa otro.\n- razon: máximo 10 palabras.",
              "role": "system"
            },
            {
              "content": "=Email: {{ $json.email }}\nMensaje: {{ $json.message }}"
            }
          ]
        },
        "jsonOutput": true,
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Clasificar con IA",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [120, 340],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      },
      "onError": "continueRegularOutput"
    },
    {
      "parameters": {
        "jsCode": "// Normaliza la salida del modelo y garantiza que SIEMPRE haya una categoría válida.\nconst VALIDAS = ['soporte', 'ventas', 'otro'];\nconst salida = [];\n\nfor (let i = 0; i < items.length; i++) {\n  const ai = items[i].json ?? {};\n\n  // La forma exacta depende de simplify/jsonOutput y de la versión del nodo.\n  // Se cubren todas las variantes en vez de asumir una.\n  const candidato =\n    ai?.message?.content?.categoria ??\n    ai?.content?.categoria ??\n    ai?.categoria ??\n    (typeof ai?.message?.content === 'string' ? ai.message.content : null) ??\n    (typeof ai?.content === 'string' ? ai.content : null) ??\n    '';\n\n  let categoria = String(candidato)\n    .toLowerCase()\n    .replace(/[^a-záéíóúñ]/g, '');\n\n  // Fallback duro: si el modelo alucinó, se va a #general, no revienta el flujo.\n  if (!VALIDAS.includes(categoria)) categoria = 'otro';\n\n  const confianza = Number(\n    ai?.message?.content?.confianza ?? ai?.content?.confianza ?? ai?.confianza ?? 0\n  );\n  const razon = String(\n    ai?.message?.content?.razon ?? ai?.content?.razon ?? ai?.razon ?? 'sin detalle'\n  );\n\n  const origen = $('Extraer Datos').all()[i]?.json ?? {};\n\n  salida.push({\n    json: {\n      email: origen.email || 'desconocido',\n      message: origen.message || '',\n      recibido_en: origen.recibido_en,\n      categoria,\n      confianza: isNaN(confianza) ? 0 : confianza,\n      razon,\n    },\n  });\n}\n\nreturn salida;"
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Normalizar Clasificación",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [340, 340]
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
                    "id": "c-soporte",
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
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "strict",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "c-ventas",
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
                    "id": "c-otro",
                    "leftValue": "={{ $json.categoria }}",
                    "rightValue": "otro",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "renameOutput": true,
              "outputKey": "otro"
            }
          ]
        },
        "options": {
          "fallbackOutput": 2
        }
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Enrutar por Categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [560, 340]
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:tools: *Nuevo mensaje de SOPORTE*\n*De:* {{ $json.email }}\n*Confianza:* {{ $json.confianza }} — _{{ $json.razon }}_\n\n>>> {{ $json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Slack · #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [800, 140],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      },
      "webhookId": "b1c2d3e4-1111-4111-8111-111111111111"
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nuevo lead de VENTAS*\n*De:* {{ $json.email }}\n*Confianza:* {{ $json.confianza }} — _{{ $json.razon }}_\n\n>>> {{ $json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack · #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [800, 340],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      },
      "webhookId": "b1c2d3e4-2222-4222-8222-222222222222"
    },
    {
      "parameters": {
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:inbox_tray: *Mensaje sin clasificar (OTRO)*\n*De:* {{ $json.email }}\n*Confianza:* {{ $json.confianza }} — _{{ $json.razon }}_\n\n>>> {{ $json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false
        }
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack · #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [800, 540],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      },
      "webhookId": "b1c2d3e4-3333-4333-8333-333333333333"
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ JSON.stringify({ ok: true, email: $('Normalizar Clasificación').item.json.email, categoria: $('Normalizar Clasificación').item.json.categoria }) }}",
        "options": {}
      },
      "id": "a1b2c3d4-0009-4000-8000-000000000009",
      "name": "Responder al Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [1040, 340]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [[{ "node": "Extraer Datos", "type": "main", "index": 0 }]]
    },
    "Extraer Datos": {
      "main": [[{ "node": "Clasificar con IA", "type": "main", "index": 0 }]]
    },
    "Clasificar con IA": {
      "main": [[{ "node": "Normalizar Clasificación", "type": "main", "index": 0 }]]
    },
    "Normalizar Clasificación": {
      "main": [[{ "node": "Enrutar por Categoría", "type": "main", "index": 0 }]]
    },
    "Enrutar por Categoría": {
      "main": [
        [{ "node": "Slack · #support", "type": "main", "index": 0 }],
        [{ "node": "Slack · #sales", "type": "main", "index": 0 }],
        [{ "node": "Slack · #general", "type": "main", "index": 0 }]
      ]
    },
    "Slack · #support": {
      "main": [[{ "node": "Responder al Webhook", "type": "main", "index": 0 }]]
    },
    "Slack · #sales": {
      "main": [[{ "node": "Responder al Webhook", "type": "main", "index": 0 }]]
    },
    "Slack · #general": {
      "main": [[{ "node": "Responder al Webhook", "type": "main", "index": 0 }]]
    }
  },
  "settings": {
    "executionOrder": "v1"
  },
  "pinData": {},
  "staticData": null,
  "meta": {
    "instanceId": "reemplazar-instance-id"
  },
  "tags": []
}
```

## Qué reemplazar antes de activarlo

1. **Credenciales**: los `REEMPLAZAR_ID_CREDENCIAL_*`. Lo más simple es importar, abrir cada nodo y seleccionar la credencial desde el dropdown (n8n reescribe el ID solo).
2. **Slack**: el bot tiene que estar invitado a los 3 canales (`/invite @tu-bot`) y con scope `chat:write`. Si usás modo `name` y falla, cambiá el `channelId` a modo `list` y elegí el canal — así queda el ID `C0XXXXXXX`, que es más estable que el nombre.
3. **Modelo**: `gpt-4o-mini` con `temperature: 0`. Para esta tarea no necesitás nada más caro; clasificar 3 categorías no es un problema de razonamiento.

## Decisiones que vale la pena que veas

- **El nodo Code no es decorativo.** La forma exacta del output del nodo OpenAI cambia según `simplify`/`jsonOutput` y la versión del nodo (`$json.content`, `$json.message.content`, objeto ya parseado…). El Code cubre todas las variantes y, si el modelo alucina algo fuera de las 3 categorías, cae a `otro` en vez de tirar el flujo. Un clasificador sin fallback duro es una bomba de tiempo.
- **`onError: continueRegularOutput` en el nodo de IA**: si OpenAI se cae o da 429, el mensaje igual llega a `#general` en vez de perderse. Prefiero un mensaje mal ruteado que un mensaje perdido.
- **`fallbackOutput: 2` en el Switch**: cualquier cosa inesperada va a `#general`.
- **URL del webhook**: `https://tu-n8n/webhook/clasificar-mensaje` (en test es `/webhook-test/`).

Prueba rápida:

```bash
curl -X POST https://tu-n8n/webhook-test/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email":"ana@empresa.com","message":"No puedo entrar a mi cuenta, me tira error 403"}'
```

## Alternativa más corta (si querés menos nodos)

n8n tiene `@n8n/n8n-nodes-langchain.textClassifier`: le declarás las categorías y **te da una salida por cada una**, sin Switch, sin Code, sin parsear JSON. Usa un sub-nodo `lmChatOpenAi` como modelo. Quedan 6 nodos en vez de 9.

Se lo dejé con OpenAI + Switch porque es lo que pediste, es más portable entre versiones de n8n y te deja ver la razón de la clasificación en Slack (útil las primeras semanas para calibrar el prompt). Si después de 200 mensajes la clasificación te convence, migrá al Text Classifier y borrá el Code.