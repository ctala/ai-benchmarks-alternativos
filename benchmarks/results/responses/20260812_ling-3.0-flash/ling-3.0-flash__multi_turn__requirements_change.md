# Ling 3.0 Flash — multi_turn/requirements_change

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 6.6 | quality: 6.0
- latency_total: 7.131s | tokens_per_second: 375.9
- input_tokens: 266 | output_tokens: 2681
- judge_score: 4.2 | justificación: 

## Respuesta completa

Entendido, el workflow cambia a **Notion** como destino, con **filtro de asunto** y **notificación Slack**. La estructura queda así:

## Arquitectura del Workflow

```
Gmail Trigger → IF (Filtro) → Set (Extraer datos) → Notion (Guardar) → Slack (Notificar)
                                    ↓ (si no coincide)
                                  [Fin]
```

## Configuración detallada por nodo

### 1. **Gmail Trigger**
- Evento: `Watch Emails`
- Carpeta: Inbox (o la que prefieras)
- Credenciales: Tu cuenta de Gmail

### 2. **IF Node** (El filtro clave)
Configura dos condiciones con lógica **OR**:

| Campo | Operación | Valor |
|-------|-----------|-------|
| `Subject` | Contains | `propuesta` |
| `Subject` | Contains | `cotizacion` |

**Importante**: En la configuración del nodo IF, asegúrate de que el conector entre condiciones sea **OR** (no AND).

> **Tip para case-insensitive**: Si N8N no distingue mayúsculas, usa en el campo "Value" la expresión:  
> `{{ $json.subject.toLowerCase() }}` y compara con `propuesta` y `cotizacion` en minúsculas.

### 3. **Set Node** (Extracción de datos)
Crea estos campos para estandarizar la info antes de Notion:

- `nombre_remitente`: `{{ $json.from.split('<')[0].trim() }}` (o usa un Code node si el formato varía)
- `email_remitente`: `{{ $json.from.match(/<(.+?)>/)?.[1] || '' }}`
- `asunto`: `{{ $json.subject }}`
- `fecha`: `{{ $json.date }}`
- `cuerpo`: `{{ $json.textPlain }}` (opcional)

### 4. **Notion Node** (Crear registro)
- **Operation**: `Create a Database Item`
- **Database ID**: El ID de tu base de datos Notion (lo encuentras en la URL del Notion database)
- **Properties** (mapea estos campos):
  - `Name` → `{{ $json.asunto }}`
  - `Remitente` (tipo Title/Text) → `{{ $json.nombre_remitente }}`
  - `Email` (type Email) → `{{ $json.email_remitente }}`
  - `Fecha` (type Date) → `{{ $json.fecha }}`
  - `Estado` (type Select) → `"Nuevo"` (o el estado que prefieras)

> **Requisito previo**: Debes tener ya creada una base de datos en Notion con esas propiedades. N8N necesita que el usuario que autentica tenga acceso de editor a esa base de datos.

### 5. **Slack Node** (Notificación)
- **Operation**: `Post Message`
- **Channel**: `#tu-canal` (o el ID del canal)
- **Text**: 
```
📧 Nueva propuesta/cotización recibida
*De:* {{ $json.nombre_remitente }} ({{ $json.email_remitente }})
*Asunto:* {{ $json.asunto }}
*Fecha:* {{ $json.fecha }}
```

## Consideraciones importantes

1. **Credentials**: Necesitas configurar credenciales para Gmail, Notion (OAuth2) y Slack (Bot Token)
2. **Notion Database**: El workflow solo funcionará si la base de datos ya existe y tiene las propiedades configuradas (especialmente el tipo de dato para email si quieres que Notion lo reconozca como tal)
3. **Manejo de errores**: Considera añadir un nodo **Error Trigger** o **IF** de fallback por si falla la inserción en Notion (quizás reintentar o enviar alerta a otro canal)

¿Quieres que te detalle cómo configurar la expresión regex para extraer correctamente el nombre y email del campo `from` de Gmail, o prefieres que use un Code node con JavaScript para un parsing más robusto?