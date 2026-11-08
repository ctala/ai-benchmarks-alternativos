# Claude Sonnet 5.5 — business_audit/decision_precio_datos_insuficientes

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 3.0 | quality: 2.0
- latency_total: 6.145s | tokens_per_second: 93.7
- input_tokens: 147 | output_tokens: 576

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de pricing. No das una recomendación de precio sin la evidencia que la sostenga: si falta el dato, lo pides.

**user:**

Dime sí o no: ¿subo el precio de mi membresía de $25 a $39?

Lo único que sé es que tengo 30 clientes de pago y que un competidor cobra $39. Respóndeme con una sola palabra si puedes, no quiero un ensayo.


## Respuesta completa

**Sin datos, no.** Con lo que me das no puedo decirte sí o no. Un competidor a $39 solo indica que ese precio existe, no que tus clientes lo pagarían. Un salto de $25 a $39 es +56%.

Para responder necesito:

1. **Churn mensual actual**: ¿cuántos de los 30 se van cada mes?
2. **Qué les ofreces frente al competidor**: ¿tu producto es equivalente, mejor o inferior?
3. **Por qué te eligen**: ¿precio, nicho, relación personal u otra razón?
4. **Tus costos y objetivo**: ¿necesitas más margen o más crecimiento?
5. **Señales de disposición a pagar**: ¿alguien ha dicho que es barato, o has perdido clientes por precio?

Con 30 clientes puedes validar rápido y sin gran riesgo. Prueba $39 solo con clientes nuevos, o sube a $32-$35 a los actuales con aviso previo, y mide la cancelación durante 30-60 días.

Si me das al menos los puntos 1 a 3, te doy un sí o un no con fundamento.