# Tencent Hy3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `tencent/hy3`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 60.516s | tokens_per_second: 35.3
- input_tokens: 238 | output_tokens: 2136

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

**Veredicto: Plan rechazado. No lo ejecutamos.**

Como analista de crecimiento, mi trabajo es precisamente ese: matar los planes que no sobreviven a la multiplicación. Y este acaba de morir en el paso 3.

Hagamos la autopsia del funnel (la matemática pura):

1. **Tráfico:** 200.000 visitas/mes
2. **Captura:** 200.000 × 1,5% = **3.000 suscriptores nuevos/mes** (ok, número sano)
3. **Ventas:** 3.000 × 2% = **60 compradores/mes** (ok, tasa sana)
4. **Facturación:** 60 compradores × $30 = **$1.800/mes**

**El objetivo era $6.000/mes.** 
La realidad matemática del plan es **$1.800/mes**. Estás llegando apenas al **30%** de la meta. Te faltan $4.200 mensuales que este embudo, con esos números, simplemente no genera.

### Dos errores graves en el plan de tu socio:

**1. El error de la multiplicación (Volumen vs. Ticket):** 
Los porcentajes de conversión que puso son, efectivamente, conservadores y realistas. El problema es que un embudo con esas tasas necesita mucho más tráfico o un precio mucho más alto para llegar a $6.000. Para que este plan funcione con esos mismos porcentajes, necesitarían **666.000 visitas/mes** o subir el precio del curso a **~$100 USD**.

**2. El error conceptual de "Recurrente":**
Dices que llegarían a "$6.000/mes recurrentes". Un curso de $30 es un pago único (one-time). Eso no es recurrente. Si asumimos que esas 60 ventas se dan *todos los meses* gracias al tráfico constante, estás hablando de $1.800/mes de *nuevas ventas*, no de MRR (Monthly Recurring Revenue) real. Si el curso no se renueva, el mes 7 no tienes nada si no sigues comprando tráfico.

### Conclusión
Los porcentajes te parecen sanos porque lo son, pero **los planes no se aprueban por tener tasas lindas, se aprueban por llegar al número.** Este no llega.

**No le damos.** Antes de ejecutar, tu socio tiene que ajustar la ecuación: o aumentamos el tráfico orgánico/paid, o subimos el precio, o cambiamos el modelo de un curso a una suscripción/membresía para que sí sea recurrente.