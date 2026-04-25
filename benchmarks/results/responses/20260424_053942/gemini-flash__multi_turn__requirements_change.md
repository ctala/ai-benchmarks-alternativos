# Gemini 2.5 Flash — multi_turn/requirements_change

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 5.56 | quality: 4.16
- latency_total: 11.89s | tokens_per_second: 171.7
- input_tokens: 206 | output_tokens: 2042
- judge_score: 1.6 | justificación: 

## Respuesta completa

¡Excelente! Ese cambio a Notion y la adición de filtros y notificaciones hacen que el workflow sea mucho más potente y útil.

Aquí te detallo el workflow actualizado con Notion, el filtro por asunto y la notificación a Slack:

---

**Workflow en n8n: Gmail -> Filtro por Asunto -> Extraer Datos -> Notion -> Slack**

**Objetivo:** Leer emails de Gmail, filtrar por palabras clave en el asunto ('propuesta' o 'cotizacion'), extraer datos del remitente, asunto y fecha, guardar estos datos en una base de datos de Notion y enviar una notificación a Slack.

---

### Nodos del Workflow:

1.  **Gmail Trigger (Webhook)**
2.  **IF (Filtro por Asunto)**
3.  **Function (Procesar Email y Extraer Datos)**
4.  **Notion (Crear Elemento en Base de Datos)**
5.  **Slack (Enviar Mensaje)**

---

### Configuración Detallada de Cada Nodo:

#### 1. Gmail Trigger (Webhook)

*   **Propósito:** Escuchar nuevos emails en tu cuenta de Gmail.
*   **Configuración:**
    *   **Gmail Account:** Selecciona tu cuenta de Gmail configurada en n8n. Si no la tienes, deberás añadir una nueva credencial (OAuth2 es lo más común).
    *   **Resource:** `Message`
    *   **Events:** `New Message`
    *   **Mark as read when processed:** (Opcional, pero recomendado para evitar reprocesar emails) Marca esta opción si quieres que n8n marque el email como leído después de procesarlo.
    *   **Important:** Activa el "Webhook URL" y sigue las instrucciones para configurar el reenvío de emails en Gmail (o usa la opción de "Watch" si tu versión de n8n lo permite y está configurada para ello, aunque el Webhook es más directo para triggers).

#### 2. IF (Filtro por Asunto)

*   **Propósito:** Filtrar los emails basándose en palabras clave en el asunto.
*   **Configuración:**
    *   **Mode:** `Basic`
    *   **Value 1:** `{{ $json.subject }}` (Arrastra el campo `subject` desde la salida del nodo Gmail o escríbelo directamente).
    *   **Operation:** `Contains`
    *   **Value 2:** `propuesta`
    *   **Add Condition:** Haz clic en "Add Condition" para añadir una segunda condición.
    *   **Logic:** `OR` (Es crucial para que coincida con 'propuesta' O 'cotizacion').
    *   **Value 1 (segunda condición):** `{{ $json.subject }}`
    *   **Operation (segunda condición):** `Contains`
    *   **Value 2 (segunda condición):** `cotizacion`

    *Este nodo tendrá dos ramas de salida: "True" (si el asunto contiene 'propuesta' o 'cotizacion') y "False" (si no).*

#### 3. Function (Procesar Email y Extraer Datos) - **Conectado a la rama "True" del nodo IF**

*   **Propósito:** Extraer de forma estructurada el nombre del remitente, el email del remitente, el asunto y la fecha del email.
*   **Configuración:** Pega el siguiente código JavaScript:

    ```javascript
    const emails = [];

    for (const item of $input.json) {
        const fromHeader = item.from; // Ejemplo: "Nombre Remitente <email@dominio.com>"
        let senderName = '';
        let senderEmail = '';

        // Extraer nombre y email del remitente
        const emailMatch = fromHeader.match(/<(.*?)>/);
        if (emailMatch && emailMatch[1]) {
            senderEmail = emailMatch[1];
            const nameMatch = fromHeader.match(/(.*?) </);
            if (nameMatch && nameMatch[1]) {
                senderName = nameMatch[1].replace(/"/g, '').trim(); // Eliminar comillas y espacios
            } else {
                senderName = senderEmail; // Si no hay nombre explícito, usa el email
            }
        } else {
            senderEmail = fromHeader; // Si no hay formato <>, asume que todo es el email
            senderName = fromHeader;
        }

        emails.push({
            senderName: senderName,
            senderEmail: senderEmail,
            subject: item.subject,
            receivedDate: new Date(item.receivedDate).toISOString(), // Formato ISO para Notion
            messageId: item.id // ID único del email, útil para referencias
        });
    }

    return emails;
    ```
    *Este nodo tomará la salida del nodo IF (solo los emails filtrados) y generará un objeto JSON limpio con los campos `senderName`, `senderEmail`, `subject`, `receivedDate` y `messageId`.*

#### 4. Notion (Crear Elemento en Base de Datos)

*   **Propósito:** Guardar los datos extraídos en una base de datos de Notion.
*   **Configuración:**
    *   **Notion Account:** Selecciona o crea tu credencial de Notion. Necesitarás un "Internal Integration Token" de Notion y compartir tu base de datos con esa integración.
    *   **Resource:** `Database Item`
    *   **Operation:** `Create`
    *   **Database ID:** Aquí debes pegar el ID de tu base de datos de Notion. Para obtenerlo, abre tu base de datos en Notion en el navegador. La URL se verá algo así: `https://www.notion.so/<workspace_id>/<database_id>?v=...`. Copia el `<database_id>`.
    *   **Properties:** Aquí es donde mapeas los datos de n8n a las propiedades de tu base de datos de Notion. Asegúrate de que las propiedades en Notion tengan el tipo de dato correcto (Texto, Email, Fecha).

        *   **Name (Título de la página):** `{{ $json.subject }}` (o una combinación como `{{ $json.senderName }} - {{ $json.subject }}`)
        *   **Remitente (Texto/Email):** `{{ $json.senderName }}`
        *   **Email Remitente (Email):** `{{ $json.senderEmail }}`
        *   **Asunto (Texto):** `{{ $json.subject }}`
        *   **Fecha Recepción (Fecha):** `{{ $json.receivedDate }}`
        *   **ID Mensaje (Texto):** `{{ $json.messageId }}` (útil para tener un identificador único)

    *Asegúrate de que los nombres de las propiedades en n8n coincidan exactamente con los nombres de las columnas/propiedades en tu base de datos de Notion.*

#### 5. Slack (Enviar Mensaje)

*   **Propósito:** Enviar una notificación a un canal de Slack cuando se procesa un email filtrado.
*   **Configuración:**
    *   **Slack Account:** Selecciona o crea tu credencial de Slack (normalmente un Webhook URL).
    *   **Resource:** `Message`
    *   **Operation:** `Send`
    *   **Channel:** El nombre del canal de Slack al que quieres enviar la notificación (ej. `#notificaciones-propuestas`).
    *   **Text:** Aquí puedes construir un mensaje personalizado usando los datos extraídos.

        ```
        ¡Nueva {{ ($json.subject.includes('propuesta')) ? 'propuesta' : 'cotización' }} recibida! 🎉

        De: {{ $json.senderName }} <{{ $json.senderEmail }}>
        Asunto: {{ $json.subject }}
        Recibido el: {{ new Date($json.receivedDate).toLocaleString() }}
        ```
        *Este mensaje usará el operador ternario para indicar si es una "propuesta" o "cotización" y formateará la fecha para que sea más legible.*

---

### Pasos Adicionales y Consideraciones:

1.  **Crea tu base de datos en Notion:** Antes de configurar el nodo Notion, asegúrate de tener una base de datos creada en Notion con las propiedades (columnas) que vas a usar:
    *   `Name` (Título, requerido por Notion)
    *   `Remitente` (Texto)
    *   `Email Remitente` (Email)
    *   `Asunto` (Texto)
    *   `Fecha Recepción` (Fecha)
    *   `ID Mensaje` (Texto)
2.  **Credenciales:** Configura tus credenciales de Gmail, Notion y Slack en n8n antes de empezar a construir el workflow.
3.  **Probar el Workflow:**
    *   Usa el botón "Execute Workflow" en n8n.
    *   Envía un email de prueba a tu cuenta de Gmail con "propuesta" o "cotizacion" en el asunto.
    *   Verifica la salida de cada nodo en n8n para asegurarte de que los datos se están procesando correctamente.
    *   Comprueba tu