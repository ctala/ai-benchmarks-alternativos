# MiniMax M3.1 Flash — multi_turn/requirements_change

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 4.64 | quality: 4.0
- latency_total: 43.347s | tokens_per_second: 191.0
- input_tokens: 411 | output_tokens: 8280

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

## Estructura del workflow

```text
Gmail Trigger
      ↓
Code: Normalizar y extraer datos
      ↓
IF: ¿El asunto contiene “propuesta” o “cotización”?
      ├── Sí ──→ Notion: Create Page
      │         └→ Slack: Send Message
      └── No ──→ Fin
```

> La rama “Sí” se conecta a Notion y Slack en paralelo. La rama “No” no tiene conexión, por lo que los emails irrelevantes se descartan.

---

## 1. Nodo `Gmail Trigger`

- **Credential:** credencial OAuth de Google con permiso de lectura de Gmail.
- Configura el polling y la etiqueta o bandeja desde la que quieres recibir los emails.
- Si aparece una opción para devolver el contenido o preview del mensaje, actívala para poder guardar también un extracto.

---

## 2. Nodo `Code`: normalizar y extraer

Configúralo en modo **Run Once for All Items** y pega este código:

```javascript
const emails = $input.all();

return emails.map(({ json: email }) => {
  const headers = email.headers ?? {};

  const subject = String(
    email.subject ??
    headers.subject ??
    ''
  );

  const fromRaw =
    email.from ??
    headers.from ??
    email.sender ??
    '';

  let senderName = '';
  let senderEmail = '';

  if (typeof fromRaw === 'string') {
    // Formato: "Nombre <email@example.com>"
    const angleMatch = fromRaw.match(/<([^>]+)>/);

    senderEmail =
      angleMatch?.[1]?.trim() ||
      fromRaw.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i)?.[0] ||
      '';

    senderName = angleMatch
      ? fromRaw
          .slice(0, angleMatch.index)
          .trim()
          .replace(/^["']|["']$/g, '')
      : fromRaw
          .replace(senderEmail, '')
          .replace(/[<>]/g, '')
          .trim();
  } else {
    // Formato de la API de Gmail:
    // { value: [{ emailAddress: { name, address } }] }
    const candidates = Array.isArray(fromRaw?.value)
      ? fromRaw.value
      : fromRaw?.value
        ? [fromRaw.value]
        : [fromRaw];

    const match = candidates.find(
      item => item?.emailAddress?.address || item?.address
    );

    const addressObject = match?.emailAddress ?? match ?? {};

    senderEmail = String(
      addressObject?.address ??
      addressObject?.email ??
      ''
    );

    senderName = String(addressObject?.name ?? '');
  }

  let receivedAt = new Date().toISOString();

  if (email.date) {
    const parsedDate = new Date(email.date);

    if (!Number.isNaN(parsedDate.getTime())) {
      receivedAt = parsedDate.toISOString();
    }
  } else if (email.internalDate) {
    receivedAt = new Date(Number(email.internalDate)).toISOString();
  }

  const rawPreview =
    email.snippet ??
    email.bodyPreview ??
    email.body?.plain ??
    email.body?.text ??
    email.body ??
    '';

  const bodyPreview =
    typeof rawPreview === 'string'
      ? rawPreview.slice(0, 1000)
      : '';

  // Normaliza mayúsculas y acentos.
  // "Cotización" se convierte en "cotizacion".
  const normalizedSubject = subject
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');

  const isRelevant =
    normalizedSubject.includes('propuesta') ||
    normalizedSubject.includes('cotizacion');

  return {
    json: {
      subject,
      senderName,
      senderEmail,
      receivedAt,
      messageId: email.id ?? email.messageId ?? '',
      bodyPreview,
      normalizedSubject,
      isRelevant,
      matchedKeyword: normalizedSubject.includes('propuesta')
        ? 'propuesta'
        : normalizedSubject.includes('cotizacion')
          ? 'cotizacion'
          : ''
    }
  };
});
```

Este filtro no distingue mayúsculas y también acepta **“cotización”** con acento.

---

## 3. Nodo `IF`: comprobar el asunto

Configura la condición:

- **Left Value:** `{{ $json.isRelevant }}`
- **Operator:** `is true`

O, si tu versión de N8N permite una sola expresión:

```javascript
{{ $json.normalizedSubject.includes('propuesta') || $json.normalizedSubject.includes('cotizacion') }}
```

Conecta la salida **True** a Notion y Slack. La salida **False** puede quedarse sin conectar.

> `includes()` también captura “propuestas” y “cotizaciones”. Si necesitas exclusivamente la palabra exacta, puedes cambiarlo por una expresión con `\b(propuesta|cotizacion)\b`.

---

## 4. Nodo `Notion`: crear una página

Primero crea una base de datos en Notion con estas propiedades:

| Propiedad | Tipo en Notion |
|---|---|
| `Asunto` | Title |
| `Remitente` | Rich text |
| `Email` | Email |
| `Fecha` | Date |
| `Extracto` | Rich text |
| `Palabra clave` | Select, opcional |

Después, en N8N:

- **Credential:** conexión OAuth con Notion.
- **Resource/Operation:** `Page` → `Create` o `Create Page`.
- **Parent:** selecciona la base de datos.
- Si Noion no aparece, pega el **Database ID** de la URL de la base de datos.

Mapea las propiedades así:

```text
Asunto:
{{ $json.subject }}

Remitente:
{{ $json.senderName || $json.senderEmail }}

Email:
{{ $json.senderEmail }}

Fecha:
{{ $json.receivedAt }}

Extracto:
{{ $json.bodyPreview }}

Palabra clave:
{{ $json.matchedKeyword }}
```

La conexión OAuth de Notion debe tener acceso a esa base de datos. Para comprobarlo, comparte la base de datos con la integración de Notion utilizada por N8N.

---

## 5. Nodo `Slack`: enviar notificación

- **Credential:** credencial OAuth de Slack o token de bot.
- **Resource:** `Message`.
- **Operation:** `Send`.
- **Channel:** el canal donde quieres recibir las notificaciones, por ejemplo `#ventas`.

En el campo de texto pega:

```text
:gmail: *Nuevo email relevante recibido*

*Asunto:* {{ $json.subject }}
*Remitente:* {{ $json.senderName || $json.senderEmail }}
*Email:* {{ $json.senderEmail }}
*Fecha:* {{ $json.receivedAt }}
```

Para mencionar a una persona concreta, puedes añadir al mensaje su Slack ID:

```text
<@U12345678>
```

---

## Resultado

El workflow hará lo siguiente:

1. Lee cada email nuevo de Gmail.
2. Extrae nombre, email, asunto, fecha y un extracto.
3. Descarta los emails cuyo asunto no contenga `propuesta` o `cotización`.
4. Crea una página en Notion por cada email relevante.
5. Envía una notificación al canal de Slack.

Finalmente, guarda y **activa** el workflow. Si prefieres que Slack notifique únicamente después de que la creación en Notion haya funcionado, conecta Notion → Slack y usa en Slack las expresiones `$('Code: Normalizar y extraer datos').item.json...`.