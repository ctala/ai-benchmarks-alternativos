# Gemini 3.5 Flash Lite — multi_turn/requirements_change

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 4.88 | quality: 4.0
- latency_total: 3.445s | tokens_per_second: 264.2
- input_tokens: 202 | output_tokens: 910

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

¡Excelente cambio de planes! Esa arquitectura (Gmail -> Filtrado -> Notion -> Slack) es un clásico automatizado súper útil para la gestión de leads o proyectos.

Para lograr esto en N8N, vamos a estructurar el workflow en **4 nodos principales**. 

Aquí tienes el paso a paso de cómo configurarlo:

---

### Paso 1: Nodo Gmail (Trigger)
Queremos que el workflow se active cada vez que llegue un correo nuevo.
*   **Nodo:** `Gmail`
*   **Credenciales:** Conecta tu cuenta de Gmail.
*   **Resource:** `Message`
*   **Operation:** `Get` (o *On Message Received* usando el trigger específico).
*   **Options:** 
    *   *Download Attachments*: No (a menos que los necesites).
    *   *Simplify*: `True` (Esto te devolverá un JSON limpio con campos como `from`, `subject`, `text`, `date`).

---

### Paso 2: Nodo If (Filtro por Asunto)
Aquí filtramos para que solo pasen los emails que nos interesan.
*   **Nodo:** `If`
*   **Configuración de la condición:**
    *   Value 1: `{{ $json.subject }}` (Usando la expresión del nodo anterior).
    *   Operation: `String` -> `Contains` (o puedes usar Regex para ser más flexible).
    *   Value 2: `propuesta`
    *   *(Nota: N8N permite agregar múltiples condiciones. Agregamos otra condición con "OR" para que busque "cotizacion")*.

---

### Paso 3: Nodo Notion (Guardar datos)
Si el correo pasa el filtro, lo guardamos en tu base de datos de Notion.
*   **Nodo:** `Notion`
*   **Credenciales:** Conecta tu integración de Notion (asegúrate de haber compartido la página/base de datos con tu integración).
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Selecciona tu base de datos de Notion.
*   **Properties Mapping:** Mapea las columnas de tu Notion con los datos del email:
    *   *Título (ej. Nombre de la página):* `{{ $json.subject }}`
    *   *Remitente (Email):* `{{ $json.from }}`
    *   *Fecha:* `{{ $json.date }}`
    *   *Contenido/Snippet:* `{{ $json.snippet }}`

---

### Paso 4: Nodo Slack (Notificación)
Para avisar al equipo (o a ti mismo) de forma inmediata.
*   **Nodo:** `Slack`
*   **Credenciales:** Conecta tu bot de Slack.
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Select Channel:** Elige el canal (ej. `#leads` o `#ventas`).
*   **Text:** Escribe un mensaje dinámico usando Markdown, por ejemplo:
    > 🚀 *¡Nueva propuesta recibida!*
    > 👤 **De:** `{{ $('Gmail').item.json.from }}`
    > 📄 **Asunto:** `{{ $('Gmail').item.json.subject }}`
    > 📅 **Fecha:** `{{ $('Gmail').item.json.date }}`

---

### 💡 Tips Pro para este workflow:
1. **Limpiar el campo "From":** A veces Gmail te entrega el remitente en formato `"Nombre Apellido" <email@dominio.com>`. Si quieres extraer solo el email limpio para Notion, puedes usar una pequeña expresión en JavaScript dentro del nodo de Notion: 
   `{{ $json.from.match(/<(.+?)>/)?.[1] || $json.from }}`
2. **Case Insensitive:** En el nodo `If`, asegúrate de que la búsqueda ignore mayúsculas/minúsculas para que atrape "PROPUESTA", "Propuesta" y "propuesta".

¿Te queda alguna duda sobre la configuración de alguno de estos nodos en la interfaz de N8N?