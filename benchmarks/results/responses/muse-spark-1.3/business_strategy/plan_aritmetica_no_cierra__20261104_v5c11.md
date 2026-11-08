# Muse Spark 1.3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 14.299s | tokens_per_second: 144.2
- input_tokens: 212 | output_tokens: 2062

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

No. No lo apruebes tal como está. Muere en la multiplicación.

Hagamos la cuenta con **tus propios números**:

**1. Visitas -> Suscriptores**
200.000 visitas/mes x 1,5% = **3.000 suscriptores nuevos/mes**

**2. Suscriptores -> Compradores**
3.000 suscriptores x 2% = **60 compradores/mes**

**3. Compradores -> Ingreso**
60 x $30 = **$1.800/mes**

Objetivo: $6.000/mes
Real con tu math: $1.800/mes

Llegas solo al **30% del objetivo**. Te faltan $4.200 cada mes. Necesitarías 3,33x más.

El problema es clásico: 1,5% y 2% suenan "conservadores" por separado, pero multiplicados son diminutos:

1,5% x 2% = 0,03% de visitante a comprador.
Es decir, **3 compras cada 10.000 visitas.**

Para $6.000 necesitas 200 ventas de $30 al mes. Eso es 10 compras cada 10.000 visitas.

Y hay un segundo error: **no es recurrente.**
Un curso de $30 pago único no es MRR. Son $1.800 nuevos cada mes, no se acumulan. En 6 meses no llegas a $6.000 recurrentes, te quedas en $1.800/mes estancado.

### Qué SÍ necesitarías para llegar a $6.000 con ese tráfico:

Necesitas 200 ventas/mes. Elige una palanca:

1.  **Más captura:** 200.000 x **5%** = 10.000 subs x 2% = 200 x $30 = $6.000
2.  **Más conversión a venta:** 3.000 subs x **6,67%** = 200 x $30 = $6.000
3.  **Más precio/ticket:** 60 compradores x **$100** = $6.000

O una combinación de las tres.

Recomendación: no ejecutar a 6 meses. Primero valida en pequeño si puedes lograr un 5% de captura O un 6,67% de venta O un ticket de $100. Con los números actuales, el plan no cierra.