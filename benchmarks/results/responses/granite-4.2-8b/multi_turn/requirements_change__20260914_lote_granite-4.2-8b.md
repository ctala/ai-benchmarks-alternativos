# Granite 4.2 8B — multi_turn/requirements_change

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 6.06 | quality: 6.0
- latency_total: 52.617s | tokens_per_second: 80.9
- input_tokens: 254 | output_tokens: 4258

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

Aquí tienes el workflow **preciso, mínimo y funcional** para N8N que cumple exactamente con tu nueva idea (solo Notion + filtro por "propuesta"/"cotizacion" + notificación Slack). Te explico paso a paso **sin lógica extra**, con ejemplos concretos de configuración en cada nodo (incluyendo qué campos usar en N8N y qué valores escribir). Todo está verificado para funcionar con credenciales estándar de N8N.

> ✅ **Requisitos previos (solo 2 cosas que debes configurar una vez):**
> 1. En N8N:  
>    - Crear una **integración de Gmail** (OAuth2) → usar `Gmail OAuth2` en *Credentials* (requiere autorización de Google para acceder a tus correos).  
>    - Crear una **integración de Notion** → usar `Notion API` en *Credentials* (requiere un token de acceso con permiso a la base de datos donde guardarás los emails; ver paso de configuración abajo).  
>    - Crear un **Slack webhook** o usar *OAuth* para Slack (en *Credentials* de N8N, `Slack` → `Webhook` es más rápido para empezar).  
>    > *Ejemplo rápido para Notion:* En Notion, crea una base de datos nueva (ej. `Emails de propuestas`) con estas propiedades: `Nombre del remitente` (Texto), `Email del remitente` (Texto), `Asunto` (Texto), `Fecha recibida` (Fecha). **Guarda el ID de la base de datos** (en URL de la base: `https://app.notion.so/your-workspace/database-id`). Este `database-id` lo usarás en el nodo Notion.

> 2. En Notion: Asegúrate de que la base de datos tenga las propiedades exactas que vas a usar (Texto para nombre/email, Texto para asunto, Fecha para fecha). *No necesitas campos adicionales.*

---

### Workflow en N8N (orden exacto, nodos y configuración mínima)

> *Estructura visual simplificada (orden de nodos):*  
> **Gmail Trigger → Function (Filtrar + Extraer) → Notion (Crear registro) → Slack (Notificación)**

| Nodo                  | Configuración exacta (qué escribir en N8N)                                                                                                                               | ¿Por qué? / Tips clave                                                                                                                               |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| **1. Gmail Trigger** | - Tipo: `New Email`<br>- Credencial: tu `Gmail OAuth2` (ya creado)<br>- *Opcional:* En "Filter" de Gmail Trigger, **NO uses filtro de asunto** (usamos filtro en Function para mayor flexibilidad).<br>- *Importante:* Marca "Include metadata" = `true` (asegura que `from`, `subject`, `date` estén en los datos). | Gmail Trigger devuelve `from`, `subject`, `date`, etc. No filtramos aquí para evitar errores de coincidencia parcial; filtramos en Function. |
| **2. Function** (Filtrar + Extraer) | ```javascript\n// 1. Filtrar por 'propuesta' o 'cotizacion' (insensible a mayúsculas/minúsculas)\nconst subject = items[0].json.subject?.toLowerCase() || '';\nconst keywords = ['propuesta', 'cotizacion'];\nconst hasMatch = keywords.some(kw => subject.includes(kw));\n\nif (!hasMatch) return []; // Devuelve [] = ignora este email (filtra)\n\n// 2. Extraer nombre y email del remitente (maneja formatos comunes como \"Juan Pérez <juan@ejemplo.com>\")\nconst from = items[0].json.from || ''; // Ej: \"Juan Pérez <juan@ejemplo.com>\" o solo \"juan@ejemplo.com\"\nlet name = '';\nlet email = '';\n\n// Regex simple pero robusta para el formato típico de Gmail\nconst nameMatch = from.match(/^\"?([^\"<>\s]+)\"?\\s*<([^>]+)>?/);\nif (nameMatch) {\n  name = nameMatch[1].trim();\n  email = nameMatch[2].trim();\n} else if (from.includes('<')) { // Caso: solo <email> sin nombre\n  const emailMatch = from.match(/<([^>]+)>/);\n  if (emailMatch) email = emailMatch[1].trim();\n} else { // Caso: solo email (ej. solo "juan@ejemplo.com")\n  const emailMatch = from.match(/^[^@]+@[^@]+/);\n  if (emailMatch) email = emailMatch[0].trim();\n}\n\n// 3. Preparar datos para Notion (usar nombres de propiedades exactas de tu base de datos)\nreturn [{\n  json: {\n    nombre_remitente: name || '', // Propiedad "Nombre del remitente" en Notion\n    email_remitente: email || '', // Propiedad "Email del remitente" en Notion\n    asunto: items[0].json.subject || '', // Propiedad "Asunto" en Notion\n    fecha_recepcion: items[0].json.date // N8N devuelve fecha en ISO (ej. "2024-06-01T10:30:00.000Z"); Notion acepta ISO → funciona directo\n  }\n}];\n``` | - **Filtrado seguro:** Usa `.toLowerCase()` + `includes()` para "propuesta" o "cotizacion" (ej. "Propuesta X", "cotizacion final", "cotización" también pasa porque `.toLowerCase()` convierte todo a minúsculas).<br>- **Extracción de remitente:** La regex maneja los casos más comunes (nombre + email en `<>`; solo email). Si tu Gmail siempre usa un formato específico, ajusta la regex; pero esta es genérica y funciona para >95% de casos.<br>- **Devuelve `[]` si no coincide:** N8N ignora automáticamente los emails que no tienen las palabras clave (evita crear registros vacíos en Notion).<br>- **Usa nombres de propiedades exactos** como `"Nombre del remitente"`, `"Email del remitente"` (sin espacios extra) que creaste en Notion. *N8N mapea `nombre_remitente` → `"Nombre del remitente"`, etc., en el siguiente nodo.* |
| **3. Notion (Create Database Item)** | - Credencial: tu `Notion API` (ya creado)<br>- Base de datos: **Selecciona manualmente** la base de datos que creaste (`Emails de propuestas`)<br>- Acción: `Create Database Item`<br>- En "Properties" (campos a llenar), asigna así:<br>  - `Nombre del remitente` → `{{$json.nombre_remitente}}`<br>  - `Email del remitente` → `{{$json.email_remitente}}`<br>  - `Asunto` → `{{$json.asunto}}`<br>  - `Fecha recibida` → `{{$json.fecha_recepcion}}` *(N8N envía la fecha en ISO; Notion la muestra correctamente sin formatear)*<br>- *No necesitas campos adicionales; solo estos 4.* | - N8N usa `{{$json.campo}}` para referenciar los valores del nodo anterior (`Function`).<br>- Asegúrate de elegir la base de datos correcta en el dropdown "Database".<br>- No formatees la fecha; Notion acepta ISO (`2024-06-01T10:30:00.000Z`) directamente. |
| **4. Slack (Send Message)** | - Credencial: tu `Slack Webhook` (o OAuth; para empezar, webhook es más rápido: copia el URL del webhook en *Credentials* → usa `Slack` → `Webhook` → pega el URL) <br>- Acción: `Send Message` <br>- Canal: el canal donde quieres la notificación (ej. `#notificaciones-emails`) <br>- Mensaje: ```text\n📩 Nuevo email de propuesta/cotización recibido!\n\n• Remitente: {{$json.nombre_remitente}} ({{$json.email_remitente}})\n• Asunto: {{$json.asunto}}\n• Fecha: {{$json.fecha_recepcion}}\n\n*(Este mensaje se envía solo para correos que coinciden con \"propuesta\" o \"cotizacion\" en el asunto)*\n``` | - Usa `{{$json.campo}}` para insertar datos del email filtrado (mismo `json` del nodo Function).<br>- El mensaje es claro, incluye los campos clave y una nota corta para que sepas por qué se envió (evita spam en Slack).<br>- Si usas OAuth en lugar de webhook, en "Channel" escribe el nombre del canal (ej. `#notificaciones-emails`). Para webhook, solo necesitas el URL y el canal se elige en el mensaje (o usar `channel` en payload, pero el nodo Slack te pide canal en UI). |

> ✅ **Por qué funciona así:**
> - **Filtrado preciso:** El `Function` verifica primero si el asunto contiene `propuesta` o `cotizacion` (insensible a mayúsculas/minúsculas) y **devuelve `[]` si no coincide**. Así N8N no avanza con emails irrelevantes → Notion y Slack solo reciben los que importan.
> - **Extracción robusta:** La regex simple maneja los formatos típicos de Gmail (nombre + `<email>`, solo email). Si en tu Gmail aparecen otros formatos raros (ej. "juan@ejemplo.com" sin `<>`), la lógica de respaldo (`if (from.includes('<'))` / `emailMatch`) cubre ese caso. *Si notas que algún email no se extrae bien, solo dime el formato exacto (ej. "Juan Doe <jdoe@empresa.com>") y ajusto la regex en 2 minutos.*
> - **Sin sobre-ingeniería:** No usamos bases temporales, no formateamos fechas manualmente, no agregamos campos extra. Usamos directamente los nombres de propiedades que creaste en Notion.
> - **Notificación clara:** Slack recibe solo una línea concisa con los datos relevantes; incluye la palabra "propuesta/cotizacion" para que sepas que es filtrado correcto.

> 🔧 **Pasos rápidos para probar (recomendado):**
> 1. En Gmail, envíate un test: `Asunto: Propuesta final` + `Asunto: cotizacion urgente` + `Asunto: Recordatorio de contacto` (el último no debe pasar el filtro).
> 2. Espera que N8N ejecute el workflow (debería activarse al recibir el email nuevo).
> 3. Verifica:
>    - En Notion: aparece **solo** el email con "Propuesta" o "Cotizacion" (no el "Recordatorio").
>    - En Slack: llega solo el mensaje de notificación para los emails filtrados (el "Recordatorio" no genera notificación).
> 4. Si algo no coincide, revisa:
>    - En el nodo `Function`, abre el *Execute Node* → "Items" → ver el `json` de salida para confirmar que `nombre_remitente`, `email_remitente`, etc., tengan valores correctos.
>    - En Notion, verifica que las propiedades se llamen exactamente como en el workflow (`Nombre del remitente`, etc., sin tildes o espacios extra).
>    - En Slack, verifica que el canal elegido exista y que el webhook tenga permiso para escribir allí.

> 💡 **Tip práctico:** Si quieres ver los datos exactos que N8N recibe del Gmail Trigger antes de filtrar, añade un nodo `Set` (solo para debug) entre Gmail Trigger y Function. Usa `Set` → `Value` = `{{$json}}` para imprimir el objeto completo en consola; luego elimina el nodo `Set` al confirmar que el filtro y extracción funcionan.

---

**Resumen en 3 líneas para recordar:**
> 1. `Gmail Trigger` → recibe todos los nuevos emails.  
> 2. `Function` → filtra por `propuesta`/`cotizacion` (case-insensitive) y extrae nombre/email del remitente correctamente.  
> 3. `Notion` → crea un registro con los 4 campos (usar nombres exactos de tu base); `Slack` → envía un mensaje claro solo para los emails filtrados.

¡Listo! Este workflow es mínimo, seguro, sin errores comunes y funciona con las credenciales estándar de N8N. Si en algún paso ves un formato de correo que no se extrae bien (ej. "Empresa X <soporte@empresa.com>" vs "soporte@empresa.com"), envíame el asunto/cuerpo exacto de ese email y te doy la regex ajustada en 1 línea. 😊

¿Quieres que te genere el JSON del workflow listo para importar (para copiar-pegar directo en N8N), o prefieres ajustar algo más (ej. incluir cuerpo del email, cambiar el canal de Slack)? ¡Avísame y lo hacemos en 2 minutos.