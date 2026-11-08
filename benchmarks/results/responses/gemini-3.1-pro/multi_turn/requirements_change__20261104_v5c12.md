# Gemini 3.1 Pro — multi_turn/requirements_change

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 4.08 | quality: 4.0
- latency_total: 19.101s | tokens_per_second: 88.4
- input_tokens: 202 | output_tokens: 1689

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

¡Excelente cambio! Notion es fantástico para gestionar leads o prospectos, y Slack te mantendrá al tanto en tiempo real. 

Como emprendedor, optimizar el consumo de recursos en n8n es clave. Por eso, **el mejor enfoque técnico no es usar un nodo "IF" o "Filter" después de leer los correos**, sino decirle a Gmail que *solo* nos envíe los correos que cumplan con esas palabras. Así ahorras ejecuciones (executions) en n8n.

Aquí tienes la arquitectura actualizada y cómo configurar cada nodo:

### 1. Nodo: Gmail Trigger (El disparador)
En lugar de traer todos los correos, usaremos la sintaxis de búsqueda nativa de Gmail.
*   **Event:** On Message
*   **Format:** Resolved (esto te entrega el texto limpio y los campos separados).
*   **Options -> Query (q):** Aquí está la magia. Escribe exactamente esto:
    `subject:propuesta OR subject:cotizacion`
    *(De esta manera, el workflow solo se activará si el asunto contiene alguna de esas dos palabras).*

### 2. Nodo: Notion (Guardar los datos)
Antes de configurar este nodo, asegúrate de tener una base de datos en Notion con las siguientes columnas (Properties): *Nombre (Title), Email (Email), Asunto (Text), Fecha (Date).*
*   **Resource:** Database Page
*   **Operation:** Create
*   **Database ID:** Selecciona tu base de datos de Notion.
*   **Properties:** Aquí vas a mapear (arrastrar) los datos que vienen del nodo de Gmail.
    *   *Nombre:* `{{ $json.from.name }}`
    *   *Email:* `{{ $json.from.address }}`
    *   *Asunto:* `{{ $json.subject }}`
    *   *Fecha:* `{{ $json.date }}`

### 3. Nodo: Slack (La notificación)
Conecta este nodo justo después del de Notion (o en paralelo usando el conector del Gmail Trigger, ambas formas funcionan).
*   **Resource:** Message
*   **Operation:** Post Message
*   **Channel:** El ID o nombre de tu canal (ej. `#ventas` o `#leads`).
*   **Text:** Puedes usar expresiones para hacer un mensaje dinámico. Por ejemplo:
    ```text
    🚀 ¡Nueva solicitud recibida!
    *De:* {{ $json.from.name }} ({{ $json.from.address }})
    *Asunto:* {{ $json.subject }}
    Revisa tu Notion para más detalles.
    ```

### 💡 Tip Técnico para ti:
Configurar las credenciales (Credentials) suele ser la parte donde la mayoría se atasca, especialmente con la API de Google (OAuth2) y la integración interna de Notion. 

¿Ya tienes conectadas tus cuentas de Gmail, Notion y Slack en tu instancia de n8n, o te gustaría que te guíe paso a paso en cómo crear las credenciales para alguna de ellas? También puedo generarte el código JSON del workflow para que solo lo copies y pegues en tu n8n.