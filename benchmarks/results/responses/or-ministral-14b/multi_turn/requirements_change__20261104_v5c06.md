# Ministral 14B — multi_turn/requirements_change

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 6.21 | quality: 6.0
- latency_total: 26.181s | tokens_per_second: 36.7
- input_tokens: 215 | output_tokens: 962

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

¡Perfecto! Aquí tienes el **workflow completo en n8n** para:
✅ **Filtrar emails** con *"propuesta"* o *"cotización"* en el asunto.
✅ **Extraer datos** (remitente, asunto, cuerpo, fecha, etc.).
✅ **Guardar en Notion** (como una base de datos o página).
✅ **Enviar notificación a Slack** cuando llegue un email relevante.

---

### **🔧 Workflow en n8n (paso a paso)**
#### **1. Nodo Trigger: Gmail (Polling)**
- **Tipo de nodo**: *Gmail*
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Gmail (usa OAuth 2.0).
  - **Operation**: `Get All Emails` (o `Get New Emails` si prefieres solo los no leídos).
  - **Max Items**: `1` (para procesar uno por vez).
  - **Filter**:
    - **Subject**: `contains("propuesta") OR contains("cotización")` (case insensitive).
    - **Unread**: `true` (opcional, si quieres solo emails no leídos).

🔹 *Nota*: Si usas `Get New Emails`, n8n marcará el email como leído automáticamente.

---

#### **2. Nodo Function (Opcional: Formatear datos)**
Si quieres estructurar los datos antes de enviarlos a Notion/Slack:
```javascript
// Ejemplo: Extraer solo lo necesario
const email = $input.all()[0];

return {
  remitente: email.from,
  nombreRemitente: email.fromName,
  asunto: email.subject,
  cuerpo: email.textPlain || email.textHtml,
  fecha: email.date,
  idGmail: email.id,
  etiquetas: email.labels
};
```
*(Puedes ajustar los campos según lo que necesites en Notion).*

---

#### **3. Nodo Notion (Guardar en base de datos)**
- **Tipo de nodo**: *Notion*
- **Configuración**:
  - **Authentication**: Conecta tu integración de Notion (API Key).
  - **Operation**: `Create a Database Row` (o `Create a Page` si prefieres formato libre).
  - **Database ID**: La ID de tu base de datos de Notion (ej: `abc123...`).
  - **Properties**:
    | Campo en Notion       | Valor desde Gmail                     |
    |------------------------|---------------------------------------|
    | `Remitente`            | `{{ $json["remitente"] }}`             |
    | `Asunto`               | `{{ $json["asunto"] }}`                |
    | `Fecha`                | `{{ $json["fecha"] }}` (formatear como `YYYY-MM-DD`) |
    | `Cuerpo`               | `{{ $json["cuerpo"] }}` (truncar si es largo) |
    | `Etiqueta` (select)    | `Email` (o una etiqueta personalizada) |

🔹 *Para formatear la fecha en Notion*:
Usa un **Function Node** antes de Notion con:
```javascript
return {
  ...$input.all()[0],
  fechaFormateada: new Date($input.all()[0].fecha).toISOString().split('T')[0]
};
```
Y luego en Notion usa `{{ $json["fechaFormateada"] }}`.

---

#### **4. Nodo Slack (Notificación)**
- **Tipo de nodo**: *Slack*
- **Configuración**:
  - **Authentication**: Conecta tu workspace de Slack (OAuth).
  - **Operation**: `Send a Message`.
  - **Channel**: `#notificaciones-emails` (o el que prefieras).
  - **Message**:
    ```
    📬 **Nuevo email relevante**:
    - **Asunto**: {{ $json["asunto"] }}
    - **Remitente**: {{ $json["nombreRemitente"] }} <{{ $json["remitente"] }}>
    - **Fecha**: {{ $json["fecha"] }}
    - **Vista**: [Abrir en Gmail]({{ "https://mail.google.com/mail/u/0/#inbox/" + $json["idGmail"] }})

    *Cuerpo*: {{ $json["cuerpo"].substring(0, 200) }}... *(truncado)*
    ```
  - **Username**: `n8n-Bot` (opcional).
  - **Icon**: `:email:` (emoji de email).

---

#### **5. Nodo HTTP Request (Opcional: Webhook para más acciones)**
Si quieres que el workflow sea más flexible (ej: enviar el email a otro sistema), puedes añadir un **HTTP Request** para disparar un webhook.

---

### **📌 Ejemplo visual del workflow**
```
Gmail (Trigger)
       ↓
[Function] (Formatear datos)
       ↓
Notion (Guardar en BD)
      