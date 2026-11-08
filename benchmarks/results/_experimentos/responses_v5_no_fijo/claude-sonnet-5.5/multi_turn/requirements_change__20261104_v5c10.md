# Claude Sonnet 5.5 — multi_turn/requirements_change

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 4.22 | quality: 4.0
- latency_total: 15.03s | tokens_per_second: 142.2
- input_tokens: 365 | output_tokens: 2137

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

Entendido. El flujo queda así:

```
Gmail Trigger → IF (filtro) → Code (extraer datos) → Notion → Slack
```

## 1. Gmail Trigger
- **Event**: Message Received
- **Poll Time**: cada minuto, o lo que prefieras
- **Simplify**: desactívalo si quieres los datos del remitente ya parseados. Si lo dejas activo, el campo `From` llega como texto (`Nombre <email@dominio.com>`) y lo parseamos en el paso 3.
- Opcional: en *Filters* puedes limitar a una etiqueta, por ejemplo Inbox.

## 2. IF (filtro por asunto)
- **Value 1**: `{{ $json.Subject || $json.subject }}`
- **Operación**: String → *Matches Regex*
- **Value 2**: `propuesta|cotizaci[oó]n`
- **Flags**: activa *Ignore Case*

Esto cubre mayúsculas/minúsculas y las variantes "cotizacion" y "cotización". Solo la salida *true* continúa.

## 3. Code (extraer datos del remitente)
Modo: *Run Once for Each Item*

```javascript
const from = $json.From || $json.from?.text || '';
const subject = $json.Subject || $json.subject || '';
const date = $json.date || $json.Date || new Date().toISOString();

// Parsea "Nombre <email@dominio.com>"
const match = from.match(/^(.*?)\s*<(.+?)>$/);
const nombre = match ? match[1].replace(/"/g, '').trim() : from;
const email = match ? match[2].trim() : from;

return {
  json: {
    nombre: nombre || email,
    email,
    asunto: subject,
    fecha: new Date(date).toISOString(),
    snippet: $json.snippet || ''
  }
};
```

## 4. Notion
Antes de configurar el nodo:
1. Crea una base de datos con estas propiedades: **Nombre** (Title), **Email** (Email), **Asunto** (Text), **Fecha** (Date).
2. En Notion, ve a `···` → *Connections* y conecta tu integración con la base de datos.
3. En N8N, crea la credencial con el token de la integración.

Configuración del nodo:
- **Resource**: Database Page
- **Operation**: Create
- **Database**: selecciónala de la lista
- **Properties**:
  - Nombre → `{{ $json.nombre }}`
  - Email → `{{ $json.email }}`
  - Asunto → `{{ $json.asunto }}`
  - Fecha → `{{ $json.fecha }}`

## 5. Slack
- **Resource**: Message → **Send**
- **Channel**: el canal que quieras, por ejemplo `#ventas`
- **Text**:
```
📩 *Nuevo email relevante*
*De:* {{ $('Code').item.json.nombre }} ({{ $('Code').item.json.email }})
*Asunto:* {{ $('Code').item.json.asunto }}
```
Ajusta `'Code'` al nombre real de tu nodo. Si quieres incluir el enlace a la página de Notion, puedes usar `{{ $json.url }}`, que devuelve el nodo de Notion.

## Recomendaciones
- **Verifica los nombres de campos**: ejecuta el trigger una vez y revisa el output, porque según la versión del nodo y la opción *Simplify* pueden cambiar (`Subject` vs `subject`). El código ya contempla ambos casos.
- **Evita duplicados**: si el polling puede reprocesar emails, guarda el ID del mensaje en una propiedad de Notion y búscalo antes de crear.
- **Manejo de errores**: crea un workflow de *Error Trigger* que te avise por Slack si algo falla.

¿Quieres que te prepare el JSON completo para importarlo directamente en N8N?