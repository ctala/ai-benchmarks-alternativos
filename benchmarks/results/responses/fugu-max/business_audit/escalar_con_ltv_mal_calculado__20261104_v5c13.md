# Fugu Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/fugu-max`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 17.984s | tokens_per_second: 88.9
- input_tokens: 277 | output_tokens: 1599

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

**No escalaría con esos números.** El cálculo de LTV sobrestima cuánto tiempo se queda cada cliente y usa ingresos en vez de margen bruto.

- Con un churn mensual del **8%**, la vida esperada es aproximadamente **1 / 0,08 = 12,5 meses**, no 24.
- Ingreso esperado por cliente: **$35 × 12,5 = $437,50**.
- Margen bruto mensual por cliente: **$35 × 70% = $24,50**.
- **LTV de margen bruto:** $24,50 × 12,5 = **$306,25**.
- **LTV/CAC:** $306,25 / $290 = **1,06:1**, no cerca de 3:1.
- **Recuperación del CAC:** $290 / $24,50 ≈ **11,8 meses**.

Así, cada cliente aporta en promedio solo **$16,25 de margen bruto por encima del CAC** durante su vida, antes de gastos generales, costes de soporte no incluidos, descuentos, incertidumbre y valor del dinero en el tiempo. Con $10.000 de gasto y ese CAC, esperarías adquirir unos **34 clientes**: la diferencia estimada entre su margen bruto de vida y el gasto sería apenas **unos $560**, antes de esos otros costes.

Yo **no comprometería los $10.000 de golpe**. Primero probaría con un presupuesto limitado y mediría CAC y retención por cohortes. Como referencia, para llegar a 3:1 con estos datos tendrías que bajar el CAC a unos **$102**, o reducir el churn mensual a aproximadamente **2,8%**, manteniendo lo demás constante. La regla 3:1 no es universal, pero tus números actuales dejan muy poco margen para escalar con confianza.