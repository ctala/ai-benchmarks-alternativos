# MiniMax M3.1 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 14.0s | tokens_per_second: 147.1
- input_tokens: 310 | output_tokens: 2060

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **“Retención de ingresos” y “retención de clientes” son métricas distintas.**

### Qué significa probablemente el 114%

Si el indicador es **NRR — Net Revenue Retention / Retención Neta de Ingresos—**, la fórmula habitual es:

\[
NRR = \frac{MRR\ inicial - bajas + expansiones - reducciones}{MRR\ inicial}
\]

Un 114% significa que la **cohorte inicial de clientes genera ahora un 14% más de ingresos recurrentes**, después de contar bajas y reducciones de plan. Es decir, las upgrades compensaron e incluso superaron el churn.

Ejemplo:

- 40 clientes × 100 € = 4.000 € MRR inicial.
- Se van 4 clientes: quedan 3.600 €.
- Las upgrades añaden 960 €.
- MRR final de esa cohorte: 4.560 €.

\[
4.560 / 4.000 = 114\%
\]

Por tanto, el 114% **no significa que conserve al 114% de los clientes**. Si el indicador fuera **GRR — Gross Revenue Retention—**, que excluye las upgrades, normalmente no superaría el 100%.

### Qué dice el cambio de 40 a 36 clientes

Si no entró ningún cliente nuevo:

- Retención de clientes: \(36/40 = 90\%\).
- Churn de clientes: \(4/40 = 10\%\).

Además, 40 → 36 es una cifra **neta**: si captaste clientes nuevos, el churn real podría ser mayor. Por ejemplo, si entraste 3 clientes nuevos, en realidad se fueron 7 de los 40 iniciales, y el churn bruto sería del 17,5%.

### Conclusión

El 114% indica una **fuerte expansión de ingresos entre los clientes que permanecen**, pero no ausencia de churn. De hecho, es compatible con perder clientes y compensarlo mediante upgrades.

No dejaría de preocuparme por el churn: convendría seguir separando:

- Retención de clientes o *logo retention*.
- Churn bruto de clientes.
- GRR: cuánto ingreso se pierde antes de contar expansiones.
- NRR: cuánto crece el ingreso de la cohorte incluyendo upgrades.
- Ingresos por expansión y por contracción.
- CAC y periodo de recuperación.

También verificaría el tooltip del panel: debe aclarar si incluye expansiones, si mide MRR y qué cohorte/periodo utiliza. Un 114% mensual puede ser fuerte, pero podría ser puntual por upgrades o estacionalidad. En tu caso, la señal positiva es la monetización de la base; la señal de alerta es que estás perdiendo clientes.