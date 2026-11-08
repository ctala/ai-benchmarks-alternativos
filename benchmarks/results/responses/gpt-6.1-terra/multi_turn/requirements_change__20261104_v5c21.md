# GPT-6.1 Terra — multi_turn/requirements_change

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 5.7 | quality: 6.0
- latency_total: 14.955s | tokens_per_second: 85.9
- input_tokens: 226 | output_tokens: 1284

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

Sí. El flujo actualizado sería:

**Gmail Trigger → Extraer datos → Filtrar asunto → Crear página en Notion → Notificar en Slack**

### 1. Gmail Trigger

- Conecta tu cuenta de Gmail.
- Configura el evento para detectar **mensajes nuevos**.
- Activa la salida simplificada si tu versión de n8n ofrece esa opción.

Este trigger procesará los correos nuevos; no importa automáticamente el historial.

### 2. Code: extraer datos

Añade un nodo **Code** después del trigger, en modo **Run Once for Each Item**, con este código:

```javascript
const correo = $json;

function header(nombre) {
  const headers = correo.payload?.headers ?? correo.headers;

  if (Array.isArray(headers)) {
    return headers.find(
      h => h.name?.toLowerCase() === nombre.toLowerCase()
    )?.value;
  }

  return headers?.[nombre] ?? headers?.[nombre.toLowerCase()];
}

const remitenteOriginal =
  correo.From ?? correo.from?.text ?? correo.from ?? header('From') ?? '';

const remitente = String(remitenteOriginal);
const email = remitente.match(/[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}/)?.[0] ?? '';
const nombre = remitente.includes('<')
  ? remitente.split('<')[0].trim().replace(/^"|"$/g, '')
  : '';

const asunto = correo.Subject ?? correo.subject ?? header('Subject') ?? '';
const fechaOriginal = correo.Date ?? correo.date ?? header('Date');
const fecha = fechaOriginal
  ? new Date(fechaOriginal)
  : new Date(Number(correo.internalDate));

return {
  json: {
    nombre,
    email,
    asunto,
    fecha: Number.isNaN(fecha.getTime()) ? null : fecha.toISOString(),
    gmailId: correo.id ?? ''
  }
};
```

Los campos exactos que entrega Gmail pueden variar según la versión y la configuración del nodo. Ejecuta una prueba y revisa la salida si algún campo aparece vacío.

### 3. IF: filtrar asuntos

Añade un nodo **IF** con una condición booleana:

```javascript
{{ /\b(?:propuesta|cotizaci[oó]n)\b/i.test($json.asunto || '') }}
```

Configura la condición como **is true**. La rama verdadera continuará solo para asuntos que contengan la palabra `propuesta`, `cotizacion` o `cotización`, sin distinguir mayúsculas.

### 4. Notion: crear registro

Crea una base de datos en Notion con estas propiedades:

| Propiedad | Tipo |
|---|---|
| Asunto | Title |
| Remitente | Text |
| Email | Email |
| Fecha | Date |
| Gmail ID | Text |

Después, añade un nodo **Notion** para crear una página en esa base de datos y mapea:

- **Asunto:** `{{ $json.asunto }}`
- **Remitente:** `{{ $json.nombre }}`
- **Email:** `{{ $json.email }}`
- **Fecha:** `{{ $json.fecha }}`
- **Gmail ID:** `{{ $json.gmailId }}`

Conecta tu integración de Notion y dale acceso a la base de datos.

### 5. Slack: enviar notificación

Añade un nodo **Slack** después de Notion, selecciona **Send Message** y el canal deseado. Puedes usar este mensaje:

```text
📩 Nuevo correo de propuesta o cotización

De: {{ $('Code').item.json.nombre }} <{{ $('Code').item.json.email }}>
Asunto: {{ $('Code').item.json.asunto }}
Fecha: {{ $('Code').item.json.fecha }}
```

Sustituye `Code` por el nombre real de tu nodo de extracción. Asegúrate de que la app de Slack tenga permiso para publicar en el canal.

**Nota:** con este orden, Slack solo notificará si el registro en Notion se crea correctamente. Prueba el flujo con un correo cuyo asunto sea, por ejemplo, “Propuesta comercial” y luego actívalo.