# Claude Opus 5 — multi_turn/requirements_change

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.3 | quality: 6.0
- latency_total: 28.97s | tokens_per_second: 70.7
- input_tokens: 363 | output_tokens: 2048

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

Buen cambio — Notion es mejor idea si vas a hacer seguimiento de propuestas. Te dejo el diseño completo.

## Estructura final del workflow

```
Gmail Trigger → Filter (asunto) → Code (parsear remitente) → Notion (crear página) → Slack (notificar)
```

---

## 1. Gmail Trigger

**Importante**: filtra desde acá, no después. Gmail hace el filtro en su servidor y te ahorra ejecuciones.

- **Poll Times**: cada 5 o 15 minutos (evitá "cada minuto", consume ejecuciones al vacío)
- **Simplify**: `false` ← esto es clave, si lo dejás en `true` no te llega el body ni todos los headers
- **Filters → Search**: 
  ```
  subject:(propuesta OR cotizacion OR cotización) -in:spam
  ```

Notas sobre esto:
- Gmail normalmente ignora acentos en la búsqueda, pero incluí ambas variantes por seguridad
- Si querés solo emails no leídos, agregá `is:unread`
- Si querés excluir tus propios envíos: `-from:me`

---

## 2. Filter (red de seguridad)

Gmail a veces matchea la palabra en el cuerpo del email, no solo en el asunto. Este nodo lo corrige.

Usá un nodo **Filter** con condición String → *matches regex*:

- **Value 1**: `{{ $json.subject }}`
- **Value 2**: `(?i)(propuesta|cotizaci[oó]n)`

El `(?i)` lo hace insensible a mayúsculas. Así "PROPUESTA" y "Propuesta" pasan igual.

---

## 3. Code (parsear remitente)

El header `From` viene como `Juan Pérez <juan@empresa.com>`, hay que separarlo.

```javascript
const items = [];

for (const item of $input.all()) {
  const from = item.json.from?.value?.[0] 
    || item.json.From 
    || item.json.from 
    || '';

  let nombre = '';
  let email = '';

  if (typeof from === 'object') {
    nombre = from.name || '';
    email = from.address || '';
  } else {
    const match = String(from).match(/^\s*"?([^"<]*)"?\s*<?([^<>\s]+@[^<>\s]+)>?/);
    nombre = match ? match[1].trim() : '';
    email = match ? match[2].trim() : String(from).trim();
  }

  if (!nombre) nombre = email.split('@')[0];

  items.push({
    json: {
      nombre,
      email,
      dominio: email.split('@')[1] || '',
      asunto: item.json.subject || '(sin asunto)',
      fecha: new Date(item.json.date || Date.now()).toISOString(),
      snippet: (item.json.snippet || '').substring(0, 300),
      messageId: item.json.id || '',
      threadId: item.json.threadId || ''
    }
  });
}

return items;
```

El `dominio` te sirve después para agrupar por empresa en Notion.

---

## 4. Notion

Antes de configurar el nodo, creá la base de datos en Notion con estas propiedades **con estos nombres exactos** (si no coinciden, el nodo devuelve error 400):

| Propiedad | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Rich text |
| Fecha | Date |
| Dominio | Rich text |
| Resumen | Rich text |
| Estado | Select (opciones: Nueva, En revisión, Respondida, Descartada) |
| Message ID | Rich text |

**Configuración del nodo:**
- **Resource**: Database Page
- **Operation**: Create
- **Database ID**: seleccioná de la lista
- **Properties** (agregá una por una):

| Key | Type | Value |
|---|---|---|
| Nombre | Title | `{{ $json.nombre }}` |
| Email | Email | `{{ $json.email }}` |
| Asunto | Rich Text | `{