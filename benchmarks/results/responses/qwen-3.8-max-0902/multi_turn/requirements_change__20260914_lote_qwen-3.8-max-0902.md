# Qwen 3.8 Max 0902 — multi_turn/requirements_change

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 3.86 | quality: 4.0
- latency_total: 203.03s | tokens_per_second: 51.4
- input_tokens: 275 | output_tokens: 10437

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

Perfecto. Con el cambio, el workflow quedaria asi:

```text
Gmail Trigger
   ↓
Code / Function: extraer datos del email
   ↓
Filter / IF: solo si el asunto contiene "propuesta" o "cotizacion"
   ↓
Slack: enviar notificacion
   ↓
Notion: guardar el registro
```

Te dejo una version lista para armar en n8n.

---

## 1. Credenciales que necesitas

Antes de armar el workflow, deja listas estas credenciales en n8n:

1. **Gmail OAuth2 API**
2. **Notion API**
3. **Slack API**

Ademas:

- En Notion, crea una base de datos y compartela con tu integracion de Notion.
- En Slack, invita a tu bot al canal donde quieres recibir la notificacion.

---

## 2. Estructura recomendada del workflow

### Nodos

1. **Gmail Trigger**
2. **Code**
3. **Filter**
4. **Slack**
5. **Notion**

Conexion:

```text
Gmail Trigger → Code → Filter → Slack → Notion
```

Si quieres que la notificacion llegue aunque falle Notion, puedes conectar:

```text
Filter → Slack
Filter → Notion
```

Pero si quieres que Slack avise solo cuando realmente se guardo en Notion, usa:

```text
Filter → Slack → Notion
```

o

```text
Filter → Notion → Slack
```

Para tu caso, yo recomiendaria:

```text
Filter → Slack → Notion
```

porque la prioridad parece ser avisar rapido cuando llega un email relevante.

---

## 3. Nodo 1: Gmail Trigger

Agrega un nodo **Gmail Trigger**.

Configuracion basica:

- **Trigger**: nuevo email recibido.
- Si tu version lo permite, filtra por inbox o solo no leidos.
- Si quieres reducir ruido, puedes usar opciones como:
  - `INBOX`
  - `UNREAD`

La idea es que este nodo entregue los correos entrantes.

---

## 4. Nodo 2: Code para extraer los datos

Agrega un nodo **Code**.

Importante: configuralo como **Run Once for All Items** si vas a procesar varios emails, o como **Run Once for Each Item** si prefieres procesar uno por uno.

El codigo de abajo esta pensado para **Run Once for All Items**.

### Codigo recomendado

```javascript
const results = [];

for (const item of $input.all()) {
  const email = item.json;

  const headers = Array.isArray(email.payload?.headers)
    ? email.payload.headers
    : [];

  const getHeader = (name) => {
    const header = headers.find(
      h => (h.name || '').toLowerCase() === name.toLowerCase()
    );
    return header?.value || '';
  };

  const asText = (value) => {
    if (!value) return '';

    if (typeof value === 'string') return value;

    if (typeof value === 'object') {
      if (value.name && (value.email || value.address)) {
        return `${value.name} <${value.email || value.address}>`;
      }

      if (value.email) return value.email;
      if (value.address) return value.address;
      if (value.content) return value.content;
    }

    return String(value);
  };

  const rawFrom = asText(
    email.from ||
    email.From ||
    getHeader('From')
  );

  const rawSubject = asText(
    email.subject ||
    email.Subject ||
    getHeader('Subject')
  );

  const rawDate = asText(
    email.date ||
    email.Date ||
    getHeader('Date')
  );

  let senderName = '';
  let senderEmail = '';

  const fromMatch = rawFrom.match(
    /^\s*"?([^"<]*)"?\s*<([^>]+)>\s*$/
  );

  if (fromMatch) {
    senderName = fromMatch[1].trim();
    senderEmail = fromMatch[2].trim();
  } else if (rawFrom.includes('@')) {
    senderEmail = rawFrom.trim();
    senderName = senderEmail.split('@')[0];
  }

  let dateISO = '';

  if (email.internalDate) {
    const timestamp = Number(email.internalDate);

    if (!Number.isNaN(timestamp)) {
      dateISO = new Date(timestamp).toISOString();
    }
  }

  if (!dateISO && rawDate) {
    const parsedDate = new Date(rawDate);

    if (!Number.isNaN(parsedDate.getTime())) {
      dateISO = parsedDate.toISOString();
    }
  }

  if (!dateISO) {
    dateISO = new Date().toISOString();
  }

  const subject = rawSubject.trim();
  const subjectLower = subject.toLowerCase();

  const matchesPropuesta = subjectLower.includes('propuesta');
  const matchesCotizacion =
    subjectLower.includes('cotizacion') ||
    subjectLower.includes('cotización');

  const matchedKeyword = matchesPropuesta
    ? 'propuesta'
    : matchesCotizacion
      ? 'cotización'
      : null;

  results.push({
    json: {
      messageId: email.id || email.messageId || getHeader('Message-ID') || '',
      fromRaw: rawFrom,
      senderName: senderName || 'Desconocido',
      senderEmail: senderEmail || '',
      subject: subject || 'Sin asunto',
      subjectLower,
      dateISO,
      snippet: (email.snippet || '').slice(0, 300),
      matchedKeyword,
      matchesPropuesta,
      matchesCotizacion
    }
  });
}

return results;
```

Este nodo deja disponibles campos como:

```text
senderName
senderEmail
subject
dateISO
snippet
matchedKeyword
messageId
```

---

## 5. Nodo 3: Filter para validar asunto

Agrega un nodo **Filter** o **IF**.

La condicion debe dejar pasar solo los emails cuyo asunto contenga:

- `propuesta`
- `cotizacion`
- `cotización`

### Opcion recomendada con expresion

Si usas un nodo **Filter** con expresion, puedes poner:

```javascript
={{ !!$json.matchedKeyword }}
```

Esto deja pasar solo los emails donde `matchedKeyword` tenga valor.

### Opcion manual por condiciones

Si prefieres hacerlo por condiciones:

Condicion 1:

```text
subjectLower contains propuesta
```

Condicion 2:

```text
subjectLower contains cotizacion
```

Condicion 3:

```text
subjectLower contains cotización
```

Usa operador **OR**.

---

## 6. Nodo 4: Slack para notificar

Agrega un nodo **Slack**.

Configuracion basica:

- **Resource**: Message
- **Operation**: Send
- **Channel**: selecciona el canal donde quieres recibir la alerta
- **Text**: activa expresion y pega algo asi:

```text
:inbox_tray: *Nueva propuesta o cotizacion recibida*

*Palabra detectada:* {{ $json.matchedKeyword }}
*Remitente:* {{ $json.senderName }}
*Email:* {{ $json.senderEmail }}
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.dateISO }}
```

Si quieres incluir tambien un fragmento del email:

```text
:inbox_tray: *Nueva propuesta o cotizacion recibida*

*Palabra detectada:* {{ $json.matchedKeyword }}
*Remitente:* {{ $json.senderName }}
*Email:* {{ $json.senderEmail }}
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.dateISO }}

*Snippet:*
{{ $json.snippet }}
```

---

## 7. Nodo 5: Notion para guardar

Agrega un nodo **Notion**.

Configuracion:

- **Resource**: Database Page
- **Operation**: Create
- **Database**: selecciona tu base de datos de Notion

---

## 8. Base de datos recomendada en Notion

Crea una base de datos con estas propiedades:

| Nombre de propiedad | Tipo en Notion |
|---|---|
| Nombre | Title |
| Email | Text |
| Asunto | Text |
| Fecha | Date |
| Palabra clave | Text |
| Snippet | Text |
| Message ID | Text |

Importante: los nombres deben coincidir exactamente con los que uses en el nodo de Notion.

---

## 9. JSON de propiedades para Notion

En el nodo de Notion, cuando te pida las propiedades, puedes usar algo asi:

```json
{
  "Nombre": {
    "title": [
      {
        "text": {
          "content": "={{ $json.senderName || 'Sin nombre' }}"
        }
      }
    ]
  },
  "Email": {
    "rich_text": [
      {
        "text": {
          "content": "={{ $json.senderEmail || 'N/D' }}"
        }
      }
    ]
  },
  "Asunto": {
    "rich_text": [
      {
        "text": {
          "content": "={{ $json.subject || 'Sin asunto' }}"
        }
      }
    ]
  },
  "Fecha": {
    "date": {
      "start": "={{ $json.dateISO }}"
    }
  },
  "Palabra clave": {
    "rich_text": [
      {
        "text": {
          "content": "={{ $json.matchedKeyword || '' }}"
        }
      }
    ]
  },
  "Snippet": {
    "rich_text": [
      {
        "text": {
          "content": "={{ $json.snippet || '' }}"
        }
      }
    ]
  },
  "Message ID": {
    "rich_text": [
      {
        "text": {
          "content": "={{ $json.messageId || '' }}"
        }
      }
    ]
  }
}
```

Si no quieres guardar `Snippet` o `Message ID`, simplemente quita esos bloques del JSON y tambien esas propiedades en Notion.

---

## 10. Workflow final recomendado

```text
Gmail Trigger
   ↓
Code
   ↓
Filter
   ↓
Slack
   ↓
Notion
```

Con esto:

1. n8n detecta un nuevo email en Gmail.
2. Extrae remitente, email, asunto, fecha y snippet.
3. Filtra solo asuntos que contengan `propuesta`, `cotizacion` o `cotización`.
4. Envia una alerta a Slack.
5. Guarda el registro en Notion.

---

## 11. Recomendacion para evitar duplicados

Si el workflow se ejecuta muchas veces o Gmail Trigger llega a repetir correos, puedes agregar control de duplicados.

La forma mas simple:

1. Guarda el campo `messageId` en Notion.
2. Antes de crear la pagina en Notion, consulta si ya existe un registro con ese `messageId`.
3. Si existe, no vuelves a crearlo.

En Notion, el flujo seria:

```text
Filter
   ↓
Notion: Query Database
   ↓
IF: existe?
   ↓ No
Notion: Create Database Page
```

Y la alerta a Slack puede ir antes o despues, segun prefieras.

---

## 12. Version alternativa filtrando desde Gmail

Si quieres que Gmail entregue directamente solo correos que tengan esas palabras en el asunto, puedes usar una consulta tipo:

```text
subject:propuesta OR subject:cotizacion OR subject:cotización
```

Por ejemplo:

```text
subject:propuesta OR subject:cotizacion OR subject:cotización is:unread
```

Esto puede ser util si en lugar de usar Gmail Trigger usas:

```text
Schedule Trigger → Gmail → Get Many Messages
```

Aun asi, yo dejaria tambien el filtro dentro de n8n por seguridad.