# GPT-6 Luna Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 31.192s | tokens_per_second: 122.8
- input_tokens: 5240 | output_tokens: 3831

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

**No metería los $10.000 como apuesta de escala todavía.** El cálculo de LTV está inflado y, con los datos actuales, la economía queda muy ajustada.

- Con un churn mensual constante del **8%**, la vida esperada es aproximadamente **1 / 0,08 = 12,5 meses**, no 24. (Solo alrededor del **13,6%** seguiría activo al mes 24.)
- Ingreso esperado por cliente: **$35 / 0,08 = $437,50**.
- Para comparar con el CAC, usa el LTV de **margen bruto**: $437,50 × 70% = **$306,25**.
- **LTV de margen bruto / CAC = $306,25 / $290 ≈ 1,06**, no 2,9. Eso deja apenas **$16,25 por cliente** durante toda su vida esperada, antes de gastos generales, descuentos u otros costos.

Con $10.000 a ese CAC adquirirías unos **34 clientes**. Su margen bruto esperado de por vida sería aproximadamente **$10.560**: apenas **$560 por encima** del gasto publicitario, y ese margen se recuperaría lentamente. El plazo simple de recuperación, $290 / $24,50 al mes, da 11,8 meses, pero supone que nadie cancela; teniendo en cuenta el churn, la contribución esperada acumulada tarda alrededor de **35 meses** en alcanzar el CAC.

Para una relación de **3:1** basada en margen bruto, el CAC tendría que rondar **$102 o menos**, manteniendo lo demás igual.

Antes de escalar, probaría un presupuesto menor y validaría la retención por cohortes y el **CAC marginal**: al subir el gasto, puede empeorar. También confirmaría que el CAC incluya todos los costos de adquisición. Con estos números, escalar fuerte no parece justificado.