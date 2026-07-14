# GPT-5.6 Sol — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.98 | quality: 10.0
- latency_total: 30.611s | tokens_per_second: 49.1
- input_tokens: 186 | output_tokens: 1502
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y consejos prácticos para un emprendedor.

## Respuesta completa

No escalaría todavía. La aritmética del plan no sostiene una inversión de $10.000.

### Cálculo corregido

Con churn mensual de 8%, la vida media esperada es:

\[
1 / 0,08 = 12,5\ meses
\]

No 24 meses. De hecho, después de 24 meses solo quedaría aproximadamente:

\[
0,92^{24} = 13,5\%
\]

El LTV relevante debe calcularse sobre **margen bruto**, no sobre ingresos:

\[
LTV = \$35 \times 70\% \div 8\% = \$306,25
\]

Por tanto:

\[
LTV/CAC = 306,25 / 290 = 1,06
\]

Eso está muy lejos de un 3x saludable. Y aun aceptando tus 24 meses, el LTV bruto sería $588 y el ratio solo 2,03x.

### Qué pasaría con los $10.000

A un CAC de $290 comprarías unos 34,5 clientes.

- Margen bruto esperado durante toda su vida: aproximadamente **$10.560**
- Gasto publicitario: **$10.000**
- Margen restante esperado: apenas **$560**

Eso es antes de salarios, soporte, ventas, software, gastos generales, impuestos y costo del capital. Además, al escalar, el CAC suele subir.

El payback simple parece ser 11,8 meses:

\[
290 / (35 \times 70\%) = 11,8
\]

Pero eso ignora que parte de la cohorte abandona cada mes. Incorporando el churn, la cohorte recuperaría el CAC esperado aproximadamente en el **mes 35**, y su beneficio máximo de por vida sería muy pequeño.

### Qué tendría que cambiar

Para llegar a LTV/CAC de 3x con estos números:

- **CAC máximo:** aproximadamente **$102**, o
- **Churn mensual máximo:** aproximadamente **2,8%**, manteniendo CAC y precio, o
- **Precio aproximado:** **$99/mes**, manteniendo CAC, churn y margen.

Mi recomendación: **no metas los $10.000 de golpe**. Haz como mucho una prueba pequeña y controlada, pero solo para validar CAC y churn específicos del canal pagado. Antes de escalar, reduce drásticamente CAC o churn. Ser rentable con clientes orgánicos no implica que la adquisición pagada sea rentable.