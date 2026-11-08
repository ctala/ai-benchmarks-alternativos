# Nemotron 3 Ultra 550B — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.45 | quality: 4.0
- latency_total: 13.79s | tokens_per_second: 89.6
- input_tokens: 248 | output_tokens: 1236

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

Entendido. El flujo cambia a: **Gmail Trigger → Filtro → Notion + Slack**.

Aquí tienes la estructura exacta de nodos y la configuración clave:

---

### 1. **Gmail Trigger** (Trigger)
*   **Event**: `Message Received`
*   **Poll Times**: Cada 5 min (o lo que necesites)
*   **Options**: `Simple: false` (para tener acceso al `subject`, `from`, `body`, etc. completos).

---

### 2. **IF** (Filtro) — *Nombre sugerido: "¿Es propuesta/cotización?"*
*   **Mode**: `Boolean` (o "Conditions" en versiones nuevas)
*   **Condición 1 (Subject contiene 'propuesta')**:
    *   Value 1: `{{ $json.subject }}` → **String** → **Contains** → `propuesta` (activar *Case Insensitive*)
*   **Condición 2 (Subject contiene 'cotizacion')**:
    *   Value 1: `{{ $json.subject }}` → **String** → **Contains** → `cotizacion` (activar *Case Insensitive*)
*   **Logic**: `OR` (cumple cualquiera de las dos).
*   **Salida**: Conecta **True** al siguiente paso. **False** lo dejas suelto (o a un "No Op" si quieres loguear descartados).

> **Tip**: Si usas n8n nuevo (v1+), el node **Filter** es más limpio que el IF para esto. Mismo lógica: `subject` *contains* (case insensitive) `propuesta` **OR** `cotizacion`.

---

### 3. **Notion: Create Page** (Acción) — *Base de datos de leads/emails*
*   **Resource**: `Page` → **Operation**: `Create`
*   **Database ID**: Tu DB de Notion (selecciónala en el dropdown).
*   **Fields (mapeo clave)**:
    | Propiedad Notion (Tipo) | Expresión n8n |
    |-------------------------|---------------|
    | **Título** (Title) | `{{ $json.subject }}` |
    | **Remitente Nombre** (Rich Text / Text) | `{{ $json.from[0].name || 'Sin nombre' }}` |
    | **Remitente Email** (Email / Text) | `{{ $json.from[0].address }}` |
    | **Fecha** (Date) | `{{ $json.date }}` |
    | **Cuerpo / Snippet** (Rich Text) | `{{ $json.text?.substring(0, 2000) }}` *(limita a 2k chars)* |
    | **Message ID** (Text, único) | `{{ $json.messageId }}` *(útil para dedup futuro)* |
    | **Etiqueta** (Select/Multi-select) | `"Email Entrante"` (fijo) o dinámico según filtro |

---

### 4. **Slack: Post Message** (Acción) — *Notificación instantánea*
*   **Resource**: `Message` → **Operation**: `Post`
*   **Channel**: `#ventas` / `#leads` / tu canal.
*   **Text** (ejemplo con blocks simple):
    ```text
    📥 *Nueva propuesta/cotización*
    *Asunto:* {{ $json.subject }}
    *De:* {{ $json.from[0].name }} (<{{ $json.from[0].address }}>)
    *Fecha:* {{ $json.date }}
    *Vista previa:* {{ $json.text?.substring(0, 300) }}...
    ```
*   **Opcional**: `Blocks (JSON)` para botones ("Responder", "Ver en Notion" con URL de la page creada). Si quieres el link de Notion, necesitas pasar el `url` que devuelve el nodo Notion (usa **Merge** o **Set** entre Notion y Slack).

---

### Conexión final
```
Gmail Trigger → IF/Filter (True) → Notion Create Page → Slack Post Message
                              \
                               → (False) [opcional: log / ignore]
```

---

### Extras que te ahorrarán dolores de cabeza
1. **Deduplicación**: Gmail Trigger puede disparar doble. Guarda `messageId` en Notion (propiedad única) y antes de crear haz un **Notion: Search** o usa un **Set** con `{{ $json.messageId }}` + workflow static data para saltar repetidos.
2. **Adjuntos**: Si necesitas guardar PDFs en Notion/Drive, añade un **Gmail: Get Attachments** entre el filtro y Notion.
3. **Rate limits**: Notion y Slack tienen límites. Activa **Retry On Fail** en ambos nodos (Options → Retry On Fail: 3 veces, 30s).
4. **Testing**: En el Gmail Trigger usa "Execute Node" con un email de prueba real que tenga "propuesta" en el asunto.

---

¿Quieres el JSON del workflow para importarlo directo (`Workflows → Import`) o te armo el nodo **Set** intermedio para formatear el mensaje de Slack con el link de la page de Notion recién creada?