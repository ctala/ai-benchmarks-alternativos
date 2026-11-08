# Gemma 4 26B MoE (3.8B activos) — multi_turn/requirements_change

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.3 | quality: 6.0
- latency_total: 15.162s | tokens_per_second: 63.7
- input_tokens: 231 | output_tokens: 966

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

¡Excelente cambio! Ese workflow es mucho más profesional y útil para un proceso de ventas o gestión de leads. Al pasar a **Notion**, transformas un simple registro en una base de datos de gestión (CRM).

Aquí tienes la arquitectura lógica del workflow optimizado:

### Estructura del Workflow en N8N

1.  **Gmail Trigger**: Escucha nuevos correos.
2.  **Filter Node (El cerebro del filtro)**: Decide si el correo sigue adelante o se detiene.
3.  **Code Node (Opcional pero recomendado)**: Para limpiar el nombre del remitente y extraer datos limpios.
4.  **Notion Node**: Crea una nueva página en tu base de datos.
5.  **Slack Node**: Envía la alerta inmediata.

---

### Configuración Detallada paso a paso:

#### 1. Gmail Trigger
*   **Event**: `Message Received`.
*   **Filters**: No pongas el filtro de palabras aquí (es mejor hacerlo en el nodo Filter de N8N para tener más control), pero asegúrate de que la conexión esté activa.

#### 2. Filter Node (Filtro de palabras clave)
Aquí es donde aplicamos tu lógica.
*   **Condition 1 (OR)**:
    *   `Value 1`: `{{ $json.subject }}` (el asunto del email).
    *   `Operator`: `Contains` (Contiene).
    *   `Value 2`: `propuesta`.
*   **Condition 2 (OR)**:
    *   `Value 1`: `{{ $json.subject }}`.
    *   `Operator`: `Contains`.
    *   `Value 2`: `cotizacion`.
*   *Importante*: Configura el nodo para que sea una condición **OR** (O), para que pase si cumple cualquiera de las dos.

#### 3. Notion Node (Guardar datos)
Antes de esto, asegúrate de tener una base de datos en Notion con estas columnas: *Nombre, Email, Asunto, Fecha*.
*   **Resource**: `Database Page`.
*   **Operation**: `Create`.
*   **Database ID**: Selecciona tu base de datos de Notion.
*   **Properties**: Mapea los datos del Gmail:
    *   `Nombre` $\rightarrow$ `{{ $json.from.name }}`
    *   `Email` $\rightarrow$ `{{ $json.from.value[0].address }}`
    *   `Asunto` $\rightarrow$ `{{ $json.subject }}`
    *   `Fecha` $\rightarrow$ `{{ $json.date }}`

#### 4. Slack Node (Notificación)
*   **Resource**: `Message`.
*   **Operation**: `Post`.
*   **Channel**: El canal donde quieras recibir la alerta (ej: `#ventas` o `#leads`).
*   **Text**: Usa un mensaje dinámico para que sea útil:
    > 🚨 **¡Nueva Propuesta Recibida!** 🚨
    > *   **De:** `{{ $json.from.name }}` (`{{ $json.from.value[0].address }}`)
    > *   **Asunto:** `{{ $json.subject }}`
    > *   **Link a Notion:** [Ir a la base de datos]

---

### 💡 Consejos de Pro para tu Emprendimiento:

1.  **Manejo de Mayúsculas/Minúsculas**: En el nodo **Filter**, te recomiendo usar una expresión para convertir el asunto a minúsculas antes de comparar, así no importa si escriben "PROPUESTA" o "propuesta".
    *   Usa: `{{ $json.subject.toLowerCase() }}` en el campo de valor.
2.  **Evita Duplicados**: Si el cliente envía dos correos seguidos, Notion creará dos filas. Si quieres evitarlo, necesitarías un nodo de "Search" en Notion antes de crear la página para verificar si ese email ya existe.
3.  **Error Handling**: Si un email viene sin nombre (solo el email), el nodo de Notion podría fallar. Te recomiendo usar un pequeño nodo **Code** antes para decir: `if (!name) { name = email }`.

**¿Quieres que te ayude con el código específico de ese nodo para limpiar los datos o prefieres intentar armar la lógica de los nodos primero?**