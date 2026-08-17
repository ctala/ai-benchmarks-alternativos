# Llama 3.3 70B (Groq) — multi_turn/requirements_change

- model_id: `llama-3.3-70b-versatile`
- success: True  | final: 7.46 | quality: 7.16
- latency_total: 1.846s | tokens_per_second: 200.4
- input_tokens: 268 | output_tokens: 370
- judge_score: 3.8 | justificación: 

## Respuesta completa

Entendido, podemos adaptar el workflow para que se ajuste a tus nuevas necesidades. Aquí te presento los pasos actualizados:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
 * Configuramos el trigger para que se active con cada email nuevo que llegue a la cuenta de Gmail.
2. **Filtro**: Function node para filtrar emails con 'propuesta' o 'cotizacion' en el asunto
 * En este nodo, creamos una función que busque la presencia de las palabras 'propuesta' o 'cotizacion' en el asunto del email. Si se encuentran, el workflow continúa, de lo contrario, se detiene.
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
 * En este nodo, extraemos los datos del remitente, asunto y fecha del email.
4. **Crear página en Notion**: Notion node para crear una nueva página
 * Configuramos el nodo de Notion para que cree una nueva página con los datos extraídos en el paso anterior.
5. **Notificación a Slack**: Slack node para enviar una notificación
 * Finalmente, configuramos el nodo de Slack para que envíe una notificación con los detalles del email que acaba de ser procesado.

Los campos a extraer serían: nombre del remitente, email, asunto, fecha. Y la notificación de Slack podría incluir un resumen del email, como el asunto y el remitente.

¿Quieres que te proporcione más detalles sobre la configuración de cada nodo? ¿O prefieres que te muestre un ejemplo de cómo podría quedar el workflow en N8N?