# DeepSeek V4 Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 15.037s | tokens_per_second: 73.4
- input_tokens: 202 | output_tokens: 1103

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

Tu plan tiene un error grave en el cálculo del LTV. Con un churn mensual del 8%, la vida media de un cliente no es 2 años (24 meses), sino 1 / 0.08 = **12.5 meses**. Además, el LTV se calcula con el margen bruto, no con el ingreso total.

**LTV correcto:**  
$35 × 70% margen = $24.5 de ganancia bruta mensual por cliente.  
LTV = $24.5 / 0.08 = **$306.25**, no $840.

**Relación LTV/CAC real:**  
$306.25 / $290 = **1.06x**.

Eso está muy lejos del umbral saludable (3x o más). Con esos números, por cada dólar que inviertas en publicidad perderás dinero después de considerar el costo de adquisición y la retención real. No importa que hoy seas rentable con clientes orgánicos: escalar con paid ads así solo acelera las pérdidas.

Para escalar con publicidad necesitás:
- Reducir el churn mensual (bajarlo al menos al 5% daría 20 meses de vida media, LTV $490, LTV/CAC 1.69x, todavía insuficiente).
- Aumentar el margen o el precio (si subieras a $45 con el mismo margen, LTV $393, ratio 1.36x).
- Bajar el CAC (por debajo de $100 para aspirar a un ratio sano).

Con un churn del 8% y ese CAC, el LTV/CAC no llega ni a 1.1x. **No le des.** Primero arreglá la retención o el modelo de ingresos, después escalá.