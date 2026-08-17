# MiMo-V2.5 Pro — multi_turn/requirements_change

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 5.99 | quality: 4.84
- latency_total: 13.771s | tokens_per_second: 64.5
- input_tokens: 244 | output_tokens: 888
- judge_score: 2.4 | justificación: 

## Respuesta completa

¡Perfecto, entendido! Esa es una combinación muy útil para seguimiento comercial. El flujo quedaría así:

**Workflow: Gmail (filtrado) → Notion + Slack**

1. **Trigger**: Gmail Trigger (igual que antes)
2. **Filtro**: IF Node para verificar si el asunto contiene "propuesta" o "cotización"
3. **Procesar**: Function Node para extraer datos del email
4. **Guardar**: Notion Node para crear item en tu base de datos
5. **Notificar**: Slack Node para enviar mensaje al canal

**Configuración detallada:**

**1. Gmail Trigger:**
- Credenciales: Tu cuenta de Gmail
- Filtro: `is:unread` (opcional)

**2. IF Node (Filtro):**
- Condición 1: `{{ $json["subject"].toLowerCase().includes("propuesta") }}`
- Condición 2: `{{ $json["subject"].toLowerCase().includes("cotización") }}`
- Operador: OR (pasar si cumple cualquiera)

**3. Function Node:**
```javascript
// Extraer datos del remitente
const from = $input.item.json.from;
const nameMatch = from.match(/^(.*?)\s*<.*>/);
const emailMatch = from.match(/<(.*)>/);

return {
  nombre: nameMatch ? nameMatch[1] : from,
  email: emailMatch ? emailMatch[1] : from,
  asunto: $input.item.json.subject,
  fecha: $input.item.json.date,
  snippet: $input.item.json.snippet
};
```

**4. Notion Node:**
- Acción: "Create database item"
- Database ID: Tu base de datos de Notion
- Mapeo de propiedades:
  - Nombre → `{{ $json.nombre }}`
  - Email → `{{ $json.email }}`
  - Asunto → `{{ $json.asunto }}`
  - Fecha → `{{ $json.fecha }}`

**5. Slack Node:**
- Canal: Tu canal de ventas/soporte
- Mensaje:
```
📧 Nueva propuesta/cotización recibida
De: {{ $json.nombre }} ({{ $json.email }})
Asunto: {{ $json.asunto }}
Fecha: {{ $json.fecha }}
Snippet: {{ $json.snippet }}
```

**Requisitos previos:**
- Credenciales configuradas para Gmail, Notion y Slack
- Base de datos de Notion creada con las propiedades adecuadas
- Permiso para el bot de Slack en tu workspace

¿Quieres que te explique cómo configurar las credenciales o la estructura de Notion en detalle?