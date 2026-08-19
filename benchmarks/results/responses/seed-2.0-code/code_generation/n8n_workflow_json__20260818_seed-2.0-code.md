# Seed 2.0 Code — code_generation/n8n_workflow_json

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.62 | quality: 7.28
- latency_total: 37.116s | tokens_per_second: 55.2
- input_tokens: 153 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

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


El usuario pide un workflow de N8N en JSON que cumpla 4 puntos: webhook POST, extraer email y message, clasificar con OpenAI, enviar a Slack según clasificación.

Primero, voy a estructurar cada nodo:

1. **Nodo Webhook Trigger**: Tiene que ser POST, recibir el body, configurado para escuchar. El ID suele ser algo como "1" o un identificador único, pero N8N usa UUIDs, pero puedo usar IDs legibles pero válidos. También, en las opciones del webhook, hay que especificar que es "On Webhook Call" y método POST.

2. **Nodo de Extracción? Wait, no: el OpenAI puede usar los datos del body directamente, pero tal vez es mejor usar un nodo "Set" para extraer claramente email y message, para que el prompt de OpenAI sea más limpio. Sí, porque si el body tiene más campos, el Set filtra solo lo necesario: nombre de variable "email" = $json.body.email, "message" = $json.body.message. Eso es más mantenible.

3. **Nodo OpenAI (Chat Completion)**: Tiene que ser el modelo que sea, por ejemplo gpt-3.5-turbo (más económico). El prompt es clave: hay que dar instrucciones claras de clasificar el mensaje en exactamente 3 categorías, sin texto extra, solo la categoría. Ejemplo de system prompt: "Eres un clasificador de mensajes de clientes. Clasifica el siguiente mensaje ÚNICAMENTE en una de estas tres categorías: 'soporte', 'ventas' o 'otro'. No escribas nada más que la categoría, sin comillas ni espacios extra." Y el user prompt es el contenido del message extraído, más el email? O solo el message? Mejor solo el mensaje, porque el email es para enviar a Slack. También, configurar el nodo para usar la API Key de OpenAI (pero en N8N se guarda como credencial, así que en el JSON se pone el ID de credencial, pero como es un ejemplo, se puede poner un placeholder o dejar el campo de credencial como una referencia que el usuario rellene).

4. **Nodo de Enrutamiento (Switch)**: Porque según la clasificación de OpenAI, vamos a un nodo Slack u otro. El Switch usa como valor de entrada la respuesta del OpenAI, que debe ser exactamente "soporte", "ventas" o "otro". Las rutas son:
   - Ruta 1: Valor = "soporte" → va a Slack #support
   - Ruta 2: Valor = "ventas" → va a Slack #sales
   - Ruta Default: → va a Slack #general

5. **Tres Nodos Slack (Chat Post Message)**: Cada uno con su canal:
   - Slack Soporte: Canal #support, credencial de Slack (placeholder), texto con el email y el mensaje: "Nuevo mensaje de soporte de {{$json.email}}: {{$json.message}}"
   - Slack Ventas: Canal #sales, texto similar pero de ventas
   - Slack General: Canal #general, texto de "otro"

Ahora, hay que tener en cuenta las particularidades de N8N JSON:
- Los workflows tienen un nombre, por ejemplo "Clasificador Mensajes OpenAI → Slack"
- Cada nodo tiene un "id" único, "name" legible, "type" (ej: n8n-nodes-base.webhook, n8n-nodes-base.set, n8n-nodes-base.openAi, n8n-nodes-base.switch, n8n-nodes-base.slack)
- Las conexiones entre nodos: en N8N se usa "connections" en cada nodo, indicando qué nodos le siguen.
- Las credenciales: en N8N, las credenciales se guardan con un ID, así que en el JSON se pone algo como "credentials": {"openAiApi": {"id": "{{OPENAI_CREDENTIAL_ID}}", "name": "OpenAiApi"}} pero como es un ejemplo, se puede dejar que el usuario reemplace los placeholders, o especificar que debe configurar las credenciales en N8N.
- El nodo Webhook: su "webhookId" es generado por N8N, pero en el JSON podemos poner un placeholder, o dejar que N8N lo genere al importar.
- El nodo OpenAI: hay que especificar el modelo, el modo (Chat), los mensajes (system y user), y que la respuesta sea solo el texto (no el objeto completo), así que en el nodo OpenAI se configura "responseFormat" como "text", o usar "output" = "message" para que devuelva solo el contenido.

También, es importante que el nodo Set extraiga bien los campos: en N8N, cuando el webhook recibe un POST, el body está en $json.body, así que el Set debe tener:
- Nombre: "Datos Cliente"
- Valores:
  - email: $json.body.email
  - message: $json.body.message

Para el nodo OpenAI, el prompt del usuario debe ser el message del Set, así que:
- System Message: "Eres un clasificador de mensajes de clientes. Tu única tarea es clasificar el mensaje proporcionado EN ÚNICAMENTE UNA de estas tres categorías: 'soporte', 'ventas' o 'otro'. NO escribas absolutamente nada más que la categoría, sin comillas, sin espacios, sin explicaciones. Ejemplos de clasificación: Si el mensaje es 'No puedo acceder a mi cuenta' → soporte; Si es 'Quiero cotizar un producto' → ventas; Si es 'Hola, ¿cómo están?' → otro"
- User Message: $json.message (porque viene del nodo Set)

El nodo Switch: su "rules" son:
- Regla 1: Valor 1 = $json.response (del OpenAI), Operador = Igual a, Valor 2 = "soporte"
- Regla 2: Mismo, Valor 2 = "ventas"
- Default: Si no coincide ninguna, va a general

Los nodos Slack: cada uno usa el "email" y "message" del nodo Set, así que en el texto del mensaje Slack, usamos $json.email y $json.message (porque el flujo pasa por el Set, luego OpenAI, luego Switch, luego Slack, así que el contexto tiene esos campos).

Ahora, armar el JSON completo, teniendo en cuenta:
- El formato de N8N: empieza con { "name": "...", "nodes": [...], "connections": {...}, "active": true, "settings": {}, "versionId": "...", "id": "..." }
- Los IDs de los nodos: usar UUIDs ficticios pero válidos, o IDs secuenciales pero únicos. Por ejemplo:
  - Webhook: id "1", name "Webhook Trigger"
  - Set: id "2", name "Extraer Datos Cliente"
  - OpenAI: id "3", name "Clasificar Mensaje OpenAI"
  - Switch: id "4", name "Enrutar por Clasificación"
  - Slack Soporte: id "5", name "Enviar a Slack #support"
  - Slack Ventas: id "6", name "Enviar a Slack #sales"
  - Slack General: id "7", name "Enviar a Slack #general"

También, en las conexiones:
- Webhook (1) → Set (2)
- Set (2) → OpenAI (3)
- OpenAI (3) → Switch (4)
- Switch (4) → Ruta 0 (soporte) → Slack (5)
- Switch (4) → Ruta 1 (ventas) → Slack (6)
- Switch (4) → Ruta Default → Slack (7)

Otra cosa: el nodo Webhook debe tener "method" = "POST", "path" = "/clasificador-mensajes" (o un placeholder, pero N8N lo genera si no se especifica), "responseMode" = "onReceived" para responder rápido.

El nodo OpenAI: "typeVersion" = 4 (la última versión del nodo OpenAI en N8N), "model" = "gpt-3.5-turbo", "temperature" = 0 (para que no sea creativo, sea exacto en la clasificación), "maxTokens" = 10 (solo necesita una palabra).

Los nodos Slack: "typeVersion" = 3, "channel" = "#support" (por ejemplo), "text" = "📩 Nuevo mensaje de **SOPORTE**\n📧 Email: {{$json.email}}\n💬 Mensaje: {{$json.message}}", "parseMode" = "markdown" para que se vea bonito.

También, hay que agregar placeholders para las credenciales: en cada nodo que use credenciales (OpenAI y Slack