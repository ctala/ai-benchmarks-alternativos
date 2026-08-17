# Qwen3-Coder-Next (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.74 | quality: 7.16
- latency_total: 9.617s | tokens_per_second: 146.6
- input_tokens: 246 | output_tokens: 1410
- judge_score: 3.8 | justificación: 

## Respuesta completa

¡Excelente ajuste! Vamos a reconfigurar el workflow para que:

✅ Lea emails de Gmail  
✅ **Filtre** solo los que tengan **“propuesta” o “cotización”** (case-insensitive) en el asunto  
✅ Extraiga: **remitente (nombre + email)**, **asunto**, **fecha de recepción**  
✅ Guarde cada email en una **base de Notion** (como una página dentro de una base de datos)  
✅ Envíe una **notificación a Slack** (con enlace al email y resumen)

---

### 🔧 Workflow en N8N (pasos detallados)

#### 1. **Gmail Trigger**  
- **Node**: `Gmail Trigger`  
- **Operation**: `Email Received`  
- **Filter**:  
  - `Subject Contains`: `propuesta|cotización` *(usa regex si quieres más flexibilidad)*  
  - ⚠️ *Nota*: Gmail no permite regex en el filtro nativo. Mejor opción:  
    → Usa `Subject Contains: "propuesta"` y luego filtra en un **Function Node** para incluir “cotización” y variantes (ej. “cotización”, “cotización”, “COTIZACIÓN”, etc.).

✅ Recomendado:  
- Desactiva el filtro en el trigger  
- Usa un `Filter` node después para aplicar lógica más robusta (abajo te muestro cómo).

---

#### 2. **Filter Node** *(opcional pero recomendado para flexibilidad)*  
- **Node**: `Filter`  
- **Condition**:  
  ```text
  {{ $json["subject"].toLowerCase().includes("propuesta") || 
     $json["subject"].toLowerCase().includes("cotización") }}
  ```
  *(Asegúrate de que el campo `subject` venga en minúsculas o normalizarlo antes)*  
  → Solo deja pasar los emails que coincidan.

---

#### 3. **Function Node** *(para extraer y normalizar datos)*  
- **Node**: `Function Item` o `Function` (dependiendo de si quieres procesar uno a uno o todos)  
- **Nombre**: `Extract Sender & Format Data`  
- **Código**:
```javascript
// Asegura que el email venga en minúsculas
const subject = $json.subject?.toLowerCase() || "";
const from = $json.from || "";
const date = $json.date || new Date().toISOString();

// Parsear "Nombre <email@dominio.com>" o solo "email@dominio.com"
let senderName = "";
let senderEmail = "";

if (from.includes("<")) {
  const parts = from.split("<");
  senderName = parts[0].trim().replace(/['"]/g, "");
  senderEmail = parts[1].replace(">", "").trim();
} else {
  senderEmail = from.trim();
}

return {
  json: {
    senderName,
    senderEmail,
    subject: $json.subject,
    date,
    snippet: $json.snippet || "",
    threadId: $json.threadId,
    messageId: $json.messageId,
    emailLink: `https://mail.google.com/mail/u/0/#inbox/${$json.id}`
  }
};
```

---

#### 4. **Notion Node** *(Crear página en base de datos)*  
- **Node**: `Notion`  
- **Operation**: `Create Page`  
- **Database ID**: 📌 ID de tu base de datos en Notion (copia de la URL: `https://www.notion.so/.../{database-id}?v=...`)  
- **Properties Mapping**:
  | Notion Property | Value |
  |-----------------|-------|
  | `Name` *(o el título de tu DB)* | `{{ $json.senderName }}` *(o `{{ $json.subject }}` si prefieres como título)* |
  | `Email` *(texto)* | `{{ $json.senderEmail }}` |
  | `Asunto` *(texto)* | `{{ $json.subject }}` |
  | `Fecha` *(date)* | `{{ $json.date }}` *(asegúrate de que Notion lo acepte como ISO 8601)* |
  | `Resumen` *(rich text)* | `{{ $json.snippet }}` |
  | `Enlace al email` *(URL)* | `{{ $json.emailLink }}` |

📌 **Importante**:  
- Asegúrate de que en tu Notion DB existan los campos con los nombres exactos.  
- Usa el modo **"Automatically map to properties"** si tienes dificultades, o mapea manualmente.

---

#### 5. **Slack Node** *(notificación)*  
- **Node**: `Slack`  
- **Operation**: `Send Message`  
- **Channel**: `#alertas-cotizaciones` *(o tu canal deseado)*  
- **Text**:
```text
📩 Nueva propuesta/cotización recibida:

👤 *Remitente*: {{ $json.senderName }} ({{ $json.senderEmail }})
📝 *Asunto*: {{ $json.subject }}
📅 *Fecha*: {{ $json.date | date("DD/MM/YYYY HH:mm") }}
🔗 [Ver email en Gmail]({{ $json.emailLink }})
```

⚠️ *Requiere*:  
- Token de bot de Slack con permisos: `chat:write`, `channels:read`  
- El canal debe existir y ser accesible por tu bot.

---

### ✅ Diagrama resumen del flujo:
```
[Gmail Trigger] 
       ↓
[Filter: propuesta | cotización]  
       ↓
[Function: Extract Data]  
       ↓
[Notion: Create Page]  
       ↓
[Slack: Send Notification]
```

---

### 🔍 Tips adicionales:
- Si quieres guardar **múltiples emails** en el mismo día (sin duplicar), puedes agregar un nodo `Debounce` o usar una lógica de upsert en Notion.
- Para evitar correos de prueba o spam, puedes filtrar por dominio o usar `Gmail Search` avanzado (ej. `from:*@cliente.com subject:(propuesta OR cotización)`).
- Usa `N8N Webhook` para probar manualmente antes de activar el trigger.

---

¿Quieres que te genere el **workflow completo en JSON** para importarlo directamente en N8N? Puedo generártelo listo para copiar/pegar.