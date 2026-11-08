# GLM-5.1 — multi_turn/requirements_change

- model_id: `z-ai/glm-5.1`
- success: True  | final: 4.36 | quality: 4.0
- latency_total: 27.786s | tokens_per_second: 55.8
- input_tokens: 235 | output_tokens: 1550

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

¡Me parece excelente el giro! Es muy común ajustar los workflows a medida que vas puliendo tu proceso de negocio. Integrar Notion y Slack le da un toque mucho más profesional y automatizado a tu gestión.

Aquí tienes el paso a paso para construir este nuevo workflow en n8n:

### Estructura del Workflow
**Gmail Trigger** ➡️ **If (Filtro)** ➡️ **Notion (Crear Registro)** ➡️ **Slack (Notificación)**

### Configuración nodo por nodo:

**1. Gmail Trigger**
*   **Acción:** `On Email`
*   **Configuración:** Conecta tu cuenta de Gmail. Puedes dejar el filtro vacío para que evalúe todos los correos que entran, o si usas una etiqueta específica en Gmail, puedes ponerla aquí para que el trigger sea más rápido.

**2. If (Filtro de asunto)**
*   **Condición:** Vamos a usar la lógica "OR" (O).
*   **Value 1:** Arrastra aquí el campo `Subject` (Asunto) que viene de Gmail. En n8n suele ser `{{$json["subject"]}}`.
*   **Operation:** `Contains` (Contiene)
*   **Value 2:** Escribe `propuesta`
*   *(Haz clic en "Add condition" y cambia el AND por OR)*
*   **Value 1:** `{{$json["subject"]}}`
*   **Operation:** `Contains`
*   **Value 2:** Escribe `cotizacion`
*   *Nota:* Todo lo que sea true (verdad) saldrá por el output "True" y continuará el flujo.

**3. Notion (Crear registro en base de datos)**
*   **Acción:** `Create Database Item`
*   **Credential:** Conecta tu cuenta de Notion (necesitas darle permisos a n8n para acceder a la base de datos específica).
*   **Database ID:** Selecciona la base de datos de Notion donde quieres guardar los contactos (ej. "CRM" o "Leads").
*   **Mapeo de campos (Properties):**
    *   *Nombre:* Puedes usar el nombre del remitente `{{$json["from"]["value"][0]["name"]}}`
    *   *Email:* `{{$json["from"]["value"][0]["address"]}}`
    *   *Asunto:* `{{$json["subject"]}}`
    *   *Fecha:* `{{$json["date"]}}`
    *(Los nombres de las propiedades deben coincidir exactamente con las columnas que creaste en tu Notion).*

**4. Slack (Notificación)**
*   **Acción:** `Send Message`
*   **Credential:** Conecta tu bot o workspace de Slack.
*   **Channel:** Selecciona el canal donde quieres recibir la alerta (ej. `#ventas` o tu canal privado).
*   **Text:** Puedes armar un mensaje dinámico. Por ejemplo:
    `🚨 ¡Nueva oportunidad de venta! 🚨\nHas recibido una propuesta/cotización de: {{$json["from"]["value"][0]["address"]}}\nAsunto: {{$json["subject"]}}\nRevisa tu correo o Notion para más detalles.`

### Tip extra para emprendedores:
En el nodo de Slack, el `{{$json...}}` toma los datos del último nodo ejecutado (Notion). Si te da error de variable vacía, cambia la expresión para que lea directamente del Gmail Trigger usando el editor de expresiones de n8n (el icono del engranaje o `={{ $('Gmail Trigger').item.json.subject }}`).

¿Te gustaría que te genere el código JSON de este workflow completo para que solo lo copies y pegues directamente en tu lienzo de n8n y te ahorres armarlo a mano?