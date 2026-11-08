# Mercury 3 — multi_turn/requirements_change

- model_id: `inception/mercury-3`
- success: True  | final: 4.92 | quality: 4.0
- latency_total: 6.376s | tokens_per_second: 397.4
- input_tokens: 258 | output_tokens: 2534

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

¡Perfecto! Vamos a reestructurar el workflow: **Gmail → Filtro → Parsea → Notion + Slack**. Te dejo el paso a paso completo.

## Flujo general

```
Gmail Trigger (nuevo email)
        │
        ▼
Filter (asunto contiene "propuesta" o "cotizacion")
        │
        ▼
Function (extrae nombre y email del remitente)
        │
        ├──► Notion (crear página)
        │
        └──► Slack (enviar mensaje)
```

---

## 1. Nodo Gmail Trigger

- **Credenciales**: Conecta tu cuenta de Gmail con OAuth2 (vía Google Cloud Console).
- **Event Type**: `messageReceived` (o `new email` según la versión).
- **Search Filter (opcional pero recomendado)**: Para que Gmail solo emita los correos que te interesan, puedes escribir en el campo de búsqueda:

  ```
  subject:"propuesta" OR subject:"cotizacion"
  ```

  Así el workflow se activa únicamente con esos emails. Si prefieres filtrar después, deja este campo vacío y usa el nodo Filter.

---

## 2. Nodo Filter (si no usaste el filtro en el Trigger)

Si no configuraste el Search Filter, añade un nodo **Filter** después del Trigger.

- **Condiciones** (modo `OR`):
  - Campo: `subject` → Operación: `contains` → Valor: `propuesta`
  - Campo: `subject` → Operación: `contains` → Valor: `cotizacion`

- **Options**: Activa `Combine conditions` con `OR`.

---

## 3. Nodo Function (parsear remitente)

Este nodo separa el nombre y el email del campo `from` (que viene como `"Nombre" <correo@dominio.com>`).

```javascript
// Iteramos sobre todos los items que llegan
const items = [];

for (const item of $input.all()) {
  const from = item.json.from || '';
  const subject = item.json.subject || '';

  // Regex para extraer nombre y email
  const match = from.match(/^(.*?)\s*<([^>]+)>$/);
  const senderName = match ? match[1].trim() : from;
  const senderEmail = match ? match[2].trim() : from;

  items.push({
    json: {
      ...item.json,
      senderName,
      senderEmail,
      // Opcional: normalizar asunto
      cleanSubject: subject.trim()
    }
  });
}

return items;
```

---

## 4. Nodo Notion (crear página)

- **Credenciales**: Crea una integración en [Notion Developers](https://developers.notion.com/) y comparte tu base de datos con esa integración.
- **Resource**: `Database Page`
- **Operation**: `Create`
- **Database ID**: El ID de tu base de datos de Notion (lo encuentras en la URL de la base de datos).
- **Properties** (mapea con los campos del Function):
  - **Título** (title) → `cleanSubject`
  - **Nombre del remitente** (rich_text) → `senderName`
  - **Email del remitente** (rich_text) → `senderEmail`
  - **Fecha** (date) → `date` (o el campo que traiga el Trigger con la fecha del correo)
  - Si quieres, añade también el cuerpo del email como texto.

> 💡 Si tu base de datos tiene propiedades con otros nombres, ajústalos en el nodo.

---

## 5. Nodo Slack (notificación)

- **Credenciales**: Conecta tu workspace de Slack con el bot de n8n.
- **Operation**: `Post message`
- **Channel**: `#ventas` (o el canal que prefieras).
- **Text**: Usa un template como este:

  ```
  📩 Nueva {{ $json.subject.includes('propuesta') ? 'propuesta' : 'cotización' }} recibida
  De: {{ $json.senderName }} ({{ $json.senderEmail }})
  Asunto: {{ $json.subject }}
  ```

---

## Consejos finales

- **Prueba con un email real**: Después de conectar todo, envíate un correo con "propuesta" en el asunto para verificar que funciona.
- **Manejo de errores**: Si Notion o Slack fallan, puedes añadir un nodo `IF` después del Function para enviar un mensaje de error a otro canal.
- **Límites de Gmail**: El Trigger usa la API de Gmail, que tiene cuotas. Para volúmenes altos, considera usar un nodo **Gmail** (polling) con cron en lugar del Trigger.

¿Quieres que te ayude con algún paso específico, como la configuración de las credenciales de Notion o el mapeo de propiedades?