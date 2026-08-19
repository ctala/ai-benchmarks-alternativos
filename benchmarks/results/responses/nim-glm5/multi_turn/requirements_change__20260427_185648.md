# GLM 5 (NIM) — multi_turn/requirements_change

- model_id: `z-ai/glm5`
- success: True  | final: 6.24 | quality: 6.4
- latency_total: 199.741s | tokens_per_second: 5.1
- input_tokens: 228 | output_tokens: 1009
- judge_score: 3.2 | justificación: 

## Respuesta completa

¡Excelente cambio de idea! Notion es una herramienta fantástica para llevar un seguimiento de propuestas y cotizaciones, y Slack te va a dar la inmediatez que necesitas para no perder detalle.

Para lograr esto, tu workflow va a tener 5 nodos. Te explico la estructura y luego te doy el detalle de la configuración:

1. **Gmail Trigger**: Detecta el email nuevo.
2. **If**: Filtra por las palabras clave.
3. **Notion**: Guarda los datos si cumple la condición.
4. **Slack**: Manda la notificación si cumple la condición.
5. **No Operation**: Descarta el email si no cumple la condición.

Aquí tienes el paso a paso de cada nodo:

### 1. Gmail Trigger (Trigger node)
*   **Credenciales**: Conecta tu cuenta de Gmail.
*   **Label**: Selecciona `INBOX` (o la etiqueta que prefieras).
*   **Format**: Déjalo en `Resolved` para que los datos vengan legibles.

### 2. IF (Condition node)
Aquí vamos a filtrar solo los asuntos que te interesan.
*   **Conditions**:
    *   **Value 1**: Haz clic en *Expression* y escribe `{{ $json.subject.toLowerCase() }}` (convierte el asunto a minúsculas para que no importe si viene con mayúsculas o minúsculas).
    *   **Operation**: `Contains`
    *   **Value 2**: `propuesta`
*   **Agrega otra condición (OR)**:
    *   **Value 1**: `{{ $json.subject.toLowerCase() }}`
    *   **Operation**: `Contains`
    *   **Value 2**: `cotizacion` (sin tilde para abarcar más posibilidades, o con tilde si eres estricto).

*Si el asunto contiene alguna de esas palabras, el flujo irá por la rama "True". Si no, por la "False".*

### 3. Notion (Action node - Rama True)
*   **Credenciales**: Conecta tu integration de Notion (necesitas haberla creado en Notion y haber compartido tu base de datos con ella).
*   **Resource**: `Database Page`
*   **Operation**: `Create`
*   **Database ID**: Selecciona la base de datos de Notion donde quieres guardar las propuestas.
*   **Properties**: Mapea las columnas de tu base de Notion con los datos del email:
    *   **Título (Name)**: `{{ $json.subject }}`
    *   **Email del remitente**: `{{ $json.from.text }}`
    *   **Estado** (si tienes un select): Puedes ponerle por defecto "Nuevo" o "Pendiente de revisar".
*   **Content (Page Body)**: Aquí puedes poner el cuerpo del email usando `{{ $json.text }}` o `{{ $json.html }}` para que tengas todo el contexto dentro de la página de Notion.

### 4. Slack (Action node - Rama True)
*   **Credenciales**: Conecta tu app de Slack (necesitas un Bot Token con permisos de `chat:write`).
*   **Resource**: `Message`
*   **Operation**: `Send`
*   **Channel**: Selecciona el canal donde quieres que llegue la alerta (ej. `#ventas` o `#notificaciones`).
*   **Text**: Arma un mensaje claro usando expresiones. Por ejemplo:
    ```text
    🚨 *¡Nueva propuesta recibida!*
    *De:* {{ $json.from.text }}
    *Asunto:* {{ $json.subject }}
    ¡Revisa los detalles en Notion!
    ```

### 5. No Operation, do nothing (Action node - Rama False)
*   Simplemente arrastra este nodo a la rama "False" del IF. Esto es solo para que N8N no marque la rama con un error visualmente, significa "si no tiene las palabras, no hago nada y termino".

---

**💡 Tip de productividad:** 
Si quieres que el mensaje de Slack incluya un enlace directo a la página que se acaba de crear en Notion, puedes usar el ID de la página que devuelve el nodo de Notion. La URL sería algo como `https://www.notion.so/{{ $json.id.replace(/-/g, '') }}`. Así, desde Slack, haces clic y vas directo al registro.

¿Tienes ya creada la base de datos en Notion y la integration, o necesitas ayuda con ese paso también?