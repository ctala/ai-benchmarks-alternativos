# Muse Ember — business_strategy/plan_aritmetica_no_cierra

- model_id: `meta/muse-ember`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 5.464s | tokens_per_second: 408.3
- input_tokens: 212 | output_tokens: 2231

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

No. No lo apruebes con ese objetivo.

Los porcentajes por separado parecen conservadores, pero juntos no llegan ni de cerca. Hagamos la multiplicación del propio plan:

**200.000 visitas/mes**
x 1,5% de captura = **3.000 suscriptores**
x 2% de compra = **60 ventas**
x $30 = **$1.800 / mes**

No $6.000. Llegas al 30% del objetivo. Te faltan $4.200, un factor de 3,3x.

Y los 6 meses no lo arreglan: ese es el resultado *mensual* en régimen. Si acumulas la lista, el promedio sigue siendo el mismo.

### Qué tendrías que cambiar para llegar a $6.000

Necesitas 200 ventas/mes a $30, no 60. Manteniendo todo lo demás igual, tendrías que multiplicar por 3,3 una sola variable:

* **Tráfico:** 666.667 visitas/mes (no 200.000)
* **Captura:** 5% (no 1,5%)
* **Compra:** 6,7% (no 2%)
* **Precio:** $100 (no $30)

Ninguna de esas es "conservadora" por sí sola.

La salida realista no es tocar una variable, es rediseñar el funnel con una combinación, por ejemplo: captura al 3% con un lead magnet de verdad + compra al 3,3% con una mejor oferta/precio. Eso sí da 200 ventas.

Además hay un segundo problema: un curso de $30 pago único no es ingreso *recurrente*. Cada mes necesitas conseguir 60 compradores nuevos sí o sí.

**Veredicto:** Si ejecutas este plan tal cual, planifica $1.800/mes, no $6.000.