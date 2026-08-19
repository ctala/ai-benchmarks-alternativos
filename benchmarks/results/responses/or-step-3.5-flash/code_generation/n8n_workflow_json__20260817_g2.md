# Step 3.5 Flash — code_generation/n8n_workflow_json

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.71 | quality: 8.2
- latency_total: 33.361s | tokens_per_second: 61.4
- input_tokens: 134 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es relevante y clara, proporcionando una buena estructura para el workflow de n8n, aunque carece de detalles específicos como el JSON final y configuraciones exactas.

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

Vamos a crear un workflow de n8n que cumpla con los requisitos.

Pasos:
1. Nodo Webhook (POST) para recibir los datos.
2. Extraer los campos "email" y "message" del body (ya vienen en el webhook, pero aseguramos).
3. Nodo OpenAI para clasificar el mensaje en una de las tres categorías.
4. Dependiendo de la clasificación, enviar a un canal de Slack diferente.

Para el nodo OpenAI, usaremos un modelo de chat (gpt-3.5-turbo o gpt-4) con un prompt que pida clasificar el mensaje en una de las tres categorías.

Para Slack, necesitaremos un nodo de Slack que envíe un mensaje a un canal. Configuraremos tres nodos de Slack (o uno solo con una expresión que determine el canal) pero para simplificar, podemos usar un solo nodo de Slack y usar una expresión en el campo "Channel" para que elija el canal basado en la clasificación.

Sin embargo, n8n permite usar expresiones en los campos. Podemos hacer:

- Usar un nodo de IA (OpenAI) que devuelva la clasificación en un campo (por ejemplo, "classification").
- Luego, en el nodo de Slack, el campo "Channel" puede ser una expresión que mapee:
   classification == "soporte" -> "#support"
   classification == "ventas" -> "#sales"
   classification == "otro" -> "#general"

Pero también podríamos tener tres nodos de Slack separados con condiciones (IF) pero es más eficiente con un solo nodo y expresión.

Sin embargo, el requisito dice "según la clasificación, envíe el email a un canal de Slack diferente". Podemos hacerlo de dos formas:

Opción A: Un solo nodo Slack con expresión para el canal.
Opción B: Tres nodos Slack con condiciones (IF) que enruten según la clasificación.

Vamos a elegir la Opción A por simplicidad y menos nodos.

Pero ten en cuenta que el nodo Slack necesita un token y la configuración del canal. El canal será dinámico.

En el JSON del workflow, el nodo Slack tendrá en el campo "channel" una expresión como:

`{% if $json.classification == "soporte" %}#support{% elsif $json.classification == "ventas" %}#sales{% else %}#general{% endif %}`

Sin embargo, el nodo Slack en n8n espera un string para el canal, y podemos usar una expresión.

Pero también debemos tener en cuenta que el mensaje a enviar a Slack debe incluir el email y el mensaje original.

Vamos a estructurar:

1. Webhook (POST) -> captura el body.
2. Nodo OpenAI (classify) -> recibe el mensaje y devuelve la clasificación.
3. Nodo Slack -> envía el mensaje al canal correspondiente.

En el nodo OpenAI, debemos configurar:

- Resource: "Chat"
- Model: "gpt-3.5-turbo" (o el que prefieras)
- Prompt: algo como: "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Mensaje: {{ $json.message }}. Responde solo con la categoría."

Pero también podríamos pedir que devuelva un JSON, pero para simplificar, pedimos solo la categoría y luego la extraemos.

En el nodo OpenAI, la respuesta vendrá en `$json.response` (dependiendo de la configuración). Normalmente, la respuesta del modelo está en `$json.message.content` (si usamos el recurso "Chat" y la opción "Return Answer" está activada). 

En n8n, cuando usas el nodo OpenAI con el recurso "Chat", la respuesta por defecto es un objeto con:
- "message": { "content": "respuesta", ... }

Pero podemos configurar para que devuelva solo el contenido. En la configuración del nodo, hay una opción "Return Answer" que devuelve solo el string de la respuesta.

Para este ejemplo, asumamos que activamos "Return Answer", entonces la respuesta estará en `$json.answer`.

Entonces, después del nodo OpenAI, tendremos un campo "answer" con la clasificación.

Luego, en el nodo Slack, podemos usar:

- Channel: `{% if $json.answer == "soporte" %}#support{% elsif $json.answer == "ventas" %}#sales{% else %}#general{% endif %}`

Pero también debemos formatear el mensaje de Slack. Podemos enviar un mensaje que incluya el email y el mensaje original.

En el nodo Slack, el campo "Text" puede ser:

`Nuevo mensaje de {{ $json.email }}: {{ $json.message }}`

Pero también podríamos incluir la clasificación, por ejemplo:

`[{{ $json.answer }}] Nuevo mensaje de {{ $json.email }}: {{ $json.message }}`

Ahora, el workflow completo en JSON.

Nota: En el JSON, los nodos tienen un "id" único, "name", "type", etc.

Vamos a construir:

1. Webhook node (type: "n8n-nodes-base.webhook")
2. OpenAI node (type: "n8n-nodes-base.openAi")
3. Slack node (type: "n8n-nodes-base.slack")

Además, necesitamos conectar los nodos.

El webhook dispara el OpenAI, y el OpenAI dispara el Slack.

En el JSON, las conexiones se definen en "connections".

También debemos tener en cuenta que el webhook espera un POST, y extraerá automáticamente el body. En el webhook, el método es POST y la ruta puede ser la que quieras, pero en el JSON se define "path": "webhook".

Para el nodo OpenAI, necesitamos configurar la credencial (credentials) y el prompt.

En el JSON, las credenciales se referencian por nombre, pero en el archivo de exportación, las credenciales no se incluyen (se gestionan aparte). Así que en el JSON pondremos un placeholder para la credencial.

Lo mismo para Slack.

Vamos a escribir el JSON.

Estructura:

{
  "name": "Clasificador de mensajes a Slack",
  "nodes": [
    {
      "parameters": {
        "path": "webhook",
        "httpMethod": "POST",
        "responseMode": "onReceived",
        "options": {}
      },
      "id": "webhook",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [x, y]
    },
    {
      "parameters": {
        "resource": "chat",
        "model": "gpt-3.5-turbo",
        "prompt": "Clasifica el siguiente mensaje en una de estas categorías: 'soporte', 'ventas' o 'otro'. Mensaje: {{ $json.message }}. Responde solo con la categoría.",
        "options": {},
        "returnAnswer": true
      },
      "id": "openAi",
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "typeVersion": 1,
      "position": [x, y],
      "credentials": {
        "openAi": "openAiAccount"  // Este es el nombre de la credencial en n8n
      }
    },
    {
      "parameters": {
        "channel": {
          "__rl": true,
          "value": "{% if $json.answer == 'soporte' %}#support{% elsif $json.answer == 'ventas' %}#sales{% else %}#general{% endif %}",
          "type": "string"
        },
        "text": "Nuevo mensaje de {{ $json.email }}: {{ $json.message }}",
        "otherOptions": {}
      },
      "id": "slack",
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [x, y],
      "credentials": {
        "slackApi": "slackAccount"  // Este es el nombre de la credencial en n8n
      }
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "OpenAI",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "OpenAI": {
      "main": [
        [
          {
            "node": "Slack",
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

Notas:
- En el nodo Webhook, el "path" es "webhook" pero se puede cambiar.
- En el nodo OpenAI, usamos "returnAnswer": true para que la respuesta sea un string en `$json.answer`.
- En