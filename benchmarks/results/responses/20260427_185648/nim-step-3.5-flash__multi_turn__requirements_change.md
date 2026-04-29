# Step 3.5 Flash (NIM) — multi_turn/requirements_change

- model_id: `stepfun-ai/step-3.5-flash`
- success: True  | final: 6.53 | quality: 7.52
- latency_total: 40.995s | tokens_per_second: 40.9
- input_tokens: 264 | output_tokens: 1676
- judge_score: 4.0 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes el workflow ajustado a tus nuevos requerimientos:

---

### **Workflow N8N: Gmail → Notion + Notificación Slack**

**Objetivo:**  
Leer emails de Gmail que contengan **"propuesta"** o **"cotización"** en el asunto, extraer datos del remitente, guardarlos en Notion y notificar por Slack.

---

### **Nodos y Configuración:**

#### 1. **Gmail Trigger**  
- **Tipo:** `Gmail Trigger` (evento: *New Email*)  
- **Filtro en el propio nodo Gmail:**  
  En el campo **"Search Query"** (consulta de búsqueda), usa:  
  ```plaintext
  subject:propuesta OR subject:cotizacion
  ```
  *Esto filtra solo emails con esas palabras en el asunto.*  
- **Opciones recomendadas:**  
  - Marcar `Mark as read` si no quieres que se queden como no leídos.  
  - Ajusta el intervalo de revisión (ej: cada 5 minutos).

---

#### 2. **Function Node** (Extracción y formateo)  
```javascript
// Extraer datos clave del email
const email = $input.all()[0].json;

// Parsear remitente (ej: "Juan Pérez <juan@empresa.com>")
let fromName = "Desconocido";
let fromEmail = "Sin email";

if (email.from) {
  const match = email.from.match(/^(.*?)\s*<(.*?)>$/);
  if (match) {
    fromName = match[1].trim();
    fromEmail = match[2];
  } else {
    fromEmail = email.from;
  }
}

// Formato de fecha (opcional: convertir a formato legible)
const date = new Date(email.date).toLocaleString();

return [{
  json: {
    nombre_remitente: fromName,
    email_remitente: fromEmail,
    asunto: email.subject || "Sin asunto",
    fecha: date,
    // Guardar también el ID del email para evitar duplicados
    gmail_id: email.id,
    // Enlace directo al email en Gmail
    gmail_link: `https://mail.google.com/mail/u/0/#inbox/${email.id}`
  }
}];
```

---

#### 3. **Notion Node** (Crear página en base de datos)  
- **Tipo:** `Notion` → `Create`  
- **Conexión:**  
  - **Integration:** Conecta tu integración de Notion (crea una en [notion.so/my-integrations](https://www.notion.so/my-integrations)).  
  - **Database:** Selecciona la base de datos de Notion donde guardarás los registros.  
- **Mapeo de propiedades:**  
  Asegúrate de que tu base de datos en Notion tenga estas propiedades (con los mismos nombres o mapea manualmente):  
  - `nombre_remitente` → Tipo: *Title* (o *Text* si no es título).  
  - `email_remitente` → Tipo: *Text*.  
  - `asunto` → Tipo: *Text*.  
  - `fecha` → Tipo: *Date*.  
  - `gmail_link` → Tipo: *URL*.  
  - `gmail_id` → Tipo: *Text* (oculto si no quieres mostrarlo).  
- **Nota:** En Notion, la propiedad **Title** es obligatoria; usualmente se usa `asunto` o `nombre_remitente`.

---

#### 4. **Slack Node** (Notificación)  
- **Tipo:** `Slack` → `Post`  
- **Conexión:** Usa un *Webhook URL* de Slack (crea una app en [api.slack.com](https://api.slack.com/) y activa *Incoming Webhooks*).  
- **Configuración:**  
  - **Channel:** El canal donde llegarán las notificaciones (ej: `#cotizaciones`).  
  - **Message:** Personaliza con datos del email:  
    ```plaintext
    � Nueva propuesta/cotización recibida:
    *De:* {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
    *Asunto:* {{ $json.asunto }}
    *Fecha:* {{ $json.fecha }}
    <{{ $json.gmail_link }}|Ver en Gmail>
    ```
  - **Username/Emoji:** Opcional (ej: "Bot Cotizaciones" 🤖).

---

### **Flujo Completo:**
```
Gmail Trigger (filtrado por asunto) 
→ Function Node (extrae y formatea) 
→ Notion (crea registro) 
→ Slack (envía notificación)
```

---

### **Consideraciones Adicionales:**

1. **Evitar duplicados en Notion:**  
   - Usa la propiedad `gmail_id` (ID único del email) para buscar existentes antes de crear.  
   - En el nodo Notion, puedes usar la opción **"Update if exists"** con un filtro por `gmail_id`.  
   - O bien, en un **Function Node** previo, hacer una llamada a la API de Notion para buscar si ya existe.

2. **Manejo de errores:**  
   - Agrega un **Error Trigger** para capturar fallos en Notion/Slack y notificarlos por otro canal (ej: email).

3. **Pruebas:**  
   - Activa el workflow en modo *Manual* primero y envía un email de prueba con "propuesta" en el asunto.

4. **Permisos:**  
   - En Gmail: Asegúrate de que la cuenta tenga menos seguridad de apps activada o usa OAuth2.  
   - En Notion: Comparte la base de datos con la integración (en Notion: `...` → *Add connections* → selecciona tu integración).

---

¿Necesitas ayuda con la configuración específica de algún nodo (por ejemplo, cómo obtener el Database ID de Notion)?