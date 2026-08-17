# Sakana Namazu — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/sakana-namazu`
- success: True  | final: 6.28 | quality: 6.67
- latency_total: 12.629s | tokens_per_second: 162.2
- input_tokens: 231 | output_tokens: 2048

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

No. No le metas los $10.000 todavía. Tu plan muere en la aritmética.

Hay dos errores que hacen que tu LTV/CAC real no esté en ~2,9, sino en **~1,05x**. Es decir: apenas recuperas lo que invertiste y te quedas sin margen para operar. Te rompo los números:

### 1. Un churn del 8 % mensual no da “unos 2 años” de vida
La vida promedio de un cliente se calcula como **1 / churn mensual**.

- 1 / 0,08 = **12,5 meses** de vida promedio, no 24.
- Un churn del 8 % mensual significa que, al cabo de un año, solo retienes al ~36 % de tus clientes. Eso es una hemorragia.

Si tus clientes se quedaran 2 años, tu churn mensual debería estar cerca del **4 %**.

### 2. El LTV se calcula sobre margen