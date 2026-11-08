# Kimi K2.5 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 5.32 | quality: 6.0
- latency_total: 167.445s | tokens_per_second: 26.6
- input_tokens: 266 | output_tokens: 4457

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

Aquí tienes el workflow paso a paso. Es un flujo **Trigger → Parseo → Filtro → Guardar → Notificar**.

---

### 🔧 Arquitectura del Workflow

```
[Gmail Trigger] 
      ↓
[Code: Parsear Remitente]
      ↓
[IF: Filtro Asunto]
      ↓ (true)
[Notion: Crear DB Item] → [Slack: Enviar Mensaje]
```

---

### 1️⃣ Gmail Trigger (On Message Received)
- **Credential:** Conecta tu cuenta de Google (OAuth2).
- **Event:** `On Message Received` (es polling, revisa cada X minutos).
- **Label:** `INBOX` (o la etiqueta que uses para negocios).
- **Format:** `Resolved` (te da el texto limpio del email).
- **Options:** Deja `Download Attachments` en **false** para ahorrar cuota.

> ⚠️ **Tip:** La primera vez que actives el workflow, si tienes muchos emails sin leer, N8N puede procesarlos todos. Te recomiendo marcar como leídos los viejos antes de activarlo, o agregar un nodo "NoOp" con límite de ejecución en las primeras pruebas.

---

### 2️⃣ Code Node: Extraer Nombre y Email
El campo `from` de Gmail viene como `Juan Pérez <juan@empresa.com>`. Úsalo para separar datos limpios antes de mandarlos a Notion.

**Añade un nodo "Code"** y pega esto:

```javascript
const results = [];

for (const item of $input.all()) {
  const fromRaw = item.json.from || '';
  // Regex para separar "Nombre" <email>
  const match = fromRaw.match(/^(.*)<([^>]+)>$/);
  
  const nombre = match ? match[1].trim().replace(/"/g, '') : fromRaw;
  const email = match ? match[2].trim() : '';
  
  results.push({
    json: {
      nombre_remitente: nombre,
      email_remitente: email,
      asunto: item.json.subject,
      fecha: item.json.receivedDate, // Notion prefiere ISO 8601
      snippet: item.json.snippet,
    }
  });
}

return results;
```

---

### 3️⃣ IF Node: Filtro "Propuesta / Cotización"
Aquí filtras solo los que interesan. Te doy **dos opciones**:

#### Opción A (Simple): Contains
- **Mode:** ANY
- **Condition 1:** `asunto` → **Contains** → `propuesta` → **Ignore Case: true**
- **Condition 2:** `asunto` → **Contains** → `cotizacion` → **Ignore Case: true**
- **Condition 3:** `asunto` → **Contains** → `cotización` → **Ignore Case: true** *(por si usan tilde)*

#### Opción B (Pro): Regex
- **Condition 1:** `asunto` → **Regex** → 
  ```
  (?i)(propuesta|cotizaci[oó]n)
  ```
*(El `(?i)` lo hace case-insensitive y captura "cotizacion" y "cotización" de una)*

- Conecta el cable **true** al nodo Notion. El **false** lo dejas sin conectar (o a un NoOp).

---

### 4️⃣ Notion: Crear Página en Base de Datos
**Requisito previo:** Tener una integración de Notion (Internal Integration) y compartirle tu base de datos.

- **Operation:** Create a Database Item
- **Database:** Selecciona tu DB (o pega el Database ID).
- **Mapeo de propiedades** (ajusta según los nombres exactos de tu DB en Notion):

| Propiedad en Notion | Tipo en Notion | Valor en N8N |
|---|---|---|
| `Nombre` | Title | `{{ $json.nombre_remitente }}` |
| `Email` | Email | `{{ $json.email_remitente }}` |
| `Asunto` | Rich Text | `{{ $json.asunto }}` |
| `Fecha` | Date | `{{ $json.fecha }}` |
| `Estado` | Select | `Nuevo Lead` *(opcional)* |
| `Origen` | Rich Text | `Gmail` *(opcional)* |

> ⚠️ **Tip crítico:** Los nombres de las propiedades en Notion deben coincidir **exactamente** (mayúsculas, tildes y espacios). Si una propiedad es tipo `Email`, Notion validará que sea un formato de email válido.

---

### 5️⃣ Slack: Notificación
- **Credential:** Conecta Slack por OAuth o Incoming Webhook.
- **Operation:** Post to Channel (o Send Message).
- **Channel:** `#leads`, `#ventas` o el que uses.
- **Message Text:**

```
🚀 *Nuevo lead por email*

👤 *Nombre:* {{ $json.nombre_remitente }}
📧 *Email:* {{ $json.email_remitente }}
📝 *Asunto:* {{ $json.asunto }}
📅 *Fecha:* {{ $json.fecha }}
✅ Guardado en Notion.
```

---

### 📋 Checklist antes de activar

1. **Gmail:** Tener la API de Gmail habilitada en Google Cloud y las credenciales OAuth en N8N.
2. **Notion:** 
   - Crear integración en [notion.so/my-integrations](https://notion.so/my-integrations).
   - Compartir la base de datos con la integración (botón *Share* → Invite → tu integración).
   - Verificar que los tipos de propiedad coincidan con los datos que envías.
3. **Slack:** Crear una app en tu workspace o usar un Webhook URL.
4. **Fechas:** Si Notion rechaza el formato de fecha, añade un nodo **Date & Time** entre el Code y Notion para formatear `receivedDate` a ISO (ej: `YYYY-MM-DDTHH:mm:ss`).

---

### 🛡️ Errores comunes a evitar

| Problema | Solución |
|---|---|
| Notion dice "property not found" | Revisa que el nombre de la propiedad en N8N sea **idéntico** al de Notion. |
| Slack no notifica | Revisa que el bot tenga permisos en el canal o que el Webhook esté activo. |
| El filtro atrapa emails viejos | El trigger es por polling; usa la condición regex y asegúrate de que el intervalo de polling no sea muy agresivo (ej: cada 5 min). |
| El nombre del remitente viene vacío | Algunos emails solo traen el email sin nombre. El código ya contempla eso y deja el email como nombre. |

---

Si quieres, **te puedo generar el JSON listo para importar** en N8N. Solo dime los nombres exactos de las propiedades de tu base de datos en Notion y el canal de Slack, y lo armo para que lo copies y pegues. ¿Te sirve?