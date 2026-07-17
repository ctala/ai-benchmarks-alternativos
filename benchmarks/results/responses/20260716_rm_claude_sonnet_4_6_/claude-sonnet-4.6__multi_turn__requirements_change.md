# Claude Sonnet 4.6 (ultimo Anthropic) — multi_turn/requirements_change

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 5.52 | quality: 6.0
- latency_total: 18.674s | tokens_per_second: 57.2
- input_tokens: 265 | output_tokens: 1068
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de leer emails de Gmail, extraer datos del remitente y guardarlos en un Google Sheet, en su lugar, introduce un flujo de trabajo diferente que involucra Notion y Slack, lo que la hace irrelevante y poco precisa en el contexto dado.

## Respuesta completa

# Workflow N8N: Gmail → Filtro → Notion + Slack

## Arquitectura del Workflow

```
Gmail Trigger → IF (filtro asunto) → Notion (crear página) → Slack (notificación)
                      ↓
                 [No match] → Stop
```

---

## Nodo 1: Gmail Trigger

**Tipo:** `Gmail Trigger`

**Configuración:**
```
- Event: Message Received
- Credentials: Tu cuenta Gmail (OAuth2)
- Poll Times: cada 5 minutos (o el intervalo que prefieras)
```

---

## Nodo 2: IF - Filtrar por asunto

**Tipo:** `IF`

**Condiciones (OR entre ambas):**
```
Condición 1:
  - Value 1: {{ $json.subject.toLowerCase() }}
  - Operation: Contains
  - Value 2: propuesta

Condición 2:
  - Value 1: {{ $json.subject.toLowerCase() }}
  - Operation: Contains
  - Value 2: cotizacion
```

> ⚠️ Usar `.toLowerCase()` evita problemas con mayúsculas/minúsculas

---

## Nodo 3: Notion - Crear página

**Tipo:** `Notion`
**Operation:** `Create Page`

**Configuración de propiedades:**
```json
{
  "Nombre": {
    "type": "title",
    "value": "{{ $json.from.name }} - {{ $json.subject }}"
  },
  "Email Remitente": {
    "type": "email",
    "value": "{{ $json.from.value[0].address }}"
  },
  "Asunto": {
    "type": "rich_text",
    "value": "{{ $json.subject }}"
  },
  "Fecha Recibido": {
    "type": "date",
    "value": "{{ $json.date }}"
  },
  "Tipo": {
    "type": "select",
    "value": "{{ $json.subject.toLowerCase().includes('propuesta') ? 'Propuesta' : 'Cotización' }}"
  }
}
```

> 📌 Asegúrate de tener una base de datos en Notion creada con esas columnas antes de conectar

---

## Nodo 4: Slack - Notificación

**Tipo:** `Slack`
**Operation:** `Send Message`

**Configuración:**
```
- Channel: #nombre-de-tu-canal (ej: #ventas o #leads)
- Message Type: Text

- Text:
🚨 *Nuevo email importante recibido*

👤 *De:* {{ $json.from.name }} ({{ $json.from.value[0].address }})
📧 *Asunto:* {{ $json.subject }}
📅 *Fecha:* {{ $json.date }}
🏷️ *Tipo:* {{ $json.subject.toLowerCase().includes('propuesta') ? 'Propuesta' : 'Cotización' }}

✅ Guardado en Notion automáticamente.
```

---

## Checklist antes de activar

- [ ] Credenciales de **Gmail OAuth2** configuradas
- [ ] Credenciales de **Notion API** configuradas (Integration Token)
- [ ] Base de datos de Notion **compartida** con tu integración
- [ ] ID de la base de datos Notion copiado correctamente
- [ ] Bot de **Slack** agregado al canal destino
- [ ] Credenciales de **Slack OAuth2** configuradas

---

## Tips adicionales

| Situación | Solución |
|---|---|
| Emails con tilde (cotización) | Agrega también `cotizaci` como filtro alternativo |
| Quieres guardar el cuerpo del email | Agrega campo `Body` en Notion con `{{ $json.text }}` |
| Demasiadas notificaciones | Agrega nodo `Wait` o filtra por dominio del remitente |
| Quieres evitar duplicados | Agrega nodo `Notion Search` antes de crear la página |

¿Quieres que agregue algo más, como guardar adjuntos o clasificar por tipo de cliente?