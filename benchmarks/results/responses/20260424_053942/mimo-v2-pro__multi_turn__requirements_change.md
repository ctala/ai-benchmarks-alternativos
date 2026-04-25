# MiMo-V2-Pro — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 5.55 | quality: 4.44
- latency_total: 25.615s | tokens_per_second: 71.3
- input_tokens: 244 | output_tokens: 1827
- judge_score: 1.6 | justificación: 

## Respuesta completa

# Workflow: Gmail → Filtro → Notion + Slack

## Vista general del flujo

```
┌──────────────┐    ┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Gmail        │───▶│ IF          │───▶│ Notion       │───▶│ Slack       │
│ Trigger      │    │ (filtro)    │    │ (guardar)    │    │ (notificar) │
└──────────────┘    └─────────────┘    └──────────────┘    └─────────────┘
```

---

## Nodo 1: Gmail Trigger

```
Credential: Gmail OAuth2
Event:      Message
Poll:       Cada 1 minuto (o lo que prefieras)
```

---

## Nodo 2: IF (Filtro)

Usa **dos condiciones** con operador **OR**:

```
Condición 1:
  - Valor 1:  {{ $json.subject }}
  - Operation: contains
  - Valor 2:  propuesta

Condición 2:
  - Valor 1:  {{ $json.subject }}
  - Operation: contains
  - Valor 2:  cotizacion
```

> **True** → sigue a Notion y Slack
> **False** → se detiene (el email no nos interesa)

---

## Nodo 3: Notion (Create Database Item)

```
Credential:    Notion API
Operation:     Create
Database ID:   <el ID de tu base de datos en Notion>

Campos a mapear:
─────────────────────────────────────────────
  Propiedad en Notion        │  Valor (expresión)
─────────────────────────────────────────────
  Remitente (Title)          │  {{ $json.from.value[0].name }}
  Email                      │  {{ $json.from.value[0].address }}
  Asunto                     │  {{ $json.subject }}
  Fecha                      │  {{ $json.date }}
  Extracto                   │  {{ $json.snippet }}
─────────────────────────────────────────────
```

---

## Nodo 4: Slack (Send Message)

```
Credential: Slack OAuth2
Channel:    #proyectos (o el canal que quieras)
Text:

  📩 *Nuevo email detectado*
  ─────────────────────────
  *De:* {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})
  *Asunto:* {{ $json.subject }}
  *Fecha:* {{ $json.date }}
  *Resumen:* {{ $json.snippet }}
```

---

## Pasos previos importantes

### 1. Credenciales necesarias
```
✅ Gmail OAuth2   → Google Cloud Console → habilitar Gmail API
✅ Notion API      → notion.so/my-integrations → crear integración
                    → compartir la DB con la integración
✅ Slack OAuth2    → api.slack.com → crear app → permisos chat:write
```

### 2. Base de datos en Notion
Crea una DB con estas propiedades:
```
- Remitente  → Title
- Email      → Email
- Asunto     → Text
- Fecha      → Date
- Extracto   → Text
```

---

## JSON completo del workflow (importar directo)

```json
{
  "name": "Gmail → Filtro → Notion + Slack",
  "nodes": [
    {
      "parameters": {
        "pollTimes": { "item": [{ "mode": "everyMinute" }] },
        "filters": {}
      },
      "name": "Gmail Trigger",
      "type": "n8n-nodes-base.gmailTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": { "caseSensitive": false },
          "combinator": "or",
          "conditions": [
            {
              "leftValue": "={{ $json.subject }}",
              "rightValue": "propuesta",
              "operator": { "type": "string", "operation": "contains" }
            },
            {
              "leftValue": "={{ $json.subject }}",
              "rightValue": "cotizacion",
              "operator": { "type": "string", "operation": "contains" }
            }
          ]
        }
      },
      "name": "Filtrar Asunto",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [500, 300]
    },
    {
      "parameters": {
        "operation": "create",
        "databaseId": "<TU_DATABASE_ID>",
        "propertiesUi": {
          "propertyValues": [
            { "key": "Remitente", "titleValue": "={{ $json.from.value[0].name }}" },
            { "key": "Email", "stringValue": "={{ $json.from.value[0].address }}" },
            { "key": "Asunto", "stringValue": "={{ $json.subject }}" },
            { "key": "Fecha", "dateValue": "={{ $json.date }}" },
            { "key": "Extracto", "stringValue": "={{ $json.snippet }}" }
          ]
        }
      },
      "name": "Guardar en Notion",
      "type": "n8n-nodes-base.notion",
      "typeVersion": 2,
      "position": [750, 200]
    },
    {
      "parameters": {
        "channel": "#proyectos",
        "text": "📩 *Nuevo email detectado*\n─────────────────────────\n*De:* {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})\n*Asunto:* {{ $json.subject }}\n*Fecha:* {{ $json.date }}\n*Resumen:* {{ $json.snippet }}"
      },
      "name": "Notificar Slack",
      "type": "n8n-nodes-base.slack",
      "typeVersion": 2,
      "position": [750, 400]
    }
  ],
  "connections": {
    "Gmail Trigger": { "main": [[{ "node": "Filtrar Asunto", "type": "main", "index": 0 }]] },
    "Filtrar Asunto": {
      "main": [
        [
          { "node": "Guardar en Notion", "type": "main", "index": 0 },
          { "node": "Notificar Slack", "type": "main", "index": 0 }
        ],
        []
      ]
    }
  }
}
```

> **Reemplaza** `<TU_DATABASE_ID>` con el ID real de tu base de datos Notion.

---

## Posibles mejoras

| Mejora | Cómo |
|--------|------|
| **Case insensitive** | Ya está configurado con `caseSensitive: false` |
| **Adjuntar archivos** | Agregar nodo HTTP Request para descargar attachments |
| **Evitar duplicados** | Agregar un IF que verifique si el email ya existe en Notion |
| **Etiquetar en Gmail** | Agregar nodo Gmail al final para marcar como procesado |

¿Quieres que profundice en alguna de estas mejoras o que ajuste algo del flujo?