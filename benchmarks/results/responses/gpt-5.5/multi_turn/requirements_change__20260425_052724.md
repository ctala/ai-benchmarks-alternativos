# GPT-5.5 — multi_turn/requirements_change

- model_id: `gpt-5.5`
- success: True  | final: 5.32 | quality: 4.64
- latency_total: 15.015s | tokens_per_second: 87.4
- input_tokens: 226 | output_tokens: 1313
- judge_score: 2.0 | justificación: 

## Respuesta completa

Claro. El workflow quedaría así:

## Workflow en n8n

**Gmail Trigger → Filtro por asunto → Extraer datos → Guardar en Notion → Notificación Slack**

---

## 1. Gmail Trigger

Nodo: **Gmail Trigger**

Configuración sugerida:

- **Event**: `Message Received`
- **Poll Times**: cada 1, 5 o 10 minutos, según necesidad.
- **Label**: `INBOX`, si solo quieres emails entrantes.
- **Simplify Output**: activado, si está disponible.

Este nodo leerá cada email nuevo que llegue a Gmail.

---

## 2. Filtro por asunto

Nodo: **IF**

Condición:

- **Value 1**:

```js
{{ $json.subject.toLowerCase() }}
```

- Operación: `contains`
- **Value 2**:

```text
propuesta
```

Agrega otra condición con **OR**:

- **Value 1**:

```js
{{ $json.subject.toLowerCase() }}
```

- Operación: `contains`
- **Value 2**:

```text
cotizacion
```

Opcionalmente, también puedes agregar:

```text
cotización
```

por si llega con tilde.

La lógica debería ser:

```text
subject contiene "propuesta"
OR
subject contiene "cotizacion"
OR
subject contiene "cotización"
```

Solo la rama `true` continúa al resto del workflow.

---

## 3. Extraer datos del remitente

Nodo: **Code**

Este nodo limpia y separa el nombre y email del remitente.

Código:

```js
const from = $json.from || '';
const subject = $json.subject || '';
const date = $json.date || new Date().toISOString();

let senderName = '';
let senderEmail = '';

const match = from.match(/^(.*?)\s*<(.+?)>$/);

if (match) {
  senderName = match[1].replace(/"/g, '').trim();
  senderEmail = match[2].trim();
} else {
  senderEmail = from.trim();
  senderName = '';
}

return [
  {
    json: {
      senderName,
      senderEmail,
      subject,
      date,
      snippet: $json.snippet || '',
      messageId: $json.id || $json.messageId || '',
    }
  }
];
```

Esto generará datos como:

```json
{
  "senderName": "Juan Pérez",
  "senderEmail": "juan@empresa.com",
  "subject": "Propuesta comercial",
  "date": "2026-04-25T10:00:00.000Z",
  "snippet": "Hola, te envío la propuesta..."
}
```

---

## 4. Crear base de datos en Notion

En Notion crea una database, por ejemplo:

**Nombre:** `Emails de propuestas`

Propiedades recomendadas:

| Propiedad | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Text |
| Fecha | Date |
| Snippet | Text |
| Message ID | Text |
| Estado | Select |

Ejemplo de valores para `Estado`:

- Nuevo
- Contactado
- En revisión
- Cerrado

---

## 5. Guardar datos en Notion

Nodo: **Notion**

Configuración:

- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database**: selecciona tu database de Notion.

Mapeo de campos:

### Nombre

```js
{{ $json.senderName || $json.senderEmail }}
```

### Email

```js
{{ $json.senderEmail }}
```

### Asunto

```js
{{ $json.subject }}
```

### Fecha

```js
{{ $json.date }}
```

### Snippet

```js
{{ $json.snippet }}
```

### Message ID

```js
{{ $json.messageId }}
```

### Estado

```text
Nuevo
```

Importante: asegúrate de haber compartido la database de Notion con tu integración de Notion, si no n8n no podrá verla.

---

## 6. Notificación a Slack

Nodo: **Slack**

Configuración:

- **Resource**: `Message`
- **Operation**: `Send`
- **Channel**: el canal que quieras, por ejemplo `#ventas` o `#propuestas`.

Mensaje sugerido:

```text
Nueva propuesta/cotización recibida 📩

Remitente: {{ $json.senderName || 'Sin nombre' }}
Email: {{ $json.senderEmail }}
Asunto: {{ $json.subject }}
Fecha: {{ $json.date }}

Se guardó automáticamente en Notion.
```

---

## Estructura final del workflow

```text
Gmail Trigger
   ↓
IF - Asunto contiene propuesta/cotizacion/cotización
   ↓ true
Code - Extraer remitente
   ↓
Notion - Crear página en database
   ↓
Slack - Enviar notificación
```

La rama `false` del IF puede quedar sin conectar, así los emails que no cumplan la condición simplemente se ignoran.

---

## Recomendación extra

Para evitar duplicados, puedes guardar el `Message ID` en Notion y antes de crear una nueva página hacer una búsqueda en Notion para verificar si ese email ya fue registrado. Esto es útil si el workflow se reintenta o si Gmail devuelve el mismo mensaje más de una vez.