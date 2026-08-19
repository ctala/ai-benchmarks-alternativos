# Grok 4.6 — multi_turn/requirements_change

- model_id: `x-ai/grok-4.6`
- success: True  | final: 4.06 | quality: 4.0
- latency_total: 35.159s | tokens_per_second: 47.5
- input_tokens: 425 | output_tokens: 1671

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

Flujo actualizado: Gmail → filtrar asunto → extraer datos → Notion → Slack.

## Flujo

```
Gmail Trigger → IF (asunto) → Set (datos) → Notion → Slack
```

Si el asunto no coincide, el IF corta el flujo y no se crea nada en Notion ni se notifica.

---

## 1. Gmail Trigger

- **Node:** Gmail Trigger
- **Event:** Message Received
- **Simplify:** On (más fácil de mapear)
- **Poll Times:** cada 1 minuto (o el intervalo que uses)

Campos útiles que llegan:
- `From` / `from`
- `Subject` / `subject`
- `Date` / `date`
- `snippet` o `text`

Si usas el modo no simplificado, el asunto suele estar en `headers` y el remitente en `payload.headers`. Con **Simplify** evitas parsear headers.

---

## 2. IF — solo “propuesta” o “cotización”

- **Node:** IF
- **Combinator:** OR
- **Condition 1:** String → `{{$json.subject}}` → **contains** → `propuesta` → Case Insensitive: On
- **Condition 2:** String → `{{$json.subject}}` → **contains** → `cotizacion` → Case Insensitive: On
- **Condition 3 (recomendado):** String → `{{$json.subject}}` → **contains** → `cotización` → Case Insensitive: On

Conecta **solo la salida true** al siguiente nodo.

Si tu Gmail Trigger no trae `subject`, usa:

```
{{$json.Subject}}
```

o, en modo raw:

```
{{$json.payload.headers.find(h => h.name.toLowerCase() === 'subject').value}}
```

---

## 3. Set — normalizar remitente y asunto

- **Node:** Set (o Edit Fields)
- **Mode:** Manual Mapping

Campos:

| Nombre | Valor |
|---|---|
| `email` | `{{$json.from.value[0].address}}` |
| `nombre` | `{{$json.from.value[0].name \|\| $json.from.value[0].address}}` |
| `asunto` | `{{$json.subject}}` |
| `fecha` | `{{$json.date}}` |
| `snippet` | `{{$json.snippet}}` |
| `gmailId` | `{{$json.id}}` |

Si con Simplify el `from` llega como string (`"Ana Pérez <ana@empresa.com>"`), usa un **Code** node en vez de Set:

```javascript
const item = $input.first().json;

const fromRaw = item.from || item.From || '';
const match = String(fromRaw).match(/^(?:"?([^"<]*)"?\s*)?<?([^>]+@[^>]+)>?$/);

const nombre = (match?.[1] || '').trim();
const email = (match?.[2] || String(fromRaw)).trim();

return [{
  json: {
    nombre: nombre || email,
    email,
    asunto: item.subject || item.Subject || '',
    fecha: item.date || item.internalDate || new Date().toISOString(),
    snippet: item.snippet || '',
    gmailId: item.id || ''
  }
}];
```

---

## 4. Notion — crear página / registro

Primero crea una base en Notion con estas propiedades:

| Propiedad Notion | Tipo |
|---|---|
| Nombre | Title |
| Email | Email |
| Asunto | Text |
| Fecha | Date |
| Snippet | Text |
| Gmail ID | Text (útil para no duplicar) |
| Estado | Select (`Nuevo`, `Revisado`) |

**Node:** Notion  
**Resource:** Database Page  
**Operation:** Create  
**Database:** tu base de leads/propuestas

Mapeo:

- **Nombre (title):** `{{$json.nombre}}`
- **Email:** `{{$json.email}}`
- **Asunto:** `{{$json.asunto}}`
- **Fecha:** `{{$json.fecha}}`
- **Snippet:** `{{$json.snippet}}`
- **Gmail ID:** `{{$json.gmailId}}`
- **Estado:** `Nuevo`

Credenciales: conexión Notion con acceso a esa database (share the integration to the page).

---

## 5. Slack — aviso

- **Node:** Slack
- **Resource:** Message
- **Operation:** Post
- **Channel:** `#leads` o el que uses
- **Text:**

```
Nueva propuesta/cotización

De: {{$json.nombre}} <{{$json.email}}>
Asunto: {{$json.asunto}}
Fecha: {{$json.fecha}}

{{$json.snippet}}
```

Si el Slack queda **después** de Notion, los campos siguen disponibles si Notion no pisa el JSON. Para no depender de eso, pon Slack **en paralelo** con Notion desde el Set/Code:

```
Set/Code ─┬─→ Notion
          └─→ Slack
```

Así la notificación no falla si Notion da error, o al revés.

Si quieres Slack **solo si Notion se creó bien**, déjalo en serie: Set → Notion → Slack.

---

## Conexiones

**Opción A — Slack independiente (recomendada):**

1. Gmail Trigger → IF  
2. IF (true) → Code/Set  
3. Code/Set → Notion  
4. Code/Set → Slack  

**Opción B — Slack solo si se guardó:**

1. Gmail Trigger → IF  
2. IF (true) → Code/Set → Notion → Slack  

---

## Extra útil (opcional)

**Evitar duplicados**  
Antes de Notion, un Notion **Get Many / Search** filtrando `Gmail ID equals {{$json.gmailId}}`. Si ya existe, no crees otra página.

**Filtro también en Gmail**  
En el trigger puedes poner un filtro Gmail, por ejemplo:

```
subject:(propuesta OR cotizacion OR cotización)
```

Eso reduce ejecuciones. Igual deja el IF por si el filtro de Gmail no cubre acentos o mayúsculas.

**Etiquetar el mail**  
Después de procesarlo, un Gmail node **Add Label** (`Procesado`) para no reprocesar si cambias el trigger a “unseen”.

---

## Checklist de credenciales

- Gmail OAuth2 con scope de leer correo  
- Notion integration invitada a la database  
- Slack bot con `chat:write` en el canal  

Si quieres, en el siguiente mensaje te armo el JSON exportable del workflow (nodos + connections) listo para importar en n8n. Dime solo: ¿Notion Database Page o Notion como tabla simple, y Slack en paralelo o después de Notion?