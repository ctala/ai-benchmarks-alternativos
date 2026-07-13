# GPT-5.6 Terra — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 7.14 | quality: 8.4
- latency_total: 15.672s | tokens_per_second: 97.4
- input_tokens: 186 | output_tokens: 1526

## Respuesta completa

No le daría todavía con esos números. Tu cálculo de LTV tiene dos problemas:

1. **Un churn mensual de 8% no equivale a 24 meses de vida media.**  
2. **Estás comparando ingresos de LTV contra CAC de publicidad**, cuando deberías comparar margen bruto/contribución contra CAC.

## Recalculando

### 1. Vida media esperada

Con churn mensual de 8%:

\[
\text{vida media} = \frac{1}{0,08} = 12,5 \text{ meses}
\]

No 24 meses.

Como comprobación: tras 24 meses, la retención esperada sería:

\[
0,92^{24} \approx 13,5\%
\]

Es decir, solo alrededor del 13,5% de esa cohorte seguiría activa a los dos años.

### 2. Margen bruto mensual por cliente

\[
\$35 \times 70\% = \$24,50/mes
\]

### 3. LTV ajustado por margen

\[
LTV = \$24,50 \times 12,5 = \$306,25
\]

(Sin descontar el valor del dinero en el tiempo, ni soporte, ni costes de éxito de cliente, ni devoluciones, ni impuestos, etc.)

### 4. Ratio LTV/CAC

\[
\frac{\$306,25}{\$290} = 1,06x
\]

No es 2,9x. Es aproximadamente **1,06x**.

Por cada $290 que gastas para adquirir un cliente, esperas generar solo unos **$306 de margen bruto acumulado**. Te quedan apenas:

\[
\$306,25 - \$290 = \$16,25
\]

por cliente, **antes de costes fijos, equipo, producto, soporte, ventas, impuestos y coste de capital**.

En la práctica, es muy probable que esa adquisición sea no rentable.

## El problema de caja es aún peor

No recuperas los $290 rápidamente.

El aporte mensual inicial de un cliente es $24,50, pero cada mes sobreviven menos clientes de la cohorte. Con ese churn, necesitas aproximadamente **35 meses** para recuperar el CAC esperado de $290 a nivel cohorte.

A los 12 meses, el margen bruto acumulado esperado de un cliente sería aproximadamente:

\[
\$306,25 \times (1 - 0,92^{12}) \approx \$194
\]

Todavía estarías unos **$96 por debajo del CAC**, sin contar gastos operativos.

## Qué implica gastar $10.000 ahora

Con un CAC de $290:

\[
\frac{\$10.000}{\$290} \approx 34,5
\]

Adquirirías unos **34–35 clientes**.

- CAC total: **$10.000**
- Margen bruto esperado durante toda la vida de esa cohorte:  

\[
34,5 \times \$306,25 \approx \$10.560
\]

- Excedente bruto teórico total: apenas **~$560**

Y ese excedente llega repartido durante años, no este mes. No financia cómodamente ni tu operación actual ni más crecimiento pagado.

## Qué tendría que cambiar para escalar

Para llegar a un ratio LTV/CAC de 3x con tu margen y churn actuales:

\[
CAC_{\max} = \frac{\$306,25}{3} \approx \$102
\]

Necesitarías bajar el CAC de **$290 a aproximadamente $100**.

Alternativamente, puedes mejorar alguna combinación de:

- **Reducir churn:** es probablemente la palanca más potente.
- **Subir precio o ARPU:** planes superiores, uso, asientos, add-ons.
- **Mejorar margen bruto:** aunque 70% ya es razonable.
- **Bajar CAC:** mejor targeting, creativo, funnel, canal, referidos y conversión.
- **Mejorar retención de los clientes adquiridos por ads:** no asumir que tienen el mismo churn que tus clientes orgánicos.

## Veredicto

**No escalaría a $10.000/mes todavía.** Con las métricas dadas, estás comprando crecimiento con una economía unitaria casi plana y una recuperación de caja demasiado lenta.

Primero validaría cohortes pagadas reales y buscaría, como mínimo:

- LTV de margen / CAC de **3x**;
- recuperación de CAC compatible con tu caja —idealmente bastante menor que 12 meses, y desde luego no ~35 meses en expectativa de cohorte—;
- churn medido por canal y por cohorte, no solo un promedio global.

Tu plan no muere por falta de demanda; con estos números, muere por aritmética.