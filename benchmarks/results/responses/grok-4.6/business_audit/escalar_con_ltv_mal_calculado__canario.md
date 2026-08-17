# Grok 4.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 54.008s | tokens_per_second: 47.5
- input_tokens: 394 | output_tokens: 2563

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

**No. Con estos números el plan muere en la aritmética.**

El lifetime no es ~24 meses. Con churn mensual constante del 8 % la vida media esperada es \(1 / 0{,}08 = 12{,}5\) meses. (El 63 % de los clientes se habrán ido antes de cumplir el año: \(0{,}92^{12} \approx 0{,}37\).)

El LTV tampoco es \(35 \times 24\). Hay que usar el margen de contribución, no el revenue:
- Contribución mensual = \(35 \times 0{,}70 = 24{,}50\)
- LTV = \(24{,}50 \times 12{,}5 = 306{,}25\)

LTV/CAC real = \(306 / 290 \approx 1{,}05\). Ni siquiera 2, y mucho menos 3. El payback es \(290 / 24{,}50 \approx 11{,}8\) meses: casi un año para recuperar el CAC, justo cuando la mayoría ya se ha ido.

Incluso si usáramos tu lifetime equivocado de 24 meses, el LTV con margen sería \(24{,}50 \times 24 = 588\), ratio \(2{,}0\). Sigue por debajo del umbral habitual y el payback seguiría siendo largo.

Meter \(10{,}000\) este mes compra ~34 clientes. Esa cohorte genera ~\(833\) de contribución al mes y empieza a evaporarse de inmediato. Vas a convertir un negocio ya rentable en uno que quema caja durante muchos meses con un retorno esperado apenas positivo (sin descontar el valor del dinero en el tiempo, sin costes de soporte extra, sin el riesgo de que el CAC suba o el churn de los clientes de paid sea peor).

Para que el paid scaling tenga sentido con estos inputs necesitarías, como mínimo, un CAC sustancialmente más bajo (~100 o menos para un ratio ~3) o un churn claramente inferior (hacia el 3-4 % mensual). Con los números actuales no apruebo el gasto. Recalcula o reduce el test a una cantidad pequeña y mide cohortes reales antes de escalar.