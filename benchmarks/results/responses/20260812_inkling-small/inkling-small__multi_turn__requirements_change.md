# Inkling Small — multi_turn/requirements_change

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 6.05 | quality: 6.0
- latency_total: 17.633s | tokens_per_second: 112.1
- input_tokens: 231 | output_tokens: 1977

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

Perfecto, entonces el flujo es:

**Gmail → Filtro por asunto → Extraer remitente → Notion (DB) + Slack (notificación)**

Aquí tienes la arquitectura paso a paso para construirlo en N8N:

### 1. Trigger: **Gmail** (New Email)
Configúralo para que lea la bandeja que quieras (o usa el nodo IMAP si prefieres). Trae el payload completo del mensaje.

---

### 2. Filtro: **IF** o **Filter** (condición)
No uses un nodo básico de texto; usa un nodo **IF** en modo **Expression** para que sea caso-insensible y cubra ambas palabras (con/sin tilde):

```expression
{{ ($json.subject || '').toLowerCase().includes('propuesta') || ($json.subject || '').toLowerCase().includes('cotizacion') || ($json.subject || '').toLowerCase().includes('cotización') }}
```
- **True** (sí pasa): continúa al flujo.
- **False** (no pasa): detén o ignora.

---

### 3. Extracción de datos: **Set** o **Function**
Usa un nodo **Set** para limpiar los datos del remitente y el mensaje antes de enviarlos a Notion/Slack:

| Campo | Expresión |
|-------|-----------|
| `nombre_remitente` | `{{ $json.from.name || $json.from.email || 'Sin nombre' }}` |
| `email_remitente` | `{{ $json.from.email }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date || $json.internalDate || $json.payload.headers.find(h => h.name === 'Date').value }}` |
| `snippet` | `{{ $json.snippet }}` |

---

### 4. Notion: **Notion** (Create Page / Add to Database)
Primero crea una base de datos en Notion con estas propiedades (ejemplo):

- **Nombre** (Title): nombre del remitente
- **Email** (Email): email
- **Asunto** (Rich text): asunto
- **Fecha** (Date): fecha del email

En el nodo Notion:
- **Operation**: `Create Page` (o `Create Database Item` si tu versión lo permite) apuntando a tu **Database ID**.
- **Properties**:
  - `Nombre` → `{{ $json.nombre_remitente }}`
  - `Email` → `{{ $json.email_remitente }}`
  - `Asunto` → `{{ $json.asunto }}`
  - `Fecha` → `{{ $json.fecha }}`

> **Nota:** Necesitas la integración de Notion con token y el ID de la base de datos.

---

### 5. Notificación: **Slack** (Post Message)
Después del nodo Notion (o en paralelo si usas un **Split In Batches** / **Merge**, pero aquí es secuencial), envía al canal que quieras (`#propuestas`, `#ventas`, etc.):

- **Channel**: `#tu-canal`
- **Text**:
```text
📩 *Nueva propuesta/cotización recibida*

*Remitente:* {{ $json.nombre_remitente }} <{{ $json.email_remitente }}>
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
```

---

### Flujo visual resumido:
```
[Gmail Trigger]
    ↓
[IF: ¿asunto tiene propuesta/cotizacion?]
    ↓ (True)
[Set: extraer remitente / asunto / fecha]
    ↓
[Notion: Crear entrada en DB]
    ↓
[Slack: Enviar alerta]
```

### Tips rápidos:
- Asegúrate de que el nodo Gmail esté configurado con la cuenta correcta (OAuth2 o credenciales de app).
- Si el asunto viene con HTML o espacios raros, pon un nodo **Code** antes del IF para limpiar: `{{ $json.subject.replace(/<[^>]*>/g, '').trim() }}`.
- Si quieres que el mensaje de Slack sea más "bonito", usa un nodo **Markdown** o arma un bloque con attachments.

¿Necesitas que te pase el JSON exacto de los nodos o que detalle cómo configurar la base de datos de Notion con las propiedades exactas?