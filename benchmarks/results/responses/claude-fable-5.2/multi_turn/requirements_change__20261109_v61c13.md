# Claude Fable 5.2 — multi_turn/requirements_change

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 3.81 | quality: 4.0
- latency_total: 20.14s | tokens_per_second: 98.6
- input_tokens: 365 | output_tokens: 1985

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

Con esos cambios, el workflow queda así:

**Gmail Trigger → Filter → Edit Fields → Notion → Slack**

## 1. Gmail Trigger
- **Event**: Message Received
- **Poll Times**: Every Minute (o el intervalo que prefieras)
- **Simplify**: desactivado, para que el remitente llegue separado en nombre y email

## 2. Filter
Deja pasar solo los emails con "propuesta" o "cotizacion" en el asunto:
- **Value 1**: `{{ $json.subject }}`
- **Operación**: String → Matches Regex
- **Regex**: `/propuesta|cotizaci[oó]n/i`

El regex ignora mayúsculas y acepta "cotización" con o sin tilde.

## 3. Edit Fields (Set)
Reemplaza al Function node, porque no hace falta código:

| Campo | Valor |
|---|---|
| `nombre` | `{{ $json.from.value[0].name \|\| $json.from.value[0].address }}` |
| `email` | `{{ $json.from.value[0].address }}` |
| `asunto` | `{{ $json.subject }}` |
| `fecha` | `{{ $json.date }}` |

Si el remitente no tiene nombre, `nombre` usa el email.

## 4. Notion
Antes de configurar el nodo, crea una base de datos en Notion con estas propiedades:
- **Nombre** (Title)
- **Email** (Email)
- **Asunto** (Text)
- **Fecha** (Date)

Después comparte la base de datos con tu integración de Notion (menú `···` → Connections). Si no lo haces, N8N no la verá.

En el nodo:
- **Resource**: Database Page
- **Operation**: Create
- **Database**: selecciona la tuya
- **Properties**: asigna cada propiedad al campo correspondiente del paso 3

## 5. Slack
- **Resource**: Message
- **Operation**: Send
- **Channel**: el canal donde quieres el aviso
- **Text**:

```
📩 Nueva propuesta/cotización
*De:* {{ $('Edit Fields').item.json.nombre }} ({{ $('Edit Fields').item.json.email }})
*Asunto:* {{ $('Edit Fields').item.json.asunto }}
```

Uso `$('Edit Fields')` en lugar de `$json` porque, después del nodo de Notion, `$json` contiene la respuesta de Notion y no los datos del email.

¿Quieres que te ayude con las credenciales de Notion o de Slack?