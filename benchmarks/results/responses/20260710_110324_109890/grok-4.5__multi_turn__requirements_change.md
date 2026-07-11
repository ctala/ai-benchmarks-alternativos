# Grok 4.5 — multi_turn/requirements_change

- model_id: `x-ai/grok-4.5`
- success: True  | final: 4.72 | quality: 4.72
- latency_total: 16.195s | tokens_per_second: 96.7
- input_tokens: 425 | output_tokens: 1566
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos de guardar los datos en un Google Sheet, sino que introduce Notion y Slack, lo que la hace irrelevante para la tarea original.

## Respuesta completa

Perfecto, actualizamos el workflow. Queda así:

```
Gmail Trigger → IF (filtro asunto) → Function (extraer datos) → Notion (crear página) → Slack (notificación)
```

---

## 1. Gmail Trigger

- **Node**: `Gmail Trigger`
- **Event**: `Message Received`
- **Simple / Poll**: cada X minutos (o push si tienes OAuth bien configurado)
- **Options**:
  - Filtra en Gmail si quieres: `subject:(propuesta OR cotizacion)`  
    (opcional; el filtro real lo hacemos en el IF por si falla el query de Gmail)

Conecta tu cuenta de Gmail (OAuth2).

---

## 2. IF — filtrar por asunto

- **Node**: `IF`
- **Condición** (OR):

| Campo | Operación | Valor |
|--------|-----------|--------|
| `{{ $json.subject }}` | contains | `propuesta` |
| `{{ $json.subject }}` | contains | `cotizacion` |

- Marca **Case Sensitive = false** (o normaliza a minúsculas en un Set previo).
- Rama **true** → sigue el flujo.
- Rama **false** → no hagas nada (o un NoOp).

Si el asunto llega con acentos (`cotización`), puedes usar dos condiciones extra o normalizar el subject en un Function antes del IF.

---

## 3. Function — extraer datos del remitente

- **Node**: `Code` (o `Function` en versiones antiguas)

```javascript
// Entrada típica del Gmail Trigger
const item = $input.first().json;

// "Name <email@domain.com>" o solo el email
const fromRaw = item.from || item.headers?.from || '';
const match = fromRaw.match(/^(?:"?([^"]*)"?\s)?<?([^>]+@[^>]+)>?$/);

const nombre = (match && match[1] ? match[1].trim() : '') || 'Sin nombre';
const email = (match && match[2] ? match[2].trim() : fromRaw).toLowerCase();

return [{
  json: {
    nombre,
    email,
    asunto: item.subject || '',
    fecha: item.date || item.internalDate || new Date().toISOString(),
    snippet: item.snippet || '',
    messageId: item.id || item.messageId || '',
    threadId: item.threadId || '',
  }
}];
```

Ajusta los paths (`from`, `subject`, etc.) según lo que devuelva tu Gmail Trigger en la pestaña de Output.

---

## 4. Notion — guardar el registro

- **Node**: `Notion`
- **Resource**: `Page` (o `Database Page`)
- **Operation**: `Create`
- **Database**: elige tu base de Notion (debe estar compartida con la integración de Notion)

**Mapeo de propiedades** (ejemplo; adapta a tus columnas):

| Propiedad Notion | Tipo | Valor |
|------------------|------|--------|
| Nombre (Title) | Title | `{{ $json.nombre }}` |
| Email | Email / Text | `{{ $json.email }}` |
| Asunto | Text | `{{ $json.asunto }}` |
| Fecha | Date | `{{ $json.fecha }}` |
| Snippet | Text | `{{ $json.snippet }}` |
| Message ID | Text | `{{ $json.messageId }}` |

**Requisitos en Notion**:
1. Crea una integración en [notion.so/my-integrations](https://www.notion.so/my-integrations).
2. Comparte la base de datos con esa integración.
3. En N8N usa la credential de Notion (Internal Integration Token).

---

## 5. Slack — notificación

- **Node**: `Slack`
- **Resource**: `Message`
- **Operation**: `Post`
- **Channel**: el canal que quieras (ej. `#leads` o `#propuestas`)
- **Text** (ejemplo):

```
Nuevo email de propuesta/cotización

• Remitente: {{ $json.nombre }} <{{ $json.email }}>
• Asunto: {{ $json.asunto }}
• Fecha: {{ $json.fecha }}
• Vista previa: {{ $json.snippet }}
```

Si usas Block Kit, puedes armar un mensaje más legible; el texto simple suele bastar.

Credential: Bot Token o OAuth de Slack, con permiso de escribir en el canal.

---

## Orden final de nodos

1. **Gmail Trigger**  
2. **IF** (asunto contiene `propuesta` **OR** `cotizacion`)  
3. **Code** (extraer nombre, email, etc.)  
4. **Notion** (Create Database Page)  
5. **Slack** (Post Message)

Todo en la rama **true** del IF, en serie: Notion y luego Slack (o en paralelo con un Merge si prefieres independencia).

---

## Tips prácticos

| Tema | Recomendación |
|------|----------------|
| Acentos | Filtra también `cotización` / `propuesta` o normaliza: `$json.subject.toLowerCase().normalize('NFD').replace(/\p{Diacritic}/gu,'')` |
| Duplicados | Guarda `messageId` en Notion y, si quieres, un IF previo que busque si ya existe |
| Errores | Activa “Continue On Fail” en Notion/Slack y un Error Trigger o notificación aparte |
| Pruebas | Desactiva el Trigger, usa “Execute Workflow” con un email de prueba pinneado |
| Rate limits | Gmail/Notion/Slack: no pongas el poll demasiado agresivo |

---

## Variante opcional: filtro en Gmail

En el Gmail Trigger, en **Filters / Query**:

```text
subject:(propuesta OR cotizacion OR cotización)
```

Así reduces volumen; el IF del workflow sigue siendo la red de seguridad.

---

Si quieres, en el siguiente mensaje te puedo pasar:
1. el **JSON exportable** del workflow para importar en N8N, o  
2. el mapeo exacto de propiedades según los nombres de columnas de tu base de Notion.

Dime cómo se llaman las propiedades de tu database de Notion y el canal de Slack, y lo dejamos listo para copiar/pegar.