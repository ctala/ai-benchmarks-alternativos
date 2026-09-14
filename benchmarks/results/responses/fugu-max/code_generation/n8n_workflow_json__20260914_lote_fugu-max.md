# Fugu Max — code_generation/n8n_workflow_json

- model_id: `sakana/fugu-max`
- success: True  | final: 7.47 | quality: 8.6
- latency_total: 20.549s | tokens_per_second: 154.4
- input_tokens: 194 | output_tokens: 3173
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON completo para un workflow de n8n que cumple con los requisitos especificados. La estructura es clara y organizada, facilitando su implementación. Aunque la profundidad es adecuada, podría haber incluido más detalles sobre la configuración de credenciales o manejo de errores.

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

Aquí tienes el JSON completo del workflow de n8n listo para importar. 

### Cómo importarlo:
1. Copia todo el bloque JSON que aparece abajo.
2. En tu panel de n8n, abre un nuevo workflow o uno existente.
3. Presiona `Ctrl + V` (o `Cmd + V` en Mac), o ve al menú de tres puntos arriba a la derecha y selecciona **"Import from Clipboard"**.
4. Solo necesitarás asignar tus credenciales de **OpenAI** y **Slack** en los nodos correspondientes.

```json
{
  "name": "Clasificación de Mensajes con OpenAI y Slack",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "incoming-message",
        "responseMode": "onReceived",
        "responseData": "allEntries",
        "options": {}
      },
      "id": "1e11400a-4228-4ce6-a67b-1fa2207b6401",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [
        260,
        340
      ]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-4o-mini",
        "messages": {
          "values": [
            {
              "role": "system",
              "content": "Eres un clasificador estricto de mensajes de clientes. Debes clasificar el mensaje del usuario únicamente en una de las siguientes tres categorías: 'soporte', 'ventas' u 'otro'. Responde exclusivamente con la palabra de la categoría elegida, todo en minúsculas y sin ningún signo de puntuación ni texto adicional."
            },
            {
              "role": "user",
              "content": "={{ $json.body.message }}"
            }
          ]
        },
        "options": {
          "temperature": 0.1
        }
      },
      "id": "e0b969e2-2a5b-4375-9c98-1e428bc3a5e1",
      "name": "Clasificar Mensaje (OpenAI)",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1.4,
      "position": [
        480,
        340
      ]
    },
    {
      "parameters": {
        "dataType": "string",
        "value1": "={{ $json.message.content.trim().toLowerCase() }}",
        "rules": {
          "rules": [
            {
              "value2": "soporte"
            },
            {
              "value2": "ventas",
              "output": 1
            }
          ]
        },
        "fallbackOutput": 2
      },
      "id": "4da65b74-325b-4bfe-a9c6-1f7c32bf8ff1",
      "name": "Ruta por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": 3,
      "position": [
        700,
        340
      ]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=🚨 *Nuevo ticket de Soporte*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "bfa24314-e53f-4221-a169-8e4cae752be3",
      "name": "Slack #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        940,
        180
      ]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=💼 *Nuevo contacto de Ventas*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "1bc699cf-d69c-4dc4-bd86-c39f0412e840",
      "name": "Slack #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        940,
        340
      ]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=💬 *Nuevo mensaje General*\n*De:* {{ $('Webhook').item.json.body.email }}\n*Mensaje:* {{ $('Webhook').item.json.body.message }}",
        "otherOptions": {}
      },
      "id": "2bc84310-85f2-4529-873b-eb8fa0a943a5",
      "name": "Slack #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2.2,
      "position": [
        940,
        500
      ]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje (OpenAI)",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Clasificar Mensaje (OpenAI)": {
      "main": [
        [
          {
            "node": "Ruta por Clasificación",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Ruta por Clasificación": {
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
  }
}
```

### Formato esperado en el POST:
El webhook espera una solicitud con cuerpo en formato JSON como este:
```json
{
  "email": "usuario@ejemplo.com",
  "message": "Hola, tengo problemas para iniciar sesión en mi cuenta."
}
```