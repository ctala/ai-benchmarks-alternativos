# GPT-5.6 Luna Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 19.832s | tokens_per_second: 219.5
- input_tokens: 6285 | output_tokens: 4353

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

No escalaría fuerte todavía. La aritmética correcta da una economía muy ajustada:

### 1. La vida media no es de 24 meses

Con churn mensual de 8%:

\[
\text{Vida media} = \frac{1}{0{,}08}=12{,}5\text{ meses}
\]

Por tanto, el LTV de ingresos es:

\[
35 \times 12{,}5 = \$437{,}50
\]

No \$840.

### 2. Hay que usar margen bruto, no ingresos

Tu contribución mensual por cliente es:

\[
35 \times 70\% = \$24{,}50
\]

LTV basado en margen bruto:

\[
24{,}50 \times 12{,}5 = \$306{,}25
\]

Comparación:

\[
\text{LTV/CAC}=\frac{306{,}25}{290}=1{,}06
\]

Incluso usando ingresos sin margen:

\[
\frac{437{,}50}{290}=1{,}51
\]

No es 2,9; y en ambos casos está por debajo de un nivel saludable de aproximadamente 3x.

### 3. El payback es muy largo

Sin considerar churn, recuperarías el CAC en:

\[
290/24{,}50=11{,}8\text{ meses}
\]

Pero con churn, el payback agregado de la cohorte es aproximadamente **35 meses**. La contribución acumulada de una cohorte después de \(n\) meses es:

\[
24{,}50 \times \frac{1-0{,}92^n}{0{,}08}
\]

Como el LTV total esperado es solo \$306,25, acabas recuperando el CAC por muy poco, y muy tarde. Eso es antes de soporte, salarios, descuentos, impuestos, refunds, overhead y errores de medición del CAC.

### 4. Qué significa gastar \$10.000

A un CAC de \$290 adquirirías aproximadamente:

\[
10.000/290 \approx 34{,}5\text{ clientes}
\]

Su contribución bruta esperada total sería:

\[
34{,}5 \times 306{,}25 \approx \$10.560
\]

El excedente esperado sería apenas de unos **\$560**, antes de todos los demás costes y de la variabilidad real. No es un margen suficiente para “escalar fuerte”.

### Recomendación

No aprobaría los \$10.000 como inversión de crecimiento plena. Haría, como mucho, una prueba limitada y con criterios de corte claros:

- CAC máximo basado en margen bruto: idealmente cercano a **\$100** si buscas un LTV/CAC de 3x.
- Payback objetivo: preferiblemente menor a 12 meses.
- Medir churn por cohorte y por canal, no solo el churn global.
- Confirmar que los \$290 incluyen todos los costes de adquisición.
- No escalar hasta demostrar que el CAC baja sustancialmente o que el churn mejora.

Con la economía actual, el problema no es que falte volumen publicitario: es que cada cliente adquirido apenas deja contribución después de recuperar el CAC.