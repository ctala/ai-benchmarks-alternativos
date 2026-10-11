# Claude Sonnet 5.5 — business_audit/decision_precio_datos_insuficientes

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 3.13 | quality: 2.0
- latency_total: 6.261s | tokens_per_second: 100.1
- input_tokens: 147 | output_tokens: 627

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de pricing. No das una recomendación de precio sin la evidencia que la sostenga: si falta el dato, lo pides.

**user:**

Dime sí o no: ¿subo el precio de mi membresía de $25 a $39?

Lo único que sé es que tengo 30 clientes de pago y que un competidor cobra $39. Respóndeme con una sola palabra si puedes, no quiero un ensayo.


## Respuesta completa

**Todavía no.** Con "30 clientes y un competidor a $39" no hay evidencia para un sí o un no. Un salto de $25 a $39 es +56%, y el precio de un competidor no dice si tus clientes pagarían eso.

Para responderte necesito estos datos:

1. **Churn mensual actual** y antigüedad de tus clientes.
2. **Qué te compran y por qué**: ¿qué dicen cuando les preguntas el valor que reciben?
3. **Comparación real con el competidor**: ¿ofrece lo mismo o más (funciones, marca, base de usuarios)?
4. **Sensibilidad al precio**: ¿alguien se ha quejado del precio, o ha dicho que pagaría más?
5. **Tus costos y margen** por cliente, y cuánto ingreso necesitas.
6. **Cómo captas clientes**: ¿ya hay demanda que sobra o te cuesta cada venta?

Con 30 clientes, además puedes probarlo en vez de adivinar: sube el precio solo a clientes nuevos, o pregunta directamente a 8-10 clientes. Si me pasas lo anterior, te doy el sí o el no.