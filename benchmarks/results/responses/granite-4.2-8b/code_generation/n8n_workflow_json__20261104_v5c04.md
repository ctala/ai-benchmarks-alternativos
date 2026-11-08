# Granite 4.2 8B — code_generation/n8n_workflow_json

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 7.5 | quality: 8.2
- latency_total: 88.38s | tokens_per_second: 80.5
- input_tokens: 134 | output_tokens: 7118
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, cumpliendo con los requisitos del flujo de trabajo, aunque la profundidad es limitada ya que sigue la instrucción directamente sin ofrecer insights adicionales.

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

{
  "nodes": [
    {
      "type": "n8n-nodes-base.webhook",
      "name": "Webhook",
      "position": [0, 0],
      "webhookId": "receive_message",
      "method": "POST",
      "path": "receive-message"
    },
    {
      "type": "n8n-nodes-base.function",
      "name": "Extract Fields",
      "position": [100, 0],
      "functionCode": "const input = items[0].json;\n// Validar que los campos existan\nif (!input.email || !input.message) {\n  return [{ error: 'Faltan email o message en el cuerpo del webhook' }];\n}\nreturn [{\n  email: input.email,\n  message: input.message,\n}];"
    },
    {
      "type": "n8n-nodes-base.openai",
      "name": "Classify Message",
      "position": [200, 0],
      "model": "gpt-3.5-turbo",
      "prompt": "Clasifica el siguiente mensaje **exactamente** en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. Responde **solo** con la categoría (sin texto adicional, sin mayúsculas/minúsculas inconsistentes). Mensaje: {{ $json.message }}",
      "options": {}
    },
    {
      "type": "n8n-nodes-base.switch",
      "name": "Route by Category",
      "position": [300, 0],
      "conditions": [
        {
          "value1": "={{ $json.text.toLowerCase() }}",
          "value2": "soporte",
          "operation": "equals"
        },
        {
          "value1": "={{ $json.text.toLowerCase() }}",
          "value2": "ventas",
          "operation": "equals"
        },
        {
          "value1": "={{ $json.text.toLowerCase() }}",
          "value2": "otro",
          "operation": "equals"
        }
      ]
    },
    {
      "type": "n8n-nodes-base.slack",
      "name": "Send to Support",
      "position": [400, -50],
      "channel": "#support",
      "text": "📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
      "options": {}
    },
    {
      "type": "n8n-nodes-base.slack",
      "name": "Send to Sales",
      "position": [400, 50],
      "channel": "#sales",
      "text": "📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
      "options": {}
    },
    {
      "type": "n8n-nodes-base.slack",
      "name": "Send to General",
      "position": [400, 100],
      "channel": "#general",
      "text": "📧 Email: {{ $json.email }}\n💬 Mensaje: {{ $json.message }}",
      "options": {}
    }
  ],
  "connections": {
    "Webhook": {
      "main": [["Extract Fields"]]
    },
    "Extract Fields": {
      "main": [["Classify Message"]]
    },
    "Classify Message": {
      "main": [["Route by Category"]]
    },
    "Route by Category": {
      "main": [
        ["Send to Support", 0],
        ["Send to Sales", 1],
        ["Send to General", 2]
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "1"
}