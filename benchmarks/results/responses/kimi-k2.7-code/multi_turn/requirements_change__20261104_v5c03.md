# Kimi K2.7 Code — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.22 | quality: 8.0
- latency_total: 16.859s | tokens_per_second: 60.0
- input_tokens: 265 | output_tokens: 1012

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

Perfecto, ajustamos el workflow. Esta sería la estructura:

1. **Gmail Trigger** → Se activa con cada email nuevo
2. **Code node (o Set node)** → Extrae nombre y email del remitente
3. **Filter node** → Solo deja pasar si el asunto contiene "propuesta" o "cotizacion"
4. **Notion** → Crea un registro en tu base de datos
5. **Slack** → Envía la notificación

---

### Paso a paso:

**1. Gmail Trigger**
- Modo: `On message received`
- Selecciona tu credencial de Gmail

**2. Extraer datos del remitente (Code node)**
Gmail devuelve el remitente como `"Juan Pérez <juan@empresa.com>"`. Úsalo para separar nombre y email:

```js
const from = $input.first().json.from || "";

// Extraer nombre
const nameMatch = from.match(/^(.*?)\s*</);
const name = nameMatch ? nameMatch[1].trim() : "";

// Extraer email
const emailMatch = from.match(/<([^>]+)>/);
const email = emailMatch ? emailMatch[1] : from;

return {
  json: {
    senderName: name,
    senderEmail: email,
    subject: $input.first().json.subject,
    date: $input.first().json.date,
  }
};
```

**3. Filter node**
Condición para que pase solo si el asunto contiene "propuesta" o "cotizacion":

```
{{ $json.subject.toLowerCase().includes("propuesta") || $json.subject.toLowerCase().includes("cotizacion") }}
```

**4. Notion → Create Database Item**
- Selecciona tu base de datos
- Mapea las propiedades:
  - `Nombre` → `{{ $json.senderName }}`
  - `Email` → `{{ $json.senderEmail }}`
  - `Asunto` → `{{ $json.subject }}`
  - `Fecha` → `{{ $json.date }}`

**5. Slack → Send Message**
- Canal: el que prefieras
- Mensaje:
```
Nuevo email de oportunidad:
De: {{ $json.senderName }} ({{ $json.senderEmail }})
Asunto: {{ $json.subject }}
```

---

### Requisitos previos:
- Tener configuradas las credenciales de Gmail, Notion y Slack en N8N.
- En Notion, crear la base de datos con las propiedades que vas a mapear.
- En Slack, autorizar el bot en el canal destino.

¿Te gustaría que te pase el JSON del workflow listo para importar?