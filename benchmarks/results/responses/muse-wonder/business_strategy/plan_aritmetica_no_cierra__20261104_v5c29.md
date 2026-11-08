# Muse Wonder — business_strategy/plan_aritmetica_no_cierra

- model_id: `meta/muse-wonder`
- success: True  | final: 8.16 | quality: 10.0
- latency_total: 19.492s | tokens_per_second: 96.1
- input_tokens: 212 | output_tokens: 1873

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

No. Los porcentajes son sanos, el problema es la multiplicación.

El plan, con sus propios números, no llega a $6.000. Llega a menos de un tercio.

### Hagamos la cuenta

**1. Visitas a suscriptores**
200.000 visitas x 1,5% = **3.000 suscriptores/mes**

**2. Suscriptores a compradores**
3.000 suscriptores x 2% = **60 compradores/mes**

**3. Compradores a ingresos**
60 compradores x $30 = **$1.800/mes**

No $6.000/mes. Son $1.800/mes.

Les faltan $4.200, o sea necesitan **3,33 veces más** de lo que el plan produce.

### Y hay un segundo error: no es recurrente

Un curso de $30 se compra una vez. Esos 60 compradores del mes 1 no vuelven a comprar el mismo curso en el mes 2.

Por lo tanto no se acumula. Si mantienen las 200.000 visitas, harán ~$1.800 en el mes 1, ~$1.800 en el mes 2, ~$1.800 en el mes 6. Nunca escala a $6.000 solo por pasar el tiempo, a menos que crezca el tráfico o vendan productos nuevos a la lista.

### Qué tendrían que cambiar para llegar a $6.000

Para $6.000 necesitan 200 ventas/mes a $30, no 60.

Manteniendo todo lo demás igual, necesitarían UNA de estas cosas:

* **Tráfico:** 666.667 visitas/mes en vez de 200.000
* **Captura:** 5% en vez de 1,5%
* **Conversión a venta:** 6,7% en vez de 2%
* **Precio:** $100 en vez de $30

Ninguna de esas solas parece "conservadora".

Una combinación realista sí podría cerrar, por ejemplo:

200.000 x **3% de captura** = 6.000 suscriptores
6.000 x **2,5% de compra** = 150 compradores
150 x **$40 de ticket** = **$6.000**

Pero eso ya es otro plan: hay que duplicar la captura, mejorar la venta y subir el ticket/precio con un upsell.

### Veredicto

No lo aprueben para ejecutar 6 meses esperando $6.000.

Aprueben, como mucho, un test de 30 días para validar si ese 1,5% y ese 2% son reales. Si lo son, el negocio base da $1.800/mes, y a partir de ahí deciden qué palanca van a mover para multiplicarlo por 3,33.