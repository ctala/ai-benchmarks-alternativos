# DeepSeek V4.1 Flash — multi_turn/requirements_change

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 6.23 | quality: 6.0
- latency_total: 14.454s | tokens_per_second: 107.9
- input_tokens: 270 | output_tokens: 1559

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

Claro, cambio el plan. Así queda el workflow:

**Gmail Trigger → Filter → Notion → Slack**

---

### 1. Gmail Trigger
En **Filters → Search** puedes filtrar ya desde Gmail con sintaxis de búsqueda:

```
subject:propuesta OR subject:cotizacion OR subject:cotización
```

⚠️ Ojo: Gmail no maneja bien los acentos en la búsqueda, así que "cotización" puede no matchear. Por eso yo dejaría el Search vacío (o solo `is:unread`) y haría el filtrado fino en el nodo siguiente. Así controlás el tema de mayúsculas/acentos.

---

### 2. Filter node (o Function, si querés normalizar acentos)
Camino simple con un **Filter node** → Condition:

- Left: `{{ $json.subject.toLowerCase() }}`
- Operator: **contains**
- Right: `propuesta`

Y una segunda condición con **OR** para `cotizacion`.

Si querés que "Cotización" y "COTIZACIÓN" también entren, usá un **Code node** con esta normalización:

```javascript
return items.filter(item => {
  const subject = (item.json.subject || '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, ''); // saca acentos
  return subject.includes('propuesta') || subject.includes('cotizacion');
});
```

---

### 3. Notion — Create a Database Page
Necesitás una base en Notion con estas propiedades (los tipos importan, si no el nodo falla):

| Propiedad | Tipo en Notion | Valor desde n8n |
|---|---|---|
| Name | Title | `{{ $json.subject }}` |
| Email | Email | `{{ $json.from.value[0].address }}` |
| Remitente | Rich text | `{{ $json.from.value[0].name }}` |
| Fecha | Date | `{{ new Date($json.date).toISOString() }}` |

En el nodo: **Database ID** (lo sacás de la URL de la base), **Database Page → Title** mapeado, y agregás cada propiedad.

Dos cosas que suelen romper acá:
- La integración de Notion tiene que estar **compartida explícitamente** con esa base (⋯ → Connections en Notion).
- Si el header `date` del email no trae zona horaria, `new Date()` te puede tirar `Invalid Date`. En ese caso usá `{{ new Date($json.date).toISOString() }}` con fallback a `{{ $now.toISOString() }}`.

---

### 4. Slack — Send Message
- **Channel**: el que quieras
- **Text**:
```
📩 Nueva {{ $json.subject.toLowerCase().includes('propuesta') ? 'propuesta' : 'cotización' }}
De: {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})
Asunto: {{ $json.subject }}
```

---

### Detalle de conexión
No los pongas en paralelo por defecto: si Notion falla, no te llega la notificación (o al revés, según el orden). Si querés que un fallo de Notion no te ciegue, conectá el Slack node **desde el Filter node** (rama paralela) en lugar de después de Notion.

¿Querés que te arme también un chequeo de duplicados, o el esquema exacto de la base de Notion para importar?