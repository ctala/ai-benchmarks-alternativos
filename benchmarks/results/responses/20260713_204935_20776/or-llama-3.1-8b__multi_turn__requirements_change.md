# Llama 3.1 8B Instant — multi_turn/requirements_change

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 6.75 | quality: 6.0
- latency_total: 2.045s | tokens_per_second: 144.2
- input_tokens: 249 | output_tokens: 295
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de guardar datos en Google Sheets, sino que introduce Notion, lo que reduce la precisión y relevancia; sin embargo, la estructura y claridad son adecuadas.

## Respuesta completa

Entendido, un poco más complejo pero aún así es un workflow manejable. Aquí te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Filtro**: Filter node (aplicar filtro para incluir solo emails con 'propuesta' o 'cotización' en el asunto)
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
4. **Notificación**: Slack node para enviar notificación cuando llegue un email que cumpla con el filtro
5. **Guardar**: Notion node para agregar datos a una base de datos en Notion

Configura el Trigger de Gmail para leer los emails de tu cuenta de Gmail. Luego, en el node Filter, configura la condición para que solo incluya emails con 'propuesta' o 'cotización' en el asunto. En el node Function, configura la extracción de los campos que necesitas (nombre del remitente, email, asunto, fecha). En el node Slack, configura el canal de Slack y el mensaje que se enviará cuando llegue un email que cumpla con el filtro. Finalmente, en el node Notion, configura la base de datos y la página donde se insertará el nuevo registro.

¿Necesitas ayuda con la configuración de algún nodo en particular?