# GPT-5.6 Terra Pro — multi_turn/requirements_change

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 4.07 | quality: 4.0
- latency_total: 36.824s | tokens_per_second: 180.4
- input_tokens: 7591 | output_tokens: 6643

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

Puedes montar el workflow así:

```text
Gmail Trigger
  → Code / Set (normalizar y extraer datos)
  → IF (filtrar asunto)
  → Notion (crear página en base de datos)
  → Slack (enviar notificación)
```

## 1. Gmail Trigger

Añade el nodo **Gmail Trigger**.

Configuración recomendada:

- **Event**: `Message Received`
- **Simplify**: activado, si está disponible
- **Search / Filters**: puedes filtrar desde Gmail con esta consulta:

```text
subject:(propuesta OR cotizacion)
```

> Nota: para evitar depender solo de la búsqueda de Gmail —por variaciones como `cotización` con tilde o mayúsculas— también aplicaremos el filtro dentro de n8n con un nodo **IF**.

Conecta tus credenciales OAuth2 de Gmail.

---

## 2. Nodo Code: extraer y normalizar datos

Añade un nodo **Code** justo después del trigger.

Nombre sugerido: `Preparar datos del email`

Código:

```javascript
const email = $input.item.json;

const subject = email.subject || '';
const from = email.from || '';
const date = email.date || new Date().toISOString();

// Intenta separar: "Nombre Apellido <correo@dominio.com>"
const match = from.match(/^(?:"?([^"<]+)"?\s)?<?([^>\s]+@[^>\s]+)>?$/);

const senderName = match?.[1]?.trim() || '';
const senderEmail = match?.[2]?.trim() || from;

// Normaliza para filtrar sin distinguir mayúsculas o tildes
const normalizedSubject = subject
  .toLowerCase()
  .normalize('NFD')
  .replace(/[\u0300-\u036f]/g, '');

return [{
  json: {
    senderName,
    senderEmail,
    subject,
    normalizedSubject,
    receivedAt: date,
    gmailMessageId: email.id || email.messageId || '',
    snippet: email.snippet || email.textPlain || '',
  }
}];
```

Este nodo deja los datos preparados, por ejemplo:

```json
{
  "senderName": "Ana Pérez",
  "senderEmail": "ana@empresa.com",
  "subject": "Propuesta comercial para su empresa",
  "normalizedSubject": "propuesta comercial para su empresa",
  "receivedAt": "2025-01-15T10:00:00.000Z",
  "gmailMessageId": "abc123",
  "snippet": "Hola, adjuntamos nuestra propuesta..."
}
```

---

## 3. Nodo IF: filtrar “propuesta” o “cotización”

Añade un nodo **IF** después del Code.

Configura una condición de tipo **Boolean**:

- **Value 1** (Expression):

```javascript
{{ $json.normalizedSubject.includes('propuesta') || $json.normalizedSubject.includes('cotizacion') }}
```

- **Operation**: `is true`

Conecta únicamente la salida **true** al nodo Notion.

Así se aceptarán asuntos como:

- `Propuesta de colaboración`
- `Nueva cotización`
- `COTIZACIÓN servicios SEO`
- `Re: propuesta comercial`

Y se ignorarán emails sin esas palabras.

---

## 4. Notion: guardar en una base de datos

Primero crea una base de datos en Notion, por ejemplo: **Propuestas recibidas**.

Propiedades recomendadas:

| Propiedad en Notion | Tipo |
|---|---|
| Nombre | Title |
| Email remitente | Email |
| Asunto | Text / Rich text |
| Fecha recepción | Date |
| ID Gmail | Text |
| Extracto | Text / Rich text |
| Estado | Select |

Luego añade el nodo **Notion**:

- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database**: selecciona tu base de datos

Mapea las propiedades así:

### Nombre (Title)

```javascript
{{ $json.senderName || $json.senderEmail }}
```

### Email remitente

```javascript
{{ $json.senderEmail }}
```

### Asunto

```javascript
{{ $json.subject }}
```

### Fecha recepción

```javascript
{{ $json.receivedAt }}
```

### ID Gmail

```javascript
{{ $json.gmailMessageId }}
```

### Extracto

```javascript
{{ $json.snippet }}
```

### Estado

Valor fijo sugerido:

```text
Nuevo
```

> Importante: debes compartir la base de datos de Notion con la integración de Notion que uses en n8n. En Notion, abre la base de datos → menú `...` → `Connections` → añade tu integración.

---

## 5. Slack: enviar notificación

Después del nodo Notion, añade un nodo **Slack**.

Configuración:

- **Resource**: `Message`
- **Operation**: `Send`
- **Channel**: por ejemplo `#propuestas` o el canal que prefieras.

Mensaje sugerido:

```text
:new: *Nueva propuesta o cotización recibida*

*Remitente:* {{ $('Preparar datos del email').item.json.senderName || 'Sin nombre' }}
*Email:* {{ $('Preparar datos del email').item.json.senderEmail }}
*Asunto:* {{ $('Preparar datos del email').item.json.subject }}
*Fecha:* {{ $('Preparar datos del email').item.json.receivedAt }}

Registrado en Notion correctamente.
```

Si quieres incluir un enlace directo al registro de Notion, usa la URL devuelta por el nodo Notion, normalmente:

```javascript
{{ $json.url }}
```

Por ejemplo:

```text
:link: Ver en Notion: {{ $json.url }}
```

---

## Estructura final

```text
[Gmail Trigger]
       ↓
[Preparar datos del email - Code]
       ↓
[IF: asunto contiene propuesta o cotizacion]
       ↓ true
[Notion: Create Database Page]
       ↓
[Slack: Send Message]
```

## Recomendación para evitar duplicados

Aunque Gmail Trigger normalmente no repite mensajes, puedes añadir una validación adicional antes de crear la página en Notion:

```text
IF
  → Notion: buscar por “ID Gmail”
  → IF: no existe
  → Notion: crear página
  → Slack
```

Guarda siempre `gmailMessageId` en Notion y úsalo como identificador único. Así, aunque el workflow se ejecute dos veces sobre el mismo correo, no crearás registros ni notificaciones duplicadas.