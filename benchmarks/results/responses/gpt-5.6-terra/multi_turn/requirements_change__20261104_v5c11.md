# GPT-5.6 Terra — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 4.14 | quality: 4.0
- latency_total: 22.311s | tokens_per_second: 119.8
- input_tokens: 226 | output_tokens: 2673

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

Puedes montar este workflow:

```text
Gmail Trigger
   ↓
Code / Preparar datos del email
   ↓
IF / ¿Asunto contiene “propuesta” o “cotización”?
   ├─ No → Termina
   └─ Sí
        ↓
     Notion / Crear página en base de datos
        ↓
     Slack / Enviar notificación
```

## 1. Gmail Trigger

Añade un nodo **Gmail Trigger**.

Configuración recomendada:

- **Event**: `Message Received`
- Conecta tus credenciales de Gmail.
- Opcionalmente, si el nodo muestra un campo de búsqueda o *Search Query*, puedes añadir:

```text
subject:(propuesta OR cotizacion OR cotización)
```

Aun así, mantén el filtro con el nodo **IF**, porque así controlas mejor mayúsculas, acentos y variaciones del asunto.

---

## 2. Nodo Code: preparar y extraer los datos

Añade un nodo **Code** después de Gmail Trigger y llámalo, por ejemplo:

```text
Preparar datos
```

Configúralo como **Run Once for All Items** y usa este código:

```javascript
function getHeader(item, headerName) {
  const headers = item.headers || item.payload?.headers || [];
  const target = headerName.toLowerCase();

  // Si Gmail devuelve headers como array
  if (Array.isArray(headers)) {
    const header = headers.find(
      (h) => (h.name || '').toLowerCase() === target
    );
    if (header) return header.value || '';
  }

  // Si Gmail devuelve headers como objeto
  if (headers && typeof headers === 'object') {
    const key = Object.keys(headers).find(
      (k) => k.toLowerCase() === target
    );
    if (key) return headers[key] || '';
  }

  return '';
}

function extractSender(from) {
  // Ejemplo: "Juan Pérez <juan@empresa.com>"
  const match = from.match(/^\s*"?([^"<]*)"?\s*<([^>]+)>\s*$/);

  if (match) {
    return {
      nombre: match[1].trim() || match[2].trim(),
      email: match[2].trim(),
    };
  }

  // Si Gmail devuelve directamente el email
  return {
    nombre: from.trim(),
    email: from.trim(),
  };
}

return $input.all().map((item) => {
  const data = item.json;

  const from =
    data.from ||
    data.From ||
    getHeader(data, 'From') ||
    '';

  const subject =
    data.subject ||
    data.Subject ||
    getHeader(data, 'Subject') ||
    '';

  const date =
    data.date ||
    data.Date ||
    getHeader(data, 'Date') ||
    '';

  const sender = extractSender(from);

  // Normaliza acentos y mayúsculas:
  // "Cotización", "COTIZACION" y "cotizacion" coincidirán.
  const normalizedSubject = subject
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase();

  const coincideFiltro =
    normalizedSubject.includes('propuesta') ||
    normalizedSubject.includes('cotizacion');

  let fechaISO = null;

  if (date) {
    const parsedDate = new Date(date);
    if (!isNaN(parsedDate.getTime())) {
      fechaISO = parsedDate.toISOString();
    }
  }

  return {
    json: {
      ...data,
      remitenteNombre: sender.nombre,
      remitenteEmail: sender.email,
      asunto: subject,
      fechaEmail: fechaISO,
      mensajeId: data.id || data.messageId || '',
      coincideFiltro,
    },
  };
});
```

Este nodo deja los datos preparados así:

```json
{
  "remitenteNombre": "Juan Pérez",
  "remitenteEmail": "juan@empresa.com",
  "asunto": "Propuesta comercial para su empresa",
  "fechaEmail": "2025-01-15T10:30:00.000Z",
  "mensajeId": "..."
}
```

---

## 3. Nodo IF: filtrar propuestas y cotizaciones

Añade un nodo **IF** después de `Preparar datos`.

Configuración:

- Condición: **Boolean**
- Valor 1:

```text
{{ $json.coincideFiltro }}
```

- Operación: `is true`

Conecta únicamente la salida **true** al resto del flujo.

Así se ignorarán todos los emails cuyo asunto no contenga:

- `propuesta`
- `cotización`
- `cotizacion`

Sin importar mayúsculas o acentos.

---

## 4. Preparar la base de datos de Notion

En Notion crea una base de datos, por ejemplo llamada:

```text
Leads desde Gmail
```

Crea estas propiedades:

| Propiedad en Notion | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Text / Rich Text |
| Fecha del email | Date |
| ID Gmail | Text / Rich Text |

> `Nombre` debe ser de tipo **Title**, porque Notion requiere una propiedad principal de ese tipo.

---

## 5. Nodo Notion: crear un registro

Añade un nodo **Notion** conectado a la salida `true` del nodo IF.

Según la versión de n8n, selecciona algo equivalente a:

- **Resource**: `Database Page` o `Page`
- **Operation**: `Create`
- Selecciona tu base de datos: `Leads desde Gmail`

Mapea las propiedades así:

### Nombre

```text
{{ $json.remitenteNombre || $json.remitenteEmail }}
```

### Email

```text
{{ $json.remitenteEmail }}
```

### Asunto

```text
{{ $json.asunto }}
```

### Fecha del email

```text
{{ $json.fechaEmail }}
```

### ID Gmail

```text
{{ $json.mensajeId }}
```

Con esto, cada email filtrado generará una nueva página/registro en tu base de datos de Notion.

---

## 6. Nodo Slack: notificar cuando llegue un email relevante

Después del nodo Notion añade un nodo **Slack**.

Configuración:

- **Resource**: `Message`
- **Operation**: `Send`
- Selecciona el canal, por ejemplo:

```text
#nuevas-propuestas
```

En el campo **Text** puedes usar este mensaje:

```text
:nueva: *Nueva propuesta o cotización recibida*

*Remitente:* {{ $('Preparar datos').item.json.remitenteNombre }}
*Email:* {{ $('Preparar datos').item.json.remitenteEmail }}
*Asunto:* {{ $('Preparar datos').item.json.asunto }}
*Fecha:* {{ $('Preparar datos').item.json.fechaEmail }}

El contacto ya fue guardado en Notion.
```

El uso de:

```text
$('Preparar datos').item.json...
```

permite recuperar los datos originales incluso después de que Notion haya creado la página.

---

## Recomendación adicional: evitar duplicados

Si el workflow pudiera procesar el mismo correo más de una vez, usa `mensajeId` como identificador único.

Antes de crear la página en Notion puedes añadir:

1. Un nodo **Notion - Search**
2. Buscar por la propiedad `ID Gmail`
3. Un nodo **IF**
   - Si no existe: crear página y enviar Slack.
   - Si ya existe: terminar el flujo.

Así evitas crear contactos duplicados y enviar notificaciones repetidas.