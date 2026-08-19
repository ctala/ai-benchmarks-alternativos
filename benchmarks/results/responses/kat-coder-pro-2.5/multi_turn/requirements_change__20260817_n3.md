# KAT Coder Pro v2.5 — multi_turn/requirements_change

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 6.04 | quality: 6.0
- latency_total: 5.72s | tokens_per_second: 94.4
- input_tokens: 233 | output_tokens: 540

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



Entendido, workflow actualizado. La estructura seria:

**Gmail Trigger** → **IF (filtro asunto)** → **Notion (guardar)** + **Slack (notificar)**

Aca te detallo cada nodo:

### 1. Gmail Trigger
- **Evento**: `messageAdded`
- **Filtro de labels**: `INBOX`
- **Polling**: cada 1-5 minutos (o webhook si lo configuras)

### 2. IF Node (filtro)
Condicion para pasar al siguiente paso:
```javascript
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}
```

### 3. Notion Node (crear pagina)
- **Operacion**: `Create a page`
- **Parent**: tu database ID de Notion
- **Properties a mapear**:
  - `Remitente` → `{{ $json.from }}`
  - `Email` → `{{ $json.email }}`
  - `Asunto` → `{{ $json.subject }}`
  - `Fecha` → `{{ $json.date }}`
  - `Snippet` → `{{ $json.snippet }}`

### 4. Slack Node (notificacion)
- **Operacion**: `Post Message`
- **Canal**: el que elijas (ej: `#propuestas`)
- **Mensaje**:
```
📩 Nueva propuesta/cotización recibida
De: {{ $json.from }}
Asunto: {{ $json.subject }}
Fecha: {{ $json.date }}
```

### Consideraciones de credenciales
Necesitas configurar 4 credenciales en N8N:
- **Gmail**: OAuth2 (Google Cloud Console)
- **Notion**: Internal Integration Token (notion.so/my-integrations)
- **Slack**: Bot Token (slack apps)

Quieres que te ayude con la configuracion de alguna credencial en particular, o prefieres que te genere el JSON del workflow para importarlo directo?