# Qwen 3.6 27B base (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 4.33 | quality: 4.0
- latency_total: 47.213s | tokens_per_second: 60.2
- input_tokens: 233 | output_tokens: 2844

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

¡Perfecto! Cambio de rumbo totalmente válido. Vamos a diseñar un workflow robusto, filtrado y con notificaciones en tiempo real. Te lo dejo paso a paso listo para copiar en n8n.

## 🧩 Estructura del Workflow
```
[Gmail Trigger] 
       │
       ▼
[IF Node] → ¿Contiene "propuesta" o "cotización" en el asunto?
   ├── ✅ True → [Code/Function] (limpieza/estructura) → ──┬── [Notion] (Add Page)
   │                                                      └── [Slack] (Send Message)
   └── ❌ False → [End] (ignora el email)
```

---

## 🔧 Configuración nodo por nodo

### 1. `Gmail Trigger`
- **Resource:** `Email`
- **Operation:** `New Email`
- **Polling Interval:** `1 minute` (recomendado)
- **Filter by Label:** Opcional. Si no usas labels, déjalo vacío.
- ⚠️ Asegúrate de tener la credencial de Gmail con el scope `https://www.googleapis.com/auth/gmail.readonly`.

### 2. `IF Node` (Filtro de asunto)
- **Condition:** `Expression`
- **Expression:**
  ```js
  {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}
  ```
- **True:** Sigue al siguiente nodo
- **False:** Conecta a un nodo `End` (o déjalo sin conectar para que n8n lo ignore)

### 3. `Code Node` (Opcional pero recomendado)
Sirve para estandarizar los datos antes de enviarlos a Notion y Slack.
```js
// Extrae y limpia datos relevantes
const from = $json.from || "";
const emailMatch = from.match(/<([^>]+)>/);
const email = emailMatch ? emailMatch[1] : from;
const name = emailMatch ? from.replace(emailMatch[0], "").trim() : email;

return {
  json: {
    nombre: name,
    email: email,
    asunto: $json.subject,
    fecha: $json.date,
    cuerpo: $json.textBody || $json.htmlBody || "",
    id_gmail: $json.id
  }
};
```

### 4. `Notion Node` (Add Page)
- **Resource:** `Database`
- **Operation:** `Add Page`
- **Database ID:** `(Pega el ID de tu base de datos de Notion)`
- **Properties:** Mapea así (ajusta nombres si tu DB los tiene diferentes):
  | Propiedad en Notion | Tipo | Valor en n8n |
  |---------------------|------|--------------|
  | Nombre de la página | Title | `{{ $json.asunto }}` |
  | Email | Email | `{{ $json.email }}` |
  | Remitente | Title | `{{ $json.nombre }}` |
  | Fecha recepción | Date | `{{ $json.fecha }}` |
  | Estado | Select | `Nueva` |
  | ID Gmail | Rich Text | `{{ $json.id_gmail }}` |

📌 **Nota importante:** El ID de la base de datos se obtiene desde la URL de Notion: `https://www.notion.so/tu-espacio/[DATABASE_ID]` (la cadena alfanumérica de 32 caracteres).

### 5. `Slack Node` (Send Message)
- **Resource:** `Message`
- **Channel:** `#tu-canal` o ID de usuario
- **Message Type:** `Text`
- **Text:**
  ```
  📧 *Nueva propuesta/cotización recibida*
  👤 Remitente: {{ $json.nombre }}
  📩 Email: {{ $json.email }}
  📝 Asunto: {{ $json.asunto }}
  🕒 Fecha: {{ $json.fecha }}
  🔗 [Ver en Notion](URL_DE_TU_DB_NOTION)
  ```
- ⚠️ Asegúrate de que la credencial de Slack tenga los scopes: `chat:write`, `channels:read` (o `groups:read` si es privado).

---

## 🛡️ Buenas prácticas para producción

1. **Deduplicación:** El trigger de Gmail puede repetir emails si hay retrasos en el polling. Agrega un `IF` previo que verifique si `{{ $json.id }}` ya existe en Notion (usando un `Notion` node en modo `Get Many` con filtro `id_gmail`), o habilita la opción `Mark as Read` en el trigger.
2. **Manejo de errores:** Conecta un `Error Trigger` a un canal de Slack o email para alertarte si falla la conexión con Notion o Slack.
3. **Rate Limits:** Gmail permite ~250 requests/min. Con polling de 1 min estás bien. Notion y Slack no suelen ser problema con este volumen.
4. **Testing:** Usa `Test Workflow` con un email real que contenga "propuesta" en el asunto. Revisa el output de cada nodo antes de activar.

---

¿Quieres que te genere el JSON exportable del workflow para que lo importes directo en n8n, o prefieres que ajustemos algo (ej. filtrar por remitente específico, agregar campo de prioridad, o enviar el cuerpo del email a Notion)?