# Claude Opus 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.25 | quality: 10.0
- latency_total: 13.954s | tokens_per_second: 85.4
- input_tokens: 320 | output_tokens: 1191

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

# No lo aprobaría así: los números del plan dan $1.800/mes, no $6.000

Los porcentajes pueden ser razonables, pero multiplicados no llegan al objetivo.

## La cuenta

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | — | 200.000 |
| Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| Compradores (2%) | 3.000 × 0,02 | **60** |
| Ingresos ($30) | 60 × $30 | **$1.800/mes** |

Eso es el **30% del objetivo**. Faltan $4.200/mes.

## Otro problema: "recurrentes"

Un curso de $30 se vende **una sola vez** por cliente. No es recurrente. Cada mes hay que conseguir 60 compradores *nuevos*. Los suscriptores acumulados pueden aportar ventas tardías, pero no es un ingreso garantizado mes a mes.

## ¿Qué haría falta para llegar a $6.000?

Se necesitan **200 ventas/mes** a $30. Algunas formas de lograrlo, cada una moviendo una sola palanca:

| Palanca | Valor actual | Valor necesario | ¿Realista? |
|---|---|---|---|
| Conversión a suscriptor | 1,5% | **5%** (10.000 subs) | Difícil, más del triple |
| Conversión a compra | 2% | **6,7%** | Difícil, más del triple |
| Precio del curso | $30 | **$100** | Posible si el producto lo justifica |
| Tráfico | 200.000 | **667.000** | Improbable en 6 meses |

Lo más sensato es **combinar palancas moderadas**. Por ejemplo:
- Captura del 2% → 4.000 suscriptores
- Compra del 3% → 120 ventas
- Precio de $50 → **$6.000/mes**

También conviene sumar algo **realmente recurrente**, como una membresía, una comunidad paga o una suscripción, o un upsell de mayor precio. Así el ingreso no depende de vender a gente nueva cada mes.

## Recomendación

No ejecutar el plan tal cual. En cambio:
1. **Corregir el objetivo o la estrategia.** Con estos supuestos, la meta honesta es ~$1.800/mes.
2. **Validar los porcentajes primero.** Lancen el formulario y el curso durante 4–6 semanas y midan las conversiones reales antes de proyectar.
3. **Rediseñar la oferta** (precio, upsell, producto recurrente) para que la multiplicación sí cierre en $6.000.

¿Quieren que armemos una versión del plan con combinaciones de precio y producto que sí lleguen al objetivo?