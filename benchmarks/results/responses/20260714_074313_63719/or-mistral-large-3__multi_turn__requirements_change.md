# Mistral Large 3 675B — multi_turn/requirements_change

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 4.51 | quality: 4.0
- latency_total: 22.263s | tokens_per_second: 65.0
- input_tokens: 227 | output_tokens: 1447
- judge_score: 1 | justificación: La respuesta no cumple con los requisitos originales de leer emails de Gmail y guardar datos en un Google Sheet, sino que introduce Notion y Slack, lo que la hace irrelevante y poco precisa.

## Respuesta completa

¡Perfecto! Aquí tienes el **workflow completo en n8n** con los ajustes que necesitas:

---

### **Workflow: Gmail → Notion + Slack (filtrando "propuesta" o "cotización")**
*(Pasos detallados con configuración de cada nodo)*

---

### **1. Gmail Trigger (Disparador)**
- **Nodo**: `Gmail Trigger`
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Gmail (OAuth2).
  - **Resource**: `Message`
  - **Operation**: `On Email Received`
  - **Options**:
    - **Label**: `INBOX` (o el label que prefieras).
    - **Polling Interval**: `5 minutes` (o el tiempo que desees).

---

### **2. IF Node (Filtrar emails con "propuesta" o "cotización")**
- **Nodo**: `IF`
- **Configuración**:
  - **Conditions**:
    - **String** → `Subject` (del Gmail Trigger) **contains** `propuesta` (ignora mayúsculas/minúsculas).
    - **OR** (añade otra condición con el operador `OR`).
    - **String** → `Subject` **contains** `cotizacion`.
  - **Output**:
    - **True Branch**: Continúa el workflow (emails que cumplen la condición).
    - **False Branch**: Termina el workflow (emails que no cumplen).

---

### **3. Function Node (Extraer datos del remitente)**
- **Nodo**: `Function`
- **Código JavaScript** (para parsear el remitente y otros datos):
  ```javascript
  // Extraer datos del email
  const from = $node["Gmail Trigger"].json["from"];
  const subject = $node["Gmail Trigger"].json["subject"];
  const date = $node["Gmail Trigger"].json["date"];

  // Parsear el nombre y email del remitente (ejemplo: "Nombre Apellido <email@dominio.com>")
  const emailRegex = /<([^>]+)>/;
  const nameRegex = /^([^<]+)/;

  const email = from.match(emailRegex) ? from.match(emailRegex)[1] : from;
  const name = from.match(nameRegex) ? from.match(nameRegex)[1].trim() : "Sin nombre";

  // Devolver datos estructurados para Notion
  return {
    nombre: name,
    email: email,
    asunto: subject,
    fecha: date,
  };
  ```

---

### **4. Notion Node (Guardar en una base de datos)**
- **Nodo**: `Notion`
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Notion (API Key + Database ID).
  - **Resource**: `Database Page`
  - **Operation**: `Create Page`
  - **Database ID**: ID de tu base de datos en Notion (ejemplo: `12345678-1234-5678-1234-567812345678`).
  - **Properties**:
    - **Nombre**: `{{ $node["Function"].json["nombre"] }}`
    - **Email**: `{{ $node["Function"].json["email"] }}`
    - **Asunto**: `{{ $node["Function"].json["asunto"] }}`
    - **Fecha**: `{{ $node["Function"].json["fecha"] }}`
    - **Estado**: `Nuevo` (o el valor que prefieras).
  - **Options**:
    - **Simplify Output**: `true` (para facilitar el mapeo).

*(Nota: Asegúrate de que tu base de datos en Notion tenga las columnas correspondientes: `Nombre`, `Email`, `Asunto`, `Fecha`, `Estado`).*

---

### **5. Slack Node (Notificación)**
- **Nodo**: `Slack`
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Slack (OAuth2 o Webhook).
  - **Resource**: `Message`
  - **Operation**: `Post Message`
  - **Channel**: `#notificaciones` (o el canal que prefieras).
  - **Text**:
    ```
    📧 *Nueva propuesta/cotización recibida* 📧
    *Remitente*: {{ $node["Function"].json["nombre"] }} ({{ $node["Function"].json["email"] }})
    *Asunto*: {{ $node["Function"].json["asunto"] }}
    *Fecha*: {{ $node["Function"].json["fecha"] }}
    ```
  - **Options**:
    - **As User**: `true` (para que aparezca como tu usuario).
    - **Icon Emoji**: `:email:` (opcional).

---

### **6. (Opcional) Error Handling**
- **Nodo**: `Error Trigger` (para manejar errores en el workflow).
  - Conecta este nodo a los nodos anteriores para recibir notificaciones si algo falla.

---

### **Diagrama del Workflow**
```
Gmail Trigger → IF (filtrar) → Function (parsear) → Notion (guardar) → Slack (notificar)
                     |
                     → (False Branch: Terminar)
```

---

### **Notas importantes**:
1. **Notion**:
   - Necesitas crear una base de datos en Notion con las propiedades mencionadas.
   - Obtén el `Database ID` desde la URL de tu base de datos en Notion (ejemplo: `https://www.notion.so/workspace/12345678-1234-5678-1234-567812345678?v=...`).
   - Genera una **API Key** en Notion (Settings → Integrations).

2. **Slack**:
   - Si usas un **Webhook**, configúralo en Slack (Apps → Incoming Webhooks).
   - Si usas **OAuth2**, autoriza la app de n8n en Slack.

3. **Gmail**:
   - Asegúrate de que n8n tenga permisos para leer tus emails (OAuth2).

---

### **¿Necesitas ayuda con algo más?**
- ¿Quieres que el workflow también extraiga archivos adjuntos del email?
- ¿O prefieres que los datos se guarden en una tabla específica de Notion con formato?
- ¿Necesitas que la notificación de Slack incluya un botón para "Aceptar/Rechazar" la propuesta?