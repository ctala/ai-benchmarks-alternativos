# Qwen3-Coder-Next (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 4.68 | quality: 4.0
- latency_total: 12.639s | tokens_per_second: 96.0
- input_tokens: 246 | output_tokens: 1213

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

¡Excelente mejora! Aquí tienes un **workflow completo en N8N** que cumple con tus nuevos requisitos:

---

### 📥 **Workflow: Gmail → Filtrar por palabra clave → Guardar en Notion → Notificar en Slack**

#### 🔧 **Nodos necesarios** (en orden):
1. **Gmail Trigger** – *Polling* (busca emails nuevos periódicamente)
2. **Filter** – Filtra solo emails con `propuesta` o `cotización` (case-insensitive)
3. **Function Item** – Extrae y formatea datos (remitente, asunto, fecha, cuerpo)
4. **Notion Create Page** – Guarda la información en una base de datos de Notion
5. **Slack Notification** – Envía mensaje a un canal o DM

---

### ✅ **Configuración paso a paso**

#### 1. **Gmail Trigger**
- **Operation**: `Email Received`
- **Polling Interval**: `every 5 mins` (ajústalo según necesites)
- **Label**: `Unread` (opcional, para no procesar duplicados)
- ✅ **Importante**: En *Advanced*, activa `Include Raw Body` y `Include Headers` si quieres extraer con más precisión.

> 💡 *Sugerencia*: Usa una cuenta de Gmail dedicada o una con permisos limitados para evitar problemas con la autenticación.

---

#### 2. **Filter Node**  
- **Type**: `Item Lists`
- **Condition**:  
  ```n8n
  {{ $json["subject"].toLowerCase().includes("propuesta") || $json["subject"].toLowerCase().includes("cotización") || $json["subject"].toLowerCase().includes("cotizacion") }}
  ```
  *(Incluye variante sin tilde por seguridad)*  
- **Keep if match**: ✅  
- **Otherwise**: *Drop item* (los que no coincidan se descartan)

> 🔍 *Nota*: Si el asunto no está en `subject`, asegúrate de que el trigger incluya el campo `subject`. Si no, puedes usar una expresión más robusta como:
> ```n8n
> {{ ($json["subject"] || $json["headers"]["subject"]).toLowerCase().includes(...) }}
> ```

---

#### 3. **Function Item Node** *(para estructurar los datos)*  
Nombre: `Format Email Data`  
Código:

```javascript
const fromHeader = $json.from || {};
const name = fromHeader.name || "Sin nombre";
const email = fromHeader.address || "sin@email.com";
const subject = $json.subject || "";
const date = $json.date || new Date().toISOString();
const bodyPreview = ($json.body || "").substring(0, 500); // Primeros 500 chars

return {
  json: {
    remitente: name,
    email: email,
    asunto: subject,
    fecha: date,
    cuerpo: bodyPreview,
    id_email: $json.id, // útil para evitar duplicados en Notion
  }
};
```

---

#### 4. **Notion Create Page**  
- **Database ID**: ID de tu base de datos en Notion (copia de la URL: `.../db/XXXXXXXXXXXXXX`)
- **Authentication**: Token de integración (con permisos de escritura)
- **Properties** (ajusta según tu esquema en Notion):
  - `Nombre` → `{{ $json.remitente }}`
  - `Email` → `{{ $json.email }}`
  - `Asunto` → `{{ $json.asunto }}`
  - `Fecha` → `{{ $json.fecha }}`
  - `Cuerpo` → `{{ $json.cuerpo }}` *(como texto largo)*  
  - `Estado` (opcional, por defecto: `"Pendiente"`)

> ⚠️ Asegúrate de que los nombres de las propiedades coincidan *exactamente* con los de tu base de datos en Notion.

---

#### 5. **Slack Message**  
- **Channel**: `#propuestas-cotizaciones` (o tu canal deseado)
- **Authentication**: App de Slack con permisos `chat:write`
- **Message**:
  ```
  📩 Nueva propuesta/cotización recibida:
  • Remitente: {{ $json.remitente }} ({{ $json.email }})
  • Asunto: {{ $json.asunto }}
  • Ver en Notion: [Abrir página]({{ $json.notion_url }})  // *opcional si guardas la URL*
  ```

> 🔗 *Para incluir enlace directo a la página de Notion*, puedes usar un **Set Node** o **Function Item** previo para generar la URL así:
> ```n8n
> {{ "https://notion.so/" + $json.page_id }}
> ```
> (si guardas `page_id` en Notion)

---

### 📌 Bonus: Evitar duplicados (opcional pero recomendado)
- Usa un **Set Node** después del trigger para marcar los emails procesados:
  - Agrega una etiqueta en Gmail: `Procesado`
  - O usa el ID del email como clave única en Notion (como una propiedad `ID Email` con tipo `Unique`).

---

### 🔗 ¿Quieres el **workflow listo para importar**?  
Te genero el JSON completo (listo para copiar y pegar en *Import* de N8N). ¿Te interesa? Solo dime y lo envío.