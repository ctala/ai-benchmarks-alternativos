# Claude Opus 5 Fast — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 18.105s | tokens_per_second: 169.2
- input_tokens: 318 | output_tokens: 3064

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

## Veredicto corto: no. El plan, con sus propios números, llega a $1.800/mes. Es el 30% del objetivo.

Antes de discutir si los porcentajes son "sanos", hay que multiplicarlos. Ese paso no está hecho.

## La cadena, ejecutada

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | — | 200.000 |
| × 1,5% captura | 200.000 × 0,015 | 3.000 suscriptores |
| × 2% compra | 3.000 × 0,02 | **60 compradores** |
| × $30 | 60 × 30 | **$1.800/mes** |

**Faltan $4.200/mes.** Para llegar a $6.000 necesitás 200 ventas mensuales, no 60. Es un factor de **3,33×**, no un ajuste fino.

El problema estructural: dos porcentajes de un dígito multiplicados entre sí dan tres décimas de por ciento. 1,5% × 2% = 0,03% de las visitas termina comprando. 200.000 × 0,0003 = 60. Cada porcentaje suena razonable por separado; el producto es brutal.

## Tres problemas además del aritmético

**1. Eso no es recurrente.** Un curso de $30 es venta única. Los $1.800 se repiten sólo si cada mes entran 3.000 suscriptores *nuevos* y compran a la misma tasa. La lista acumulada no ayuda: al mes 4 tenés 12.000 suscriptores, pero 9.000 ya vieron la oferta y no compraron. El 2% aplica a la cohorte nueva, no al stock. Ingreso plano, no creciente, y atado a sostener las 200.000 visitas.

**2. Bruto ≠ neto.** Restá pasarela de pago (~3%), reembolsos (5-10% es normal en infoproductos baratos), e impuestos. Los $1.800 quedan en ~$1.550 reales.

**3. "Conservador" es una etiqueta, no un dato.** 1,5% de visita-a-suscriptor es razonable con un formulario bien ubicado y una oferta concreta; con un formulario genérico al pie es más común 0,3-0,8%. Y 2% de lista-a-compra es plausible en una lista cultivada, no en suscriptores fríos de la semana pasada. Pregunta previa a todo: ¿las 200.000 son *sesiones* o *usuarios únicos*? Si son sesiones, la base real puede ser 120.000. Y ¿ese tráfico tiene que ver con el tema del curso, o llega por notas que no se relacionan?

## Qué haría falta de verdad

Cualquiera de estas, sola:

- Precio de $30 → **$100** (misma conversión, cosa que no pasa: subir precio baja la tasa de compra)
- Captura de 1,5% → **5%**
- Compra de 2% → **6,7%**
- Tráfico de 200.000 → **666.000 visitas**

Ninguna es creíble aislada. La vía realista es combinada, porque los factores se multiplican: mejorar cada palanca ~1,5× da 3,375×.

**Escenario que sí cierra:** captura 2,25% → 4.500 subs × 3% compra = 135 ventas × $45 = **$6.075/mes**.

Ese es el plan honesto. Y notá lo que exige: rediseñar la captura, mejorar la secuencia de venta *y* subir el precio 50%. Tres proyectos, no "poner un formulario".

## Mi recomendación

No aprobar como está. Aprobar una versión reescrita con estas condiciones:

1. **Medir antes de proyectar.** Poné el formulario dos semanas y mirá la captura real. Es el número más barato de conseguir y el que más mueve el resultado.
2. **Declarar el objetivo del mes 6 como $2.000-2.500**, con $6.000 como meta del mes 12-18. El plan actual no falla por vago, falla por un objetivo que nadie multiplicó.
3. **Si $6.000 en 6 meses es innegociable** (¿lo es? ¿de dónde sale ese número?), entonces el curso de $30 es el producto equivocado. Con un producto de $150-300 necesitás 20-40 ventas mensuales en vez de 200, y eso sí es alcanzable con 3.000 suscriptores.
4. **Cronograma real:** el mes 1 no factura. Se va en construir el formulario, escribir la secuencia y grabar. El ingreso empieza en el mes 2-3, así que "6 meses" son en realidad 4 de operación.

El plan de tu socio no está mal encaminado — el embudo es correcto y el tráfico es un activo real que mucha gente no tiene. Lo que falta es una multiplicación y una decisión sobre el precio. Con $30 de ticket, esa lista no llega. Con $150, la conversación cambia por completo.