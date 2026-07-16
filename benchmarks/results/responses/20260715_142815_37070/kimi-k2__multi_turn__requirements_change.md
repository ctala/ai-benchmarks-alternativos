# Kimi K2 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 4.58 | quality: 4.0
- latency_total: 21.849s | tokens_per_second: 40.1
- input_tokens: 267 | output_tokens: 876
- judge_score: 3.0 | justificación: 

## Respuesta completa

Perfecto, ahora es más completo. Aquí está el workflow actualizado:

## Flujo N8N

```
Gmail Trigger → Filter → Parse Data → Notion → Slack
```

## Configuración paso a paso

### 1. **Gmail Trigger**
- **Trigger event**: Message received
- **Search query** (opcional pero eficiente): `subject:(propuesta OR cotización OR cotizacion)`
- O deja el query vacío y filtras después

### 2. **Filter** (o If node)
```
Condition: {{ $json.subject }}
Operation: contains
Value: propuesta,cotización,cotizacion
```

> **Nota**: Usa "OR" si el nodo lo permite, o haz un filtro con expresión regex: `/propuesta|cotización|cotizacion/i`

### 3. **Code/Set node** (Parse Data)
```javascript
// Extraer datos del remitente
const from = $json.from;
const match = from.match(/(?:"?([^"]*?)"?\s)?<(.+?)>/);

return {
  json: {
    nombre_remitente: match?.[1]?.trim() || from,
    email_remitente: match?.[2] || from,
    asunto: $json.subject,
    fecha: $json.date,
    snippet: $json.snippet,
    id_mensaje: $json.id
  }
};
```

### 4. **Notion** (Create database item)

| Campo Notion | Valor mapeado |
|-------------|---------------|
| Name (título) | `{{ $json.asunto }}` |
| Remitente | `{{ $json.nombre_remitente }}` |
| Email | `{{ $json.email_remitente }}` |
| Fecha | `{{ $json.fecha }}` |
| Estado | "Nuevo" (select) |
| Origen | "Email" |

**Configuración del nodo:**
- **Resource**: Database
- **Operation**: Create a database item
- **Database**: Selecciona tu base de datos de Notion

### 5. **Slack** (Send message)

**Canal**: `#notificaciones` o tu canal preferido

**Mensaje**:
```
📧 Nueva oportunidad de *{{ $json.asunto }}*

De: {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
Fecha: {{ $json.fecha }}

Ver en Notion → {{ $json.url }}  // si quieres, añade otro nodo para obtener la URL
```

---

## Esquema visual

```
┌─────────────┐    ┌─────────┐    ┌───────────┐    ┌────────┐    ┌───────┐
│ Gmail       │───→│ Filter  │───→│ Parse     │───→│Notion  │───→│Slack  │
│ Trigger     │    │ (propuesta│   │ Data      │    │(Create)│    │Notify │
│             │    │ cotizacion)│  │           │    │        │    │       │
└─────────────┘    └─────────┘    └───────────┘    └────────┘    └───────┘
```

---

## Requisitos previos

| Servicio | Configuración |
|----------|---------------|
| **Gmail** | Cuenta conectada en Credentials |
| **Notion** | Integration creada + base de datos compartida |
| **Slack** | App instalada en workspace con permisos `chat:write` |

---

## Mejora opcional: evitar duplicados

Añade un **Notion node** antes de crear, que busque si ya existe el `id_mensaje`. Si existe → no crear.

¿Necesitas que profundice en algún nodo específico o que te dé la expresión exacta para el filtro?