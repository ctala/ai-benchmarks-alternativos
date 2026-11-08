# GPT-5.6 Sol — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 4.28 | quality: 4.0
- latency_total: 14.012s | tokens_per_second: 112.5
- input_tokens: 226 | output_tokens: 1577

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

Claro. El workflow quedaría así:

**Gmail Trigger → Code (extraer/filtrar) → IF → Notion → Slack**

## 1. Gmail Trigger

Añade un nodo **Gmail Trigger**:

- Conecta tus credenciales de Gmail.
- Evento: **Message Received**
- Activa **Simplify**, si está disponible.
- En el filtro de búsqueda usa:

```text
{subject:propuesta subject:cotizacion subject:"cotización"}
```

Esto reduce los correos procesados. Aun así, añadiremos una validación dentro de n8n para asegurar el filtrado.

---

## 2. Code: extraer los datos del correo

Añade un nodo **Code** y pega:

```javascript
const headers = $json.payload?.headers || [];

const getHeader = (name) =>
  headers.find(h => h.name?.toLowerCase() === name.toLowerCase())?.value;

const subject = $json.subject || getHeader('Subject') || '';
const from = $json.from || getHeader('From') || '';
const rawDate = $json.date || getHeader('Date') || new Date().toISOString();

// Normaliza acentos y mayúsculas
const normalizedSubject = subject
  .normalize('NFD')
  .replace(/[\u0300-\u036f]/g, '')
  .toLowerCase();

const isRelevant =
  normalizedSubject.includes('propuesta') ||
  normalizedSubject.includes('cotizacion');

// Extraer email y nombre del remitente
const emailMatch = from.match(/<([^>]+)>/) || from.match(/[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}/);
const email = emailMatch ? emailMatch[1] || emailMatch[0] : '';

const senderName = from
  .replace(/<[^>]+>/, '')
  .replace(email, '')
  .replace(/^["']|["']$/g, '')
  .trim();

const messageId = $json.id || $json.messageId || '';
const threadId = $json.threadId || messageId;

return [{
  json: {
    isRelevant,
    senderName: senderName || email,
    senderEmail: email,
    subject,
    receivedAt: new Date(rawDate).toISOString(),
    messageId,
    threadId,
    snippet: $json.snippet || $json.textPlain || '',
    gmailUrl: threadId
      ? `https://mail.google.com/mail/u/0/#inbox/${threadId}`
      : ''
  }
}];
```

Este nodo también reconoce **“cotización”** con tilde.

---

## 3. IF: validar el asunto

Añade un nodo **IF**:

- Valor 1:

```text
{{ $json.isRelevant }}
```

- Operación: **is true**

Continúa el workflow únicamente desde la salida **true**.

---

## 4. Preparar la base de datos en Notion

Crea una base de datos con estas propiedades:

| Propiedad | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Rich text |
| Fecha | Date |
| Gmail ID | Rich text |
| Enlace | URL |
| Extracto | Rich text |

Crea una integración en Notion, copia su token y comparte la base de datos con esa integración.

---

## 5. Notion: crear el registro

Añade un nodo **Notion**:

- Resource: **Database Page**
- Operation: **Create**
- Selecciona la base de datos.

Mapea las propiedades:

- **Nombre**

```text
{{ $json.senderName }}
```

- **Email**

```text
{{ $json.senderEmail }}
```

- **Asunto**

```text
{{ $json.subject }}
```

- **Fecha**

```text
{{ $json.receivedAt }}
```

- **Gmail ID**

```text
{{ $json.messageId }}
```

- **Enlace**

```text
{{ $json.gmailUrl }}
```

- **Extracto**

```text
{{ $json.snippet }}
```

---

## 6. Slack: enviar la notificación

Conecta un nodo **Slack** después de Notion:

- Resource: **Message**
- Operation: **Send**
- Selecciona el canal.
- Mensaje:

```text
📩 Nueva propuesta o cotización

*Remitente:* {{ $('Code').item.json.senderName }}
*Email:* {{ $('Code').item.json.senderEmail }}
*Asunto:* {{ $('Code').item.json.subject }}
*Fecha:* {{ $('Code').item.json.receivedAt }}
*Abrir en Gmail:* {{ $('Code').item.json.gmailUrl }}
```

La referencia `$('Code')` debe coincidir con el nombre real de tu nodo Code. Si lo llamas **Extraer datos**, utiliza:

```text
{{ $('Extraer datos').item.json.subject }}
```

Con esta estructura, Slack solo notificará si el correo cumple el filtro y se guardó correctamente en Notion.