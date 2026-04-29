# Mistral Large 3 675B (NIM) — multi_turn/requirements_change

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 5.85 | quality: 5.28
- latency_total: 214.165s | tokens_per_second: 6.1
- input_tokens: 228 | output_tokens: 1313
- judge_score: 2.4 | justificación: 

## Respuesta completa

¡Perfecto! Aquí tienes el flujo ajustado para **Notion + Slack** con filtros por palabras clave (`propuesta` o `cotización`). Te detallo cada nodo:

---

### **1. Nodo Trigger: Gmail**
- **Tipo**: *Gmail Trigger*
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Gmail (usa OAuth2).
  - **Options**:
    - **Trigger On**: `New Email` (se activa con cada email nuevo).
    - **Polling Interval**: `5 minutes` (o el tiempo que prefieras).
    - **Max Results**: `1` (para procesar uno por uno).

---

### **2. Nodo IF: Filtrar por asunto**
- **Tipo**: *IF*
- **Configuración**:
  - **Condition**:
    - **Value 1**: `{{ $node["Gmail Trigger"].json["subject"] }}`
    - **Operation**: `Contains` (contiene).
    - **Value 2**: `propuesta,cotización` (separado por comas para buscar ambas palabras).
  - **Output**:
    - **True**: Continúa el flujo si el asunto coincide.
    - **False**: Termina el flujo (ignorar email).

---

### **3. Nodo Function: Extraer datos del remitente**
- **Tipo**: *Function*
- **Código** (extrae nombre, email, asunto, fecha y body):
```javascript
// Extraer datos del remitente
const sender = $node["Gmail Trigger"].json["from"];
const emailMatch = sender.match(/<(.*)>/);
const email = emailMatch ? emailMatch[1] : sender;
const name = sender.split("<")[0].trim();

// Datos del email
const subject = $node["Gmail Trigger"].json["subject"];
const date = $node["Gmail Trigger"].json["date"];
const body = $node["Gmail Trigger"].json["textPlain"] || "Sin texto plano";

// Devolver datos estructurados para Notion
return [{
  json: {
    senderName: name,
    senderEmail: email,
    subject: subject,
    date: date,
    body: body
  }
}];
```
**Salida esperada**:
```json
{
  "senderName": "Juan Pérez",
  "senderEmail": "juan@example.com",
  "subject": "Propuesta de servicio",
  "date": "2023-10-15T10:00:00.000Z",
  "body": "Hola, adjunto mi propuesta..."
}
```

---

### **4. Nodo Notion: Guardar datos**
- **Tipo**: *Notion* (Node *Append Block* o *Create Page* según tu base de datos).
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Notion.
  - **Resource**: `Database Page`.
  - **Operation**: `Create`.
  - **Database ID**: ID de tu base de datos en Notion (ej: `a1b2c3d4e5`).
  - **Properties**:
    - **Name**: `{{ $node["Function"].json["senderName"] }}`.
    - **Email** (columna tipo "Email"): `{{ $node["Function"].json["senderEmail"] }}`.
    - **Subject** (columna tipo "Text"): `{{ $node["Function"].json["subject"] }}`.
    - **Date** (columna tipo "Date"): `{{ $node["Function"].json["date"] }}`.
    - **Body** (columna tipo "Text"): `{{ $node["Function"].json["body"] }}`.

**Ejemplo de base de datos en Notion**:
| Propiedad  | Tipo     |
|------------|----------|
| Name       | Title    |
| Email      | Email    |
| Subject    | Text     |
| Date       | Date     |
| Body       | Text     |

---

### **5. Nodo Slack: Notificación**
- **Tipo**: *Slack*
- **Configuración**:
  - **Authentication**: Conecta tu workspace de Slack.
  - **Resource**: `Message`.
  - **Operation**: `Post`.
  - **Channel**: `#notificaciones` (o el canal que prefieras).
  - **Text**:
    ```
    📬 *Nuevo email con propuesta/cotización*
    *Remitente*: {{ $node["Function"].json["senderName"] }} ({{ $node["Function"].json["senderEmail"] }})
    *Asunto*: {{ $node["Function"].json["subject"] }}
    *Fecha*: {{ $node["Function"].json["date"] }}
    ```
  - **Options**:
    - **As User**: `True` (para que aparezca como tu usuario).
    - **Icon Emoji**: `:email:` (opcional).

---

### **6. Nodo Error Handler (Opcional)**
- **Tipo**: *Error Trigger* (para manejar fallos).
- **Configuración**:
  - Conecta este nodo a todos los anteriores.
  - Envía un mensaje a Slack o email si algo falla (ej: error al guardar en Notion).

---

### **Diagrama del flujo**:
```
Gmail Trigger → IF (filtrar asunto) → Function (extraer datos) → Notion → Slack
                     ↓ (False)
                   [Terminar]
```

---

### **Pasos adicionales**:
1. **Notion**:
   - Crea una base de datos con las propiedades mencionadas.
   - Comparte la base con tu integración de Notion (en *Settings & Members* > *Integrations*).
2. **Slack**:
   - Asegúrate de que el bot tenga permisos para enviar mensajes en el canal.
3. **Pruebas**:
   - Envía un email de prueba con asunto `Cotización de prueba` para verificar que todo funcione.

¿Necesitas ayuda con algún paso en específico? Por ejemplo, ¿cómo obtener el `Database ID` de Notion o configurar la autenticación en Slack?