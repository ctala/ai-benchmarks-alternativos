# Mistral Nemo — multi_turn/requirements_change

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.37 | quality: 5.48
- latency_total: 8.098s | tokens_per_second: 21.2
- input_tokens: 230 | output_tokens: 172
- judge_score: 2.6 | justificación: 

## Respuesta completa

Entendido, te puedo ayudar a configurar un nuevo workflow con esos requisitos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtrar**: Function node para verificar si el asunto incluye la palabra 'propuesta' o 'cotización'. Si no cumple, el workflow se detiene.
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha y cuerpo del email.
4. **Guardar**: Notion node para agregar una nueva página con los datos extraídos (remitente, asunto, fecha, cuerpo del email)
5. **Notificar**: Slack node para enviar una notificación a un canal específico cada vez que se guarda una nueva página en Notion.

Te puedo ayudar a configurar los nodes de función y la condición en el node de filtrado?