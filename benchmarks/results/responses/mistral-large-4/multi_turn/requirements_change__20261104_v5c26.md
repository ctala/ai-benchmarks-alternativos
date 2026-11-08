# Mistral Large 4.0 — multi_turn/requirements_change

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 4.41 | quality: 4.0
- latency_total: 23.511s | tokens_per_second: 74.1
- input_tokens: 226 | output_tokens: 1742

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

Perfecto, ese flujo es ideal para ventas. Aquí tienes el workflow completo paso a paso:

## Estructura del Workflow

```
[Gmail Trigger] → [Filter: Asunto] → [Set: Extraer datos] → [Notion: Crear página] → [Slack: Notificar]
```

---

## 1. Gmail Trigger (Nodo: Gmail Trigger)
- **Operación**: `Get Many` (polling) o `On New Email` (si usas webhook)
- **Filtros opcionales**: Puedes poner query `subject:propuesta OR subject:cotizacion` aquí, pero te recomiendo dejarlo vacío y filtrar después para controlar mayúsculas/minúsculas.

**Campos que vienen por defecto**: `from`, `subject`, `date`, `snippet`, `textPlain`, `id`

---

## 2. Filter Node (Nodo: IF)
Condiciones (OR):
- **Condition 1**: `{{ $json.subject.toLowerCase().includes('propuesta') }}` → `is true`
- **Condition 2**: `{{ $json.subject.toLowerCase().includes('cotizacion') }}` → `is true` (también acepta "cotización" si quitas el acento, o usa `.normalize('NFD').replace(/[\u0300-\u036f]/g, '')` para quitar acentos)

*Si no cumple → No hace nada (ruta false vacía)*

---

## 3. Set Node (Extraer datos limpios)
Nombre: `Preparar datos`

Campos a crear:
- **nombre_remitente**: `{{ $json.from.split('<')[0].trim().replace(/"/g, '') }}`
- **email_remitente**: `{{ $json.from.match(/<(.+?)>/) ? $json.from.match(/<(.+?)>/)[1] : $json.from }}`
- **asunto**: `{{ $json.subject }}`
- **fecha_recibido**: `{{ $json.date }}`
- **resumen**: `{{ $json.snippet }}` (o `{{ $json.textPlain.substring(0, 500) }}` para los primeros 500 caracteres)
- **email_id**: `{{ $json.id }}` (para evitar duplicados después)

---

## 4. Notion Node (Crear registro)
- **Resource**: `Database Item`
- **Operation**: `Create`
- **Database**: Selecciona tu base de datos de "Propuestas/Cotizaciones"

**Mapeo de propiedades** (ajusta a los nombres de tu DB):
- **Name** (título): `{{ $json.asunto }}`
- **Email** (email): `{{ $json.email_remitente }}`
- **Remitente** (rich text): `{{ $json.nombre_remitente }}`
- **Fecha** (date): `{{ $json.fecha_recibido }}`
- **Estado** (select): `Nuevo`
- **Resumen** (rich text): `{{ $json.resumen }}`
- **ID Email** (rich text): `{{ $json.email_id }}` (para control de duplicados)

---

## 5. Slack Node (Notificación)
- **Resource**: `Message`
- **Operation**: `Post`
- **Channel**: `#ventas` o `#propuestas` (o tu usuario directo)

**Mensaje**:
```
🚨 *Nueva propuesta recibida*
• *De*: {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
• *Asunto*: {{ $json.asunto }}
• *Fecha*: {{ $json.fecha_recibido }}
• *Resumen*: {{ $json.resumen }}
📄 Guardado en Notion
```

---

## Tips importantes para producción:

1. **Evitar duplicados**: Antes del nodo de Notion, agrega un nodo **Notion → Search** buscando por el `email_id`. Si existe, no crees uno nuevo (usa un IF).

2. **Manejo de acentos**: Si alguien escribe "COTIZACIÓN" con acento, el filtro falla. Usa esta expresión más robusta:
   ```javascript
   {{ $json.subject.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').includes('cotizacion') }}
   ```

3. **Error handling**: Agrega un nodo **Error Trigger** aparte que te mande a Slack si falla cualquier nodo del flujo principal.

4. **Frecuencia**: Configura el Gmail Trigger para que revise cada 1-5 minutos (no cada segundo para no quemar los límites de la API).

¿Necesitas que te detalle cómo configurar la base de datos específica en Notion (qué tipos de propiedades usar) o cómo manejar los duplicados?