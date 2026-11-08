# Qwen 3.6 35B base (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 4.65 | quality: 4.0
- latency_total: 22.032s | tokens_per_second: 120.2
- input_tokens: 237 | output_tokens: 2649

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



Excelente cambio. Integrar **Gmail → Notion → Slack** es un flujo muy común en automatizaciones de negocio. Aquí tienes la estructura exacta y la configuración paso a paso para n8n:

### 🧩 Estructura del Workflow
```
[Gmail Trigger] → [Function (Parsear remitente)] → [IF (Filtrar asunto)]
       ↓ True                              ↓ False
[Notion: Crear Página] ↔ [Slack: Enviar Mensaje]
```

---

### 🔧 Configuración paso a paso

#### 1. **Gmail Trigger**
- **Operation**: `On New Email`
- **Credentials**: Conecta tu cuenta de Gmail con OAuth2.
- **Fields to return**: Asegúrate de incluir `from`, `subject`, `date`, `snippet`.
- ⚠️ *Tip*: Activa `Test Mode` la primera vez para no perder correales antiguos.

#### 2. **Function Node** (Recomendado para parsear el remitente)
Gmail devuelve el campo `from` como texto plano (`"Juan Pérez <juan@ejemplo.com>"`). Este nodo lo separa:
```javascript
const from = $json.from || '';
const match = from.match(/(.+?)\s*<(.+?)>/);
return {
  json: {
    ...$json,
    senderName: match ? match[1].trim() : from,
    senderEmail: match ? match[2] || from : from,
    subject: $json.subject || '',
    date: $json.date || new Date().toISOString()
  }
};
```

#### 3. **IF Node** (Filtro por asunto)
- **Condition**: `Custom Expression`
- **Expression**:
```javascript
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}
```
- Conecta la rama `True` a Notion y Slack. La rama `False` al final del workflow.

#### 4. **Notion Node** (`Create Page`)
- **Operation**: `Create Page`
- **Database ID**: ID de la base de datos en Notion (obténlo de la URL: `notion.so/tu-usuario/XXXXXXXXXXXXXXXXXXXXXXXXXXXX`)
- **Properties Mapping** (ejemplo basado en una DB típica):
  | Propiedad en Notion | Valor en n8n |
  |---------------------|--------------|
  | `Title`             | `{{ $json.subject }}` |
  | `Remitente` (Text)  | `{{ $json.senderName }}` |
  | `Email` (Email)     | `{{ $json.senderEmail }}` |
  | `Fecha de llegada` (Date) | `{{ $json.date }}` |
  | `Asunto` (Text)     | `{{ $json.subject }}` |

⚠️ **Importante**: Los nombres de las propiedades deben coincidir **exactamente** con los de tu base de datos en Notion, y el tipo de dato debe ser compatible (ej. `date` en Notion acepta ISO 8601).

#### 5. **Slack Node** (`Send Message`)
- **Operation**: `Send Message`
- **Channel**: Selecciona o escribe el nombre del canal (ej. `#ventas-nuevas`)
- **Message**:
```
📩 Nuevo email filtrado
👤 Remitente: {{ $json.senderName }}
📧 Email: {{ $json.senderEmail }}
📌 Asunto: {{ $json.subject }}
🕒 Fecha: {{ $json.date }}
```
- Conecta este nodo en paralelo con el de Notion (ambos salen de la rama `True` del IF).

---

### ✅ Requisitos previos
1. **Conexiones activas**: Gmail, Notion y Slack deben estar autorizadas en n8n.
2. **Base de datos en Notion**: Crea una DB con las propiedades que vas a mapear.
3. **Permisos en Notion**: En la integración, activa `Pages` (Write) y `Database` (Read/Write).
4. **Canal de Slack**: Asegúrate de que el bot de n8n tenga permisos para escribir en el canal.

---

### 🔍 Tips de depuración
- Si Notion falla, revisa los **logs del nodo**: suele ser por nombres de propiedades mal escritos o tipos de dato incompatibles.
- Usa el modo `Debug` de n8n para inspeccionar el JSON que sale de Gmail y confirmar que `subject` y `from` se están parseando correctamente.
- Si quieres agregar el cuerpo del email o archivos adjuntos, puedo extenderte la configuración.

¿Quieres que te genere el archivo `.json` exportable para importarlo directo en tu instancia de n8n, o prefieres ajustar algún campo específico (ej. agregar el cuerpo del email, categorizar por tipo de propuesta, etc.)?