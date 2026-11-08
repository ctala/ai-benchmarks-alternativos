# Tencent Hy4 preview — multi_turn/requirements_change

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.02 | quality: 4.0
- latency_total: 175.965s | tokens_per_second: 65.5
- input_tokens: 267 | output_tokens: 11527

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

¡Entendido! Actualizamos el workflow. La nueva estructura (más limpia y fácil de mantener) sería esta:

```text
Gmail Trigger  →  Extraer Datos (Code)  →  Filtrar Asunto (IF)  →  Notion (crear página)
                                                     └────────────→  Slack (notificar)
```

La idea es: **primero** extraemos y normalizamos los datos del email, **después** filtramos por el asunto, y finalmente guardamos en Notion y avisamos en Slack (en paralelo).

---

## 1. Gmail Trigger
- **Nodo:** `Gmail Trigger`
- **Credencial:** tu cuenta de Gmail (OAuth2).
- **Trigger On:** `Message Received` (cuando llegue un email nuevo).
- **Opcional:** si el nodo tiene la opción **“Simple”** o **“Simplify”**, actívala. Si no la tiene, no pasa nada: el siguiente nodo Code sabe leer los headers.

---

## 2. Extraer Datos (Code)
Este nodo toma el email y lo convierte en campos limpios: `nombre`, `email`, `asunto`, `fecha` y `mensaje`.

- **Nodo:** `Code`
- **Mode:** `Run Once for All Items`
- **Código:** (pégalo tal cual)

```javascript
const items = $input.all();
const resultados = [];

for (const item of items) {
  const j = item.json;

  // --- ASUNTO ---
  let asunto = j.subject || '';
  if (!asunto && j.payload && j.payload.headers) {
    const h = j.payload.headers.find(h => h.name.toLowerCase() === 'subject');
    if (h) asunto = h.value;
  }

  // --- REMITENTE (From) ---
  let from = j.from || '';
  if (!from && j.payload && j.payload.headers) {
    const h = j.payload.headers.find(h => h.name.toLowerCase() === 'from');
    if (h) from = h.value;
  }

  // --- FECHA ---
  let fecha = '';
  if (j.date) {
    const d = new Date(j.date);
    fecha = isNaN(d.getTime()) ? j.date : d.toISOString();
  } else if (j.internalDate) {
    fecha = new Date(Number(j.internalDate)).toISOString();
  }

  // --- SEPARAR NOMBRE Y EMAIL ---
  let nombre = '';
  let email = '';
  const match = from.match(/^(.*?)<(.+)>$/);
  if (match) {
    nombre = match[1].replace(/["']/g, '').trim();
    email = match[2].trim();
  } else {
    email = from.trim();
    nombre = email.split('@')[0];
  }

  // --- CUERPO / RESUMEN ---
  const mensaje = j.snippet || j.text || (j.payload && j.payload.snippet) || '';

  resultados.push({
    json: {
      nombre,
      email,
      asunto,
      fecha,
      mensaje
    }
  });
}

return resultados;
```

---

## 3. Filtrar Asunto (IF)
Aquí descartamos los emails que no sean de propuestas/cotizaciones.

- **Nodo:** `IF`
- **Combinator:** `OR`
- **Condiciones** (sobre el campo `{{ $json.asunto }}`):
  1. `Contains` → `propuesta` (activa **Ignore Case**)
  2. `Contains` → `cotizacion` (activa **Ignore Case**)
  3. `Contains` → `cotización` (activa **Ignore Case**)

> ✅ Así cubres si escriben “cotizacion” sin acento o “cotización” con acento.  
> *Alternativa más corta:* usar una sola condición **Regex** con `.*(propuesta|cotización|cotizacion).*` e Ignore Case activado.

Conecta solo la salida **true** del IF hacia Notion y Slack. La salida **false** la dejas sin conectar (el workflow simplemente termina).

---

## 4. Notion (guardar los datos)
Antes que nada, en Notion crea una **base de datos** con estas columnas (puedes usar otros nombres, pero luego debes mapearlos igual):

- `Asunto` → tipo **Title**
- `Nombre` → tipo **Text**
- `Email` → tipo **Email** (o Text)
- `Fecha` → tipo **Date**
- `Mensaje` → tipo **Text**

Luego configura el nodo:

- **Nodo:** `Notion`
- **Credencial:** tu integración de Notion (crea el token en notion.so/my-integrations y **comparte la base de datos con la integración**).
- **Resource:** `Database Page`
- **Operation:** `Create`
- **Database:** selecciona tu base de datos.
- **Properties** (mapea así):
  - `Asunto` (Title): `{{ $json.asunto }}`
  - `Nombre`: `{{ $json.nombre }}`
  - `Email`: `{{ $json.email }}`
  - `Fecha`: `{{ $json.fecha }}`
  - `Mensaje`: `{{ $json.mensaje }}`

---

## 5. Slack (notificación)
- **Nodo:** `Slack`
- **Credencial:** tu app de Slack (el bot necesita el scope `chat:write`).
- **Resource:** `Message`
- **Operation:** `Post`
- **Channel:** el canal donde quieras recibir el aviso (ej. `#propuestas`).
- **Text:** (puedes personalizarlo)

```text
:email: *Nueva propuesta o cotización recibida*
*De:* {{ $json.nombre }} (<{{ $json.email }}>)
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
*Resumen:* {{ $json.mensaje }}
```

> 💡 **Tip pro:** si quieres que el mensaje de Slack incluya el **enlace a la página de Notion** que se acaba de crear, mueve el nodo de Slack **después** del de Notion y agrega al final del texto:  
> `*Ver en Notion:* {{ $json.url }}`  
> (En ese caso, para los datos del remitente usa `{{ $('Extraer Datos').first().json.nombre }}`, etc.)

---

## ¿Quieres el JSON listo para importar?
Si me confirmas:
1. Los **nombres exactos** de las columnas en tu base de Notion,
2. El **canal de Slack** (o si prefieres que te llegue por DM),

…te preparo el **workflow en JSON** para que lo copies y lo importes directamente en n8n sin configurar nodo por nodo.