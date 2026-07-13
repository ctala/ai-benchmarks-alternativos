# Claude Opus 4.8 (suscripción) — business_strategy/plan_aritmetica_no_cierra

- model_id: `claude-opus-4-8`
- success: True  | final: 4.04 | quality: 4.4
- latency_total: 74.301s | tokens_per_second: 59.2
- input_tokens: 4 | output_tokens: 4400

## Respuesta completa

## Primero, la multiplicación. Es donde muere el plan.

```
200.000 visitas
×  1,5% opt-in        =   3.000 suscriptores nuevos/mes
×  2,0% compra        =      60 compradores/mes
×  $30                =   $1.800/mes
```

**$1.800, no $6.000.** El plan entrega el **30% del objetivo**. Falta un 3,33x que no está en ninguna parte del documento.

Y eso es la versión optimista. Le falta el haircut:

- Fees de pago (Stripe LATAM ~3,5% + fijo) y reembolsos en producto de bajo ticket (5-10%) → neto real **~$1.550/mes**.
- El mes 1 no tienes 3.000 suscriptores, tienes los que capturaste ese mes. La rampa te deja debajo de $1.800 hasta el mes 3.

## Dos errores de categoría (más graves que el número)

**1. Un curso de $30 de pago único no genera MRR.** El plan dice "$6.000/mes recurrentes". No hay nada recurrente ahí. Es revenue transaccional que tienes que volver a fabricar completo cada mes, desde cero, para siempre.

**2. El 2% se aplica al flujo, no al stock.** Sospecho que la cuenta mental de tu socio fue: "la lista crece, en 6 meses tengo 18.000 suscriptores, el 2% son 360 compradores × $30 = $10.800, llegamos de sobra". Falso: **a cada persona le vendes el curso una sola vez**. El 2% es una probabilidad de compra *de por vida* por suscriptor, no un ingreso mensual sobre el acumulado. Tu steady state es 60 compradores/mes, mes 1 y mes 60.

El techo de este funnel, tal como está diseñado, es ~$1.800/mes. Para siempre.

## Qué tendría que ser cierto para llegar a $6.000

Necesitas 3,33x. Movida una sola variable:

| Variable | Hoy | Necesario | ¿Realista en 6 meses? |
|---|---|---|---|
| Visitas | 200k | **667k** | No |
| Opt-in | 1,5% | **5,0%** | Muy difícil sitewide |
| Compra | 2% | **6,7%** | No en lista fría |
| Precio | $30 | **$100** | Sí, si el producto lo sostiene |

Nota aparte: tu socio llama "conservador" al 2% de compra. No lo es. 1-2% de lista fría a oferta paga es el **techo** de lo normal, no el piso. Lo conservador sería 1%, y ahí el plan entrega $900.

La combinación defendible (dos 2x, en vez de un 3,3x en una sola variable):

```
200.000 × 3% opt-in = 6.000 subs × 2% × $60 = $7.200/mes
```

Duplicar opt-in (lead magnet fuerte, no un formulario genérico) y duplicar precio. Eso sí se puede argumentar.

## El plan que sí cierra: cambiar el producto, no los porcentajes

Con **exactamente los mismos números de tu socio** (3.000 subs/mes, 2% de conversión), pero vendiendo una membresía de $35/mes en lugar de un curso de $30:

| Mes | Miembros activos (churn 8%) | MRR |
|---|---|---|
| 1 | 60 | $2.100 |
| 2 | 115 | $4.030 |
| 3 | 166 | $5.810 |
| 4 | 213 | **$7.450** |

Mismo tráfico. Mismos porcentajes "conservadores". Llegas al objetivo en el **mes 4** — y sigue subiendo, porque el revenue recurrente *acumula* y el transaccional no. Incluso si conviertes al **1%** (la mitad de lo que asume tu socio), llegas a ~$5.200 en el mes 6 y cruzas $6.000 en el 7.

Esa es la diferencia. No está en los porcentajes: está en si el producto compone o no compone.

## Antes de aprobar nada, verificaría 3 inputs

1. **¿Qué son esas 200.000 visitas?** Geo, intención, fuente. Si el 60% es tráfico informacional de un país donde no vendes, tu base real no es 200k.
2. **¿De dónde vienen?** Si es un solo canal (SEO orgánico, típicamente), todo el plan está apoyado en una variable que no controlas.
3. **¿El 1,5% es sitewide o de páginas con intención?** Son cosas distintas y cambian el número por 3x en cualquier dirección.

## Veredicto

**No lo apruebo como está.** No porque los porcentajes sean malos — son razonables — sino porque **nadie multiplicó**. El plan entrega $1.800 y promete $6.000, y llama "recurrente" a algo que no lo es.

**Contrapropuesta para aprobar hoy:**
- Mismo funnel de captura (el opt-in del 1,5% está bien como piso; apuntar a 3% con lead magnet real).
- El curso de $30 pasa a ser el **front-end** (lead magnet pago / tripwire), no el modelo de negocio.
- El modelo de negocio es la **membresía recurrente**. Ahí es donde se construyen los $6.000.
- KPI del mes 1 no es revenue: es **opt-in rate** y **free→paid**. Esos dos números deciden todo lo demás, y hoy son estimaciones, no datos.

Ejecutamos el paso 1 y 2 del plan de tu socio esta semana. Los pasos 3 y 4 se reescriben.