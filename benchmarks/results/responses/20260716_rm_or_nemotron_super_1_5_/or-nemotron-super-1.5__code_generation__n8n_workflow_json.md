# Nemotron Super 49B v1.5 — code_generation/n8n_workflow_json

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 7.81 | quality: 8.4
- latency_total: 32.81s | tokens_per_second: 52.8
- input_tokens: 134 | output_tokens: 1731
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del workflow de N8N, aunque la profundidad es moderada ya que sigue un enfoque directo sin insights adicionales.

## Respuesta completa

Aquí tienes el workflow completo en formato JSON para N8N que cumple con tus requisitos:

```json
{
  "nodes": [
    {
      "parameters": {},
      "name": "Webhook",
      "type": "n8n-nodes-base.Webhook",
      "typeVersion": 1,
      "position": [300, 100]
    },
    {
      "parameters": {
        "values": [
          {
            "name": "email",
            "value": "={{ $body.email }}",
            "type": "string"
          },
          {
            "name": "message",
            "value": "={{ $body.message }}",
            "type": "string"
          }
        ]
      },
      "name": "Extract Fields",
      "type": "n8n-nodes-base.Set",
      "typeVersion": 1,
      "position": [500, 100]
    },
    {
      "parameters": {
        "model": "text-davinci-003",
        "prompt": "Clasifica el siguiente mensaje en una de las siguientes categorías: 'soporte', 'ventas' o 'otro'.\n\nMensaje:\n{{ message }}\n\nCategoría:",
        "outputVariableName": "category"
      },
      "name": "Classify Message",
      "type": "n8n-nodes-base.OpenAI",
      "typeVersion": 1,
      "position": [700, 100]
    },
    {
      "parameters": {
        "cases": [
          {
            "name": "soporte",
            "value": "={{ ${{ node: 'Classify Message' }}.data.category }}",
            "type": "string"
          },
          {
            "name": "ventas",
            "value": "={{ ${{ node: 'Classify Message' }}.data.category }}",
            "type": "string"
          },
          {
            "name": "otro",
            "value": "={{ ${{ node: 'Classify Message' }}.data.category }}",
            "type": "string"
          }
        ]
      },
      "name": "Route by Category",
      "type": "n8n-nodes-base.Switch",
      "typeVersion": 1,
      "position": [900, 100]
    },
    {
      "parameters": {
        "channel": "#support",
        "text": "Correo: {{ email }}\nMensaje: {{ message }}"
      },
      "name": "Slack - Soporte",
      "type": "n8n-nodes-base.Slack",
      "typeVersion": 1,
      "position": [1100, 50]
    },
    {
      "parameters": {
        "channel": "#sales",
        "text": "Email: {{ email }}\nMessage: {{ message }}"
      },
      "name": "Slack - Ventas",
      "type": "n8n-nodes-base.Slack",
      "typeVersion": 1,
      "position": [1100, 200]
    },
    {
      "parameters": {
        "channel": "#general",
        "text": "Email: {{ email }}\nMessage: {{ message }}"
      },
      "name": "Slack - General",
      "type": "n8n-nodes-base.Slack",
      "typeVersion": 1,
      "position": [1100, 350]
    }
  ],
  "connections": {
    "Webhook": [
      {
        "node": "Extract Fields",
        "type": "main"
      }
    ],
    "Extract Fields": [
      {
        "node": "Classify Message",
        "type": "main"
      }
    ],
    "Classify Message": [
      {
        "node": "Route by Category",
        "type": "main"
      }
    ],
    "Route by Category": [
      {
        "node": "Slack - Soporte",
        "type": "case: soporte"
      },
      {
        "node": "Slack - Ventas",
        "type": "case: ventas"
      },
      {
        "node": "Slack - General",
        "type": "case: otro"
      }
    ]
  }
}
```

Este workflow contiene:

1. **Webhook**: Recibe la solicitud POST inicial
2. **Extract Fields**: Extrae los campos "email" y "message" del body
3. **Classify Message**: Usa OpenAI para clasificar el mensaje
4. **Route by Category**: Enruta el mensaje según la clasificación
5. **Slack Nodes**: Envía el mensaje al canal correspondiente en Slack

**Notas importantes**:
1. Necesitarás configurar las credenciales de OpenAI y Slack en N8N antes de usar este workflow
2. El nodo de OpenAI usa un prompt en español para clasificar el mensaje
3. Los mensajes se formatean con los campos extraídos usando expresiones N8N ({{ email }} y {{ message }})
4. Asegúrate de tener los canales #support, #sales y #general existentes en tu espacio de Slack

Para usar este workflow:
1. Copia el JSON
2. En N8N, crea un nuevo workflow
3. Usa el botón "Import" y pega el JSON
4. Configura las credenciales para OpenAI y Slack
5. Active el webhook y pruebe el flujo con una solicitud POST ```json
{
  "email": "ejemplo@dominio.com",
  "message": "Necesito ayuda con mi cuenta"
}
```