# Kimi K2.5 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 3.87 | quality: 4.0
- latency_total: 171.112s | tokens_per_second: 27.6
- input_tokens: 266 | output_tokens: 4716

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

Aquí tienes el flujo completo, paso a paso, con las expresiones listas para copiar y pegar.

### 🔄 Diagrama del Workflow

```
[Gmail Trigger] → [Filter: propuesta/cotizacion] → [Set: Limpiar datos] → [Notion: Crear registro] → [Slack: Notificar]
```

---

### 1️⃣ Gmail Trigger
- **Node:** `Gmail` → `On Message Received`
- **Credential:** Conecta tu cuenta de Google (OAuth2).
- **Options:**
  - **Label:** `INBOX`
  - **Format:** `Full` (para obtener `from`, `subject`, `date`, etc.)
  - **Simple:** Desactivado (así tienes toda la metadata).
  - **Poll Times:** Cada 1 minuto (o el intervalo que prefieras).

> ⚠️ **Importante:** El campo `from` llega como texto plano: `Juan Pérez <juan@empresa.com>`. Más adelante lo separaremos en nombre y email.

---

### 2️⃣ Filter (Filtrar Asunto)
Usa el nodo **`Filter`** (más limpio que IF para esto).

- **Conditions combinator:** `OR`
- **Condition 1:**
  - **Value 1:** `={{ $json.subject.toLowerCase() }}`
  - **Operation:** `Contains`
  - **Value 2:** `propuesta`
- **Condition 2:**
  - **Value 1:** `={{ $json.subject.toLowerCase() }}`
  - **Operation:** `Contains`
  - **Value 2:** `cotizacion`

Esto deja pasar solo los emails que contengan esas palabras, sin importar mayúsculas/minúsculas.

---

### 3️⃣ Set (Extraer y Limpiar Datos)
Usa el nodo **`Set`** (versión 3) para crear variables limpias antes de enviar a Notion.

Añade estos campos (`Add Field` → `Text`):

| Nombre | Valor (Expression) |
|--------|-------------------|
| `nombre` | `={{ $json.from.replace(/<[^>]+>/, '').trim() }}` |
| `email` | `={{ ($json.from.match(/<([^>]+)>/) \|\| [null, $json.from])[1] }}` |
| `asunto` | `={{ $json.subject }}` |
| `fecha` | `={{ $json.date }}` |
| `texto` | `={{ $json.text }}` |

> 💡 **Nota:** La expresión de `email` funciona incluso si el remitente no tiene nombre y solo envía la dirección plana.

---

### 4️⃣ Notion (Crear entrada en Base de Datos)
Usa el nodo **`Notion`** → **Resource:** `Database Page` → **Operation:** `Create`.

**Pre-requisito:** En Notion, crea una base de datos (ej: *"Leads Email"*) con estas propiedades (ajusta los nombres a las tuyas):
- `Nombre` (Title)
- `Email` (Email)
- `Asunto` (Rich Text)
- `Fecha` (Date)
- `Estado` (Select)

Luego comparte la base de datos con tu integración de Notion (en `...` → `Add connections`).

**Configuración del nodo:**
- **Database:** Selecciona tu base.
- **Properties (mapeo):**
  - **Nombre (Title):** `{{ $json.asunto }}`
  - **Email (Email):** `{{ $json.email }}`
  - **Asunto (Rich Text):** `{{ $json.asunto }}`
  - **Fecha (Date):** `{{ $json.fecha }}`
  - **Estado (Select):** `Nuevo` *(o deja vacío para que Notion use el default)*

---

### 5️⃣ Slack (Notificación)
Usa el nodo **`Slack`** → **Resource:** `Message` → **Operation:** `Post`.

- **Channel:** `#oportunidades` (o el nombre/ID de tu canal).
- **Text:**
```markdown
📩 *Nueva oportunidad de email*

*De:* {{ $json.nombre }} <{{ $json.email }}>
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

👉 Revisa los detalles en Notion.
```

**Mejora Pro:** Si quieres que el mensaje de Slack incluya un link directo a la fila de Notion recién creada:
1. En el nodo de Notion, la salida incluye `url`.
2. Conecta la salida de Notion a Slack (en lugar de la salida del nodo Set).
3. En el mensaje de Slack usa: `{{ $json.url }}`.

Para hacer eso, simplemente cambia el origen de datos del nodo Slack para que lea del nodo Notion, o usa una expresión como:
```markdown
🔗 *Ver en Notion:* {{ $('Notion').item.json.url }}
```

---

### 🛠 Checklist de Credenciales
Antes de activar el workflow, asegúrate de tener:

1. **Gmail:** API habilitada en Google Cloud Console. OAuth con scopes `https://www.googleapis.com/auth/gmail.readonly` (o `modify` si planeas marcar como leído).
2. **Notion:** Integración creada en [notion.so/my-integrations](https://notion.so/my-integrations). La base de datos **debe estar compartida** con esa integración.
3. **Slack:** App creada en [api.slack.com](https://api.slack.com). Token de Bot con scopes `chat:write` y `chat:write.public` (si el canal es público).

---

### 🚀 Tip Extra: Evitar duplicados
Si usas el trigger por **polling**, N8N trae los últimos N emails cada vez. Para no procesar el mismo email 2 veces:
- Activa la opción **"Simple"** desactivada y usa un nodo **`Compare Datasets`** o **`Google Sheets / Notion → Search`** para verificar si el `messageId` ya existe antes de crearlo.
- Alternativa más simple: En Gmail Trigger, si usas la opción de leer solo **Unread** y luego marcas el email como leído (con un nodo Gmail → Mark as Read al final), evitas reprocesarlo.

¿Te gustaría que te genere el **JSON del workflow** listo para importar a tu N8N? Solo dime y te lo armo.