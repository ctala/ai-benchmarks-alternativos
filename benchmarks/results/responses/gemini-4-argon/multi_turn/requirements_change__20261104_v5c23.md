# Gemini 4 Argon — multi_turn/requirements_change

- model_id: `google/gemini-4-argon`
- success: True  | final: 4.28 | quality: 4.0
- latency_total: 12.611s | tokens_per_second: 56.9
- input_tokens: 248 | output_tokens: 717

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

¡Excelente cambio! Usar Notion como CRM o base de datos y Slack para alertas en tiempo real es un flujo de trabajo mucho más potente para un emprendedor. 

Además, hay un truco técnico aquí: **no necesitas un nodo "IF" para filtrar**. Podemos hacer el filtro directamente en el nodo de Gmail para ahorrar ejecuciones de tu servidor o cuenta de N8N.

Aquí tienes la nueva estructura paso a paso:

### 1. Gmail Trigger (con filtro incluido)
En lugar de traer todos los correos y filtrarlos después, le diremos a Gmail que solo se active con los que nos interesan.
*   **Event:** Message Received.
*   **Simplify:** `True` (Esto es clave en N8N para que te entregue los datos limpios y no tengas que usar código para extraer el remitente).
*   **Filters -> Search:** Pon exactamente esto: `subject:(propuesta OR cotizacion)`

*Nota: Con `Simplify` activado, N8N ya te separa automáticamente el nombre y el correo del remitente en variables listas para usar.*

### 2. Notion Node (Guardar los datos)
Antes de configurar este nodo, asegúrate de crear una Base de Datos (tabla) en Notion con las columnas: *Asunto (Title), Nombre (Text), Email (Email), y Fecha (Date).* No olvides darle permisos a tu integración de N8N dentro de esa página de Notion (en los tres puntitos arriba a la derecha -> "Conexiones").

*   **Resource:** Database Page
*   **Operation:** Create
*   **Database ID:** Selecciona tu tabla de la lista.
*   **Properties (Mapeo de datos):**
    *   **Asunto (Title):** Arrastra el campo `Subject` del nodo de Gmail.
    *   **Email:** Arrastra el campo `From -> value[0] -> address`.
    *   **Nombre:** Arrastra el campo `From -> value[0] -> name`.
    *   **Fecha:** Arrastra el campo `Date`.

### 3. Slack Node (Notificación al equipo)
Lo conectamos después de Notion. ¿Por qué después? Porque así puedes incluir el link directo a la página de Notion recién creada en tu mensaje de Slack.

*   **Resource:** Message
*   **Operation:** Post
*   **Channel:** Elige tu canal (ej. `#ventas` o `#alertas`).
*   **Text:** Puedes armar un mensaje dinámico arrastrando los datos. Ejemplo:
    > 🚨 *¡Nueva oportunidad detectada!*
    > **De:** {{ $node["Gmail Trigger"].json["from"]["value"][0]["name"] }} ({{ $node["Gmail Trigger"].json["from"]["value"][0]["address"] }})
    > **Asunto:** {{ $node["Gmail Trigger"].json["subject"] }}
    > 🔗 Ver en Notion: {{ $json["url"] }} *(Este último dato viene del nodo de Notion anterior)*.

---

**Resumen del flujo:**
`[Gmail Trigger (Filtrado)]` ➡️ `[Notion (Crear Página)]` ➡️ `[Slack (Enviar Alerta)]`

¿Ya tienes creadas las credenciales (API Keys) de Notion y Slack en tu N8N, o necesitas ayuda con esa parte porque suele ser donde más se traban al principio?