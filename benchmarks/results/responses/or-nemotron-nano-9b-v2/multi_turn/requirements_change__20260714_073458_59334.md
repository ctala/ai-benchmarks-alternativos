# Nemotron Nano 9B v2 — multi_turn/requirements_change

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 6.22 | quality: 6.0
- latency_total: 37.827s | tokens_per_second: 32.3
- input_tokens: 239 | output_tokens: 1221
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando un flujo de trabajo detallado que incorpora los requisitos actualizados, con una utilidad práctica significativa para un emprendedor.

## Respuesta completa



¡Claro! Aquí tienes el workflow actualizado con tus requisitos:

---

### **1. Trigger: Gmail Trigger**
- Configura el trigger para leer nuevos correos.
- Asegúrate de tener la autenticación de Gmail habilitada (OAuth o API key).

---

### **2. Nodo de Extracción de Datos (Function Node)**
- **Propósito**: Extraer los campos necesarios:  
  - Remitente (`sender.name`, `sender.email`)  
  - Asunto (`subject`)  
  - Fecha (`date`)  
- **Código de ejemplo (JavaScript)**:
  ```javascript
  const data = {
    sender: msg.sender,
    subject: msg.subject,
    date: msg.date
  };
  return data;
  ```

---

### **3. Nodo de Filtro (Filter Node)**
- **Condición**:  
  - `subject` contiene **"propuesta"** O **"cotizacion"**  
  - Ejemplo de condición:  
    ```javascript
    msg.subject.toLowerCase().includes('propuesta') || msg.subject.toLowerCase().includes('cotizacion')
    ```

---

### **4. Nodo de Notion**
- **Propósito**: Guardar los datos filtrados en una página de Notion.
- **Configuración**:  
  - Integra Notion usando su API (necesitarás la clave de integración de Notion y el ID de la página o base donde guardarás los datos).  
  - Mapea los campos (`sender`, `subject`, `date`) a propiedades de Notion.  
- **API de Notion**: Usa la [API de Notion](https://developers.notion.com/) para crear entradas. Ejemplo de payload:
  ```json
  {
    "parent": { "database_id": "TU_ID_DE_BASE_DE_NOTION" },
    "properties": {
      "Remitente": { "title": [ { "text": { "content": msg.sender.name } } ] },
      "Asunto": { "title": [ { "text": { "content": msg.subject } } ] },
      "Fecha": { "date": { "start": msg.date } }
    }
  }
  ```

---

### **5. Notificación en Slack (Slack Webhook Node)**
- **Propósito**: Enviar una notificación cuando un correo cumple el filtro.  
- **Configuración**:  
  - Usa un webhook de Slack (genera uno en [Slack API](https://api.slack.com/messaging/webhooks)).  
  - Envía un mensaje con detalles del correo (ej: asunto, remitente).  
- **Ejemplo de payload**:
  ```json
  {
    "text": `Nuevo correo con "propuesta" o "cotizacion":  
    Asunto: ${msg.subject}  
    Remitente: ${msg.sender.name} (${msg.sender.email})`
  }
  ```

---

### ** Flujo Final:**
```
Gmail Trigger → Function Node (extracción) → Filter Node (propuesta/cotizacion) → Notion Node (guardar) → Slack Webhook (notificación)
```

---

### **Pasos a seguir en N8N:**
1. Instala los nodos necesarios:  
   - `Gmail`, `Function`, `Filter`, `Notion`, `Slack Webhook`.  
2. Configura las credenciales (API keys, OAuth tokens).  
3. Prueba el flujo con un correo de prueba.  

¿Necesitas ayuda con la configuración específica de algún nodo (ej: código de Notion o Slack)?
