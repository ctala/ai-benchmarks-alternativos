# Nemotron 3 Ultra 550B (NIM) — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 193.488s | tokens_per_second: 17.3
- input_tokens: 133 | output_tokens: 3338

## Respuesta completa

Aquí tienes el JSON completo del workflow de n8n.

**Notas importantes antes de importar:**
1.  **Credenciales:** Debes configurar tus credenciales de **OpenAI** y **Slack** en n8n y seleccionarlas en los nodos correspondientes (marcados como `YOUR_OPENAI_CREDENTIALS_ID` y `YOUR_SLACK_CREDENTIALS_ID`).
2.  **Canales de Slack:** El nodo de Slack requiere el **Channel ID** (ej: `C012AB3CD`), no el nombre (`#support`). He puesto placeholders (`SLACK_CHANNEL_ID_SUPPORT`, etc.) que debes reemplazar por los IDs reales. Puedes obtenerlos con el nodo "Slack > Channel > Get All" o clic derecho en Slack > "Copiar ID del canal".
3.  **Respuesta del Webhook:** El workflow responde `200 OK` inmediatamente al recibir la petición (modo `onReceived`) para no bloquear al emisor mientras se procesa la IA.

```json
{
  "name": "Clasificar Email y Enviar a Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-mensaje",
        "responseMode": "onReceived",
        "responseData": {
          "options": {}
        },
        "options": {}
      },
      "id": "1",
      "name": "Webhook Recibido",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        250,
        300
      ],
      "webhookId": "clasificar-mensaje-unico"
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "email",
              "value": "={{ $json.body.email }}",
              "type": "string"
            },
            {
              "id": "2",
              "name": "message",
              "value": "={{ $json.body.message }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "2",
      "name": "Extraer Campos",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [
        500,
        300
      ]
    },
    {
      "parameters": {
        "model": {
          "__rl": true,
          "mode": "list",
          "value": "gpt-4o-mini"
        },
        "options": {
          "temperature": 0,
          "responseFormat": "json_object"
        },
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador de mensajes. Analiza el mensaje del usuario y devuelve ÚNICAMENTE un objeto JSON válido con una clave 'categoria'. Los valores permitidos son EXACTAMENTE: 'soporte', 'ventas', 'otro'.\n\nCriterios:\n- 'soporte': Problemas técnicos, errores, bugs, ayuda con la plataforma, contraseñas, facturación técnica.\n- 'ventas': Consultas de precios, planes, demos, upgrades, nuevos contratos, negociación.\n- 'otro': Spam, saludos sin contexto, consultas irrelevantes, quejas generales sin acción clara."
            },
            {
              "role": "user",
              "content": "={{ $json.message }}"
            }
          ]
        }
      },
      "id": "3",
      "name": "Clasificar con OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.8,
      "position": [
        750,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIALS_ID",
          "name": "OpenAI Account"
        }
      }
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {
              "id": "1",
              "name": "categoria",
              "value": "={{ JSON.parse($json.choices[0].message.content).categoria }}",
              "type": "string"
            }
          ]
        },
        "options": {}
      },
      "id": "4",
      "name": "Parsear Categoría IA",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3.2,
      "position": [
        1000,
        300
      ]
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
                  "typeValidation": "strict"
                },
                "string": [
                  {
                    "value1": "={{ $json.categoria }}",
                    "operation": "equals",
                    "value2": "soporte"
                  }
                ]
              },
              "output": "soporte"
            },
            {
              "conditions": {
                "options": {
                  "caseSensitive": false,
                  "leftValue": "",
                  "typeValidation": "strict"
                },
                "string": [
                  {
                    "value1": "={{ $json.categoria }}",
                    "operation": "equals",
                    "value2": "ventas"
                  }
                ]
              },
              "output": "ventas"
            }
          ]
        },
        "options": {}
      },
      "id": "5",
      "name": "Switch: ¿Categoría?",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 2,
      "position": [
        1250,
        300
      ]
    },
    {
      "parameters": {
        "channel": "SLACK_CHANNEL_ID_SUPPORT",
        "text": "🆘 *Nuevo Ticket de SOPORTE*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.categoria }}",
        "options": {}
      },
      "id": "6",
      "name": "Slack: #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1500,
        100
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "SLACK_CHANNEL_ID_SALES",
        "text": "💰 *Nueva Oportunidad de VENTAS*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.categoria }}",
        "options": {}
      },
      "id": "7",
      "name": "Slack: #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1500,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack Account"
        }
      }
    },
    {
      "parameters": {
        "channel": "SLACK_CHANNEL_ID_GENERAL",
        "text": "📥 *Mensaje CLASIFICADO COMO 'OTRO'*\n*Email:* {{ $json.email }}\n*Mensaje:* {{ $json.message }}\n*Categoría IA:* {{ $json.categoria }}",
        "options": {}
      },
      "id": "8",
      "name": "Slack: #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.1,
      "position": [
        1500,
        500
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIALS_ID",
          "name": "Slack Account"
        }
      }
    }
  ],
  "connections": {
    "Webhook Recibido": {
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
            "node": "Parsear Categoría IA",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Parsear Categoría IA": {
      "main": [
        [
          {
            "node": "Switch: ¿Categoría?",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch: ¿Categoría?": {
      "main": [
        [
          {
            "node": "Slack: #support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: #sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack: #general",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "1.0",
  "meta": {
    "templateCredsSetupCompleted": true
  },
  "id": "1"
}
```

### Cómo importar y configurar:

1.  Copia el JSON anterior.
2.  En n8n, ve a **Workflows** → **Import** (arriba a la derecha) → Pega el JSON → **Import**.
3.  Abre el workflow.
4.  **Nodo "Clasificar con OpenAI"**: Haz clic → Credenciales → Selecciona tu credencial de OpenAI.
5.  **Nodos Slack (#support, #sales, #general)**: Haz clic en cada uno → Credenciales → Selecciona tu credencial de Slack.
6.  **Canales Slack**: En cada nodo Slack, cambia el campo `channel` (actualmente `SLACK_CHANNEL_ID_...`) por el **ID real del canal** (ej: `C05XXXXXX`).
    *   *Tip:* Si quieres usar el nombre (`#support`), asegúrate que el bot de Slack esté invitado al canal y a veces n8n resuelve el nombre, pero el **ID es 100% fiable**.
7.  Guarda y haz clic en **Execute Workflow** (para activar el webhook de prueba) o **Activate** (para producción).

### Ejemplo de Payload para probar (POST a `https://tu-dominio/webhook/clasificar-mensaje`):

```json
{
  "email": "cliente@ejemplo.com",
  "message": "Hola, mi factura del mes pasado tiene un error en el IVA, necesito que me la corrijan urgente."
}
```
*Debería clasificarse como **soporte** e ir a #support.*