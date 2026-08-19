# Gemini 3.1 Flash Lite — multi_turn/requirements_change

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 6.79 | quality: 6.4
- latency_total: 3.664s | tokens_per_second: 221.4
- input_tokens: 206 | output_tokens: 811
- judge_score: 3.2 | justificación: 

## Respuesta completa

¡Excelente cambio! Notion es una herramienta mucho más potente para gestionar leads o propuestas.

Para lograr esto, vamos a estructurar el flujo de la siguiente manera:

### Estructura del Workflow
1. **Gmail Trigger**: Configurado para recibir emails.
2. **Filter (IF)**: Para validar si el asunto contiene "propuesta" o "cotización".
3. **Notion**: Para crear una fila en tu base de datos.
4. **Slack**: Para enviarte la notificación.

---

### Paso a paso de la configuración:

#### 1. Gmail Trigger
*   **Event:** `Message Received`
*   **Download Attachments:** Apagado (a menos que los necesites).
*   **Simple/Polling:** Usa `Polling` para verificar cada X minutos.

#### 2. IF Node (El filtro)
Aquí es donde aplicamos la lógica:
*   **Condition:** `String` -> `Subject` -> `Contains` -> `propuesta`
*   **Add Condition:** `OR`
*   **Condition:** `String` -> `Subject` -> `Contains` -> `cotización` (o `cotizacion` sin tilde por seguridad).
*   *Nota:* Asegúrate de marcar la opción **"Ignore Case"** para que filtre independientemente de si está en mayúsculas o minúsculas.

#### 3. Notion Node
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Pega el ID de tu base de datos (puedes obtenerlo de la URL de tu página de Notion).
*   **Properties:** Aquí mapeas los campos. Ejemplo:
    *   `Nombre`: `{{ $json.from.value[0].name }}`
    *   `Email`: `{{ $json.from.value[0].address }}`
    *   `Asunto`: `{{ $json.subject }}`
    *   `Fecha`: `{{ $json.date }}`
*   *Tip:* Asegúrate de que en Notion las columnas tengan el tipo de dato correcto (Text, Email, Date).

#### 4. Slack Node
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** El canal donde quieres recibir la alerta.
*   **Text:** Puedes poner algo como: 
    > "📩 Nueva propuesta recibida de: {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }}). 
    > Asunto: {{ $json.subject }}"

---

### Tips de experto para este flujo:

1.  **Regex en el Filtro:** Si quieres ser más preciso, en el nodo **IF**, puedes usar una expresión regular (Regex) para capturar ambas palabras en una sola condición: `(?i)propuesta|cotizacion`.
2.  **Limpieza de datos:** A veces el campo `from` de Gmail viene con un formato complejo. Si ves que el nombre sale extraño, puedes añadir un nodo **Code** antes de Notion para limpiar el string:
    ```javascript
    // Ejemplo rápido para limpiar el nombre
    items[0].json.senderName = items[0].json.from.value[0].name || "Sin nombre";
    return items;
    ```
3.  **Error Handling:** Si el nodo de Notion falla (ej: la API está caída), te recomiendo conectar el nodo de Slack a la salida de error del nodo de Notion, así te enterarás si algo no se guardó.

**¿Necesitas ayuda con la conexión (OAuth) de alguno de estos servicios o quieres que te pase el JSON del código del workflow para que lo importes directo?**