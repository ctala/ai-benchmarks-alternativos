# DeepSeek V4 Flash 0731 — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 4.72 | quality: 4.0
- latency_total: 54.557s | tokens_per_second: 36.0
- input_tokens: 244 | output_tokens: 1965

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

Perfecto, el cambio es sencillo. Te detallo el workflow actualizado con los 5 nodos en secuencia. Lo bueno es que Slack y Notion pueden ejecutarse en paralelo después del filtro y la extracción.

Aquí tienes la configuración nodo por nodo:

---

### **Flujo completo:**
`Gmail Trigger` → `Filter` → `Function (Extraer)` → (se divide en dos) `Slack` + `Notion`

---

### **1. Nodo: Gmail Trigger**
- **Authentication**: OAuth2 (conecta tu cuenta de Gmail).
- **Event**: `Message received`.
- **Filter**: (Opcional) puedes dejarlo vacío, el filtro de asunto lo haremos en el siguiente nodo.

---

### **2. Nodo: Filter**
Este nodo se encarga de dejar pasar solo los emails que cumplan la condición.

- **Conditions**:
  - **Condition 1**: `{{ $json.subject }}` → **String** → **Contains** → `propuesta`
  - **Combine with**: `OR`
  - **Condition 2**: `{{ $json.subject }}` → **String** → **Contains** → `cotizacion`
- **Options**: Asegúrate de que el modo sea `Keep matches` (deja pasar los que cumplen).

---

### **3. Nodo: Function (Extraer datos)**
Aquí limpias y estructuras los datos. El código JavaScript es el siguiente:

```javascript
// El email de Gmail llega en formato "Nombre <email>"
const from = $json.from || '';
const subject = $json.subject || '';
const date = $json.date || new Date().toISOString();

// Extraer nombre y email del remitente
const match = from.match(/(.*)<(.*)>/);
const senderName = match ? match[1].trim() : from;
const senderEmail = match ? match[2].trim() : from;

// Devolver el objeto limpio
return [{
  json: {
    senderName,
    senderEmail,
    subject,
    date
  }
}];
```

---

### **4. Nodo: Slack**
Conecta este nodo directamente desde la salida del nodo **Function**.

- **Authentication**: Conecta tu app de Slack.
- **Operation**: `Send message to a channel`.
- **Channel**: `#propuestas` (o el canal que prefieras).
- **Message Text**:
```
📩 Nueva propuesta/cotización recibida:
• De: {{ $json.senderName }} ({{ $json.senderEmail }})
• Asunto: {{ $json.subject }}
• Fecha: {{ $json.date }}
```

---

### **5. Nodo: Notion**
Conecta este nodo **también** desde la salida del nodo **Function** (así se ejecuta en paralelo con Slack).

- **Authentication**: Conecta tu integración de Notion.
- **Operation**: `Create a page`.
- **Database ID**: Pega el ID de tu base de datos en Notion.
- **Title** (propiedad título): `{{ $json.subject }}`
- **Propiedades adicionales** (mapea según los campos de tu base de datos):
  - `Remitente`: `{{ $json.senderName }}`
  - `Email`: `{{ $json.senderEmail }}`
  - `Fecha`: `{{ $json.date }}`

---

### **Consejos finales:**
- **Prueba primero** con el nodo Function activado en modo "Manual" para ver si el parsing del remitente funciona bien con tus emails reales.
- **Manejo de errores**: Si Slack falla, Notion seguirá funcionando porque están en paralelo. Si quieres que ambos sean críticos, puedes añadir un nodo `Error Trigger` o usar `Stop and Error`.
- **Optimización**: Si recibes muchos emails, puedes activar la opción `Execute once per item` en Slack y Notion para que procesen cada email individualmente.

¿Necesitas ayuda con la conexión OAuth de Gmail o la integración de Notion?