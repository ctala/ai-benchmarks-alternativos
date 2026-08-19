# Gemini 3.5 Flash Lite — multi_turn/requirements_change

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 4.89 | quality: 4.0
- latency_total: 3.726s | tokens_per_second: 231.1
- input_tokens: 206 | output_tokens: 861

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

¡Excelente cambio! Un sistema de gestión de leads o propuestas automatizado en Notion y Slack es un clásico moderno de la productividad y encaja perfecto con n8n.

Para lograr esto, vamos a estructurar el workflow en 5 nodos. Aquí tienes el plano técnico de cómo configurarlo:

---

### Arquitectura del Workflow

```text
[Gmail Trigger] ──> [If (Filtro Asunto)] ──> [Notion (Crear Página)] ──> [Slack (Enviar Notificación)]
```
*(Nota: El nodo "If" saldrá a Notion y luego a Slack en cadena).*

---

### Configuración Paso a Paso:

#### 1. Nodo: **Gmail Trigger**
*   **Credential to connect with:** Configura tus credenciales de Google OAuth2.
*   **Event:** `Message Received` (Mensaje recibido).
*   **Parameters:**
    *   **Download Attachments:** No (a menos que los necesites).
    *   **Simple:** `False` (para tener acceso completo a los headers del correo).
    *   **Options > Include Spam Trash:** `False`.

#### 2. Nodo: **If** (El filtro)
Aquí filtramos para que solo pasen los correos que nos interesan.
*   **Condition:** `String` -> `{{ $json.subject }}`
*   **Operation:** `Contains`
*   **Value 1:** `propuesta`
*   *Nota sobre la segunda condición:* Como n8n permite múltiples condiciones, añade un O (`OR`) donde la condición sea que el asunto contenga `cotizacion` (o asegúrate de cubrir variaciones como "cotización" con tilde).

#### 3. Nodo: **Notion** (Guardar datos)
*   **Credential to connect with:** Tu integración de Notion.
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Selecciona tu base de datos en Notion (previamente debes haber compartido esa base de datos con tu integración de Notion).
*   **Mapeo de propiedades (Properties):**
    *   *Propiedad Título (ej. "Asunto"):* Mapea `{{ $json.subject }}`
    *   *Propiedad Email (Email):* Mapea `{{ $json.from.email }}` (o usa una expresión regular si el campo `from` viene en formato "Nombre <email@domain.com>").
    *   *Propiedad Nombre (Text):* Mapea `{{ $json.from.name }}`
    *   *Propiedad Fecha (Date):* Mapea `{{ $json.date }}`

*(Tip Pro: Si el campo `from` de Gmail te llega como "Juan Perez <juan@gmail.com>", puedes usar una pequeña expresión en n8n para limpiarlo, o dejar que Notion guarde el string completo).*

#### 4. Nodo: **Slack** (Notificación)
*   **Credential to connect with:** Tu Bot de Slack.
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Select Channel:** Elige el canal (ej. `#ventas` o `#leads`).
*   **Text:** Escribe un mensaje dinámico usando Markdown, por ejemplo:
    > 🚀 *¡Nueva propuesta recibida!*
    > 👤 **De:** `{{ $('Gmail Trigger').item.json.from.name }}` (`{{ $('Gmail Trigger').item.json.from.email }}`)
    > 📌 **Asunto:** `{{ $('Gmail Trigger').item.json.subject }}`
    > 📄 *Guardado automáticamente en Notion.*

---

### ¿Cómo proceder ahora?

¿Quieres que te detalle cómo extraer limpiamente el nombre y el email del campo `from` de Gmail (que a veces viene combinado), o te sientes cómodo montando esto en tu canvas de n8n?