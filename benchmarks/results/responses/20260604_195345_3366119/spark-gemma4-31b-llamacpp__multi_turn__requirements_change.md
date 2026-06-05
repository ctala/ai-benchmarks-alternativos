# Gemma 4 31B (Spark llama-server Q4_K_M) — multi_turn/requirements_change

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 6.51 | quality: 7.24
- latency_total: 91.541s | tokens_per_second: 9.8
- input_tokens: 230 | output_tokens: 900
- judge_score: 3.8 | justificación: 

## Respuesta completa

Entendido. El flujo se vuelve más interesante ahora que añadimos lógica de filtrado y múltiples destinos. Aquí tienes la arquitectura técnica detallada para montar este workflow en n8n.

### Estructura del Workflow

**Gmail Trigger** $\rightarrow$ **Filter Node** $\rightarrow$ **Notion Node** $\rightarrow$ **Slack Node**

---

### Configuración Paso a Paso

#### 1. Gmail Trigger (El disparador)
*   **Resource:** `Message`
*   **Event:** `Message Received`
*   **Filtros iniciales:** Te recomiendo configurar el campo **"Filters"** (si usas la versión más reciente de n8n) o dejar que lleguen todos y filtrar en el siguiente nodo.
*   **Importante:** Asegúrate de seleccionar que quieres recuperar el cuerpo del mensaje y los metadatos del remitente.

#### 2. Filter Node (La lógica de negocio)
Aquí es donde decidimos si el email nos interesa.
*   **Condición:** Selecciona el campo `Subject` (Asunto).
*   **Operador:** `Contains` (Contiene) o `Regex` (Expresión Regular).
*   **Valor:** Para que sea "uno u otro", lo ideal es usar una expresión regular: `(propuesta|cotizacion)`.
*   **Configuración:** Asegúrate de activar la opción **"Ignore Case"** para que detecte "Propuesta", "PROPUESTA" o "propuesta".

#### 3. Notion Node (El almacenamiento)
Antes de configurar el nodo, debes tener una Base de Datos en Notion con las columnas: *Nombre (Título), Email (Email), Asunto (Texto) y Fecha (Fecha)*.
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database ID:** Selecciona tu base de datos desde el desplegable.
*   **Mapping:** Mapea los datos del nodo de Gmail a las columnas de Notion:
    *   `Nombre` $\rightarrow$ `From Name`
    *   `Email` $\rightarrow$ `From Email`
    *   `Asunto` $\rightarrow$ `Subject`

#### 4. Slack Node (La notificación)
Este nodo va conectado **después** de Notion (para asegurarnos de que primero se guardó el dato).
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** Selecciona el canal (ej. `#ventas` o `#leads`).
*   **Text:** Crea un mensaje dinámico usando expresiones. Ejemplo:
    > 🚀 **¡Nueva oportunidad detectada!**
    > **Cliente:** `{{ $node["Gmail Trigger"].json["from"]["name"] }}`
    > **Asunto:** `{{ $node["Gmail Trigger"].json["subject"] }}`
    > 📝 *Ya ha sido registrado en Notion.*

---

### 💡 Tips Técnicos para Emprendedores (Best Practices)

1.  **Manejo de Errores:** Si Notion falla (por ejemplo, por un problema de permisos), el mensaje de Slack no se enviará. Si quieres que Slack se envíe *siempre*, independientemente de si se guardó en Notion, conecta el **Filter Node** a Notion y a Slack en paralelo (dos flechas saliendo del filtro).
2.  **Seguridad de Credenciales:** No olvides usar las **OAuth2 credentials** para Gmail y Notion; es la forma más segura y estable de evitar que el workflow se detenga cada pocos días.
3.  **Evitar Duplicados:** Si el trigger de Gmail se activa por "emails recibidos", ten cuidado con los hilos de conversación. Si el cliente responde al mismo correo, el filtro volverá a detectar la palabra "propuesta" en el asunto y creará una fila duplicada en Notion.
    *   *Solución:* Podrías añadir un nodo de **Notion (Search)** antes de crear la página para verificar si ese email ya existe en la base de datos.

**¿Necesitas que te ayude con la expresión regular exacta para el filtro o con la conexión de la API de Notion?**