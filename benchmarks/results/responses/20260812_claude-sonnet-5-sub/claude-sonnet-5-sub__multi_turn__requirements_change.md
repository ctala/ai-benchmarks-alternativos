# Claude Sonnet 5 (suscripción) — multi_turn/requirements_change

- model_id: `claude-sonnet-5`
- success: True  | final: 5.4 | quality: 6.0
- latency_total: 29.937s | tokens_per_second: 49.7
- input_tokens: 2 | output_tokens: 1487

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

Entendido, ajustamos el flujo. Queda así:

1. **Gmail Trigger** — se activa con cada email nuevo (poll cada 1 min)
2. **Filter** (o **IF**) — solo pasa si el asunto contiene "propuesta" o "cotización"
3. **Set/Code** — extrae y normaliza los datos del remitente
4. **Notion** — crea una página/registro en la base de datos
5. **Slack** — notifica el hallazgo

## Detalle de configuración

**1. Gmail Trigger**
- Poll Times: cada 1-5 min según urgencia
- Filters → puedes usar el query de Gmail directo (`subject:(propuesta OR cotizacion)`) y ahorrarte el nodo Filter, o dejarlo abierto y filtrar después con más control.

**2. Filter (si no filtraste en el trigger)**
```
Condition: {{ $json.subject.toLowerCase() }} contains "propuesta"
OR
{{ $json.subject.toLowerCase() }} contains "cotizacion"
```
Nota: agrega también "cotización" con tilde o usa una normalización previa (`.normalize("NFD").replace(/[\u0300-\u036f]/g, "")`) para no perder emails por el acento.

**3. Set / Code node** — mapea los campos que necesitas:
```js
{
  nombre: $json.from.value[0].name,
  email: $json.from.value[0].address,
  asunto: $json.subject,
  fecha: $json.date,
  snippet: $json.snippet
}
```

**4. Notion node**
- Operation: `Create Database Page`
- Database: la que uses para leads/propuestas
- Mapea cada property (Nombre, Email, Asunto, Fecha) a los campos del paso anterior
- Requiere credential de Notion (integration token con acceso a esa database)

**5. Slack node**
- Operation: `Post Message`
- Channel: el que definas (ej. `#leads` o `#ventas`)
- Mensaje sugerido:
```
📩 Nueva propuesta/cotización de {{$json.nombre}} ({{$json.email}})
Asunto: {{$json.asunto}}
```

## Antes de armarlo, dos preguntas

1. **¿Ya tienes la database de Notion creada** con las properties (Nombre, Email, Asunto, Fecha) o necesitas que te pase también la estructura recomendada?
2. **¿El Slack va con formato simple o quieres bloques/Block Kit** (botón para abrir el email, etc.)?

Con eso te armo el JSON completo del workflow listo para importar.