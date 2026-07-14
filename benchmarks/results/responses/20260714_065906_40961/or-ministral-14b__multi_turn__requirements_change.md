# Ministral 14B — multi_turn/requirements_change

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 6.26 | quality: 6.0
- latency_total: 17.268s | tokens_per_second: 97.1
- input_tokens: 227 | output_tokens: 1676
- judge_score: 3.0 | justificación: La respuesta es parcialmente precisa y clara, pero no cumple con el requisito original de guardar los datos en Google Sheets, en su lugar sugiere Notion y Slack, lo que reduce su relevancia y coherencia contextual.

## Respuesta completa

¡Perfecto! Vamos a crear un **workflow en n8n** que:
1. **Monitoree Gmail** (solo emails con "propuesta" o "cotización" en el asunto).
2. **Extraiga datos** del remitente (nombre, email, asunto, cuerpo, etc.).
3. **Guarde en Notion** (en una base de datos o tabla específica).
4. **Envía una notificación a Slack** cuando llegue un email relevante.

---

### **📌 Workflow en n8n (paso a paso)**

#### **1. Configuración inicial**
- **Trigger**: **Gmail - Watch Emails** (buscar el nodo en la barra de búsqueda).
  - **Autenticación**: Conecta tu cuenta de Gmail (usa OAuth2).
  - **Query** (filtro):
    ```
    subject:propuesta OR subject:cotización
    ```
    *(Esto busca emails donde el asunto contenga "propuesta" o "cotización", en cualquier formato: "Propuesta X", "Cotización 2024", etc.)*
  - **Start Date**: Puedes dejarlo en blanco para capturar todos los nuevos emails.

---

#### **2. Extraer datos del email (Function Node)**
Agrega un **Function Node** para estructurar los datos antes de enviarlos a Notion y Slack.
**Código JavaScript (modificable):**
```javascript
// Extrae datos clave del email
const emailData = {
  id: $node["Gmail"].json["id"],
  threadId: $node["Gmail"].json["threadId"],
  subject: $node["Gmail"].json["payload"]["headers"].find(h => h.name === "Subject").value,
  from: $node["Gmail"].json["payload"]["headers"].find(h => h.name === "From").value,
  fromName: $node["Gmail"].json["payload"]["headers"].find(h => h.name === "From").name,
  date: $node["Gmail"].json["payload"]["headers"].find(h => h.name === "Date").value,
  body: $node["Gmail"].json["payload"]["parts"][0].body,
  labels: $node["Gmail"].json["labelIds"],
  snippet: $node["Gmail"].json["snippet"]
};

// Formatea el mensaje para Slack (opcional)
const slackMessage = {
  text: `📬 *Nuevo email con palabra clave:*\n` +
        `📌 **Asunto:** ${emailData.subject}\n` +
        `👤 **De:** ${emailData.fromName} <${emailData.from}>\n` +
        `📅 **Fecha:** ${emailData.date}\n` +
        `🔗 *Email:* ${emailData.snippet}`
};

return [
  { json: emailData }, // Para Notion
  { json: slackMessage } // Para Slack
];
```

---

#### **3. Guardar en Notion (Notion - Add a New Database Item)**
Agrega el nodo **Notion - Add a New Database Item**.
- **Autenticación**: Conecta tu cuenta de Notion (usa la API key de integración).
- **Database ID**: La ID de tu base de datos en Notion (ej: `https://www.notion.so/workspace/...` → extrae el ID de la URL).
- **Properties** (campos):
  | Campo en Notion       | Valor desde el email               |
  |-----------------------|------------------------------------|
  | `Asunto`              | `{{ $node["Function"].json[0].subject }}` |
  | `Remitente`           | `{{ $node["Function"].json[0].from }}` |
  | `Nombre del remitente`| `{{ $node["Function"].json[0].fromName }}` |
  | `Fecha`               | `{{ $node["Function"].json[0].date }}` |
  | `Cuerpo`              | `{{ $node["Function"].json[0].body }}` |
  | `ID del email`        | `{{ $node["Function"].json[0].id }}` (opcional, para referencia) |

*(Asegúrate de que los nombres de los campos en Notion coincidan exactamente con los de la tabla.)*

---

#### **4. Notificar en Slack (Slack - Send Message)**
Agrega el nodo **Slack - Send Message**.
- **Autenticación**: Conecta tu cuenta de Slack (usa una **Webhook Incoming** o un **Token de Usuario**).
- **Channel**: El canal donde quieres recibir las notificaciones (ej: `#alertas-emails`).
- **Message**: Usa el formato preparado en el **Function Node**:
  ```plaintext
  {{ $node["Function"].json[1].text }}
  ```
*(O personaliza el mensaje directamente aquí si prefieres otro formato.)*

---

#### **5. (Opcional) Marcar el email como leído o moverlo a una carpeta**
Si quieres evitar procesar el mismo email dos veces, puedes agregar un nodo **Gmail - Modify Email** para:
- **Marcarlo como leído** (`read`).
- **Moverlo a una carpeta** (ej: "Propuestas recibidas") usando `labelIds`.

---

### **🔄 Ejecución del workflow**
1. **Guarda el workflow** en n8n.
2. **Actívalo** (el botón de "play" en la esquina superior derecha).
3. **Prueba enviando un email** con "propuesta" o "cotización" en el asunto.
   - Deberías ver:
     - Una nueva entrada en Notion.
     - Un mensaje en Slack.

---

### **🔧 Posibles mejoras**
1. **Filtros más específicos**:
   - Usar `subject:propuesta AND label:inbox` para solo emails no marcados.
   - Excluir remitentes específicos (ej: `from:no-reply@dominio.com`).
2. **Extraer datos adicionales**:
   - Adjuntos (si hay archivos, usa el nodo **Gmail - Get Email Attachments**).
   - Parsear el cuerpo del email para extraer precios, fechas, etc. (con expresiones regulares).
3. **Notificaciones por prioridad**:
   - Usar colores en Slack (`:red[URGENTE]`) o emojis según el asunto.
4. **Automatizar respuestas**:
   - Agregar un nodo **Gmail - Send Email** para responder automáticamente.

---
### **📌 Ejemplo visual del workflow**
```
Gmail (Trigger) → [Filtra emails con "propuesta" o "cotización"]
       ↓
Function Node → [Estructura datos para Notion y Slack]
       ↓
Notion (Add Item) → [Guarda en base de datos]
       ↓
Slack (Send Message) → [Notifica en canal]
```

---
### **⚠️ Notas importantes**
- **Permisos en Gmail**: Asegúrate de que la cuenta de Gmail tenga acceso a "Gmail API" y los permisos necesarios.
- **Notion**: La base de datos debe estar configurada con los campos correctos antes de ejecutar el workflow.
- **Slack**: Usa un **Webhook Incoming** para evitar problemas de autenticación.

Si necesitas ayuda con algún paso en específico (ej: configurar Notion o Slack), dime y te doy detalles adicionales. ¡También puedo compartir un ejemplo de workflow exportable si lo prefieres!