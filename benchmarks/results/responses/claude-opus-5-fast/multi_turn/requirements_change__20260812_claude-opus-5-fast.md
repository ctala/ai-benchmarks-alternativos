# Claude Opus 5 Fast — multi_turn/requirements_change

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 3.91 | quality: 4.0
- latency_total: 12.687s | tokens_per_second: 161.4
- input_tokens: 363 | output_tokens: 2048

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

Buen cambio — de hecho el workflow queda más útil así. Te dejo la arquitectura nueva y la configuración de cada nodo.

## Estructura del workflow

```
Gmail Trigger → IF (filtro asunto) → Code (parsear remitente) → Notion (crear página)
                                                              ↓
                                                          Slack (notificar)
```

## Nodo 1: Gmail Trigger

**Truco importante**: filtrá lo más posible en el propio trigger para no gastar ejecuciones (en n8n Cloud cada poll que trae items cuenta).

| Parámetro | Valor |
|---|---|
| Poll Times | Every X Minutes → 5 |
| Simplify | **OFF** (necesitás los headers completos) |
| Filters → Search | `subject:(propuesta OR cotizacion) is:unread` |

La búsqueda de Gmail ignora acentos, así que `cotizacion` también matchea "cotización". No pasa lo mismo si filtrás por código, por eso conviene delegarlo a Gmail.

## Nodo 2: IF (red de seguridad)

Aunque Gmail ya filtró, dejá un IF por si alguien escribe "Re: propuesta" en el cuerpo y Gmail lo interpreta raro.

- Condición: **String → matches regex**
- Value 1: `{{ $json.subject || $json.Subject }}`
- Value 2: `(?i)(propuesta|cotizaci[oó]n)`

## Nodo 3: Code (parsear remitente)

```js
const out = [];

for (const item of $input.all()) {
  const j = item.json;

  // El Gmail Trigger cambia la forma del payload segun Simplify.
  // Cubrimos los dos casos.
  let rawFrom = j.from || j.From || '';
  if (!rawFrom && Array.isArray(j.payload?.headers)) {
    rawFrom = j.payload.headers.find(h => h.name.toLowerCase() === 'from')?.value || '';
  }

  const m = rawFrom.match(/^\s*"?([^"<]*?)"?\s*<?([^<>\s]+@[^<>\s]+?)>?\s*$/);
  const nombre = (m?.[1] || '').trim() || null;
  const email  = (m?.[2] || rawFrom).trim().toLowerCase();

  out.push({