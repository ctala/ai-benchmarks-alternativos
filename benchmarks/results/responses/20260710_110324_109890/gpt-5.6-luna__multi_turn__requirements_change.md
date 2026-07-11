# GPT-5.6 Luna — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 4.85 | quality: 4.72
- latency_total: 14.297s | tokens_per_second: 134.1
- input_tokens: 226 | output_tokens: 1917
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en Google Sheets, en su lugar sugiere Notion y Slack, lo que la hace irrelevante y poco precisa.

## Respuesta completa

Puedes montar este workflow:

```text
Gmail Trigger
   ↓
IF: asunto contiene “propuesta” o “cotización”
   ↓
Code: extraer remitente y normalizar datos
   ↓
Notion: crear página en una base de datos
   ↓
Slack: enviar notificación
```

## 1. Gmail Trigger

Configura las credenciales de Gmail y usa una búsqueda como:

```text
in:anywhere {subject:propuesta subject:cotizacion subject:cotización}
```

Esto reduce el número de emails procesados desde el inicio. Aun así, conviene mantener el nodo `IF` como segunda validación.

Si tu versión de n8n no tiene campo de búsqueda en `Gmail Trigger`, déjalo escuchando emails nuevos y aplica el filtro en el siguiente nodo.

## 2. Nodo IF

Añade un nodo **IF** después del trigger.

Configura una condición de tipo **Expression**:

```javascript
{{
  (() => {
    const subject = String(
      $json.subject ||
      $json.payload?.headers?.find(h => h.name?.toLowerCase() === 'subject')?.value ||
      ''
    ).toLowerCase();

    return subject.includes('propuesta') ||
           subject.includes('cotizacion') ||
           subject.includes('cotización');
  })()
}}
```

La salida `true` continuará hacia Notion y Slack. La salida `false` puede quedar sin conectar.

## 3. Nodo Code: extraer datos del remitente

Añade un nodo **Code** en modo `Run Once for All Items` con este código:

```javascript
return items.map(item => {
  const data = item.json;

  const headers =
    data.payload?.headers ||
    data.headers ||
    [];

  function getHeader(name) {
    const header = headers.find(
      h => String(h.name || '').toLowerCase() === name.toLowerCase()
    );

    return header?.value || '';
  }

  const rawFrom =
    getHeader('From') ||
    data.from ||
    data.sender ||
    '';

  const rawSubject =
    getHeader('Subject') ||
    data.subject ||
    '';

  const rawDate =
    getHeader('Date') ||
    data.internalDate ||
    new Date().toISOString();

  let senderName = '';
  let senderEmail = '';

  if (typeof rawFrom === 'object') {
    senderName = rawFrom.name || '';
    senderEmail = rawFrom.email || rawFrom.address || '';
  } else {
    const fromText = String(rawFrom);

    const match = fromText.match(/^(.*?)\s*<([^>]+)>$/);

    if (match) {
      senderName = match[1].replace(/^["']|["']$/g, '').trim();
      senderEmail = match[2].trim();
    } else {
      senderEmail = fromText.trim();
    }
  }

  return {
    json: {
      senderName,
      senderEmail,
      subject: String(rawSubject),
      receivedAt: rawDate,
      gmailId: data.id || '',
      threadId: data.threadId || '',
      snippet: data.snippet || ''
    }
  };
});
```

El resultado tendrá estos campos:

```text
senderName
senderEmail
subject
receivedAt
gmailId
threadId
snippet
```

## 4. Crear la base de datos en Notion

Crea una base de datos en Notion con estas propiedades:

| Propiedad | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Text |
| Fecha | Date |
| Gmail ID | Text |
| Thread ID | Text |
| Extracto | Text |

Comparte la base de datos con la integración de Notion que utilizarás en n8n:

1. Abre la base de datos en Notion.
2. Ve a **Share**.
3. Añade tu integración.
4. En n8n, crea las credenciales de Notion.

## 5. Nodo Notion

Añade un nodo:

```text
Notion → Database Page → Create
```

Selecciona tu base de datos y asigna las propiedades:

### Nombre

```javascript
{{ $json.senderName || $json.senderEmail }}
```

### Email

```javascript
{{ $json.senderEmail }}
```

### Asunto

```javascript
{{ $json.subject }}
```

### Fecha

Si la propiedad de Notion es de tipo fecha:

```javascript
{{ new Date($json.receivedAt).toISOString() }}
```

### Gmail ID

```javascript
{{ $json.gmailId }}
```

### Thread ID

```javascript
{{ $json.threadId }}
```

### Extracto

```javascript
{{ $json.snippet }}
```

El nombre exacto de cada propiedad debe coincidir con el nombre configurado en la base de datos de Notion.

## 6. Nodo Slack

Después del nodo de Notion, añade:

```text
Slack → Message → Send
```

Selecciona el canal y utiliza un mensaje como:

```text
📩 Nuevo email relevante recibido

👤 Remitente: {{ $('Code').item.json.senderName || 'Sin nombre' }}
✉️ Email: {{ $('Code').item.json.senderEmail }}
📝 Asunto: {{ $('Code').item.json.subject }}
📅 Fecha: {{ $('Code').item.json.receivedAt }}

El email fue guardado en Notion.
```

Si el nodo Code tiene otro nombre, reemplaza `Code` por el nombre real del nodo.

## Orden recomendado

```text
Gmail Trigger
  → IF
  → Code - Extraer datos
  → Notion - Crear página
  → Slack - Notificar
```

Colocar Slack después de Notion garantiza que la notificación solo se envíe cuando el registro se haya creado correctamente en Notion.