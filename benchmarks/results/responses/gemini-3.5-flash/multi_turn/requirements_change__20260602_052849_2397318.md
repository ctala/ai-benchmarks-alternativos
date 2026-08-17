# Gemini 3.5 Flash — multi_turn/requirements_change

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 7.31 | quality: 9.2
- latency_total: 12.155s | tokens_per_second: 168.2
- input_tokens: 202 | output_tokens: 2044
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profundiza en la automatización de negocios al sugerir Notion y Slack, ofreciendo una guía detallada y clara para implementar el flujo de trabajo, lo que la hace altamente útil para un emprendedor.

## Respuesta completa

¡Excelente cambio! Pasar de Google Sheets a **Notion** como base de datos (CRM) y añadir alertas en **Slack** es una automatización de nivel profesional para cualquier negocio. Además, filtrar por palabras clave te ahorrará mucho ruido.

Aquí tienes el diseño del nuevo workflow y un **truco de optimización**: en lugar de usar un nodo "Filter" después de recibir los correos, configuraremos el filtro directamente dentro del disparador de Gmail. Esto evitará que consumas ejecuciones de n8n innecesarias con correos que no te interesan.

---

### Estructura del Workflow en n8n

El flujo quedará así:
`Gmail Trigger (con filtro integrado)` ➔ `Notion (Crear página)` ➔ `Slack (Enviar mensaje)`

---

### Configuración paso a paso

#### 1. Gmail Trigger (Disparador)
Este nodo se activará solo cuando llegue un correo que cumpla con tus condiciones.
*   **Trigger On:** `Email Received`
*   **Filters:**
    *   **Query:** `subject:(propuesta OR cotización OR cotizacion)`
    *(Esto busca en el asunto cualquiera de las tres palabras, ignorando mayúsculas/minúsculas y acentos gracias al motor de búsqueda de Google).*

#### 2. Notion (Crear página en Base de Datos)
Antes de configurar este nodo, ve a Notion, crea una base de datos (tabla) con estas columnas:
*   `Nombre` (tipo Title) -> Para el Asunto del correo.
*   `Remitente` (tipo Text) -> Para el Nombre del remitente.
*   `Email` (tipo Email) -> Para la dirección de correo.
*   `Fecha` (tipo Date) -> Para la fecha de recepción.

*En n8n, configura el nodo de Notion:*
*   **Resource:** `Database Page`
*   **Operation:** `Create`
*   **Database:** Selecciona tu base de datos (recuerda compartir la base de datos con tu integración de Notion).
*   **Properties:** Mapea los campos usando las expresiones de n8n:
    *   *Nombre:* `{{ $json.subject }}`
    *   *Remitente:* `{{ $json.from.name }}`
    *   *Email:* `{{ $json.from.value[0].address }}`
    *   *Fecha:* `{{ $json.date }}`

#### 3. Slack (Enviar Mensaje)
Para notificarte al instante en el canal que elijas (ej. `#ventas` o `#general`).
*   **Resource:** `Message`
*   **Operation:** `Post`
*   **Channel:** Elige tu canal (ej. `#notificaciones`).
*   **Text:** Puedes usar formato Markdown para que se vea genial:
    ```text
    🚨 *¡Nueva oportunidad recibida!* 🚨
    Subject: *{{ $json.subject }}*
    Remitente: {{ $json.from.name }} (<mailto:{{ $json.from.value[0].address }}|{{ $json.from.value[0].address }}>)
    
    📥 Ya ha sido registrado automáticamente en Notion.
    ```

---

### Código para importar a n8n

Puedes copiar este código JSON y pegarlo directamente en tu lienzo de n8n (Ctrl+V o Cmd+V) para que se creen los nodos automáticamente. Solo tendrás que conectar tus cuentas de Gmail, Notion y Slack.

```json
{
  "meta": {
    "instanceId": "identificador_de_tu_instancia"
  },
  "nodes": [
    {
      "parameters": {
        "pollTimes": {
          "item": [
            {
              "mode": "everyMinute"
            }
          ]
        },
        "filters": {
          "q": "subject:(propuesta OR cotización OR cotizacion)"
        },
        "placeholder": ""
      },
      "id": "a9b7c6d5-e4f3-4a2b-9c8d-7e6f5a4b3c2d",
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1.1,
      "position": [250, 360],
      "credentials": {
        "gmailOAuth2": {
          "id": "tu_credencial_de_gmail",
          "name": "Gmail Account"
        }
      }
    },
    {
      "parameters": {
        "resource": "databasePage",
        "databaseId": {
          "__rl": true,
          "mode": "list",
          "value": ""
        },
        "propertiesUi": {
          "propertyValues": [
            {
              "key": "Nombre",
              "title": "={{ $json.subject }}"
            },
            {
              "key": "Remitente",
              "richText": {
                "text": [
                  {
                    "text": {
                      "content": "={{