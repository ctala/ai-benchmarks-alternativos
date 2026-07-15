# Claude Haiku 4.5 — multi_turn/requirements_change

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 6.15 | quality: 6.0
- latency_total: 4.577s | tokens_per_second: 82.6
- input_tokens: 264 | output_tokens: 378
- judge_score: 3.0 | justificación: La respuesta es parcialmente precisa y clara, pero no cumple con los requisitos originales de guardar datos en Google Sheets, en su lugar usa Notion y Slack, lo que reduce su relevancia y utilidad práctica.

## Respuesta completa

Excelente, así es más útil. Te dejo el flujo completo:

## Workflow en N8N:

### 1. **Trigger: Gmail**
- Configura para que lea emails nuevos
- No hay filtro aquí, lo hacemos después

### 2. **Filter Node** (Condicional)
```
Condición: subject contiene "propuesta" OR "cotizacion"
```
- Solo continúa si se cumple

### 3. **Function Node** (Extrae datos)
```javascript
return {
  from_name: $input.first().json.from.name,
  from_email: $input.first().json.from.email,
  subject: $input.first().json.subject,
  date: $input.first().json.date,
  snippet: $input.first().json.snippet.substring(0, 200)
};
```

### 4. **Notion Node** (Guarda en BD)
- Selecciona tu database de Notion
- Mapea los campos extraídos a las propiedades de Notion

### 5. **Slack Node** (Notificación)
- Canal: elige donde notificar
- Mensaje: `Nuevo email de {{from_name}} ({{from_email}}) - Asunto: {{subject}}`

---

**Consejo**: Usa el modo "Always Output Data" en el Filter para que no se rompa el flujo si no hay coincidencias.

¿Necesitas ayuda con la configuración de algún nodo específico?