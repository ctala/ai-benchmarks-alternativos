# Mercury 3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `inception/mercury-3`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 5.396s | tokens_per_second: 501.5
- input_tokens: 226 | output_tokens: 2706

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

No lo aprobaría todavía. Este plan tiene un error clásico de multiplicación: con tus propios números no llegas a $6.000, sino a **$1.800/mes**.

## La matemática del plan

- 200.000 visitas × 1,5% = **3.000 suscriptores/mes**
- 3.000 suscriptores × 2% = **60 ventas/mes**
- 60 ventas × $30 = **$1.800/mes**

Eso es el **30% de la meta**. Faltan $4.200 mensuales.

## El problema de “recurrentes”

Un curso de $30 no es un ingreso recurrente. Es una venta única.

Si asumes que la lista se acumula y que cada mes un 2% de **toda la lista** compra, entonces sí llegarías a $6.000 alrededor del mes 4:

- Mes 1: 3.000 suscriptores → $1.800
- Mes 2: 6.000 suscriptores → $3.600
- Mes 3: 9.000 suscriptores → $5.400
- Mes 4: 12.000 suscriptores → $7.200

Pero eso implica que las mismas personas pueden comprar el mismo curso varias veces, o que tienes otros productos, upsells o una membresía. Si es una compra única, ese cálculo no funciona.

## Qué se necesita realmente para llegar a $6.000

Con $30 y 2% de conversión, necesitas **200 ventas/mes**.

- Si es sobre lista acumulada: necesitas **10.000 suscriptores activos**.
- Si es sobre suscriptores nuevos: necesitas **10.000 suscriptores nuevos cada mes**, lo que con 1,5% de captura exigiría **666.667 visitas/mes**.

Alternativas para que el plan cierre:

- Subir el precio a **$100** manteniendo 60 ventas/mes → $6.000.
- Mejorar la captura a **5%** → 10.000 suscriptores/mes → 200 ventas → $6.000.
- Mejorar la compra a **~6,7%** sobre 3.000 suscriptores → 200 ventas → $6.000.

## Antes de aprobar, necesito saber

1. ¿El curso es una venta única o es recurrente/membresía?
2. ¿Las 200.000 visitas son reales, únicas y relevantes para el curso?
3. ¿Cuál es la conversión actual del sitio? ¿Hay datos previos?
4. ¿Qué tasa de apertura y de email marketing esperas? Un 2% de compra sobre suscriptores fríos es optimista si no hay un embudo de nurturing.
5. ¿$6.000 es ingreso o ganancia? Hay que descontar costos.

**Conclusión:** no le damos todavía. El plan necesita ajustar el modelo de ingresos o las palancas de conversión. Con los números actuales, el resultado real es $1.800/mes, no $6.000.