# GPT-5.6 Luna — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 13.308s | tokens_per_second: 83.4
- input_tokens: 186 | output_tokens: 1110

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

No lo aprobaría **como escala fuerte** con esos números. El error principal es la vida media.

### Recalculando

Con churn mensual de 8%:

\[
\text{Vida esperada} \approx \frac{1}{0.08}=12.5\text{ meses}
\]

No 24 meses.

**LTV de ingresos:**

\[
35 \times 12.5 = \$437.50
\]

Pero para compararlo con CAC deberías usar el margen bruto:

\[
\$437.50 \times 70\% = \$306.25
\]

Por tanto:

\[
\text{LTV/CAC}=\frac{306.25}{290}=1.06
\]

Eso está muy lejos de un objetivo habitual de aproximadamente **3x**.

### Otros problemas

- El CAC consume casi todo el margen bruto esperado: quedan solo **$16.25 por cliente** antes de soporte, salarios, software, refunds y otros gastos.
- El payback no es realmente de \(290 / 24.50 = 11.8\) meses, porque los clientes van churnando. Considerando la retención mensual, recuperar el CAC mediante margen bruto esperado tarda aproximadamente **35 meses**.
- Si el CAC de $290 aumenta al escalar, la economía pasa rápidamente a ser negativa.
- El benchmark de 3x normalmente se calcula usando **LTV basado en margen de contribución**, no ingresos brutos.

### Qué CAC necesitarías

Para alcanzar un LTV/CAC de 3:

\[
\frac{306.25}{3} \approx \$102
\]

Tu CAC debería estar aproximadamente en **$100 o menos**, salvo que puedas mejorar sustancialmente el churn o el margen.

### Sobre los $10.000

A $290 de CAC comprarías unos:

\[
10{,}000 / 290 \approx 34\text{ clientes}
\]

En términos esperados, esos clientes generarían unos $10.560 de margen bruto total durante toda su vida, apenas $560 por encima del gasto publicitario y antes de todos los demás costes. Eso no es un colchón suficiente para justificar una expansión agresiva.

**Recomendación:** no escales todavía. Haría una prueba limitada y con criterios de corte claros, pero buscaría primero:

1. Reducir CAC hacia $100–$150.
2. Bajar el churn mensual del 8%.
3. Medir LTV por cohortes reales, no asumir una vida fija.
4. Incluir costes de soporte, onboarding y operación.
5. Confirmar que el CAC se mantiene al aumentar el presupuesto.

Con los datos actuales, la conclusión correcta es: **el negocio puede ser rentable en general, pero la adquisición pagada a $290 no tiene suficiente margen para escalar con seguridad.**