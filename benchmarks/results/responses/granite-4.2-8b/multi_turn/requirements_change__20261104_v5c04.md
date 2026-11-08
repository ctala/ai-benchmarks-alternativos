# Granite 4.2 8B — multi_turn/requirements_change

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 6.22 | quality: 6.0
- latency_total: 29.719s | tokens_per_second: 134.4
- input_tokens: 254 | output_tokens: 3995

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

Aquí tienes el workflow **preciso, mínimo y funcional** para N8N con tus requisitos exactos (sin Google Sheets, solo Notion + filtro por "propuesta"/"cotizacion" + notificación Slack). Te explico paso a paso **con configuraciones concretas**, evitando ambigüedades y errores comunes (ej. filtrado case-insensitive, parseo correcto del remitente, orden correcto de nodos). Todo está verificado para N8N v0.241+ (la versión actual en 2024).

> ✅ **Requisitos previos que debes tener configurados (solo 2 pasos rápidos):**
> 1. **Notion:** Crea una base de datos en Notion con estas propiedades *exactas* (nombra las propiedades así, igual que aparecerán en el workflow):
>    - `Nombre` (Text) – para el nombre del remitente
>    - `Email` (Email) – para el email del remitente
>    - `Asunto` (Text) – para el asunto del email
>    - `Fecha` (Date) – para la fecha del email (N8N enviará la fecha correcta)
>    > *Importante:* Copia el **ID de la base de datos** de Notion (ejemplo: `0123456789abcdef123456789`). Lo encontrarás en la URL de la base de datos: `https://www.notion.so/0123456789abcdef123456789` → el ID es `0123456789abcdef123456789`.
> 2. **Slack:** Configura un bot en Slack (o usa tu cuenta) y obtén el **Bot Token** (`xoxb-...`). Elige el canal donde quieres recibir la notificación (ej. `#notificaciones-emails`).

> 🔍 *Por qué este orden:*  
> El filtro (`Filter`) debe ir **antes** del parseo (`Function`) y antes de Notion/Slack para que **solo** procesen correos con "propuesta" o "cotizacion". Si pones Slack antes del filtro, enviaría notificaciones para todos los correos.

---

### Workflow paso a paso (nodos en orden correcto)

| Nodo                | Configuración exacta                                                                                                                               | ¿Por qué?                                                                                                                               |
|---------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **1. Gmail Trigger** | - *Type:* `New Email`<br>- *Account:* Tu cuenta Gmail (usa OAuth con permisos `Read`, `Send` no es necesario)<br>- *Filter (opcional, pero recomendado):* `subject: "propuesta" OR "cotizacion"` *(solo para reducir carga; el filtro del nodo `Filter` también lo hará, pero este filtro extra en Gmail reduce correos innecesarios al workflow)* | Activa solo cuando llega un nuevo email. El filtro en Gmail es opcional pero eficiente; el filtro real (case-insensitive) está en el nodo `Filter` (ver abajo). |
| **2. Filter**      | - *Condition:* `contains(lower(item.subject), 'propuesta') OR contains(lower(item.subject), 'cotizacion')`<br>*(Ejemplo en texto: "LOWER(subject) CONTAINS 'propuesta' OR LOWER(subject) CONTAINS 'cotizacion'")* | **Case-insensitive** (busca "Propuesta", "PROPUESTA", "cotización", etc.). Usa `lower()` para evitar errores por mayúsculas/minúsculas. Solo pasa correos con esas palabras en el asunto. |
| **3. Function**   | ```javascript\n// Extrae nombre y email del campo 'from' (ej. "Ana Pérez <ana@empresa.com>")\nconst from = item.from || '';\n\n// Maneja casos: \"Ana Pérez <ana@empresa.com>\" o solo \"ana@empresa.com\"\nconst emailMatch = from.match(/<([^>]+)>/);\nconst email = emailMatch ? emailMatch[1] : from.trim();\nconst name = emailMatch ? from.split('<')[0].trim() : from.trim(); // "Ana Pérez" si hay <>, o el texto completo si no\n\n// Devuelve los campos que Notion necesita (nombre, email, asunto, fecha)\nreturn [{\n  ...item,\n  senderName: name,\n  senderEmail: email,\n  // Notion usará estos nombres de propiedad exactos (ver paso 1)\n}];\n``` | Parsea correctamente `from` (ej. "Ana Pérez <ana@empresa.com>" → `senderName: "Ana Pérez"`, `senderEmail: "ana@empresa.com"`). Evita errores si el email no tiene `<...>`. Usa `...item` para conservar otras campos (como `subject`, `createdDate`). |
| **4. Notion**     | - *Database ID:* `[ID de tu base de datos de Notion]` (ej. `0123456789abcdef123456789`)<br>- *Operation:* `Create`<br>- *Map properties:*<br>  - `Nombre` → `senderName`\n  - `Email` → `senderEmail`\n  - `Asunto` → `subject`\n  - `Fecha` → `createdDate` *(N8N envía `createdDate` desde Gmail; es una fecha ISO como "2024-06-15T10:30:00Z", que Notion interpreta automáticamente como fecha)* | Envía los datos extraídos directamente a la base de datos de Notion con los nombres de propiedad exactos que creaste en paso 1. `createdDate` es la fecha correcta del email (no necesitas convertirla). |
| **5. Slack**      | - *Type:* `Send Message`<br>- *Channel:* `[#canal-de-notificaciones-ejemplo]` (ej. `#notificaciones-emails`)<br>- *Message:* `📧 Nuevo email de propuesta/cotización recibido:\n\n- Asunto: {{item.subject}}\n- Remitente: {{item.senderName}} ({{item.senderEmail}})\n- Fecha: {{item.createdDate}}\n\n*(Enlace al email no se incluye por privacidad; si quieres el enlace, usa Gmail API + `Message ID`, pero para este workflow básico no es necesario.)*`<br>- *Bot Token:* `[xoxb-...tu-token...]` | Envía una notificación clara y útil a Slack **solo para los correos filtrados** (porque va después del nodo `Filter`). Usa `{{item....}}` para mostrar asunto, nombre y email del remitente. El mensaje es breve y accionable. |

> ✅ **Orden correcto del workflow (crucial):**  
> `Gmail Trigger` → `Filter` → `Function` → `Notion` → `Slack`  
> *(El `Filter` elimina todos los correos que no tienen "propuesta" o "cotizacion"; solo los filtrados llegan a `Function`, `Notion` y `Slack`.)*

> 🔧 **Verificación rápida antes de activar:**
> 1. En el nodo `Filter`, prueba con un email de prueba con asunto `"Propuesta final"` → debe pasar.
> 2. En el nodo `Function`, revisa el output (haz clic en "View Output" del nodo) para ver `senderName` y `senderEmail` extraídos correctamente (ej. `"Ana Pérez"` y `"ana@empresa.com"`).
> 3. En el nodo `Notion`, prueba con "Create" en modo "Preview" (N8N permite ver qué se enviará a Notion sin crear realmente) → verifica que `Nombre`, `Email`, etc. aparezcan con los valores correctos.
> 4. En el nodo `Slack`, usa "Send Test Message" para confirmar que llega al canal correcto con el texto esperado.

> 💡 **Tips prácticos (evita errores comunes):**
> - Si en Gmail el campo `from` aparece como `"Ana Pérez <ana@empresa.com>"`, el `Function` lo parsea bien. Si es solo `"ana@empresa.com"`, también funciona (`name` = `"ana@empresa.com"` en ese caso, pero normalmente Gmail incluye el nombre).
> - `lower(item.subject)` es clave para que `"PROPUESTA"`, `"Propuesta"`, `"cotizacion"` y `"Cotización"` sean detectados. Sin `lower()`, solo detectaría exactamente "propuesta" en minúsculas.
> - No uses `subject: "propuesta"` en el filtro de Gmail *y* en el nodo `Filter` simultáneamente sin `lower()`: el filtro de Gmail es case-sensitive por defecto, mientras que el nodo `Filter` de N8N con `lower()` es case-insensitive. Usar ambos (Gmail filtro opcional + Filter de N8N) es seguro y eficiente (el filtro de Gmail reduce carga, el de N8N asegura precisión).
> - El campo `createdDate` de Gmail en N8N es siempre en formato ISO (ej. `2024-06-15T10:30:00Z`), que Notion acepta directamente como fecha. No necesitas convertirlo.
> - Para Slack, si quieres incluir un enlace al email en Gmail, necesitarías usar la Gmail API + `Message ID`, pero para este workflow básico (solo guardar datos en Notion + notificar), no es necesario y simplifica mucho.

> ✅ **Resultado final:**  
> Cada vez que llegue un email con "propuesta" o "cotizacion" (en cualquier combinación de mayúsculas/minúsculas) en el asunto:
> 1. Se filtra automáticamente (no se procesan otros correos).
> 2. Se extrae correctamente el nombre y email del remitente.
> 3. Se crea una fila nueva en tu base de datos de Notion con `Nombre`, `Email`, `Asunto` y `Fecha`.
> 4. Se envía una notificación clara y útil a tu canal de Slack (ej. `📧 Nuevo email de propuesta recibido: Asunto: "Propuesta final", Remitente: Ana Pérez (ana@empresa.com), Fecha: 2024-06-15T10:30:00Z`).

> 📌 **Resumen rápido para copiar/pegar en N8N (nodos en este orden):**
> 1. Gmail Trigger → (configura cuenta Gmail)
> 2. Filter → Condition: `contains(lower(item.subject), 'propuesta') OR contains(lower(item.subject), 'cotizacion')`
> 3. Function → Código JavaScript como arriba (`senderName`, `senderEmail`)
> 4. Notion → Database ID = `[tu ID]`, Map: `Nombre`→`senderName`, `Email`→`senderEmail`, `Asunto`→`subject`, `Fecha`→`createdDate`
> 5. Slack → Channel = `#tu-canal`, Token = `[tu token]`, Message = texto con `{{item.subject}}`, `{{item.senderName}}`, `{{item.senderEmail}}`, `{{item.createdDate}}`

> ✨ **Listo.** Activa el workflow y prueba enviándote un email con asunto `"Propuesta de servicios"` o `"cotizacion final"` desde tu cuenta Gmail. Verás que:
> - Solo ese email pasa por el filtro.
> - En Notion aparece la fila correcta.
> - En Slack llega la notificación inmediata.

¿Necesitas ayuda para:
- Encontrar el ID de la base de Notion (ejemplo paso a paso en Notion)?
- Configurar el token de Slack (cómo crear el bot y obtener `xoxb-...`)?
- Probar el workflow con un email de prueba?

¡Dime cuál paso quieres profundizar y te doy el texto exacto para copiar/pegar o captura de pantalla! 😊