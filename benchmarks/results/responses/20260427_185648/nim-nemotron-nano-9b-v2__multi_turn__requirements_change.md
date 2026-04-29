# Nemotron Nano 9B v2 (NIM) — multi_turn/requirements_change

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 7.13 | quality: 8.36
- latency_total: 27.929s | tokens_per_second: 49.9
- input_tokens: 239 | output_tokens: 1394
- judge_score: 4.6 | justificación: 

## Respuesta completa



¡Claro! Aquí tienes el workflow actualizado con las nuevas necesidades:

---

### **Workflow en N8N (paso a paso):**

1. **Trigger: Gmail Trigger**  
   - Configura el trigger para que escuche las nuevas emails en tu cuenta de Gmail (puedes filtrar por carpetas, etiquetas o remitente si lo deseas).

2. **Filter Node (Filtrar por palabra clave en el asunto)**  
   - Usa un **Filter node** para verificar si el **asunto** de cada email contiene las palabras "propuesta" o "cotización".  
   - Ejemplo de condición:  
     ```javascript
     msg.body.subject.includes('propuesta') || msg.body.subject.includes('cotización')
     ```

3. **Extract Data Node (Extraer datos del remitente y otros campos)**  
   - Usa un **Function node** para obtener los datos relevantes:  
     - **Remitente**: `msg.sender.email` o `msg.sender.name`  
     - **Asunto**: `msg.body.subject`  
     - **Fecha**: `msg.body.date`  
     - (Opcional) Cuerpo del email si quieres guardarlo en Notion.  
   - Ejemplo de salida:  
     ```json
     {
       "remitente": "nombre@ejemplo.com",
       "asunto": "Propuesta de colaboración",
       "fecha": "2023-10-05",
       "cuerpo": "Detalles del email..."
     }
     ```

4. **Notion Node (Guardar en Notion)**  
   - Usa un **Notion node** (necesitarás la integración de Notion en N8N y un token de API).  
   - Configura una base de datos en Notion donde se guardarán los datos (ej: "Propuestas y Cotizaciones").  
   - Mapea los campos extraídos a las propiedades de la base (ej: `remitente`, `asunto`, `fecha`).  
   - Ejemplo de payload:  
     ```json
     {
       "properties": {
         "Remitente": { "title": [ { "name": "remitente" } ] },
         "Asunto": { "title": [ { "name": "asunto" } ] },
         "Fecha": { "date": { "start": "fecha" } }
       }
     }
     ```

5. **Slack Notification Node (Notificación en Slack)**  
   - Usa un **Webhook node** de Slack (necesitarás un webhook de tu canal de Slack).  
   - Envía un mensaje automático cuando un email filtrado sea guardado en Notion.  
   - Ejemplo de mensaje:  
     ```
     ¡Nuevo email filtrado!  
     Remitente: {{remitente}}  
     Asunto: {{asunto}}  
     Fecha: {{fecha}}
     ```

---

### **Detalles clave a configurar:**
- **Notion**:  
  - Instala la integración de Notion en N8N y configura tu token de API.  
  - Asegúrate de que la base de datos exista y los campos coincidan con los datos que envías.  
- **Slack**:  
  - Genera un webhook en Slack (en la configuración de tu canal).  
  - Personaliza el mensaje con los campos que desees mostrar.  

---

¿Quieres que te ayude a configurar cada nodo con más detalle (ej: código exacto para el Function node o cómo crear el webhook de Slack)?
