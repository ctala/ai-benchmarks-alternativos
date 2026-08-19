# Sakana Namazu — code_generation/n8n_workflow_json

- model_id: `sakana/sakana-namazu`
- success: True  | final: 6.25 | quality: 6.52
- latency_total: 8.422s | tokens_per_second: 243.2
- input_tokens: 207 | output_tokens: 2048
- judge_score: 2.8 | justificación: 

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

El usuario quiere un workflow de N8N en formato JSON que:
1. Se active con un webhook POST
2. Extraiga "email" y "message" del body
3. Use nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Según la clasificación, envíe a diferentes canales de Slack:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Necesito generar un JSON válido de N8N. Los nodos típicos serían:
- Webhook (trigger)
- Set o directamente pasar a OpenAI (pero necesitamos extraer email y message)
- OpenAI Chat Model o OpenAI node (en N8N hay varias versiones). En N8N moderno suele usarse el nodo de OpenAI con "Message Model" o el nodo "AI Agent". Pero para una clasificación simple, se puede usar el nodo "OpenAI" (text generation) o el nodo "Chat OpenAI". Sin embargo, para mantenerlo simple y compatible, usaré el nodo "OpenAI" (la versión de completions o chat) o mejor aún, el nodo "OpenAI" tipo "message" (chat model).

En realidad, en N8N los workflows se exportan con una estructura específica. Voy a crear un workflow estándar con nodos:
1. "Webhook" - POST
2. "OpenAI" - para clasificación
3. "Switch" o "IF" - para rutear según la clasificación. Pero en N8N se puede usar un nodo "Switch" (ahora llamado "Switch" en versiones recientes, aunque a veces se usa "IF" múltiple). En el JSON de N8N, el nodo "Switch" permite múltiples outputs basados en reglas.
4. Tres nodos de "Slack" para enviar mensajes a cada canal.

Espera, en N8N el nodo "OpenAI" moderno (después de las actualizaciones de AI) puede ser un poco complejo. Pero también puedo usar el nodo "HTTP Request" o simplemente el nodo "OpenAI" con operation "message". Sin embargo, para asegurar compatibilidad, mejor usar un nodo genérico de "OpenAI" o "Chat Model". 

Pero en realidad, lo más compatible es usar el nodo "OpenAI" (el clásico, no el de LangChain) con operation "completion" o "chat". En versiones recientes de N8N, el nodo "OpenAI" tiene operation 'message' para el modelo de chat.

La estructura del JSON de N8N es algo así:
```json
{
  "name": "Clasificador IA a Slack",
  "nodes": [
    {
      "parameters": {},
      "id": "uuid",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [x, y],
      "webhookId": "uuid"
    },
    ...
  ],
  "connections": {...}
}
```

Necesito asegurarme de usar UUIDs coherentes. Generaré UUIDs v4.

Nodos:
1. Webhook:
   - path: clasifica-email
   - method: POST
   - responseMode: onReceived (o lastNode)
   - jsonParameters: true? No, por defecto.
   - options: {}

2. OpenAI:
   - En N8N, el nodo OpenAI (tipo message/chat) necesita:
     - model: gpt-4o-mini o gpt-3.5-turbo
     - messages: array con user message
   - La versión del nodo OpenAI varía. En versiones modernas (typeVersion 1 para chat), pero para ser más compatible con la mayoría, usaré el nodo "OpenAI" con operation "completion".
   
   Sin embargo, la API de completions legacy no es ideal. El nodo "OpenAI" en N8N soporta chat en typeVersion 1. Veamos la estructura típica de un nodo OpenAI en N8N:

```json
{
  "parameters": {
    "resource": "chat",
    "operation": "message",
    "model": "gpt-4o-mini",
    "messages": {
      "values": [
        {
          "role": "user",
          "content": "Clasifica el siguiente mensaje en una de estas categorías: soporte, ventas, otro. Responde solo con la categoría en minúsculas, sin puntuación ni explicaciones.\n\nMensaje: {{ $json.body.message }}"
        }
      ]
    }
  },
  "name": "Clasificar con OpenAI",
  "type": "n8n-nodes-base.openAi",
  "typeVersion": 1,
  ...
}
```

Espera, el webhook body se accede como `$json.body` o directamente `$json` dependiendo de la versión. En webhooks POST con Content-Type application/json, N8N pone los datos en `$json.body` en algunas versiones? No, en realidad, en el nodo webhook, los datos entrantes están directamente en `$json` si es un JSON body. Pero a veces están en `$json.body` si el nodo los encapsula. En muchos casos es `$json.body` para la propiedad body, pero en versiones recientes de N8N, para el trigger webhook, los datos del body están en el json principal, es decir, para acceder a email sería `$json.email` y `$json.message`. Voy a usar `$json.message` y `$json.email` asumiendo que el webhook recibe el JSON directamente.

3. Switch:
   - El nodo Switch en N8N permite múltiples outputs.
   - rules: 
     - output 0: value equal to "soporte"
     - output 1: value equal to "ventas"
     - output 2: value equal to "otro" (o fallback)
   - mode: rules
   - dataType: string
   - value1: `{{ $json.content }}` (o donde venga la respuesta de OpenAI)

El problema es cómo extraer la respuesta de OpenAI. Si uso el nodo OpenAI chat message, la respuesta suele estar en `$json.message` o `$json.content`. Depende del nodo. En el nodo OpenAI (resource: chat, operation: message), la respuesta suele estar en `$json.content` o `$json.message.content`. Necesito verificar la estructura típica.

En N8N, el nodo OpenAI retorna un item con `content` o `message`? Para la operación "message" del recurso "chat", el resultado típico es un array y cada item tiene un `message` con `content`, o directamente `content`. En versiones recientes, el campo es `message` con un objeto que tiene `content`. Pero a veces el nodo expone `content` directamente. 

Para ser seguro, puedo usar un nodo Set antes del Switch para normalizar la clasificación, o simplemente asumir que está en `$json.content` o `$json.message.content`. 

Otra opción es usar el nodo "Code" para extraerlo, pero eso complica.

En realidad, el nodo OpenAI en N8N (typeVersion 1, resource chat, operation message) devuelve el contenido en `$json.message.content`. Pero en algunos casos `$json.content`. 

Voy a usar un nodo "Move Binary Data" o mejor, un nodo "Set" (Data transformation) para crear un campo "categoria" basado en la salida de OpenAI, y luego usar ese campo en el Switch.

Nodo "Set" (llamado "Edit Fields" en versiones nuevas, tipo `n8n-nodes-base.set`, typeVersion 3?):
```json
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "name": "categoria",
          "value": "={{ $json.message.content.trim().toLowerCase() }}",
          "type": "string"
        },
        {
          "name": "email",
          "value": "={{ $('Webhook').first().json.email }}",
          "type": "string"
        },
        {
          "name": "message",
          "value": "={{ $('Webhook').first().json.message }}",
          "type": "string"
        }
      ]
    }
  }
}
```

Luego el Switch usa `{{ $json.categoria }}`.

Nodos de Slack:
- Necesitan el canal (channel ID o nombre).
- text: `Nuevo mensaje de {{ $json.email }}: {{ $json.message }}`
- authentication: "oAuth2" o "accessToken". Pero en el JSON de workflow no necesitamos credenciales reales, solo la estructura. Así que dejo los parámetros