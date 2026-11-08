# Ling 3.0 Flash — multi_turn/requirements_change

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 4.97 | quality: 4.0
- latency_total: 20.332s | tokens_per_second: 91.1
- input_tokens: 266 | output_tokens: 1853

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

¡Perfecto, entendido! Cambiamos el destino y agregamos filtro + notificación. Acá te va el workflow actualizado con todos los nodos:

---

## Flujo: Gmail → Filtrar → Notion + Slack

### Estructura general:

```
[Gmail Trigger] → [Filter] → [Function] → [Notion] → [Slack]
```

---

### 1. 📥 Gmail Trigger
- **Evento**: "New Email Received"
- **Configuración**:
  - Selecciona la cuenta de Gmail conectada
  - Opcional: puedes configurar una búsqueda avanzada para optimizar (ej: `in:inbox`), pero el filtro lo haremos después
- **Salida**: Cada email nuevo como un item con campos como `subject`, `from`, `date`, `body`, etc.

---

### 2. 🔍 Filter Node (Filtrar asunto)
Este nodo decide si el email cumple la condición o no.

- **Condición 1** (rama "verdadera"):
  - Valor: `{{ $json.subject }}`
  - Operador: `Contains`
  - Valor: `propuesta`

- **Condición 2** (sumada con OR):
  - Valor: `{{ $json.subject }}`
  - Operador: `Contains`
  - Valor: `cotizacion`

> **Importante**: Configura ambas condiciones con lógica **OR** para que pase si tiene "propuesta" **o** "cotizacion". Si quieres que sea case-insensitive, puedes usar un **Function** node antes para pasar todo a minúsculas:

```javascript
const email = $input.first();
email.json.subject_lower = email.json.subject.toLowerCase();
return [email];
```
Y luego en el Filter usar `subject_lower` con los valores `propuesta` y `cotizacion`.

---

### 3. ⚙️ Function Node (Extraer datos del remitente)

```javascript
const email = $input.first();
const from = email.json.from || email.json.sender || '';

return [{
  json: {
    remitente_nombre: from,
    remitente_email: from,
    asunto: email.json.subject,
    fecha: email.json.date,
    cuerpo: email.json.textBody || email.json.htmlBody || '',
    timestamp: new Date().toISOString()
  }
}];
```

Esto te deja limpios los datos que vas a guardar en Notion.

---

### 4. 📝 Notion Node (Guardar en base de datos)

- **Operación**: "Create a Database Item" (o "Append to Database" según versión)
- **Database ID**: Selecciona tu base de datos de Notion (necesitas tenerla ya creada con los campos que quieras)
- **Mapeo de campos**:

| Campo en Notion | Valor |
|---|---|
| **Remitente** | `{{ $json.remitente_nombre }}` |
| **Email** | `{{ $json.remitente_email }}` |
| **Asunto** | `{{ $json.asunto }}` |
| **Fecha** | `{{ $json.fecha }}` |
| **Cuerpo** | `{{ $json.cuerpo }}` |

> **Prerequisito**: En Notion, crea una base de datos con propiedades como: *Remitente* (título), *Email* (texto), *Asunto* (texto), *Fecha* (date), *Cuerpo* (texto). Luego conecta la integración Notion en N8N (Settings → Integrations → Notion, o vía OAuth).

---

### 5. 💬 Slack Node (Notificación)

- **Recurso**: Message
- **Operación**: Post Message
- **Channel**: Selecciona el canal (ej: `#notificaciones` o el ID del canal)
- **Texto**:

```
📩 *Nuevo email detectado!*
*Remitente:* {{ $json.remitente_nombre }}
*Email:* {{ $json.remitente_email }}
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
```

> **Prerequisito**: Conecta tu workspace de Slack en N8N (Settings → Integrations → Slack) y asegúrate de que el bot tenga permisos para escribir en el canal.

---

### Resumen visual del workflow:

```
 ┌──────────────┐
 │ Gmail Trigger │  ← Detecta cada email nuevo
 └──────┬───────┘
        │
 ┌──────▼───────┐
 │   Filter     │  ← Solo si asunto contiene "propuesta" o "cotizacion" (OR)
 └──────┬───────┘
        │ (solo los que pasan el filtro)
 ┌──────▼───────┐
 │  Function    │  ← Extrae remitente, asunto, fecha, cuerpo
 └──────┬───────┘
        │
   ┌────┴────┐
   │         │
   ▼         ▼
┌──────┐ ┌────────┐
│Notion│ │ Slack  │  ← Guarda en BD + notifica al canal
└──────┘ └────────┘
```

---

### ⚠️ Notas importantes:
1. **Notion**: Necesitas crear la base de datos manualmente primero y luego conectarla en N8N.
2. **Slack**: El bot de Slack debe estar invitado al canal donde quieres recibir las notificaciones.
3. **Gmail Trigger**: Por defecto trae emails de la bandeja de entrada. Si solo quieres leer ciertos remitentes, puedes agregar otro filtro adicional.
4. **Activación**: Recuerda activar ("Active") el workflow para que el trigger funcione en tiempo real.

¿Querés que te pase la configuración con más detalle de algún nodo en particular, o que agregue algo más como adjuntos de email o deduplicación?