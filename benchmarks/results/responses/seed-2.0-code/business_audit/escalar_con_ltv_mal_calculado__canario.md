# Seed 2.0 Code — business_audit/escalar_con_ltv_mal_calculado

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 33.454s | tokens_per_second: 61.2
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


El usuario es un fundador que cree que puede escalar con publicidad, pero tiene errores en su cálculo de LTV. Primero, voy a desglosar sus equivocaciones paso a paso, luego recalcular los números reales, y luego decidir si le doy o no, con recomendaciones.

Primero, su error principal: calcula el tiempo de vida como 2 años (24 meses) sin usar el churn correctamente. El churn mensual es 8%, así que el tiempo de vida promedio (Lifetime, LT) no es 100%/8% = 12.5 meses? Wait, no, wait: en SaaS o suscripciones mensuales, el Lifetime promedio es 1 / churn mensual SOLO si es churn exponencial, pero wait, no, el cálculo tradicional es LT = 1 / churn rate mensual (en decimal) porque la probabilidad de que se quede es 1 - churn, así que es una serie geométrica: sumatorio de (1 - churn)^t desde t=0 hasta infinito, que es 1/churn. Oh, él dijo 2 años, que es 24 meses, pero 8% mensual es 1/0.08 = 12.5 meses. Ese es su primer error gordo: confundió el tiempo de vida real.

Segundo, olvidó aplicar el margen bruto al LTV. El LTV no es ingresos totales, sino valor neto para la empresa, es decir, LTV = Margen Bruto por cliente × Lifetime. Él usó ingresos brutos (35/mes) sin el 70% de margen. Ese es el segundo error.

Tercero, su ratio LTV/CAC lo dijo "por encima de 3" pero su cálculo erróneo dio 2.9, lo cual ya está por debajo, pero con los números reales es peor.

Vamos a calcular paso a paso, ordenado:

1. **Error 1: Tiempo de Vida (LT) mal calculado**
   - Él dijo 24 meses. ¿Por qué? Quizás confundió churn anual con mensual? 8% anual sería ~0.67% mensual, pero no, él dijo churn mensual 8%.
   - Cálculo correcto de LT para suscripciones mensuales con churn constante: Es la suma de las probabilidades de permanecer cada mes, que es una serie geométrica convergente:
     LT = 1 / Churn_Mensual (en decimal) = 1 / 0.08 = **12.5 MESES** (no 24). Ojo: esto es el promedio, algunos se quedan más, otros menos, pero el promedio es 12.5.

2. **Error 2: LTV sin margen bruto (error crítico)**
   - Él calculó LTV como Ingresos Totales Promedio (35×24=840), pero el **LTV REAL es el VALOR NETO que aporta el cliente a la empresa**, es decir, después de costos variables (infraestructura, pagos, etc.). Para eso se usa el margen bruto POR CLIENTE.
   - Margen bruto por cliente/mes = Precio × Margen Bruto % = 35 × 0.7 = **$24.5/mes**

3. **Cálculo CORRECTO de LTV**
   - LTV = Margen Bruto por Cliente × Lifetime = 24.5 × 12.5 = **$306.25**
   - Wait, ¿podemos usar el cálculo más preciso con descuento de flujo de caja? Porque el dinero de hoy vale más que el de mañana. El fundador no lo mencionó, pero incluso sin descuento (descuento = 0%), el LTV es 306.25. Si usamos un descuento mensual razonable (por ejemplo, 1% mensual = 12.68% anual, costo de capital), el LTV sería:
     LTV_descontado = (Margen × (1 - churn)) / (churn + descuento) = (24.5 × 0.92) / (0.08 + 0.01) = 22.54 / 0.09 ≈ **$250.44**
   - Eso es aún peor, pero incluso el LTV sin descuento (el más favorable para él) es ~306.

4. **Ratio LTV/CAC REAL**
   - Él calculó 840/290 ≈ 2.89 (dijo 2.9, y que "está por encima de 3" pero ni siquiera su cálculo erróneo lo está).
   - Cálculo correcto (sin descuento): 306.25 / 290 ≈ **1.056**
   - Con descuento: 250.44 / 290 ≈ **0.86**
   - El estándar de la industria es **LTV/CAC ≥ 3 (idealmente 4+)** para que la publicidad pagada sea rentable a largo plazo, y además, el payback period (tiempo en recuperar el CAC) debe ser ≤ 12 meses (idealmente ≤ 6).

5. **Payback Period (Tiempo de Recuperación del CAC)**
   - Esto es crucial porque el fundador quiere meter $10k: ¿cuánto tiempo tarda en recuperar ese dinero?
   - Payback = CAC / Margen Bruto por Cliente/Mes = 290 / 24.5 ≈ **11.8 MESES**
   - Ojo: esto es el promedio, y solo si el cliente no se va antes del payback. Pero el churn es 8% mensual, así que la probabilidad de que un cliente se quede 12 meses es (0.92)^11 ≈ 39% (porque el primer mes es 0.92, segundo 0.92², ..., undécimo mes 0.92¹¹ para llegar a 12 meses). Así que **solo el 39% de los clientes recuperarán el CAC**, el resto se irán antes y perderás dinero con ellos.

6. **Simulación de los $10k Invertidos**
   - Número de clientes adquiridos: 10000 / 290 ≈ 34 clientes.
   - Ingresos brutos totales promedio por cliente: 35 × 12.5 = 437.5.
   - Margen bruto total por cliente: 306.25.
   - Margen bruto total de 34 clientes: 34 × 306.25 = **10.412,5**
   - Así que sin descuento, ganas ~$412 en total? Pero eso es el promedio, y con descuento de flujo de caja, pierdes dinero (34 × 250.44 = 8.514,96 < 10.000). Además, no estás contando costos fijos (tu sueldo, alquiler, etc.)? El fundador dijo "soy rentable", pero eso es con los clientes actuales, pero los nuevos clientes apenas cubren el CAC, no contribuyen a costos fijos.

7. **¿Por qué el fundador cometió esos errores?**
   - Confundió churn mensual con anual: si el churn fuera 8% ANUAL, el LT sería 1/(0.08/12) = 150 meses (12.5 años), pero no, él dijo 8% mensual.
   - Olvidó que el LTV es margen, no ingresos: esto es un error MUY común entre fundadores, porque confunden lo que entra por caja con lo que se queda.
   - Su ratio erróneo ya estaba por debajo del estándar (2.9 < 3), pero con números reales es casi 1, lo que es terrible.

8. **Conclusión y Recomendaciones**
   - NO le doy, por los errores de cálculo y que la publicidad no es rentable.
   - Pasos a hacer antes de escalar:
     1. Reducir el CAC: optimizar campañas, mejorar targeting, creativos, landing pages.
     2. Aumentar el margen bruto: negociar con procesadores de pagos, reducir costos de infraestructura.
     3. Reducir el churn: mejorar onboarding, soporte, producto, planes anuales (que reducen churn mensual).
     4. Aumentar el precio: $35/mes, ¿es el precio óptimo?