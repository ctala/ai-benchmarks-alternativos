# Qwen 3.8 Max 0902 — multi_turn/requirements_change

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 3.63 | quality: 4.0
- latency_total: 388.424s | tokens_per_second: 41.0
- input_tokens: 275 | output_tokens: 15929

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

Perfecto. Te dejo una versión completa del workflow pensado para n8n:

```text
Gmail Trigger → Code: extraer datos + detectar propuesta/cotización → Filter → Notion: crear página → Slack: notificar
```

La idea es:

1. Leer emails nuevos desde Gmail.
2. Extraer nombre del remitente, email, asunto y fecha.
3. Filtrar solo asuntos que contengan `propuesta` o `cotización` / `cotizacion`.
4. Guardar esos datos en una base de datos de Notion.
5. Enviar una notificación a Slack.

---

## 1. Prepara tu base de datos en Notion

Crea una base de datos en Notion con estas propiedades, por ejemplo:

| Propiedad en Notion | Tipo        |
|---------------------|-------------|
| Nombre              | Title       |
| Email               | Email       |
| Asunto              | Rich text   |
| Fecha               | Date        |
| Email ID            | Rich text   |
| Origen              | Select      |

Importante:

- La propiedad `Nombre` debe ser el campo título.
- `Email ID` te servirá para evitar duplicados más adelante si quieres.
- Debes compartir la base de datos con tu integración de Notion.

---

## 2. Nodo Gmail Trigger

Agrega el nodo:

```text
Gmail Trigger
```

Configuración recomendada:

- Trigger: nuevo email recibido.
- Si tu versión lo permite, puedes filtrar por carpeta/label: `INBOX`.
- Opcional: puedes usar un filtro de Gmail como:

```text
subject:propuesta OR subject:cotizacion OR subject:cotización
```

Aunque luego pondremos un filtro dentro del workflow para asegurarnos.

Nota: si el Gmail Trigger de tu instancia solo devuelve el ID del mensaje y no incluye `payload.headers`, agrega después un nodo Gmail con operación `Get` usando:

```javascript
{{ $json.id }}
```

Pero en muchas versiones el Gmail Trigger ya devuelve el mensaje completo.

---

## 3. Nodo Code: extraer datos del remitente y detectar palabra clave

Agrega un nodo:

```text
Code
```

Nombre recomendado:

```text
Extraer y filtrar
```

Modo:

```text
Run Once for All Items
```

Pega este código:

```javascript
const items = [];

for (const item of $input.all()) {
  const email = item.json || {};
  const headers = email.payload?.headers || [];

  const getHeader = (name) => {
    const header = headers.find(
      (h) => (h.name || '').toLowerCase() === name.toLowerCase()
    );
    return header?.value || '';
  };

  const subject = getHeader('Subject') || email.subject || '';
  const fromRaw = getHeader('From') || email.from || '';
  const dateRaw = getHeader('Date') || email.date || '';

  // Detecta propuesta o cotización/cotizacion en el asunto
  const isTarget = /propuesta|cotizaci[oó]n/i.test(subject || '');

  let fromName = '';
  let fromEmail = fromRaw.trim();

  // Intenta separar: "Nombre Apellido <email@dominio.com>"
  if (fromRaw.includes('<') && fromRaw.includes('>')) {
    const namePart = fromRaw.split('<')[0].trim().replace(/^"|"$/g, '');
    const emailPart = fromRaw.split('<')[1]?.split('>')[0]?.trim() || '';

    if (emailPart) {
      fromName = namePart;
      fromEmail = emailPart;
    }
  }

  // Si no hay nombre, usa la parte antes del @
  if (!fromName && fromEmail.includes('@')) {
    fromName = fromEmail.split('@')[0];
  }

  let receivedAt = new Date().toISOString();

  if (dateRaw) {
    const parsed = new Date(dateRaw);
    if (!isNaN(parsed.getTime())) {
      receivedAt = parsed.toISOString();
    }
  }

  items.push({
    json: {
      emailId: email.id || '',
      threadId: email.threadId || '',
      fromName,
      fromEmail,
      subject,
      receivedAt,
      snippet: email.snippet || '',
      isTarget,
    },
  });
}

return items;
```

Este nodo devuelve campos como:

```javascript
{
  emailId: '...',
  threadId: '...',
  fromName: 'Juan Perez',
  fromEmail: 'juan@empresa.com',
  subject: 'Propuesta comercial',
  receivedAt: '2026-...',
  snippet: '...',
  isTarget: true
}
```

---

## 4. Nodo Filter: solo propuestas o cotizaciones

Agrega un nodo:

```text
Filter
```

o también puedes usar:

```text
IF
```

Condición:

```text
isTarget equals true
```

En forma de expresión:

```javascript
{{ $json.isTarget }}
```

Valor esperado:

```text
true
```

Si usas el nodo Filter nuevo de n8n, puedes dejarlo como:

- Left value:

```javascript
{{ $json.isTarget }}
```

- Operator:

```text
is true
```

o:

```text
equals
```

- Right value:

```text
true
```

Solo los emails que tengan `propuesta` o `cotización/cotizacion` en el asunto continuarán.

---

## 5. Nodo Notion: guardar el contacto

Agrega el nodo:

```text
Notion
```

Nombre recomendado:

```text
Guardar en Notion
```

Configuración:

- Resource: `Database Page`
- Operation: `Create`
- Database: selecciona tu base de datos.
- Credentials: tu credencial de Notion.

Luego mapea las propiedades:

| Propiedad Notion | Valor en n8n |
|------------------|--------------|
| Nombre           | `{{ $json.fromName }}` |
| Email            | `{{ $json.fromEmail }}` |
| Asunto           | `{{ $json.subject }}` |
| Fecha            | `{{ $json.receivedAt }}` |
| Email ID         | `{{ $json.emailId }}` |
| Origen           | `Gmail` |

Ejemplo de valores:

```javascript
{{ $json.fromName }}
```

```javascript
{{ $json.fromEmail }}
```

```javascript
{{ $json.subject }}
```

```javascript
{{ $json.receivedAt }}
```

```javascript
{{ $json.emailId }}
```

Importante: los nombres de las propiedades deben coincidir exactamente con los que creaste en Notion.

---

## 6. Nodo Slack: enviar notificación

Agrega el nodo:

```text
Slack
```

Nombre recomendado:

```text
Avisar Slack
```

Configuración:

- Resource: `Message`
- Operation: `Send`
- Channel: por ejemplo `#ventas`, `#propuestas`, `#notificaciones`, etc.
- Credentials: tu credencial de Slack.

Texto sugerido:

```text
:inbox_tray: Nueva propuesta/cotización recibida

*De:* {{ $('Extraer y filtrar').item.json.fromName }} <{{ $('Extraer y filtrar').item.json.fromEmail }}>
*Asunto:* {{ $('Extraer y filtrar').item.json.subject }}
*Fecha:* {{ $('Extraer y filtrar').item.json.receivedAt }}
*Notion:* {{ $json.url || '' }}
```

Si tu nodo Code tiene otro nombre, cambia:

```javascript
$('Extraer y filtrar')
```

por el nombre exacto de tu nodo.

Si Notion no devuelve `url`, puedes usar también:

```javascript
{{ $json.id }}
```

o construir una URL si tienes el page ID.

---

## 7. Flujo completo

El workflow debería quedar así:

```text
Gmail Trigger
     ↓
Extraer y filtrar
     ↓
Filtro propuesta/cotización
     ↓
Guardar en Notion
     ↓
Avisar Slack
```

---

## Opción alternativa: notificar aunque Notion falle

Si conectas:

```text
Filter → Notion → Slack
```

Slack solo se ejecutará si Notion se ejecuta correctamente.

Si quieres que Slack avise inmediatamente aunque Notion falle, conecta Slack en paralelo:

```text
              → Notion
Filter
              → Slack
```

En ese caso, en Slack puedes usar directamente:

```text
:inbox_tray: Nueva propuesta/cotización recibida

*De:* {{ $json.fromName }} <{{ $json.fromEmail }}>
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.receivedAt }}
```

---

## Recomendación opcional: marcar email como leído

Si configuras el Gmail Trigger para leer solo emails no leídos, puedes evitar que se procesen otra vez agregando al final un nodo Gmail.

Después de Slack, agrega:

```text
Gmail
```

Configuración:

- Resource: `Message`
- Operation: `Mark as Read` o `Update`, según tu versión.
- Message ID:

```javascript
{{ $('Extraer y filtrar').item.json.emailId }}
```

Así el email ya no aparecerá como no leído después de procesarse.

---

## Recomendación opcional: evitar duplicados en Notion

Como Gmail puede volver a procesar un correo en algunos escenarios, puedes guardar siempre:

```javascript
{{ $json.emailId }}
```

en la propiedad `Email ID`.

Luego, si quieres una versión más robusta:

1. Antes de crear la página en Notion, usa un nodo Notion con operación `Query`.
2. Filtra por `Email ID` igual a:

```javascript
{{ $json.emailId }}
```

3. Usa un nodo `IF` para verificar si ya existe.
4. Solo crea la página si no existe.

Estructura:

```text
Filter → Notion Query → IF → Notion Create → Slack
```

---

## Credenciales necesarias

Necesitarás configurar estas credenciales en n8n:

### Gmail

OAuth2 con permisos como:

```text
https://www.googleapis.com/auth/gmail.readonly
```

Si quieres marcar como leído:

```text
https://www.googleapis.com/auth/gmail.modify
```

### Notion

Puedes usar:

- OAuth2, o
- Internal Integration Token.

Asegúrate de que la integración tenga acceso a la base de datos donde quieres guardar los registros.

### Slack

Para enviar mensajes, el bot necesita permisos como:

```text
chat:write
```

Y debe estar invitado al canal donde enviará la notificación.

---

## Prueba rápida

Envía un email de prueba con asuntos como:

```text
Propuesta comercial
```

```text
Cotización de servicios
```

```text
Cotizacion solicitada
```

Y verifica:

1. Que Gmail Trigger reciba el email.
2. Que el nodo Code extraiga `fromName`, `fromEmail`, `subject`.
3. Que `isTarget` sea `true`.
4. Que Notion cree la página.
5. Que Slack reciba el mensaje.

---

## Posible problema con acentos

Si el asunto viene codificado y el filtro no detecta `cotización`, puedes usar también la variante sin tilde:

```text
cotizacion
```

El regex actual ya contempla ambas:

```javascript
/propuesta|cotizaci[oó]n/i
```

Si aun así no detecta asuntos codificados, lo más simple es filtrar también desde Gmail Trigger con:

```text
subject:propuesta OR subject:cotizacion OR subject:cotización
```

---

En resumen, el workflow mínimo sería:

```text
Gmail Trigger → Code → Filter → Notion → Slack
```

con el nodo Code extrayendo remitente/asunto/fecha y marcando `isTarget` cuando el asunto contiene `propuesta` o `cotización/cotizacion`.