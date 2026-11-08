# GPT-6.1 Terra — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 12.555s | tokens_per_second: 70.0
- input_tokens: 186 | output_tokens: 879

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

**No escalaría todavía.** Con tus datos, la publicidad apenas recuperaría su costo antes de gastos adicionales.

El cálculo corregido, suponiendo un churn constante del 8% mensual, sin expansión de ingresos y con el margen bruto estable, es:

- **Vida media estimada:** 1 / 0,08 = **12,5 meses**, no 24.
- **Margen bruto mensual por cliente:** $35 × 70% = **$24,50**.
- **LTV bruto estimado:** $24,50 × 12,5 = **$306,25**.
- **LTV/CAC:** $306,25 / $290 = **1,06**, no 2,9.

Quedan solo **$16,25 por cliente** para cubrir soporte, gastos comerciales y administrativos, impuestos y beneficio. Además, incluso con tu supuesto de 24 meses, el LTV ajustado por margen sería $588 y el LTV/CAC sería **2,03**.

Si inviertes $10.000 al mismo CAC, adquirirías unos **34 clientes**. Su margen bruto esperado durante toda su vida sería aproximadamente **$10.560**: apenas $560 por encima de la inversión, antes de los demás gastos. Y, bajo el mismo modelo de churn, recuperar el CAC acumulado de la cohorte tardaría alrededor de **36 meses**.

Antes de aumentar el gasto, validaría el churn y el CAC por cohorte e incluiría todos los costos de adquisición. Como referencia, con ese LTV necesitarías un CAC cercano a **$102** para llegar a una relación de 3; alternativamente, tendrías que mejorar sustancialmente la retención o el margen.