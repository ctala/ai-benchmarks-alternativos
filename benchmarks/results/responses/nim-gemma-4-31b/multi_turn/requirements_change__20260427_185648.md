# Gemma 4 31B (NIM) — multi_turn/requirements_change

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 6.83 | quality: 7.24
- latency_total: 90.209s | tokens_per_second: 9.2
- input_tokens: 241 | output_tokens: 829
- judge_score: 3.8 | justificación: 

## Respuesta completa

¡Entendido! El cambio es sencillo y, de hecho, hace que el workflow sea mucho más potente. Ahora pasamos de una simple hoja de cálculo a una base de datos relacional en Notion y un sistema de alertas en tiempo real con Slack.

Aquí tienes la estructura técnica detallada para montar este workflow:

### 1. Trigger: Gmail (Poll o Webhook)
*   **Nodo:** `Gmail Trigger`
*   **Evento:** `Message Received`
*   **Filtro Inicial:** Para optimizar el flujo y no procesar cada email que recibes, puedes usar el campo **Filters** $\rightarrow$ **Q (Query)**.
*   **Query sugerida:** `subject:(propuesta OR cotizacion)`
    *   *Tip técnico:* Hacer el filtro directamente en el trigger de Gmail es mucho más eficiente que usar un nodo de filtro después, ya que n8n solo se activará cuando se cumpla la condición.

### 2. Nodo de Filtrado (Opcional/Seguridad)
Si prefieres no usar la Query de Gmail o quieres reglas más complejas:
*   **Nodo:** `Filter`
*   **Condición:** `Subject` $\rightarrow$ `Contains` $\rightarrow$ `propuesta` **OR** `Subject` $\rightarrow$ `Contains` $\rightarrow$ `cotizacion`.

### 3. Nodo de Notion (Crear Registro)
*   **Nodo:** `Notion`
*   **Operación:** `Create Database Page`
*   **Configuración:**
    *   **Database ID:** Selecciona tu base de datos de "Leads" o "Propuestas".
    *   **Properties:** Mapea los datos del email a las columnas de Notion:
        *   *Nombre del Remitente* $\rightarrow$ `From Name`
        *   *Email* $\rightarrow$ `From Address`
        *   *Asunto* $\rightarrow$ `Subject`
        *   *Fecha* $\rightarrow$ `Date`

### 4. Nodo de Slack (Notificación)
*   **Nodo:** `Slack`
*   **Operación:** `Post Message`
*   **Canal:** Elige el canal de tu equipo (ej: `#ventas` o `#alertas`).
*   **Mensaje:** Puedes usar expresiones para que sea dinámico. Ejemplo:
    > 🔔 **¡Nueva Propuesta Recibida!**
    > 👤 **De:** `{{ $json.from.name }}` (`{{ $json.from.address }}`)
    > 📝 **Asunto:** `{{ $json.subject }}`
    > 🚀 *Ya ha sido registrado en Notion.*

---

### Resumen del flujo lógico:
`Gmail Trigger (Query: propuesta OR cotizacion)` $\rightarrow$ `Notion (Create Page)` $\rightarrow$ `Slack (Post Message)`

### 💡 Consejos Pro para emprendedores:

1.  **Manejo de Errores:** Te recomiendo añadir un **Error Trigger** o configurar el "On Error" de los nodos a "Continue", para que si Notion falla por algún motivo, al menos recibas la notificación de Slack.
2.  **Limpieza de Datos:** Si notas que los nombres de los remitentes vienen con formatos extraños (ej: `"Juan Perez <juan@email.com>"`), puedes insertar un nodo **Set** o un **Code Node** antes de Notion para limpiar el texto usando una expresión regular (Regex).
3.  **Conexiones:** Recuerda que para Notion necesitarás crear una "Integración" en el panel de Notion y **compartir la base de datos** con esa integración, de lo contrario n8n no la encontrará.

**¿Quieres que te ayude con la expresión regular para limpiar el nombre del remitente o prefieres intentar montarlo primero?**