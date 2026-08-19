# Gemma 4 12B (Spark llama-server, reasoning) — multi_turn/requirements_change

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 6.94 | quality: 7.52
- latency_total: 53.672s | tokens_per_second: 25.8
- input_tokens: 228 | output_tokens: 1386
- judge_score: 4.0 | justificación: 

## Respuesta completa

Es un cambio excelente. Este es un flujo de trabajo clásico de **"Lead Management"** (Gestión de Prospectos). Al pasar de Google Sheets a Notion, ganas una interfaz mucho más visual para gestionar el seguimiento.

Aquí tienes la estructura del nuevo workflow y la lógica que debemos aplicar:

### Estructura del Workflow en n8n

1.  **Gmail Trigger**: Detecta el correo entrante.
2.  **Filter Node**: Filtra por palabras clave en el asunto.
3.  **Edit Fields (Set)**: Limpia y organiza los datos (Nombre, Email, Asunto, Cuerpo).
4.  **Notion Node**: Crea una nueva página en tu base de datos.
5.  **Slack Node**: Envía la alerta al canal correspondiente.

---

### Configuración paso a paso

#### 1. Gmail Trigger
Configúralo para que revise tu bandeja de entrada. 
*   **Tip técnico:** Puedes usar el campo "Filters" en el nodo para que n8n solo traiga correos que ya cumplen ciertos criterios, pero es más seguro hacerlo en el siguiente paso (Filter Node) para tener más control.

#### 2. Filter Node (El "Cerebro" del filtro)
Aquí es donde aplicamos tu regla. Configura una condición lógica:
*   **Condition:** `Subject` (Asunto)
*   **Operator:** `Contains` (Contiene)
*   **Value:** `propuesta`
*   **OR (O)**
*   **Value:** `cotizacion`

*Esto asegura que si el correo no tiene ninguna de esas dos palabras, el workflow se detiene ahí y no hace nada más.*

#### 3. Edit Fields (Set)
Antes de enviar a Notion, necesitamos "limpiar" la información. Gmail entrega mucha información basura. Aquí crearemos variables claras:
*   `Nombre`: `{{ $json.from.name }}`
*   `Email`: `{{ $json.from.address }}`
*   `Asunto`: `{{ $json.subject }}`
*   `Contenido`: `{{ $json.textPlain }}` (o el cuerpo del mensaje).

#### 4. Notion Node
Selecciona la acción **"Create Database Page"**.
*   **Database ID**: Selecciona tu base de datos de "Prospectos" o "Ventas".
*   **Mapping**: Mapea los campos que creaste en el paso anterior a las propiedades de Notion (ej: la variable `Email` va a la propiedad de tipo "Email" en Notion).

#### 5. Slack Node
Selecciona la acción **"Send Message"**.
*   **Channel**: Selecciona tu canal (ej: #ventas-nuevas).
*   **Text**: Puedes personalizar el mensaje para que sea útil:
    > "🚀 **Nuevo Lead detectado!**
    > **De:** {{ $json.Nombre }} ({{ $json.Email }})
    > **Asunto:** {{ $json.Asunto }}
    > [Ver en Notion](URL_DE_TU_PAGINA_DE_NOTION)"

---

### Consejos de experto para este workflow:

1.  **Manejo de HTML:** Gmail a veces envía el cuerpo en HTML. Si ves que en Notion llega con códigos extraños (como `<div>...</div>`), asegúrate de usar la propiedad `textPlain` en lugar de `body` en el nodo de Gmail.
2.  **ID de Notion:** Cuando configures el nodo de Notion, asegúrate de que la base de datos tenga las columnas (propiedades) creadas previamente con los nombres exactos que vas a usar.
3.  **Frecuencia:** Si usas el "Gmail Trigger" por polling (revisión cada X minutos), asegúrate de que el intervalo sea el adecuado para tu negocio (ej. cada 1 o 5 minutos).

**¿Te gustaría que te ayude con la expresión exacta para el nodo de Filter o prefieres que profundicemos en cómo conectar Notion?**