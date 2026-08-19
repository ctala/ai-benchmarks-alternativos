# Tencent Hy3 — multi_turn/requirements_change

- model_id: `tencent/hy3`
- success: True  | final: 7.36 | quality: 8.0
- latency_total: 41.107s | tokens_per_second: 81.3
- input_tokens: 260 | output_tokens: 3343

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

¡Cambio de planes perfecto! N8N es muy flexible para eso. 

Para lograr lo que necesitas, el flujo quedaría con **4 nodos** en cadena:

1. **Gmail Trigger**: Escucha los correos nuevos.
2. **IF (Filtro)**: Solo deja pasar los que tienen "propuesta" o "cotizacion" en el asunto.
3. **Notion**: Crea una página en tu base de datos con los datos del remitente.
4. **Slack**: Envía la notificación al canal que elijas.

---

### 🛠️ Configuración paso a paso

**1. Gmail Trigger**
*   **Event**: `Message Received`
*   **Simplify**: `True` (esto te da acceso directo a `subject` y `from` sin tener que escarbar en el JSON crudo).

**2. IF (Filtrar Asunto)**
*   **Combinator**: `OR` (Alguna de las condiciones)
*   **Condición 1**: `{{ $json.subject }}` *contains* `propuesta`
*   **Condición 2**: `{{ $json.subject }}` *contains* `cotizacion`
*(Tip: En las opciones del nodo desactiva "Case Sensitive" para que detecte también "Propuesta" o "COTIZACION").*

**3. Notion**
*   **Resource**: `Database Page`
*   **Operation**: `Create`
*   **Database ID**: Pega el ID de tu base de datos de Notion.
*   **Properties** (mapeo de campos):
    *   *Título (Title)*: `{{ $json.from }}` (ej. "Juan Perez <juan@empresa.com>")
    *   *Asunto (Text)*: `{{ $json.subject }}`
    *   *Fecha (Date)*: `{{ $json.internalDate }}` o `{{ $now }}`

**4. Slack**
*   **Resource**: `Message`
*   **Channel**: El canal donde quieres recibir alertas (ej. `#ventas`).
*   **Text**: `📩 Nuevo lead filtrado: "{{ $json.subject }}" de {{ $json.from }}`

---

### ⚡ Importa el workflow directamente (JSON)
Para ahorrarte el trabajo manual, copia este código, ve a N8N -> **Menu (arriba izquierda) -> Import from File / Paste**, y pega esto (recuerda luego poner tu Database ID de Notion y conectar tus credenciales):

```json
{
  "nodes": [
    {
      "parameters": { "event": "messageReceived", "simplify": true },
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1,
      "position": [-400, 0]
    },
    {
      "parameters": {
        "conditions": {
          "options": { "caseSensitive": false },
          "combinator": "or",
          "conditions": [
            { "leftValue": "={{ $json.subject }}", "rightValue": "propuesta", "operator": "contains" },
            { "leftValue": "={{ $json.subject }}", "rightValue": "cotizacion", "operator": "contains" }
          ]
        }
      },
      "name": "IF (Filtrar Asunto)",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [-200, 0]
    },
    {
      "parameters": {
        "resource": "databasePage",
        "operation": "create",
        "databaseId": "PEG_AQUI_TU_NOTION_DB_ID",
        "propertiesUi": {
          "propertyValues": [
            { "key": "Nombre", "value": "={{ $json.from }}" },
            { "key": "Asunto", "value": "={{ $json.subject }}" },
            { "key": "Fecha", "value": "={{ $now }}" }
          ]
        }
      },
      "name": "Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 1,
      "position": [0, -100]
    },
    {
      "parameters": {
        "channel": "#tu-canal",
        "text": "📩 Nuevo email filtrado: {{$json.subject}} de {{$json.from}}"
      },
      "name": "Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 1,
      "position": [0, 100]
    }
  ],
  "connections": {
    "Gmail Trigger": { "main": [[ { "node": "IF (Filtrar Asunto)", "type": "main", "index": 0 } ]] },
    "IF (Filtrar Asunto)": { "main": [[ 
      { "node": "Notion", "type": "main", "index": 0 },
      { "node": "Slack", "type": "main", "index": 0 }
    ]] }
  }
}
```

---

### 💡 Un tip extra para emprendedores:
El campo `from` de Gmail viene generalmente como `"Nombre del Cliente <email@cliente.com>"`. Si quieres separar el **nombre** y el **correo electrónico** en dos columnas distintas de Notion, puedes insertar un nodo **"Set"** entre el IF y Notion, y usar estas expresiones:
*   **Email limpio**: `{{ $json.from.match(/<(.*)>/) ? $json.from.match(/<(.*)>/)[1] : $json.from }}`
*   **Nombre**: `{{ $json.from.split('<')[0].trim() }}`

¿Quieres que te arme el workflow ya con ese nodo "Set" para tener Notion súper ordenado?