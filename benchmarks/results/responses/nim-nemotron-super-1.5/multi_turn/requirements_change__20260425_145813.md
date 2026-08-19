# Nemotron Super 49B v1.5 (NIM) — multi_turn/requirements_change

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.43 | quality: 7.52
- latency_total: 84.753s | tokens_per_second: 22.5
- input_tokens: 249 | output_tokens: 1909
- judge_score: 4.0 | justificación: 

## Respuesta completa

Perfecto, te guiaré paso a paso para crear este workflow en n8N con las nuevas condiciones:

### **1. Configurar el Trigger (Gmail)**
- **Node:** `Gmail - Get New Emails`  
  - **Configuración:**  
    - **Only Trigger Once For Each Email:** Activar.  
    - **Filter:** Dejar vacío (filtraremos después con un nodo aparte).  
    - **Actions:** Seleccionar "Fetch all emails (including attachments)".  
    - **Polling Interval:** Ej: "Every 5 minutes" (ajusta según tus necesidades).

---

### **2. Filtrar Emails con "propuesta" o "cotización"**
- **Node:** `Filter`  
  - **Condition:**  
    - Usa una **expression** para verificar si el asunto contiene las palabras clave:  
      ```  
      {{ $json["subject"].toLowerCase().includes("propuesta") || $json["subject"].toLowerCase().includes("cotizacion") }}  
      ```  
    - Esto asegura que sea insensible a mayúsculas/minúsculas.

---

### **3. Extraer Datos Relevantes**
- **Node:** `Function`  
  - **Código JavaScript:**  
    ```javascript  
    return [  
      $input.item().json({  
        remitente_nombre: $input.item().json("from")?.name || "",  
        remitente_email: $input.item().json("from")?.address || "",  
        asunto: $input.item().json("subject"),  
        fecha: $input.item().json("date")  
      })  
    ];  
    ```  
  - Esto extrae los datos del remitente, asunto y fecha.

---

### **4. Enviar Datos a Notion**
- **Node:** `Notion - Create Database Page`  
  - **Configuración previa en Notion:**  
    1. Crea una base de datos vacía.  
    2. Agrega propiedades (columnas) para:  
       - **Nombre del remitente** (Tipo: Texto).  
       - **Email del remitente** (Tipo: Texto).  
       - **Asunto** (Tipo: Texto).  
       - **Fecha** (Tipo: Fecha).  
  - **En n8N:**  
    - **Database ID:** Copia el ID de tu base de datos de Notion (está en la URL de la base: `https://www.notion.so/<ID_BASE_DE_DATOS>/...`).  
    - **Page Properties:** Mapea los campos:  
      ```  
      {  
        "Nombre del remitente": "={{ $json.remitente_nombre }}",  
        "Email del remitente": "={{ $json.remitente_email }}",  
        "Asunto": "={{ $json.asunto }}",  
        "Fecha": [  
          {  
            "date": {  
              "start": "={{ new Date($json.fecha).toISOString() }}",  
              "end": "={{ new Date($json.fecha).toISOString() }}"  
            }  
          }  
        ]  
      }  
      ```  

---

### **5. Notificación en Slack**
- **Node:** `Slack - Send Message`  
  - **Configuración:**  
    - **Channel:** Selecciona el canal de Slack (ej: `#notificaciones`).  
    - **Text:** Personaliza el mensaje usando expresiones:  
      ```  
      Nuevo email que menciona "propuesta" o "cotización":  
      📧 **Asunto:** {{ $json.asunto }}  
      📄 **Remitente:** {{ $json.remitente_nombre }} ({{ $json.remitente_email }})  
      ⏰ **Fecha:** {{ new Date($json.fecha).toLocaleString() }}  
      ```  
  - **Auth:** Asegúrate de tener el webhook de Slack configurado en n8N.

---

### **Conexión Final**
- Conecta los nodos en este orden:  
  `Gmail` → `Filter` → `Function` → `Notion` + `Slack` (ambos en paralelo o en secuencia).

---

### **Pruebas y Ajustes**
1. **Prueba el workflow** enviando un email con "propuesta" o "cotización" en el asunto.  
2. Verifica que los datos llegan a Notion y aparece la notificación en Slack.  
3. Ajusta las expresiones si es necesario (ej: formatos de fecha).

¿Necesitas ayuda con la configuración de autenticación para Gmail, Notion o Slack en n8N? 😊