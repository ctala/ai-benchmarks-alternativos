# Muse Glimmer 30B — multi_turn/requirements_change

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 6.9 | quality: 6.0
- latency_total: 0.944s | tokens_per_second: 90.0
- input_tokens: 242 | output_tokens: 85

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico para emprendedores que trabajan con N8N.

**user:**

Necesito un workflow en N8N que lea emails de Gmail, extraiga los datos del remitente, y los guarde en un Google Sheet.

**assistant:**

Perfecto, ese workflow es bastante directo. Te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Extraer datos**: Function node para parsear remitente, asunto, fecha
3. **Guardar**: Google Sheets node para agregar una fila

Los campos a extraer serian: nombre del remitente, email, asunto, fecha. Quieres que te detalle la configuracion de cada nodo?

**user:**

En realidad, cambio de idea. No quiero Google Sheets, quiero que los datos vayan a Notion. Ademas, quiero que el workflow filtre solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Y que me mande una notificacion a Slack cuando llegue uno.


## Respuesta completa

Entendido, cambiamos a Notion + Slack.

El flujo seria:

1. Gmail Trigger
2. IF node para filtrar asunto con 'propuesta' o 'cotizacion'
3. Function node para extraer datos del remitente
4. Notion node para crear pagina
5. Slack node para notificar

¿En qué base de datos de Notion quieres guardar las entradas?