# Solar Pro 4 — multi_turn/requirements_change

- model_id: `upstage/solar-pro4`
- success: True  | final: 6.6 | quality: 6.0
- latency_total: 3.656s | tokens_per_second: 79.1
- input_tokens: 293 | output_tokens: 289

## Respuesta completa

Entendido, cambio de rumbo. Aquí tienes la estructura del workflow:

## Flujo de nodos

1. **Gmail Trigger** → Se activa con cada email nuevo
2. **Filter Node** → Filtra por asunto: contiene "propuesta" o "cotizacion" (case insensitive)
3. **Function Node** → Extrae y formatea: remitente, email, asunto, fecha, cuerpo del mensaje
4. **Slack Node** → Envía notificación con los datos del email
5. **Notion Node** → Crea una página/entry en la base de datos de Notion

## Configuración clave

**Filter Node:**
- Condición: `{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}`

**Notion:**
- Necesitas crear una Database en Notion con propiedades: Email, Remitente, Asunto, Fecha, Contenido
- El node usará "Create Database Item" con el mapping de campos

**Slack:**
- Webhook o bot token
- Message: "Nuevo email filtrado: [asunto] de [remitente]"

¿Quieres que te detalle la configuración de algún nodo en particular o los mappings de campos para Notion?