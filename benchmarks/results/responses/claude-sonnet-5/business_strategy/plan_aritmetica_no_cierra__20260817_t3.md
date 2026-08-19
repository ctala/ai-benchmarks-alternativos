# Claude Sonnet 5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 23.678s | tokens_per_second: 78.8
- input_tokens: 318 | output_tokens: 1865

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

## Verificación de la matemática

Multipliquemos la cadena exactamente como la plantea el plan:

```
200.000 visitas
   × 1,5% conversión a suscriptor  =  3.000 suscriptores/mes
   × 2% conversión a compra        =  60 compradores/mes
   × $30 (precio del curso)        =  $1.800/mes
```

**Resultado real: $1.800/mes, no $6.000/mes.**

Falta un **3,3x** para llegar al objetivo. No es un error de redondeo, es una brecha estructural: el plan tal como está escrito llega al 30% de la meta.

## Un segundo problema, más grave: la palabra "recurrentes"

Un curso de $30 es **venta única**, no suscripción. Cada suscriptor compra una vez y no vuelve a pagar. Lo que este embudo genera —si el tráfico se mantiene estable mes a mes— es un **flujo mensual de ingresos nuevos**, no MRR real (no hay churn, no hay cobro recurrente, no hay LTV acumulándose). Si el tráfico baja un mes, el ingreso baja ese mes. Vale la pena que se alineen en qué significa "recurrente" antes de fijar el objetivo.

## ¿Qué tendría que cambiar para cerrar la brecha de 3,3x?

Algunas combinaciones que sí llegan a $6.000 (elige una o mezcla varias, no las sumes todas):

| Palanca | Valor necesario (dejando el resto igual) |
|---|---|
| Precio del curso | subir de $30 a ~$100 |
| Conversión a suscriptor | subir de 1,5% a ~5% |
| Conversión a compra | subir de 2% a ~6,7% |
| Tráfico | subir de 200k a ~666k visitas/mes |
| Combinado realista | ej: suscriptor 3% + compra 3,3% + precio $30 → ~$5.940 |

## Mi recomendación

No lo apruebes en su forma actual. No porque los porcentajes individuales sean irreales (1,5% y 2% son razonables), sino porque **nadie hizo la multiplicación final antes de comprometerse con la cifra de $6.000**.

Antes de ejecutar, pediría que el socio ajuste el plan eligiendo explícitamente qué palanca van a mover (precio, oferta upsell, mejorar el embudo) para cerrar el 3,3x, y que reformule el objetivo como "ingreso mensual por ventas" en lugar de "recurrente", salvo que agreguen algo que sí sea suscripción (membresía, cohortes pagas, etc.).