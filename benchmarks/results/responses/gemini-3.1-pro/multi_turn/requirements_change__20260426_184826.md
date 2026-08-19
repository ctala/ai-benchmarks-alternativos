# Gemini 3.1 Pro — multi_turn/requirements_change

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.3 | quality: 7.44
- latency_total: 19.167s | tokens_per_second: 95.7
- input_tokens: 206 | output_tokens: 1835
- judge_score: 4.0 | justificación: 

## Respuesta completa

¡Excelente cambio! Usar Notion para gestionar prospectos y Slack para enterarte al instante es un *stack* de ventas clásico y súper efectivo para cualquier emprendedor.

Además, te voy a dar un **truco ninja de n8n** para el filtro: en lugar de usar un nodo extra para filtrar (lo cual consumiría ejecuciones de tu servidor), vamos a decirle a Gmail que *solo* le envíe a n8n los correos que cumplan esa condición.

Aquí tienes la arquitectura paso a paso de tu nuevo workflow:

### 🛠️ Preparación previa (En Notion)
Antes de ir a n8n, crea una base de datos en Notion (como una tabla) con las siguientes columnas (Propiedades):
*   **Nombre** (Tipo: *Title* - para el asunto o nombre del remitente)
*   **Email** (Tipo: *Email*)
*   **Asunto** (Tipo: *Text*)
*   **Fecha** (Tipo: *Date*)
*   *Importante:* Recuerda ir a los tres puntos arriba a la derecha en Notion, "Conexiones" y agregar tu integración de n8n para que tenga permisos de escritura.

---

### ⚙️ Configuración del Workflow en n8n

#### 1. Nodo: Gmail Trigger (El inicio y el filtro)
*   **Event:** `Message Received` (Mensaje recibido).
*   **Credential:** Conecta tu cuenta de Google.
*   **Options -> Query (El truco ninja):** Aquí vas a escribir exactamente esto: 
    `subject:propuesta OR subject:cotizacion`
    *¿Qué hace esto?* Le dice a la API de Gmail que n8n solo debe activarse si el asunto contiene alguna de esas dos palabras. Te ahorras un nodo de filtro y optimizas el rendimiento.

#### 2. Nodo: Notion (Guardar los datos)
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Selecciona la base de datos que creaste.
*   **Properties:** Aquí vas a mapear los datos que vienen de Gmail arrastrándolos desde el panel izquierdo (Output del nodo de Gmail) hacia los campos de Notion:
    *   *Email:* Arrastra el campo `from` (o extrae el email si viene con formato `Nombre <email@...>`, n8n suele separar esto en `from.value[0].address`).
    *   *Asunto:* Arrastra el campo `subject`.
    *   *Fecha:* Arrastra el campo `date`.

#### 3. Nodo: Slack (La notificación)
*   Conecta este nodo justo después del de Notion (o en paralelo desde el nodo de Gmail, como prefieras, pero en serie te aseguras de que se guardó en Notion primero).
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** Escribe el nombre de tu canal, por ejemplo `#ventas` o `#alertas`.
*   **Text:** Aquí puedes usar una expresión para que el mensaje sea dinámico. Por ejemplo:
    `🚀 ¡Nueva oportunidad! Hemos recibido un correo de {{ $json.from.value[0].name }}. Asunto: "{{ $json.subject }}". Ya está guardado en Notion.`

---

### 💡 Un consejo extra:
El campo `from` de Gmail a veces viene como `Juan Perez <juan@empresa.com>`. Si en n8n ves que el nodo de Gmail te entrega ese bloque de texto completo y quieres separar el nombre del correo para Notion, me avisas y te paso un pequeño código de un nodo **Code** (o usando expresiones regulares) para limpiarlo a la perfección.

¿Quieres que te genere el **código JSON** de este workflow para que solo tengas que copiarlo y pegarlo directamente en tu lienzo de n8n?