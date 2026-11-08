# Grok 4.6 — multi_turn/requirements_change

- model_id: `x-ai/grok-4.6`
- success: True  | final: 4.21 | quality: 4.0
- latency_total: 22.357s | tokens_per_second: 73.5
- input_tokens: 425 | output_tokens: 1644

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

Perfecto, el flujo queda más útil así. Estructura:

**Gmail Trigger → Filter (asunto) → Extraer datos → Notion → Slack**

---

### 1. Gmail Trigger
- **Credential**: tu cuenta de Gmail (OAuth2)
- **Poll Times**: cada 1–5 min (o el intervalo que uses)
- **Simple**: deja el filtro de Gmail vacío; el filtro lo haces en N8N para no perder emails por sintaxis de Gmail
- Si quieres filtrar ya en Gmail: `subject:(propuesta OR cotizacion)` (Gmail no distingue tildes de forma fiable)

---

### 2. Filter (IF o Filter node)
Condición (OR):

- `{{ $json.subject }}` contains `propuesta` (ignore case)
- `{{ $json.subject }}` contains `cotizacion` (ignore case)

En un **IF** node:

```
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') || $json.subject.toLowerCase().includes('cotización') }}
```

Incluye `cotización` con tilde para no perder emails.

---

### 3. Extraer datos (Set o Code)
Campos típicos del Gmail node: `from`, `from.value[0].name`, `from.value[0].address`, `subject`, `date`, `text`, `html`, `id`.

**Set node** (recomendado):

| Nombre | Valor |
|---|---|
| `nombre` | `{{ $json.from.value[0].name \|\| '' }}` |
| `email` | `{{ $json.from.value[0].address }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |
| `snippet` | `{{ $json.textPlain \|\| $json.snippet \|\| '' }}` |
| `gmailId` | `{{ $json.id }}` |
| `threadId` | `{{ $json.threadId }}` |

Si el payload de tu versión de N8N trae `From` como string (`"Juan Pérez <juan@empresa.com>"`), usa un **Code** node:

```javascript
const item = $input.first().json;

function parseFrom(from) {
  if (!from) return { name: '', email: '' };
  if (typeof from === 'object') {
    const v = Array.isArray(from.value) ? from.value[0] : from;
    return { name: v.name || '', email: v.address || v.email || '' };
  }
  const m = String(from).match(/^(?:"?([^"<]*)"?\s*)?<([^>]+)>$/) || String(from).match(/([^<\s]+@[^>\s]+)/);
  if (m && m[2]) return { name: (m[1] || '').trim(), email: m[2].trim() };
  return { name: '', email: String(from).trim() };
}

const { name, email } = parseFrom(item.from || item.From);
const subject = item.subject || item.Subject || '';

return [{
  json: {
    nombre: name,
    email,
    asunto: subject,
    fecha: item.date || item.Date || new Date().toISOString(),
    snippet: (item.textPlain || item.snippet || item.text || '').slice(0, 500),
    gmailId: item.id,
    threadId: item.threadId || '',
  }
}];
```

---

### 4. Notion — Create Database Page
1. Crea una base en Notion, por ejemplo **Leads / Propuestas**, con propiedades:
   - **Nombre** (Title)
   - **Email** (Email)
   - **Asunto** (Rich text)
   - **Fecha** (Date)
   - **Snippet** (Rich text)
   - **Gmail ID** (Rich text) — útil para no duplicar
   - **Estado** (Select: Nuevo, Contactado, etc.)
2. Conecta la integración de Notion a esa página/base.
3. En N8N, nodo **Notion** → **Create Database Page**:
   - Database: tu base
   - Mapeo:
     - Title `Nombre` → `{{ $json.nombre || $json.email }}`
     - Email → `{{ $json.email }}`
     - Asunto → `{{ $json.asunto }}`
     - Fecha → `{{ $json.fecha }}`
     - Snippet → `{{ $json.snippet }}`
     - Gmail ID → `{{ $json.gmailId }}`
     - Estado → `Nuevo`

**Evitar duplicados (opcional):** antes del Create, un **Notion → Get Many** filtrando `Gmail ID equals {{ $json.gmailId }}`. Si hay resultados, salta el create (IF).

---

### 5. Slack — Send Message
Después de Notion (o en paralelo con Notion, mismo output del Set):

- Canal: `#leads` o el que uses
- Mensaje:

```
Nueva propuesta/cotización

De: {{ $json.nombre }} <{{ $json.email }}>
Asunto: {{ $json.asunto }}
Fecha: {{ $json.fecha }}

{{ $json.snippet }}
```

Si el Slack va **después** de Notion, las expresiones pueden ser `$json` del nodo Set, no del de Notion. Usa el nombre del nodo, por ejemplo:

`{{ $('Set datos').item.json.email }}`

---

### Orden de nodos

```
Gmail Trigger
    → IF (asunto contiene propuesta/cotizacion/cotización)
        true → Set / Code (extraer)
            → Notion (Create page)
            → Slack (Send message)
        false → (nada)
```

Notion y Slack pueden ir **en paralelo** desde el Set, para que un fallo de Notion no bloquee Slack (o al revés). Si quieres “solo avisar si se guardó en Notion”, déjalos en serie: Set → Notion → Slack.

---

### Credenciales que necesitas
- Gmail OAuth2 (scopes de lectura)
- Notion (Internal Integration + compartir la database)
- Slack (Bot token con `chat:write` en el canal)

---

### Detalles que suelen romper el flujo
- El Filter debe ir **después** del trigger, no dentro de Gmail, si quieres controlar tildes y mayúsculas.
- En Gmail Trigger, activa **Download Attachments** solo si los necesitas; si no, déjalo off.
- Timezone: convierte fecha a ISO si Notion Date no la acepta: `{{ $json.fecha }}`.
- Palabras extra: `presupuesto`, `quote`, `proposal` si te llegan en inglés.

Si quieres, el siguiente paso puede ser el JSON exportable del workflow (nodos + conexiones) listo para importar en N8N, o la versión con anti-duplicados por Gmail ID.