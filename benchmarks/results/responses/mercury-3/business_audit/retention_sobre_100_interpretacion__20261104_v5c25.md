# Mercury 3 — business_audit/retention_sobre_100_interpretacion

- model_id: `inception/mercury-3`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 6.747s | tokens_per_second: 357.4
- input_tokens: 153 | output_tokens: 2411

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, no es correcto. Y no, no deberías dejar de preocuparte por el churn.

Lo que estás viendo es **retención neta de ingresos** (Net Revenue Retention, NRR), no retención de clientes. Son métricas distintas y pueden contar historias muy diferentes.

## Qué significa realmente 114%

La retención neta de ingresos mide **cuánto ingreso recurrente conservas de tus clientes existentes**, sumando los upgrades y restando bajas, downgrades y churn:

\[
NRR = \frac{MRR\ inicial + expansión - contracción - churn}{MRR\ inicial}
\]

Que dé 114% significa que **los ingresos de tu base actual crecieron un 14%**, no que no se te haya ido nadie.

De hecho, tu propio contexto lo confirma:

- El mes pasado tenías **40 clientes de pago**.
- Este mes tienes **36**.
- Perdiste **4 clientes**, o sea un **10% de churn de clientes**.
- Tu retención de clientes es del **90%**, no del 114%.

Lo que pasa es que los clientes que se quedaron y subieron de plan aportaron suficiente ingreso extra como para compensar la pérdida de los 4 que se fueron. Eso es excelente para la monetización, pero no significa que no haya fuga.

## Un ejemplo numérico

Supón que el mes pasado tenías $40,000 de MRR (promedio $1,000 por cliente).

Este mes:

- 4 clientes se van: pierdes $4,000.
- Los 36 restantes, antes de upgrades, aportarían $36,000.
- Para que el NRR sea 114%, necesitas $45,600 de MRR.
- Eso implica que los upgrades aportaron $9,600 adicionales.

Es decir: perdiste clientes, pero los que se quedaron pagan mucho más. El panel solo te muestra el efecto neto en ingresos, no la salud de tu base de clientes.

## Por qué no puedes ignorar el churn

1. **Tu base se está encogiendo.** Si sigues perdiendo 4 clientes al mes, eventualmente te quedas sin clientes, aunque el ingreso promedio suba.
2. **La expansión no es garantizada.** Los upgrades pueden ser puntuales. Si se detienen, el ingreso caerá rápido.
3. **Captar clientes nuevos es más caro que retener.** Si el churn es alto, necesitas gastar cada vez más solo para mantener el mismo nivel de ingresos.
4. **Un NRR alto puede enmascarar problemas de producto.** Si tus clientes se van pero los que se quedan pagan más, puede que estés sobreviviendo gracias a unos pocos clientes grandes, no a un negocio sano.

## Qué deberías mirar

- **Churn de clientes**: 40 → 36 = 10% mensual. Eso es alto.
- **Retención bruta de ingresos (GRR)**: excluye upgrades. Seguramente está por debajo del 100%, probablemente cerca del 90%.
- **NRR por cohorte**: no solo el global, para ver si la expansión compensa el churn de forma consistente.
- **LTV y CAC**: si el churn es alto, tu LTV baja y necesitas CAC mucho más bajo para que el negocio sea rentable.

En resumen: 114% de retención de ingresos es una buena señal de que tus clientes valoran el producto y están dispuestos a pagar más. Pero no es una señal de que no se te vaya nadie. Tu churn de clientes es real y deberías atacarlo antes de poner todo el esfuerzo en captar gente nueva.