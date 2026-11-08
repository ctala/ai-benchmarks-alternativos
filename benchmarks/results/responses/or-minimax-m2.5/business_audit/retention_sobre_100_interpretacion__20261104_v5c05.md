# MiniMax M2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 7.55 | quality: 8.0
- latency_total: 9.139s | tokens_per_second: 99.7
- input_tokens: 130 | output_tokens: 911

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

# No, esa interpretación no es correcta

El 114% te está diciendo algo importante, pero no lo que crees. Desglosemos:

## Lo que realmente significa 114%

La **retención de ingresos** (Net Revenue Retention) mide dinero, no clientes. Puedes tener:

- Gente que se va (churn) → baja los ingresos
- Gente que se queda y gasta más (upgrades, más uso) → sube los ingresos

Con 114%, el efecto neto es que los clientes que conservaste te generan **14% más ingresos** que el mes pasado. Eso es bueno.

## Pero mirá tu situación real

| Métrica | Valor |
|---------|-------|
| Clientes mes pasado | 40 |
| Clientes este mes | 36 |
| **Clientes perdidos** | 4 (10% churn) |
| Ingresos | Subieron por upgrades |

Perdiste el **10% de tus clientes**. Eso no es "no se me va nadie". Es churn real.

## Por qué no podés dejar de preocuparte por el churn

El 114% es un indicador de *expansión*, no de retención pura. Depende de dos cosas:

1. **Upgrades** → te generan más ingreso por cliente
2. **Churn** → te resta clientes

Si mañana nadie hace upgrade, tu NRR cae a 90% (porque seguís perdiendo 10% de clientes). Estás dependiendo de que los clientes que se quedan gasten más para compensar los que se van.

## La lectura correcta

Tenés un negocio donde:
- Los clientes que se quedan valoran el producto (por eso suben de plan)
- Pero también se te escapan clientes nuevos o inadecuados

El churn del 10% mensual es preocupante. Si mantenés ese ritmo, en 7 meses te quedás sin clientes.

**Conclusión**: Seguí invirtiendo en captar, pero no abandones el análisis de por qué se van esos 4 clientes. El 114% es un indicador de que *los que se quedan son buenos*, no de que el churn no importa.