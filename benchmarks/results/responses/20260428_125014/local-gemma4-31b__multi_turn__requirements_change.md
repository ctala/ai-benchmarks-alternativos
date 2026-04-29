# Gemma 4 31B (DGX Spark Q4_K_M) — multi_turn/requirements_change

- model_id: `gemma4:31b`
- success: True  | final: 6.24 | quality: 6.4
- latency_total: 131.645s | tokens_per_second: 9.4
- input_tokens: 228 | output_tokens: 1232
- judge_score: 3.2 | justificación: 

## Respuesta completa

No hay problema, los cambios de rumbo son normales en el emprendimiento. Este flujo es más robusto y profesional. 

Lo más eficiente aquí es **filtrar los correos desde la fuente (Gmail)** en lugar de traer todos los emails a n8n y filtrarlos después. Esto ahorra tiempo de ejecución y evita errores.

Aquí tienes la arquitectura técnica del workflow:

### 🗺️ Mapa del Workflow
`Gmail Trigger` $\rightarrow$ `Notion Node` $\rightarrow$ `Slack Node`

---

### 🛠️ Configuración Detallada

#### 1. Gmail Trigger (El disparador)
En lugar de recibir todos los correos, usaremos el campo **"Filters"** o **"Query"**.
*   **Event:** `Message Received`
*   **Query:** `subject:(propuesta OR cotizacion)` 
    *   *Nota: Esto hace que n8n solo se active cuando el asunto contenga alguna de esas dos palabras.*
*   **Format:** `Resolved` (para que los datos vengan limpios).

#### 2. Notion Node (El almacenamiento)
Antes de configurar el nodo, asegúrate de haber creado una base de datos en Notion con las columnas: **Nombre** (Title), **Email** (Email), **Asunto** (Text) y **Fecha** (Date).
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Selecciona tu base de datos desde el desplegable.
*   **Properties:**
    *   **Nombre:** `{{ $json.from.name }}`
    *   **Email:** `{{ $json.from.value[0].address }}`
    *   **Asunto:** `{{ $json.subject }}`
    *   **Fecha:** `{{ $json.date }}`

#### 3. Slack Node (La notificación)
Este nodo va conectado después de Notion. Si Notion falla, no te notificará (lo cual es correcto, ya que el dato no se guardó).
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** Selecciona el canal (ej. `#ventas` o `#leads`).
*   **Text:** 
    > 🔔 **¡Nueva oportunidad detectada!**
    > 📩 **De:** {{ $json.from.name }} ({{ $json.from.value[0].address }})
    > 📝 **Asunto:** {{ $json.subject }}
    > 🚀 *Ya ha sido guardado en la base de datos de Notion.*

---

### 💡 Tips Técnicos para Emprendedores (Pro Tips):

1.  **Cuidado con el Formato de Fecha:** Notion es muy exigente con las fechas. Si notas que el nodo de Notion te da error, añade un nodo **"Date & Time"** antes de Notion para convertir la fecha de Gmail al formato ISO 8601.
2.  **Evitar Duplicados:** Si quieres evitar que un mismo email se guarde dos veces, podrías añadir un nodo de Notion antes de crear la página para "Buscar" si el ID del mensaje de Gmail ya existe en tu base de datos.
3.  **Manejo de Errores:** Te recomiendo activar la opción **"On Error $\rightarrow$ Continue"** en el nodo de Slack, para que si Slack falla, el flujo no se marque como "Error" ya que lo más importante (guardar en Notion) ya se cumplió.

**¿Tienes ya las credenciales de Notion y Slack conectadas en n8n o necesitas que te ayude a configurarlas?**