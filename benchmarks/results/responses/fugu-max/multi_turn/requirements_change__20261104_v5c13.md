# Fugu Max — multi_turn/requirements_change

- model_id: `sakana/fugu-max`
- success: True  | final: 4.34 | quality: 4.0
- latency_total: 10.729s | tokens_per_second: 177.6
- input_tokens: 362 | output_tokens: 1905

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

Perfecto, cambia bastante la cosa. Te dejo el flujo final y luego el detalle de cada nodo.

**Flujo:** Gmail Trigger → Code (filtrar + parsear) → Notion (crear página) → Slack (notificar)

---

## 1. Gmail Trigger

- **Event**: Message Received
- **Poll Times**: cada minuto (o lo que necesites)
- **Filters → Query**: déjalo **vacío** (filtramos en n8n, te explico por qué abajo)

## 2. Code node — "Filtrar y parsear"

Aquí hacemos dos cosas: descartar los que no interesan y limpiar el remitente.

```js
const normalizar = (s) =>
  (s || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');

const out = [];

for (const item of $input.all()) {
  const asunto = item.json.Subject || '';

  // Filtro: "propuesta" o "cotizacion" (con o sin acento)
  if (!/propuesta|cotizacion/.test(normalizar(asunto))) continue;

  const fromRaw = item.json.From || '';
  const m = fromRaw.match(/^(.*?)\s*<(.+)>$/);

  out.push({
    json: {
      nombre: m ? m[1].replace(/"/g, '').trim() : fromRaw.trim(),
      email: m ? m[2].trim() : fromRaw.trim(),
      asunto: asunto,
      fecha: item.json.Date || new Date().toISOString(),
      snippet: item.json.snippet || '',
      messageId: item.json.id
    }
  });
}

return out;
```

Si devuelve `[]`, el workflow se detiene ahí y no crea nada en Notion ni notifica. Justo lo que quieres.

## 3. Notion — Create a Page

- **Resource**: Database Page
- **Database**: tu base de datos
- **Properties**: mapea con expresiones del nodo anterior:

| Propiedad Notion | Tipo | Valor |
|---|---|---|
| Name | Title | `{{ $json.asunto }}` |
| Remitente | Rich text | `{{ $json.nombre }}` |
| Email | Email | `{{ $json.email }}` |
| Fecha | Date | `{{ $json.fecha }}` |
| Extracto | Rich text | `{{ $json.snippet }}` |

⚠️ **Importante**: la base de datos tiene que estar **compartida con la integración de Notion** (en Notion → `···` → Connections → añade tu integración). Si no, el nodo no la ve en el desplegable.

## 4. Slack — Send a Message

- **Channel**: el canal donde quieras el aviso
- **Text**:

```
📩 Nueva {{ $json.asunto }}
De: {{ $json.nombre }} ({{ $json.email }})
{{ $json.fecha }}
```

En "Additional Fields" puedes añadir el enlace al email de Gmail si quieres:
`https://mail.google.com/mail/u/0/#inbox/{{ $json.messageId }}`

---

## Dos detalles que suelen romper esto

**El filtro lo pongo en n8n, no en el Query de Gmail.** El motivo: la búsqueda de Gmail **no es insensible a acentos**, así que `subject:cotizacion` no encuentra "cotización". Podrías poner `subject:{propuesta cotizacion cotización}` en el Query para reducir volumen, pero la normalización con `.normalize('NFD')` del Code node es más fiable. Si quieres, puedes hacer las dos cosas: Query restrictivo en Gmail + Code como red de seguridad.

**Orden Notion → Slack.** Si Notion falla (base no compartida, propiedad mal mapeada), Slack no se envía y te enteras. Si prefieres que la notificación salga igualmente, activa **Continue On Fail** en el nodo de Notion y pon el Slack en paralelo. Yo recomiendo el orden secuencial: si no se guardó, no quieres que te avisen como si estuviera guardado.

¿Quieres que te genere el JSON importable del workflow completo?