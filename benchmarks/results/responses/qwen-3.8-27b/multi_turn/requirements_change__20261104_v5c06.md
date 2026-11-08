# Qwen 3.8 27B — multi_turn/requirements_change

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 4.15 | quality: 4.0
- latency_total: 104.027s | tokens_per_second: 53.7
- input_tokens: 275 | output_tokens: 5591

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



Perfecto, con ese cambio el workflow final quedaría así:

## Workflow en N8N

### 1. Gmail Trigger
- Nodo: **Gmail Trigger**
- Escucha nuevos emails entrantes.
- Si quieres, puedes limitar la ejecución a cuentas o bandejas específicas.

---

## 2. Nodo Code: “Filtrar y extraer”

Este nodo va a:

- leer el asunto y el remitente,
- normalizar el texto para aceptar:
  - `propuesta`
  - `Propuesta`
  - `PROPUESTA`
  - `cotización`
  - `cotizacion`
- extraer:
  - nombre del remitente,
  - email del remitente,
  - asunto,
  - fecha,
  - snippet del mensaje,
- filtrar solo los emails que tengan `propuesta` o `cotización/cotizacion` en el asunto,
- si no coincide, detener el flujo.

### Código para el nodo Code

```js
const item = $input.first().json;

// Buscar el mensaje según la versión del nodo Gmail
const msg = item?.data?.payload ? item.data : (item?.payload ? item : (item?.message?.payload ? item.message : item));

const headers = msg?.payload?.headers || [];

const getHeader = (name) => {
  const h = headers.find(h => (h.name || '').toLowerCase() === name);
  return h?.value || '';
};

const subject = getHeader('subject');
const from = getHeader('from');
const date = getHeader('date');
const snippet = msg?.snippet || msg?.payload?.bodyData || '';

// Parsear remitente
let email = '';
let senderName = '';

const emailMatch = from.match(/<([^>]+)>/);

if (emailMatch) {
  email = emailMatch[1].trim();
  senderName = from.split('<')[0].replace(/^["']|["']$/g, '').trim();
} else if (from.includes('@')) {
  email = from.trim();
  senderName = email.split('@')[0];
} else {
  email = from;
  senderName = from;
}

// Normalizar: minúsculas y sin acentos
const normalize = (s = '') =>
  String(s)
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .trim();

const nSubject = normalize(subject);

// Solo avanzar si el asunto contiene "propuesta" o "cotizacion"
const matches = nSubject.includes('propuesta') || nSubject.includes('cotizacion');

if (!matches) {
  return [];
}

return [
  {
    json: {
      'Remitente': senderName || 'Desconocido',
      'Email': email || 'desconocido',
      'Asunto': subject || '(sin asunto)',
      'Fecha': date || new Date().toISOString(),
      'Snippet': String(snippet).slice(0, 500)
    }
  }
];
```

---

## 3. Nodo Notion

Conectas el output del nodo **Filtrar y extraer** a **Notion**.

### Configuración sugerida

- Nodo: **Notion**
- Resource: **Database**
- Operation: **Create** / **Append row**  
  *depende de tu versión de N8N; el objetivo es crear una fila/página nueva en tu base de datos*

### Campos a mapear

Suponiendo que tu base de datos Notion tenga estas columnas:

- Remitente
- Email
- Asunto
- Fecha
- Snippet

Entonces mapeas:

- Remitente: `={{ $json['Remitente'] }}`
- Email: `={{ $json['Email'] }}`
- Asunto: `={{ $json['Asunto'] }}`
- Fecha: `={{ $json['Fecha'] }}`
- Snippet: `={{ $json['Snippet'] }}`

> Si tu base de datos usa propiedades con nombres diferentes, solo cambia los campos a los que corresponda.

---

## 4. Nodo Slack

Después de Notion, agregas un nodo **Slack** para avisar.

### Configuración

- Nodo: **Slack**
- Resource: **Message**
- Operation: **Create**
- Channel: `#tu-canal`

### Texto del mensaje

Usa este texto para que el Slack tome los datos del nodo Code, no del output de Notion:

```text
📩 Nuevo email relevante

Remitente: {{ $('Filtrar y extraer').first().json['Remitente'] }}
Correo: {{ $('Filtrar y extraer').first().json['Email'] }}
Asunto: {{ $('Filtrar y extraer').first().json['Asunto'] }}
Fecha: {{ $('Filtrar y extraer').first().json['Fecha'] }}
Vista previa: {{ $('Filtrar y extraer').first().json['Snippet'] }}
```

---

# Flujo final

Queda así:

1. **Gmail Trigger**
2. **Filtrar y extraer**
3. **Guardar en Notion**
4. **Notificar en Slack**

---

# Comportamiento esperado

- Si llega un email con asunto que contiene:
  - `propuesta`
  - `Propuesta`
  - `PROPUESTA`
  - `cotización`
  - `cotizacion`

entonces:

1. extrae los datos del remitente,
2. guarda el registro en Notion,
3. envía una notificación a Slack.

- Si el asunto no contiene esas palabras, el workflow **no hace nada**.

---

# Opcional recomendado

Si quieres que el workflow sea más robusto, también puedes:

- guardar solo emails de ciertos remitentes,
- excluir emails marcados como spam,
- registrar el ID del mensaje de Gmail para evitar duplicados,
- enviar a Slack solo si la carga en Notion fue exitosa.

Si quieres, en el siguiente mensaje te dejo **el workflow completo en JSON para importarlo directamente en N8N**.