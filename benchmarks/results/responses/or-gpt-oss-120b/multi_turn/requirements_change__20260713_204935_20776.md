# GPT-OSS 120B — multi_turn/requirements_change

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 4.71 | quality: 4.0
- latency_total: 41.481s | tokens_per_second: 49.4
- input_tokens: 285 | output_tokens: 2048
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos especificados, ya que introduce Notion y Slack en lugar de Google Sheets, lo cual es irrelevante para la tarea original.

## Respuesta completa

## 📋 Resumen del flujo

| Paso | Nodo (n8n) | Qué hace | Comentario |
|------|------------|----------|------------|
| 1️⃣ | **Gmail Trigger** | Detecta cada email nuevo en la cuenta de Gmail | Se dispara solo cuando llega un mensaje nuevo |
| 2️⃣ | **IF (Filtro de asunto)** | Descarta los correos que **no** contengan “propuesta” o “cotización” en el asunto | Usa una expresión regular para que sea insensible a mayúsculas/minúsculas |
| 3️⃣ | **Function (Parsear datos)** | Extrae y formatea la información del remitente (nombre, email), asunto y fecha | Opcional: puedes añadir más campos (cuerpo, adjuntos…) |
| 4️⃣ | **Notion → Create Page** | Crea una nueva página/registro en la base de datos de Notion con los datos extraídos | Necesitas una base de datos con columnas: `Remitente`, `Email`, `Asunto`, `Fecha`, `ID del correo` (opcional) |
| 5️⃣ | **Slack → Send Message** | Envía una notificación a un canal o DM de Slack con un resumen del email | Puedes personalizar el mensaje con emojis, enlaces al registro de Notion, etc. |
| 6️⃣ (opcional) | **Error Workflow** | Captura errores y los envía a Slack o a un email de admin | Muy útil en producción |

A continuación tienes la configuración paso‑a‑paso de cada nodo, con ejemplos concretos y los fragmentos de código que necesitarás.

---

## 1️⃣ Gmail Trigger – “Watch Emails”

| Campo | Valor | Comentario |
|-------|-------|------------|
| **Resource** | `Message` | |
| **Operation** | `Watch` (o `Get All` si prefieres polling) | `Watch` usa push (Webhooks) y es más instantáneo |
| **Mailbox** | `INBOX` | Cambia si usas otro label |
| **Include Attachments** | `No` (a menos que los necesites) |
| **Mark As Read** | `Yes` (opcional) | Evita volver a procesar el mismo mensaje |
| **Trigger on** | `New Email` | |
| **Filters** | **Leave empty** – el filtrado lo haremos después | |

> **Nota**: Si tu cuenta está bajo G‑Suite con 2FA, crea una *App password* o habilita OAuth2 en n8n → **Credentials → Gmail OAuth2**.

---

## 2️⃣ IF – Filtrar por asunto

### Configuración del nodo

1. **Add Condition** → `String` → `Subject` (campo del mensaje de Gmail)  
2. **Operation** → `Matches (RegExp)`  
3. **Value** → `(?i)\\b(propuesta|cotizacion)\\b`

- `(?i)` = case‑insensitive.  
- `\\b` = límite de palabra, evita coincidencias parciales (p.ej. “repropuesta”).

### Resultado

- **True** → pasa al siguiente nodo (emails que sí contienen la palabra).  
- **False** → se descarta (puedes conectar a un nodo *No Operation* si quieres registrar que se ignoró).

---

## 3️⃣ Function – Parsear y formatear datos

Copia este código en el **Function node** (puedes llamarlo *Parse Email*):

```javascript
// Entrada: item0 = email de Gmail
const email = items[0].json;

// Helper para extraer nombre y email del campo "From"
function parseFrom(fromHeader) {
  // Ejemplo: "Juan Pérez <juan.perez@example.com>"
  const match = fromHeader.match(/^(.*?)(?:\s*<([^>]+)>)?$/);
  if (!match) return { name: '', address: '' };
  const name = match[1].replace(/["']/g, '').trim();
  const address = match[2] ? match[2].trim() : '';
  return { name, address };
}

const { name, address } = parseFrom(email.from);
const subject = email.subject || '';
const date = new Date(email.internalDate).toISOString(); // formato ISO para Notion
const messageId = email.id; // opcional: guardamos el ID para evitar duplicados

return [
  {
    json: {
      remitenteNombre: name,
      remitenteEmail: address,
      asunto: subject,
      fecha: date,
      gmailMessageId: messageId,
    },
  },
];
```

> **Resultado**: Cada ejecución entrega un objeto con los campos que vamos a enviar a Notion y a Slack.

---

## 4️⃣ Notion – Create Page

### Preparación en Notion

1. Crea una **Base de datos** (Table, Board, List…) en la página donde quieras almacenar los correos.  
2. Añade las siguientes propiedades (tipo *Text* o *Date*):
   - `Remitente` (texto)
   - `Email` (texto)
   - `Asunto` (texto)
   - `Fecha` (date)
   - `Gmail ID` (texto, opcional, para evitar duplicados)
3. Copia el **Database ID** de la URL: `https://www.notion.so/…/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=…` → la parte después del último `/` y antes de `?v=`.

### Configuración del nodo

| Campo | Valor |
|-------|-------|
| **Resource** | `Database` |
| **Operation** | `Create` |
| **Database ID** | *pega aquí el ID de tu tabla* |
| **Page Properties** | Mapea cada propiedad con los datos del Function node: |
| `Remitente` | `{{ $json["remitenteNombre"] }}` |
| `Email` | `{{ $json["remitenteEmail"] }}` |
| `Asunto` | `{{ $json["asunto"] }}` |
| `Fecha` | `{{ $json["fecha"] }}` |
| `Gmail ID` | `{{ $json["gmailMessageId"] }}` |
| **Add to Parent** | (opcional) si quieres que la página se cree dentro de una sub‑página o workspace específico. |
| **Credentials** | Notion OAuth2 (crea credencial una vez y reutilízala). |

> **Tip**: Si tu base de datos tiene una columna de tipo *Select* o *Multi‑Select*, usa la sintaxis: `{{ ["Valor1","Valor2"] }}`.

---

## 5️⃣ Slack – Send Message

### Configuración básica

| Campo | Valor |
|-------|-------|
| **Resource** | `Message` |
| **Operation** | `Send` |
| **Channel** | `#general` (o el canal que prefieras) |
| **Message** | Usa plantilla **Mustache** (n8n lo interpreta automáticamente): |

```markdown
🚀 *Nuevo email con propuesta/cotización* 🚀
*Remitente:* {{ $json["remitenteNombre"] }} <{{ $json["remitenteEmail"] }}>
*Asunto:* {{ $json["asunto"] }}
*Fecha:* {{ $json["fecha"] }}

🔗 <https://www.notion.so/{{ $json["gmailMessageId"] }}|Ver registro en Notion>
```

> **Enlace a Notion**: Si quieres que el link abra directamente la página creada, usa la propiedad `id` que Notion devuelve en la respuesta del nodo **Create Page**. Por ejemplo, conecta la salida del nodo Notion a un **Set** que guarde `pageId = $json["id"]` y luego usa `https://www.notion.so/<pageId>` en el mensaje.

### Opciones extra

- **Attachments**: Puedes adjuntar el snippet del cuerpo del email (`{{ $json["body"] }}`) o enlaces a archivos si los descargaste previamente.
- **Mention**: `<!channel>` o `<!here>` para notificar a todo el equipo.

---

## 6️⃣ (Opcional) Manejo de errores – “Error Workflow”

1. **Add a “Error Trigger”** al final del workflow (o usa la opción *Execute Workflow on Error*).  
2. Conecta a otro **Slack → Send Message** con un texto como:

```markdown
⚠️ *Error en el workflow de Gmail → Notion* ⚠️
*Workflow:* {{ $workflow.id }}
*Error:* {{ $error.message }}
```

3. (Opcional) Añade un **Email → Send** a tu propio correo de admin.

---

## 📐 Diagrama rápido (texto)

```
[Gmail Trigger] → [IF (asunto contiene propuesta|cotizacion)] → (True)
          |                                         |
          └─ (False) ──► [No Operation]             |
                                                   ↓
                                            [Function: Parse Email]
                                                  