# MiniMax M3 (directo / sub) — code_generation/n8n_workflow_json

- model_id: `MiniMax-M3`
- success: True  | final: 6.85 | quality: 8.32
- latency_total: 144.137s | tokens_per_second: 37.0
- input_tokens: 292 | output_tokens: 5326
- judge_score: 3.8 | justificación: 

## Respuesta completa

<think>
The user wants me to generate a complete N8N workflow in JSON format. Let me break down the requirements:

1. Webhook trigger (POST)
2. Extract "email" and "message" from body
3. Use OpenAI node to classify the message into "soporte", "ventas", or "otro"
4. Use a Switch/IF node to route to different Slack channels based on classification

Let me build a complete, valid N8N workflow JSON.

Key considerations:
- N8N workflow structure includes nodes, connections, settings, and pinData
- Each node needs a unique name, type, typeVersion, position, and parameters
- Connections link nodes together
- I need to use proper N8N node types:
  - `n8n-nodes-base.webhook` for the trigger
  - `n8n-nodes-base.set` or `n8n-nodes-base.code` to extract fields
  - `@n8n/n8n-nodes-langchain.openAi` or `n8n-nodes-base.openAi` for OpenAI
  - `n8n-nodes-base.switch` for routing
  - `n8n-nodes-base.slack` for Slack messages

Let me think about the version of OpenAI node. The newer one is `@n8n/n8n-nodes-langchain.openAi` but the simpler one for basic completion is `n8n-nodes-base.openAi`. I'll use the langchain one as it's more current and supports the chat model.

Actually, for simplicity and broad compatibility, I'll use the `n8n-nodes-base.openAi` node which is straightforward for a classification task.

Let me design the workflow:

1. **Webhook Node** - POST endpoint
2. **Set Node** - Extract email and message into clean fields
3. **OpenAI Node** - Classify the message
4. **Switch Node** - Route based on classification
5. **Slack Nodes** (3x) - Send to different channels

Let me write the JSON:

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "webhook-node-id",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhookId": "unique-webhook-id"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "email-assignment",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "message-assignment",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-node-id",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "messages": [
          {
            "role": "system",
            "content": "Eres un clasificador de mensajes. Responde SOLO con una de estas tres palabras: 'soporte', 'ventas' u 'otro'. Clasifica el siguiente mensaje del usuario."
          },
          {
            "role": "user",
            "content": "={{ $json.message }}"
          }
        ],
        "simplifyOutput": true
      },
      "id": "openai-node-id",
      "name": "Classify with AI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [680, 300]
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
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "soporte",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": true,
                  "leftValue": "",
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content }}",
                    "rightValue": "ventas",
                    "operator": {
                      "type": "string",
                      "operation": "equals"
                    }
                  }
                ],
                "combinator": "and"
              },
              "outputKey": "ventas"
            }
          ]
        },
        "options": {}
      },
      "id": "switch-node-id",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [900, 300]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=📩 *Nuevo mensaje de SOPORTE*\n*De:* {{ $('Extract Fields').item.json.email }}\n*Mensaje:* {{ $('Extract Fields').item.json.message }}\n*Clasificación:* soporte",
        "otherOptions": {}
      },
      "id": "slack-support-id",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 200]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje de VENTAS*\n*De:* {{ $('Extract Fields').item.json.email }}\n*Mensaje:* {{ $('Extract Fields').item.json.message }}\n*Clasificación:* ventas",
        "otherOptions": {}
      },
      "id": "slack-sales-id",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 300]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📌 *Nuevo mensaje GENERAL*\n*De:* {{ $('Extract Fields').item.json.email }}\n*Mensaje:* {{ $('Extract Fields').item.json.message }}\n*Clasificación:* otro",
        "otherOptions": {}
      },
      "id": "slack-general-id",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1120, 400]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "Classify with AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify with AI": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
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
  "tags": [],
  "triggerCount": 1,
  "updatedAt": "2024-01-15T10:00:00.000Z",
  "versionId": "1"
}
```

Wait, I need to reconsider the Switch node output. The Switch node has multiple outputs and each rule goes to a different output. The "fallback" output (when no rules match) would go to "otro".

Let me revise this. The Switch node by default has one output per rule plus a fallback output. So:
- Output 0: soporte -> Slack Support
- Output 1: ventas -> Slack Sales
- Output 2 (fallback): otro -> Slack General

Let me also make the OpenAI node's response handling clearer. With `simplifyOutput: true`, the response structure changes. Let me think about the proper path.

With the LangChain OpenAI node v1, the output structure typically is:
```
{
  "message": {
    "role": "assistant",
    "content": "soporte"
  }
}
```

So `$json.message.content` would give us the classification. That should work.

Let me also add a note about credentials - the user will need to set up OpenAI and Slack credentials in N8N.

Let me also add proper settings and meta info. I'll finalize the JSON.

One more consideration: the Switch node in N8N v1 with `typeVersion: 3` uses the rules format. I need to make sure the format is correct.

Actually, let me check the Switch node format more carefully. The v3 Switch node uses:
```json
{
  "rules": {
    "values": [
      {
        "conditions": {...},
        "renameOutput": true,
        "outputKey": "soporte"
      }
    ]
  }
}
```

And the connections need to map each output index to the corresponding node. So if there are 2 rules, there are 3 outputs (0, 1 for the rules, and 2 for the fallback).

Wait, that's not right either. In N8N Switch, if you have N rules, you have N+1 outputs (the last one being the fallback). The `renameOutput` and `outputKey` are for naming the outputs in the UI.

Let me also think about whether to use `n8n-nodes-base.openAi` (legacy) or `@n8n/n8n-nodes-langchain.openAi` (new). The new one is recommended for new workflows, but requires the LangChain nodes package to be installed. The legacy one is more universally available.

I'll go with the legacy `n8n-nodes-base.openAi` for broader compatibility.

Let me restructure for the legacy OpenAI node:
```json
{
  "parameters": {
    "operation": "text",
    "model": "gpt-4o-mini",
    "prompt": {
      "value": "..."
    }
  }
}
```

Actually, the legacy OpenAI node has different operations. Let me use "message" operation (chat completion):

```json
{
  "parameters": {
    "operation": "message",
    "modelId": "gpt-4o-mini",
    "messages": [...]
  }
}
```

Hmm, the legacy node's typeVersion and parameters structure... Let me just use a generic structure that should work.

Actually, for the cleanest and most modern approach, let me use the LangChain OpenAI node which is the recommended one in current N8N versions. The structure is:

```json
{
  "type": "@n8n/n8n-nodes-langchain.openAi",
  "typeVersion": 1,
  "parameters": {
    "resource": "chat",
    "operation": "message",
    "modelId": {"__rl": true, "value": "gpt-4o-mini", "mode": "list"},
    "messages": [...],
    "simplifyOutput": true
  }
}
```

OK let me finalize this. I'll also add a fallback option for "otro" as the default route.

Let me also make sure the workflow JSON is complete and valid for import into N8N. I'll include:
- A unique `id` for the workflow
- A descriptive `name`
- All required `nodes` array
- All required `connections` object
- `settings` with execution order
- `versionId` and `meta` if needed

Let me write the final version now.

For the Switch node connections, since it has 2 rules and 1 fallback, that's 3 outputs total:
- Output 0 (soporte rule matched) -> Slack Soporte
- Output 1 (ventas rule matched) -> Slack Ventas
- Output 2 (fallback) -> Slack General

Let me write the final JSON:
</think>
# Workflow N8N - Clasificador de Mensajes con IA

Aquí tienes el JSON completo del workflow. Puedes importarlo directamente en N8N (`Ctrl+O` o arrastrando el archivo).

```json
{
  "name": "Clasificador de Mensajes con IA",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "responseMode": "onReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "11111111-1111-1111-1111-111111111111",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [240, 300],
      "webhookId": "abc123webhook"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "a2-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "22222222-2222-2222-2222-222222222222",
      "name": "Extract Fields",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [460, 300]
    },
    {
      "parameters": {
        "resource": "chat",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "value": "gpt-4o-mini",
          "mode": "list"
        },
        "messages": [
          {
            "role": "system",
            "content": "Eres un clasificador de mensajes. Tu única tarea es clasificar el mensaje del usuario en UNA de estas tres categorías exactas: 'soporte', 'ventas' u 'otro'. Reglas: - 'soporte': problemas técnicos, errores, bugs, ayuda con el producto, incidencias. - 'ventas': consultas de precios, planes, compras, cotizaciones, upgrades. - 'otro': todo lo que no encaje en las anteriores. Responde SOLO con la palabra de la categoría, sin comillas, sin explicaciones, sin puntos."
          },
          {
            "role": "user",
            "content": "={{ $json.message }}"
          }
        ],
        "simplifyOutput": true,
        "options": {}
      },
      "id": "33333333-3333-3333-3333-333333333333",
      "name": "Classify with AI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1,
      "position": [680, 300]
    },
    {
      "parameters": {
        "rules": {
          "values": [
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content }}",
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
                  "typeValidation": "loose"
                },
                "conditions": [
                  {
                    "leftValue": "={{ $json.message.content }}",
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
      "id": "44444444-4444-4444-4444-444444444444",
      "name": "Route by Category",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [900, 300]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#support",
        "text": "=📩 *Nuevo mensaje de SOPORTE*\n\n*De:* {{ $('Extract Fields').item.json.email }}\n*Mensaje:* {{ $('Extract Fields').item.json.message }}\n*Clasificación:* soporte",
        "otherOptions": {}
      },
      "id": "55555555-5555-5555-5555-555555555555",
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1180, 200],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#sales",
        "text": "=💰 *Nuevo mensaje de VENTAS*\n\n*De:* {{ $('Extract Fields').item.json.email }}\n*Mensaje:* {{ $('Extract Fields').item.json.message }}\n*Clasificación:* ventas",
        "otherOptions": {}
      },
      "id": "66666666-6666-6666-6666-666666666666",
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1180, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "post",
        "channel": "#general",
        "text": "=📌 *Nuevo mensaje GENERAL*\n\n*De:* {{ $('Extract Fields').item.json.email }}\n*Mensaje:* {{ $('Extract Fields').item.json.message }}\n*Clasificación:* otro",
        "otherOptions": {}
      },
      "id": "77777777-7777-7777-7777-777777777777",
      "name": "Slack - General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [1180, 400],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_CON_TU_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extract Fields",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extract Fields": {
      "main": [
        [
          {
            "node": "Classify with AI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Classify with AI": {
      "main": [
        [
          {
            "node": "Route by Category",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Route by Category": {
      "main": [
        [
          {
            "node": "Slack - Soporte",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - Ventas",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack - General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1",
    "saveExecutionProgress": true,
    "saveManualExecutions": true,
    "callerPolicy": "workflowsFromSameOwner"
  },
  "staticData": null,
  "tags": [
    {
      "name": "clasificación",
      "id": "tag1"
    },
    {
      "name": "slack",
      "id": "tag2"
    }
  ],
  "active": false,
  "versionId": "1"
}
```

---

## 🔧 Configuración Necesaria Antes de Importar

### 1️⃣ Credenciales OpenAI
Crea la credencial en N8N: **Credentials → New → OpenAI API** y obtén la API key en [platform.openai.com](https://platform.openai.com).

### 2️⃣ Credenciales Slack
- Ve a [api.slack.com/apps](https://api.slack.com/apps) → **Create New App**
- Añade el scope `chat:write` y `chat:write.public`
- Instala la app en tu workspace
- En N8N: **Credentials → New → Slack API** → pega el **Bot User OAuth Token** (empieza con `xoxb-...`)

### 3️⃣ Reemplazar el ID de credencial
Busca en el JSON `"REEMPLAZAR_CON_TU_CREDENCIAL_SLACK"` y reemplázalo con el ID de tu credencial Slack (lo ves en la URL de la credencial creada en N8N).

---

## 📋 Flujo del Workflow

```
POST /classify-message
        ↓
   [Webhook]
        ↓
   [Extract Fields]  → Extrae email y message del body
        ↓
   [Classify with AI]  → OpenAI clasifica en: soporte | ventas | otro
        ↓
   [Route by Category]  → Switch con 3 salidas
        ↓
   ┌────────────┬──────────────┬──────────────┐
   ↓            ↓              ↓
[Slack        [Slack          [Slack
 Soporte]      Ventas]         General]
 #support      #sales          #general
```

---

## 🧪 Ejemplo de prueba con cURL

```bash
curl -X POST http://localhost:5678/webhook/classify-message \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@ejemplo.com",
    "message": "Tengo un error al iniciar sesión en la plataforma"
  }'
```

**Respuesta esperada:** El mensaje se clasificará como `soporte` y se enviará a `#support`.