# Kimi K3 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 5.21 | quality: 6.0
- latency_total: 73.855s | tokens_per_second: 38.9
- input_tokens: 374 | output_tokens: 2875

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

Buena combinacion, ese flujo es muy util para seguimiento comercial. La estructura seria:

**Gmail Trigger → Code (extraer datos) → Notion → Slack**

Te detallo cada nodo:

---

### 1. Gmail Trigger

- **Event**: Message Received
- **Poll Times**: cada minuto (o el intervalo que prefieras)
- **Filters → Search**: `subject:propuesta OR subject:cotizacion`

**Ventaja clave**: al filtrar en el trigger con la busqueda de Gmail, no gastas ejecuciones con emails irrelevantes. Ademas, la busqueda de Gmail es case-insensitive, asi que "Propuesta", "PROPUESTA" o "propuesta" matchean igual.

> Alternativa: si prefieres ver el filtro en el canvas, usa un nodo **IF** con la expresion:
> ```
> {{$json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion')}}
> ```

---

### 2. Code node (extraer datos del remitente)

En modo "Run Once for Each Item":

```javascript
const from = $json.from || $json.From || "";
const match = from.match(/^(.*?)\s*<(.+?)>$/);

return [{
  json: {
    nombre: match ? match[1].replace(/"/g, '').trim() : from.trim(),
    email: match ? match[2].trim() : from.trim(),
    asunto: $json.subject || $json.Subject,
    fecha: $json.date || $json.Date,
    snippet: $json.snippet || ""
  }
}];
```

Esto separa el nombre y el email cuando vienen en formato `"Juan Perez <juan@empresa.com>"`.

---

### 3. Notion node

- **Resource**: Database Page
- **Operation**: Create
- **Database**: selecciona tu base de datos
- **Properties** (mapeo sugerido):
  - `Nombre` (title): `{{ $json.nombre }}`
  - `Email` (email): `{{ $json.email }}`
  - `Asunto` (rich text): `{{ $json.asunto }}`
  - `Fecha` (date): `{{ $json.fecha }}`

**Requisito previo**: crea la base de datos en Notion con esas propiedades y **compartela con tu integracion** (boton "..." → Connections → agregar tu integracion). Si no, no aparecera en el dropdown de N8N.

---

### 4. Slack node

- **Resource**: Message
- **Operation**: Post
- **Channel**: el que uses para ventas/leads
- **Text**:

```
📩 *Nuevo email de propuesta/cotizacion*
*De:* {{ $json.nombre }} ({{ $json.email }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
```

---

### Checklist final

1. Credenciales configuradas: Gmail (OAuth2), Notion (integration token), Slack
2. Probar con "Test workflow" enviandote un email de prueba con "cotizacion" en el asunto
3. Verificar que la fila se creo en Notion y llego el mensaje a Slack
4. **Activar el workflow** (switch arriba a la derecha)

Quieres que te genere el JSON del workflow completo para importarlo directamente en tu instancia de N8N?