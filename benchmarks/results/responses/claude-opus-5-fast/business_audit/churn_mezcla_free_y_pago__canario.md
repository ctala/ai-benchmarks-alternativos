# Claude Opus 5 Fast — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 3.92 | quality: 4.0
- latency_total: 10.742s | tokens_per_second: 190.7
- input_tokens: 262 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

## Respuesta corta

Tu churn de pago es 9,1% (2 de 22), no 31%. Pero tampoco puedes afirmar que sea 9,1%, y esa es la parte incómoda.

## Qué está midiendo realmente ese 31%

| Segmento | Inicio | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | 33,7% |
| Pago | 22 | 2 | 9,1% |
| Mezclado | 200 | 62 | 31,0% |

El 31% es aritméticamente correcto y operativamente inútil. El 89% de tu base es gratuita, así que el número mezclado es esencialmente "tasa de abandono del plan gratuito" con un poco de ruido de pago encima. Si mañana duplicas tus registros gratuitos, tu "churn" subirá aunque no pierdas ni un cliente de pago. Es una métrica que se mueve por razones que no tienen que ver con la salud del negocio.

Primera pregunta que deberías responderte: **ese 5% que tenías en la cabeza, ¿de dónde salía?**