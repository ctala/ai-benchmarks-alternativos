# Tencent Hy4 — multi_turn/requirements_change

- model_id: `tencent/hy4`
- success: True  | final: 5.71 | quality: 6.0
- latency_total: 51.627s | tokens_per_second: 97.2
- input_tokens: 267 | output_tokens: 5018

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

Vale, actualizado. El esquema queda así:

```
Gmail Trigger → Extraer datos (Code) → Filter → Notion → Slack
```

Pongo Notion **antes** de Slack para que el mensaje pueda incluir el link directo a la ficha creada.

---

## 1. Gmail Trigger
- **Evento**: `Message Received`
- **Simple**: `false` (importante: así te llegan `From`, `Subject`, `Date` completos, no solo el `snippet`)
- **Poll**: cada minuto por defecto. Si quieres instantáneo, cambia a *Gmail Watch* con Pub/Sub.

## 2. Code node → `Extraer datos`

Modo **Run Once for All Items**. Hace tres cosas a la vez: normaliza acentos, parsea el remitente y marca el match.

```js
const norm = s => (s || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

return $input.all().map(({ json }) => {
  const asunto = json.Subject || json.subject || '';
  const from   = json.From   || json.from   || '';
  const asuntoNorm = norm(asunto);

  // "Juan Pérez <juan@empresa.com>" → nombre + email por separado
  const m = from.match(/^\s*"?(.+?)"?\s*<([^>]+)>\s*$/);

  return { json: {
    ...json,
    coincide: /propuesta|cotizacion/.test(asuntoNorm),
    nombre:   m ? m[1].trim() : from.trim(),
    email:    m ? m[2].trim() : from.trim(),
    asunto,
    fecha:    json.Date || json.date || new Date().toISOString(),
    gmailId:  json.id,
    gmailUrl: `https://mail.google.com/mail/u/0/#inbox/${json.id}`,
    tipo:     asuntoNorm.includes('propuesta') ? 'Propuesta' : 'Cotización',
  }};
});
```

> 💡 **Detalle que suele romper en español**: el usuario escribió `cotizacion`, pero el 80% de los correos llegan con `cotización`. El `.normalize('NFD')` quita el acento antes de comparar, así ambas versiones pasan. Sin esto, pierdes correos silenciosamente.

## 3. Filter node
- **Combinator**: `and` (una sola condición)
- Condición: `{{ $json.coincide }}` → **is true**

Si prefieres cero código, sustituye los nodos 2 y 3 por un **IF** con `combinator: "or"` y dos `contains` sobre `{{ $json.Subject.toLowerCase() }}`, pero seguirías teniendo el problema del acento y el `From` sin parsear.

## 4. Notion → `Create Database Page`

Crea la database con estas propiedades y mapea así:

| Propiedad Notion | Tipo | Valor en n8n |
|---|---|---|
| Nombre | **Title** | `{{ $json.nombre }}` |
| Email | Email | `{{ $json.email }}` |
| Asunto | Rich text | `{{ $json.asunto }}` |
| Tipo | Select | `{{ $json.tipo }}` *(crea las opciones `Propuesta` y `Cotización`)* |
| Fecha | Date | `{{ $json.fecha }}` |
| Gmail ID | Rich text | `{{ $json.gmailId }}` |
| URL Gmail | URL | `{{ $json.gmailUrl }}` |

⚠️ **El bloqueo clásico**: en Notion, entra a la database → `...` → **Connections** → conecta tu integración de n8n. Si no, el nodo da `object not found` aunque el ID esté bien.

## 5. Slack → `Post Message to Channel`

Canal `#ventas` (o el que uses). Ojo con dos cosas: después de Notion, `$json` ya es la respuesta de Notion, así que los datos del correo se referencian **por nombre de nodo**; y Slack usa `<url|text>`, no Markdown.

```
📩 *Nueva {{ $('Extraer datos').item.json.tipo }}*
*De:* {{ $('Extraer datos').item.json.nombre }} · {{ $('Extraer datos').item.json.email }}
*Asunto:* {{ $('Extraer datos').item.json.asunto }}
<{{ $('Extraer datos').item.json.gmailUrl }}|Abrir en Gmail> · <{{ $json.url }}|Ver ficha en Notion>
```

---

## Tres ajustes "pro" según cómo lo uses

1. **Duplicados**: el trigger de Gmail puede re-entregar el mismo mensaje tras un reinicio. Añade un *Query Database* filtrando por `Gmail ID` antes del Create, o usa esa columna para dedupe manual.
2. **Slack aunque Notion falle**: pon Notion y Slack en ramas paralelas desde el Filter (Slack pierde el link a la ficha), o activa `Continue On Fail` en Notion + un Error Trigger.
3. **Solo bandeja de entrada**: añade `labelIds: ["INBOX"]` en el trigger si no quieres que dispare con enviados o borradores.

¿Quieres que te lo deje como **JSON listo para importar** (con los `typeVersion` de n8n 1.x) y te detallo el alta de las 3 credenciales — Gmail OAuth2, Notion integration y Slack bot?