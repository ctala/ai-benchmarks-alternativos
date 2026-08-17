# Gemma 4 26B MoE (3.8B activos) — multi_turn/requirements_change

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.96 | quality: 7.88
- latency_total: 32.03s | tokens_per_second: 33.0
- input_tokens: 230 | output_tokens: 1057
- judge_score: 4.0 | justificación: 

## Respuesta completa

¡Entendido! Ese es un cambio excelente. Pasar de Google Sheets a **Notion** le da una estructura de base de datos mucho más profesional, y los filtros de palabras clave junto con la notificación de **Slack** convierten este workflow en un sistema de gestión de leads o ventas real.

Aquí tienes la arquitectura técnica del nuevo workflow:

### Estructura del Workflow en N8N

1.  **Gmail Trigger**: Escucha nuevos correos.
2.  **Filter Node**: Filtra por palabras clave en el asunto.
3.  **Code Node (Opcional pero recomendado)**: Para limpiar y estructurar los datos.
4.  **Notion Node**: Crea una nueva página en tu base de datos.
5.  **Slack Node**: Envía el aviso de alerta.

---

### Configuración paso a paso

#### 1. Gmail Trigger
*   **Resource**: `Message`
*   **Event**: `Received`
*   **Filters**: No pongas filtros aquí para que N8N reciba todo y el filtrado lo haga el nodo siguiente (esto te da más control para debuguear).
*   *Tip técnico:* Asegúrate de que el nodo esté configurado para traer el `Snippet` o el `Body` si necesitas leer el contenido.

#### 2. Filter Node (El cerebro del filtrado)
Para que funcione con "o" (una palabra o la otra), configuraremos una condición lógica:
*   **Condition 1**: `String` -> `Subject` (del Gmail) -> `Contains` -> `propuesta`
*   **Logic**: Cambia el operador de `AND` a `OR`.
*   **Condition 2**: `String` -> `Subject` (del Gmail) -> `Contains` -> `cotizacion`
*   *Nota:* Si quieres que no importe si está en mayúsculas o minúsculas, te recomiendo usar una expresión en el campo de comparación para convertir todo a minúsculas: `{{ $json.subject.toLowerCase() }}`.

#### 3. Notion Node (La base de datos)
Antes de configurar el nodo, tu base de datos en Notion debe tener estas columnas (Properties):
*   `Nombre` (Title)
*   `Email` (Email)
*   `Asunto` (Text)
*   `Fecha` (Date)

**En N8N:**
*   **Resource**: `Database Page`
*   **Operation**: `Create`
*   **Database ID**: (Lo obtienes de la URL de tu base de datos de Notion).
*   **Mapping**: Mapea los campos del Gmail a las propiedades de Notion:
    *   `Nombre` $\rightarrow$ `{{ $json.from.name }}`
    *   `Email` $\rightarrow$ `{{ $json.from.value[0].address }}`
    *   `Asunto` $\rightarrow$ `{{ $json.subject }}`
    *   `Fecha` $\rightarrow$ `{{ $json.date }}`

#### 4. Slack Node (La notificación)
*   **Resource**: `Message`
*   **Operation**: `Post`
*   **Channel**: El canal donde quieras recibir la alerta (ej: `#ventas`).
*   **Text**: Usa un mensaje dinámico para que sea útil:
    > 🚀 **¡Nueva Propuesta Recibida!**
    > *   **De:** `{{ $json.from.name }}` (`{{ $json.from.value[0].address }}`)
    > *   **Asunto:** `{{ $json.subject }}`
    > *   *Revisa Notion para más detalles.*

---

### 💡 Consejos de Pro para tu implementación:

1.  **Manejo de errores**: Si un email no tiene un "Nombre" (solo tiene la dirección de correo), el nodo de Notion podría fallar. En el mapeo de Notion, puedes usar una expresión como esta para evitar errores:
    `{{ $json.from.name || $json.from.value[0].address }}` (Esto dice: "Usa el nombre, pero si no existe, usa el email").
2.  **Pruebas (Testing)**: No actives el workflow de inmediato. Usa el botón **"Test Step"** en cada nodo. Primero prueba el filtro con un email de prueba que tú mismo te envíes.
3.  **Optimización de Gmail**: Si recibes cientos de correos al día, el trigger de Gmail puede consumir muchos recursos. Si es el caso, te recomiendo filtrar desde el mismo Gmail usando el campo `Q` (Query) con `subject:(propuesta OR cotizacion)`. Esto hace que N8N solo trabaje cuando hay algo relevante.

**¿Quieres que te ayude con la expresión exacta de JavaScript para el nodo de limpieza o tienes dudas con la conexión de Notion?**