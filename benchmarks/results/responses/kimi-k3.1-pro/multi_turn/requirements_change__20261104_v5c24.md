# Kimi K3.1 Pro — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 3.71 | quality: 4.0
- latency_total: 204.184s | tokens_per_second: 31.0
- input_tokens: 374 | output_tokens: 6331

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

Perfecto. El flujo quedaría así:

**Gmail Trigger → Preparar y filtrar → Notion → Slack**

Solo los emails que contengan **“propuesta”** o **“cotización”** en el asunto continuarán. El filtro ignorará mayúsculas y acentos, por lo que también detectará `COTIZACION`, `Cotización`, etc.

## 1. Prepara la base de datos de Notion

Crea una base con estas propiedades:

| Propiedad | Tipo en Notion |
|---|---|
| Asunto | Title |
| Remitente | Text |
| Email | Email |
| Recibido | Date |
| Gmail ID | Text |
| Gmail URL | URL |

Después, comparte la base de datos con la integración de Notion que utilizarás en n8n. Este paso es imprescindible para que n8n pueda crear páginas.

## 2. Configura el nodo Gmail Trigger

- **Credential:** tu cuenta de Gmail mediante OAuth2.
- **Event:** `Message Received`.
- **Poll interval:** cada minuto, o la frecuencia que prefieras.
- No configures todavía un filtro por asunto; lo haremos dentro del workflow para controlar correctamente acentos y mayúsculas.

## 3. Añade un nodo Code llamado “Preparar y filtrar”

Selecciona **Mode: Run Once for All Items** y pega este código:

```javascript
const results = [];

for (const item of $input.all()) {
  const data = item.json;
  const rawHeaders = data.payload?.headers ?? data.headers ?? [];
  const headers = Array.isArray(rawHeaders) ? rawHeaders : [];

  const getHeader = (name) =>
    headers.find(
      (h) => h.name?.toLowerCase() === name.toLowerCase()
    )?.value ?? '';

  const subject = String(
    data.Subject ?? data.subject ?? getHeader('Subject') ?? ''
  );

  const from = String(
    data.From ?? data.from ?? getHeader('From') ?? ''
  );

  const dateValue = data.Date ?? data.date ?? getHeader('Date');

  // Normaliza mayúsculas y acentos: "Cotización" → "cotizacion"
  const normalizedSubject = subject
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase();

  // Admite singular y plural
  const matches = /\b(propuestas?|cotizacion(?:es)?)\b/.test(
    normalizedSubject
  );

  // Si no coincide, este email no pasa a Notion ni a Slack
  if (!matches) continue;

  const senderEmail = (
    from.match(/<([^>]+)>/)?.[1] ??
    from.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i)?.[0] ??
    from
  ).trim();

  const senderName = from.includes('<')
    ? from.split('<')[0].trim().replace(/^["']|["']$/g, '')
    : '';

  let receivedAt;

  if (data.internalDate) {
    receivedAt = new Date(Number(data.internalDate)).toISOString();
  } else {
    const parsedDate = new Date(dateValue);
    receivedAt = Number.isNaN(parsedDate.getTime())
      ? new Date().toISOString()
      : parsedDate.toISOString();
  }

  results.push({
    json: {
      gmailId: data.id ?? '',
      threadId: data.threadId ?? '',
      senderName,
      senderEmail,
      subject,
      receivedAt,
      snippet: data.snippet ?? '',
      gmailUrl: data.id
        ? `https://mail.google.com/mail/u/0/#all/${data.id}`
        : ''
    }
  });
}

return results;
```

Si un email no cumple el filtro, el nodo devuelve cero elementos y la ejecución no continúa.

## 4. Guarda los datos en Notion

Añade un nodo **Notion**:

- **Operation:** crear página. Según la versión del nodo, puede aparecer como `Database Page → Create`.
- **Database:** selecciona la base preparada anteriormente.
- Configura las propiedades así:

| Propiedad de Notion | Expresión de n8n |
|---|---|
| Asunto | `{{ $json.subject }}` |
| Remitente | `{{ $json.senderName }}` |
| Email | `{{ $json.senderEmail }}` |
| Recibido | `{{ $json.receivedAt }}` |
| Gmail ID | `{{ $json.gmailId }}` |
| Gmail URL | `{{ $json.gmailUrl }}` |

Para un remitente como `Ana López <ana@empresa.com>`, obtendrás:

- **Remitente:** `Ana López`
- **Email:** `ana@empresa.com`

## 5. Envía la notificación a Slack

Conecta el nodo **Slack** después de Notion:

- **Operation:** `Send Message`.
- **Channel:** por ejemplo, `#ventas`.
- **Text:**

```text
:email: *Nueva oportunidad comercial*

*Remitente:* {{ $('Preparar y filtrar').item.json.senderName || 'Sin nombre' }}
*Email:* {{ $('Preparar y filtrar').item.json.senderEmail }}
*Asunto:* {{ $('Preparar y filtrar').item.json.subject }}

<{{ $('Preparar y filtrar').item.json.gmailUrl }}|Abrir en Gmail>
<{{ $json.url }}|Ver en Notion>
```

La última línea utiliza la URL devuelta por Notion. Si tu versión del nodo no devuelve `$json.url`, puedes eliminarla.

Al colocar Slack después de Notion, la notificación solo se enviará cuando el registro se haya guardado correctamente.

## 6. Prueba el comportamiento

Envía tres correos de prueba:

1. **Asunto:** `Propuesta de servicios` → se guarda y notifica.
2. **Asunto:** `Re: COTIZACIÓN solicitada` → se guarda y notifica.
3. **Asunto:** `Coordinemos una reunión` → se descarta.

Finalmente, **activa el workflow**: el Gmail Trigger no procesará correos nuevos de forma permanente mientras el workflow esté desactivado. Si usas un canal privado de Slack, recuerda invitar también al bot de n8n.