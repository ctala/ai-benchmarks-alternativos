# Hermes 4 405B — multi_turn/requirements_change

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 6.93 | quality: 6.52
- latency_total: 4.642s | tokens_per_second: 34.9
- input_tokens: 248 | output_tokens: 162
- judge_score: 3.6 | justificación: 

## Respuesta completa

Muy bien, ajustemos el workflow a tus nuevos requisitos:

1. **Trigger**: Gmail Trigger (encendido con cada email nuevo)
2. **Filtro**: IF node para chequear si el asunto contiene 'propuesta' o 'cotizacion'
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Guardar**: Notion node para crear una pagina nueva en una base de datos existente
5. **Notificar**: Slack node para mandar un mensaje con los detalles del email

Ahora, si quieres te explico con mas detalle la configuracion de cada nodo, especialmente la parte de la funcion para extraer los datos y la integracion con Notion que puede ser un poco mas compleja.