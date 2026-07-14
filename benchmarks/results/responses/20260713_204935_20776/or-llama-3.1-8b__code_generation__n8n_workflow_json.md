# Llama 3.1 8B Instant — code_generation/n8n_workflow_json

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 5.62 | quality: 4.92
- latency_total: 12.824s | tokens_per_second: 73.5
- input_tokens: 125 | output_tokens: 942
- judge_score: 1.8 | justificación: 

## Respuesta completa

A continuación te muestro un ejemplo de cómo podría estructurarse el workflow en N8N:

```json
{
  "name": "Flujo de clasificación de mensajes",
  "nodes": [
    {
      "label": "Inicio",
      "type": "n8n-nodes-base.webhookTrigger",
      "parameters": {},
      "name": "Comenzar con webhook"
    },
    {
      "label": "Obtener campos email y message",
      "type": "n8n-nodes-base.json",
      "parameters": {
        "jsonPath": "$.body.email, $..body.message"
      },
      "name": "Obtener campos"
    },
    {
      "label": "Clasificar mensaje con OpenAI",
      "type": "n8n-nodes-base.openai",
      "parameters": {
        "apiUrl": "https://api.openai.com/v1/engines/your-engine-id/model/your-model-id",
        "apiKey": "your-api-key",
        "json": "{\"prompt\":\"{{$message}}\"}"
      },
      "name": "Clasificar mensaje"
    },
    {
      "label": "Enviar a soporte",
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "your-slack-channel-id",
        "message": "{\"text\":\"{{$message}}\"}"
      },
      "name": "Enviar a soporte"
    },
    {
      "label": "Enviar a ventas",
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "your-slack-channel-id",
        "message": "{\"text\":\"{{$message}}\"}"
      },
      "name": "Enviar a ventas"
    },
    {
      "label": "Enviar a general",
      "type": "n8n-nodes-base.slack",
      "parameters": {
        "channel": "your-slack-channel-id",
        "message": "{\"text\":\"{{$message}}\"}"
      },
      "name": "Enviar a general"
    }
  ],
  "connections": {
    "Comenzar con webhook": {
      "main": [
        {
          "node": "Obtener campos",
          "pipe": [
            {
              "operation": "get",
              "value": "1"
            }
          ]
        }
      ]
    },
    "Obtener campos": {
      "main": [
        {
          "node": "Clasificar mensaje",
          "pipe": [
            {
              "operation": "set",
              "value": "={{$message}}"
            }
          ]
        }
      ]
    },
    "Clasificar mensaje": {
      "main": [
        {
          "node": "Enviar a soporte",
          "pipe": [
            {
              "operation": "if",
              "value": "={{$message}} = \"soporte\""
            }
          ]
        },
        {
          "node": "Enviar a ventas",
          "pipe": [
            {
              "operation": "if",
              "value": "={{$message}} = \"ventas\""
            }
          ]
        },
        {
          "node": "Enviar a general",
          "pipe": [
            {
              "operation": "if",
              "value": "={{$message}} = \"otro\""
            }
          ]
        }
      ]
    },
    "Enviar a soporte": {
      "main": [
        {
          "node": "Enviar a soporte",
          "pipe": [
            {
              "operation": "set",
              "value": "={{$message}} = \"soporte\""
            }
          ]
        }
      ]
    },
    "Enviar a ventas": {
      "main": [
        {
          "node": "Enviar a ventas",
          "pipe": [
            {
              "operation": "set",
              "value": "={{$message}} = \"ventas\""
            }
          ]
        }
      ]
    },
    "Enviar a general": {
      "main": [
        {
          "node": "Enviar a general",
          "pipe": [
            {
              "operation": "set",
              "value": "={{$message}} = \"otro\""
            }
          ]
        }
      ]
    }
  }
}
```

Ten en cuenta que esta es solo una implementación posible y que es posible que debas adaptarla a tus necesidades específicas.