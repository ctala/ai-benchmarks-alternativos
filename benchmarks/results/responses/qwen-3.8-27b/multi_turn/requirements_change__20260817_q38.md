# Qwen 3.8 27B — multi_turn/requirements_change

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 4.18 | quality: 4.0
- latency_total: 57.768s | tokens_per_second: 30.5
- input_tokens: 275 | output_tokens: 1763

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



# Workflow N8N: Gmail → Filtro → Notion + Slack

## Estructura general

```
Gmail Trigger → IF (filtro) → Function (extraer datos) → Notion (crear página)
                                              ↓
                                        Slack (notificar)
```

---

## Nodo 1: Gmail Trigger

| Campo | Valor |
|-------|-------|
| **Authentication** | Gmail OAuth2 (configura tu cuenta) |
| **Event** | `Message Received` |
| **Poll time** | 1 min (o lo que prefieras) |
| **Filter** | (opcional) `has:unread` para no re-procesar |

> Asegúrate de que el OAuth2 de Gmail tenga el scope `gmail.readonly`.

---

## Nodo 2: IF (Filtro por asunto)

**Condiciones:**

| # | Campo | Operador | Valor | Lógica |
|---|-------|----------|-------|--------|
| 1 | `={{ $json.subject }}` | contains (case insensitive) | `propuesta` | — |
| 2 | `={{ $json.subject }}` | contains (case insensitive) | `cotizacion` | **OR** |

> ⚠️ **Importante:** En la configuración del nodo IF, cambia la lógica de las condiciones de **AND → OR** para que pase si contiene *cualquiera* de las dos palabras.

**Ramas:**
- **True** → va a Function
- **False** → se descarta (no pasa a ningún lado)

---

## Nodo 3: Function (Extraer y formatear datos)

**Type:** `Function` (Code node)

```javascript
const email = $input.first().json;

// Extraer datos del remitente
const sender = email.payload.from || email.payload.sender || {};
const senderName = sender.name || sender.email?.split('@')[0] || 'Desconocido';
const senderEmail = sender.email || sender.address || '';

// Formatear fecha
const date = email.payload.date ? new Date(email.payload.date).toISOString() : new Date().toISOString();

// Snippet del cuerpo (primeros 200 chars)
const body = (email.payload.text || email.payload.html || '').replace(/<[^>]*>/g, '').trim().substring(0, 200);

return [{
  json: {
    sender_name: senderName,
    sender_email: senderEmail,
    subject: email.payload.subject || '',
    date: date,
    snippet: body,
    // Campos para Notion (ajusta nombres a tu database)
    notion_sender: senderName,
    notion_email: senderEmail,
    notion_subject: email.payload.subject || '',
    notion_date: date,
    notion_snippet: body,
  }
}];
```

> Si la estructura de `payload` difiere según cómo N8N entrega el email, revisa el output del Gmail Trigger en modo debug y ajusta los campos.

---

## Nodo 4: Notion (Crear página)

| Campo | Valor |
|-------|-------|
| **Authentication** | Notion Integration Token |
| **Resource** | Database |
| **Operation** | Create Page |
| **Database ID** | `tu_database_id` (lo encuentras en la URL de la base) |
| **Property Names** | (ver abajo) |

**Mapeo de propiedades** (ajusta a los nombres exactos de tu database):

| Propiedad Notion | Valor |
|-----------------|-------|
| `Remitente` | `={{ $json.notion_sender }}` |
| `Email` | `={{ $json.notion_email }}` |
| `Asunto` | `={{ $json.notion_subject }}` |
| `Fecha` | `={{ $json.notion_date }}` |
| `Snippet` | `={{ $json.notion_snippet }}` |

> **Tip:** Crea la database en Notion con estos tipos:
> - Remitente → **Rich Text**
> - Email → **Rich Text**
> - Asunto → **Rich Text**
> - Fecha → **Date**
> - Snippet → **Rich Text**

---

## Nodo 5: Slack (Notificación)

Conéctalo **después de Notion** (así se notifica solo si el guardado fue exitoso).

| Campo | Valor |
|-------|-------|
| **Authentication** | Slack OAuth2 |
| **Operation** | Send Message |
| **Channel** | `#tu-canal` (ej: `#leads-propuestas`) |
| **Message** | (ver abajo) |

**Mensaje (multi-line):**

```
:envelope: *Nueva propuesta/cotización recibida*

*Remitente:* {{ $json.notion_sender }}
*Email:* {{ $json.notion_email }}
*Asunto:* {{ $json.notion_subject }}
*Fecha:* {{ $json.notion_date }}

> {{ $json.notion_snippet }}
```

> El Slack OAuth2 necesita el scope `chat:write`.

---

## Resumen del flujo

```
┌─────────────┐     ┌──────────┐     ┌────────────┐     ┌────────┐     ┌────────┐
│ Gmail       │────▶│ IF       │────▶│ Function   │────▶│ Notion │────▶│ Slack  │
│ Trigger     │     │ (filtro) │     │ (parsear)  │     │(crear) │     │(alert) │
└─────────────┘     └──────────┘     └────────────┘     └────────┘     └────────┘
                       False → ❌
```

---

## Checklist antes de activar

- [ ] OAuth2 de Gmail con scope `gmail.readonly`
- [ ] Integration Token de Notion con acceso a la database
- [ ] OAuth2 de Slack con scope `chat:write`
- [ ] Database de Notion creada con las propiedades correctas
- [ ] Canal de Slack existe y el bot tiene acceso
- [ ] Prueba con un email de prueba que tenga "propuesta" en el asunto

---

¿Quieres que te genere también un **error handler** (por ejemplo, si Notion falla, que te avise por Slack con el error) o que ajuste algo de la estructura?