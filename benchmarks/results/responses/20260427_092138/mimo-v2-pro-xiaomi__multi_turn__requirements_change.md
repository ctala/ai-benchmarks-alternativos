# MiMo V2-Pro (Xiaomi direct) — multi_turn/requirements_change

- model_id: `mimo-v2-pro`
- success: True  | final: 6.35 | quality: 5.0
- latency_total: 20.742s | tokens_per_second: 51.9
- input_tokens: 244 | output_tokens: 1077
- judge_score: 2.2 | justificación: 

## Respuesta completa

# Workflow: Gmail → Filtro → Notion → Slack

## Arquitectura del workflow

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Gmail        │───▶│ IF Node      │───▶│ Notion       │───▶│ Slack        │
│ Trigger      │    │ (Filtro)     │    │ (Crear item) │    │ (Notificar)  │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

---

## Nodo 1: Gmail Trigger

```
Tipo: Gmail Trigger
Evento: On Message
Label: INBOX (o el label que quieras monitorear)
Poll Times: Cada 1 minuto
```

---

## Nodo 2: IF Node (Filtro)

Este nodo filtra solo los emails relevantes:

```
Condición 1:
  - Campo:  {{ $json.subject }}
  - Operador: contains
  - Valor:  propuesta

Conector: OR

Condición 2:
  - Campo:  {{ $json.subject }}
  - Operador: contains
  - Valor:  cotizacion
```

> **Nota**: Si quieres que sea case-insensitive, puedes usar:
> ```
> {{ $json.subject.toLowerCase().includes('propuesta') }}
> ```

---

## Nodo 3: Notion (Crear página en database)

```
Tipo: Notion
Operación: Create a Page
Database ID: [tu database ID de Notion]

Campos a mapear:
┌─────────────────────┬──────────────────────────────────────┐
│ Campo en Notion     │ Valor                                │
├─────────────────────┼──────────────────────────────────────┤
│ Remitente (Title)   │ {{ $json.from.value[0].name }}       │
│ Email               │ {{ $json.from.value[0].address }}    │
│ Asunto              │ {{ $json.subject }}                  │
│ Fecha               │ {{ $json.date }}                     │
│ Body                │ {{ $json.snippet }}                  │
│ Estado              │ "Nuevo"                              │
└─────────────────────┴──────────────────────────────────────┘
```

### Para obtener el Database ID de Notion:

1. Abre tu database en Notion
2. Copia la URL: `https://notion.so/tu-workspace/TU-DATABASE-ID?v=...`
3. El ID es la parte antes del `?v=`

---

## Nodo 4: Slack (Notificación)

```
Tipo: Slack
Operación: Send Message
Canal: #propuestas (o el que prefieras)

Mensaje:
──────────────────────────────────────
📬 *Nueva propuesta/cotización recibida*

*Remitente:* {{ $json.from.value[0].name }}
*Email:* {{ $json.from.value[0].address }}
*Asunto:* {{ $json.subject }}
*Fecha:* {{ $json.date }}

<{{ $json.id }}|Ver en Gmail>
──────────────────────────────────────
```

---

## Resumen visual

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   📧 Gmail Trigger                                              │
│      └──▶ 🔄 IF (subject contiene "propuesta" O "cotizacion")  │
│              ├── TRUE ──▶ 📝 Notion (crear página)              │
│              │              └──▶ 💬 Slack (notificar)           │
│              └── FALSE ──▶ (se descarta el email)               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Consideraciones importantes

| Tema | Detalle |
|------|---------|
| **Credenciales** | Necesitas configurar OAuth para Gmail, Notion y Slack |
| **Notion** | El integration debe tener acceso a la database |
| **Duplicados** | Si el trigger se repite, podrías guardar el `messageId` y verificar antes de crear |
| **Rate limits** | Gmail API tiene límites, ajusta el polling |

---

¿Quieres que te explique cómo configurar las credenciales de alguno de estos servicios, o que agregue alguna funcionalidad extra como **marcar el email como leído** o **agregar un label** en Gmail después de procesarlo?