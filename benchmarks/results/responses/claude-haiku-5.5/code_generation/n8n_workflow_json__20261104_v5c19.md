# Claude Haiku 5.5 — code_generation/n8n_workflow_json

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.81 | quality: 8.6
- latency_total: 24.664s | tokens_per_second: 272.7
- input_tokens: 177 | output_tokens: 6726
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cubriendo los requisitos del workflow de N8N con un enfoque claro en la clasificación de mensajes y la integración con Slack. Aunque la profundidad es adecuada, podría haberse beneficiado de más detalles sobre la configuración de credenciales o manejo de errores. La claridad y utilidad práctica son altas, lo que permite a un emprendedor implementar el workflow con facilidad.

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

Aquí tienes el workflow completo. Puedes copiarlo y pegarlo directamente en n8n con **Ctrl+V** sobre el lienzo.

```json
{
  "name": "Clasificador de mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "responseCode": 200,
        "options": {}
      },
      "id": "a1b2c3d4-0001-4000-8000-000000000001",
      "name": "Webhook POST",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [0, 300],
      "webhookId": "a1b2c3d4-0001-4000-8000-000000000101"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "a1b2c3d4-0002-4000-8000-000000000001",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "a1b2c3d4-0002-4000-8000-000000000002",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0002-4000-8000-000000000003",
      "name": "Extraer campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [220, 300]
    },
    {
      "parameters": {
        "resource": "text",
        "operation": "message",
        "modelId": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Clasifica el mensaje del usuario en UNA de estas categorías: soporte (problemas técnicos, errores, ayuda con el producto), ventas (precios, compras, demos, planes, cotizaciones) u otro (cualquier otro caso). Responde ÚNICAMENTE con una de estas palabras exactas: soporte, ventas, otro. No añadas nada más."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "a1b2c3d4-0003-4000-8000-000000000001",
      "name": "OpenAI Clasificar",
      "type": "@n8n/n8n-nodes-langchain.openAi",
      "typeVersion": 1.8,
      "position": [440, 300],
      "credentials": {
        "openAiApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "jsCode": "const respuesta = String(\n  $input.first().json.message?.content ??\n  $input.first().json.content ??\n  $input.first().json.text ??\n  ''\n).toLowerCase().trim();\n\nlet categoria = 'otro';\nif (respuesta === 'soporte' || respuesta.includes('soporte')) {\n  categoria = 'soporte';\n} else if (respuesta === 'ventas' || respuesta.includes('ventas')) {\n  categoria = 'ventas';\n}\n\nconst base = $('Extraer campos').first().json;\n\nreturn [{\n  json: {\n    email: base.email,\n    message: base.message,\n    categoria\n  }\n}];"
      },
      "id": "a1b2c3d4-0004-4000-8000-000000000001",
      "name": "Normalizar categoría",
      "type": "n8n-nodes-base.code",
      "typeVersion": 2,
      "position": [660, 300]
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
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "a1b2c3d4-0005-4000-8000-000000000011",
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
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "a1b2c3d4-0005-4000-8000-000000000021",
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
                  "typeValidation": "strict"
                },
                "conditions": [
                  {
                    "id": "a1b2c3d4-0005-4000-8000-000000000031",
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
        "options": {}
      },
      "id": "a1b2c3d4-0005-4000-8000-000000000001",
      "name": "Switch por categoría",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [880, 300]
    },
    {
      "parameters": {
        "authentication": "accessToken",
        "resource": "message",
        "operation": "post",
        "select": "channel",
        "channelId": {
          "__rl": true,
          "mode": "name",
          "value": "#support"
        },
        "text": "=📩 *Nuevo mensaje de soporte*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000001",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 120],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
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
          "mode": "name",
          "value": "#sales"
        },
        "text": "=💰 *Nuevo mensaje de ventas*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000002",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 300],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
          "name": "Slack account"
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
          "mode": "name",
          "value": "#general"
        },
        "text": "=💬 *Nuevo mensaje general*\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "a1b2c3d4-0006-4000-8000-000000000003",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [1120, 480],
      "credentials": {
        "slackApi": {
          "id": "REEMPLAZAR_ID_CREDENCIAL_SLACK",
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
            "node": "Extraer campos",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Extraer campos": {
      "main": [
        [
          {
            "node": "OpenAI Clasificar",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Clasificar": {
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
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
  "triggerCount": 0,
  "versionId": "1"
}
```

## Cómo usarlo

1. **Importa el JSON** en n8n (Ctrl+V sobre el lienzo, o *Workflow → Import from file*).
2. **Configura las credenciales:**
   - **OpenAI Clasificar:** crea una credencial de tipo *OpenAI API* con tu API key y asígnala.
   - **Slack (los tres nodos):** crea una credencial de tipo *Slack API* (token de un bot con permisos `chat:write`) y asígnala. Los nodos usan `authentication: accessToken`; si tu versión de n8n usa OAuth2, cambia el tipo de credencial en el nodo.
   - Los campos `REEMPLAZAR_ID_CREDENCIAL_...` se reemplazan automáticamente al seleccionar la credencial en la UI.
3. **Asegúrate de que el bot de Slack esté en los canales** `#support`, `#sales` y `#general`, ya que de lo contrario no podrá publicar (`/invite @nombre_del_bot`).
4. **Activa el workflow** (interruptor *Active* arriba a la derecha). La URL de producción del webhook será algo como `https://tu-n8n/webhook/clasificar-mensaje`.

## Prueba

```bash
curl -X POST https://tu-n8n/webhook/clasificar-mensaje \
  -H "Content-Type: application/json" \
  -d '{"email": "cliente@ejemplo.com", "message": "Hola, la aplicación se cierra cada vez que intento iniciar sesión."}'
```

Este mensaje debería clasificarse como **soporte** y publicarse en `#support`.

## Notas

- **Estructura del flujo:** Webhook → Extraer campos (Set) → OpenAI → Normalizar categoría (Code) → Switch → Slack (uno de tres).
- **Normalización:** el nodo Code limpia la respuesta de la IA y, si no reconoce la categoría, la envía a `otro`, de modo que siempre se publica en algún canal.
- **Versiones de nodos:** los `typeVersion` corresponden a n8n 1.x recientes. Si al importar aparece un aviso de versión, puedes ajustar el número en el nodo o actualizar n8n.
- **Respuesta del webhook:** está configurada como `onReceived`, de modo que el emisor recibe un `200` inmediatamente, sin esperar a que OpenAI y Slack terminen.