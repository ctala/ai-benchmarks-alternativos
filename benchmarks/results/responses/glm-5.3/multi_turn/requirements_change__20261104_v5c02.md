# GLM 5.3 — multi_turn/requirements_change

- model_id: `z-ai/glm-5.3`
- success: True  | final: 5.35 | quality: 6.0
- latency_total: 91.349s | tokens_per_second: 45.4
- input_tokens: 235 | output_tokens: 4143

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

Sin problema, reestructuramos. El flujo queda así:

**Gmail Trigger → Code (extraer datos) → IF (filtro por asunto) → Notion → Slack**

### 1. Gmail Trigger
- Evento: **Message Received** (se dispara con cada email nuevo)
- Deja el polling en el intervalo por defecto (1 minuto)

### 2. Code node — "Extraer datos"
El campo `from` de Gmail viene en formatos distintos según la versión del nodo (`"Nombre <email>"` o un objeto), así que mejor normalizarlo aquí:

```javascript
const email = $input.first().json;

let nombre = '';
let correo = '';

if (typeof email.from === 'object' && email.from?.value?.[0]) {
  nombre = email.from.value[0].name || '';
  correo = email.from.value[0].address || '';
} else if (typeof email.from === 'string') {
  const match = email.from.match(/^(.*?)\s*<(.+?)>$/);
  if (match) {
    nombre = match[1].replace(/"/g, '').trim();
    correo = match[2];
  } else {
    correo = email.from;
  }
}

const asunto = email.subject || '(sin asunto)';

// Minúsculas y sin acentos, para que el filtro no falle con "cotizacion" vs "cotización"
const asuntoNormalizado = asunto
  .toLowerCase()
  .normalize('NFD')
  .replace(/[\u0300-\u036f]/g, '');

return [{
  json: {
    nombre,
    correo,
    asunto,
    asuntoNormalizado,
    fecha: email.date || new Date().toISOString(),
    snippet: email.snippet || ''
  }
}];
```

### 3. IF node — "¿Es propuesta o cotización?"
Dos condiciones con combinator **OR**:
- `{{ $json.asuntoNormalizado }}` — *contains* — `propuesta`
- `{{ $json.asuntoNormalizado }}` — *contains* — `cotizacion`

(Sin acento en el valor porque ya lo normalizamos en el Code node.)

### 4. Notion node
- Resource: **Database Page** → Operation: **Create**
- Selecciona tu base de datos y mapea las propiedades:

| Propiedad en Notion | Valor |
|---|---|
| Nombre (Title) | `{{ $json.asunto }}` |
| Remitente (Text) | `{{ $json.nombre }}` |
| Email (Email) | `{{ $json.correo }}` |
| Fecha (Date) | `{{ $json.fecha }}` |
| Extracto (Text) | `{{ $json.snippet }}` |

### 5. Slack node
- Resource: **Message** → Operation: **Send**
- Channel: tu canal
- Text:

```
📧 Nueva propuesta/cotización recibida
*De:* {{ $json.nombre }} ({{ $json.correo }})
*Asunto:* {{ $json.asunto }}
```

### Detalles que suelen fallar

1. **Notion**: aunque el token de la integración sea válido, vas a recibir un error 404 si no compartiste la base de datos con la integración. En la base de datos: menú **⋯ → Connections → tu integración**.
2. **Slack**: si usas un bot, invítalo al canal con `/invite @tu-bot`, o te dará "channel_not_found".
3. **Notion primero, Slack después**: en ese orden, la notificación solo se envía si el registro en Notion se guardó bien (así la notificación implica que todo funcionó).

¿Quieres que ajustemos algo, por ejemplo qué pasa con los emails que NO coinciden con el filtro (se pueden archivar o marcar como leídos), o quieres agregar un enlace al email original en el mensaje de Slack?