# Gemma 4 31B — multi_turn/requirements_change

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 4.91 | quality: 4.0
- latency_total: 12.271s | tokens_per_second: 65.3
- input_tokens: 231 | output_tokens: 801

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

Cambiamos el rumbo. Este flujo es más potente porque ahora incluye **filtrado inteligente** y **notificaciones en tiempo real**.

Aquí tienes la arquitectura técnica del workflow y cómo configurar cada nodo:

### 🏗️ Estructura del Workflow
`Gmail Trigger` $\rightarrow$ `Filter Node` $\rightarrow$ `Notion Node` $\rightarrow$ `Slack Node`

---

### ⚙️ Configuración Paso a Paso

#### 1. Gmail Trigger (El disparador)
*   **Evento:** `On Message Received`.
*   **Filtros de Gmail:** Para optimizar el workflow y que no se ejecute con cada spam, en el campo **Filters** de n8n, puedes poner: `label:INBOX`.
*   **Importante:** Asegúrate de activar la opción de leer el cuerpo del mensaje si necesitas extraer más datos luego.

#### 2. Filter Node (El portero)
Aquí es donde aplicamos tu lógica de palabras clave.
*   **Condición:** Selecciona el campo `Subject` (Asunto).
*   **Operador:** `Regex Match` (es la forma más eficiente de buscar varias palabras).
*   **Valor:** `(propuesta|cotizacion)`
    *   *Nota: El símbolo `|` actúa como un "O" lógico. Si el asunto contiene cualquiera de las dos, el flujo continúa.*

#### 3. Notion Node (La base de datos)
*   **Operación:** `Create Database Page`.
*   **Database ID:** Selecciona tu base de datos de "Leads" o "Cotizaciones".
*   **Mapeo de campos:**
    *   **Nombre (Título):** Arrastra el campo `Subject` del nodo de Gmail.
    *   **Email (Email/Text):** Arrastra el `From Email`.
    *   **Fecha (Date):** Arrastra la `Date` del email.
    *   **Estado (Select):** Puedes poner un valor fijo como "Pendiente de Revisar".

#### 4. Slack Node (La alerta)
*   **Operación:** `Post Message`.
*   **Channel:** Selecciona el canal (ej. `#ventas` o `#notificaciones`).
*   **Texto:** Usa expresiones para que el mensaje sea útil. Ejemplo:
    > 🔔 **¡Nueva oportunidad detectada!**
    > 📧 **De:** `{{ $json.from.name }} <{{ $json.from.email }}>`
    > 📝 **Asunto:** `{{ $json.subject }}`
    > 🚀 *Ya ha sido guardado en Notion.*

---

### 💡 Tips Técnicos para Emprendedores (Pro-Tips)

1.  **Manejo de Errores:** Te recomiendo añadir un nodo de **Error Trigger** al principio. Si Notion falla (por ejemplo, si cambias un nombre de columna), n8n te avisará en lugar de que el email se pierda en el limbo.
2.  **Evitar Duplicados:** Si el trigger de Gmail lee el mismo correo dos veces, tendrás filas duplicadas en Notion. Para evitarlo, puedes usar un nodo de **Wait** o, mejor aún, marcar el email en Gmail con una etiqueta (ej. "Procesado") al final del flujo usando otro nodo de Gmail.
3.  **Case Insensitive:** En el nodo de Filtro, asegúrate de que la expresión regular no distinga entre mayúsculas y minúsculas para que detecte "PROPUESTA", "Propuesta" o "propuesta".

**¿Necesitas que te ayude con la expresión regular exacta o tienes dudas sobre cómo conectar la API de Notion?**