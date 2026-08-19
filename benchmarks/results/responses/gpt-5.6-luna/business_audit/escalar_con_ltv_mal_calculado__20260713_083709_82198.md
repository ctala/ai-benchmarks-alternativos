# GPT-5.6 Luna — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.61 | quality: 8.4
- latency_total: 7.049s | tokens_per_second: 153.6
- input_tokens: 186 | output_tokens: 1083

## Respuesta completa

No lo aprobaría todavía. Hay dos errores importantes:

1. **Con un churn mensual de 8%, la vida esperada no es 24 meses.**  
   Bajo churn constante:

\[
\text{Vida esperada}=\frac{1}{0.08}=12.5\text{ meses}
\]

2. **El LTV debe calcularse sobre margen bruto, no sobre ingresos.**

### Recalculando

- Ingreso mensual: **$35**
- Margen bruto: **70%**
- Margen bruto mensual por cliente:  
  \[
  35 \times 70\% = \$24.50
  \]
- LTV sobre margen bruto:  
  \[
  24.50 \times 12.5 = \$306.25
  \]
- CAC: **$290**

Por tanto:

\[
LTV/CAC = \frac{306.25}{290}=1.06
\]

No es 2.9. El 2.9 usa ingresos y además una duración de 24 meses. Incluso usando tus supuestos originales, el LTV de ingresos sería $840, pero no deberías compararlo directamente contra un CAC sin descontar el costo de servir al cliente.

### Resultado económico

El margen bruto esperado después del CAC sería aproximadamente:

\[
306.25 - 290 = \$16.25\text{ por cliente}
\]

Eso es antes de salarios, soporte, software, impuestos, reembolsos, descuentos, costes de onboarding y cualquier otro gasto operativo.

El período de recuperación del CAC sería:

\[
\frac{290}{24.50}=11.8\text{ meses}
\]

Es decir, casi un año. Además, el CAC puede empeorar al escalar el gasto publicitario.

Con $10.000 comprarías aproximadamente:

\[
\frac{10,000}{290}=34.5\text{ clientes}
\]

La contribución bruta esperada de esos clientes sería cercana a $10.560, dejando solo unos **$560 antes de costes operativos y riesgo de estimación**. Eso no es un margen de seguridad suficiente.

### Qué tendría que cambiar

Para alcanzar un LTV/CAC de 3x con estos márgenes, el CAC máximo sería:

\[
\frac{306.25}{3} \approx \$102
\]

Alternativamente, manteniendo un CAC de $290, necesitarías aproximadamente:

- churn mensual cercano o inferior a **2.8%**, o
- mayor precio,
- mayor margen,
- más expansión/upsells,
- o una combinación de lo anterior.

**Recomendación:** no comprometas los $10.000 de una vez. Haz una prueba escalonada con un presupuesto pequeño y criterios explícitos: CAC máximo, churn de los clientes adquiridos, payback y retención a 30/90 días. Con los números actuales, el crecimiento pagado es apenas marginalmente rentable y puede destruir valor si el CAC sube aunque sea un poco.