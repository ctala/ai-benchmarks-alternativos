# DeepSeek V4 Flash (OpenRouter) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.57 | quality: 7.6
- latency_total: 7.448s | tokens_per_second: 78.0
- input_tokens: 202 | output_tokens: 581

## Respuesta completa

No, no le des. Tu cálculo de LTV está mal por un error crítico en la vida media del cliente.

Con un churn mensual del 8%, la vida media de un cliente es:
\[
\frac{1}{0.08} = 12.5 \text{ meses}
\]
No 24 meses. El LTV correcto, considerando el margen bruto del 70%, es:
\[
LTV = 35 \times 12.5 \times 0.70 = \$306.25
\]
Esto da un ratio LTV/CAC de:
\[
\frac{306.25}{290} \approx 1.056
\]
Estás al borde de la rentabilidad, no por encima de 3. Invertir \$10,000 en publicidad a ese CAC apenas te generará un retorno marginal, y cualquier variación en el churn o el CAC (por ejemplo, si la calidad de los leads baja) te dejará en pérdidas.

Además, un LTV/CAC de 1.056 no cubre costos fijos ni de operación; para escalar con publicidad pagada se recomienda al menos 3:1. Primero, reduce el churn o busca un canal de adquisición más barato antes de escalar.