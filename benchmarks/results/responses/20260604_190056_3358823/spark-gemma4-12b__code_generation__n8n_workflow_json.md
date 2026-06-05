# Gemma 4 12B (Spark llama-server Q4_K_M) — code_generation/n8n_workflow_json

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 6.73 | quality: 7.48
- latency_total: 114.863s | tokens_per_second: 25.1
- input_tokens: 131 | output_tokens: 2886
- judge_score: 3.2 | justificación: 

## Respuesta completa

Para generar este workflow en n8n, he diseñado una estructura que utiliza un **Webhook**, un nodo de **OpenAI** (usando una cadena de chat simple para clasificación), un nodo **Switch** para la lógica de rutas y tres nodos de **Slack** para los destinos finales.

### Instrucciones para usar este JSON:
1. Copia el código JSON de abajo.
2. Abre tu instancia de n8n.
3. Crea un nuevo workflow.
4. Pega el código directamente en el lienzo (Ctrl+V o Cmd+V) o impórtalo desde el menú de "Import".
5. **Configuración necesaria:**
   - Debes configurar tus credenciales de **OpenAI** y **Slack**.
   - En el nodo de Slack, asegúrate de que el ID del canal sea correcto (ej: `C12345678`).
   - En el nodo de Webhook, usa la "Test URL" mientras pruebas y la "Production URL" cuando lo actives.

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "classify-message",
        "options": {}
      },
      "id": "1f7e8d3a-8b9c-4d2e-a1b2-c3d4e5f6g7h8",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [400, 400]
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "prompt": {
          "parameters": [
            {
              "role": "system",
              "content": "Eres un asistente que clasifica mensajes de clientes. Responde ÚNICAMENTE con una de estas tres palabras: \"soporte\", \"ventas\" o \"otro\". No añadas explicaciones ni puntos finales."
            },
            {
              "content": "Clasifica el siguiente mensaje: {{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0
        }
      },
      "id": "2a3b4c5d-6e7f-8g9h-0i1j-2k3l4m5n6o7p",
      "name": "OpenAI Classification",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [800, 400],
      "credentials": {
        "openAiApi": {
          "id": "TU_ID_DE_CREDENCIAL_OPENAI",
          "name": "OpenAI account"
        }
      }
    },
    {
      "parameters": {
        "rules": {
          "rules": [
            {
              "options": {
                "caseSensitive": false
              },
              "value1": "={{ $json.message.trim().toLowerCase() }}",
              "operation": "equal",
              "value2": "soporte"
            },
            {
              "options": {
                "caseSensitive": false
              },
              "value1": "={{ $json.message.trim().toLowerCase() }}",
              "operation": "equal",
              "value2": "ventas"
            },
            {
              "operation": "otherwise",
              "next_node": "otro"
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "3b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q",
      "name": "Switch Route",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 1,
      "position": [1050, 400]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=📩 *Nuevo Ticket de Soporte*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "4c5d6e7f-8g9h-0i1j-2k3l-4m5n6o7p8q9r",
      "name": "Slack Support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1400, 250],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💰 *Nuevo Lead de Ventas*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "5d6e7f8g-9h0i-1j2k-3l4m-5n6o7p8q9r0s",
      "name": "Slack Sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1400, 400],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
          "name": "Slack account"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=📝 *Otro Mensaje*\n*Email:* {{ $node[\"Webhook\"].json.body.email }}\n*Mensaje:* {{ $node[\"Webhook\"].json.body.message }}",
        "otherOptions": {}
      },
      "id": "6e7f8g9h-0i1j-2k3l-4m5n-6o7p8q9r0s1t",
      "name": "Slack General",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [1400, 550],
      "credentials": {
        "slackApi": {
          "id": "TU_ID_DE_CREDENCIAL_SLACK",
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
            "node": "OpenAI Classification",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI Classification": {
      "main": [
        [
          {
            "node": "Switch Route",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Switch Route": {
      "main": [
        [
          {
            "node": "Slack Support",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack Sales",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Slack General",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Explicación del flujo:

1.  **Webhook**: Escucha una petición POST. Espera un JSON como este:
    ```json
    {
      "email": "cliente@ejemplo.com",
      "message": "Mi producto llegó roto y necesito ayuda técnica."
    }
    ```
2.  **OpenAI Classification**: Toma el campo `message` y le pide a GPT-3.5 que lo clasifique. He configurado la "Temperatura" en 0 para que la respuesta sea determinista y solo devuelva la palabra clave.
3.  **Switch Route**: Evalúa el texto devuelto por la IA.
    - Si es "soporte" -> Ruta 1.
    - Si es "ventas" -> Ruta 2.
    - Cualquier otra cosa (o "otro") -> Ruta 3.
4.  **Slack Nodes**: Envía un mensaje formateado a los canales correspondientes, recuperando los datos originales del email y el mensaje mediante la referencia `$node["Webhook"]`.