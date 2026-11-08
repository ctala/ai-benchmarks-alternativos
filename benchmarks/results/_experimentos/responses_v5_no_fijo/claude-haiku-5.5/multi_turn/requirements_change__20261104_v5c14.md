# Claude Haiku 5.5 — multi_turn/requirements_change

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.17 | quality: 6.0
- latency_total: 12.363s | tokens_per_second: 210.1
- input_tokens: 365 | output_tokens: 2598

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

Perfecto, con esos cambios el flujo queda así:

**Gmail Trigger → IF (filtro) → Code (extraer datos) → Notion (guardar) → Slack (notificar)**

## 1. Gmail Trigger

- **Event**: Message Received
- **Simplify**: desactivado, para que recibas los campos completos
- **Filters → Search**: `subject:(propuesta OR cotizacion OR cotización)`

Este filtro hace que Gmail solo entregue los emails relevantes, así el resto del flujo no se ejecuta en vano. Como Gmail no siempre distingue bien las tildes, el nodo IF siguiente sirve de verificación.

## 2. IF (filtro de seguridad)

- **Combinator**: OR
- **Condiciones** (tipo String, operación *contains*):
  - `{{ $json.subject.toLowerCase() }}` contains `propuesta`
  - `{{ $json.subject.toLowerCase() }}` contains `cotizacion`
  - `{{ $json.subject.toLowerCase() }}` contains `cotización`

Salida **true** → continúa el flujo. Salida **false** → puedes dejarla sin conectar.

## 3. Code (extraer datos)

Modo: *Run Once for Each Item*. Código JavaScript:

```javascript
const from = $json.from || '';
const match = from.match(/^"?(.*?)"?\s*<(.+?)>$/);

const nombre = match ? match[1].trim() : from.split('@')[0];
const email = match ? match[2].trim() : from.trim();

return {
  json: {
    nombre,
    email,
    asunto: $json.subject,
    fecha: new Date($json.date).toISOString(),
    snippet: $json.snippet
  }
};
```

Este código separa `Juan Pérez <juan@empresa.com>` en nombre y email.

## 4. Notion (guardar)

Antes de empezar, crea una base de datos en Notion con estas propiedades:
- **Nombre** (tipo Title)
- **Email** (Email)
- **Asunto** (Text)
- **Fecha** (Date)
- **Snippet** (Text)

Luego, en la integración de Notion (notion.so/my-integrations) dale acceso a esa base de datos desde la configuración de la página. Sin este paso, n8n no la verá.

En el nodo Notion:
- **Resource**: Database Page
- **Operation**: Create
- **Database**: la base que creaste
- **Propiedades** (con expresiones):
  - Nombre: `{{ $json.nombre }}`
  - Email: `{{ $json.email }}`
  - Asunto: `{{ $json.asunto }}`
  - Fecha: `{{ $json.fecha }}`
  - Snippet: `{{ $json.snippet }}`

## 5. Slack (notificar)

Necesitas una Slack App con permiso `chat:write` instalada en tu workspace e invitada al canal donde quieres las notificaciones (`/invite @nombre-de-tu-app`).

En el nodo Slack:
- **Resource**: Message
- **Operation**: Send
- **Channel**: el canal elegido
- **Text**:

```
📩 Nueva propuesta/cotización recibida
De: {{ $('Code').item.json.nombre }} ({{ $('Code').item.json.email }})
Asunto: {{ $('Code').item.json.asunto }}
```

Usé `$('Code')` porque la salida de Notion no incluye esos datos, así que hay que referenciar el nodo anterior directamente.

## Pruebas

1. Envíate un email de prueba con "Propuesta" en el asunto y otro sin esas palabras.
2. Ejecuta el workflow manualmente y revisa que solo el primero llegue a Notion y Slack.
3. Revisa en cada nodo la salida para confirmar que los campos se mapean bien.
4. Cuando todo funcione, activa el workflow.

Si Notion te da error de propiedad, revisa que los nombres de las columnas coincidan exactamente (incluyendo mayúsculas) con los que usas en el nodo.