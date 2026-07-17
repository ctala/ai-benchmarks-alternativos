# Nemotron 3 Super — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 5.35 | quality: 4.0
- latency_total: 0.926s | tokens_per_second: 2142.5
- input_tokens: 242 | output_tokens: 1984
- judge_score: 3.0 | justificación: 

## Respuesta completa



Aquí tienes el workflow actualizado según tus nuevos requisitos, optimizado para eficiencia y claridad. He incluido detalles críticos de configuración para cada nodo, considerando buenas prácticas de n8n (como evitar procesamiento innecesario y manejar formatos de datos correctamente).

---

### **Flujo de Trabajo Final**  
`Gmail Trigger → Filter (Asunto) → Function (Extraer datos) → Notion (Crear página) → Slack (Notificación)`

---

### **Configuración Paso a Paso**

#### **1. Gmail Trigger**  
- **Propósito**: Detectar correos nuevos entrantes.  
- **Configuración clave**:  
  - *Evento*: `Watch Emails` (se activa al llegar un nuevo correo).  
  - *Only Get Unread Emails*: **✅ Activado** (evita reprocesar correos ya vistos; marca como leído automáticamente tras el flujo si añades un nodo adicional opcional al final, pero por simplicidad asumimos que gestionas esto manualmente o con filtros de Gmail).  
  - *Labels*: Dejar vacío (para revisar bandeja de entrada principal) o especificar una etiqueta si usas filtrado previo en Gmail.  
  - *Intervalo de sondeo*: `5 minutos` (ajustable según urgencia; no uses menos de 1 min para evitar límites de API).  

> ⚠️ **Nota importante**: Si deseas marcar automáticamente los correos como "leídos" tras procesarlos, añade un nodo `Gmail` (acción `Modify Email`) al final del flujo con `Mark as Read: true`. Lo omito aquí por no haberlo solicitado, pero es recomendable para producción.

---

#### **2. Filter (Asunto)**  
- **Propósito**: Filtrar solo correos cuyo asunto contenga **"propuesta"** o **"cotizacion"** (case-insensitive).  
- **Configuración clave**:  
  - *Condición*: Usa una **expresión JS** en el campo `Filter`:  
    ```javascript
    $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion')
    ```  
  - *Por qué así*:  
    - `.toLowerCase()` garantiza que funcione sin importar mayúsculas/minúsculas (ej: "PROPUESTA", "CoTiZaCiOn").  
    - Evita usar nodos `IF` separados (más eficiente y menos nodos en el flujo).  
  - *Salida*: Solo continúa si la condición es `true`.

---

#### **3. Function (Extraer datos del remitente)**  
- **Propósito**: Parsear el campo `from` de Gmail (ej: `"Juan Pérez <juan@empresa.com>"`) en nombre y email separados, además de normalizar la fecha.  
- **Configuración clave**:  
  - *Código del nodo*:  
    ```javascript
    const from = $json.from; // Ej: "Juan Pérez <juan@empresa.com>"
    
    // Extraer email usando regex (maneja casos con o sin <>)
    const emailMatch = from.match(/<([^>]+)>/);
    let email = from;
    let name = from;
    
    if (emailMatch) {
      email = emailMatch[1]; // Contenido dentro de <>
      name = from.replace(/<[^>]+>/g, '').trim(); // Quita <> y espacios
    }
    
    // Si el nombre queda vacío (ej: "<juan@empresa.com>"), usar el email como nombre
    if (!name) name = email;
    
    // Normalizar fecha a ISO 8601 (requerido por Notion y consistente en zonas horarias)
    const receivedDate = new Date($json.date).toISOString();
    
    return [{
      json: {
        senderName: name,
        senderEmail: email,
        subject: $json.subject,
        receivedDate: receivedDate // Formato: "2024-06-15T10:30:00.000Z"
      }
    }];
    ```  
  - *Salida*: Un objeto JSON con `{ senderName, senderEmail, subject, receivedDate }`.

---

#### **4. Notion (Crear página en base de datos)**  
- **Propósito**: Guardar los datos extraídos como una nueva fila en tu base de datos de Notion.  
- **Configuración clave**:  
  - *Recurso*: `Database` → `Create Page`.  
  - *Base de datos*: Selecciona tu DB previamente creada en Notion (debe tener estas propiedades):  
    - `Nombre Remitente` (tipo **Título** o **Texto**)  
    - `Email Remitente` (tipo **Email** o **Texto**)  
    - `Asunto` (tipo **Texto**)  
    - `Fecha Recepción` (tipo **Fecha** → formato *ISO 8601*).  
  - *Mapeo de campos*:  
    | Propiedad en Notion | Valor desde nodo Function |  
    |---------------------|---------------------------|  
    | Nombre Remitente    | `{{ $json.senderName }}`  |  
    | Email Remitente     | `{{ $json.senderEmail }}` |  
    | Asunto              | `{{ $json.subject }}`     |  
    | Fecha Recepción     | `{{ $json.receivedDate }}`|  
  - *Opcional*: Activa `Ignore Errors` si quieres que el flujo continúe aunque falle Notion (pero revisa logs para depurar).

---

#### **5. Slack (Notificación)**  
- **Propósito**: Enviar alerta a un canal/usuario de Slack cuando se procesa un correo filtrado.  
- **Configuración clave**:  
  - *Recurso*: `Slack` → `Send Message`.  
  - *Canal*: Especifica el nombre del canal (ej: `#notificaciones-propuestas`) o usuario (`@usuario`).  
  - *Texto del mensaje*: Usa esta plantilla para claridad:  
    ```text
    📧 *Nuevo correo de propuesta/cotización recibido*  
    • *De*: {{ $json.senderName }} <{{ $json.senderEmail }}>  
    • *Asunto*: {{ $json.subject }}  
    • *Fecha*: {{ new Date($json.receivedDate).toLocaleString() }}  
    ✅ *Guardado en Notion: [Ver base de datos](https://www.notion.so/tu-db-link)*  
    ```  
    - *Notas*:  
      - `{{ $json.senderName }}` proviene directamente del nodo **Function** (n8n mantiene acceso a nodos previos por nombre).  
      - `toLocaleString()` convierte la fecha ISO a formato legible según tu zona horaria local (ej: "15/06/2024, 10:30:00").  
      - El enlace a Notion es opcional; reemplázalo con tu URL real si quieres acceso directo.  
  - *Opcional*: Añade emojis o formato *Slack mrkdwn* para destacar el mensaje (como en el ejemplo arriba).

---

### **Esquema Visual del Flujo**  
```
[Gmail Trigger]  
        ↓  
[Filter: Asunto incluye "propuesta" O "cotizacion"]  
        ↓  
[Function: Parsear remitente + normalizar fecha]  
        ↓  
[Notion: Crear página en DB]  
        ↓  
[Slack: Enviar notificación formateada]  
```

---

### **Recomendaciones Críticas para Producción**  
1. **Credenciales**: Asegúrate de tener configuradas en n8n:  
   - Gmail (con permisos `https://mail.google.com/`).  
   - Notion (token de integración con acceso a tu DB).  
   - Slack (token de bot con permiso `chat:write` en el canal objetivo).  
2. **Manejo de errores**:  
   - Añade un nodo `Error Trigger` al final para notificar fallos (ej: si Notion falla, avisa por Slack separado).  
   - Usa `Execute Workflow` para reintentar flujos fallidos (n8n Enterprise) o revisa los *Execution Logs*.  
3. **Optimización**:  
   - Si recibes muchos correos, aumenta el intervalo del Gmail Trigger a 10-15 min para evitar límites de API.  
   - En Notion, usa una DB con propiedades indexadas (ej: `Fecha Recepción`) para búsquedas rápidas.  

Este flujo cumple exactamente con tus requisitos: filtrado preciso, extracción robusta de datos, integración limpia con Notion y notificación accionable en Slack. ¿Necesitas ayuda para crear la base de datos en Notion o ajustar algún nodo específico? 😊