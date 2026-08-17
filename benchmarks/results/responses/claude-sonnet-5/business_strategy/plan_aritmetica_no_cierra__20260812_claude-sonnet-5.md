# Claude Sonnet 5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 25.273s | tokens_per_second: 73.1
- input_tokens: 318 | output_tokens: 1847

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

# No, la matemática no cierra. Vamos a los números.

## El cálculo real del funnel

```
200.000 visitas
   × 1,5% → 3.000 suscriptores/mes
   × 2%   →    60 compradores/mes
   × $30  →  $1.800/mes
```

**No llegan a $6.000. Llegan a $1.800.** Eso es el **30% del objetivo**, no "cómodo".

## Dónde está el error de razonamiento

Los porcentajes individuales pueden ser "conservadores" en aislamiento, pero **cuando se multiplican tres tasas de conversión en cascada, los conservadurismos se acumulan en contra tuya**, no a favor. 1,5% × 2% es un funnel que retiene el 0,03% del tráfico original. Con ese ratio, necesitás mucho más volumen del que tenés.

## Qué necesitarían para llegar a $6.000

$6.000 / $30 = **200 compradores/mes** (no 60).

Con conversión de 2% suscriptor→comprador, eso exige **10.000 suscriptores/mes** (no 3.000).
Con conversión de 1,5% visita→suscriptor, eso exige **~667.000 visitas/mes** (no 200.000).

O sea: **falta multiplicar por ~3,3x en algún punto del funnel** (tráfico, o conversión a suscriptor, o conversión a compra, o combinación de las tres).

## Un problema adicional, aparte de la multiplicación

Le están llamando "**$6.000/mes recurrentes**" a la venta de un producto de **pago único de $30**. Eso no es MRR real: es ingreso repetible *solo si* siguen alimentando el funnel con tráfico nuevo todos los meses en el mismo volumen. No hay retención, no hay LTV expansion, no hay cohortes acumulándose. Si el tráfico cae un mes, el ingreso cae ese mismo mes. Es más frágil de lo que el plan sugiere.

## Qué preguntaría antes de aprobar

1. ¿De dónde sale el 3,3x faltante: más tráfico, mejor conversión a lista, o mejor conversión a venta?
2. ¿Tienen data real de algún test piloto, o los % son supuestos sin validar?
3. ¿Consideraron un segundo producto/upsell para subir el ticket promedio y no depender solo de escalar volumen?

**Recomendación: no ejecutar el plan tal cual está.** Pedirle a tu socio que rehaga la proyección con el gap explícito y decida qué palanca van a mover para cerrarlo, antes de invertir tiempo/dinero en construir el funnel.