# KAT Coder Air v2.5 — multi_turn/requirements_change

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 4.9 | quality: 4.0
- latency_total: 8.377s | tokens_per_second: 193.6
- input_tokens: 233 | output_tokens: 1622

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



¡Excelente cambio! Aquí te detallo el workflow completo con los nuevos requisitos:

## **Workflow: Gmail → Notion + Slack**

### **Nodos necesarios:**
1. **Gmail Trigger** (Trigger)
2. **Filter** (Filtro por asunto)
3. **Function** (Extraer datos)
4. **Notion** (Crear página en base de datos)
5. **Slack** (Notificación)

---

## **Configuración paso a paso:**

### **1. Gmail Trigger**
- **Trigger**: `On New Email`
- **Folder**: `INBOX`
- **Polling Interval**: `5` minutos
- **Output**: `All email fields`

---

### **2. Filter** (Filtro por asunto)
- **Condition**:
  - `subject` → `contains` → `propuesta`
  - `OR`
  - `subject` → `contains` → `cotizacion`
- **Case sensitive**: `Desactivado` (para capturar "Propuesta", "COTIZACIÓN", etc.)

---

### **3. Function** (Extraer datos)
```javascript
const email = items[0].json;
const sender = email.from || email.sender;

return [
  {
    json: {
      senderName: sender.name || 'Sin nombre',
      senderEmail: sender.email,
      subject: email.subject,
      date: new Date(email.date).toLocaleString('es-ES'),
      body: email.text || email.html,
      threadId: email.threadId
    }
  }
];
```

---

### **4. Notion** (Crear página)
- **Operation**: `Create Page`
- **Database ID**: ID de tu base de datos en Notion
- **Properties** (ejemplo de mapeo):
  | Propiedad Notion | Campo n8n |
  |------------------|-----------|
  | Nombre           | `senderName` |
  | Email            | `senderEmail` |
  | Asunto           | `subject` |
  | Fecha            | `date` |
  | Cuerpo           | `body` |

**Nota**: Crea primero la base de datos en Notion con estas propiedades.

---

### **5. Slack** (Notificación)
- **Operation**: `Send Message`
- **Channel**: `#tu-canal`
- **Message**:
```
📧 *Nuevo email con propuesta/cotización*

👤 *Remitente:* {{senderName}}
📧 *Email:* {{senderEmail}}
📝 *Asunto:* {{subject}}
📅 *Fecha:* {{date}}
```

---

## **Variables de entorno necesarias:**
1. **Gmail**: OAuth2 conectado
2. **Notion**: API Key + Database ID
3. **Slack**: Bot Token + Channel ID

---

## **Ejemplo de salida del Function node:**
```json
{
  "senderName": "Juan Pérez",
  "senderEmail": "juan@empresa.com",
  "subject": "Propuesta comercial Q4",
  "date": "15/03/2025 10:30:00",
  "body": "Hola, adjunto nuestra propuesta...",
  "threadId": "18a2b3c4d5e6"
}
```

---

## **Optimizaciones posibles:**
- Agregar un **HTTP Request** para buscar en CRM si el email ya existe
- Usar **Merge** para comparar con registros anteriores
- Añadir **Error Handling** con Slack si falla Notion

¿Necesitas que te ayude con la configuración exacta de algún nodo en específico o con el mapeo de propiedades en Notion?