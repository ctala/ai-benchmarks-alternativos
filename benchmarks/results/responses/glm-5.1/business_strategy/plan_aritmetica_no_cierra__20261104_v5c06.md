# GLM-5.1 — business_strategy/plan_aritmetica_no_cierra

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 18.584s | tokens_per_second: 60.6
- input_tokens: 212 | output_tokens: 1126

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

# No se aprueba. La multiplicación no llega.

Tu socio hizo lo que hace casi todo el mundo: eligió porcentajes que suenan bien por separado y nunca los multiplicó de punta a punta.

## La cuenta real

| Paso | Cálculo | Resultado |
|------|---------|-----------|
| Visitas | — | 200.000 |
| Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| Compradores (2%) | 3.000 × 0,02 | **60** |
| Ingresos ($30 c/u) | 60 × $30 | **$1.800** |

**$1.800, no $6.000.**

El plan queda en **30% del objetivo**. No es un ajuste fino, es un abismo.

## Qué se necesitaría para llegar a $6.000 con estos porcentajes

- **666.667 visitas/mes** (3,3× más tráfico)
- o **5% de captura** (3,3× más conversión)
- o **6,7% de compra** (3,3× más venta)
- o **$100 de precio** (3,3× más caro)

O una combinación de los cuatro. Pero algo tiene que ceder 3,3×.

## Y hay un segundo problema

El plan dice **"recurrentes"**. Un curso de $30 se vende una vez. No hay recurrencia. A menos que el 2% compre *cada mes* —lo cual no va a pasar con el mismo curso y la misma lista.

## Veredicto

> Los porcentajes individualmente son sanos. El problema es que **son sanos y por eso no llegan**. Si fueran lo suficientemente altos para llegar a $6.000, ya no serían conservadores —serían irreales.

Vuelve con tu socio, pongan los $1.800 sobre la mesa, y decidan qué palanca mueven: **tráfico, captura, conversión, precio o modelo de recurrencia real.**