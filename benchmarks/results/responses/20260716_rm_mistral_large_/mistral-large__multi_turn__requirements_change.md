# Mistral Large — multi_turn/requirements_change

- model_id: `mistralai/mistral-large`
- success: True  | final: 5.66 | quality: 6.0
- latency_total: 20.6s | tokens_per_second: 65.4
- input_tokens: 227 | output_tokens: 1347
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de leer emails de Gmail y guardar datos en un Google Sheet, en su lugar, introduce Notion y Slack, lo que reduce su relevancia y utilidad práctica.

## Respuesta completa

¡Perfecto! Aquí tienes el flujo detallado para **n8n** que cumple con todos tus requisitos:

---

### **Workflow: Gmail → Filtrar por asunto → Notion + Notificación en Slack**
*(Pasos y configuración de cada nodo)*

---

### **1. Nodo: Gmail Trigger**
**Configuración:**
- **Resource:** `Message`
- **Operation:** `On Email Received` (se activa cuando llega un nuevo email).
- **Authentication:** Conecta tu cuenta de Gmail (OAuth2).
- **Options:**
  - **Download Attachments:** `False` (a menos que necesites adjuntos).
  - **Format:** `Resolved` (para obtener datos estructurados).

---

### **2. Nodo: IF (Filtrar emails con "propuesta" o "cotización")**
**Configuración:**
- **Condition:** `String`
- **Value 1:** `{{ $node["Gmail Trigger"].json["subject"] }}`
- **Operation:** `Contains` (contiene).
- **Value 2:** `propuesta,cotizacion` (n8n buscará cualquiera de estas palabras en el asunto).
  - *Nota:* Si quieres que sea **case-insensitive** (mayúsculas/minúsculas), usa una **Function** para convertir el asunto a minúsculas:
    ```javascript
    return $node["Gmail Trigger"].json["subject"].toLowerCase().includes("propuesta") ||
           $node["Gmail Trigger"].json["subject"].toLowerCase().includes("cotizacion");
    ```

**Salidas:**
- **True Branch:** El email cumple la condición → sigue el flujo.
- **False Branch:** Ignora el email (puedes dejarlo vacío o conectarlo a un nodo de "No Operation").

---

### **3. Nodo: Function (Extraer datos del remitente)**
**Código JavaScript:**
```javascript
// Extraer datos del remitente (nombre y email)
const sender = $node["Gmail Trigger"].json["from"];
const emailRegex = /<([^>]+)>/; // Extrae el email entre < >
const email = sender.match(emailRegex) ? sender.match(emailRegex)[1] : sender;
const name = sender.replace(emailRegex, '').trim();

// Obtener fecha del email (en formato ISO)
const date = $node["Gmail Trigger"].json["date"];

// Obtener asunto
const subject = $node["Gmail Trigger"].json["subject"];

// Devolver datos estructurados para Notion
return {
  email: email,
  name: name,
  subject: subject,
  date: date,
  status: "Nuevo" // Campo opcional para Notion
};
```

---

### **4. Nodo: Notion (Agregar página a una base de datos)**
**Configuración:**
- **Resource:** `Database Page`
- **Operation:** `Create`
- **Authentication:** Conecta tu cuenta de Notion (integración con API).
- **Database ID:** ID de tu base de datos en Notion (ej: `https://www.notion.so/workspace/123456789?v=abcdef` → el ID es `123456789`).
- **Properties:**
  - **Name (Título):** `{{ $node["Function"].json["subject"] }}`
  - **Email (Email):** `{{ $node["Function"].json["email"] }}`
  - **Nombre (Text):** `{{ $node["Function"].json["name"] }}`
  - **Fecha (Date):** `{{ $node["Function"].json["date"] }}`
  - **Estado (Select):** `{{ $node["Function"].json["status"] }}`

*Nota:* Asegúrate de que los nombres de las propiedades en Notion coincidan exactamente con los que usas en n8n.

---

### **5. Nodo: Slack (Notificación)**
**Configuración:**
- **Resource:** `Message`
- **Operation:** `Post`
- **Authentication:** Conecta tu cuenta de Slack (OAuth2 o token de bot).
- **Channel:** `#notificaciones` o el canal que prefieras.
- **Text:**
  ```
  📬 *Nueva propuesta/cotización recibida*
  *Remitente:* {{ $node["Function"].json["name"] }} ({{ $node["Function"].json["email"] }})
  *Asunto:* {{ $node["Function"].json["subject"] }}
  *Fecha:* {{ $node["Function"].json["date"] }}
  ```
- **Options:**
  - **As User:** `False` (para que aparezca como el bot).
  - **Icon Emoji:** `:email:` (opcional).

---

### **Diagrama del Workflow**
```
Gmail Trigger → IF (Filtrar) → Function (Extraer datos)
       ↓ (True)
Notion (Guardar) → Slack (Notificar)
       ↓ (False)
[Fin del flujo]
```

---

### **Pasos adicionales recomendados:**
1. **Prueba el flujo:**
   - Usa el modo **"Test Workflow"** en n8n para enviar un email de prueba con el asunto "Prueba propuesta".
   - Verifica que los datos aparezcan en Notion y que Slack reciba la notificación.

2. **Manejo de errores:**
   - Agrega un nodo **Error Trigger** para capturar fallos (ej: si Notion no responde) y enviar una alerta a Slack.

3. **Optimización:**
   - Si recibes muchos emails, considera usar el nodo **Gmail** con la operación `Search` en lugar de `On Email Received` para procesar emails en batch (ej: cada hora).

---

### **Ejemplo de salida en Notion:**
| Name          | Email               | Subject               | Date                  | Status |
|---------------|---------------------|-----------------------|-----------------------|--------|
| Juan Pérez    | juan@ejemplo.com    | Cotización proyecto X | 2023-10-15T10:00:00Z  | Nuevo  |

---

¿Necesitas ayuda para configurar algún nodo en específico o ajustar algo más? 😊