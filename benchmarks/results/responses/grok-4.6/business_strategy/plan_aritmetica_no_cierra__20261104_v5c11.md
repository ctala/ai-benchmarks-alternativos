# Grok 4.6 — business_strategy/plan_aritmetica_no_cierra

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 23.07s | tokens_per_second: 58.8
- input_tokens: 400 | output_tokens: 1357

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

**No. Los números no llegan.** El plan muere en la multiplicación.

Cálculo con *sus propios supuestos*:

- 200.000 visitas × 1,5 % = **3.000 suscriptores/mes**
- 3.000 × 2 % = **60 ventas/mes**
- 60 × $30 = **$1.800/mes**

Objetivo: **$6.000**. Están al **30 %** del target. Faltan **$4.200/mes** (más de 3×).

Para llegar a $6.000 con un producto de $30 necesitan **200 ventas/mes**. Con 2 % de conversión eso exige **10.000 suscriptores**, lo que a 1,5 % requiere **~667.000 visitas/mes**, no 200.000.

Además el plan habla de “$6.000/mes **recurrentes**”. Un curso de $30 es ingreso puntual, no recurrente, salvo que lo conviertan en suscripción/membresía (no está en el plan).

Los porcentajes pueden ser “sanos”; el problema es que **no multiplican hasta el objetivo**. No ejecutamos esto. O suben tráfico/conversiones/precio de forma realista y vuelven a calcular, o cambian de oferta.