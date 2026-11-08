# DeepSeek V3 — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 4.71 | quality: 4.0
- latency_total: 20.969s | tokens_per_second: 38.9
- input_tokens: 244 | output_tokens: 816

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

Excelente, el workflow se vuelve más completo. Te propongo esta estructura:

## Workflow N8N: Filtro de Emails → Notion + Slack

### **Nodos necesarios:**

1. **Gmail Trigger** - Lee emails nuevos
2. **IF node** - Filtra por "propuesta" o "cotización" en el asunto
3. **Function node** - Extrae datos del remitente
4. **Notion node** - Crea página en base de datos
5. **Slack node** - Envía notificación

---

### **Configuración detallada:**

#### **1. Gmail Trigger**
- **Credenciales**: Conectar cuenta de Gmail
- **Trigger**: "Email Received"
- **Options**: 
  - `Simplify Output`: ✅ Activado
  - `Ignore SSL Issues`: ✅ (si tienes problemas)

#### **2. IF node** (filtro por asunto)
```javascript
// Filtra emails con palabras clave
const subject = $json.subject.toLowerCase();
const keywords = ['propuesta', 'cotizacion', 'cotización'];

return keywords.some(keyword => subject.includes(keyword));
```

#### **3. Function node** (extracción de datos)
```javascript
// Extrae datos del remitente del email
const email = $json.from.value[0];

// Separar nombre y email
const match = email.address.match(/(.*)<(.*)>/);
let nombre = '';
let emailAddress = '';

if (match) {
  nombre = match[1].trim();
  emailAddress = match[2].trim();
} else {
  nombre = email.name || '';
  emailAddress = email.address;
}

// Crear objeto con los datos
return {
  json: {
    remitente_nombre: nombre,
    remitente_email: emailAddress,
    asunto: $json.subject,
    fecha: $json.date,
    contenido: $json.textPlain || $json.textHtml,
    email_id: $json.messageId
  }
};
```

#### **4. Notion node** (crear página)
- **Resource**: Page
- **Operation**: Create
- **Database ID**: Tu ID de base de datos de Notion
- **Properties** (mapeo):
  - **Título**: `{{$json.remitente_nombre}} - {{$json.asunto}}`
  - **Email**: `{{$json.remitente_email}}`
  - **Fecha**: `{{$json.fecha}}`
  - **Asunto**: `{{$json.asunto}}`
  - **Estado**: "Por revisar" (propiedad select)

#### **5. Slack node** (notificación)
- **Resource**: Message
- **Operation**: Post
- **Channel ID**: ID del canal de Slack
- **Text**:
```text
📬 *Nueva propuesta recibida*
*De:* {{$json.remitente_nombre}}
*Email:* {{$json.remitente_email}}
*Asunto:* {{$json.asunto}}
*Enviado a:* Notion ✅
```

---

### **Flujo alternativo (opcional):**
- Agregar un **Error Trigger** para manejar fallos
- Agregar un **Delay node** si recibes muchos emails
- Usar **Webhook node** si quieres notificaciones adicionales

### **Consideraciones importantes:**
1. **Notion**: Necesitas crear una base de datos primero y obtener su ID
2. **Slack**: Necesitas crear una app en Slack y obtener permisos
3. **Gmail**: Verifica que tengas acceso IMAP habilitado

¿Quieres que te explique cómo configurar las credenciales o necesitas ajustes específicos?