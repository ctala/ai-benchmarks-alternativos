# Seed 2.0 Code — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 38.803s | tokens_per_second: 52.8
- input_tokens: 249 | output_tokens: 2048

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


El usuario ya es rentable, quiere meter 10k en publicidad, pero su cálculo de LTV está MUY mal. Primero, voy a desglosar paso por paso, como analista de unit economics que no se deja engañar por la aritmética básica.

Primero, su error GRAVE: el cálculo de vida útil (Lifetime) con churn mensual del 8%. Él dijo "unos 2 años" = 24 meses, pero ¿cómo se calcula el Lifetime CORRECTO? No es un número arbitrario. El Lifetime (LT) para churn mensual es 1 / churn mensual, PERO OJO: eso es para churn exponencial, pero hay que ajustar por margen bruto, y también él olvidó descontar el valor temporal del dinero? Wait, no, primero el error más obvio:

1. Cálculo de LT ERRÓNEO: Él supuso 24 meses, pero con 8% de churn mensual, ¿cuál es el promedio real? El LT promedio (en términos de valor presente, pero incluso sin descuento) es 1 / churn mensual SOLO si el churn es constante y es el churn de clientes (no de ingresos, aquí es igual porque precio es fijo). Wait 1/0.08 = 12.5 MESES, NO 24. ¡Eso es el error PRINCIPAL! ¿Por qué? Porque el churn es el porcentaje que se va CADA MES, así que la vida media es 1 sobre churn mensual. Vamos a comprobar: si tienes 100 clientes, mes 1 se van 8, quedan 92; mes 2 se van 8% de 92 = 7.36, quedan 84.64; etc. El número promedio de meses que se quedan es ~12.5, no 24. ¿De dónde sacó él 2 años? Probablemente confundió churn anual con mensual: si churn fuera 8% ANUAL, LT sería 12.5 años, pero no, él dijo 8% MENSUAL.

2. Segundo error: LTV no es Precio × LT, es (Precio × Margen Bruto) × LT. Porque el margen bruto es lo que te queda DESPUÉS de costos variables (infraestructura, pagos). Él usó el precio bruto, no el margen.

3. Tercer error: Incluso si LT fuera 24, él usó precio sin margen: 35×24=840, pero LTV REAL (sin descuento) es (35×0.7)×LT = 24.5 × LT.

4. Cuarto punto: LTV/CAC óptimo no es "más o menos 3", es que LTV (con margen, con descuento) sea ≥3×CAC, y que el payback period (tiempo en recuperar el CAC) sea lo más corto posible, idealmente <12 meses para no quemar caja.

Ahora vamos a calcular LOS NÚMEROS REALES, paso a paso, sin trucos:

Paso 1: Calcular Lifetime (LT) CORRECTO para churn mensual constante (8% = 0.08):
LT = 1 / churn_mensual = 1 / 0.08 = 12.5 MESES.
(Nota: Esto es el "expected lifetime" en términos de la media geométrica, que es el valor correcto para LTV. Si queremos ser más precisos, podemos calcular el valor presente neto (LTV_NPV) porque el dinero de hoy vale más que el de mañana. Vamos a usar un descuento mensual razonable para startups: 1% mensual (12.68% anual, tasa de costo de capital o de oportunidad).)

Paso 2: Calcular Margen Bruto por Mes (MB_mes):
Precio × Margen Bruto = 35 × 0.7 = $24.5/mes POR CLIENTE.

Paso 3: Calcular LTV SIN DESCUENTO (LTV_bruto):
MB_mes × LT = 24.5 × 12.5 = $306.25.

Paso 4: Calcular LTV CON DESCUENTO (LTV_NPV, más realista):
La fórmula de LTV_NPV para pagos mensuales constantes, churn mensual r, descuento mensual d:
LTV_NPV = MB_mes × [ (1 + r) / (d + r - d×r) ]
(Usamos la fórmula de perpetuidad con decaimiento por churn y descuento.)
Si d = 0.01 (1% mensual), r = 0.08:
LTV_NPV = 24.5 × [1.08 / (0.01 + 0.08 - 0.01×0.08)] = 24.5 × [1.08 / 0.0892] ≈ 24.5 × 12.107 ≈ $296.62.

Paso 5: Comparar con CAC ($290):
- LTV_bruto (sin descuento) = $306.25 → LTV/CAC = 306.25 / 290 ≈ 1.056.
- LTV_NPV (realista) = $296.62 → LTV/CAC ≈ 1.023.
- Payback Period (tiempo en recuperar CAC con MB_mes): ¿Cuántos meses tardas en cobrar $290 con $24.5/mes? 290 / 24.5 ≈ 11.84 MESES. PERO OJO: eso es si el cliente NO se va antes de ese plazo. Pero con churn del 8% mensual, ¿cuál es la probabilidad de que el cliente se quede 12 meses? (1 - 0.08)^12 ≈ 0.3677 → SOLO EL 36.8% DE LOS CLIENTES LLEGARÁN A PAGAR LO SUFICIENTE PARA RECUPERAR EL CAC. El 63.2% se irá ANTES de que recuperes tu inversión en publicidad.

Ahora, ¿qué pasó con el cálculo del fundador? Errores FATALES:
1. LT arbitrario (24 meses) en lugar del cálculo real por churn (12.5 meses).
2. Usó Precio en lugar de Margen Bruto (olvidó que no se queda con los $35, solo con $24.5).
3. No consideró descuento del valor temporal del dinero (opcional pero relevante, pero incluso sin él, el LTV es casi igual al CAC).
4. Confundió el ratio LTV/CAC: él pensó que estaba en 2.9, pero está en ~1.02, que es CASO CERO (apenas recuperas el CAC, sin ganancias por el cliente, y sin considerar costos fijos, impuestos, etc.).

Además, el plan de meter $10k: ¿cuántos clientes adquiriría? 10.000 / 290 ≈ 34.48 clientes → ~34 clientes. El valor total que generarían (LTV_NPV total) es 34 × 296.62 ≈ $10.085. Así que apenas recuperas los $10k, SIN GANANCIAS, y con el riesgo de que el churn sea mayor, o que el CAC aumente al escalar (porque cuando metes más presupuesto, la calidad de la audiencia baja, el CAC sube).

Otro punto: el churn del 8% mensual es MUY ALTO. Es un churn anual de (1 - 0.92^12) ≈ 63.2% → casi 2/3 de tus clientes se van al año. Eso es insostenible para escalar con publicidad pagada, porque necesitas que los clientes se queden más tiempo para generar margen.

Ahora, ¿qué recomendar? Primero, ARREGLAR LOS NÚMEROS, luego:
1. Reducir el churn (8% mensual es demasiado alto: ¿por qué se van? Mejorar producto, onboarding, soporte).
2. Reducir el CAC (optimizar publicidad: audiencias mejor segmentadas, creatividades mejoradas, landing pages optimizadas, tal vez pro canales más baratos).
3. Aumentar el margen bruto o el precio (¿puedes subir el precio? ¿reducir costos de infraestructura/pagos?).
4. Antes de meter $10k,