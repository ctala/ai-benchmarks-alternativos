# Llama 3.3 70B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta-llama/llama-3.3-70b-instruct`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 3.602s | tokens_per_second: 88.0
- input_tokens: 218 | output_tokens: 317

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

No le doy.

Tienes un error en el cálculo del LTV. El churn mensual es del 8%, lo que significa que la tasa de retención mensual es del 92%. Para calcular el LTV, debes considerar la tasa de retención.

La fórmula para calcular el LTV es:

LTV = Precio mensual x Margen bruto x (1 / (1 - Tasa de retención mensual))

Donde la tasa de retención mensual es 0,92 (1 - 0,08).

LTV = 35 x 0,7 x (1 / (1 - 0,92))
LTV = 35 x 0,7 x (1 / 0,08)
LTV = 35 x 0,7 x 12,5
LTV = 306,25

Ahora, calculemos el LTV/CAC:

LTV/CAC = 306,25 / 290
LTV/CAC = 1,056

Este resultado es mucho menor que el 3 que mencionas. Esto significa que, con estos números, estás gastando más en adquirir un cliente de lo que esperas ganar con él a largo plazo.

No te recomiendo invertir $10.000 en publicidad con estos números. Deberías reconsiderar tu estrategia de adquisición de clientes o intentar reducir el CAC para mejorar la rentabilidad.