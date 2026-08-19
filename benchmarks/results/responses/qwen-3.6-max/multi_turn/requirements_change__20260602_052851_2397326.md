# Qwen 3.6 Max — multi_turn/requirements_change

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 4.81 | quality: 4.72
- latency_total: 64.914s | tokens_per_second: 38.6
- input_tokens: 233 | output_tokens: 2505
- judge_score: 2.0 | justificación: La respuesta no cumple con el requisito original de guardar datos en un Google Sheet, en su lugar, introduce Notion y Slack, lo que la hace irrelevante. Aunque la estructura y configuración son claras, no se ajusta al contexto solicitado.

## Respuesta completa

Perfecto, ajustamos el flujo. Aquí tienes la arquitectura exacta y la configuración nodo por nodo para **N8N v1+**:

### 🔁 Estructura del Workflow
```
Gmail Trigger → Filter → Code (parseo) → Notion → Slack
```

---

### 🔧 Configuración Nodo por Nodo

#### 1️⃣ **Gmail Trigger**
- **Event:** `Email Received`
- **Options:** 
  - `Download Attachments`: ❌ (no necesario)
  - `Simple`: ✅ (devuelve estructura limpia)
- **Credencial:** Conecta tu cuenta de Gmail con permisos de lectura.

#### 2️⃣ **Filter Node** (Filtro por asunto)
- **Condition 1:** `{{$json.subject}}` → `Contains` → `propuesta`
- **Condition 2:** `{{$json.subject}}` → `Contains` → `cotizacion`
- **Logical Operator:** `OR`
- ✅ Activa `Case Insensitive` para que no importe mayúsculas/minúsculas.
- *Nota:* Solo los emails que cumplan seguirán al siguiente nodo.

#### 3️⃣ **Code Node** (Extracción y limpieza de datos)
Usa este script en modo `Run Once for All Items`:
```javascript
const items = $input.all();

return items.map(item => {
  const from = item.json.from || '';
  // Extrae nombre y email de formatos como "Juan Pérez <juan@ejemplo.com>"
  const match = from.match(/^(.*?)\s*<([^>]+)>$/);
  const senderName = match ? match[1].trim() : from.split('@')[0];
  const senderEmail = match ? match[2] : from;

  return {
    json: {
      sender_name: senderName,
      sender_email: senderEmail,
      subject: item.json.subject || '',
      received_at: item.json.date || new Date().toISOString(),
      snippet: (item.json.snippet || '').slice(0, 200)
    }
  };
});
```

#### 4️⃣ **Notion Node** (Guardar en base de datos)
- **Operation:** `Create` → `Database Page`
- **Database ID:** Pega el ID de tu base de datos en Notion (está en la URL después de `/`)
- **Properties Mapping:**
  - `Title` → `{{$json.subject}}`
  - `Email` (tipo Email) → `{{$json.sender_email}}`
  - `Remitente` (tipo Text) → `{{$json.sender_name}}`
  - `Fecha Recepción` (tipo Date) → `{{$json.received_at}}`
  - `Estado` (tipo Select) → `Nuevo`
- ⚠️ **Importante:** La base de datos en Notion debe existir previamente con esas propiedades y tipos exactos.

#### 5️⃣ **Slack Node** (Notificación)
- **Operation:** `Send Message`
- **Channel / User:** `#tu-canal` o `@tu-usuario`
- **Message Type:** `Blocks` o `Text` (recomiendo Text para simplicidad)
- **Message:**
```
📩 *Nueva propuesta/cotización recibida*
👤 *Remitente:* {{$json.sender_name}} <{{$json.sender_email}}>
📝 *Asunto:* {{$json.subject}}
📅 *Fecha:* {{$json.received_at}}
🔗 *Ver en Notion:* {{$json.url}} (si mapeas la URL que devuelve Notion)
```

---

### 📋 Requisitos Previos
1. **Credenciales en N8N:** Gmail, Notion (Integration Token + base de datos compartida con la integración), Slack (Bot Token con scopes `chat:write`, `channels:read`).
2. **Base de datos en Notion:** Crea una DB con las propiedades mencionadas. Comparte la DB con tu integración de Notion (`••• → Add connections → Tu integración`).
3. **Permisos Gmail:** Si usas cuenta corporativa, verifica que no haya restricciones de API.

---

### 🚀 Tips Pro para Emprendedores
- ✅ **Prueba con `Execute Workflow`** antes de activar el trigger. Usa un email de prueba con "propuesta" en el asunto.
- 🔁 **Idempotencia:** Agrega un `Merge` o `IF` antes de Notion si quieres evitar duplicados (ej. filtrar por `messageId`).
- 🛡️ **Error Handling:** Activa `Continue On Fail` en Notion/Slack y conecta un `Error Trigger` para que no se detenga todo si falla una notificación.
- ⏱️ **Polling vs Webhook:** Gmail Trigger usa polling por defecto (~5 min). Si necesitas tiempo real, configura un webhook con Google Pub/Sub (más avanzado).

¿Quieres que te genere el **JSON exportable** listo para importar en tu instancia de N8N? Solo dime tu versión de N8N y si prefieres que el flujo incluya control de duplicados por `messageId`.