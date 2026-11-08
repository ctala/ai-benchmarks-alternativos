# Inkling Small — multi_turn/requirements_change

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 4.26 | quality: 4.0
- latency_total: 67.19s | tokens_per_second: 45.8
- input_tokens: 230 | output_tokens: 3077

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

Perfecto, actualizado. Ahora tu flujo es:

**Gmail → Filtro por asunto → Notion + Slack**

Aquí te dejo la arquitectura paso a paso para N8N:

### 1. Trigger: Gmail
- **Nodo:** `Gmail Trigger`
- Configura tu credencial OAuth de Gmail.
- Opcional (recomendado): en los parámetros de búsqueda pon `is:unread` o `newer_than:1d` para no releer todo.

### 2. Extraer + Filtrar (lo más importante)
En lugar de complicar el IF con OR, usa un nodo **Code** (o Function) para evaluar el filtro fácilmente:

**Nodo: Function / Code** (nombre: `Evaluar Filtro`)
```javascript
const subject = ($json.subject || '').toString();
const lower = subject.toLowerCase();
const pasa = lower.includes('propuesta') || lower.includes('cotizacion');

// Devolvemos todo el email más una flag booleana
return [{
  json: {
    ...$json,
    pasaFiltro: pasa,
    remitenteNombre: $json.from?.name || $json.from?.email || 'Desconocido',
    remitenteEmail: $json.from?.email || 'N/A',
    asuntoLimpio: $json.subject || 'Sin asunto',
    fecha: $json.date || new Date()
  }
}];
```

**Nodo: IF** (nombre: `¿Tiene propuesta o cotización?`)
- **Condition:** `pasaFiltro` `equals` `true`
- **True branch:** continúa al paso 3.
- **False branch:** no hagas nada (o conecta a `NoOp`).

> Esto hace el filtro en el workflow y es case-insensitive (`propuesta`, `COTIZACION`, `Propuesta`... todo pasa).

### 3. Formatear datos para Notion y Slack
**Nodo: Set** (nombre: `Datos para Notion`)
Crea los campos que vas a usar en ambos destinos:
- `nombreRemitente`: `{{ $json.remitenteNombre }}`
- `emailRemitente`: `{{ $json.remitenteEmail }}`
- `asunto`: `{{ $json.asuntoLimpio }}`
- `fechaRecibido`: `{{ $json.fecha }}`
- `mensajeSlack`: `Nuevo email de {{ $json.remitenteNombre }} — *{{ $json.asuntoLimpio }}*`

### 4. Guardar en Notion
**Nodo: Notion** (nombre: `Crear en Notion`)
- **Action:** `Create a Database Page` (o `Create Page` si usas una DB de tipo tabla).
- **Credential:** Integration Token de Notion.
- **Database:** Selecciona tu base de datos (debe estar compartida con la integración).
- **Properties:** Mapea:
  - `Nombre` (Title): `{{ $json.nombreRemitente }}`
  - `Email` (Email): `{{ $json.emailRemitente }}`
  - `Asunto` (Rich Text / Title): `{{ $json.asunto }}`
  - `Fecha` (Date): `{{ $json.fechaRecibido }}`

> **Tip:** En Notion crea una base de datos con al menos estas propiedades antes de conectar N8N.

### 5. Notificar a Slack
**Nodo: Slack** (nombre: `Notificar Slack`)
- **Credential:** Slack OAuth o Incoming Webhook.
- **Operation:** `Post Message`
- **Channel:** `#propuestas` (o el que uses)
- **Text:** `{{ $json.mensajeSlack }}`
- Puedes agregar `*Asunto:* {{ $json.asunto }}` y un enlace al email si quieres.

### Estructura visual del flujo
```
[Gmail Trigger]
      ↓
[Code: Evaluar Filtro]
      ↓
     IF (pasaFiltro == true)
      ↓ (true)
[Set: Datos]
      ↓
   ├──→ [Notion: Crear DB]  (guarda)
   └──→ [Slack: Post Msg]   (avisa)
```

### Credenciales que necesitas configurar
1. **Gmail:** OAuth 2.0 (Google Cloud Console).
2. **Notion:** Internal Integration (`https://www.notion.so/my-integrations`) + compartir la base de datos con ella.
3. **Slack:** App de Slack con permisos `chat:write` y `channels:read`.

¿Quieres que te pase la expresión exacta para el nodo IF si prefieres no usar el Code node, o que te detalle cómo configurar el campo `from` de Gmail si te llega como string en lugar de objeto?