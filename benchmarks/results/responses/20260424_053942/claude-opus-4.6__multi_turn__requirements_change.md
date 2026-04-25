# Claude Opus 4.6 — multi_turn/requirements_change

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 5.92 | quality: 4.64
- latency_total: 23.614s | tokens_per_second: 65.2
- input_tokens: 265 | output_tokens: 1540
- judge_score: 2.0 | justificación: 

## Respuesta completa

# Workflow N8N: Gmail → Filtro → Notion + Slack

Perfecto, te armo el workflow completo con los cambios. Son 4 nodos conectados así:

```
Gmail Trigger → IF (Filtro) → Notion (Guardar)
                                    ↓
                              Slack (Notificar)
```

---

## Nodo 1: Gmail Trigger

**Tipo:** Gmail Trigger

```
Configuración:
├── Credential: Tu cuenta Gmail (OAuth2)
├── Poll Times: Every Minute (o el intervalo que prefieras)
├── Filters:
│   └── Label: INBOX
└── Options:
    └── Mark as Read: true (opcional, para no reprocesar)
```

> **Dato importante:** Activa el acceso a la API de Gmail en Google Cloud Console y configura las credenciales OAuth2 en N8N.

---

## Nodo 2: IF (Filtro por Asunto)

**Tipo:** IF

```json
{
  "conditions": {
    "options": {
      "caseSensitive": false,
      "leftValue": "",
      "typeValidation": "loose"
    },
    "combinator": "or",
    "conditions": [
      {
        "id": "condition_1",
        "leftValue": "={{ $json.subject }}",
        "rightValue": "propuesta",
        "operator": {
          "type": "string",
          "operation": "contains"
        }
      },
      {
        "id": "condition_2",
        "leftValue": "={{ $json.subject }}",
        "rightValue": "cotización",
        "operator": {
          "type": "string",
          "operation": "contains"
        }
      },
      {
        "id": "condition_3",
        "leftValue": "={{ $json.subject }}",
        "rightValue": "cotizacion",
        "operator": {
          "type": "string",
          "operation": "contains"
        }
      }
    ]
  }
}
```

> **Nota:** Se incluye "cotización" y "cotizacion" (con y sin tilde) para no perder emails.

---

## Nodo 3: Notion (Guardar en Base de Datos)

**Tipo:** Notion

```
Configuración:
├── Credential: Tu integración de Notion (API Key)
├── Resource: Database Page
├── Operation: Create
├── Database ID: [ID de tu base de datos en Notion]
│
└── Properties (mapeo de columnas):
    │
    ├── Nombre Remitente (Title):
    │   └── {{ $json.from.value[0].name }}
    │
    ├── Email (Email / Rich Text):
    │   └── {{ $json.from.value[0].address }}
    │
    ├── Asunto (Rich Text):
    │   └── {{ $json.subject }}
    │
    ├── Fecha (Date):
    │   └── {{ $json.date }}
    │
    └── Estado (Select):
        └── "Pendiente de revisión"
```

### Preparación en Notion:

Crea una base de datos con estas columnas:

| Columna            | Tipo en Notion |
|--------------------|----------------|
| Nombre Remitente   | Title          |
| Email              | Email          |
| Asunto             | Rich Text      |
| Fecha              | Date           |
| Estado             | Select         |

---

## Nodo 4: Slack (Notificación)

**Tipo:** Slack

```
Configuración:
├── Credential: Tu Bot de Slack (OAuth2)
├── Resource: Message
├── Operation: Send
├── Channel: #leads (o el canal que prefieras)
│
└── Message (Block Kit / Text):
```

```
🔔 *Nuevo email con propuesta/cotización*

👤 *Remitente:* {{ $('Notion').item.json.from.value[0].name }}
📧 *Email:* {{ $('Notion').item.json.from.value[0].address }}
📋 *Asunto:* {{ $('Notion').item.json.from.value[0].subject }}
📅 *Fecha:* {{ $('Notion').item.json.date }}

✅ Ya fue registrado en Notion.
```

---

## Flujo Visual Completo

```
┌──────────────┐
│ Gmail Trigger │
│ (cada minuto) │
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│     IF - Filtro por Asunto   │
│ contiene "propuesta"    OR   │
│ contiene "cotización"   OR   │
│ contiene "cotizacion"        │
└──────┬───────────┬───────────┘
       │ TRUE      │ FALSE
       ▼           ▼
┌─────────────┐  (se descarta)
│   Notion    │
│ Crear Page  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Slack    │
│  Notificar  │
└─────────────┘
```

---

## Checklist antes de activar

- [ ] Credenciales de Gmail configuradas (OAuth2)
- [ ] Credenciales de Notion configuradas (Integration Token)
- [ ] Base de datos de Notion creada con las columnas indicadas
- [ ] Compartir la base de datos con tu integración de Notion
- [ ] Credenciales de Slack configuradas (Bot Token)
- [ ] Bot de Slack añadido al canal destino
- [ ] Ejecutar prueba manual con un email de prueba
- [ ] Activar el workflow

---

¿Necesitas que te detalle cómo configurar alguna de las credenciales (Gmail, Notion o Slack) o quieres que le agreguemos algo más al workflow, como por ejemplo extraer archivos adjuntos?