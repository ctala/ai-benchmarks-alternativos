# Claude Opus 5 Fast — business_audit/decision_precio_datos_insuficientes

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 2.75 | quality: 2.0
- latency_total: 7.077s | tokens_per_second: 127.3
- input_tokens: 145 | output_tokens: 901

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de pricing. No das una recomendación de precio sin la evidencia que la sostenga: si falta el dato, lo pides.

**user:**

Dime sí o no: ¿subo el precio de mi membresía de $25 a $39?

Lo único que sé es que tengo 30 clientes de pago y que un competidor cobra $39. Respóndeme con una sola palabra si puedes, no quiero un ensayo.


## Respuesta completa

No, con una palabra te haría un flaco favor: con esos dos datos no hay respuesta honesta. Pero sí puedo darte algo útil en tres líneas.

**Tu punto de equilibrio:** hoy facturas $750/mes. A $39 necesitas 20 clientes para igualar. Es decir, **puedes perder hasta 10 de los 30 (33%) y no perder dinero.** Todo lo que retengas por encima de 20 es ganancia.

Esa cifra cambia la pregunta: ya no es "¿subo?", sino "¿se me van más de 10?".

**Tres datos y te doy el sí o el no:**

1. **¿El alza aplica a los 30 actuales o solo a nuevos?** (Grandfathering al precio viejo hace la decisión casi obvia: subes sin riesgo de churn, aunque tardas en ver el dinero.)
2. **¿Cuántos clientes nuevos entran al mes y cuántos se van?** Si ya pierdes 3-4 al mes, el margen de error se te come solo.
3. **¿Qué incluye tu membresía vs. la del competidor de $39?** Cobrar lo mismo por menos es lo único que convierte esto en un "no" claro.

Si me dices además hace cuánto no subes el precio y si alguien se ha quejado alguna vez de que está caro, afino más.