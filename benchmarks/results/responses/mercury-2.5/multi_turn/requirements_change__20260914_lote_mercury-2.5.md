# Mercury 2.5 — multi_turn/requirements_change

- model_id: `inception/mercury-2.5`
- success: True  | final: 5.35 | quality: 4.0
- latency_total: 2.291s | tokens_per_second: 479.2
- input_tokens: 241 | output_tokens: 1098

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



Entendido. El flujo quedaría así:

1.  **Trigger**: Gmail Trigger (monitoriza bandeja de entrada).
2.  **Filtro**: Nodo IF que verifique si el campo 'subject' contiene 'propuesta' o 'cotizacion' (usa expresión regex o string includes).
3.  **Notion**: Conecta a tu base de datos. Mapea remitente, asunto, fecha y enlace al email.
4.  **Slack**: Nodo Send Chat Message para avisar en el canal designado.

¿Quieres que te sugiera cómo configurar las expresiones para el filtro o cómo mapear los campos en Notion?