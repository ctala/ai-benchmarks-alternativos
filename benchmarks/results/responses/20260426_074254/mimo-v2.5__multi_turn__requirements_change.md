# MiMo-V2.5 (omnimodal) — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 6.88 | quality: 7.24
- latency_total: 9.861s | tokens_per_second: 91.9
- input_tokens: 244 | output_tokens: 906
- judge_score: 3.8 | justificación: 

## Respuesta completa

Perfecto, el workflow ahora es más completo. Aquí tienes la estructura:

## **Workflow: Emails → Notion + Notificación Slack**

### **Nodos necesarios:**
1. **Gmail Trigger** → 2. **If (filtro)** → 3. **Function (extraer)** → 4. **Notion** + 5. **Slack** (en paralelo)

---

### **1. Gmail Trigger**
- **Event**: `Email Received`
- **Poll Times**: `Every 1 min` (o como prefieras)
- **Filters**: Ninguno (filtraremos después)

---

### **2. If (Filtro por asunto)**
- **Condition**: `String` → `subject`
- **Operation**: `Contains`
- **Value 1**: `propuesta`
- **Value 2**: `cotizacion`
- **Combine**: `OR`

---

### **3. Function (Extraer datos)**
```javascript
const email = $input.first().json;

return {
  json: {
    nombre_remitente: email.from?.name || 'Sin nombre',
    email_remitente: email.from?.email || 'Sin email',
    asunto: email.subject || 'Sin asunto',
    fecha: email.date || new Date().toISOString(),
    body_preview: email.text?.substring(0, 200) || ''
  }
};
```

---

### **4. Notion (Crear página)**
- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database ID**: (tu base de datos de Notion)
- **Properties**:
  - `Name` (título): `={{ $json.asunto }}`
  - `Email`: `={{ $json.email_remitente }}`
  - `Fecha`: `={{ $json.fecha }}`
  - `Remitente`: `={{ $json.nombre_remitente }}`

---

### **5. Slack (Notificación)**
- **Resource**: `Message`
- **Operation**: `Send`
- **Channel**: `#proyectos` (o el que uses)
- **Message Type**: `Text`
- **Text**: 
```
📧 *Nuevo email importante* de {{ $json.nombre_remitente }}
*Asunto:* {{ $json.asunto }}
*Email:* {{ $json.email_remitente }}
*Guardado en Notion* ✅
```

---

### **Conexiones:**
```
Gmail Trigger → If → Function → Notion
                       ↓
                     Slack
```

---

### **Credenciales necesarias:**
- Gmail OAuth2
- Notion Integration (con permisos de escritura)
- Slack OAuth2

---

### **¿Qué necesitas configurar?**
1. **Base de datos de Notion**: ¿Qué campos específicos tienes en tu DB?
2. **Canal de Slack**: ¿A dónde quieres las notificaciones?
3. **Frecuencia de revisión**: ¿Cada cuánto revisar emails?

¿Quieres que ajuste algo específico o agregue más campos?