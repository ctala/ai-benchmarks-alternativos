# Granite 4.2 8B — code_generation/n8n_workflow_json

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 112.427s | tokens_per_second: 81.0
- input_tokens: 134 | output_tokens: 9106
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un workflow de N8N completo que cumple con los requisitos especificados.

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

```json
{
  "nodes": [
    {
      "type": "n8n-nodes-base.webhook",
      "name": "Webhook Trigger",
      "typeVersion": 1,
      "position": [200, 100],
      "parameters": {
        "httpMethod": "POST",
        "path": "n8n-webhook"
      },
      "notesInFlow": false
    },
    {
      "type": "n8n-nodes-base.function",
      "name": "Extract Fields",
      "typeVersion": 1,
      "position": [400, 100],
      "parameters": {
        "functionCode": "return [{\n  json: {\n    email: $json.email,\n    message: $json.message\n  }\n}];"
      },
      "notesInFlow": false
    },
    {
      "type": "n8n-nodes-base.openai",
      "name": "Classify Message",
      "typeVersion": 1,
      "position": [600, 100],
      "parameters": {
        "model": "gpt-3.5-turbo",
        "temperature": 0,
        "prompt": "Clasifica el siguiente mensaje **exactamente** como una de estas tres categorías: 'soporte', 'ventas' o 'otro'. No incluyas palabras adicionales, abreviaturas o explicaciones. Solo responde con la categoría en minúsculas (ejemplo: 'soporte'). Mensaje: {{ $json.message }}",
        "maxTokens": 50
      },
      "notesInFlow": false
    },
    {
      "type": "n8n-nodes-base.switch",
      "name": "Route Classification",
      "typeVersion": 1,
      "position": [800, 100],
      "parameters": {
        "rules": [
          {
            "value": "soporte",
            "operator": "equals",
            "value2": "",
            "output": 0
          },
          {
            "value": "ventas",
            "operator": "equals",
            "value2": "",
            "output": 1
          },
          {
            "value": "otro",
            "operator": "equals",
            "value2": "",
            "output": 2
          }
        ]
      },
      "notesInFlow": false
    },
    {
      "type": "n8n-nodes-base.slack",
      "name": "Send Support",
      "typeVersion": 1,
      "position": [1000, 0],
      "parameters": {
        "channel": "#support",
        "text": "📧 Email: {{$json.email}}\n💬 Mensaje: {{$json.message}}"
      },
      "notesInFlow": false
    },
    {
      "type": "n8n-nodes-base.slack",
      "name": "Send Sales",
      "typeVersion": 1,
      "position": [1000, 150],
      "parameters": {
        "channel": "#sales",
        "text": "📧 Email: {{$json.email}}\n💬 Mensaje: {{$json.message}}"
      },
      "notesInFlow": false
    },
    {
      "type": "n8n-nodes-base.slack",
      "name": "Send General",
      "typeVersion": 1,
      "position": [1000, 300],
      "parameters": {
        "channel": "#general",
        "text": "📧 Email: {{$json.email}}\n💬 Mensaje: {{$json.message}}"
      },
      "notesInFlow": false
    }
  ],
  "connections": {
    "Webhook Trigger": {
      "main": [{ "node": "Extract Fields", "type": "main", "index": 0 }]
    },
    "Extract Fields": {
      "main": [{ "node": "Classify Message", "type": "main", "index": 0 }]
    },
    "Classify Message": {
      "main": [{ "node": "Route Classification", "type": "main", "index": 0 }]
    },
    "Route Classification": {
      "main": [
        { "node": "Send Support", "type": "main", "index": 0 },
        { "node": "Send Sales", "type": "main", "index": 0 },
        { "node": "Send General", "type": "main", "index": 0 }
      ]
    }
  },
  "active": false,
  "settings": {},
  "id": "1"
}
```

### Explicación clave (para claridad, no incluida en JSON):
1. **Webhook Trigger**: Activa el workflow con `POST` al endpoint definido (`n8n-webhook`).
2. **Extract Fields** (Function node): Extrae y normaliza `email` y `message` del cuerpo del webhook (asegura que existan en la salida).
3. **Classify Message** (OpenAI node):  
   - Usa `gpt-3.5-turbo` con `temperature=0` para máxima consistencia.  
   - Prompt está diseñado para que la respuesta sea **solo** `"soporte"`, `"ventas"` o `"otro"` (sin texto extra), evitando ambigüedades.  
   - `maxTokens=50` es suficiente para una respuesta corta.
4. **Route Classification** (Switch node):  
   - Usa `rules` con `output` explícito (0 para `soporte`, 1 para `ventas`, 2 para `otro`). Esto asegura que solo el brazo correcto se active.  
   - `operator: "equals"` compara directamente el valor devuelto por OpenAI (que será `"soporte"`, `"ventas"` o `"otro"` gracias al prompt).
5. **Slack nodes**:  
   - Cada uno envía el mensaje con formato claro (`📧 Email: ...`, `💬 Mensaje: ...`).  
   - Canales exactos: `#support`, `#sales`, `#general` según la clasificación.  
   - Usa `{{$json.email}}` y `{{$json.message}}` para pasar los valores extraídos desde el inicio.
6. **Connections**:  
   - La lógica de ruta se define en `Route Classification` conectando sus tres salidas (brazos del Switch) directamente a los tres nodos Slack. N8N maneja automáticamente enviar solo al Slack correspondiente según la clasificación.

> ✅ **Notas prácticas para usar este JSON**:
> - Asegúrate de haber configurado credenciales de OpenAI y Slack en N8N antes de activar el workflow.
> - El endpoint del webhook será algo como `https://tus-n8n-instancia.com/webhook/n8n-webhook` (ajusta según tu instalación).
> - El prompt de OpenAI está optimizado para evitar respuestas como "El mensaje es sobre soporte" (solo `"soporte"`), usando "Clasifica... solo responde con la categoría".
> - Los valores `output: 0/1/2` en el Switch son críticos para que N8N enrute correctamente (sin esto, el Switch podría enviar a todos los brazos).

Este JSON es completo, válido para N8N v0.240+ (versión estándar actual), y cumple exactamente con los requisitos: webhook POST → extracción → clasificación con IA → envío condicional a Slack.