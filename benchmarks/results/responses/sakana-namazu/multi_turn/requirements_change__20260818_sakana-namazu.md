# Sakana Namazu — multi_turn/requirements_change

- model_id: `sakana/sakana-namazu`
- success: True  | final: 5.81 | quality: 6.0
- latency_total: 10.001s | tokens_per_second: 204.8
- input_tokens: 266 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico para emprendedores que trabajan con N8N.

**user:**

Necesito un workflow en N8N que lea emails de Gmail, extraiga los datos del remitente, y los guarde en un Google Sheet.

**assistant:**

Perfecto, ese workflow es bastante directo. Te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Extraer datos**: Function node para parsear remitente, asunto, fecha
3. **Guardar**: Google Sheets node para agregar una fila

Los campos a extraer serian: nombre del remitente, email, asunto, fecha. Quieres que te detalle la configuracion de cada nodo?

**user:**

En realidad, cambio de idea. No quiero Google Sheets, quiero que los datos vayan a Notion. Ademas, quiero que el workflow filtre solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Y que me mande una notificacion a Slack cuando llegue uno.


## Respuesta completa

El usuario ha cambiado sus requerimientos. Ahora necesita:
1. Leer emails de Gmail
2. Filtrar emails que contengan "propuesta" o "cotizacion" en el asunto (case-insensitive idealmente)
3. Extraer datos del remitente
4. Guardar en Notion (en lugar de Google Sheets)
5. Enviar notificacion a Slack cuando llegue uno que cumpla la condicion

Debo proporcionar una respuesta clara, estructurada, explicando el workflow paso a paso con los nodos de N8N necesarios, incluyendo configuraciones clave y el código/expressions necesarios.

Nodos necesarios:
1. Gmail Trigger (On message received) o Schedule Trigger + Gmail (Fetch messages) - pero para instantaneo mejor Gmail Trigger. Necesito verificar si N8N tiene Gmail Trigger nativo. Sí, tiene "Gmail Trigger" en nodos regulares.
2. IF node o Filter node para verificar si el asunto contiene "propuesta" o "cotizacion". Puede usar un IF node con condicion "contains" y usar una expresion regex o simplemente OR. En N8N, el node IF permite condiciones string: contains. Puede hacer un OR o usar una expresion regex. Regex seria mejor: asunto.match(/propuesta|cotizacion/i)
3. Notion node: Create a database item. Necesita Database ID.
4. Slack node: Post a message.
5. Set node o directamente extraer datos del Gmail.

Datos a extraer del remitente: Nombre y Email. En Gmail node, from.value tiene el email, from.text tiene el nombre+email usualmente. Pero depende del formato. Generalmente viene como "Nombre <email@dominio.com>" en el campo "from".

Es mejor usar un Set node para estructurar los datos antes de enviarlos a Notion y Slack.

Estructura propuesta:
- Trigger: Gmail Trigger
- Set (opcional) o directo: Extraer datos. En realidad puedo recomendar un Code node o expresiones en Notion/Slack, pero quizás un Set node es mas amigable para usuarios no tecnicos. O puedo recomendar extraer directamente.
- IF Node: Condition check
- True branch:
  - Notion: Create Page/Database Item
  - Slack: Send Message
- False branch: Nothing (puede conectar a No Operation)

Detalles importantes:
- Gmail Trigger configuration: puede necesitar OAuth2 con Google.
- IF Node condition: {{ $json.snippet }} o {{ $json.subject }} ? En Gmail Trigger de N8N, el campo de asunto generalmente es $json.subject o similar. En realidad, dependiendo del nodo de N8N, la propiedad para el asunto puede ser 'subject'. Debo ser general o revisar mentalmente.
En n8n, el trigger de Gmail devuelve campos como: id, threadId, labelIds, snippet, payload, sizeEstimate, historyId, internalDate. El asunto y remitente usualmente están dentro de los headers (payload.headers). Esto es importante. El asunto no viene como campo top-level directamente en el trigger de N8N, viene en payload.headers donde name = "Subject" y name = "From".
Esto complica un poco. Necesito mencionar que el asunto y remitente están en headers.

Alternativa: Usar el regular "Gmail" node (get email) después del trigger si el trigger no da el asunto directamente, o extraerlo con una expresión.
En N8N, el Gmail Trigger tiene una opción "Simplify" (simplified: true). Si está activada, quizá ya extrae campos comunes. En las versiones recientes, el trigger de Gmail puede simplificar y extraer textHtml, textPlain, subject, from, etc. Si no, hay que usar una Function/Code node o expresiones en JSON.

Dado que es un asistente técnico, debo ser preciso.

Pasos detallados:
1. **Gmail Trigger**: Elegir "On Message Received". Conectar cuenta. Opcional: usar "Download Attachments" si se necesita, pero aquí no. Asegurarse de que esté en modo simplificado si está disponible para obtener subject/from directamente. Si no, usar un Set node para parsear los headers.

Como no sé con exactitud la versión de n8n del usuario, es mejor dar una solución robusta usando un **Code node (Function)** o explicar que puede usar el campo 'headers'.

Es mejor usar una aproximación que funcione independientemente de la versión:

Metodología:
1. **Gmail Trigger**: Obtener mensajes.
2. **Code Node (Function)** o **Set + Expressions**: Extraer "From", "Subject", "Date" de `payload.headers`. O si usa el Gmail node "Get Message" después del trigger, también funciona. Pero un Code node es más limpio para parsear headers.
3. **IF Node**: Usar una condición Regex para que case-insensitive capture "propuesta" o "cotizacion" (y sus variantes sin tilde? El usuario escribió "cotizacion" sin tilde, pero puede que llegue "cotización". Mejor usar regex que cubra ambas: /propuesta|cotizaci[oó]n/i ). En N8N IF node se puede usar string "Contains" y poner una condición con OR, o regex. Regex es más elegante. Pero el IF node nativo en n8n no tiene regex directamente en la UI básica de condiciones (tiene: equal, contains, starts with, etc). "Contains" permite solo strings fijas. Para OR se puede anidar IFs o usar un Code/Function node para evaluar y devolver un booleano, o usar el Conditional node.
En versiones recientes, el IF node (llamado ahora "If" o "Filter") permite Regex. Aunque si no, una expresión como: `{{ $json.subject.match(/propuesta|cotizaci[oó]n/i) ? true : false }}` en un Set node, luego usar IF sobre ese booleano.
Simplifiquemos: usar un **Code node (JavaScript)** para:
- Parsear headers
- Hacer el match regex
- Devolver objeto limpio con: nombre, email, asunto, fecha, matches (boolean)

Esto centraliza la lógica y hace el workflow más fácil de entender.

Luego:
4. **IF Node**: `matches` is true.
5. **True**: 
   - **Notion** -> **Create a Database Item**: Mapear propiedades. Necesito asumir que la base de datos en Notion tiene columnas como: Nombre, Email, Asunto, Fecha. En Notion, el "title" es el campo principal.
   - **Slack** -> **Post Message**: Enviar mensaje al canal deseado con info resumida.
6. **False**: Conectar a Nothing (o dejar desconectado).

Especificaciones de Notion:
- Necesita la integration (token) y el Database ID.
- Las propiedades deben coincidir.

Especificaciones de Slack:
- Necesita credencial Slack (OAuth o webhook).
- Channel ID o nombre (#general).

Voy a estructurar la respuesta:
- Resumen del workflow
- Paso a paso
  1. Gmail Trigger
  2. Function/Code node para parsear y filtrar (explicar el código)
  3. IF node
  4. Notion node (true branch)
  5. Slack node (true branch)
- Código del Function node
- Consideraciones (credenciales, regex, duplicados - puede agregar un "Notion: Find Database Item" antes de crear para evitar duplicados si el workflow corre varias veces, aunque con Gmail trigger y history quizá no sea tan necesario, pero es buena práctica).

Código del Function node (para N8N Code node, modo "Run Once for All Items" o "Run Once for Each Item"). Para triggers, va Run Once for Each Item.

```javascript
// Run once for each item
const item = $input.first().json;

// Helper para extraer header
const getHeader = (headers, name) => {
  const h = headers.find(h => h.name === name);
  return h ? h.value : '';
};

const headers = item.payload?.headers || [];
const from = getHeader(headers, 'From');
const subject = getHeader(headers, 'Subject');
const date = getHeader(headers, 'Date');

// Extraer email y nombre de "From" (puede ser "Nombre <email>" o solo "email")
const fromMatch = from.match(/(?:"?([^"]*)"?\s)?(?:<?(.+@[^>]+)>?)/);
const nombre = fromMatch && fromMatch[1] ? fromMatch[1].trim() : '';
const email = fromMatch && fromMatch[2] ? fromMatch[2].trim() :