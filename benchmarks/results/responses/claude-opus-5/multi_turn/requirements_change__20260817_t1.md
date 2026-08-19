# Claude Opus 5 — multi_turn/requirements_change

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.27 | quality: 6.0
- latency_total: 34.241s | tokens_per_second: 70.7
- input_tokens: 363 | output_tokens: 2421

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

Buen cambio — Notion es mejor que Sheets para este caso porque cada propuesta queda como una página donde podés agregar seguimiento después.

El workflow queda así:

```
Gmail Trigger → IF (filtro asunto) → Code (extraer datos) → Notion (crear página) → Slack (notificar)
```

## 1. Gmail Trigger

Acá tenés un atajo importante: **filtrá directo en el trigger** en vez de traer todos los emails y descartarlos después. Gmail soporta su sintaxis de búsqueda en el campo de query.

- **Poll Times**: cada 5 o 15 minutos (según urgencia real)
- **Filters → Search**: `subject:(propuesta OR cotizacion)`
- **Simplify**: activado (te devuelve el payload limpio)

Con esto Gmail ya te entrega solo lo que te interesa y ahorrás ejecuciones.

## 2. Nodo IF (red de seguridad opcional)

El search de Gmail a veces es generoso con variantes (busca "cotizaciones", acentos, etc.). Si querés control estricto, agregá un IF:

- **Condition**: String → Matches Regex
- **Value 1**: `{{ $json.subject }}`
- **Value 2**: `(?i)(propuesta|cotizaci[oó]n)`

El `(?i)` hace la comparación case-insensitive y `[oó]` cubre el acento.

Si el search del trigger te funciona bien en la práctica, podés saltear este nodo.

## 3. Code node — extraer remitente

Gmail te devuelve el `from` en formato `"Juan Pérez" <juan@empresa.com>`. Este código lo separa:

```javascript
const items = [];

for (const item of $input.all()) {
  const from = item.json.from || '';
  
  // Separa nombre y email
  const match = from.match(/^(.*?)\s*<(.+?)>$/);
  const nombre = match ? match[1].replace(/"/g, '').trim() : '';
  const email = match ? match[2].trim() : from.trim();
  
  // Dominio, útil para identificar la empresa
  const dominio = email.split('@')[1] || '';
  
  items.push({
    json: {
      nombre: nombre || email.split('@')[0],
      email: email,
      dominio: dominio,
      asunto: item.json.subject || '(sin asunto)',
      fecha: item.json.date,
      snippet: (item.json.snippet || '').substring(0, 300),
      threadId: item.json.threadId,
      gmailLink: `https://mail.google.com/mail/u/0/#inbox/${item.json.threadId}`,
    }
  });
}

return items;
```

Dos detalles que agregué y te van a servir:

- **`dominio`**: te permite agrupar por empresa en Notion sin trabajo extra
- **`gmailLink`**: link directo al thread, así desde Notion abrís el email original con un clic

## 4. Notion node

Primero armá la base de datos en Notion con estas propiedades:

| Propiedad | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Empresa | Text |
| Asunto | Text |
| Fecha recibido | Date |
| Estado | Select (Nueva / En revisión / Respondida / Cerrada) |
| Resumen | Text |
| Link Gmail | URL |

Configuración del nodo:

- **Resource**: Database Page
- **Operation**: Create
- **Database ID**: seleccionás de la lista
- **Properties**:

```
Nombre (title)        → {{ $json.nombre }}
Email (email)         → {{ $json.email }}
Empresa (rich_text)   → {{ $json.dominio }}
Asunto (rich_text)    → {{ $json.asunto }}
Fecha recibido (date) → {{ $json.fecha }}
Estado (select)       → Nueva
Resumen (rich_text)   → {{ $json.snippet }}
Link Gmail (url)      → {{ $json.gmailLink }}
```

⚠️ Antes de que funcione: en Notion tenés que compartir la base de datos con tu integración. Abrí la DB → menú `···` → *Connections* → *Connect to* → tu integración. Si te salta un error 404 en n8n, casi siempre es esto.

## 5. Slack node

- **Resource**: Message
- **Operation**: Send
- **Send To**: Channel (ej. `#ventas`)
- **Message Type**: Block Kit o texto simple

Versión texto simple:

```
📬 *Nueva propuesta recibida*

*De:* {{ $json.nombre }} ({{ $json.email }})
*Empresa:* {{ $json.dominio }}
*Asunto:* {{ $json.asunto }}

<{{ $json.gmailLink }}|Ver email> · <{{ $('Notion').item.json.url }}|Ver en Notion>
```

El `$('Notion').item.json.url` toma el link de la página recién creada, así desde Slack vas directo al registro.

## Cosas a tener en cuenta

**Duplicados.** El Gmail Trigger marca lo procesado, pero si volvés a activar el workflow tras un rato inactivo puede reprocesar. Si te pasa, agregá antes de Notion un nodo Notion → *Get Many* con filtro por `threadId` y un IF que corte si ya existe.

**Múltiples emails por ejecución.** Si llegan 3 emails juntos, el Code node devuelve 3 items y los nodos siguientes corren 3 veces. Eso es lo que querés, pero significa 3 mensajes a Slack. Si preferís un resumen agrupado, avisame y lo armamos distinto.

**Testing.** Antes de activarlo, usá *Execute Workflow* con el trigger en modo manual y mandate un email de prueba con "cotización" en el asunto. Así validás el mapeo de propiedades sin ensuciar la base.

¿Querés que agreguemos algo para clasificar automáticamente por tipo o urgencia? Con un nodo de IA analizando el cuerpo del email podrías llenar el campo Estado o agregar un score de prioridad.