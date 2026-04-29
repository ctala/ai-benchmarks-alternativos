# Nemotron Nano 9B v2 (NIM) — code_generation/n8n_workflow_json

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 7.11 | quality: 8.88
- latency_total: 28.035s | tokens_per_second: 61.3
- input_tokens: 129 | output_tokens: 1719
- judge_score: 4.2 | justificación: 

## Respuesta completa



Aquí tienes el workflow en formato JSON para N8N que cumple con tus requisitos:

```json
{
  "nodes": [
    {
      "type": "webhook",
      "id": "webhook-1",
      "name": "Webhook Incoming",
      "config": {
        "method": "POST"
      }
    },
    {
      "type": "function",
      "id": "extract-fields",
      "name": "Extract Fields",
      "config": {
        "code": "return {\n  email: $json.email,\n  message: $json.message\n};"
      }
    },
    {
      "type": "ai.openai",
      "id": "openai-classify",
      "name": "Classify with OpenAI",
      "config": {
        "apiKey": "YOUR_OPENAI_API_KEY",
        "model": "gpt-3.5-turbo",
        "prompt": "Classifica el siguiente mensaje en una de estas categorías: soporte, ventas, otro. Responde solo con la categoría. Mensaje: {{message}}"
      }
    },
    {
      "type": "switch",
      "id": "switch-category",
      "name": "Route to Slack",
      "config": {
        "conditions": [
          {
            "name": "soporte",
            "expression": "$json.category === 'soporte'"
          },
          {
            "name": "ventas",
            "expression": "$json.category === 'ventas'"
          },
          {
            "name": "other",
            "expression": "true"
          }
        ]
      }
    },
    {
      "type": "webhook",
      "id": "slack-support",
      "name": "Slack - Support",
      "config": {
        "url": "YOUR_SLACK_WEBHOOK_URL_FOR_SUPPORT",
        "method": "POST",
        "body": {
          "text": "New support request from {{email}}\n\n{{message}}"
        }
      }
    },
    {
      "type": "webhook",
      "id": "slack-sales",
      "name": "Slack - Sales",
      "config": {
        "url": "YOUR_SLACK_WEBHOOK_URL_FOR_SALES",
        "method": "POST",
        "body": {
          "text": "New sales inquiry from {{email}}\n\n{{message}}"
        }
      }
    },
    {
      "type": "webhook",
      "id": "slack-general",
      "name": "Slack - General",
      "config": {
        "url": "YOUR_SLACK_WEBHOOK_URL_FOR_GENERAL",
        "method": "POST",
        "body": {
          "text": "General message from {{email}}\n\n{{message}}"
        }
      }
    }
  ],
  "links": [
    {
      "from": "webhook-1",
      "to": "extract-fields"
    },
    {
      "from": "extract-fields",
      "to": "openai-classify"
    },
    {
      "from": "openai-classify",
      "to": "switch-category"
    },
    {
      "from": "switch-category:soporte",
      "to": "slack-support"
    },
    {
      "from": "switch-category:ventas",
      "to": "slack-sales"
    },
    {
      "from": "switch-category:other",
      "to": "slack-general"
    }
  ]
}
```

### Explicación de los componentes:

1. **Webhook Incoming**:
   - Escucha solicitudes POST
   - El body debe contener campos `email` y `message`

2. **Extract Fields**:
   - Extrae los campos `email` y `message` del JSON entrante

3. **Classify with OpenAI**:
   - Usa el modelo GPT-3.5 para clasificar el mensaje
   - El prompt está ajustado para responder solo con la categoría

4. **Switch Node**:
   - Enruta a diferentes canales de Slack según la clasificación

5. **Slack Webhooks**:
   - Tres nodos separados para cada canal (#support, #sales, #general)
   - Cada uno necesita su propia URL de webhook de Slack

### Configuración requerida:
- Reemplaza `YOUR_OPENAI_API_KEY` con tu clave real de OpenAI
- Reemplaza las URLs de Slack Webhook (`YOUR_SLACK_WEBHOOK_URL_FOR_...`) con tus URLs reales

### Notas:
- El formato de mensaje en Slack incluye el email y el mensaje original para contexto
- Asegúrate de tener instalados los nodos necesarios en tu instancia de N8N:
  - `webhook`
  - `function` (para extraer campos)
  - `ai.openai`
  - `switch`

¿Quieres que agregue algún manejo de errores o validación adicional?
