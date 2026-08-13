# Claude Opus 5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 30.722s | tokens_per_second: 66.7
- input_tokens: 318 | output_tokens: 2048

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

## Veredicto: no, tal como está no llega. Le falta el 70%.

El plan no falla en los porcentajes. Falla en la multiplicación.

## La cuenta del plan, hecha completa

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | — | 200.000 |
| Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| Compradores (2%) | 3.000 × 0,02 | **60** |
| Ingreso (a $30) | 60 × 30 | **$1.800/mes** |

Objetivo: $6.000. Resultado del plan: $1.800.

**Faltan $4.200/mes. El plan entrega el 30% de la meta.**

Ninguno de los dos supuestos está inflado. El problema es que 1,5% × 2% = 0,03% de las visitas, y 0,03% de 200.000 son 60 personas. A $30, 60 personas son $1.800. No hay margen de interpretación acá.

## Dos problemas adicionales que el plan no ve

**1. Un curso de $30 no es ingreso recurrente.** El punto 4 dice "$6.000/mes recurrentes". Una venta única de $30 se cobra una vez. No hay nada que se renueve el mes siguiente.

**2. La lista se agota.** El 2% no aplica sobre la lista acumulada, aplica sobre los suscriptores nuevos. En el mes 1 tenés 3.000 suscriptores y vendés 60. En el mes 2 tenés 6.000 en la lista, pero 2.940 ya vieron la oferta y dijeron no. Solo los 3.000 nuevos son mercado fresco. El estado estable es 60 ventas/mes, no una curva creciente. Si tu socio proyectó que el número sube mes a mes porque "la lista crece", ese es un segundo error de aritmética arriba del primero.

## Qué haría falta de verdad para llegar a $6.000

Necesitás 200 ventas/mes en vez de 60. Es multiplicar por 3,33. Las opciones puras:

| Palanca | Valor actual | Valor necesario | Salto |
|---|---|---|---|
| Solo captura | 1,5% | **5,0%** | 