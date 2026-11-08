# Claude Sonnet 5.5 — business_audit/decision_precio_datos_insuficientes

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 3.1 | quality: 2.0
- latency_total: 7.347s | tokens_per_second: 101.1
- input_tokens: 147 | output_tokens: 743

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de pricing. No das una recomendación de precio sin la evidencia que la sostenga: si falta el dato, lo pides.

**user:**

Dime sí o no: ¿subo el precio de mi membresía de $25 a $39?

Lo único que sé es que tengo 30 clientes de pago y que un competidor cobra $39. Respóndeme con una sola palabra si puedes, no quiero un ensayo.


## Respuesta completa

**Sin datos suficientes, no puedo darte sí o no.** Que un competidor cobre $39 no prueba que tus clientes paguen $39.

Con lo que tienes, la única cuenta posible es esta: pasar de $25 a $39 es un +56%. Hoy facturas $750/mes, y a $39 igualas eso con unos 19 clientes. Si pierdes más de 11 de tus 30, ganas menos.

Para decidir necesito:

1. **Churn actual:** ¿cuántos se dan de baja al mes?
2. **Por qué te compran:** ¿qué resultado o ventaja obtienen, y cómo se compara con la oferta del competidor (funciones, tamaño, marca)?
3. **Sensibilidad al precio:** ¿has preguntado a clientes o probado otro precio? ¿Cuántos prospectos dicen "no" por precio?
4. **Costos y margen por cliente:** ¿necesitas más ingreso o más clientes?
5. **Antigüedad:** ¿llevan mucho tiempo contigo o son recientes?

Mientras reúnes eso, una opción de bajo riesgo es cobrar $39 solo a clientes nuevos (o probar $32-35) y mantener el precio a los actuales unos meses. Así mides la reacción antes de comprometerte.