# Kimi K3 — multi_turn/requirements_change

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 3.88 | quality: 4.0
- latency_total: 44.21s | tokens_per_second: 39.3
- input_tokens: 374 | output_tokens: 1738
- judge_score: 1 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en un Google Sheet, sino que usa Notion y Slack, lo que la hace irrelevante y poco precisa.

## Respuesta completa

Perfecto, el workflow queda así:

**Gmail Trigger → IF (filtro) → Notion → Slack**

Te detallo cada nodo:

## 1. Gmail Trigger
- **Event**: Message Received
- **Poll interval**: cada minuto (o el que prefieras)
- **Tip**: puedes filtrar directamente aquí usando la búsqueda de Gmail en *Filters → Search*:
  ```
  subject:(propuesta OR cotizacion)
  ```
  Esto es más eficiente porque Gmail hace el filtrado. Aun así, te recomiendo mantener el IF node como respaldo y para mayor claridad.

## 2. IF (filtro por asunto)
- Condición 1: `{{ $json.Subject }}` → *contains* → `propuesta`
- Condición 2 (OR): `{{ $json.Subject }}` → *contains* → `cotizacion`
- Activa la opción **ignore case** para que no importe si viene en mayúsculas.

## 3. Notion
- **Resource**: Database Page → **Operation**: Create
- **Campos a mapear**: Nombre, Email, Asunto, Fecha

Ojo con esto: Gmail devuelve el remitente como `Juan Pérez <juan@empresa.com>`. Para separarlo, usa estas expresiones:
```
Nombre: {{ $json.From.split('<')[0].trim() }}
Email:  {{ $json.From.split('<')[1].replace('>', '') }}
```

**Requisitos previos en Notion:**
- Crear la base de datos con las propiedades (el Email debe ser tipo *Email*, la Fecha tipo *Date*)
- Crear una integración en notion.so/my-integrations y **compartir la base de datos con esa integración** (esto es lo que más se olvida y causa el error "database not found")

## 4. Slack
- **Resource**: Message → **Operation**: Post
- Ejemplo de mensaje:
  ```
  📩 Nueva oportunidad de *{{ $json.From.split('<')[0].trim() }}*
  Asunto: {{ $json.Subject }}
  Email: {{ $json.From.split('<')[1].replace('>', '') }}
  ```

¿Quieres que te pase el JSON del workflow completo para importarlo directo en tu instancia de N8N?