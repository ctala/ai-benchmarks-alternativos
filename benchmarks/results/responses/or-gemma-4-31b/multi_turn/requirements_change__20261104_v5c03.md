# Gemma 4 31B — multi_turn/requirements_change

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 6.54 | quality: 6.0
- latency_total: 7.356s | tokens_per_second: 109.6
- input_tokens: 230 | output_tokens: 806

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

¡Perfecto! El cambio es sencillo. Básicamente, estamos sustituyendo la base de datos y añadiendo una capa de **lógica de filtrado** y una **notificación**.

Aquí tienes la arquitectura técnica de cómo debe quedar tu workflow en n8n:

### 🗺️ Mapa del Workflow
`Gmail Trigger` $\rightarrow$ `Filter Node` $\rightarrow$ `Notion Node` $\rightarrow$ `Slack Node`

---

### 🛠️ Configuración Detallada Nodo por Nodo

#### 1. Gmail Trigger (El disparador)
*   **Evento:** `Message Received`.
*   **Filtros:** Puedes dejarlo vacío aquí o poner `q: "propuesta OR cotizacion"` directamente en el campo de búsqueda de Gmail para que n8n solo procese esos correos desde el inicio (esto ahorra ejecuciones).
*   **Output:** Asegúrate de que esté configurado para traer el cuerpo del mensaje y los metadatos del remitente.

#### 2. Filter Node (El portero)
Si no filtraste en el paso anterior, usa el nodo **Filter**:
*   **Condición 1:** `Subject` $\rightarrow$ `Contains` $\rightarrow$ `propuesta`
*   **Operador:** Cambia "AND" por **"OR"**.
*   **Condición 2:** `Subject` $\rightarrow$ `Contains` $\rightarrow$ `cotizacion`
*   *Tip:* Para que no importe si escribieron "Propuesta" (mayúscula) o "propuesta" (minúscula), usa una expresión regular o convierte el texto a minúsculas antes de comparar.

#### 3. Notion Node (La base de datos)
*   **Resource:** `Database Page`.
*   **Operation:** `Create`.
*   **Database ID:** Selecciona tu base de datos de Notion (asegúrate de que la integración de Notion tenga acceso a esa página específica).
*   **Mapeo de campos:**
    *   Nombre del Cliente $\rightarrow$ `{{ $json.from.name }}`
    *   Email $\rightarrow$ `{{ $json.from.address }}`
    *   Asunto $\rightarrow$ `{{ $json.subject }}`
    *   Fecha $\rightarrow$ `{{ $json.date }}`

#### 4. Slack Node (La alerta)
*   **Resource:** `Message`.
*   **Operation:** `Post`.
*   **Channel:** Selecciona el canal (ej. `#ventas` o `#leads`).
*   **Text:** Crea un mensaje dinámico:
    > 🚀 **¡Nueva oportunidad detectada!**
    > **Cliente:** {{ $json.from.name }}
    > **Asunto:** {{ $json.subject }}
    > *Ya ha sido guardado en Notion.*

---

### 🚀 Tips Técnicos para Emprendedores:

1.  **Manejo de Errores:** Te recomiendo añadir un **Error Trigger** al workflow. Si Notion falla (por ejemplo, por un campo mal configurado), quieres saberlo inmediatamente en lugar de perder el lead.
2.  **Limpieza de Datos:** Si notas que el nombre del remitente viene sucio (ej: `"Juan Perez <juan@email.com>"`), puedes usar un nodo **Edit Fields (Set)** antes de Notion para limpiar el texto usando una expresión simple de JavaScript `.split('<')[0]`.
3.  **Seguridad:** No olvides configurar las credenciales de Google y Notion usando **OAuth2** para que el workflow sea estable y no expire la sesión cada pocos días.

**¿Quieres que te ayude con la expresión exacta para limpiar el nombre del remitente o prefieres intentar montarlo primero?**