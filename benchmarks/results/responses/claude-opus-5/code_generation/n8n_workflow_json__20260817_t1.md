# Claude Opus 5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.02 | quality: 7.2
- latency_total: 81.491s | tokens_per_second: 100.5
- input_tokens: 175 | output_tokens: 8192
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

# Workflow N8N: Clasificador de mensajes con IA → Slack

## JSON completo (listo para importar)

```json
{
  "name": "Clasificador de mensajes IA -> Slack",
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
      "position": [-220, 300],
      "webhookId": "a1b2c3d4-0001-4000-8000-000000000001"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "asg-email",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "asg-message",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            },
            {
              "id": "asg-fecha",
              "name": "recibidoEn",
              "value": "={{ $now.toISO() }}",
              "type": "string"
            }
          ]
        },
        "includeOtherFields": false,
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000002",
      "name": "Extraer datos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [0, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "loose",
            "version": 2
          },
          "conditions": [
            {
              "id": "val-email",
              "leftValue": "={{ $json.email }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            },
            {
              "id": "val-message",
              "leftValue": "={{ $json.message }}",
              "rightValue": "",
              "operator": {
                "type": "string",
                "operation": "notEmpty",
                "singleValue": true
              }
            }
          ],
          "combinator": "and"
        },
        "looseTypeValidation": true,
        "options": {}
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000003",
      "name": "Payload valido?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [220, 300]
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
              "content": "Eres un clasificador de mensajes entrantes de clientes.\n\nClasifica el mensaje del usuario en EXACTAMENTE una de estas categorias:\n- \"soporte\": problemas tecnicos, errores, bugs, la cuenta no funciona, ayuda con el producto ya comprado, reclamos de servicio.\n- \"ventas\": precios, planes, cotizaciones, demos, facturacion previa a la compra, intencion de comprar o ampliar contrato.\n- \"otro\": todo lo demas (saludos, spam, postulaciones de empleo, prensa, mensajes sin sentido).\n\nResponde UNICAMENTE con un objeto JSON valido con esta forma:\n{\"categoria\": \"soporte|ventas|otro\", \"confianza\": 0.0-1.0, \"motivo\": \"explicacion breve en espanol\"}\n\nNo agregues texto adicional ni bloques de codigo.",
              "role": "system"
            },
            {
              "content": "=Mensaje del cliente (email: {{ $json.email }}):\n\"\"\"\n{{ $json.message }}\n\"\"\"",
              "role": "user"
            }
          ]
        },
        "jsonOutput": true,
        "simplify": true,
        "options": {
          "temperature": 0
        }
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000004",
      "name": "Clasificar con OpenAI",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [460, 200],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_OPENAI",
          "name": "OpenAi account"
        }
      },
      "onError": "continueRegularOutput",
      "retryOnFail": true,
      "maxTries": 2
    },
    {
      "parameters": {
        "jsCode": "// Normaliza la salida del modelo y la une con los datos originales\nconst out = [];\n\nfor (let i = 0; i < $input.all().length; i++) {\n  const item = $input.all()[i];\n\n  // La respuesta puede venir como objeto (jsonOutput) o como string\n  let raw =\n    item.json?.message?.content ??\n    item.json?.content ??\n    item.json?.text ??\n    item.json ??\n    '';\n\n  let parsed;\n  if (raw && typeof raw === 'object') {\n    parsed = raw;\n  } else {\n    try {\n      parsed = JSON.parse(\n        String(raw).replace(/```json/gi, '').replace(/```/g, '').trim()\n      );\n    } catch (e) {\n      parsed = { categoria: 'otro', confianza: 0, motivo: 'No se pudo parsear la respuesta del modelo' };\n    }\n  }\n\n  const permitidas = ['soporte', 'ventas', 'otro'];\n  let categoria = String(parsed.categoria ?? 'otro').toLowerCase().trim();\n  if (!permitidas.includes(categoria)) categoria = 'otro';\n\n  // Datos originales del webhook\n  const origen = $('Extraer datos').all()[i]?.json ?? $('Extraer datos').first().json;\n\n  out.push({\n    json: {\n      email: origen.email,\n      message: origen.message,\n      recibidoEn: origen.recibidoEn,\n      categoria,\n      confianza: typeof parsed.confianza === 'number' ? parsed.confianza : null,\n      motivo: parsed.motivo ?? null\n    }\n  });\n}\n\nreturn out;"
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000005",
      "name": "Normalizar clasificacion",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [680, 200]
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "sw-soporte",
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
                  "typeValidation": "loose",
                  "version": 2
                },
                "conditions": [
                  {
                    "id": "sw-ventas",
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
        "looseTypeValidation": true,
        "options": {
          "fallbackOutput": "extra",
          "renameFallbackOutput": "otro"
        }
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000006",
      "name": "Enrutar por categoria",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3.2,
      "position": [900, 200]
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#support",
          "mode": "name"
        },
        "text": "=:sos: *Nuevo ticket de SOPORTE*\n*Email:* {{ $json.email }}\n*Recibido:* {{ $json.recibidoEn }}\n*Confianza IA:* {{ $json.confianza }}\n*Motivo IA:* {{ $json.motivo }}\n\n*Mensaje:*\n>>> {{ $json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false,
          "mrkdwn": true
        }
      },
      "id": "a1b2c3d4-0007-4000-8000-000000000007",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1160, 20],
      "credentials": {
        "slackOAuth2Api": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#sales",
          "mode": "name"
        },
        "text": "=:moneybag: *Nuevo lead de VENTAS*\n*Email:* {{ $json.email }}\n*Recibido:* {{ $json.recibidoEn }}\n*Confianza IA:* {{ $json.confianza }}\n*Motivo IA:* {{ $json.motivo }}\n\n*Mensaje:*\n>>> {{ $json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false,
          "mrkdwn": true
        }
      },
      "id": "a1b2c3d4-0008-4000-8000-000000000008",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1160, 200],
      "credentials": {
        "slackOAuth2Api": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "authentication": "oAuth2",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "value": "#general",
          "mode": "name"
        },
        "text": "=:inbox_tray: *Nuevo mensaje SIN CLASIFICAR (otro)*\n*Email:* {{ $json.email }}\n*Recibido:* {{ $json.recibidoEn }}\n*Confianza IA:* {{ $json.confianza }}\n*Motivo IA:* {{ $json.motivo }}\n\n*Mensaje:*\n>>> {{ $json.message }}",
        "otherOptions": {
          "includeLinkToWorkflow": false,
          "mrkdwn": true
        }
      },
      "id": "a1b2c3d4-0009-4000-8000-000000000009",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.3,
      "position": [1160, 380],
      "credentials": {
        "slackOAuth2Api": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "errorMessage": "=Payload invalido: se requieren los campos 'email' y 'message' en el body."
      },
      "id": "a1b2c3d4-0010-4000-8000-000000000010",
      "name": "Error payload invalido",
      "type": "n8n-nodes-base.stopAndError",
      "typeVersion": 1,
      "position": [460, 420]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Extraer datos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer datos": {
      "main": [
        [
          {
            "node": "Payload valido?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Payload valido?": {
      "main": [
        [
          {
            "node": "Clasificar con OpenAI",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Error payload invalido",
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
            "node": "Normalizar clasificacion",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalizar clasificacion": {
      "main": [
        [
          {
            "node": "Enrutar por categoria",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Enrutar por categoria": {
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
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "pinData": {},
  "tags": [],
  "active": false,
  "versionId": "1"
}
```

---

## Cómo usarlo

**1. Importar:** en n8n → menú `···` → *Import from Clipboard* → pega el JSON.

**2. Configurar credenciales** (reemplaza los IDs placeholder haciendo clic en cada nodo y seleccionando tu credencial):
- `Clasificar con OpenAI` → credencial **OpenAI API**
- Los 3 nodos de Slack → credencial **Slack OAuth2** (o cambia `authentication` a `accessToken` y usa `slackApi`)

**3. Permisos de Slack** necesarios en tu app: `chat:write` y `chat:write.public` (este último para postear en canales donde el bot no fue invitado). Si no, invita el bot con `/invite @tu-bot` en `#support`, `#sales` y `#general`.

**4. Activar** el workflow y copiar la URL de producción del webhook.

## Probar

```bash
curl -X POST https://tu-n8n.com/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{
    