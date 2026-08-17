# GPT-OSS 20B — multi_turn/requirements_change

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.07 | quality: 4.0
- latency_total: 14.351s | tokens_per_second: 137.3
- input_tokens: 277 | output_tokens: 1970
- judge_score: 4.0 | justificación: La respuesta es precisa y clara, proporcionando un workflow detallado y útil, aunque no sigue exactamente los requisitos iniciales de guardar datos en Google Sheets, sino en Notion, lo que afecta la relevancia y coherencia contextual.

## Respuesta completa

¡Claro! Vamos a armar un workflow en **n8n** que:

1. **Escuche** correos entrantes en Gmail.  
2. **Filtre** solo los con “propuesta” o “cotización” en el asunto.  
3. **Extraiga** datos del remitente (nombre y email).  
4. **Guarde** esos datos en una base de datos de **Notion**.  
5. **Notifique** a un canal de **Slack** cada vez que se procese un correo válido.

A continuación tienes los pasos con la configuración exacta de cada nodo y el código que necesitarás.

---

## 1. Requisitos previos

| Recurso | Qué necesitas | Cómo conseguirlo |
|---------|---------------|------------------|
| **Gmail** | Credenciales OAuth 2.0 (client id/secret) | Sigue la guía de n8n para la integración de Gmail. |
| **Notion** | API token y ID de la base de datos | Crea una integración en Notion y copia el token. Obtén el ID de la base de datos en la URL (`/database/<ID>`). |
| **Slack** | Webhook o App con permiso `chat:write` | Ve a *Apps > Manage > Create New App* y añade un webhook, o usa un app con OAuth. |

> **Tip**: Si ya tienes los credenciales en tu instancia de n8n, ve directamente a “Credentials” > “Add New” y crea cada uno.

---

## 2. Estructura del workflow

```
Gmail Trigger → Filter → Function (parse sender) → Notion → Slack
```

### 2.1 Gmail Trigger

1. **Add node** → `Gmail Trigger`.  
2. **Authentication**: Selecciona la credencial que creaste.  
3. **Trigger**:  
   - `Trigger on new message`.  
4. **Query**: En la sección *“Search query”* escribe:  

   ```
   subject:propuesta OR subject:cotizacion
   ```

   > Esto garantiza que el trigger solo se active cuando el asunto contenga *propuesta* o *cotización* (mayúsculas/minúsculas no importan).  

5. **Options**: Opcionalmente, activa *“Include Email Body”* si quieres usar el cuerpo en la Notion más adelante.

### 2.2 Filter Node

Aunque el trigger ya filtra por asunto, es una buena práctica usar un `IF` node para asegurarnos y añadir lógica adicional si lo necesitas.

1. **Add node** → `IF`.  
2. **Conditions** → `{{$json["subject"]}}` contains `propuesta` **OR** `{{$json["subject"]}}` contains `cotizacion`.  
3. **Connect**: `Gmail Trigger` → `IF`.  
4. **Create two outputs**: *Yes* → continue, *No* → terminate (no acción).

### 2.3 Function Node – “Parse Sender”

Este nodo extrae y limpia el nombre y el email del remitente.

1. **Add node** → `Function`.  
2. **Code** (copy & paste):

   ```javascript
   // Gmail gives the sender as "Name <email@domain.com>"
   const rawSender = $json["from"]; // e.g. "Juan Pérez <juan.perez@example.com>"

   // Regex to capture name and email
   const regex = /^(.*) <(.+)>$/;
   const match = rawSender.match(regex);

   let senderName = "";
   let senderEmail = "";

   if (match) {
     senderName = match[1].trim();
     senderEmail = match[2].trim();
   } else {
     // Fallback if format is just an email
     senderEmail = rawSender.trim();
   }

   return {
     name: senderName,
     email: senderEmail,
     subject: $json["subject"],
     date: $json["internalDate"], // or $json["date"] if you prefer
   };
   ```

3. **Output**: Este nodo devuelve un objeto con `name`, `email`, `subject`, `date`.  
4. **Connect**: `IF → Yes` → `Function`.

### 2.4 Notion Node – “Create Page”

1. **Add node** → `Notion`.  
2. **Operation**: `Create`.  
3. **Database ID**: Pega el ID de tu base de datos de Notion.  
4. **Properties**: Asigna cada campo a la propiedad correspondiente en Notion. Ejemplo:

   | n8n field | Notion property | Type |
   |-----------|-----------------|------|
   | `name` | `Remitente` | Text |
   | `email` | `Email` | Email |
   | `subject` | `Asunto` | Text |
   | `date` | `Fecha` | Date |

   > Asegúrate de que los nombres de las propiedades coincidan exactamente con los de Notion.

5. **Connect**: `Function` → `Notion`.

### 2.5 Slack Node – “Send Message”

1. **Add node** → `Slack`.  
2. **Operation**: `Send Message`.  
3. **Authentication**: Selecciona tu credencial de Slack.  
4. **Channel**: Elige el canal o ID donde quieres recibir la notificación.  
5. **Message**: Puedes usar datos del correo:

   ```txt
   📧 Nuevo email recibido de {{$node["Parse Sender"].json["name"]}} ({{$node["Parse Sender"].json["email"]}})
   Asunto: {{$node["Parse Sender"].json["subject"]}}
   ```

6. **Connect**: `Notion` → `Slack`.

---

## 3. Conexiones finales

```
[Gmail Trigger] --(trigger)--> [IF]
[IF Yes] --(yes)--> [Function (Parse Sender)]
[Function] --(output)--> [Notion]
[Notion] --(success)--> [Slack]
```

> Si prefieres que la notificación Slack se envíe **antes** de crear la página de Notion, basta con intercambiar la posición de los nodos `Notion` y `Slack`.

---

## 4. Pruebas y puesta en marcha

1. **Activar el workflow**: Asegúrate de que esté en “Active”.  
2. **Enviar un email de prueba**: Con asunto `propuesta` o `cotización`.  
3. **Verifica**:  
   - La fila aparece en tu base de datos de Notion.  
   - Se recibe el mensaje en Slack.  
4. **Logs**: Usa el nodo `Set` o `Code` si necesitas depurar.  
5. **Monitorear**: En la pestaña *“Execution Log”* de n8n puedes ver cada paso y los datos que pasan.

---

## 5. Tips de optimización

| Situación | Solución |
|-----------|----------|
| **Correo sin nombre** | El regex devuelve solo email; la propiedad “Remitente” quedará vacía. |
| **Asunto con espacios extra** | Puedes usar `{{$json["subject"]}}.trim()` antes de evaluar el filtro. |
| **Fecha en formato legible** | Si prefieres una fecha más amigable, en el Function node añade:

   ```javascript
   const date = new Date(parseInt($json["internalDate"]));
   return { ... , formattedDate: date.toISOString() };
   ```

   Y usa `formattedDate` en Notion. |
| **Múltiples correos en una ejecución** | Si usas “Trigger” con “Batch”, tendrás un array de emails. Necesitarás un `SplitInBatches` node antes de `IF`. |

---

## 6. Resumen rápido

- **Trigger**: Gmail con query `subject:propuesta OR subject:cotizacion`.  
- **Filtro**: IF node para seguridad adicional.  
- **Parser**: Function node que devuelve `{name, email, subject, date}`.  
- **Almacenamiento**: Notion Create Page con las propiedades adecuadas.  
- **Notificación**: Slack message con la información extraída.  

¡Listo! Con este workflow tendrás los datos de los correos filtrados directamente en Notion y una alerta en Slack cada vez que algo nuevo llegue. Si necesitas ajustar campos adicionales o cambiar la lógica de filtrado, solo edita los nodos correspondientes. 🚀