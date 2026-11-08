# GLM 5.3 Flash — multi_turn/requirements_change

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 4.53 | quality: 4.0
- latency_total: 58.207s | tokens_per_second: 71.1
- input_tokens: 235 | output_tokens: 4138

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

Bien, con esos cambios el workflow queda asi:

```
Gmail Trigger → Code (parsear remitente) → Notion
                                         → Slack
```

**1. Gmail Trigger**
- Simplify: ON
- En **Filters → Search** poné: `subject:(propuesta OR cotizacion)`
- Esto filtra a nivel de Gmail y te ahorra un nodo Filter. Gmail search no distingue mayúsculas/minúsculas. Ojo: si te pueden escribir "cotización" con acento, incluí ambas variantes: `subject:(propuesta OR cotizacion OR cotización)`

*Si preferís el filtro visible dentro de n8n (por ejemplo para contar los descartados), usá un nodo Filter con dos condiciones unidas por OR: Subject contains "propuesta", Subject contains "cotizacion".*

**2. Code node (Parsear Remitente)**

El campo From llega tipo `"Juan Perez" <juan@empresa.com>`, así que conviene separarlo:

```javascript
const from = $json.From || '';
const match = from.match(/^"?([^"<]*)"?\s*<(.+)>$/);

return [{
  json: {
    nombre: match ? match[1].trim() : from,
    email: match ? match[2] : from,
    asunto: $json.Subject || '',
    fecha: new Date($json.Date || Date.now()).toISOString(),
  }
}];
```

*(Si tu versión del trigger trae los campos dentro de `headers`, ajustá las referencias: `$json.headers.From`, etc.)*

**3. Notion node**
- Resource: Database Page / Operation: Create
- Seleccioná tu base de datos y mapeá las propiedades:
  - Nombre (Title) → `{{ $json.nombre }}`
  - Email (Email) → `{{ $json.email }}`
  - Asunto (Rich Text) → `{{ $json.asunto }}`
  - Fecha (Date) → `{{ $json.fecha }}`

Importante: en Notion tenés que compartir la base de datos con tu integración (⋯ → Connections), si no, el nodo no la encuentra.

**4. Slack node**
- Operation: Send Message
- Channel: el que uses (ej. `#ventas`)
- Text: `📬 Nueva propuesta de {{ $json.nombre }} ({{ $json.email }}): "{{ $json.asunto }}"`

Notion y Slack van conectados en paralelo desde la salida del Code node, así uno no bloquea al otro.

**Credenciales necesarias:** OAuth de Gmail, API token de Notion, y una app de Slack con permiso `chat:write` para el canal.

¿Ya tenés la base de Notion creada con esas propiedades, o querés que te arme la estructura sugerida de la database primero?