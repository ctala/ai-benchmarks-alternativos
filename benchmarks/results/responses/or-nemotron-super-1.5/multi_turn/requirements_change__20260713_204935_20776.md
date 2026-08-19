# Nemotron Super 49B v1.5 — multi_turn/requirements_change

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.0 | quality: 6.0
- latency_total: 29.764s | tokens_per_second: 49.2
- input_tokens: 252 | output_tokens: 1465
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que incorpora los nuevos requisitos de manera efectiva, ofreciendo utilidad práctica y manteniendo la coherencia contextual.

## Respuesta completa

Perfecto, aquí tienes el **workflow actualizado** con los nuevos requisitos:

---

### **Workflow en N8N:**
1. **Trigger: Gmail - Get New Emails**  
   - Configura el trigger para buscar nuevos correos (ej: cada 5 minutos).  
   - En "Filter", agrega una condición para que solo se activen correos con **'propuesta' o 'cotización'** en el asunto (usa `subject contains`).

2. **Function Node: Extraer y filtrar datos**  
   - **Objetivo**: Extraer los campos necesarios y aplicar el filtro de texto (por si el trigger no lo hace).  
   - **Código**:  
     ```javascript
     // Solo pasan los correos con las palabras clave en el asunto
     if (
       items[0].data.subject.toLowerCase().includes('propuesta') ||
       items[0].data.subject.toLowerCase().includes('cotizacion')
     ) {
       return items;
     } else {
       return [];
     }
     ```
   - **Datos extraidos**:  
     - `Nombre del remitente`: `items[0].data.from`  
     - `Email del remitente`: Extrae el email del campo `from` (parsearlo si es necesario).  
     - `Asunto`: `items[0].data.subject`  
     - `Fecha`: `items[0].data.date`

3. **Notion - Create Item**  
   - **Configuración**:  
     - Conecta tu cuenta de Notion.  
     - Selecciona la **base de datos** donde guardarás los datos.  
     - Mapea los campos:  
       - **Nombre del remitente** → Propiedad "Nombre" en Notion.  
       - **Email** → Propiedad "Email".  
       - **Asunto** → Propiedad "Asunto".  
       - **Fecha** → Propiedad "Fecha" (tipo fecha en Notion).  

4. **Slack - Send Message**  
   - **Configuración**:  
     - Conecta tu cuenta de Slack.  
     - Selecciona el canal o usuario donde enviar la notificación.  
     - Ejemplo de mensaje:  
       ```  
       Nuevo correo con "propuesta/cotización":  
       📧 **Asunto**: {{items(0).data.subject}}  
       📬 **Remitente**: {{items(0).data.from}}  
       ⏰ **Fecha**: {{items(0).data.date}}  
       ```  

---

### **Pasos adicionales**:
- **Autenticación**: Asegúrate de tener configuradas las credenciales para **Gmail**, **Notion** y **Slack** en N8N.  
- **Prueba**: Envía un correo de prueba con las palabras clave en el asunto y verifica que llegue a Notion y Slack.  
- **Manejo de errores**: Agrega un **Log Message** o **Error Handling** para depurar problemas.  

¿Necesitas ayuda con la configuración específica de algún nodo o con la estructura de la base de datos en Notion? 😊