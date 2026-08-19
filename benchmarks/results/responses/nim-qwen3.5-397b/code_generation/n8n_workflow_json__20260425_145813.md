# Qwen 3.5 397B (NIM) — code_generation/n8n_workflow_json

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 6.42 | quality: 7.48
- latency_total: 90.27s | tokens_per_second: 22.7
- input_tokens: 120 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí tienes el código JSON completo para el workflow de n8n.

### Instrucciones previas a la importación:
1.  **Credenciales:** Este workflow asume que ya tienes configuradas las credenciales en tu instancia de n8n para:
    *   **OpenAI API** (Nombre por defecto en el nodo: `OpenAI account`)
    *   **Slack API** (Nombre por defecto en el nodo: `Slack account`)
2.  **Configuración de Slack:** El workflow intenta enviar mensajes a los canales `#support`, `#sales` y `#general`. Asegúrate de que el bot de Slack (la app que instalaste con las credenciales) tenga permiso para unirse y escribir en estos canales. Si tus canales tienen nombres diferentes, edita los nodos de Slack correspondientes después de importar.
3.  **Webhook:** Al importar, el nodo Webhook generará una URL única. Deberás usar esa URL para hacer la prueba POST.

### Código JSON del Workflow

Copia el siguiente bloque y guárdalo como un archivo `.json` o pégalo directamente en el lienzo de n8n (usando `Ctrl+V` o la opción "Import from File"):

```json
{
  "name": "Clasificador IA a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "options": {}
      },
      "id": "webhook-node",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1.1,
      "position": [
        250,
        300
      ],
      "webhookId": "unique-webhook-id-placeholder"
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-3.5-turbo"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un asistente que clasifica mensajes de clientes. Debes responder ÚNICAMENTE con una de estas tres palabras en minúscula: 'soporte', 'ventas' u 'otro'. No añadas explicaciones ni puntuación."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        },
        "options": {}
      },
      "id": "openai-node",
      "name": "OpenAI",
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        650,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "TU_CREDENCIAL_OPENAI_AQUI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "promptType": "define",
        "text": "={{ $json.message }}",
        "options": {}
      },
      "id": "chain-node",
      "name": "Chain",
      "type": "@n8n/n8n-nodes-langchain.chainLlm",
      "typeVersion": 1.4,
      "position": [
        450,
        300
      ]
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "category-id",
              "name": "category",
              "value": "={{ $json.output }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "set-category",
      "name": "Set Category",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.4,
      "position": [
        850,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "cond-soporte",
              "leftValue": "={{ $json.category }}",
              "rightValue": "soporte",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combineOperation": "and"
        },
        "options": {}
      },
      "id": "if-soporte",
      "name": "Es Soporte?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1050,
        300
      ]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "cond-ventas",
              "leftValue": "={{ $json.category }}",
              "rightValue": "ventas",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combineOperation": "and"
        },
        "options": {}
      },
      "id": "if-ventas",
      "name": "Es Ventas?",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2.2,
      "position": [
        1050,
        550
      ]
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#support",
        "text": "🔴 *Nuevo ticket de SOPORTE*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-soporte",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        200
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_AQUI",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#sales",
        "text": "💰 *Nuevo lead de VENTAS*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-ventas",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        450
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_AQUI",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "resource": "message",
        "operation": "send",
        "channel": "#general",
        "text": "ℹ️ *Mensaje GENERAL*\n\n*De:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack-general",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1250,
        700
      ],
      "credentials": {
        "slackApi": {
          "id": "TU_CREDENCIAL_SLACK_AQUI",
          "name": "Slack account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Chain",
            "type": "main",
            "index": 0
          }
        ]
      ]