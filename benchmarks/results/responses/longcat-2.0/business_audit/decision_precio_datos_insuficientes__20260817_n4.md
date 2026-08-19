# LongCat 2.0 — business_audit/decision_precio_datos_insuficientes

- model_id: `meituan/longcat-2.0`
- success: True  | final: 3.11 | quality: 2.0
- latency_total: 14.626s | tokens_per_second: 26.5
- input_tokens: 110 | output_tokens: 388

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de pricing. No das una recomendación de precio sin la evidencia que la sostenga: si falta el dato, lo pides.

**user:**

Dime sí o no: ¿subo el precio de mi membresía de $25 a $39?

Lo único que sé es que tengo 30 clientes de pago y que un competidor cobra $39. Respóndeme con una sola palabra si puedes, no quiero un ensayo.


## Respuesta completa

No puedo responder "sí" o "no" con una sola palabra porque falta evidencia crítica.

Necesito estos datos para darte una recomendación:

1. **Costo de adquisición de clientes (CAC)** y **costo de servicio por cliente**
2. **Tasa de cancelación (churn)** actual y la que estimas con el nuevo precio
3. **Valor de vida del cliente (LTV)** actual
4. **Elasticidad de la demanda**: ¿cuántos clientes crees que perderías con cada incremento de precio?
5. **Segmentación**: ¿tus 30 clientes son todos iguales o hay segmentos con diferente disposición a pagar?
6. **Valor percibido**: ¿qué diferenciador tienes frente al competidor que cobra $39?

Sin esto, subir de $25 a $39 (56% de aumento) es una decisión ciega que podría reducir tus ingresos totales o destruir tu base de clientes. Dame los datos y te daré una respuesta con evidencia.