# GLM 5.2 — multi_turn/requirements_change

- model_id: `z-ai/glm-5.2`
- success: True  | final: 4.43 | quality: 4.0
- latency_total: 18.882s | tokens_per_second: 80.6
- input_tokens: 235 | output_tokens: 1521

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

¡Entendido! Me parece un cambio excelente. Notion es fantástico para gestionar este tipo de información y el filtro con Slack te ahorrará mucho tiempo, dejándote enfocado solo en lo que importa.

Aquí tienes la estructura del nuevo workflow en n8n:

### 1. Nodo: Gmail Trigger
*   **Acción:** Se activa automáticamente cuando llega un correo nuevo.
*   **Configuración:**
    *   Conecta tu cuenta de Gmail.
    *   En "Label", selecciona `INBOX` (o la etiqueta que prefieras).
    *   En "Fetch By", elige `Message` para traer los datos del correo.
    *   Ajusta el tiempo de revisión (Polling time) a 1 minuto o el que prefieras.

### 2. Nodo: If (Filtro de Asunto)
*   **Acción:** Filtra los correos para que solo continúen si cumplen la condición.
*   **Configuración:**
    *   **Value 1:** Arrastra el campo del asunto desde el nodo de Gmail (suele ser `{{$json["subject"]}}`).
    *   **Condition:** `Contains` (Contiene).
    *   **Value 2:** Escribe `propuesta`.
    *   Haz clic en "Add condition" y cambia a "OR" (O).
    *   **Value 1:** Vuelve a arrastrar el asunto.
    *   **Condition:** `Contains`.
    *   **Value 2:** Escribe `cotizacion` (o `cotización`, depende de cómo te escriban, puedes añadir ambas).
*   *Nota:* Todo lo que conectes a partir de aquí debe salir por la rama **"True"** del nodo IF.

### 3. Nodo: Notion (Crear registro)
*   **Acción:** Guarda los datos del remitente en una base de datos de Notion.
*   **Pre-requisito:** Debes tener una base de datos (Database) creada en Notion con columnas para Nombre, Email, Asunto y Fecha.
*   **Configuración:**
    *   Conecta tu cuenta de Notion (necesitarás darle permisos a n8n para acceder a esa base de datos específica).
    *   **Resource:** `Database Page`
    *   **Operation:** `Create`
    *   **Database ID:** Selecciona tu base de datos.
    *   En las propiedades (Properties), mapea los datos:
        *   *Title (Título):* Asunto del email `{{$json["subject"]}}`
        *   *Email:* Email del remitente `{{$json["from"]["value"][0]["address"]}}` *(así se extrae el email puro en n8n)*
        *   *Nombre:* Nombre del remitente `{{$json["from"]["value"][0]["name"]}}`
        *   *Fecha:* Fecha del email `{{$json["date"]}}`

### 4. Nodo: Slack (Notificación)
*   **Acción:** Te avisa por Slack que hay un nuevo registro.
*   **Configuración:**
    *   Conecta tu cuenta de Slack.
    *   **Resource:** `Message`
    *   **Operation:** `Send`
    *   **Channel:** Selecciona tu canal o chat directo (ej. `#ventas` o tu usuario `@tu_usuario`).
    *   **Message:** Puedes armar un texto dinámico, por ejemplo:
        `🚨 ¡Nueva propuesta/cotización recibida! 🚀 \n*De:* {{$json["from"]["value"][0]["name"]}} ({{$json["from"]["value"][0]["address"]}})\n*Asunto:* {{$json["subject"]}}`

**Un consejo técnico:** Para el nodo de Notion, si el remitente no tiene un nombre configurado en su cliente de correo, el campo `name` puede venir vacío. Si quieres asegurarte de que siempre haya un nombre, puedes usar una pequeña expresión condicional en n8n o simplemente dejarlo así y revisarlo a mano.

¿Quieres que te genere el código JSON del workflow para que solo lo copies y pegues directamente en tu lienzo de n8n?