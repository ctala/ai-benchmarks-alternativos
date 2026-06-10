# Claude Fable 5 (suscripción) — multi_turn/requirements_change

- model_id: `claude-fable-5`
- success: True  | final: 5.59 | quality: 6.4
- latency_total: 15.784s | tokens_per_second: 71.7
- input_tokens: 2 | output_tokens: 1132

## Respuesta completa

Perfecto, queda así el flujo actualizado:

**Gmail Trigger → IF (filtro) → Notion → Slack**

## 1. Gmail Trigger

- Event: **Message Received**
- Poll Times: cada minuto (o el intervalo que prefieras)
- Opcional: en "Filters" puedes poner directamente `subject:(propuesta OR cotizacion)` usando la sintaxis de búsqueda de Gmail. Esto filtra en origen y te ahorras procesar emails irrelevantes.

> Tip: si usas el filtro nativo de Gmail, el nodo IF se vuelve redundante. Pero te dejo ambas opciones por si quieres lógica más compleja después.

## 2. IF Node (filtro alternativo en n8n)

Si prefieres filtrar dentro del workflow:

- Condición tipo **String** con OR (agrega 2 condiciones, combinador "Any"):
  - `{{ $json.subject.toLowerCase() }}` → contains → `propuesta`
  - `{{ $json.subject.toLowerCase() }}` → contains → `cotizacion`

El `.toLowerCase()` es importante: "Propuesta" y "PROPUESTA" no matchean si comparas literal.

## 3. Notion Node

- Operation: **Create** → Database Page
- Necesitas crear primero la base de datos en Notion con estas propiedades:
  - **Nombre** (Title)
  - **Email** (Email)
  - **Asunto** (Text)
  - **Fecha** (Date)
- Mapeo de campos desde el Gmail Trigger:
  - Nombre: `{{ $json.from.value[0].name }}`
  - Email: `{{ $json.from.value[0].address }}`
  - Asunto: `{{ $json.subject }}`
  - Fecha: `{{ $json.date }}`

> Gotcha: la estructura del campo `from` varía según si el Gmail Trigger tiene "Simplify" activado o no. Con Simplify ON suele ser `$json.from` directo como string. Ejecuta el trigger una vez y revisa el output real antes de mapear.

## 4. Slack Node

- Operation: **Send Message**
- Channel: el que elijas
- Texto sugerido:

```
📨 Nueva propuesta/cotización recibida
De: {{ $json.from.value[0].name }} ({{ $json.from.value[0].address }})
Asunto: {{ $json.subject }}
```

Conéctalo **después de Notion** (no en paralelo) para que la notificación solo llegue si el guardado fue exitoso.

## Credenciales necesarias

1. **Gmail**: OAuth2 (Google Cloud Console → habilitar Gmail API)
2. **Notion**: integración interna en notion.so/my-integrations + **compartir la database con la integración** (error más común: la integración existe pero no tiene acceso a la base)
3. **Slack**: app de Slack con scope `chat:write` + invitar el bot al canal

¿Quieres que te genere el JSON completo del workflow para importarlo directo en n8n?