# MiniMax M3 — multi_turn/requirements_change

- model_id: `minimax/minimax-m3`
- success: True  | final: 5.6 | quality: 6.0
- latency_total: 140.025s | tokens_per_second: 68.6
- input_tokens: 407 | output_tokens: 9608

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

Sí. Puedes reemplazar Google Sheets por **Notion** y filtrar los emails antes de guardarlos.

## Flujo recomendado

```text
Gmail Trigger
      ↓
Code: Extraer remitente y normalizar asunto
      ↓
IF: ¿El asunto contiene “propuesta” o “cotización”?
      ├─ Sí → Notion: Crear página
      └─ Sí → Slack: Enviar notificación
```

Las dos ramas después del `IF` pueden ejecutarse en paralelo, de modo que Slack avisa aunque Notion tenga algún problema.

---

## 1. Nodo Gmail Trigger

Configuración:

- **Credential:** tu cuenta de Gmail mediante OAuth2.
- **Trigger On:** `Message Received`.
- **Poll Time:** `Every Minute` o el intervalo que prefieras.
- **Label:** `INBOX`.
- **Simplify:** activado.

El alcance de Google puede ser:

```text
https://www.googleapis.com/auth/gmail.readonly
```

> Gmail Trigger funciona por sondeo: no es un webhook instantáneo. Con una频率 de un minuto normalmente será casi en tiempo real.

---

## 2. Nodo Code: extraer remitente y comprobar el asunto

Crea un nodo **Code**, ponle el nombre:

```text
Extraer remitente
```

En **Mode**, selecciona `Run Once for Each Item` y pega:

```javascript
const item = $input.first();
const j = item.json;

// Extrae nombre y email del remitente en diferentes formatos de Gmail
function parseFrom(value) {
  if (!value) return { name: '', email: '' };

  if (typeof value === 'string') {
    const match = value.match(/^\s*(.*?)\s*<([^>]+)>\s*$/);

    if (match) {
      return {
        name: match[1].replace(/^["']|["']$/g, '').trim(),
        email: match[2].trim(),
      };
    }

    return {
      name: '',
      email: value.trim(),
    };
  }

  if (Array.isArray(value)) {
    return parseFrom(value[0]);
  }

  if (value.value) {
    return parseFrom(
      Array.isArray(value.value) ? value.value[0] : value.value
    );
  }

  if (value.address || value.email) {
    return {
      name: value.name || '',
      email: value.address || value.email,
    };
  }

  return { name: '', email: '' };
}

const sender = parseFrom(j.from ?? j.sender);

const headers = j.payload?.headers ?? [];

const subjectHeader = headers.find(
  (header) => header.name?.toLowerCase() === 'subject'
)?.value;

const dateHeader = headers.find(
  (header) => header.name?.toLowerCase() === 'date'
)?.value;

const subject = j.subject ?? subjectHeader ?? '';

let emailDate = j.date || dateHeader || '';

if (!emailDate && j.internalDate) {
  emailDate = new Date(Number(j.internalDate)).toISOString();
}

// Normaliza acentos: detecta "cotización" y "cotizacion"
const normalizedSubject = String(subject)
  .normalize('NFD')
  .replace(/[\u0300-\u036f]/g, '')
  .toLowerCase();

// Detecta singular y plural
const matchesFilter = /\b(propuestas?|cotizaciones?)\b/.test(
  normalizedSubject
);

const messageId = j.id ?? j.messageId ?? '';

const gmailUrl = messageId
  ? `https://mail.google.com/mail/u/0/#all/${messageId}`
  : '';

return [
  {
    json: {
      ...j,
      sender_name: sender.name,
      sender_email: sender.email,
      subject: String(subject),
      email_date: emailDate,
      gmail_url: gmailUrl,
      matches_filter: matchesFilter,
    },
  },
];
```

Este código:

- Extrae nombre y correo del remitente.
- Admite diferentes formatos del campo `from`.
- Detecta `propuesta`, `propuestas`, `cotizacion`, `cotizaciones` y `cotización`.
- Genera un enlace directo al email en Gmail.

---

## 3. Nodo IF: filtrar por asunto

Añade un nodo **IF** conectado al anterior.

Configura la condición:

- **Left Value:** `{{ $json.matches_filter }}`
- **Operator:** `is true`
- **Value:** `true`

Conexiones:

- Salida **true** → nodo de Notion.
- Salida **true** → nodo de Slack.
- Salida **false** → déjala sin conectar.

De esta forma, los emails no relevantes terminan ahí y no generan página en Notion ni mensaje en Slack.

---

## 4. Nodo Notion

Añade el nodo **Notion**:

- **Operation:** `Create Page` o `Create Database Row`, según tu versión de N8N.
- **Parent:** la base de datos donde quieres guardar los emails.
- **Credential:** tu integración de Notion.

Importante: la base de datos debe estar compartida con la integración de Notion.

### Propiedades recomendadas

| Propiedad en Notion | Tipo | Valor en N8N |
|---|---|---|
| `Asunto` | Title | `{{ $json.subject }}` |
| `Remitente` | Rich text | `{{ $json.sender_name }}` |
| `Email` | Email o Rich text | `{{ $json.sender_email }}` |
| `Fecha` | Date | `{{ $json.email_date }}` |
| `ID Gmail` | Rich text | `{{ $json.id }}` |
| `Enlace Gmail` | URL | `{{ $json.gmail_url }}` |

Los nombres de las propiedades deben coincidir exactamente con los de tu base de datos. Si la propiedad principal se llama `Nombre` en vez de `Asunto`, utiliza `Nombre` como tipo `Title`.

---

## 5. Nodo Slack

Añade el nodo **Slack**:

- **Resource:** `Message`.
- **Operation:** `Send Message`.
- **Channel:** selecciona el canal de destino.
- **Credential:** tu credencial de Slack.

En el campo de texto pega:

```text
:rotating_light: *Nuevo email comercial detectado*

*Asunto:* {{ $json.subject }}
*Remitente:* {{ $json.sender_name || $json.sender_email }}
*Email:* {{ $json.sender_email }}
*Fecha:* {{ $json.email_date }}

{{ $json.gmail_url }}
```

La aplicación de Slack debe tener permiso `chat:write` y, si el canal es privado, debes invitar al bot al canal.

---

## Resultado

Cuando llegue un email cuyo asunto contenga una de las palabras permitidas:

1. N8N extrae los datos del remitente.
2. Crea una página en Notion.
3. Envía una notificación a Slack.

Los demás emails se descartan después del filtro.

Para evitar duplicados en Notion, conserva el campo `ID Gmail` y, si el volumen es alto, puedes añadir un nodo **Notion: Search/Database Rows** antes de crear la página para comprobar si ese ID ya existe.