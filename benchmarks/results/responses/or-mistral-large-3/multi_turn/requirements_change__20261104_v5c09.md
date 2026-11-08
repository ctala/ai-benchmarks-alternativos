# Mistral Large 3 675B — multi_turn/requirements_change

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 4.51 | quality: 4.0
- latency_total: 14.764s | tokens_per_second: 98.9
- input_tokens: 227 | output_tokens: 1460

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

¡Perfecto! Aquí tienes el **workflow completo en n8n** con los ajustes que necesitas:

---

### **1. Gmail Trigger (Disparador)**
- **Nodo**: *Gmail Trigger*
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Gmail.
  - **Options**:
    - **Trigger On**: `New Email` (o `New Labeled Email` si prefieres usar una etiqueta).
    - **Polling Interval**: Cada 5-10 minutos (ajusta según necesidad).
  - **Filter** (opcional):
    - Si quieres filtrar por etiqueta (ej: "Propuestas"), configúralo aquí.

---

### **2. Function Node (Filtrar emails con "propuesta" o "cotización")**
- **Nodo**: *Function*
- **Código** (para filtrar solo emails con las palabras clave en el asunto):
  ```javascript
  // Extraer el asunto del email
  const subject = $input.all()[0].json.subject;

  // Convertir a minúsculas para comparación insensible a mayúsculas
  const lowerSubject = subject.toLowerCase();

  // Filtrar si contiene "propuesta" o "cotizacion"
  if (lowerSubject.includes("propuesta") || lowerSubject.includes("cotizacion")) {
    return $input.all(); // Continúa el workflow
  } else {
    return []; // Detiene el workflow para este email
  }
  ```

---

### **3. Function Node (Extraer datos del remitente)**
- **Nodo**: *Function*
- **Código** (para parsear remitente, asunto, fecha, etc.):
  ```javascript
  const emailData = $input.all()[0].json;

  // Extraer datos del remitente
  const from = emailData.from;
  const senderName = from.split("<")[0].trim(); // Nombre del remitente
  const senderEmail = from.match(/<([^>]+)>/)[1]; // Email del remitente

  // Datos del email
  const subject = emailData.subject;
  const date = emailData.date;
  const body = emailData.text || emailData.html; // Texto plano o HTML

  // Retornar datos estructurados para Notion
  return [{
    json: {
      "Nombre": senderName,
      "Email": senderEmail,
      "Asunto": subject,
      "Fecha": date,
      "Contenido": body,
    }
  }];
  ```

---

### **4. Notion Node (Guardar en una base de datos)**
- **Nodo**: *Notion*
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Notion.
  - **Resource**: `Database Page`.
  - **Operation**: `Create Page`.
  - **Database ID**: ID de tu base de datos en Notion (ej: `https://www.notion.so/workspace/1234567890abcdef` → el ID es `1234567890abcdef`).
  - **Properties**:
    - Mapea los campos del JSON anterior a las propiedades de tu base de datos en Notion. Ejemplo:
      - `Nombre` → Propiedad "Nombre" (tipo: *Text*).
      - `Email` → Propiedad "Email" (tipo: *Email*).
      - `Asunto` → Propiedad "Asunto" (tipo: *Text*).
      - `Fecha` → Propiedad "Fecha" (tipo: *Date*).
      - `Contenido` → Propiedad "Contenido" (tipo: *Text* o *Rich Text*).

---

### **5. Slack Node (Notificación)**
- **Nodo**: *Slack*
- **Configuración**:
  - **Authentication**: Conecta tu cuenta de Slack (usando un *Webhook* o *OAuth*).
  - **Resource**: `Message`.
  - **Operation**: `Post Message`.
  - **Channel**: Canal donde quieres la notificación (ej: `#propuestas`).
  - **Text**:
    ```plaintext
    📩 *Nueva propuesta/cotización recibida* 📩
    *Remitente*: {{ $node["Function1"].json["Nombre"] }} ({{ $node["Function1"].json["Email"] }})
    *Asunto*: {{ $node["Function1"].json["Asunto"] }}
    *Fecha*: {{ $node["Function1"].json["Fecha"] }}
    ```
  - **Options**:
    - **Username**: `n8n Bot` (o el nombre que prefieras).
    - **Icon Emoji**: `:email:` (o el emoji que quieras).

---

### **6. (Opcional) Error Handling**
- **Nodo**: *IF* (para manejar errores)
  - Si algún nodo falla (ej: Notion no responde), puedes enviar un mensaje de error a Slack o a tu email.

---

### **Diagrama del Workflow**
```plaintext
Gmail Trigger → Function (Filtrar) → Function (Extraer datos) → Notion → Slack
```

---

### **Notas importantes**:
1. **Permisos**:
   - Asegúrate de que el *Google OAuth* tenga acceso a Gmail.
   - En Notion, comparte la base de datos con el *integration* de n8n (crea un *integration* en [Notion Developers](https://www.notion.so/my-integrations)).
   - En Slack, crea un *Webhook* o usa OAuth para enviar mensajes.

2. **Pruebas**:
   - Usa el modo *Test* en n8n para probar cada nodo con un email de ejemplo.
   - Verifica que los datos se guarden correctamente en Notion y que la notificación llegue a Slack.

3. **Optimización**:
   - Si recibes muchos emails, ajusta el *Polling Interval* en el Gmail Trigger para evitar saturación.
   - Si el cuerpo del email es HTML, puedes usar un nodo *HTML Extract* para limpiar el texto.

---

### **Ejemplo de salida en Notion**:
| Nombre       | Email               | Asunto                     | Fecha       | Contenido          |
|--------------|---------------------|----------------------------|-------------|--------------------|
| Juan Pérez   | juan@ejemplo.com    | Propuesta de servicio      | 2023-10-01  | Hola, adjunto...   |

---

¿Necesitas ayuda con algún paso en específico? Por ejemplo:
- ¿Cómo configurar el *integration* en Notion?
- ¿Cómo crear el *Webhook* en Slack?
- ¿Cómo depurar si algo no funciona?