# Nemotron 3 Ultra 550B — multi_turn/requirements_change

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 5.25 | quality: 5.2
- latency_total: 22.937s | tokens_per_second: 32.6
- input_tokens: 248 | output_tokens: 748

## Respuesta completa

Entendido. El flujo quedaría así:

**Nodos necesarios:**
1. **Gmail Trigger** (polling o webhook)
2. **IF** (filtro por asunto)
3. **Notion** (Create Page en tu base de datos)
4. **Slack** (Post Message a canal/DM)

---

### 1. Gmail Trigger
- **Event**: `Message Received`  
- **Options**: `Include Attachments` = false (si no los necesitas)  
- **Poll Time**: cada 5 min (o webhook si tienes dominio verificado)

---

### 2. IF Node (Filtro)
**Mode**: `Boolean`  
**Conditions** (OR logic):
```javascript
// Expression 1
{{ $json.subject.toLowerCase().includes('propuesta') }}

// Expression 2  
{{ $json.subject.toLowerCase().includes('cotizacion') }}
```
*Conecta **True** → Notion + Slack | **False** → (nada / termina)*

---

### 3. Notion - Create Page
- **Database ID**: tu base de datos de "Leads / Propuestas"
- **Properties mapping**:
  | Property (Notion) | Value (Expression) |
  |-------------------|---------------------|
  | **Nombre / Título** | `{{ $json.from.name || $json.from.email }}` |
  | **Email** | `{{ $json.from.email }}` |
  | **Asunto** | `{{ $json.subject }}` |
  | **Fecha** | `{{ $json.date }}` (type: Date) |
  | **Cuerpo (preview)** | `{{ $json.text?.slice(0, 2000) }}` |
  | **Message ID** | `{{ $json.messageId }}` (útil para dedup) |

---

### 4. Slack - Post Message
- **Channel**: `#propuestas` o tu user ID (DM)
- **Text** (Markdown):
```
📩 *Nueva propuesta/cotización*
*De:* {{ $json.from.name }} (<{{ $json.from.email }}>)
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.date }}
*Ver en Notion:* {{ $notion.page_url }}  // si capturas el output del nodo anterior
```
> Tip: usa **Set** antes de Slack para guardar `{{ $notion.url }}` si Notion lo devuelve, o construye la URL manual si tu DB es pública.

---

### Extras recomendados
- **Deduplicación**: añade un **Function** o **SplitInBatches** + **Notion Search** por `Message ID` antes de crear página.
- **Error handling**: activa *Continue On Fail* en Slack para que no rompa el flujo si falla el webhook.
- **Rate limits**: Gmail Trigger ya respeta cuotas; Notion ~3 req/s, Slack ~1 msg/s — estás bien.

---

¿Quieres que te genere el JSON del workflow para importarlo directo en n8n (Ctrl+V en el canvas)?