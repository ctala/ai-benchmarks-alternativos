# Nemotron 3 Super — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.45 | quality: 8.72
- latency_total: 27.414s | tokens_per_second: 171.4
- input_tokens: 248 | output_tokens: 4699
- judge_score: 4.6 | justificación: 

## Respuesta completa



Aquí tienes el workflow actualizado en **n8n** que cumple con tus nuevos requisitos:  
**Lee Gmail → Filtra emails con "propuesta" o "cotizacion" en el asunto → Extrae datos del remitente → Guarda en Notion → Notifica en Slack**.  

---

### 🔧 **Workflow Paso a Paso**  
*(Asume que ya tienes credenciales configuradas para Gmail, Notion y Slack en n8n)*  

#### **1. Trigger: Gmail**  
- **Nodo**: `Gmail Trigger`  
- **Configuración**:  
  - **Event**: `New Email`  
  - **Label**: `INBOX` (por defecto, para bandejas de entrada)  
  - **Mark as Read**: `No` (opcional; déjalo en `No` si quieres que los emails queden como no leídos para revisarlos manualmente después)  
  - **Solo Emails No Vistos**: `Sí` (recomendado para evitar procesar emails antiguos en cada ejecución)  

> ⚠️ **Nota**: Si usas etiquetas específicas en Gmail (ej: `Propuestas`), cambia `Label` a esa etiqueta. De lo contrario, revisará toda la bandeja de entrada.

---

#### **2. Filtro: Solo emails con "propuesta" o "cotizacion" en el asunto**  
- **Nodo**: `Filter`  
- **Configuración**:  
  - **Condición 1**:  
    - **Field**: `Subject`  
    - **Operation**: `contains`  
    - **Value**: `propuesta`  
  - **Condición 2** (haz clic en `+ Add Condition`):  
    - **Field**: `Subject`  
    - **Operation**: `contains`  
    - **Value**: `cotizacion`  
    - **Relationship**: `OR` (esto es clave: el filtro pasará si **al menos una** de las condiciones es verdadera)  

> 💡 **¿Por qué no usar mayúsculas/minúsculas?**  
> El filtro `contains` en n8n es **case-sensitive**. Si quieres ignorar mayúsculas/minúsculas (ej: "PROPUESTA", "Propuesta"), reemplaza este nodo por un `Function` node con:  
> ```javascript
> const subject = $json.subject.toLowerCase();
> return subject.includes('propuesta') || subject.includes('cotizacion');
> ```  
> Pero para la mayoría de casos, el filtro anterior funciona si los emails usan minúsculas estándar.

---

#### **3. Extraer datos del remitente (nombre, email, asunto, fecha)**  
- **Nodo**: `Function`  
- **Código**:  
  ```javascript
  // Extraer nombre y email del campo "from" (formato: "Nombre <email@ejemplo.com>" o solo "email@ejemplo.com")
  const from = $json.from;
  let senderName = '';
  let senderEmail = '';

  const match = from.match(/^(.+?)\s*<(.+?)>$/);
  if (match) {
    senderName = match[1].trim(); // Nombre antes de < >
    senderEmail = match[2].trim(); // Email dentro de < >
  } else {
    senderEmail = from.trim(); // Si no hay < >, asumimos que es solo email
    // senderName queda vacío (se mostrará solo el email en Notion/Slack)
  }

  // Formatear fecha a ISO (compatible con Notion)
  const date = new Date($json.date);
  const formattedDate = date.toISOString();

  return [
    {
      senderName,
      senderEmail,
      subject: $json.subject,
      date: formattedDate, // Notion requiere formato ISO para propiedades de tipo "Fecha"
      // Puedes añadir más campos aquí si necesitas (ej: cuerpo del email: $json.body.plain)
    }
  ];
  ```
- **Salida**: Un JSON con `{ senderName, senderEmail, subject, date }` listo para usar en los siguientes nodos.

---

#### **4. Guardar en Notion**  
- **Nodo**: `Notion`  
- **Configuración**:  
  - **Resource**: `Page`  
  - **Operation**: `Create`  
  - **Database ID**: `[ID de tu base de datos en Notion]` (ej: `https://www.notion.so/mi-empresa/1a2b3c4d5e6f7g8h9i0j`)  
    - 🔍 **Cómo obtenerlo**: Abre tu base de datos en Notion → copia la parte larga del URL después de `/` y antes de `?v=` (ej: `1a2b3c4d5e6f7g8h9i0j`).  
  - **Propiedades a mapear** (ajusta según las columnas de tu DB):  
    | Propiedad en Notion | Valor desde n8n |  
    |---------------------|----------------|  
    | `Nombre Remitente` (texto) | `{{ $json.senderName }}` |  
    | `Email Remitente` (texto) | `{{ $json.senderEmail }}` |  
    | `Asunto` (texto) | `{{ $json.subject }}` |  
    | `Fecha` (fecha) | `{{ $json.date }}` |  

> ✅ **Requisito previo en Notion**:  
> Crea una base de datos con estas propiedades (tipo exacto):  
> - `Nombre Remitente`: `Texto`  
> - `Email Remitente`: `Texto`  
> - `Asunto`: `Texto`  
> - `Fecha`: `Fecha` (no "Fecha y hora" si solo necesitas día; pero ISO incluye hora, así que usa "Fecha y hora" si quieres precisión).  

---

#### **5. Notificar en Slack**  
- **Nodo**: `Slack`  
- **Configuración**:  
  - **Resource**: `Message`  
  - **Operation**: `Send`  
  - **Canal**: `#propuestas` (o el nombre de tu canal; ej: `@juan` para mensaje directo)  
  - **Texto**:  
    ```markdown
    :page_facing_up: *Nueva propuesta recibida*  
    • *Asunto*: {{ $json.subject }}  
    • *De*: {{ $json.senderName || $json.senderEmail }}  
    • *Fecha*: {{ new Date($json.date).toLocaleString() }}  
    ```  
    - 💡 **Notas**:  
      - `{{ $json.senderName || $json.senderEmail }}` muestra el nombre si existe, sino el email (evita campos vacíos).  
      - `toLocaleString()` formatea la fecha legiblemente (ej: `21/10/2023, 10:30:00`).  
      - Usa emojis (:page_facing_up:) para destacar el mensaje (opcional).  

---

### 📌 **Resumen del Flujo**  
`Gmail Trigger`  
 ↓  
`Filter` (asunto contiene "propuesta" **OR** "cotizacion")  
 ↓  
`Function` (extrae nombre/email + formatea fecha)  
 ↓  
`Notion` (crea fila en DB)  
 ↓  
`Slack` (envía notificación formateada)  

---

### ⚠️ **Checks Importantes Antes de Activar**  
1. **Credenciales**:  
   - Verifica que las credenciales de **Gmail**, **Notion** (token de integración con acceso a la DB) y **Slack** (bot token con `chat:write`) estén configuradas en n8n.  
2. **Base de datos en Notion**:  
   - Asegúrate de que las propiedades coincidan exactamente con lo mapeado en el nodo Notion (nombres y tipos).  
   - Prueba manualmente creando una entrada en Notion para confirmar que el formato de fecha ISO funciona.  
3. **Prueba el workflow**:  
   - Usa la opción `Execute Node` en cada paso para validar salidas (ej: después del `Function`, verifica que `senderName` y `date` tengan valores válidos).  
   - Envía un email de prueba a tu Gmail con asunto: `"Propuesta de servicios"` o `"Solicitud de cotización"` y revisa si aparece en Notion y Slack.  

---

### 🛠️ **Personalizaciones Adicionales (Opcional)**  
- **Ignorar emails tuyos**: Añade una condición en el `Filter` para excluir tu propio email (ej: `From` does not contain `tucorreo@empresa.com`).  
- **Adjuntos**: Si necesitas procesar adjuntos, agrega un nodo `IF` después del `Function` para revisar `$json.attachments` y guardar archivos en Notion (como enlaces) o Google Drive.  
- **Historial**: Usa un nodo `Set` antes de Notion para agregar un campo `ProcesadoEn` con `{{ $now }}` para auditoría.  

¿Necesitas ayuda para ajustar algún paso específico (ej: formato de fecha, manejo de adjuntos, o credenciales)? ¡Avísame y te guío! 😊