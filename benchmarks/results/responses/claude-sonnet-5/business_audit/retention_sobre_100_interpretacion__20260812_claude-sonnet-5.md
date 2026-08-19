# Claude Sonnet 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.0 | quality: 8.0
- latency_total: 14.664s | tokens_per_second: 72.7
- input_tokens: 216 | output_tokens: 1066

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa lectura es incorrecta, y en tu caso concreto es especialmente engañosa. Vamos a desglosarlo.

## Qué mide realmente ese 114%

Es casi seguro que es **Net Revenue Retention (NRR)**, que se calcula sobre los ingresos de los clientes que ya tenías, no sobre el número de clientes:

NRR = (Ingresos inicio + Expansión − Contracción − Churn) / Ingresos inicio

Un 114% significa que **los ingresos** de esa cohorte crecieron un 14% neto. Pero eso puede convivir perfectamente con una pérdida importante de clientes, si los que se quedan gastan mucho más.

## Tu caso: pasaste de 40 a 36 clientes

Eso es una **pérdida de logos del 10%** (4 de 40). No es "prácticamente nadie se va": es 1 de cada 10 clientes.

Lo que probablemente pasó es que los subidas de plan de los que se quedaron (36 clientes) compensaron con creces:
- Los ingresos perdidos por los 4 que se fueron (churn de ingresos).
- Cualquier downgrade de otros.

Y el resultado neto en euros fue positivo (+14%). Pero eso es una métrica de **ingresos**, no de **retención de clientes (logo retention)**.

## Por qué la diferencia importa

- **NRR alto + churn de logos alto** suele ser señal de que tu base de clientes se está concentrando en pocas cuentas grandes. Es una situación con riesgo de concentración: si una de esas cuentas grandes se va, el impacto es mucho mayor.
- Si el 10% que se fue eran los clientes más pequeños o los de menor "fit", puede no ser grave. Pero si no lo sabes, es una pregunta que deberías hacerte, no asumir que está bien.
- Un churn de logos del 10%/mes es una tasa muy alta (equivalente a ~70%+ anualizado si es constante). Aunque el NRR esté sano, ese ritmo de fuga de clientes suele ser insostenible para el crecimiento a largo plazo (necesitas reponer constantemente esa base con clientes nuevos, y cada vez con contratos más caros para compensar).

## Qué mirar en paralelo

1. **Logo retention / logo churn**: cuántos clientes (no €) se quedaron.
2. **Quiénes se fueron**: ¿eran cuentas pequeñas de prueba, o clientes "de verdad"?
3. **NRR desagregado**: cuánto es expansión de los que se quedaron vs. cuánto es churn de ingresos de los que se fueron. Un 114% puede ocultar, por ejemplo, un -30% de churn de ingresos compensado por +44% de expansión.

## Conclusión

No puedes "dejar de preocuparte por el churn". El NRR de 114% te dice que monetizas bien a quien se queda, pero tienes una fuga de clientes del 10% mensual que merece investigación urgente, independientemente de que la caja esté creciendo hoy.