# Llama 4 Maverick — multi_turn/requirements_change

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 6.0 | quality: 6.0
- latency_total: 15.999s | tokens_per_second: 35.7
- input_tokens: 230 | output_tokens: 571
- judge_score: 5 | justificación: La respuesta es precisa, relevante y mantiene el contexto, ofreciendo una guía detallada y útil para adaptar el workflow a los nuevos requisitos, con claridad y profundidad adecuadas.

## Respuesta completa

**Adaptación del Workflow**

El workflow se puede adaptar para cumplir con tus nuevos requisitos. A continuación, te presento los pasos actualizados:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
 * Configura el nodo para que se conecte a tu cuenta de Gmail y especifique la carpeta o etiqueta que deseas monitorear.
2. **Filtrar emails**: IF node para filtrar emails según el asunto
 * Configura el nodo para que verifique si el asunto del email contiene las palabras "propuesta" o "cotización" (puedes utilizar una expresión regular para lograr esto).
3. **Extraer datos**: Function node para parsear remitente, asunto, fecha
 * Utiliza JavaScript para extraer los datos necesarios del email, como el nombre del remitente, el email, el asunto y la fecha.
4. **Guardar en Notion**: Notion node para agregar una nueva página o actualizar una existente
 * Configura el nodo para que se conecte a tu cuenta de Notion y especifique la base de datos o la página donde deseas guardar los datos.
5. **Notificación en Slack**: Slack node para enviar una notificación
 * Configura el nodo para que se conecte a tu cuenta de Slack y especifique el canal o el usuario que deseas notificar.

**Detalles de configuración**

* En el nodo de Gmail Trigger, debes configurar la conexión a tu cuenta de Gmail y especificar la carpeta o etiqueta que deseas monitorear.
* En el nodo IF, puedes utilizar una expresión regular como `{{ $json.subject.toLowerCase().includes('propuesta') || $json.subject.toLowerCase().includes('cotizacion') }}` para filtrar los emails según el asunto.
* En el nodo Function, puedes utilizar JavaScript para extraer los datos necesarios del email. Por ejemplo:
```javascript
const remitente = $json.from;
const asunto = $json.subject;
const fecha = $json.date;

return {
  remitente: remitente,
  asunto: asunto,
  fecha: fecha
};
```
* En el nodo Notion, debes configurar la conexión a tu cuenta de Notion y especificar la base de datos o la página donde deseas guardar los datos.
* En el nodo Slack, debes configurar la conexión a tu cuenta de Slack y especificar el canal o el usuario que deseas notificar.

**Conclusión**

Con estos pasos, puedes crear un workflow en N8N que lea emails de Gmail, filtre aquellos que contengan las palabras "propuesta" o "cotización" en el asunto, extraiga los datos del remitente y los guarde en Notion, y te envíe una notificación a Slack cuando llegue uno de esos emails. ¿Quieres que te ayude con la configuración específica de cada nodo?