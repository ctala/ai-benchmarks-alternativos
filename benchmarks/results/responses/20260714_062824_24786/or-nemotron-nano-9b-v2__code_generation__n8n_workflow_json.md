# Nemotron Nano 9B v2 — code_generation/n8n_workflow_json

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 8.04 | quality: 8.6
- latency_total: 47.819s | tokens_per_second: 38.0
- input_tokens: 129 | output_tokens: 1818
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una estructura clara y utilidad práctica, aunque carece de profundidad en términos de insights adicionales.

## Respuesta completa



Aquí tienes el workflow en formato JSON para N8N que cumple con tus requisitos:

```json
{
  "workflows": [
    {
      "id": "workflow_1",
      "name": "Clasificador de mensajes por canal",
      "nodes": [
        {
          "id": "node_0",
          "type": "webhook",
          "enabled": true,
          "webhookAddress": "https://yourdomain.com/webhook",
          "auth": {
            "enabled": false
          }
        },
        {
          "id": "node_1",
          "type": "json",
          "enabled": true,
          "json": {
            "email": "$.body.email",
            "message": "$.body.message"
          }
        },
        {
          "id": "node_2",
          "type": "ai",
          "enabled": true,
          "ai": {
            "model": "gpt-3.5-turbo",
            "apiKey": "YOUR_OPENAI_API_KEY",
            "prompt": "Clasifica este mensaje en una de las siguientes categorías: soporte, ventas o otro. Responde solo con la categoría en español.",
            "input": "$.message"
          }
        },
        {
          "id": "node_3",
          "type": "router",
          "enabled": true,
          "router": {
            "match": "$.ai.result",
            "rules": [
              {
                "value": "soporte",
                "next": "node_4"
              },
              {
                "value": "ventas",
                "next": "node_5"
              },
              {
                "value": "otro",
                "next": "node_6"
              }
            ]
          }
        },
        {
          "id": "node_4",
          "type": "slack",
          "enabled": true,
          "slack": {
            "webhookUrl": "YOUR_SLACK_WEBHOOK_URL_FOR_SUPPORT",
            "message": "Nuevo mensaje de soporte de {{$.email}}: {{$.message}}"
          }
        },
        {
          "id": "node_5",
          "type": "slack",
          "enabled": true,
          "slack": {
            "webhookUrl": "YOUR_SLACK_WEBHOOK_URL_FOR_SALES",
            "message": "Nuevo mensaje de ventas de {{$.email}}: {{$.message}}"
          }
        },
        {
          "id": "node_6",
          "type": "slack",
          "enabled": true,
          "slack": {
            "webhookUrl": "YOUR_SLACK_WEBHOOK_URL_FOR_GENERAL",
            "message": "Nuevo mensaje general de {{$.email}}: {{$.message}}"
          }
        }
      ],
      "connections": [
        { "from": "node_0", "to": "node_1" },
        { "from": "node_1", "to": "node_2" },
        { "from": "node_2", "to": "node_3" },
        { "from": "node_3", "to": "node_4" },
        { "from": "node_3", "to": "node_5" },
        { "from": "node_3", "to": "node_6" }
      ]
    }
  ]
}
```

### Explicación del workflow:

1. **Webhook POST (node_0)**:
   - Activa el workflow cuando recibe una solicitud POST en la URL especificada
   - No requiere autenticación en este ejemplo

2. **Nodo JSON (node_1)**:
   - Extrae los campos `email` y `message` del body de la solicitud

3. **Nodo de IA (node_2)**:
   - Usa OpenAI (GPT-3.5-turbo) para clasificar el mensaje
   - El prompt debe ser ajustado según tus necesidades
   - El resultado se almacena en `$.ai.result`

4. **Router (node_3)**:
   - Enruta el flujo según el resultado de la clasificación

5. **Nodos de Slack (node_4, node_5, node_6)**:
   - Enviarán el mensaje al canal correspondiente según la clasificación
   - Reemplaza `YOUR_SLACK_WEBHOOK_URL_FOR_*` con tus URLs reales de webhook de Slack

### Requisitos adicionales:
1. Debes tener configurados los webhooks de Slack en cada nodo
2. Reemplaza `YOUR_OPENAI_API_KEY` con tu clave real de OpenAI
3. Asegúrate de tener permisos para usar los modelos de OpenAI
4. Ajusta el prompt de OpenAI según el tipo de mensajes que recibirás

### Notas:
- Puedes agregar validaciones adicionales para manejar errores en la clasificación
- Para seguridad, considera usar autenticación en el webhook inicial
- Puedes personalizar los mensajes que se envían a Slack agregando más contexto
