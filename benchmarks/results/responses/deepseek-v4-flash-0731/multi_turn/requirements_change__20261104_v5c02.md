# DeepSeek V4 Flash 0731 — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 5.09 | quality: 4.0
- latency_total: 12.894s | tokens_per_second: 151.8
- input_tokens: 324 | output_tokens: 1957

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

¡Perfecto! Entonces el workflow queda así:

**Gmail Trigger → Filtro (asunto) → [Si cumple] → Slack (notificación) + Notion (crear página)**

Te explico cada nodo con su configuración:

---

## 1. Nodo: Gmail Trigger
- **Evento**: `Message received` (se dispara con cada email nuevo).
- **Cuenta**: Conecta tu Gmail con OAuth.
- **Opcional**: En `Filters` puedes poner `in:inbox` para solo leer la bandeja de entrada.

Este nodo entrega los datos del email, incluyendo `subject`, `from`, `date`, etc.

---

## 2. Nodo: IF (Filtro por asunto)
- **Condiciones** (modo `OR`):
  - `{{ $json.subject }}` → `contains` → `propuesta`
  - `{{ $json.subject }}` → `contains` → `cotizacion`

Así, solo pasan los correos cuyo asunto contenga alguna de esas palabras.

---

## 3. (Opcional) Nodo: Function para extraer remitente
Si quieres guardar **nombre** y **email** por separado, agrega un nodo `Function` después del IF (en la rama `true`):

```javascript
const from = $json.from;
const match = from.match(/^(.*?)\s*<([^>]+)>/);
if (match) {
  return [{
    ...$json,
    senderName: match[1].trim(),
    senderEmail: match[2].trim()
  }];
} else {
  return [{
    ...$json,
    senderName: from,
    senderEmail: from
  }];
}
```

Esto convierte `"Juan Pérez <juan@mail.com>"` en `senderName: "Juan Pérez"` y `senderEmail: "juan@mail.com"`.

---

## 4. Nodo: Slack (notificación)
- **Operación**: `Send a message`.
- **Canal**: Elige el canal (ej. `#alertas`).
- **Mensaje**: Puedes usar texto fijo + variables, por ejemplo:
  ```
  📩 Nuevo correo con propuesta/cotización
  *De:* {{ $json.senderName }} ({{ $json.senderEmail }})
  *Asunto:* {{ $json.subject }}
  *Fecha:* {{ $json.date }}
  ```

---

## 5. Nodo: Notion (guardar registro)
- **Operación**: `Create Page`.
- **Base de datos**: Selecciona la base de datos en Notion donde quieres guardar.
- **Propiedades**: Mapea los campos, por ejemplo:
  - `Nombre` → `{{ $json.senderName }}`
  - `Email` → `{{ $json.senderEmail }}`
  - `Asunto` → `{{ $json.subject }}`
  - `Fecha` → `{{ $json.date }}`

---

## Conexión final
Conecta la salida `true` del nodo IF a **dos nodos en paralelo**: Slack y Notion (puedes arrastrar el cable a ambos). Así, cuando llegue un correo que cumpla el filtro, se notifica en Slack y se guarda en Notion al mismo tiempo.

---

### Notas adicionales
- Si prefieres no usar código, puedes reemplazar el nodo Function por un nodo `Edit Fields (Set)` y usar expresiones como `{{ $json.from.split('<')[0] }}` para el nombre, pero la regex es más precisa.
- Verifica que las integraciones de Slack y Notion estén conectadas en N8N (credenciales).
- El nodo Gmail Trigger puede usar *polling* (revisar cada X minutos) o *webhook* si configuras Google Cloud Pub/Sub. Para pruebas, el polling está bien.

¿Quieres que profundice en algún nodo o en la configuración de las credenciales?