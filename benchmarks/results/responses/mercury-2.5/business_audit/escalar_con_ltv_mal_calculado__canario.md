# Mercury 2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.48 | quality: 10.0
- latency_total: 2.806s | tokens_per_second: 713.0
- input_tokens: 226 | output_tokens: 2001

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



No apruebo el plan. La matemática no sostiene el crecimiento agresivo.

Aquí está el desglose real:

1. **Vida del cliente:** Con un 8% de churn mensual, el tiempo promedio de permanencia es 1 ÷ 0.08 = 12.5 meses, no 24.
2. **Margen:** El LTV debe basarse en el margen bruto, no en los ingresos. $35 × 70% = $24.50 de margen mensual.
3. **LTV Correcto:** $24.50 ÷ 0.08 = $306.25.
4. **Ratio LTV/CAC:** $306.25 ÷ $290 ≈ 1.06.

Con un ratio de 1.06, estás recuperando solo un poco más de lo que inviertes en adquirir un cliente. Escalar con publicidad pagada bajo estas condiciones quemará caja rápidamente. Para escalar seguro, necesitas un ratio superior a 3. Enfócate primero en reducir el CAC o mejorar la retención antes de aumentar el presupuesto.