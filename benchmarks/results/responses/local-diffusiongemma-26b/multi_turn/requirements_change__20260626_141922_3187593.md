# DiffusionGemma 26B-A4B (DGX Spark Q8_0) — multi_turn/requirements_change

- model_id: `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0`
- success: True  | final: 7.42 | quality: 8.16
- latency_total: 56.178s | tokens_per_second: 27.3
- input_tokens: 0 | output_tokens: 1536
- judge_score: 4.2 | justificación: 

## Respuesta completa

thought
Technical assistant for entrepreneurs using n8n.
Read Gmail emails, extract sender (name, email), subject, date, save to Notion (instead of Google Sheets), filter for emails containing "propuesta" or "cotizacion" in the subject, and send a Slack notification.

    *   *Step 1: Trigger.* Gmail Trigger (watch for new emails).
    *   *Step 2: Filter.* Filter node (check subject for "propuesta" or "cotizacion").
    *   *Step 3: Data Transformation.* Set node or Code node (to format the data for Notion).
    *   *Step 4: Storage.* Notion node (create a database page).
    *   *Step 5: Notification.* Slack node (send message).

    *   **Node 1: Gmail Trigger**
        *   Event: "Message Received".
        *   Filters: Can use Gmail's native filters to save executions, but the user asked for a filter in the workflow logic. I'll show how to use the Filter node for clarity, or mention query for efficiency. Let's stick to the Filter node for regex or multiple conditions.

    *   **Node 2: Filter (The logic)**
        *   Condition: Subject contains "propuesta" OR Subject contains "cotizacion".
        *   Case-insensitive is important here.

    *   **Node 3: Set (Data Preparation)**
        *   Extract: `From Name`, `From Email`, `Subject`, `Date`.

    *   **Node 4: Notion**
        *   Operation: "Create Page".
        *   Database ID: (Placeholder).
        *   Mapping: Map the Set fields to Notion properties.

    *   **Node 5: Slack**
        *   Operation: "Post Message".
        *   Text: "Nueva propuesta recibida: [Subject] de [Sender]".

    *   Introduction: Acknowledge the change in requirements.
    *   Step-by-step workflow breakdown.
    *   Specific configuration details for each node.
    *   Tips for success (authentication, mapping).

    *   *Correction on Gmail Trigger:* It's actually more efficient to use a query in the Gmail Trigger itself (e.g., `subject:(propuesta OR cotizacion)`) to avoid running the workflow for every email. I should mention this as a pro-tip.
    *   *Notion setup:* Remind the user they need a database in Notion with specific columns first.¡Excelente cambio! El flujo hacia Notion es muy útil para gestionar leads o propuestas de forma visual, y añadir filtros te ayudará a no saturar tu Notion con información innecesaria.

Aquí tienes la estructura del workflow optimizada para n8n:

### Estructura del Workflow
1. **Gmail Trigger**: Detecta los correos nuevos.
2. **Filter**: Selecciona solo los que interesan.
3. **Set (Edit Fields)**: Prepara los datos para Notion y Slack.
4. **Notion**: Crea el registro en tu base de datos.
5. **Slack**: Envía la alerta inmediata.

---

### Configuración detallada de cada nodo

#### 1. Gmail Trigger (El disparador)
*   **Event**: `Message Received`.
*   **Filters (Opcional pero recomendado)**: Para ahorrar ejecuciones de n8n, puedes poner en el campo "Filters": `subject:(propuesta OR cotizacion)`. Esto hará que n8n solo se despierte si el correo ya cumple el criterio.
*   **Format**: `Resolved Data`.

#### 2. Filter (El filtro de lógica)
Si no usaste el filtro del paso anterior, usa este nodo:
*   **Conditions**: `OR` (o cualquiera de).
*   **Condición 1**: `{{ $json.subject }}` — **Contains** `propuesta`.
*   **Condición 2**: `{{ $json.subject }}` — **Contains** `cotizacion`.
*   *Nota: Asegúrate de activar "Ignore Case" para que detecte mayúsculas y minúsculas.*

#### 3. Set / Edit Fields (Limpieza de datos)
Este nodo sirve para organizar la información antes de enviarla a Notion. Crea los siguientes campos:
*   **remitente_nombre**: `{{ $json.from[0].name }}`
*   **remitente_email**: `{{ $json.from[0].address }}`
*   **asunto**: `{{ $json.subject }}`
*   **fecha**: `{{ $json.date }}` (puedes usar una expresión para darle formato si lo prefieres).

#### 4. Notion (Guardar datos)
*   **Resource**: `Database Page`.
*   **Operation**: `Create`.
*   **Database ID**: Selecciona tu base de datos de Notion.
*   **Properties**: Aquí mapeas las columnas de tu Notion con los datos que sacaste en el nodo "Set":
    *   *Nombre* -> `{{ $json.remitente_nombre }}`
    *   *Email* -> `{{ $json.remitente_email }}`
    *   *Asunto* -> `{{ $json.asunto }}`
    *   *Fecha* -> `{{ $json.fecha }}`

#### 5. Slack (Notificación)
*   **Resource**: `Message`.
*   **Operation**: `Post`.
*   **Channel**: Selecciona tu canal (ej. `#ventas`).
*   **Text**: Puedes armar un mensaje dinámico:
    > "🔔 *¡Nueva propuesta recibida!* 🔔
    > *De:* {{ $json.remitente_nombre }} ({{ $json.remitente_email }})
    > *Asunto:* {{ $json.asunto }}"

---

### Tips de experto para emprendedores:

1.  **Notion**: Antes de conectar el nodo de n8n, asegúrate de que la base de datos en Notion tenga las columnas creadas con el tipo exact correcto (Texto para nombres, Fecha para la fecha).
2.  **Formato de fecha**: Gmail envía la fecha en un formato largo. Si en Notion se ve raro, en el nodo Set usa esta expresión: `{{ DateTime($json.date).format('YYYY-MM-DD') }}`.
3.  **Pruebas**: Usa el botón "Test Step" en cada nodo enviándote un correo de prueba manualmente para verificar que los datos fluyen correctamente hacia Notion y Slack.

¿Quieres que te ayude con alguna expresión específica para formatear el texto o la conexión con la API de Notion?