# Llama 3.1 8B Instant — code_generation/n8n_workflow_json

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 6.38 | quality: 5.68
- latency_total: 5.002s | tokens_per_second: 145.3
- input_tokens: 126 | output_tokens: 727
- judge_score: 2.2 | justificación: 

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

Aquí te dejo un ejemplo de un workflow de N8N en JSON que cumple con tus requisitos:
```json
{
  "nodes": [
    {
      "parameters": {
        "http": {
          "method": "POST",
          "url": "https://example.com/webhook",
          "body": "{\"email\":\"${body.email}\",\"message\":\"${body.message}\"}",
          "options": {}
        },
        "headers": {
          "Authorization": "Bearer ${n8n_credentials.oauthAccessToken}"
        }
      },
      "name": "Activar con webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [
        50,
        100
      ]
    },
    {
      "parameters": {
        "ai": {
          "model": "text-classification",
          "prompt": "${body.message}",
          "options": {
            "maxTokens": 2048
          }
        }
      },
      "name": "Clasificar mensaje",
      "type": "n8n-nodes-base.ai",
      "typeVersion": 1,
      "position": [
        200,
        100
      ]
    },
    {
      "parameters": {
        "slack": {
          "channel": "{{$json['classification'] == 'soporte' ? '#support' : ($json['classification'] == 'ventas' ? '#sales' : '#general')}}",
          "text": "Nuevo mensaje de ${body.email}: ${body.message}",
          "emoji": ":email:"
        }
      },
      "name": "Enviar a Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [
        350,
        100
      ]
    }
  ],
  "connections": {
    "Activar con webhook": {
      "main": [
        {
          "node": "Clasificar mensaje",
          "type": "main",
          "index": 0
        }
      ]
    },
    "Clasificar mensaje": {
      "main": [
        {
          "node": "Enviar a Slack",
          "type": "main",
          "index": 0
        }
      ]
    }
  }
}
```
Explicación:

1. El primer nodo es un webhook que se activa con un POST a la URL especificada en la propiedad `url`. El cuerpo del mensaje se envía como JSON con los campos `email` y `message`.
2. El segundo nodo es un nodo de IA (OpenAI) que utiliza el modelo de clasificación de texto para clasificar el mensaje como "soporte", "ventas" o "otro".
3. El tercer nodo es un nodo Slack que envía un mensaje al canal de Slack correspondiente según la clasificación del mensaje.

Notas:

* Debes reemplazar `https://example.com/webhook` con la URL real de tu webhook.
* Debes configurar las credenciales de OAuth para el nodo de webhook.
* Debes configurar las credenciales de Slack para el nodo de Slack.
* El nodo de IA (OpenAI) requiere que estés registrado y tengas una clave de API para utilizar el modelo de clasificación de texto.
* El nodo de Slack requiere que tengas un canal de Slack configurado con los nombres `#support`, `#sales` y `#general`.