# Gemini 3.1 Flash Lite (GA) — multi_turn/requirements_change

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 6.41 | quality: 6.0
- latency_total: 3.638s | tokens_per_second: 219.1
- input_tokens: 202 | output_tokens: 797

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

¡Excelente cambio! Notion es una herramienta mucho más potente para gestionar leads o propuestas.

Para lograr esto, necesitamos un flujo lógico que filtre antes de procesar. Aquí tienes la estructura paso a paso:

### Estructura del Workflow

1.  **Gmail Trigger**: Configurado para escuchar nuevos mensajes.
2.  **Filter (If)**: Nodo para validar el asunto.
3.  **Notion**: Nodo para crear la página en tu base de datos.
4.  **Slack**: Nodo para enviar la notificación.

---

### Configuración detallada:

#### 1. Gmail Trigger
*   **Event:** `Message Received`
*   **Download Attachments:** Desactivado (a menos que los necesites).
*   **Simple:** `True`.

#### 2. Filter (Nodo "If")
Aquí es donde ocurre la magia del filtrado.
*   **Condition:** String -> `Subject`
*   **Operation:** `Contains` (puedes usar Regex si quieres ser más preciso).
*   **Value 1:** `{{ $json.subject }}`
*   **Value 2 (Rule 1):** `propuesta`
*   **Add Rule (OR):**
    *   **Value 2 (Rule 2):** `cotizacion`
*   *Nota: Asegúrate de marcar "Ignore Case" para que detecte tanto "Cotización" como "cotizacion".*

#### 3. Notion (Conectado a la rama "True" del Filter)
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Selecciona tu base de datos de leads/ventas.
*   **Properties:** Mapea los campos:
    *   `Nombre`: `{{ $json.from.name }}`
    *   `Email`: `{{ $json.from.address }}`
    *   `Asunto`: `{{ $json.subject }}`
    *   `Fecha`: `{{ $json.date }}`

#### 4. Slack (Conectado después de Notion)
*   **Resource:** `Chat`
*   **Operation:** `Post Message`
*   **Channel:** Elige tu canal de ventas o alertas.
*   **Text:** Usa una expresión para el mensaje:
    > "📩 Nueva propuesta recibida de: {{ $json.from.name }} ({{ $json.from.address }}). Revisa Notion para los detalles."

---

### Consejos de experto para este flujo:

1.  **Limpieza de datos:** A veces el campo `from` en Gmail viene como "Nombre <email@ejemplo.com>". Si el nodo de Notion te da error, usa un nodo **Code** antes de Notion para separar el nombre del email usando una expresión simple:
    ```javascript
    const from = items[0].json.from.value; // Ajusta según la estructura de tu trigger
    // Puedes usar split o regex aquí para separar nombre y email
    ```
2.  **Duplicados:** Si recibes muchos emails del mismo cliente, considera añadir un nodo **"Wait"** o un **"Merge"** si quieres evitar notificaciones duplicadas en un corto periodo de tiempo.
3.  **Notion Template:** Asegúrate de que la base de datos en Notion tenga exactamente las mismas propiedades (tipo de dato) que estás enviando desde N8N (ej: que el campo Email sea de tipo 'Email' en Notion).

**¿Quieres que te pase el JSON del workflow para que solo tengas que copiar y pegar en tu N8N?** (Solo tendría que ajustar los IDs de tus credenciales).