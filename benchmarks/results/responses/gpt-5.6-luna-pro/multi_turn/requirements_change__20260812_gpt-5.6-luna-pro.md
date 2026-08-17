# GPT-5.6 Luna Pro — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 4.56 | quality: 4.0
- latency_total: 21.749s | tokens_per_second: 241.2
- input_tokens: 7086 | output_tokens: 5246

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

Puedes construirlo con este flujo:

```text
Gmail Trigger
   ↓
Gmail - Get Message
   ↓
Code - Extraer datos
   ↓
IF - Asunto válido
   ├── true → Notion - Create Page
   │            └── Slack - Send Message
   └── false → fin
```

## 1. Gmail Trigger

Configura un nodo **Gmail Trigger**:

- **Event**: `Message Received`
- **Search / Gmail Query**:

```text
{subject:propuesta subject:cotizacion}
```

Esto reduce los mensajes recibidos a aquellos cuyo asunto contiene alguna de esas palabras.

> Aunque filtremos desde Gmail, conviene mantener también un nodo `IF` para validar el asunto de forma segura.

Configura las credenciales OAuth2 de Gmail.

---

## 2. Gmail - Get Message

Añade un nodo **Gmail** después del trigger:

- **Resource**: `Message`
- **Operation**: `Get`
- **Message ID**:

```javascript
{{$json.id}}
```

Si está disponible, selecciona el formato completo de la respuesta, como `Full`, para obtener los headers del mensaje.

---

## 3. Code - Extraer datos del email

Añade un nodo **Code** con este código:

```javascript
const headers = $json.payload?.headers || [];

function getHeader(name) {
  const header = headers.find(
    h => h.name?.toLowerCase() === name.toLowerCase()
  );

  return header?.value || '';
}

const from = getHeader('From');
const subject = getHeader('Subject');
const date = getHeader('Date');
const messageId = $json.id || '';
const threadId = $json.threadId || '';

let senderName = '';
let senderEmail = '';

const emailMatch = from.match(/<([^>]+)>/);

if (emailMatch) {
  senderEmail = emailMatch[1].trim();
  senderName = from.replace(/<[^>]+>/, '').replace(/"/g, '').trim();
} else {
  senderEmail = from.trim();
  senderName = from.trim();
}

return [
  {
    json: {
      messageId,
      threadId,
      senderName,
      senderEmail,
      subject,
      receivedAt: date,
      gmailUrl: `https://mail.google.com/mail/u/0/#all/${messageId}`
    }
  }
];
```

El nodo generará estos campos:

```text
senderName
senderEmail
subject
receivedAt
gmailUrl
messageId
threadId
```

---

## 4. IF - Filtrar el asunto

Añade un nodo **IF**.

Puedes configurarlo con una condición de tipo **String**:

- **Value 1**:

```javascript
{{ $json.subject.toLowerCase() }}
```

- **Operation**: `Matches Regex`
- **Value 2**:

```text
(propuesta|cotizacion)
```

Si quieres aceptar también acentos, utiliza:

```text
(propuesta|propuesta|cotizacion|cotización)
```

La rama `true` continuará hacia Notion y Slack.

---

## 5. Notion - Create Page

Antes de configurarlo, crea una base de datos en Notion con propiedades similares a estas:

| Propiedad | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Title o Rich Text |
| Fecha | Date |
| Gmail URL | URL |
| Message ID | Rich Text |

En el nodo **Notion**:

- **Resource**: `Database Page`
- **Operation**: `Create`
- Selecciona la base de datos correspondiente.

Mapea los campos, por ejemplo:

### Nombre

```javascript
{{$json.senderName}}
```

### Email

```javascript
{{$json.senderEmail}}
```

### Asunto

```javascript
{{$json.subject}}
```

### Fecha

```javascript
{{$json.receivedAt}}
```

### Gmail URL

```javascript
{{$json.gmailUrl}}
```

### Message ID

```javascript
{{$json.messageId}}
```

Los nombres exactos de las propiedades deben coincidir con los de tu base de datos de Notion. Además, la integración de Notion debe tener acceso a esa base de datos mediante **Share → Invite**.

---

## 6. Slack - Send Message

Conecta un nodo **Slack** desde la rama `true` del nodo `IF`.

Configura:

- **Resource**: `Message`
- **Operation**: `Send`
- **Channel**: el canal donde quieras recibir las alertas

Mensaje sugerido:

```text
📩 Nuevo email de propuesta o cotización

👤 Remitente: {{$json.senderName}}
📧 Email: {{$json.senderEmail}}
📝 Asunto: {{$json.subject}}
📅 Fecha: {{$json.receivedAt}}

🔗 Abrir en Gmail: {{$json.gmailUrl}}
```

Puedes conectar Notion y Slack en paralelo desde el nodo `IF`, o colocar Slack después de Notion si prefieres notificar únicamente cuando el registro se haya creado correctamente.

## Recomendaciones

- Usa el filtro de Gmail y el nodo `IF` para evitar falsos positivos.
- Si el workflow puede ejecutarse varias veces sobre el mismo correo, guarda `messageId` en Notion y comprueba antes si ya existe.
- También puedes añadir una etiqueta de Gmail como `Procesado-N8N` después de guardar el email para evitar duplicados.
- Configura el workflow con `Active` para que el trigger de Gmail funcione automáticamente.