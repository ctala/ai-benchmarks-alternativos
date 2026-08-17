# Qwen 3.5 397B (NIM) — multi_turn/requirements_change

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 6.05 | quality: 5.56
- latency_total: 58.484s | tokens_per_second: 19.3
- input_tokens: 234 | output_tokens: 1128
- judge_score: 2.6 | justificación: 

## Respuesta completa

¡Entendido! Ese es un cambio muy común y potente para automatizar la captación de clientes o proveedores. Al cambiar a **Notion** y añadir **filtros** y **Slack**, el workflow se vuelve mucho más inteligente.

Aquí tienes la estructura lógica del workflow en N8N y los detalles de configuración para cada nodo:

### Estructura del Workflow

1.  **Trigger (Gmail):** Escucha nuevos correos.
2.  **Filtro (IF/Switch):** Revisa si el "Asunto" contiene "propuesta" O "cotización" (case-insensitive).
3.  **Acción 1 (Notion):** Crea una nueva página en tu base de datos con los datos del correo.
4.  **Acción 2 (Slack):** Envía un mensaje al canal indicado con un resumen.

---

### Detalle de Configuración por Nodo

#### 1. Trigger: Gmail Trigger
*   **Event:** `Message Received` (o `New Email`).
*   **Filters:**
    *   En la sección de filtros del trigger, puedes poner `Has the word` en el subject si tu versión de N8N lo permite directamente, pero es más seguro y flexible hacerlo con el nodo **IF** siguiente para manejar mayúsculas/minúsculas y variaciones.
*   **Credentials:** Tu cuenta de Google conectada.

#### 2. Lógica: Node "IF" (o "Switch")
Este nodo es crucial para no saturar tu Notion con correos basura.
*   **Condición:** Debes verificar el campo `Subject` (Asunto) del email.
*   **Expresión (JavaScript/N8N Expression):**
    Necesitas una condición que busque las palabras clave sin importar si están en mayúsculas o minúsculas.
    
    En el modo "Expression" del nodo IF, usarías algo así:
    ```javascript
    {{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotización') || $json.subject.toLowerCase().includes('cotizacion') }}
    ```
    *(Nota: Incluí "cotizacion" sin tilde por si te llegan correos de sistemas que no usan la ñ o tildes).*
*   **Salidas:**
    *   **True:** Continúa el flujo (hacia Notion y Slack).
    *   **False:** Detiene el flujo (no hace nada).

#### 3. Acción Destino: Notion Node
*   **Resource:** `Page`
*   **Operation:** `Create`
*   **Database ID:** El ID de tu base de datos en Notion (lo sacas de la URL de la base de datos en tu navegador).
*   **Properties (Mapeo de campos):**
    *   *Name (Título):* Mapea el `Subject` del email o pon "Propuesta de: [Remitente]".
    *   *Email (Type: Email):* Mapea el campo `From` o `From Address` del email.
    *   *Fecha (Type: Date):* Mapea el `Date` del email.
    *   *Cuerpo (Type: Text/Rich Text):* Mapea el `Text` o `HTML` del email (opcional, para tener el contexto).
    *   *Estado (Type: Select):* Puedes poner un valor fijo como "Nuevo" o "Revisar".

#### 4. Notificación: Slack Node
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** El canal donde quieres la alerta (ej. `#ventas` o `#general`).
*   **Text:** Aquí redactas el mensaje. Ejemplo:
    ```text
    🚨 *Nueva Propuesta/Cotización Recibida*
    *De:* {{ $json.from }}
    *Asunto:* {{ $json.subject }}
    *Fecha:* {{ $json.date }}
    
    Revisa la base de datos de Notion para más detalles.
    ```

### Consejos Técnicos Adicionales

1.  **Manejo de Adjuntos:** Si las propuestas vienen con PDFs adjuntos, el nodo de Gmail puede extraer el `attachmentId`. Podrías añadir un paso intermedio para descargar el archivo y subirlo a Notion como archivo adjunto a la página, aunque eso requiere un nodo extra de Google Drive o HTTP Request para descargar el binario.
2.  **Prevención de Bucles:** Asegúrate de que el trigger de Gmail tenga marcada la opción "Disable automatic execution" mientras lo pruebas, o usa el botón "Execute Node" manualmente para evitar llenar tu Notion de pruebas.
3.  **Formato de Fecha:** Notion es estricto con las fechas. Asegúrate de que el formato que sale de Gmail (ISO 8601) sea compatible o usa un nodo "Date & Time" para formatearlo antes de enviarlo a Notion si tienes errores.

¿Te gustaría que te genere el código JSON de este workflow para que solo tengas que importarlo en tu instancia de N8N?