# Gemini 2.5 Flash Lite — multi_turn/requirements_change

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 7.73 | quality: 8.0
- latency_total: 7.864s | tokens_per_second: 260.4
- input_tokens: 202 | output_tokens: 2048
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en Google Sheets, sino que cambia a Notion sin justificación, afectando la relevancia y coherencia contextual.

## Respuesta completa

¡Excelente, podemos adaptar el workflow sin problema! Notion es una gran alternativa a Google Sheets para organizar información.

Aquí te presento el nuevo workflow con las modificaciones:

1.  **Trigger**: **Gmail Trigger** (se activa con cada email nuevo)
2.  **Filtro**: **IF Node** (para verificar si el asunto contiene "propuesta" o "cotización")
3.  **Extracción de Datos**: **Function Node** (para parsear el remitente, email, asunto, fecha y cuerpo del email)
4.  **Notificación a Slack**: **Slack Node** (para enviar un mensaje cuando un email cumpla el filtro)
5.  **Guardar en Notion**: **Notion Node** (para agregar una nueva página con los datos extraídos)

Ahora, vamos a detallar la configuración de cada nodo:

---

### **Paso 1: Gmail Trigger**

Este nodo será el punto de partida de tu workflow. Se activará cada vez que llegue un nuevo correo a tu bandeja de entrada de Gmail.

*   **Nombre del Nodo**: `Nuevo Email Gmail`
*   **Operación**: `Listen for new emails`
*   **Conexión a Gmail**: Necesitarás configurar una conexión a tu cuenta de Gmail. Sigue las instrucciones de n8n para autenticarte (generalmente implica autorizar el acceso a tu cuenta de Google).
*   **Opciones de Configuración**:
    *   **Folder**: Selecciona la carpeta donde quieres que n8n escanee los correos. Lo más común es `INBOX`.
    *   **Mark as read**: Puedes marcar esta opción si quieres que los correos leídos por n8n se marquen como leídos en Gmail.
    *   **Include raw email**: Generalmente no es necesario para este caso, a menos que necesites el contenido completo del email en formato crudo.
    *   **Limit**: Puedes establecer un límite de cuántos correos procesar en cada ejecución. Para empezar, puedes dejarlo en blanco o en un número pequeño (ej. 5) para probar.

---

### **Paso 2: IF Node (Filtro de Asunto)**

Este nodo evaluará el asunto de cada email entrante para ver si contiene las palabras clave que te interesan.

*   **Nombre del Nodo**: `Filtrar Asunto`
*   **Condición 1**:
    *   **Left Value**: Selecciona `Subject` (este será un campo que vendrá del nodo anterior, el Gmail Trigger).
    *   **Operator**: `Includes`
    *   **Right Value**: Escribe `propuesta` (asegúrate de que sea en minúsculas si quieres que el filtro sea sensible a mayúsculas/minúsculas, o puedes usar `Includes (case insensitive)`).
*   **Condición 2**:
    *   **Logic**: `OR`
    *   **Left Value**: Selecciona `Subject` (de nuevo, del nodo anterior).
    *   **Operator**: `Includes`
    *   **Right Value**: Escribe `cotización`
*   **Important**: Si quieres que el filtro de mayúsculas/minúsculas no importe, usa el operador `Includes (case insensitive)`.

Si el email cumple alguna de estas condiciones, el flujo continuará por la rama "True". Si no, se detendrá.

---

### **Paso 3: Function Node (Extracción de Datos)**

Este nodo es crucial para extraer la información que necesitas del email y prepararla para Notion.

*   **Nombre del Nodo**: `Extraer Datos Email`
*   **Code**: Aquí te dejo el código que puedes usar. Asegúrate de que los nombres de los campos de entrada coincidan con lo que el Gmail Trigger te devuelve.

```javascript
// Obtener los datos del correo del nodo anterior
const emailData = $json.binary.data; // O el nombre que tenga tu nodo de Gmail trigger

// Inicializar variables
let senderName = '';
let senderEmail = '';
let subject = '';
let date = '';
let body = '';

// Extraer información básica del correo
if (emailData && emailData.length > 0) {
    const firstEmail = emailData[0]; // Asumimos que solo procesamos un email a la vez

    // Asunto
    subject = firstEmail.subject || 'Sin asunto';

    // Fecha (formatear si es necesario)
    if (firstEmail.date) {
        date = new Date(firstEmail.date).toISOString(); // Formato ISO 8601
    } else {
        date = new Date().toISOString(); // Fecha actual si no se encuentra
    }

    // Cuerpo del email (intentar obtener el texto plano)
    if (firstEmail.body && firstEmail.body.text) {
        body = firstEmail.body.text;
    } else if (firstEmail.body && firstEmail.body.html) {
        // Si solo hay HTML, podrías intentar parsearlo o simplemente guardarlo tal cual
        // Para simplificar, aquí guardamos el HTML, pero podrías usar una librería para extraer texto
        body = firstEmail.body.html;
    } else {
        body = 'Sin cuerpo de email';
    }

    // Remitente (esto puede variar según cómo Gmail provea la información)
    // Generalmente, el "from" es un array de objetos o una cadena
    if (firstEmail.from && firstEmail.from.length > 0) {
        senderEmail = firstEmail.from[0].email || '';
        senderName = firstEmail.from[0].name || senderEmail; // Si no hay nombre, usar el email
    } else if (typeof firstEmail.from === 'string') {
        // A veces viene como cadena "Nombre <email@dominio.com>"
        const fromMatch = firstEmail.from.match(/^(.*)<(.*)>$/);
        if (fromMatch) {
            senderName = fromMatch[1].trim();
            senderEmail = fromMatch[2].trim();
        } else {
            senderEmail = firstEmail.from; // Asumimos que es solo el email
            senderName = senderEmail;
        }
    } else {
        senderName = 'Remitente desconocido';
        senderEmail = 'desconocido@ejemplo.com';
    }
}

// Devolver los datos en un formato que Notion pueda entender
return [
    {
        "Sender Name": senderName,
        "Sender Email": senderEmail,
        "Subject": subject,
        "Date": date,
        "Body Preview": body.substring(0, 500) + (body.length > 500 ? '...' : '') // Un resumen del cuerpo
    }
];
```

**Explicación del código:**

*   Accede a los datos del correo (`$json.binary.data`).
*   Extrae `subject`, `date`, `body`.
*   Intenta extraer `senderName` y `senderEmail` de la propiedad `from`. La lógica de extracción del remitente puede ser un poco compleja porque Gmail puede devolverla de varias maneras. He incluido una lógica básica para cubrir los casos más comunes.
*   Formatea la fecha a ISO 8601, que es un formato estándar y fácil de usar.
*   Crea un `Body Preview` para no guardar cuerpos de email excesivamente largos en Notion directamente.
*   Devuelve un array con un objeto que contiene los datos formateados.

---

### **Paso 4: Slack Node (Notificación)**

Este nodo se ejecutará solo si el email pasó el filtro del IF Node. Te enviará una notificación a tu canal de Slack.

*   **Nombre del Nodo**: `Notificar a Slack`
*   **Operación**: `Send Message`
*   **Conexión a Slack**: Necesitarás configurar una conexión a tu espacio de trabajo de Slack. Esto generalmente implica crear una integración (App) en Slack y obtener un token.
*   **Opciones de Configuración**:
    *   **Channel**: Selecciona el canal de Slack donde quieres recibir las notificaciones (ej. `#general`, `#notificaciones-workflow`).
    *   **Text**: Aquí puedes personalizar el mensaje. Usa las variables que vienen del nodo "Extraer Datos Email". Por ejemplo:
        ```
        Nuevo email de propuesta/cotización recibido:
        *Remitente:* {{1["Sender Name"]}} ({{1["Sender Email"]}})
        *Asunto:* {{1["Subject"]}}
        *Fecha:* {{1["Date"]}}
        ```
        (El `{{1[...]}}` se refiere a la salida del primer nodo anterior, que en este caso es el nodo "Extraer Datos Email").

---

### **Paso 5: Notion Node (Guardar en Base de Datos)**

Este nodo guardará los datos del email en una base de datos de Notion.

*   **Nombre del Nodo**: `Guardar en Notion`
*   **Operación**: `Add Page`
*   **Conexión a Notion**: Necesitarás configurar una conexión a tu cuenta de Notion. Deberás autorizar a n8n para acceder a tus bases de datos.
*   **Opciones de Configuración**:
    *