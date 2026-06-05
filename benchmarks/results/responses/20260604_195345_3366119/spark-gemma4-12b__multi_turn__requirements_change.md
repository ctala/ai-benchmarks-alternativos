# Gemma 4 12B (Spark llama-server Q4_K_M) — multi_turn/requirements_change

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 6.34 | quality: 6.4
- latency_total: 29.362s | tokens_per_second: 25.5
- input_tokens: 230 | output_tokens: 750
- judge_score: 3.2 | justificación: 

## Respuesta completa

Excelente cambio. Notion es una herramienta mucho más potente para gestionar proyectos y CRM, y Slack es ideal para la alertas en tiempo real.

Aquí tienes la estructura lógica del nuevo workflow y cómo configurar cada nodo:

### Estructura del Workflow
`Gmail Trigger` ➔ `Filter` ➔ `Notion` ➔ `Slack`

---

### Configuración paso a paso:

#### 1. Gmail Trigger (El disparador)
*   **Evento:** `Message Received`.
*   **Filtro (Query):** Para que n8n no procese *todos* tus correos y ahorres ejecuciones, usa el campo "Filters" y pon: `subject:propuesta OR subject:cotizacion`.
    *   *Nota:* Esto hace que el trigger solo se active si el correo cumple la condición, ahorrando recursos.

#### 2. Filter Node (Validación extra)
Aunque ya filtramos en el trigger, es buena práctica poner un nodo **Filter** después para asegurar que los datos que pasan al siguiente paso son correctos.
*   **Condición:** `Subject` (del Gmail) contiene `propuesta` **O** `Subject` contiene `cotizacion`.
*   *Esto asegura que si el trigger falla o se cambia, el resto del flujo esté protegido.*

#### 3. Notion Node (Almacenamiento)
*   **Resource:** `Database Page`.
*   **Operation:** `Create`.
*   **Database ID:** Selecciona tu base de datos de "Leads" o "Propuestas".
*   **Mapping de campos:**
    *   **Nombre:** `Sender Name` (Extraído de Gmail).
    *   **Email:** `Sender Email`.
    *   **Asunto:** `Subject`.
    *   **Estado:** Puedes ponerlo fijo como "Nuevo".
    *   **Contenido:** El cuerpo del mensaje (Body).

#### 4. Slack Node (Notificación)
*   **Resource:** `Message`.
*   **Operation:** `Post`.
*   **Channel:** Selecciona tu canal (ej: `#ventas-alertas`).
*   **Text:** Aquí puedes usar una expresión para que sea dinámico:
    > "🚀 **Nueva Propuesta Recibida**\n\n👤 **Remitente:** {{ $json.sender_name }}\n📧 **Email:** {{ $json.sender_email }}\n📝 **Asunto:** {{ $json.subject }}\n\n[Ver en Notion](URL_DE_TU_PAGINA_DE_NOTION)"

---

### Tips de experto para este workflow:

1.  **Manejo de HTML:** Gmail entrega el cuerpo del mensaje en formato HTML. Si quieres que en Notion se vea limpio, usa un nodo **HTML Extract** o un pequeño código en un nodo **Code** para limpiar las etiquetas `<div>`, `<p>`, etc., antes de enviarlo a Notion.
2.  **ID de Notion:** Asegúrate de que las columnas en Notion coincidan exactamente con los tipos de datos (ej: que el campo de Email sea tipo "Email" o "Text").
3.  **Error Handling:** Te recomiendo añadir un nodo de **Error Trigger**. Si Notion está caído o la API falla, quieres que n8n te avise, no que el correo se pierda sin registrarse.

**¿Quieres que te ayude con el código para limpiar el HTML del correo o prefieres empezar configurando las conexiones de las APIs?**