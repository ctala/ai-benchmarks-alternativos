# Gemini 2.5 Pro — code_generation/n8n_workflow_json

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 7.3 | quality: 8.6
- latency_total: 40.648s | tokens_per_second: 113.7
- input_tokens: 115 | output_tokens: 4623
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, proporcionando un JSON bien estructurado que cumple con los requisitos especificados. Ofrece claridad y utilidad práctica, aunque carece de profundidad adicional más allá de la implementación básica.

## Respuesta completa

¡Claro! Aquí tienes el JSON completo para un workflow de N8N que cumple con todos los requisitos que has descrito.

### Cómo usar este JSON:

1.  Copia todo el contenido del bloque de código JSON.
2.  En tu instancia de N8N, ve a la vista de workflows.
3.  Haz clic en `New` para crear un nuevo workflow.
4.  En lugar de añadir nodos manualmente, haz clic en cualquier parte del canvas en blanco y presiona `Ctrl + V` (o `Cmd + V` en Mac) para pegar el código.
5.  N8N importará y construirá el workflow visualmente.

### Puntos importantes a configurar:

*   **Credenciales de OpenAI:** Selecciona tu credencial de OpenAI en el nodo "Clasificar Mensaje (OpenAI)". Si no tienes una, deberás crearla.
*   **Credenciales de Slack:** Selecciona tu credencial de Slack en los tres nodos de "Enviar a Slack". Si no tienes una, deberás crearla.
*   **Activar el Workflow:** Guarda y activa el workflow (usando el interruptor en la esquina superior derecha). Al activarlo, N8N te dará la URL de producción del webhook que deberás usar.

---

### JSON del Workflow de N8N

```json
{
  "name": "Clasificador de Emails con IA y Slack",
  "nodes": [
    {
      "parameters": {},
      "id": "2700e7ff-4348-433b-8533-3118939a3f29",
      "name": "Start",
      "type": "n8n-nodes-base.start",
      "typeVersion": "1",
      "position": [
        250,
        300
      ]
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "clasificar-email",
        "options": {}
      },
      "id": "e93540d9-b003-4f90-843e-324c56fd82c0",
      "name": "Webhook Trigger",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": "1",
      "position": [
        440,
        300
      ],
      "webhookId": "038167f9-6799-4d37-af5e-ad8da1e2d42d",
      "notes": "Se activa cuando recibe una petición POST con los campos 'email' y 'message'."
    },
    {
      "parameters": {
        "model": "gpt-3.5-turbo",
        "messages": [
          {
            "role": "system",
            "content": "Eres un experto clasificador de texto. Tu única tarea es clasificar el mensaje del usuario en una de estas tres categorías: 'soporte', 'ventas', u 'otro'.\n\nResponde únicamente con el nombre de la categoría en minúsculas y nada más."
          },
          {
            "role": "user",
            "content": "={{ $json.body.message }}"
          }
        ],
        "options": {}
      },
      "id": "3be55c0a-0498-469b-813d-5197828c460a",
      "name": "Clasificar Mensaje (OpenAI)",
      "type": "n8n-nodes-base.openAiChat",
      "typeVersion": "1",
      "position": [
        660,
        300
      ],
      "credentials": {
        "openAiApi": {
          "id": "YOUR_OPENAI_CREDENTIAL_ID",
          "name": "YOUR_OPENAI_CREDENTIAL_NAME"
        }
      },
      "notes": "Usa OpenAI para analizar el mensaje y devolver 'soporte', 'ventas' u 'otro'."
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": false,
            "type": "string"
          },
          "rules": [
            {
              "value1": "={{ $json.choices[0].message.content }}",
              "operation": "contains",
              "value2": "soporte"
            },
            {
              "value1": "={{ $json.choices[0].message.content }}",
              "operation": "contains",
              "value2": "ventas"
            }
          ]
        }
      },
      "id": "5f9a74aa-a82f-4a0b-93ff-1834ace74a58",
      "name": "Dirigir por Clasificación",
      "type": "n8n-nodes-base.switch",
      "typeVersion": "1",
      "position": [
        880,
        300
      ],
      "notes": "Dirige el flujo según la clasificación de la IA.\n\nSalida 0 -> soporte\nSalida 1 -> ventas\nSalida 2 (Default) -> otro"
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "=Nuevo mensaje de Soporte:\n\n*Email:* `{{ $('Webhook Trigger').item.json.body.email }}`\n\n*Mensaje:*\n```{{ $('Webhook Trigger').item.json.body.message }}```",
        "otherOptions": {
          "icon_emoji": ":headphone:"
        }
      },
      "id": "766a5676-e41b-4f9e-9533-3d4411132c1c",
      "name": "Enviar a #support",
      "type": "n8n-nodes-base.slack",
      "typeVersion": "1",
      "position": [
        1100,
        140
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "YOUR_SLACK_CREDENTIAL_NAME"
        }
      }
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "=Nuevo mensaje de Ventas:\n\n*Email:* `{{ $('Webhook Trigger').item.json.body.email }}`\n\n*Mensaje:*\n```{{ $('Webhook Trigger').item.json.body.message }}```",
        "otherOptions": {
          "icon_emoji": ":moneybag:"
        }
      },
      "id": "c6206140-5232-4414-8700-1c3132e09849",
      "name": "Enviar a #sales",
      "type": "n8n-nodes-base.slack",
      "typeVersion": "1",
      "position": [
        1100,
        300
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "YOUR_SLACK_CREDENTIAL_NAME"
        }
      }
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "=Nuevo mensaje (General):\n\n*Email:* `{{ $('Webhook Trigger').item.json.body.email }}`\n\n*Mensaje:*\n```{{ $('Webhook Trigger').item.json.body.message }}```",
        "otherOptions": {
          "icon_emoji": ":envelope_with_arrow:"
        }
      },
      "id": "1141364d-7a54-4340-9759-b94fcf13861c",
      "name": "Enviar a #general",
      "type": "n8n-nodes-base.slack",
      "typeVersion": "1",
      "position": [
        1100,
        460
      ],
      "credentials": {
        "slackApi": {
          "id": "YOUR_SLACK_CREDENTIAL_ID",
          "name": "YOUR_SLACK_CREDENTIAL_NAME"
        }
      }
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [
        [
          {
            "node": "Clasificar Mensaje (OpenAI)",
            "type": "main"
          }
        ]
      ]
    },
    "Clasificar Mensaje (OpenAI)": {
      "main": [
        [
          {
            "node": "Dirigir por Clasificación",
            "type": "main"
          }
        ]
      ]
    },
    "Dirigir por Clasificación": {
      "main": [
        [
          {
            "node": "Enviar a #support",
            "type": "main"
          }
        ],
        [
          {
            "node": "Enviar a #sales",
            "type": "main"
          }
        ],
        [
          {
            "node": "Enviar a #general",
            "type": "main"
          }
        ]
      ]
    }
  }
}
```

---

### Cómo probar el Webhook

Una vez que actives el workflow y obtengas la URL de producción, puedes probarlo con una herramienta como `curl` desde tu terminal.

Reemplaza `YOUR_N8N_WEBHOOK_URL` con la URL que te proporcionó N8N.

**Ejemplo para "Soporte":**

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
  "email": "cliente.problemas@email.com",
  "message": "Hola, mi cuenta se ha bloqueado y no puedo acceder. ¿Me pueden ayudar a resetear mi contraseña?"
}' \
YOUR_N8N_WEBHOOK_URL
```

**Ejemplo para "Ventas":**

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
  "email": "interesado.prospecto@email.com",
  "message": "Buenos días, me gustaría saber el precio del plan enterprise y si ofrecen algún tipo de descuento por volumen."
}' \
YOUR_N8N_WEBHOOK_URL
```

**Ejemplo para "Otro":**

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
  "email": "curioso@email.com",
  "message": "Hola, solo quería decirles que su aplicación es fantástica. ¡Sigan con el buen trabajo!"
}' \
YOUR_N8N_WEBHOOK_URL
```

Cada uno de estos comandos debería enviar el mensaje al canal de Slack correspondiente.