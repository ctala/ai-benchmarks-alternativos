# Claude Opus 4.8 — multi_turn/requirements_change

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 6.94 | quality: 8.92
- latency_total: 14.285s | tokens_per_second: 67.8
- input_tokens: 363 | output_tokens: 969
- judge_score: 5 | justificación: La respuesta es precisa y relevante, adaptando el workflow a Notion como se solicitó, con una estructura clara y detallada. Ofrece profundidad al explicar configuraciones y consideraciones, siendo altamente útil para un emprendedor.

## Respuesta completa

Buen cambio, Notion es más versátil para esto. Acá está el workflow actualizado:

## Estructura del Workflow

1. **Gmail Trigger** → se dispara con emails nuevos
2. **IF / Filter** → filtra solo los que tengan "propuesta" o "cotizacion" en el asunto
3. **Notion** → crea una página/fila en tu base de datos
4. **Slack** → envía la notificación

## Configuración de cada nodo

### 1. Gmail Trigger
- Authentication: OAuth2 (conectá tu cuenta)
- Poll Time: cada 1 min (o lo que necesites)
- Opcional: podés filtrar ya desde acá con `Search` para reducir carga

### 2. Filter (nodo IF)
Para que detecte cualquiera de las dos palabras, usá una condición con expresión:

```
{{ /propuesta|cotizacion/i.test($json.subject) }}
```

- Tipo: Boolean → `true`
- Esto usa regex con flag `i` (ignora mayúsculas/minúsculas), así detecta "Propuesta", "COTIZACION", etc.

### 3. Notion (Create Database Page)
Primero necesitás una base de datos en Notion con propiedades como:
- **Nombre remitente** (Text)
- **Email** (Email)
- **Asunto** (Title)
- **Fecha** (Date)

Mapeo en el nodo:
- Asunto → `{{ $json.subject }}`
- Email → `{{ $json.from.value[0].address }}`
- Nombre → `{{ $json.from.value[0].name }}`
- Fecha → `{{ $json.date }}`

> Ojo: la estructura exacta del campo `from` depende de cómo Gmail Trigger devuelva los datos. Conviene hacer un test run y revisar el JSON de salida real para ajustar las expresiones.

### 4. Slack (Send Message)
- Channel: el que quieras (#ventas, por ejemplo)
- Message:
```
🔔 Nueva propuesta/cotización recibida
De: {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})
Asunto: {{ $json.subject }}
```

## Recomendaciones
- **Orden**: Filter va ANTES de Notion y Slack, así solo procesás lo relevante.
- **Test primero**: Ejecutá manualmente con un email de prueba para validar el mapeo de campos antes de activarlo.
- Si querés, Notion y Slack pueden ir en paralelo (los dos después del Filter) para que se ejecuten juntos.

¿Querés que te arme el JSON del workflow para importarlo directo en N8N, o preferís que te detalle el regex del filtro por si querés agregar más palabras clave?