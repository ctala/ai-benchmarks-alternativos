# GLM 5.2 — multi_turn/requirements_change

- model_id: `z-ai/glm-5.2`
- success: True  | final: 5.86 | quality: 6.32
- latency_total: 28.695s | tokens_per_second: 47.5
- input_tokens: 235 | output_tokens: 1362
- judge_score: 3.2 | justificación: 

## Respuesta completa

¡Entendido! Excelente cambio. Notion es ideal para gestionar este tipo de leads o solicitudes, y la alerta de Slack te mantendrá al día en tiempo real. 

Aquí tienes la nueva estructura del workflow y cómo configurar cada nodo:

### 1. Nodo: Gmail Trigger
*   **Acción:** Se activa cuando llega un correo nuevo.
*   **Configuración:** 
    *   Conecta tu cuenta de Gmail.
    *   En "Label" (Etiqueta), puedes dejar `INBOX` o usar una etiqueta específica si filtras los correos en Gmail primero.
    *   Configura el "Poll Times" (cada cuánto tiempo n8n revisará el correo, ej. cada 1 minuto).

### 2. Nodo: If (Filtro de Asunto)
*   **Acción:** Dejar pasar solo los correos que te interesan.
*   **Configuración:**
    *   **Value 1:** Arrastra el campo `Subject` (Asunto) que viene de Gmail.
    *   **Operation:** `Contains` (Contiene).
    *   **Value 2:** Escribe `propuesta`.
    *   Asegúrate de activar la opción de **"OR"** y agregar una segunda condición:
        *   **Value 1:** `Subject`.
        *   **Operation:** `Contains`.
        *   **Value 2:** Escribe `cotizacion`.
*   *Nota:* La salida "True" (Verdadero) será la que conectemos a los siguientes nodos.

### 3. Nodo: Notion (Crear registro en Base de Datos)
*   **Acción:** Crear una nueva página en una base de datos de Notion.
*   **Configuración:**
    *   Conecta tu cuenta de Notion (necesitarás dar permisos a n8n para acceder a la base de datos específica).
    *   **Database:** Selecciona la base de datos donde quieres guardar los datos (ej. "Propuestas Recibidas").
    *   En las propiedades (Properties), mapea los datos del email:
        *   *Nombre / Título:* Puedes usar el `Subject` del email.
        *   *Email (Texto):* Mapea el campo `From` (o el email limpio).
        *   *Fecha (Date):* Mapea el `Date` del email.
    *   *Tip:* En el contenido de la página de Notion, puedes insertar el cuerpo del email (`Text Content`) para tener todo el contexto.

### 4. Nodo: Slack (Notificación)
*   **Acción:** Enviar un mensaje a un canal de Slack.
*   **Configuración:**
    *   Conecta tu cuenta de Slack (Bot o credenciales de usuario).
    *   **Channel:** Selecciona el canal (ej. `#ventas` o `#notificaciones`).
    *   **Message:** Puedes construir un mensaje dinámico. Ejemplo: 
        `🚨 ¡Nueva propuesta/cotización recibida! \nDe: {{$json["From"]}}\nAsunto: {{$json["Subject"]}}`

**Flujo visual:**
`Gmail Trigger` ➡️ `If (Subject contains propuesta OR cotizacion)` ➡️ (True) ➡️ `Notion` y `Slack` (estos dos últimos pueden ir en paralelo o uno detrás del otro, como prefieras).

¿Quieres que te genere el código JSON de este workflow para que lo importes directamente a tu N8n y solo tengas que conectar las cuentas, o prefieres armarlo paso a paso?