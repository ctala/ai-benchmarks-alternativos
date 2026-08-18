# Claude Opus 5 Fast — multi_turn/requirements_change

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.58 | quality: 8.0
- latency_total: 19.036s | tokens_per_second: 220.7
- input_tokens: 363 | output_tokens: 4201

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

Buen cambio — Notion es mejor para esto porque cada propuesta queda como una página con contexto, no una fila plana.

## Arquitectura del workflow

```
Gmail Trigger → Code (parsear remitente) → Notion (crear página) → Slack (notificar)
```

Nota el orden: **Slack va después de Notion**, así puedes incluir el link a la página de Notion en la notificación. Si lo pones en paralelo, pierdes eso.

---

## 1. Gmail Trigger

El filtro conviene hacerlo **aquí**, no en un nodo IF posterior. Así Gmail te devuelve solo lo relevante y no gastas ejecuciones.

| Campo | Valor |
|---|---|
| Poll Times | Every X Minutes → 5 |
| Simplify | ✅ activado |
| Filters → Search | `subject:(propuesta OR cotizacion OR cotización OR presupuesto)` |

Sobre los acentos: Gmail **normalmente** normaliza diacríticos en las búsquedas, pero no es un comportamiento documentado de forma firme. Incluir ambas variantes cuesta nada y te evita el bug silencioso de perder emails con "cotización".

**Opcional (recomendado)**: añade un nodo **Filter** después del trigger como red de seguridad:

```javascript
{{ /propuesta|cotizaci[oó]n|presupuesto/i.test($json.subject || '') }}
```

Esto te cubre si algún día cambias el query del trigger.

---

## 2. Code Node — parsear el remitente

El formato del campo `from` varía según la versión del nodo Gmail y si tienes Simplify activo. Este código es defensivo y cubre los casos comunes:

```javascript
const items = $input.all();

return items.map(item => {
  const data = item.json;

  // El campo 'from' puede venir en varios formatos según versión/simplify
  let rawFrom = '';

  if (typeof data.from === 'string') {
    rawFrom = data.from;
  } else if (data.from?.value?.[0]) {
    const v = data.from.value[0];
    return {
      json: {
        senderName: v.name || v.address?.split('@')[0] || 'Desconocido',
        senderEmail: v.address || '',
        senderDomain: (v.address || '').split('@')[1] || '',
        subject: data.subject || '(sin asunto)',
        receivedAt: data.date || new Date().toISOString(),
        snippet: (data.snippet || '').substring(0, 2000),
        gmailUrl: `https://mail.google.com/mail/u/0/#inbox/${data.id}`,
        threadId: data.threadId || '',
      }
    };
  } else if (Array.isArray(data.payload?.headers)) {
    rawFrom = data.payload.headers.find(h => h.name.toLowerCase() === 'from')?.value || '';
  }

  // Parseo de "Nombre Apellido <email@dominio.com>" o "email@dominio.com"
  const match = rawFrom.match(/^\s*(?:"?([^"<]*?)"?\s*)?<?([^\s<>]+@[^\s<>]+)>?\s*$/);
  const senderName = (match?.[1] || '').trim();
  const senderEmail = (match?.[2] || rawFrom).trim();

  return {
    json: {
      senderName: senderName || senderEmail.split('@')[0] || 'Desconocido',
      senderEmail,
      senderDomain: senderEmail.split('@')[1] || '',
      subject: data.subject || '(sin asunto)',
      receivedAt: data.date || new Date().toISOString(),
      snippet: (data.snippet || '').substring(0, 2000),
      gmailUrl: `https://mail.google.com/mail/u/0/#inbox/${data.id}`,
      threadId: data.threadId || '',
    }
  };
});
```

`senderDomain` te sirve después para agrupar por empresa en Notion.

---

## 3. Notion Node

**Resource**: Database Page → **Operation**: Create

Antes de configurarlo, crea la database en Notion con estas propiedades (los nombres deben coincidir **exactamente**, incluidas mayúsculas):

| Propiedad | Tipo Notion |
|---|---|
| Asunto | Title |
| Contacto | Rich Text |
| Email | Email |
| Dominio | Rich Text |
| Recibido | Date |
| Estado | Select (opciones: Nuevo, En revisión, Respondido, Descartado) |
| Link Gmail | URL |
| Resumen | Rich Text |

Mapeo en el nodo:

| Propiedad | Expresión |
|---|---|
| Asunto | `{{ $json.subject }}` |
| Contacto | `{{ $json.senderName }}` |
| Email | `{{ $json.senderEmail }}` |
| Dominio | `{{ $json.senderDomain }}` |
| Recibido | `{{ new Date($json.receivedAt).toISOString() }}` |
| Estado | `Nuevo` (valor fijo) |
| Link Gmail | `{{ $json.gmailUrl }}` |
| Resumen | `{{ $json.snippet }}` |

**Dos cosas que rompen esto siempre:**
1. La database tiene que estar **compartida con tu integración** de Notion (en la página: `•••` → Connections → añadir tu integración). Si no, recibes 404 aunque el ID sea correcto.
2. La propiedad de tipo **Title** es obligatoria. Si tu database usa otro nombre para el título ("Name" por defecto), ajústalo.

---

## 4. Slack Node

**Resource**: Message → **Operation**: Send

- **Send Message To**: Channel
- **Channel**: `#propuestas` (o el que uses)
- **Message Type**: Text (o Blocks si quieres botones)

Texto del mensaje:

```
📥 *Nueva propuesta recibida*

*De:* {{ $('Code').item.json.senderName }} ({{ $('Code').item.json.senderEmail }})
*Asunto:* {{ $('Code').item.json.subject }}
*Recibido:* {{ new Date($('Code').item.json.receivedAt).toLocaleString('es-ES') }}

<{{ $json.url }}|Ver en Notion> · <{{ $('Code').item.json.gmailUrl }}|Abrir en Gmail>
```

Detalles:
- `$json.url` es la URL que devuelve el nodo de Notion tras crear la página.
- Uso `$('Code').item.json.X` para referenciar el nodo anterior por nombre — si renombras el Code node, actualiza estas referencias.
- La sintaxis `<url|texto>` es el formato de links de Slack, no markdown estándar.

**Requisito**: el bot de Slack debe estar invitado al canal (`/invite @tu-bot`), y necesita el scope `chat:write`.

---

## Consideraciones antes de ponerlo en producción

**Duplicados**: si alguien responde en el mismo hilo con "Re: Propuesta", se crea una página nueva. Si te molesta, añade un nodo Notion (Get Many, con filtro por `threadId`) + IF antes de crear, para saltarte hilos ya registrados. Requiere guardar `threadId` como propiedad adicional en Notion.

**Rate limit de Notion**: 3 requests/segundo. Con volumen normal de emails no lo tocas, pero si haces una carga inicial masiva, mete un nodo Wait.

**Manejo de errores**: en Settings de cada nodo puedes activar *Continue On Fail* para que un fallo en Notion no bloquee la notificación de Slack. Yo prefiero lo contrario aquí: que falle ruidosamente, porque una propuesta perdida cuesta más que un error visible.

**Testing**: usa "Fetch Test Event" en el Gmail Trigger para traer un email real y probar el resto del flujo sin esperar a que llegue uno nuevo.

---

¿Quieres que te arme el JSON completo del workflow para importarlo directamente, o prefieres la lógica de deduplicación por `threadId` primero?