# Claude Sonnet 4.6 (suscripción) — multi_turn/requirements_change

- model_id: `claude-sonnet-4-6`
- success: True  | final: 5.11 | quality: 4.64
- latency_total: 23.596s | tokens_per_second: 52.4
- input_tokens: 3 | output_tokens: 1237
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de leer emails de Gmail y guardar datos en un Google Sheet, en su lugar, introduce Notion y Slack, lo que reduce su relevancia y utilidad práctica.

## Respuesta completa

# Workflow N8N: Gmail → Notion + Slack (con filtro)

Aquí está el diseño completo con los cambios que pediste:

---

## Arquitectura del workflow

```
Gmail Trigger → IF (filtro asunto) → Notion + Slack (en paralelo)
                      ↓ (no match)
                    Stop
```

---

## Nodo 1: Gmail Trigger

- **Node**: `Gmail Trigger`
- **Event**: `Message Received`
- **Poll interval**: cada 1 minuto (o usar Push si tienes OAuth configurado)
- **Filters**: dejar vacío (el filtro lo hacemos en el siguiente nodo para tener más control)

---

## Nodo 2: IF — Filtro de asunto

- **Node**: `IF`
- **Condición**:
  - **Value 1**: `{{ $json.subject }}`
  - **Operation**: `Regex`
  - **Value 2**: `(?i)(propuesta|cotizacion|cotización)`

> El `(?i)` hace el match case-insensitive, así captura "Propuesta", "PROPUESTA", etc.

**Si es TRUE** → continúa al siguiente nodo  
**Si es FALSE** → el workflow termina sin hacer nada

---

## Nodo 3: Set — Normalizar datos

Antes de enviar a Notion y Slack, limpia los datos en un nodo `Set`:

| Campo | Valor |
|---|---|
| `nombre_remitente` | `{{ $json.from.name \|\| $json.from.email }}` |
| `email_remitente` | `{{ $json.from.email }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $now.toISO() }}` |
| `preview` | `{{ $json.snippet }}` (primeros 200 chars del body) |

---

## Nodo 4a: Notion

- **Node**: `Notion`
- **Operation**: `Create a database item`
- **Database ID**: el ID de tu base de datos en Notion (está en la URL: `notion.so/.../{DATABASE_ID}?v=...`)
- **Properties a mapear**:

```
Nombre        → nombre_remitente
Email         → email_remitente  
Asunto        → asunto
Fecha         → fecha
Preview       → preview
Status        → "Nuevo" (valor fijo)
```

> ⚠️ Las propiedades deben existir en tu base de datos de Notion con los tipos correctos (Title, Email, Text, Date, Text, Select).

---

## Nodo 4b: Slack

Conecta este nodo **en paralelo** con Notion (ambos reciben el output del nodo `Set`):

- **Node**: `Slack`
- **Operation**: `Send a message`
- **Channel**: `#propuestas` (o el canal que uses)
- **Message**:

```
🔔 *Nueva propuesta recibida*

*De:* {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

{{ $json.preview }}
```

---

## Cómo conectar los nodos 4a y 4b en paralelo

En N8N, desde el nodo `Set` arrastra **dos conexiones**: una hacia Notion y otra hacia Slack. N8N los ejecuta en secuencia por defecto, pero funcionará correctamente. Si necesitas ejecución paralela real, usa un nodo `Split In Batches` o simplemente acepta la ejecución secuencial (es suficientemente rápida).

---

## Credenciales que necesitas configurar

| Servicio | Tipo de auth |
|---|---|
| Gmail | OAuth2 (Google) |
| Notion | API Integration Token — en notion.so/my-integrations |
| Slack | OAuth2 o Webhook URL |

> En Notion, además de crear el Integration Token, debes **compartir la base de datos con tu integration** (botón "Connect to" dentro de la página de Notion).

---

## Tip extra

Si quieres evitar duplicados (por si el trigger relee emails), agrega un nodo `IF` al final que verifique si el email ya existe en Notion antes de crearlo, usando el nodo `Notion → Get Database Items` con filtro por email.

¿Quieres que te muestre cómo exportar este workflow como JSON para importarlo directo en N8N?