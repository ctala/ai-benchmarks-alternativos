# Qwen 3.7 Flash — multi_turn/requirements_change

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 4.88 | quality: 4.0
- latency_total: 31.915s | tokens_per_second: 81.1
- input_tokens: 233 | output_tokens: 2588

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

Excelente ajuste. Cambiar el destino a Notion y añadir un filtro por palabra clave + notificación a Slack es un patrón muy común y totalmente viable en n8n. Aquí tienes la guía paso a paso para construirlo:

### 🔹 Flujo General
`Gmail Trigger` → `IF` (filtro por asunto) → `Set` (mapeo limpio) → `Notion` (crear página) → `Slack` (notificar)

---

### 🛠️ Configuración Nodo a Nodo

#### 1. **Gmail Trigger**
- **Connection**: Autenticación OAuth2 con tu cuenta de Gmail.
- **Event**: `New emails`
- **Polling Interval**: `5 minutes` (recomendado para no saturar límites).
- ⚠️ n8n maneja automáticamente la deduplicación interna, así que no procesará dos veces el mismo email.

#### 2. **IF Node** (Filtro)
- **Condition**: Usa esta expresión en el campo `Expression`:
  ```javascript
  {{ $json.subject?.toLowerCase()?.includes('propuesta') || $json.subject?.toLowerCase()?.includes('cotización') }}
  ```
- **True Route**: Continúa al siguiente nodo.
- **False Route**: Conecta a un `End` o a un `Log` opcional.

#### 3. **Set Node** (Estructurar datos)
Aquí normalizas los campos para que Notion y Slack los reciban limpios. Configura las propiedades manualmente:
| Propiedad | Valor (expresión n8n) |
|-----------|------------------------|
| `sender_name` | `{{ $json.from.name || $json.from.address }}` |
| `sender_email` | `{{ $json.from.address }}` |
| `subject` | `{{ $json.subject }}` |
| `email_date` | `{{ $new Date($json.date).toISOString() }}` |
| `gmail_url` | `https://mail.google.com/mail/u/0/#inbox/{{ $json.messageId }}` |
| `snippet` | `{{ $json.snippet }}` |

> 💡 El nodo `Set` te permite arrastrar valores desde el panel izquierdo o escribir expresiones directamente. Asegúrate de que los nombres coincidan exactamente con los que usarás en Notion y Slack.

#### 4. **Notion Node** (Crear entrada)
- **Operation**: `Create page` o `Append to database` (si ya tienes una base de datos estructurada).
- **Database ID**: Pega el ID de tu base de datos en Notion (lo encuentras en la URL: `.../database/xxxxx`).
- **Properties Mapping** (ejemplo):
  - `Name` / `Title` → `{{ $json.subject }}`
  - `Remitente` (Text/Rich Text) → `{{ $json.sender_name }}`
  - `Email Remitente` (Email/Rich Text) → `{{ $json.sender_email }}`
  - `Fecha Recepción` (Date) → `{{ $json.email_date }}`
  - `Enlace Correo` (URL) → `{{ $json.gmail_url }}`
- ⚠️ **Prerrequisito**: La base de datos debe existir en Notion y las propiedades deben tener tipos compatibles con los datos que envías.

#### 5. **Slack Node** (Notificación)
- **Operation**: `Send message`
- **Channel**: Selecciona o escribe el canal (ej: `#ventas-nuevas`)
- **Message Type**: `Blocks` (recomendado para formato rico) o `Plain text`.
- **Mensaje sugerido** (usando sintaxis Slack):
  ```text
  📩 *Nuevo correo filtrado*
  👤 *${$json.sender_name}* (`$json.sender_email`)
  📝 Asunto: `${$json.subject}`
  🕒 Fecha: `$json.email_date`
  🔗 [Ver en Gmail]($json.gmail_url)
  ```
  > En n8n, si usas el editor visual, reemplaza `${$json.campo}` por `{{ $json.campo }}` en el campo `Message`.

---

### ✅ Prerrequisitos Técnicos
1. **Notion**: Crear base de datos con propiedades predefinidas. Generar un `Internal Integration` en Notion y compartir la base de datos con ese integration.
2. **Slack**: Crear App en Slack (API tokens scope: `chat:write`, `channels:read`), instalarla en el workspace y vincularla en n8n.
3. **Gmail**: Autorización OAuth2 estándar. Si usas cuentas corporativas, verifica que el usuario tenga permisos de lectura.

---

### 🔍 Tips Pro
- **Case-insensitive**: La expresión `.toLowerCase()` garantiza que `PROPUESTA`, `Propuesta` o `propuesta` funcionen igual.
- **Manejo de errores**: Conecta el botón rojo de error del nodo Notion/Slack a un nodo `Error Trigger` → `If` → `Slack` para recibir alertas si falla la integración.
- **Paralelismo**: Si quieres ahorrar tiempo, puedes duplicar la rama después del `Set` y ejecutar Notion y Slack en paralelo. No cambia el resultado, pero acelera el flujo.
- **Logs**: Activa `Save Execution` en la configuración global para depurar sin gastar ejecuciones pagadas.

¿Quieres que te genere el JSON exportable del workflow listo para importar en n8n, o prefieres que ajustemos algún campo específico (tipos de propiedad en Notion, formato de Slack, etc.)?