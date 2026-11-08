# GPT-6.1 Sol — multi_turn/requirements_change

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 5.61 | quality: 6.0
- latency_total: 14.761s | tokens_per_second: 69.2
- input_tokens: 226 | output_tokens: 1022

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

¡Perfecto! Sustituimos Google Sheets por Notion y añadimos el filtro y la notificación:

```text
Gmail Trigger → IF: asunto válido → Preparar datos → Notion → Slack
                       └─ No → finalizar
```

### 1. Gmail Trigger: detectar correos nuevos
- Conecta tu cuenta de Gmail.
- Configura el evento de mensaje recibido y la frecuencia de revisión.
- Si solo quieres procesar la bandeja de entrada, limita la búsqueda a `in:inbox`.

### 2. IF: filtrar por asunto
Añade una condición de tipo **Boolean**, con esta expresión:

```javascript
{{ /propuesta|cotizaci[oó]n/i.test($json.subject ?? $json.Subject ?? '') }}
```

Selecciona **is true** y conecta únicamente la salida **true** al siguiente nodo.

Esto acepta asuntos como:
- “Nueva propuesta comercial”
- “Solicitud de cotizacion”
- “COTIZACIÓN de servicios”

También contempla mayúsculas y la tilde en “cotización”.

> Ejecuta una prueba del Gmail Trigger para confirmar que el asunto aparece como `subject` o `Subject`. Si tu salida tiene otra estructura, ajusta la expresión.

### 3. Preparar datos: separar nombre y email
Añade un nodo **Code**, en modo **Run Once for Each Item**, con este código:

```javascript
const j = $json;

// Admite remitentes en texto o en formato estructurado.
const from = j.from ?? j.From ?? '';
const address = from?.value?.[0];

const raw = typeof from === 'string'
  ? from
  : (from?.text ?? '');

const match = raw.match(/^\s*(.*?)\s*<([^>]+)>/);

const nombre = address?.name
  || (match ? match[1].replace(/^"|"$/g, '').trim() : '');

const email = address?.address
  || (match ? match[2].trim() : raw.trim());

const rawDate = j.date ?? j.internalDate;
const fecha = rawDate
  ? new Date(/^\d+$/.test(String(rawDate)) ? Number(rawDate) : rawDate)
  : null;

return {
  json: {
    nombre,
    email,
    asunto: j.subject ?? j.Subject ?? '',
    fecha: fecha && !isNaN(fecha.getTime()) ? fecha.toISOString() : null,
    gmailId: j.id ?? '',
  },
};
```

### 4. Notion: crear un registro
Crea una base de datos en Notion con estas propiedades:

| Propiedad | Tipo | Valor desde “Preparar datos” |
|---|---|---|
| Asunto | Título | `asunto` |
| Nombre | Texto | `nombre` |
| Email | Email | `email` |
| Fecha | Fecha | `fecha` |
| Gmail ID | Texto | `gmailId` |

En el nodo **Notion**, selecciona la operación para **crear una página en una base de datos** y mapea las propiedades.

**Importante:** comparte la base de datos con tu integración de Notion. Sin ese permiso, n8n no podrá escribir en ella. Si `fecha` está vacía, omite esa propiedad.

### 5. Slack: enviar una notificación
Conecta un nodo **Slack** después de Notion y selecciona el canal de destino. Así, la notificación se envía cuando el registro ya se ha creado.

Mensaje sugerido:

```text
📩 Nuevo correo comercial guardado en Notion

Remitente: {{ $('Preparar datos').item.json.nombre }}
Email: {{ $('Preparar datos').item.json.email }}
Asunto: {{ $('Preparar datos').item.json.asunto }}
```

Pon al nodo Code el nombre **Preparar datos** para que esas referencias funcionen.

**Recomendación para producción:** usa `Gmail ID` para comprobar si el correo ya existe en Notion antes de crearlo. Esto evita registros y avisos duplicados si vuelves a ejecutar un correo.