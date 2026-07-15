# Claude Fable 5 — multi_turn/requirements_change

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 3.89 | quality: 4.0
- latency_total: 17.378s | tokens_per_second: 59.4
- input_tokens: 363 | output_tokens: 1033
- judge_score: 3.8 | justificación: 

## Respuesta completa

Buen cambio, queda un workflow más útil. Esta sería la estructura:

## Flujo del workflow

**Gmail Trigger → IF (filtro) → Notion → Slack**

### 1. Gmail Trigger
- Evento: "Message Received"
- Puedes dejar que traiga todos los emails, porque el filtrado lo haremos en el siguiente nodo. Aunque, si prefieres optimizar, puedes usar el campo **Filters → Search** con la query de Gmail: `subject:(propuesta OR cotizacion)` y así te ahorras el nodo IF.

### 2. IF Node (si no filtras en el trigger)
- Condición tipo **String** con dos reglas conectadas por **OR**:
  - `{{ $json.subject.toLowerCase() }}` → contains → `propuesta`
  - `{{ $json.subject.toLowerCase() }}` → contains → `cotizacion`
- El `.toLowerCase()` es importante para que funcione sin importar mayúsculas.
- Tip: si quieres cubrir "cotización" con tilde, agrega una tercera condición con esa variante.

### 3. Notion Node
- Resource: **Database Page** → Operation: **Create**
- Antes necesitas crear una base de datos en Notion con estas propiedades (por ejemplo):
  - **Nombre** (Title) → nombre del remitente
  - **Email** (Email) → dirección del remitente
  - **Asunto** (Text)
  - **Fecha** (Date)
- Mapeas cada propiedad con expresiones como `{{ $json.from.value[0].name }}` y `{{ $json.from.value[0].address }}` (la estructura exacta depende de si el trigger devuelve el formato "simplified" o completo; te recomiendo ejecutar el trigger una vez y revisar el output).

### 4. Slack Node
- Operation: **Send Message**
- Canal: el que elijas
- Mensaje de ejemplo:
```
📩 Nueva propuesta/cotización recibida
De: {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})
Asunto: {{ $json.subject }}
```

## Credenciales que necesitas configurar
1. **Gmail**: OAuth2 (requiere proyecto en Google Cloud Console con la API de Gmail habilitada)
2. **Notion**: crear una integración en notion.so/my-integrations y **compartir la base de datos con la integración** (este paso se olvida siempre y es la causa #1 de errores)
3. **Slack**: crear una app en Slack con el scope `chat:write` e invitar el bot al canal

¿Quieres que te pase el JSON del workflow completo para que lo importes directamente en N8N?