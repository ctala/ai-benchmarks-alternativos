# Qwen 3.8 Flash — multi_turn/requirements_change

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 6.09 | quality: 6.0
- latency_total: 33.131s | tokens_per_second: 56.8
- input_tokens: 275 | output_tokens: 1882

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

Buen cambio. Con Notion + Slack el flujo queda así:

**Gmail Trigger → Function/IF de filtrado → Notion (crear página) → Slack (notificación)**

Te dejo el workflow detallado:

---

## 1. Gmail Trigger

**Nodo:** `Gmail Trigger`

Configuración recomendada:

- **Event:** `Email Received`
- **Poll Times:** cada 5 min
- **Query de Gmail:**

```text
subject:(propuesta OR cotizacion OR cotización)
```

Esto ya reduce el volumen antes de entrar a N8N.

### Campos importantes que trae Gmail

Depende de cómo lo configures, pero normalmente tendrás:

```json
{
  "from": "Nombre del remitente <email@dominio.com>",
  "subject": "Propuesta comercial",
  "date": "2025-01-20T10:30:00Z",
  "id": "18f...",
  "threadId": "18f...",
  "snippet": "..."
}
```

---

## 2. Function node para extraer y limpiar datos

**Nodo:** `Function`

Código sugerido:

```javascript
const item = $input.first().json;

const fromRaw = item.from || "";
const subject = item.subject || "";

// Extraer nombre y email
let senderName = "";
let senderEmail = "";

const emailMatch = fromRaw.match(/<([^>]+)>/);
if (emailMatch) {
  senderEmail = emailMatch[1].trim().toLowerCase();
  senderName = fromRaw.replace(/<[^>]+>/, "").trim();
} else {
  senderEmail = fromRaw.trim().toLowerCase();
  senderName = fromRaw.trim();
}

// Normalizar asunto
const subjectNormalized = subject
  .toLowerCase()
  .normalize("NFD")
  .replace(/[\u0300-\u036f]/g, "");

// Filtro por palabras clave
const keywords = ["propuesta", "cotizacion"];

const matches = keywords.some(keyword =>
  subjectNormalized.includes(keyword)
);

if (!matches) {
  return [];
}

return [{
  json: {
    senderName,
    senderEmail,
    subject,
    receivedAt: item.date || new Date().toISOString(),
    gmailId: item.id,
    threadId: item.threadId,
    snippet: item.snippet || "",
    bodyPreview: item.snippet || ""
  }
}];
```

---

## 3. Notion: crear página

**Nodo:** `Notion`

Configuración:

- **Resource:** `Database Page`
- **Operation:** `Create`
- **Base:** selecciona tu base de datos de Notion

### Estructura recomendada en Notion

Crea una base con estas propiedades:

| Propiedad Notion | Tipo |
|---|---|
| `Remitente` | Title |
| `Email` | Email |
| `Asunto` | Rich text |
| `Fecha` | Date |
| `Gmail ID` | Text |
| `Snippet` | Rich text |

### Mapeo de propiedades en N8N

En el nodo Notion, usa expresiones:

```json
{
  "Remitente": "={{ $json.senderName || $json.senderEmail }}",
  "Email": "={{ $json.senderEmail }}",
  "Asunto": "={{ $json.subject }}",
  "Fecha": "={{ $json.receivedAt }}",
  "Gmail ID": "={{ $json.gmailId }}",
  "Snippet": "={{ $json.snippet }}"
}
```

---

## 4. Slack: notificación

**Nodo:** `Slack`

Configuración:

- **Resource:** `Message`
- **Operation:** `Send`
- **Send To:** `Channel`
- **Channel:** tu canal, por ejemplo:

```text
#ventas
```

### Mensaje sugerido

```text
📩 Nuevo email con propuesta/cotización

👤 Remitente: {{ $json.senderName || $json.senderEmail }}
📧 Email: {{ $json.senderEmail }}
📌 Asunto: {{ $json.subject }}
📅 Fecha: {{ $json.receivedAt }}
```

Si quieres que Slack reciba los datos del paso anterior, conecta:

```text
Notion → Slack
```

y en Slack usa:

```text
{{ $('Function').item.json.senderName }}
```

o directamente:

```text
{{ $json.senderName }}
```

si el nodo Notion no modifica el JSON.

---

## 5. Evitar duplicados

Esto es importante porque Gmail puede reintentar o duplicar eventos.

### Opción simple

Usa `Gmail ID` como clave única en Notion.

Antes de crear la página, puedes agregar:

1. **Notion → Database Page → Get Many**
2. Filtro:

```json
{
  "property": "Gmail ID",
  "title": {
    "equals": "={{ $('Function').first().json.gmailId }}"
  }
}
```

3. **IF**

```text
{{ $json.results.length === 0 }}
```

Si no existe, crear en Notion.  
Si existe, ignorar.

---

## 6. Versión más robusta del flujo

El flujo ideal sería:

```text
Gmail Trigger
    ↓
Function: extraer datos + filtrar
    ↓
Notion: buscar si ya existe por Gmail ID
    ↓
IF: no existe
    ↓
Notion: crear página
    ↓
Slack: notificar
```

---

## 7. Credenciales necesarias

Debes configurar en N8N:

### Gmail

- OAuth2
- Scope mínimo:

```text
https://www.googleapis.com/auth/gmail.readonly
```

### Notion

- Internal Integration Token
- Base compartida con la integración
- Propiedades visibles para la integración

### Slack

- OAuth o token de bot
- Scope:

```text
chat:write
```

- Canal donde N8N pueda escribir

---

## 8. Consideraciones importantes

### Acentos

Tu filtro debe contemplar:

```text
cotización
cotizacion
Propuesta
PROPUESTA
```

La función que te pasé normaliza mayúsculas y acentos, así que funciona mejor.

### Gmail Trigger vs Gmail Node

Usa **Gmail Trigger**, no solo **Gmail** node.  
El trigger es el que escucha eventos nuevos.

### Latencia

N8N no recibe webhooks de Gmail de forma inmediata. Con `Gmail Trigger` normalmente hace polling cada pocos minutos.

Si necesitas casi tiempo real, tendrías que usar:

```text
Pub/Sub Push → Webhook → N8N
```

pero es más complejo.

---

## 9. Resumen final del workflow

```text
1. Gmail Trigger
   - Escucha emails nuevos
   - Filtro opcional: subject:(propuesta OR cotizacion OR cotización)

2. Function
   - Extrae nombre y email
   - Normaliza asunto
   - Filtra solo si contiene propuesta o cotizacion

3. Notion
   - Crea una página en base de datos
   - Guarda remitente, email, asunto, fecha, Gmail ID

4. Slack
   - Envía notificación al canal
```

---

Si quieres, te puedo dar el **JSON completo del workflow de N8N** listo para importar.