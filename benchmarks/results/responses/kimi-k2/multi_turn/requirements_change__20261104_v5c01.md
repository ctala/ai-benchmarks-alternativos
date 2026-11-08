# Kimi K2 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 4.39 | quality: 4.0
- latency_total: 17.735s | tokens_per_second: 46.0
- input_tokens: 267 | output_tokens: 815

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

Perfecto, entiendo los cambios. Aquí está el workflow actualizado:

## Estructura del Workflow

```
[Gmail Trigger] → [Filter] → [Parse Remitente] → [Notion] → [Slack]
```

---

## Configuración paso a paso

### 1. Gmail Trigger
- **Event**: `Message Received`
- **Options**: 
  - `Mark as Read`: No (para no perder visibilidad)
  - `Download Attachments`: No (a menos que lo necesites)

---

### 2. Filter (Condición del asunto)
```
{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}
```

---

### 3. Function → Parsear datos del remitente

```javascript
// Extraer nombre y email del formato "Nombre <email@dominio.com>"
const from = $input.first().json.from;

const match = from.match(/(.*?) <(.*?)>/);
const nombre = match ? match[1].trim() : from;
const email = match ? match[2].trim() : '';

return {
  nombre_remitente: nombre,
  email_remitente: email,
  asunto: $input.first().json.subject,
  fecha: new Date().toISOString(),
  snippet: $input.first().json.snippet // preview del contenido
};
```

---

### 4. Notion (Create Database Item)

| Propiedad | Valor |
|-----------|-------|
| **Database ID** | Tu base de datos en Notion |
| **Nombre** | `{{ $json.asunto }}` |
| **Email** | `{{ $json.email_remitente }}` |
| **Remitente** | `{{ $json.nombre_remitente }}` |
| **Fecha** | `{{ $json.fecha }}` |
| **Estado** | "Nuevo" (select) |

> **Importante**: La base de datos en Notion debe tener las mismas propiedades que defines aquí.

---

### 5. Slack (Send Message)

**Canal**: `#oportunidades` (o el que prefieras)

**Mensaje**:
```
🚨 Nueva oportunidad detectada

*De:* {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}

Ver en Notion → [link al registro]
```

---

## Diagrama visual

```
┌─────────────┐     ┌─────────┐     ┌─────────────┐
│ Gmail       │────→│ Filter  │────→│ Parse       │
│ (nuevo msg) │     │ (asunto)│     │ (remitente) │
└─────────────┘     └─────────┘     └──────┬──────┘
                                           │
                    ┌──────────────────────┘
                    ▼
           ┌─────────────┐
           │ Notion      │────────┐
           │ (guardar)   │        │
           └─────────────┘        ▼
                          ┌─────────────┐
                          │ Slack       │
                          │ (notificar) │
                          └─────────────┘
```

---

## Requisitos previos

| Servicio | Qué necesitas |
|----------|---------------|
| Gmail | OAuth2 conectado en N8N |
| Notion | Integration token + base de datos compartida |
| Slack | Bot token con permisos `chat:write` |

---

¿Necesitas que profundice en algún nodo específico? Por ejemplo, la configuración del OAuth de Gmail o la estructura exacta de la base de datos en Notion.