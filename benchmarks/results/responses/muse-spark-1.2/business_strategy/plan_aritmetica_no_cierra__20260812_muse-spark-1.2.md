# Muse Spark 1.2 — business_strategy/plan_aritmetica_no_cierra

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 9.582s | tokens_per_second: 170.2
- input_tokens: 197 | output_tokens: 1631

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

No. No lo apruebes así como está. Muere en la multiplicación.

Con sus **propios números** no llegan a $6.000:

**Fórmula: Visitas x % Captura x % Compra x Precio = Ingreso**

1.  200.000 visitas x 1,5% = **3.000 suscriptores/mes**
2.  3.000 suscriptores x 2% = **60 compradores/mes**
3.  60 compradores x $30 = **$1.800 / mes**

No son $6.000. Son $1.800. Les faltan $4.200, o sea necesitan **3,33 veces más** de lo que proyectan.

Que los porcentajes suenen "sanos y conservadores" no importa si la multiplicación no cierra.

Para llegar a $6.000 con ese modelo necesitarían 200 ventas a $30. Con sus tasas actuales necesitarían:

**Para llegar a $6.000 necesitan UNA de estas correcciones:**

*   **Más tráfico:** 666.666 visitas/mes en lugar de 200.000
*   **Más captura:** 5% de conversión a suscriptor en lugar de 1,5%
*   **Más venta:** 6,66% de conversión a compra en lugar de 2%
*   **Más precio:** Cobrar $100 por el curso en lugar de $30

O una combinación. Ejemplo realista para llegar a $6.000 con el mismo tráfico:
> 200.000 visitas x 1,5% = 3.000 suscriptores x 4% compra = 120 ventas x $50 = **$6.000**

Y ojo: eso es ingreso por ventas nuevas de ese mes. No es "recurrente" a menos que el curso sea una suscripción mensual. Si es pago único, al mes siguiente tienes que volver a conseguir 200 ventas nuevas.

**Veredicto: RECHAZADO en su forma actual.**

Antes de ejecutar 6 meses, ajusten una palanca y validen con un test pequeño de 2 semanas si esa tasa de 1,5% y 2% es real para USTEDES.

¿Quieres que te arme 3 escenarios corregidos para sí llegar a los $6.000?