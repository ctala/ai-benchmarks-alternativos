# MiMo V2.6 Pro — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 4.63 | quality: 4.0
- latency_total: 21.043s | tokens_per_second: 62.6
- input_tokens: 244 | output_tokens: 1318

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

Perfecto, vamos a reestructurar el workflow. Aquí tienes la arquitectura actualizada:

---

## 🔄 Workflow: Gmail → Filtro → Notion + Slack

### Estructura general

```
Gmail Trigger → IF (filtro asunto) → Set (extraer datos) → Notion (guardar) → Slack (notificar)
```

---

### 1️⃣ Gmail Trigger

**Tipo:** Gmail Trigger (o Webhook si prefieres polling)

| Campo | Valor |
|---|---|
| Evento | Message Received |
| Label | INBOX (o específica) |
| Poll cada | Cada 5 minutos |
| Devolver | Full Message |

---

### 2️⃣ IF Node — Filtrar por asunto

Este nodo revisa si el asunto contiene las palabras clave.

| Campo | Valor |
|---|---|
| Condición 1 | `{{ $json.subject }}` **contains** `propuesta` |
| Operador | **OR** |
| Condición 2 | `{{ $json.subject }}` **contains** `cotizacion` |

> 💡 **Tip:** Si necesitas que sea insensible a mayúsculas, usa un **Code Node** antes con:
> ```javascript
> const subject = $json.subject.toLowerCase();
> return [{ json: { ...$json, subject_lower: subject } }];
> ```
> Y luego filtras por `subject_lower`.

**Si es FALSO** → el workflow termina ahí (no pasa nada).

---

### 3️⃣ Set Node — Extraer datos del remitente

**Tipo:** Set Node

Crea estos campos:

| Nombre del campo | Value (expresión) |
|---|---|
| `remitente_nombre` | `{{ $json.from.value[0].name }}` |
| `remitente_email` | `{{ $json.from.value[0].address }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |
| `vista_previa` | `{{ $json.snippet }}` |
| `enlace` | `https://mail.google.com/mail/u/0/#inbox/{{ $json.id }}` |

> Con esto tienes todo limpio y listo para las siguientes conexiones.

---

### 4️⃣ Notion Node — Guardar en base de datos

**Tipo:** Notion → **Create a Page**

| Campo | Valor |
|---|---|
| Resource | Database |
| Operation | Create |
| Database | Tu base de datos de Notion |

**Mapeo de propiedades** (ejemplo de campos en Notion):

| Propiedad en Notion | Tipo | Value |
|---|---|---|
| Nombre | Title | `{{ $json.remitente_nombre }}` |
| Email | Text | `{{ $json.remitente_email }}` |
| Asunto | Text | `{{ $json.asunto }}` |
| Fecha | Date | `{{ $json.fecha }}` |
| Vista previa | Text | `{{ $json.vista_previa }}` |
| Enlace | URL | `{{ $json.enlace }}` |
| Estado | Select | `Nuevo` |

---

### 5️⃣ Slack Node — Notificación

**Tipo:** Slack → **Send Message**

| Campo | Valor |
|---|---|
| Channel | `#tu-canal` (o un canal específico) |
| Text | Ver abajo 👇 |

**Mensaje sugerido:**

```
📧 *Nuevo email detectado*
• *De:* {{ $json.remitente_nombre }} ({{ $json.remitente_email }})
• *Asunto:* {{ $json.asunto }}
• *Fecha:* {{ $json.fecha }}
🔗 <{{ $json.enlace }}|Ver en Gmail>
```

---

### 📋 Resumen visual del flujo

```
[⏰ Gmail Trigger]
       │
       ▼
[🔀 IF: asunto contiene "propuesta" OR "cotizacion"]
       │
    ✅ TRUE
       │
       ▼
[📝 Set: extraer nombre, email, asunto, fecha, preview]
       │
       ├──▶ [📓 Notion: crear página en base de datos]
       │
       └──▶ [💬 Slack: enviar notificación al canal]
```

---

### ⚠️ Notas importantes

1. **Credenciales**: Necesitas configurar las credenciales de **Gmail OAuth2**, **Notion API** y **Slack OAuth2** en N8N
2. **Notion**: La base de datos debe compartirse con la integración de N8N (en Notion: Share → Invite tu integración)
3. **Slack**: Tu app de Slack necesita los scopes `chat:write` y `channels:read`
4. **Duplicados**: Si quieres evitar duplicados, agrega un nodo **Google Sheets** o un **lookup en Notion** antes de guardar

---

Quieres que te detalle algún nodo con más profundidad, o prefieres que genere el JSON del workflow para importarlo directamente en N8N?