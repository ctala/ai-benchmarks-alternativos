# Claude Opus 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 17.134s | tokens_per_second: 92.1
- input_tokens: 320 | output_tokens: 1578

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

# No lo aprobaría así: los porcentajes son razonables, pero el resultado no llega

## La multiplicación

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | | 200.000 |
| Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| Compradores (2%) | 3.000 × 0,02 | **60** |
| Ingresos ($30) | 60 × $30 | **$1.800/mes** |

**El plan llega a $1.800/mes, el 30% del objetivo.** Faltan $4.200 cada mes.

## Lo que haría falta

Para $6.000 se necesitan **200 ventas al mes** ($6.000 ÷ $30). Eso exige que el 0,1% de las visitas termine en compra, y el plan actual convierte el 0,03% (1,5% × 2%). Hay que **multiplicar por 3,3** el embudo. Algunas formas de lograrlo:

| Opción | Captura | Compra | Precio | Ingresos |
|---|---|---|---|---|
| Plan actual | 1,5% | 2% | $30 | $1.800 |
| Solo subir captura | **5%** | 2% | $30 | $6.000 |
| Solo subir compra | 1,5% | **6,7%** | $30 | $6.000 |
| Solo subir precio | 1,5% | 2% | **$100** | $6.000 |
| Combinación | 2,5% | 3% | **$80** | $6.000 |

El problema es que cada palanca por separado obliga a salir del rango "conservador" que justifica el plan. La vía más realista suele ser una **combinación**: mejorar un poco cada etapa y, sobre todo, aumentar el valor por cliente.

## Ojo también con la palabra "recurrentes"

Un curso de $30 es una **venta única**, no recurrente. Cada mes dependes de captar 3.000 suscriptores nuevos y venderles otra vez. Volver a ofrecer el curso a la lista antigua rinde cada vez menos, porque quien iba a comprar ya compró. Si buscan ingresos recurrentes de verdad, hace falta una suscripción, una membresía o una escalera de productos (curso → programa avanzado → mentoría).

## Mi recomendación

1. **Ejecuten el embudo, pero como experimento.** Montar el formulario y la venta es barato y les da datos reales en 30–45 días.
2. **Cambien la meta del plan** a algo coherente con sus números: unos $1.800/mes con el embudo actual, más lo que aporten las mejoras.
3. **Diseñen desde ya las palancas que faltan:**
   - Un lead magnet más fuerte o pop-ups por intención de salida, para acercar la captura al 3–5%.
   - Una secuencia de emails de venta en lugar de un solo envío, para subir la compra.
   - Un upsell o una versión premium de $97–$197, para subir el ingreso por cliente.
4. **Mídanlo en el mes 1** y recalculen. Si la captura real resulta del 0,8% y no del 1,5%, mejor saberlo antes del mes 6.

**Resumen:** no es mal plan, pero su propia aritmética da $1.800, no $6.000. Aprueben la ejecución, no la promesa de resultado.