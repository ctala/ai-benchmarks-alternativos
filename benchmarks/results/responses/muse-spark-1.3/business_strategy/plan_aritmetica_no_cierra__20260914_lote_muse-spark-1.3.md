# Muse Spark 1.3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 16.292s | tokens_per_second: 133.5
- input_tokens: 211 | output_tokens: 2175

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

No. No lo apruebes así como está. Mueren en la multiplicación.

Hagamos la cuenta con *sus* propios números:

**1. Visitas -> Suscriptores**
200.000 visitas x 1,5% = **3.000 suscriptores / mes**

**2. Suscriptores -> Compradores**
3.000 suscriptores x 2% = **60 compradores / mes**

**3. Compradores -> Ingreso**
60 x $30 = **$1.800 / mes**

Objetivo: $6.000 / mes
Realidad del plan: $1.800 / mes

Llegan al **30% de la meta**. Les faltan $4.200 cada mes. No llegan "cómodos", no llegan.

Y hay un segundo error: eso ni siquiera es **recurrente**. Un curso de $30 es un pago único. Esos $1.800 no se repiten solos el mes siguiente, tienes que conseguir 60 compradores nuevos otra vez.

Para llegar a $6.000/mes con esas bases necesitarías:

200 compradores / mes = $6.000 / $30

Eso implica conseguir 10.000 suscriptores / mes = 200 / 2%

Con 200.000 visitas, eso es:
10.000 / 200.000 = **5% de conversión a suscriptor**, no 1,5%.

Tienes 3 caminos para que cierre, necesitas 3,33x más:

1.  **Más tráfico:** 666.667 visitas/mes con el mismo 1,5% y 2%
2.  **Mejor captura:** 5% de opt-in con el mismo tráfico y 2%
3.  **Mejor monetización:** mismo tráfico y captura, pero precio de $100 (6.000 / 60) o conversión de compra de 6,67% (200 / 3.000)

Mi recomendación como analista: no ejecutar. Devolver el plan y pedir que venga con una combinación que sí multiplique a $6.000, y que aclare si será ingreso único o MRR real.

¿Quieres que te lo re-arme con un escenario viable?