# Nemotron 3 Nano 30B — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 4.85 | quality: 4.0
- latency_total: 20.542s | tokens_per_second: 96.1
- input_tokens: 248 | output_tokens: 1974

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


### Workflow propuesto en N8N  
A continuación tienes el esquema completo del workflow que cumple con los nuevos requisitos:

| Paso | Nodo N8N | Qué hace | Configuración clave |
|------|----------|----------|----------------------|
| 1️⃣ | **Gmail Trigger** | Se ejecuta cada vez que llega un nuevo mensaje a tu bandeja. | • **Label**: elige la etiqueta que usas para los correos que quieres procesar (o deja vacío para “todas”). <br>• **Search Query**: `subject:(propuesta OR cotizacion)` – filtra por asunto. |
| 2️⃣ | **Function** (opcional) | Extrae los datos del remitente y del asunto que te interesan. | ```js\nconst mail = $json;\nreturn {\n  senderName: mail.from.name || \"\",\n  senderEmail: mail.from.email,\n  subject: mail.subject,\n  date: mail.date,\n  messageId: mail.id   // lo usamos para evitar duplicados\n};\n``` |
| 3️⃣ | **Notion** → *Create Page* | Crea una nueva página en la base de datos que elijas (ej. “Propuestas y Cotizaciones”). | • **Database ID**: el ID de la tabla donde guardas los registros. <br>• **Properties**: mapea los campos que extrajiste. Ejemplo: <br> - **Name** (título) → `subject` <br> - **Created by** → `senderName` <br> - **Email** → `senderEmail` <br> - **Date** → `date` <br> - **Message ID** → `messageId` (útil para evitar duplicados). |
| 4️⃣ | **Slack** → *Send Channel Message* | Envía una notificación a Slack cuando se crea la página en Notion. | • **Channel**: el canal donde quieres el aviso. <br>• **Message Text**: algo como `📬 Nueva propuesta/cotización recibida:\n*Asunto*: ${subject}\n*De*: ${senderName} <${senderEmail}>\n*Fecha*: ${date}` <br>• **Attachments** (opcional) para incluir enlaces o botones. |
| 5️⃣ | **IF** (opcional) | Evita procesar el mismo correo varias veces. | Usa el campo `messageId` y verifica si ya existe en una colección (por ejemplo, usando el nodo **Set** + **Collection** o **Database** de N8N). Si ya está, termina el flujo; si no, continúa. |

---

## Paso a paso en la UI de N8N

1. **Arrastra el nodo `Gmail Trigger`**  
   - **Credentials**: conecta tu cuenta de Gmail (OAuth2).  
   - En **Search Query** escribe:  
     ```
     subject:(propuesta OR cotizacion)
     ```  
   - Marca **Only New Mails** si deseas que el trigger solo dispare cuando haya correos aún no leídos.

2. **Añade un nodo `Function`** (llámalo “Parse Mail”)  
   - Copia el código del paso 2️⃣ arriba.  
   - Conecta la salida del trigger a este nodo.

3. **Conecta el nodo `Function` a `Notion → Create Page`**  
   - En **Credentials** pon tu token de Notion y selecciona la base de datos donde guardarás los registros.  
   - En **Properties**, asigna cada campo del JSON a la propiedad correspondiente de la tabla.  
   - Ejemplo de mapeo:  
     - **Name** → `subject`  
     - **Created by** → `senderName`  
     - **Email** → `senderEmail`  
     - **Date** → `date`  
     - **Message ID** → `messageId` (puedes usar este campo para hacer un “check existence” más adelante).

4. **Añade un nodo `Slack → Send Channel Message`**  
   - Conecta tus credenciales de Slack.  
   - En **Channel** pon `#tu‑canal‑de‑notificaciones`.  
   - En **Message Text**, usa la expresión `${$json.subject}` y demás variables para personalizar el mensaje.  
   - Si quieres que el mensaje sea más visual, puedes usar **Attachments** o **Blocks**.

5. **(Opcional) Añade un nodo `IF`** antes de `Notion` para evitar duplicados  
   - **Condition**: `{{ $json.messageId !== $node["Collection"].items[0]?.messageId }}` (ajusta según cómo guardes los IDs).  
   - Si pasa, continúa al resto del flujo; si no, termina.

6. **Conecta todo** y guarda el workflow.  
   - Actívalo y verifica que los correos que llegan con “propuesta” o “cotizacion” en el asunto:  
     1. Se añadan como una nueva fila en Notion.  
     2. Se envíe la notificación a Slack.  

---

## Tips y Mejores Prácticas

| Tema | Recomendación |
|------|----------------|
| **Evitar duplicados** | Usa el `Message ID` de Gmail como clave única. Puedes crear una pequeña tabla en Notion o una colección en N8N que almacene los IDs procesados y revisarla antes de crear la página. |
| **Manejo de errores** | Añade un nodo `Error Trigger` o un `Try/Catch` dentro del `Function` para capturar fallos al parsear el mail y enviarlos a un canal de Slack de “Errores”. |
| **Formato de fechas** | Gmail devuelve la fecha en formato ISO 8601 (`2025-11-03T14:30:00.000Z`). Si quieres un formato más legible en Notion/Slack, usa `new Date($json.date).toLocaleString()` dentro del `Function`. |
| **Límites de API** | Tanto Notion como Slack tienen límites de rate‑limit. Si esperas muchos correos al día, agrega un pequeño **Delay** (ej. 1 segundo) entre pasos para no saturar las APIs. |
| **Seguridad** | Nunca expongas tus tokens de API en el workflow público; usa las **Credentials** de N8N y guarda los secretos en el gestor de credenciales de la plataforma. |

---

### Ejemplo visual del flujo (texto)

```
Gmail Trigger (subject:(propuesta OR cotizacion))
   └─► Function (parse sender, subject, date, messageId)
         └─► IF (messageId no está en colección)  ← opcional
               └─► Notion → Create Page (crea registro)
                     └─► Slack → Send Channel Message (notificación)
```

---

## ¿Qué necesitas ajustar?

1. **Base de datos de Notion** – Copia el ID de la tabla donde quieres guardar los datos.  
2. **Mapeo de propiedades** – Asegúrate de que los nombres de las columnas en Notion coincidan con los campos que envías.  
3. **Canal de Slack** – Define el nombre o ID del canal donde deseas recibir la alerta.  
4. **Filtrado de asunto** – Si en algún momento quieres ampliar la lista de palabras clave, solo modifica la expresión regular en el **Search Query** del nodo Gmail Trigger.

---

### Próximos pasos

- **Prueba el workflow** con un correo de prueba que tenga “propuesta” o “cotizacion” en el asunto.  
- Verifica en Notion que se haya creado la página con los datos correctos.  
- Revisa el canal de Slack para confirmar que llega la notificación.  
- Si todo está OK, activa el workflow y deja que se ejecute automáticamente.

---

¿Te gustaría que profundice en algún nodo en particular (por ejemplo, la configuración avanzada del nodo `Function` o el manejo de duplicados con una colección en Notion)? ¡Estoy aquí para ayudarte a afinar el detalle!