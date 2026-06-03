# Claude Opus 4.8 (suscripción) — multi_turn/requirements_change

- model_id: `claude-opus-4-8`
- success: True  | final: 6.38 | quality: 7.72
- latency_total: 24.86s | tokens_per_second: 68.1
- input_tokens: 2026 | output_tokens: 1693
- judge_score: 4.2 | justificación: 

## Respuesta completa

Buen cambio — Notion + Slack con filtro de asunto es un workflow más útil. Te dejo el diseño completo actualizado.

## Estructura del workflow

```
[Gmail Trigger]
      ↓
[IF / Filter]  ← solo asuntos con "propuesta" o "cotizacion"
      ↓
[Set / Edit Fields]  ← extrae datos del remitente
      ↓
   ┌──┴──┐
   ↓     ↓
[Notion] [Slack]   ← en paralelo
```

---

## Nodo por nodo

### 1. Gmail Trigger
- **Event**: `Message Received`
- **Poll Time**: cada 1 min (o lo que necesites)
- Opcional: en *Filters → Search* podés poner `subject:(propuesta OR cotizacion)` para que Gmail filtre **antes** de traer los emails. Esto ahorra ejecuciones, pero igual conviene el nodo IF como red de seguridad (Gmail search es difuso con tildes/mayúsculas).

### 2. Filter (o IF) — filtro por asunto
Usá el nodo **Filter** si solo querés dejar pasar los que cumplen. Condición (modo *OR*), case-insensitive:

- `{{ $json.subject.toLowerCase() }}` **contains** `propuesta`
- `{{ $json.subject.toLowerCase() }}` **contains** `cotizacion`

> Tip: para cubrir tildes ("cotización"), normalizá con
> `{{ $json.subject.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"") }}`
> así "cotización" y "cotizacion" matchean igual.

### 3. Set / Edit Fields — extraer datos del remitente
El campo `from` de Gmail viene como `"Juan Pérez <juan@empresa.com>"`. Separalo:

| Campo | Valor (expresión) |
|---|---|
| `nombre` | `{{ $json.from.value?.[0]?.name \|\| $json.from.text.split('<')[0].trim() }}` |
| `email` | `{{ $json.from.value?.[0]?.address \|\| $json.from.text.match(/<(.+)>/)?.[1] }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |
| `snippet` | `{{ $json.snippet }}` |

(La estructura exacta depende de la versión del nodo Gmail; revisá el output real con un primer run y ajustá las expresiones.)

### 4. Notion — crear página/fila
- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database**: seleccioná tu base (ej. "Leads / Propuestas")
- Mapeá las propiedades de la base con los campos del paso 3:
  - Title (Name) → `{{ $json.nombre }}`
  - Email → `{{ $json.email }}`
  - Asunto → `{{ $json.asunto }}`
  - Fecha → `{{ $json.fecha }}`

⚠️ Importante: las **propiedades deben existir antes** en la base de Notion, con el **tipo correcto** (Email como tipo Email, Fecha como tipo Date). Notion no las crea solo.

### 5. Slack — notificación
- **Resource**: `Message` → **Operation**: `Send`
- **Channel**: tu canal (ej. `#ventas`)
- **Text**:
  ```
  📩 Nueva *{{ $json.asunto }}* de {{ $json.nombre }} ({{ $json.email }})
  Recibido: {{ $json.fecha }}
  ```

Conectá Notion y Slack **ambos desde el Set node** (dos ramas en paralelo) para que se ejecuten independientes.

---

## Decisiones de credenciales / setup

Para que funcione necesitás conectar 3 credenciales OAuth en N8N: **Gmail**, **Notion** (integración + compartir la base con la integración), y **Slack** (bot token con scope `chat:write`).

¿Querés que profundice en algún punto?

- **Filtro robusto** (regex para variantes: "propuestas", "cotizaciones", "presupuesto")
- **Setup de la integración de Notion** (el paso de compartir la base suele trabar a la gente)
- **El JSON del workflow listo para importar** en N8N

¿Cuál te sirve más?