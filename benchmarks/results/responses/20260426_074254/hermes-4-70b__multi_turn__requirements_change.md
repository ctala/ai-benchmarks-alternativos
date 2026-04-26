# Hermes 4 70B — multi_turn/requirements_change

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 6.84 | quality: 6.84
- latency_total: 5.649s | tokens_per_second: 28.5
- input_tokens: 248 | output_tokens: 161
- judge_score: 3.6 | justificación: 

## Respuesta completa

Claro! Entonces el workflow quedaria asi:

1. **Trigger**: Gmail Trigger (trigger con cada email nuevo)
2. **Filtro**: IF node para chequear si el asunto contiene 'propuesta' o 'cotizacion'
   * If: `{{ $json.asunto.toLowerCase().includes('propuesta') || $json.asunto.toLowerCase().includes('cotizacion') }}`
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Notion**: Notion node para crear un registro
5. **Slack**: Slack node para mandar notificacion

Dime si quieres que te detalle la configuracion de cada nodo, especialmente la parte del Function node y como estructurar los datos para Notion.