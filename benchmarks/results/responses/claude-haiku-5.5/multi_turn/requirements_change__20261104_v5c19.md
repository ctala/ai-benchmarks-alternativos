# Claude Haiku 5.5 — multi_turn/requirements_change

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.18 | quality: 6.0
- latency_total: 11.311s | tokens_per_second: 217.9
- input_tokens: 365 | output_tokens: 2465

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

Perfecto, el flujo queda así:

**Gmail Trigger → IF (filtro) → Code (extraer datos) → Notion (crear página) → Slack (notificar)**

### 1. Gmail Trigger
- **Event:** Message Received
- **Simplify:** desactivado, para tener acceso a `from`, `subject` y `date`.
- Opcional: en *Filters* puedes poner en *Search* `subject:(propuesta OR cotizacion OR cotización)` para reducir las ejecuciones. Igualmente conviene el nodo IF, que es más explícito.

### 2. IF (filtro por asunto)
- **Combinator:** OR
- **Condición 1:** `{{ $json.subject.toLowerCase() }}` → *contains* → `propuesta`
- **Condición 2:** `{{ $json.subject.toLowerCase() }}` → *contains* → `cotizacion`
- **Condición 3:** `{{ $json.subject.toLowerCase() }}` → *contains* → `cotización`

Solo la rama **true** continúa. La rama false puede quedar vacía.

### 3. Code (extraer datos del remitente)
Modo: *Run Once for Each Item*, lenguaje JavaScript:

```javascript
const from = $json.from || '';
// Formato típico: "Juan Pérez <juan@empresa.com>"
const match = from.match(/^"?(.*?)"?\s*<(.+?)>$/);

const nombre = match ? match[1].trim() : from.split('@')[0];
const email = match ? match[2].trim() : from.trim();

return {
  json: {
    nombre,
    email,
    asunto: $json.subject,
    fecha: $json.date,
  }
};
```

### 4. Notion (crear página)
Antes, crea una base de datos en Notion con estas propiedades:
- **Nombre** (Title)
- **Email** (Email)
- **Asunto** (Text)
- **Fecha** (Date)
- **Estado** (Select, con la opción "Nuevo")

En el nodo:
- **Resource:** Database Page
- **Operation:** Create
- **Database ID:** el ID que aparece en la URL de tu base de datos
- **Propiedades:**
  - Nombre → `{{ $json.nombre }}`
  - Email → `{{ $json.email }}`
  - Asunto → `{{ $json.asunto }}`
  - Fecha → `{{ $json.fecha }}`
  - Estado → `Nuevo`

### 5. Slack (notificación)
- **Resource:** Message
- **Operation:** Post
- **Channel:** el canal que elijas, por ejemplo `#propuestas`
- **Text:**

```
🆕 Nueva propuesta/cotización de {{ $('Code').item.json.nombre }} ({{ $('Code').item.json.email }})
Asunto: {{ $('Code').item.json.asunto }}
```

Uso `$('Code')` porque después del nodo de Notion el JSON cambia a la respuesta de Notion y los datos originales ya no están disponibles directamente. Si tu nodo se llama distinto, ajusta el nombre entre comillas.

### Notas
- **Acentos:** la búsqueda con `toLowerCase()` no normaliza tildes, por eso incluyo "cotizacion" y "cotización". Si quieres cubrir más variantes, añade otra condición.
- **Credenciales:** necesitarás conectar Gmail (OAuth), Notion (integración interna, y compartir la base de datos con ella) y Slack (app con permiso `chat:write` en el canal).
- **Prueba:** envía un email de prueba con "Propuesta" en el asunto y revisa cada nodo en modo ejecución antes de activar el workflow.

¿Quieres que añada manejo de errores o que guarde también el cuerpo del email en Notion?