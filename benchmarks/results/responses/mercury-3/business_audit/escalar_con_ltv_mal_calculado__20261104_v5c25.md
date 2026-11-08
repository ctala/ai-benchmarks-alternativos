# Mercury 3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `inception/mercury-3`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 6.176s | tokens_per_second: 528.3
- input_tokens: 213 | output_tokens: 3263

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

No, no te lo apruebo.

Tu cálculo tiene dos errores importantes:

1. **Vida media del cliente**: con churn mensual de 8%, la vida media es:

   \[
   1 / 0.08 = 12.5 \text{ meses}
   \]

   No 24 meses. Para que fueran 24 meses, necesitarías un churn de ~4.2% mensual.

2. **LTV debe usar margen bruto**, no el precio bruto:

   \[
   35 \times 0.70 = \$24.5 \text{ por mes}
   \]

Entonces el LTV real es:

\[
LTV = \frac{24.5}{0.08} = \$306.25
\]

Contra tu CAC de $290:

\[
\frac{LTV}{CAC} = \frac{306.25}{290} = 1.06
\]

Eso está muy por debajo de 3.

Además, tu payback es:

\[
\frac{290}{24.5} = 11.8 \text{ meses}
\]

Pero la vida media del cliente es de 12.5 meses. Es decir, apenas recuperas la inversión antes de que el cliente se vaya. Te quedan ~0.7 meses de margen por cliente, unos $17. Cualquier desviación en churn o CAC te deja en negativo.

Con $10,000 en publicidad, conseguirías ~34 clientes:

\[
10,000 / 290 \approx 34
\]

Su margen bruto total de vida sería:

\[
34 \times 306.25 \approx \$10,560
\]

O sea, solo $560 por encima de la inversión, sin contar costos fijos ni gastos operativos.

Para que esto funcionara, necesitarías:

- **CAC ≤ $102** para un LTV/CAC de 3.
- **CAC ≤ $147** para un payback de 6 meses, que es más prudente con churn de 8%.

Estás en $290. Mi recomendación: **no metas $10,000 en publicidad todavía**. Primero baja el CAC, mejora la retención o sube el margen. Con estos números, escalar con publicidad pagada es casi break-even y muy riesgoso.