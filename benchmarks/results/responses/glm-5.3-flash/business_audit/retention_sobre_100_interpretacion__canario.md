# GLM 5.3 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 54.554s | tokens_per_second: 74.4
- input_tokens: 138 | output_tokens: 4061

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, y el panel te está contando dos historias distintas. Vamos por partes.

## Qué mide realmente ese 114%

Ese número casi con certeza es **Net Revenue Retention (NRR)**: los ingresos que genera *la misma cohorte* de clientes, contando expansiones (upgrades) y restando churn y downgrades. Se mide en **dinero**, no en personas. Y sí, supera el 100%, pero la retención de *clientes* tiene techo matemático en 100% — nadie retiene clientes "por encima del 100%".

Tus datos reales de logos: **40 → 36 = 90% de retención mensual**. Se te fue 1 de cada 10 clientes en un mes. "Prácticamente no se va nadie" no es la lectura correcta; anualizado, ese ritmo implica que de cada 100 clientes solo quedan ~28 al año (0,9¹² ≈ 0,28), con vida media de ~10 meses.

## La aritmética detrás de tu panel

Asumiendo que no entraron clientes nuevos este mes (si entró alguno, el churn real fue aún mayor que 4 cuentas):

| Concepto | Número | Lectura |
|---|---|---|
| Retención de logos | 36/40 = 90% mensual | 4 cuentas perdidas |
| GRR (ingresos sin expansión) | ≈ 90% | Pierdes ~10% de ingresos por churn |
| NRR | 114% | La expansión supera lo perdido |

Si cada cliente pagaba ~100€ (4.000€ MRR inicial), un NRR de 114% significa que los supervivientes generan 4.560€: los 36 restantes aportan ~960€ de expansión, un ticket medio que sube de 100€ a ~127€. **Tu base se encoge en personas y crece en dinero.** El 114% es la expansión tapando el churn, no su ausencia.

## Por qué "meter todo en captación" es la decisión equivocada

1. **Cubo agujereado.** Con 10% de churn mensual, buena parte de lo que captes solo reemplaza a quien se va. Tu CAC está comprando reposición, no crecimiento.
2. **La expansión tiene techo.** Los upgrades son finitos: tu escalera de precios se agota. Cuando todos los que podían subir hayan subido, tu NRR converge hacia el GRR (~90%), y descubrirás el problema de churn en el peor momento posible.
3. **Concentración.** Ese +960€ probablemente venga de 2-3 cuentas. Perder una sola de ellas hunde el NRR de forma desproporcionada. Estás cada vez más expuesto a menos decisiones de compra.
4. **Volatilidad de muestra.** Con n=40, un solo upgrade o una sola fuga mueve la métrica varios puntos. Un 114% de un mes no es tendencia; es un dato.

## Lo que sí haría

- Medir las **tres métricas por separado** (logos, GRR, NRR) y mirar tendencia de 3-6 meses, no el dato puntual.
- **Entrevistar a los 4 que se fueron.** Es diagnóstico de producto/precio/servicio gratis y te está hablando ahora.
- Identificar **qué cuentas impulsaron la expansión** y medir concentración de ingresos.
- Seguir captando, sí — pero tratando el churn como el problema abierto que sigue siendo.

El 114% es genuinamente una buena noticia: significa que quienes se quedan obtienen más valor. Pero es motivo para vigilar *más* el churn, no para dejar de mirarlo.