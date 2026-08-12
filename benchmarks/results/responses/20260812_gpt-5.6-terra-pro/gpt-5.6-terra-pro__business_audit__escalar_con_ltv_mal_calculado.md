# GPT-5.6 Terra Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 36.696s | tokens_per_second: 127.9
- input_tokens: 6592 | output_tokens: 4694

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

No le daría $10.000 todavía. Tu cálculo tiene dos problemas: la duración esperada y el margen.

### 1. Con churn de 8%, la vida esperada no es 24 meses

Aproximación estándar:

\[
\text{Vida media} = \frac{1}{0{,}08} = 12{,}5 \text{ meses}
\]

Además, tras 24 meses solo seguiría activo aproximadamente:

\[
0{,}92^{24} = 13{,}5\%
\]

de la cohorte original.

### 2. El LTV debe calcularse sobre margen bruto, no ingresos

Tu contribución bruta mensual por cliente es:

\[
\$35 \times 70\% = \$24{,}50
\]

Por tanto:

\[
\text{LTV bruto} = \frac{\$24{,}50}{8\%} = \$306{,}25
\]

Comparado con tu CAC:

\[
\frac{\$306{,}25}{\$290} = 1{,}06x
\]

No tienes un ratio de 2,9x ni de 3x: tienes aproximadamente **1,06x LTV/CAC**.

Eso significa que, antes de soporte, equipo, impuestos, reembolsos, herramientas, coste de capital y cualquier gasto no incluido en el margen bruto, cada cliente adquirido deja:

\[
\$306{,}25 - \$290 = \$16{,}25
\]

Es demasiado fino para escalar. Un pequeño empeoramiento del churn o del CAC te pone en pérdidas.

### 3. El payback también es peligroso

El cliente genera $24,50/mes de margen mientras permanezca activo. Pero dado el churn, recuperar el CAC a nivel de cohorte tarda mucho más de lo que parece.

El máximo margen esperado de ese cliente es $306,25, y estás gastando $290 para adquirirlo. Para recuperar $290 necesitas capturar cerca del 95% de su LTV esperado. Con 8% de churn, eso ocurre aproximadamente hacia el mes 35 de la cohorte.

Es decir: estás poniendo efectivo hoy para recuperar casi todo el gasto muy tarde, y con solo $16 de margen esperado total por cliente.

### 4. Qué implicaría meter $10.000

A CAC de $290:

\[
\$10.000 / \$290 \approx 34{,}5 \text{ clientes}
\]

El LTV bruto total esperado de esos clientes sería:

\[
34{,}5 \times \$306{,}25 \approx \$10.560
\]

Contra $10.000 de publicidad, tu contribución bruta esperada de toda esa inversión es aproximadamente:

\[
\$10.560 - \$10.000 = \$560
\]

Y eso es **antes** de costes que probablemente no estén en el margen bruto.

## Qué tendría que cambiar para escalar

Para un ratio LTV/CAC de 3x con tu LTV actual:

\[
\text{CAC máximo} = \$306{,}25 / 3 \approx \$102
\]

Alternativamente, para sostener un CAC de $290 y llegar a 3x, necesitarías un LTV de:

\[
\$290 \times 3 = \$870
\]

Con precio de $35 y margen de 70%, eso requeriría aproximadamente un churn mensual de:

\[
\$24{,}50 / \$870 \approx 2{,}8\%
\]

O tendrías que aumentar sustancialmente ARPU/margen mediante anualidades, upsells, expansión, pricing o menor coste de servicio.

## Decisión

**No escales a $10.000 con estos números.** Haz experimentos controlados para bajar CAC de forma material y valida el churn por cohortes de clientes pagados, no por una media agregada. Como referencia, buscaría un CAC totalmente cargado de alrededor de **$100–120 o menos** antes de acelerar inversión, salvo que tengas una razón muy sólida para aceptar un retorno mucho menor y un payback largo.