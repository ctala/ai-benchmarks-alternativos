# Qwen3-Coder-Next (OpenRouter FP8) — multi_turn/requirements_change

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.05 | quality: 7.72
- latency_total: 8.463s | tokens_per_second: 147.7
- input_tokens: 246 | output_tokens: 1250
- judge_score: 4.2 | justificación: 

## Respuesta completa

¡Excelente mejora! Vamos a configurar un workflow robusto en **N8N** que:

✅ **Filtre emails** de Gmail cuyo asunto contenga *“propuesta”* o *“cotización”* (insensible a mayúsculas/minúsculas y con variante con tilde)  
✅ **Extraiga** remitente, email, asunto y fecha  
✅ **Guarde** los datos en una **base de datos de Notion**  
✅ **Envíe notificación a Slack** (con enlace al email si es posible, o datos clave)

---

### 🛠️ Workflow paso a paso

#### 1. **Trigger: Gmail – New Email (Unread)**
- **Operation**: `Get Unread Email`
- **Query**: `subject:(propuesta OR cotización OR cotizacion)`  
  *(Nota: Gmail soporta operadores de búsqueda. Esto filtra solo los que tengan alguna de las palabras en el asunto)*  
  ✅ *Importante*: Asegúrate de que el email esté marcado como *unread* al inicio para que el trigger lo detecte.

> 🔁 *Alternative*: Si prefieres procesar *todos* los nuevos emails pero filtrar luego, usa `New Email` y filtras con un `IF` node. Pero el query es más eficiente.

---

#### 2. **Function Node: Extract & Format Data**
*Nombre sugerido:* `Extract Email Data`

```javascript
// Extrae y formatea datos del email
const email = $input.item.json;

// Normaliza el asunto (minúsculas, sin tildes para consistencia)
const subject = email.subject?.toLowerCase() || '';
const hasPropuesta = subject.includes('propuesta');
const hasCotizacion = subject.includes('cotizacion') || subject.includes('cotización');

return {
  json: {
    senderName: email.from?.name || 'Sin nombre',
    senderEmail: email.from?.email || '',
    subject: email.subject,
    date: email.date || new Date().toISOString(),
    hasPropuesta,
    hasCotizacion,
    rawBody: email.body?.substring(0, 200) + '...' // solo primeros 200 chars (opcional)
  }
};
```

> 💡 *Nota*: Asumimos que el trigger devuelve el email en formato estándar de N8N (con `from`, `subject`, `date`, `body`). Si usas `Get Unread Email`, sí lo hace.

---

#### 3. **Switch Node (opcional pero recomendado)**
- **Property**: `$.json.hasPropuesta` o `$.json.hasCotizacion`
- **Type**: `Any`  
- **Branches**:
  - `✅ Propuesta o Cotización`: si cualquiera de los dos es `true`
  - `❌ Ignorar`: (opcional, para depuración)

> ✅ Esto asegura que solo sigan los emails que realmente nos interesan.

---

#### 4. **Notion – Create Page**
*En Notion:*
- Crea una base de datos (ej. `Propuestas y Cotizaciones`) con propiedades:
  - `Nombre` (Text)
  - `Email` (Email)
  - `Asunto` (Title)
  - `Fecha` (Date)
  - `Fuente` (Select: "Gmail")
  - `Resumen` (Rich Text)

*Configuración en N8N:*
- **Operation**: `Create Page`
- **Parent Database ID**: *(ID de tu DB de Notion)*  
- **Properties**:
  - `Nombre`: `{{ $json.senderName }}`
  - `Email`: `{{ $json.senderEmail }}`
  - `Asunto`: `{{ $json.subject }}`
  - `Fecha`: `{{ $json.date }}`
  - `Fuente`: `"Gmail"` (valor fijo)
  - `Resumen`: `{{ $json.rawBody }}`

> 🔑 *Importante*: Necesitas un token de integración de Notion y dar acceso a la DB.

---

#### 5. **Slack – Send Message**
- **Channel**: `#proyectos` (o el que prefieras)
- **Text** (con plantilla):
  ```
  📩 Nueva propuesta/cotización recibida:

  👤 De: {{ $json.senderName }} ({{ $json.senderEmail }})
  📬 Asunto: {{ $json.subject }}
  📅 Recibido: {{ $json.date }}

  🔗 Link al email (si usas Gmail en web): https://mail.google.com/mail/u/0/#search/from:{{ $json.senderEmail }}+subject:{{ encodeURIComponent($json.subject) }}
  ```

> 💬 *Tip*: Si el email tiene adjuntos o contenido crítico, puedes añadir más campos o usar `Send DM` a alguien específico (ej. `@tu_nombre`).

---

### 📋 Resumen del flujo:
```
Gmail (new unread + query)
   ↓
Function (extract & format)
   ↓
Switch (filter propuesta/cotización)
   ↓
Notion (create page)
   ↓
Slack (notify)
```

---

### ✅ Verificaciones clave:
- [ ] En Gmail, habilita permisos de `gmail.readonly` (o `gmail.modify` si necesitas marcar como leído).
- [ ] En Notion, comparte la DB con tu integración.
- [ ] En Slack, crea un webhook o usa una app oficial con token de bot.

---

¿Quieres que te dé el **workflow en JSON listo para importar** en N8N? Puedo generártelo con todos los nodos configurados.