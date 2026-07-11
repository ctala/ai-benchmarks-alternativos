# GPT-5.6 Sol — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 5.66 | quality: 6.88
- latency_total: 56.98s | tokens_per_second: 24.1
- input_tokens: 226 | output_tokens: 1372
- judge_score: 3.6 | justificación: 

## Respuesta completa

Claro. El workflow quedaría así:

```text
Gmail Trigger
   ↓
Extraer y normalizar datos
   ↓
IF: asunto contiene “propuesta” o “cotización”
   ├─ true → Notion: crear registro → Slack: enviar notificación
   └─ false → finalizar
```

## 1. Gmail Trigger

Añade el nodo **Gmail Trigger**:

- **Event:** `Message Received`
- **Poll Times:** cada minuto o según prefieras.
- En **Search / Filters**, si está disponible, usa:

```text
{subject:propuesta subject:cotizacion subject:cotización}
```

Aunque Gmail ya filtre, conviene mantener un filtro adicional en n8n para evitar falsos positivos.

## 2. Extraer y normalizar los datos

Añade un nodo **Code** llamado `Extraer datos` y usa:

```javascript
function getHeader(name) {
  const headers = $json.payload?.headers || [];

  const header = headers.find(
    h => h.name?.toLowerCase() === name.toLowerCase()
  );

  return (
    header?.value ||
    $json.headers?.[name.toLowerCase()] ||
    $json[name] ||
    ''
  );
}

const subject = getHeader('subject');
const fromRaw = getHeader('from');
const dateRaw = getHeader('date');

const emailMatch = fromRaw.match(/<([^>]+)>/) ||
                   fromRaw.match(/[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}/);

const email = emailMatch
  ? (emailMatch[1] || emailMatch[0]).trim()
  : '';

const senderName = fromRaw
  .replace(/<[^>]+>/, '')
  .replace(email, '')
  .replace(/^["']|["']$/g, '')
  .trim();

const normalizedSubject = subject
  .normalize('NFD')
  .replace(/[\u0300-\u036f]/g, '')
  .toLowerCase();

const isRelevant =
  normalizedSubject.includes('propuesta') ||
  normalizedSubject.includes('cotizacion');

return [{
  json: {
    messageId: $json.id || $json.messageId || '',
    senderName: senderName || email,
    senderEmail: email,
    subject,
    receivedAt: dateRaw
      ? new Date(dateRaw).toISOString()
      : new Date().toISOString(),
    isRelevant
  }
}];
```

## 3. Nodo IF

Añade un nodo **IF**:

- **Value 1:**

```text
{{ $json.isRelevant }}
```

- **Operation:** `is true`

La salida `false` puede quedar sin conectar.

## 4. Base de datos en Notion

Crea una base de datos con estas propiedades:

| Propiedad | Tipo |
|---|---|
| Asunto | Title |
| Nombre | Text |
| Email | Email |
| Fecha | Date |
| Gmail ID | Text |

Comparte la base de datos con la integración de Notion utilizada por n8n.

Después, en la salida `true`, añade un nodo **Notion**:

- **Resource:** `Database Page`
- **Operation:** `Create`
- Selecciona la base de datos.
- Mapea las propiedades:

```text
Asunto   → {{ $json.subject }}
Nombre   → {{ $json.senderName }}
Email    → {{ $json.senderEmail }}
Fecha    → {{ $json.receivedAt }}
Gmail ID → {{ $json.messageId }}
```

## 5. Notificación a Slack

Conecta el nodo **Slack** después de Notion, para notificar únicamente si el registro se guardó correctamente.

- **Resource:** `Message`
- **Operation:** `Send`
- Selecciona el canal.
- **Message:**

```text
📩 Nueva propuesta o cotización

*Remitente:* {{ $('Extraer datos').item.json.senderName }}
*Email:* {{ $('Extraer datos').item.json.senderEmail }}
*Asunto:* {{ $('Extraer datos').item.json.subject }}
*Fecha:* {{ $('Extraer datos').item.json.receivedAt }}

El contacto fue guardado en Notion.
```

De esta forma, solo los correos cuyo asunto contenga `propuesta`, `cotizacion` o `cotización` se guardarán en Notion y generarán una notificación en Slack.