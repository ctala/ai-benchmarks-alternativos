# Seed 2.0 Code — business_strategy/plan_aritmetica_no_cierra

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 33.566s | tokens_per_second: 61.0
- input_tokens: 252 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa


El usuario me pregunta si aprueba un plan de su socio para llegar a $6.000 USD/mes en 6 meses, como analista de crecimiento primero tengo que hacer la multiplicación que él dijo que la mayoría de planes mueren ahí.

Primero, desgloso los números del plan paso a paso, no solo el resultado final, también revisar los supuestos ocultos porque el socio dijo "recurrentes" pero el plan es de un curso de $30, ¿es pago único o recurrente? Ese es un punto clave.

Primero la multiplicación básica del plan como lo plantean:
1. Visitas mensuales: 200.000
2. Conversión a suscriptor: 1,5% → 200.000 * 0,015 = 3.000 suscriptores nuevos POR MES? O es acumulado? El socio dijo "recurrentes", así que hay que diferenciar flujo mensual vs stock.
3. Conversión de suscriptores a compra: 2% → Si son 3.000 suscriptores nuevos por mes, 3.000 * 0,02 = 60 compradores por mes.
4. Ingresos por comprador: $30 → 60 * 30 = $1.800 USD POR MES. ¡Eso es la cuarta parte del objetivo de $6.000!

Ahí ya está el primer error garrafal: la multiplicación básica no llega. Pero luego hay supuestos ocultos que el socio se olvidó, que son clave:

Primero, ¿el curso es pago único o recurrente? El socio dijo "recurrentes" en los ingresos, pero el curso es de $30, usualmente los cursos son pago único. Si fuera recurrente (suscripción mensual de $30), entonces tendríamos que acumular compradores mes a mes durante 6 meses, veamos eso:

Mes 1: 60 compradores → 60*30=1.800
Mes 2: 60 nuevos + 60 anteriores = 120 → 3.600
Mes 3: 180 → 5.400
Mes 4: 240 → 7.200 → Recién en el mes 4 supera los 6.000, PERO...

Hay un montón de supuestos que el socio ignoró, que son los que matan el plan:

1. **Error de cálculo base sin acumulación**: El socio dijo "con eso llegamos cómodos a los 6.000/mes recurrentes" pero su cálculo (si lo hizo) seguramente fue: 200.000 * 1,5% * 2% * 30 = 1.800, no 6.000. ¿Dónde se equivocó? Quizás pensó que el 2% es sobre las visitas, no sobre los suscriptores: 200.000 * 2% *30=120.000 no, o quizás 1,5% de 200k es 3k, 3k * 10% (no 2%) es 300, 300*30=9.000, no. O quizás confundió suscriptores acumulados con mensuales?

2. **Supuestos ocultos no declarados (y probablemente falsos)**:
   a. **Ingresos recurrentes de un curso de $30**: A menos que sea una suscripción MENSUAL de $30 (no pago único), los ingresos no son recurrentes. El socio usa "recurrentes" pero el activo es un curso, usualmente pago único. Si es pago único, los ingresos son 1.800 POR MES, no recurrentes por cliente, solo recurrentes por flujo de nuevos clientes, pero no llega al objetivo.
   b. **Tasa de abandono (churn)**: Si fuera una suscripción, los clientes no se quedan para siempre. Un churn del 5% mensual (conservador para suscripciones de cursos) haría que en el mes 6 tengas: 60 + 57 + 54,15 + ... = no llegues a 240, te quedas en ~200, que son 6.000 justo? No, 200*30=6.000, pero el churn es un factor que no se considera.
   c. **Conversiones no son constantes**: El 1,5% de conversión a suscriptor es "conservador" según ellos, pero ¿es para un formulario frío en el sitio? Si el sitio es de contenido, un formulario de suscripción al boletín puede ser 1-2%, pero un formulario de captura DIRECTO para vender un curso (no un boletín) es menor, usualmente 0,5-1%. Luego, el 2% de conversión de suscriptores a compra: si los suscriptores son de un boletín frío, el 2% es alto para un curso de $30? No, es razonable, pero si el formulario es de captura para el curso, los suscriptores son más calientes, pero la conversión a suscriptor es menor.
   d. **Visitas son constantes?**: El plan asume que las 200.000 visitas al mes se mantienen durante 6 meses, ¿es cierto? ¿Son visitas orgánicas estables, o pagadas que se van a agotar?
   e. **No hay costo?**: El objetivo es $6.000 USD/mes de ingresos o de beneficio? Si hay costos (publicidad para mantener visitas, plataforma de cursos, pasarela de pagos), los ingresos netos son menores. Por ejemplo, pasarela cobra 3,5% + $0,30 por transacción: 60 transacciones de $30 → (60*30)*0,035 + 60*0,30 = 63 + 18 = $81 en comisiones, así que ingresos netos 1.719, sin contar otros costos.

3. **Qué necesitaría para llegar a $6.000/mes?**
   - Si es pago único, ingresos mensuales (flujo): Necesitas 6.000 / 30 = 200 compradores por mes. Para 200 compradores, necesitas 200 / 0,02 = 10.000 suscriptores por mes. Para 10.000 suscriptores, necesitas 10.000 / 0,015 ≈ 666.666 visitas por mes (más del triple de las que tienen).
   - Si es suscripción mensual de $30, y sin churn, necesitas 200 suscriptores activos. Eso se logra en 4 meses (60+60+60+20=200) pero CON churn del 5%: mes 1=60, mes2=60+57=117, mes3=117+57=174, mes4=174+57=231 → recién en mes 4 supera, pero en mes 6 es 60+57+54+51+49+46=317 → 9.510, PERO el socio dijo "recurrentes" sin mencionar suscripción, así que es un engaño.

4. **Otra cosa: "recurrentes" vs "ingresos mensuales de nuevos clientes"**: El socio confunde dos conceptos clave:
   - Ingresos recurrentes (MRR): Ingresos que se repiten mes a mes por clientes existentes (suscripciones).
   - Ingresos mensuales de nuevos clientes (NMRR): Ingresos de nuevos clientes cada mes, que no se repiten (pago único).

El plan del socio dice "recurrentes" pero el activo es un curso de $30, que es pago único, así que los ingresos son NMRR de 1.800, no MRR de 6.000.

Ahora, ¿le damos? No, primero hay que corregir el cálculo, clarificar los supuestos, ajustar el plan. Pero hay que dar pasos concretos:

1. Primero, mostrar el cálculo EXACTO del plan actual para que vean que no llega:
   Cálculo del plan como lo plantean (sin acumulación, pago único):
   200.000 visitas/mes * 1,5% conv. suscriptor = 3.00