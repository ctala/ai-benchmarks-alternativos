# Grok 4.6 — business_audit/retention_sobre_100_interpretacion

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 31.064s | tokens_per_second: 55.4
- input_tokens: 328 | output_tokens: 1721

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Esa lectura es incorrecta y peligrosa.**

La cifra del 114 % es **retención neta de ingresos (NRR / Net Revenue Retention)** de la cohorte del mes anterior, no retención de clientes. Puede superar el 100 % porque incluye expansiones (upgrades de plan) que compensan —y superan— las pérdidas por churn y contracciones. No significa que “casi no se te va nadie”.

Con tus números:
- Retención de **clientes (logos)**: 36/40 = **90 %**. Churn de clientes del **10 % mensual**.
- Eso implica que, si se mantiene, en 12 meses te quedarías con ~28 % de los clientes originales (0,9¹²). Es un churn elevado para SaaS, especialmente si es recurrente.
- El 114 % de ingresos se explica porque los 36 que se quedaron subieron de plan lo suficiente como para más que cubrir los ingresos perdidos de los 4 que se fueron. Las expansiones enmascaran el problema de logos, no lo eliminan.

**No puedes dejar de preocuparte por el churn ni meter todo el esfuerzo solo en captación.** Un NRR >100 % es una señal positiva de que hay potencial de expansión en los que se quedan, pero:
- El churn de clientes sigue destruyendo base y LTV. Las expansiones tienen techo; los clientes que se van no vuelven a expandir.
- Un 10 % mensual de logos es un síntoma (onboarding, product-market fit en ciertos segmentos, pricing, soporte, etc.) que hay que diagnosticar. Ignorarlo hace que el crecimiento neto dependa cada vez más de un grupo cada vez más pequeño.
- Captar más gente nueva mientras se fuga el 10 % mensual es ineficiente: pagas CAC para reponer lo que se pierde y el NRR alto se vuelve más frágil.

Prioriza las dos cosas: reduce el churn de logos (retención + reactivación) **y** sigue captando, mientras mides también GRR (retención bruta de ingresos, sin expansiones) para ver el agujero real. El 114 % te dice que los que se quedan pagan más; no te dice que el negocio esté sano en retención de clientes.