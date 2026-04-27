# Grok 4.20 — multi_turn/requirements_change

- model_id: `x-ai/grok-4.20`
- success: True  | final: 5.85 | quality: 5.28
- latency_total: 10.749s | tokens_per_second: 71.4
- input_tokens: 337 | output_tokens: 768
- judge_score: 2.4 | justificación: 

## Respuesta completa

✅ **Perfecto**, aquí tienes el workflow actualizado y más completo según tus nuevos requisitos:

### Workflow en n8n: Emails → Notion + Notificación Slack

---

### **Nodos que vas a necesitar:**

1. **Gmail Trigger**
2. **IF** (Filtro)
3. **Function Item** (Extraer datos)
4. **Notion** (Crear Página)
5. **Slack** (Enviar mensaje)

---

### Configuración detallada:

---

#### **1. Gmail Trigger**
- **Trigger**: `Message Received`
- **Mailbox**: Inbox
- **Options**:
  - `Resolve Data`: **True**
  - `Format`: `Resolved`

---

#### **2. IF** (Filtro por asunto)
**Condition**:
- Value 1: `{{$json["subject"]}}`
- Operation: **Contains**
- Value 2: `propuesta,cotizacion` *(separado por coma)*

> En la pestaña **Options** activa: **Ignore Case** (para que detecte "Propuesta", "COTIZACION", etc.)

**True** → continúa el workflow  
**False** → termina (no hacer nada)

---

#### **3. Function Item** (Extraer y limpiar datos)

```javascript
const subject = $json.subject || "";
const from = $json.from || "";
const date = $json.date || new Date().toISOString();

let nombre = "Sin nombre";
let email = "";

if (from.includes("<")) {
    nombre = from.split("<")[0].trim().replace(/"/g, '');
    email = from.match(/<(.+)>/)[1];
} else {
    email = from;
}

return [{
    json: {
        nombre: nombre,
        email: email,
        asunto: subject,
        fecha: new Date(date).toLocaleString('es-ES'),
        url: $json.url || ""  // link al email en Gmail
    }
}];
```

---

#### **4. Notion** (Crear página en base de datos)

**Configuración:**
- **Operation**: `Create Page`
- **Database ID**: (pega el ID de tu base de datos de Notion)
- **Properties**:

| Property Name     | Type         | Value |
|-------------------|--------------|-------|
| Nombre            | Title        | `{{ $json.nombre }}` |
| Email             | Email        | `{{ $json.email }}` |
| Asunto            | Text         | `{{ $json.asunto }}` |
| Fecha de Recepción| Date         | `{{ $json.fecha }}` |
| Fuente            | Select       | `Email` |
| Enlace Gmail      | URL          | `{{ $json.url }}` |

---

#### **5. Slack** (Notificación)

**Configuración:**
- **Operation**: `Post Message`
- **Channel**: `#propuestas` (o el que prefieras)
- **Text**:

```markdown
🚀 *Nueva Propuesta/Cotización recibida*

*De:* {{ $json.nombre }} ({{ $json.email }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

Ver en Gmail → {{ $json.url }}
```

---

### Recomendaciones adicionales:

1. **Activa el Trigger** solo para emails no leídos si quieres evitar duplicados.
2. Puedes añadir un nodo **"Gmail" → "Mark as Read"** al final.
3. Crea una base de datos en Notion con las propiedades mencionadas arriba antes de conectar el nodo.

---

¿Quieres que te prepare el **JSON completo del workflow** para que lo importes directamente en n8n? Puedo generártelo listo para importar.