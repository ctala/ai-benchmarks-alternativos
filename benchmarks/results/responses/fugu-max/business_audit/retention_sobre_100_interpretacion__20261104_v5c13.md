# Fugu Max — business_audit/retention_sobre_100_interpretacion

- model_id: `sakana/fugu-max`
- success: True  | final: 7.29 | quality: 8.0
- latency_total: 6.721s | tokens_per_second: 81.1
- input_tokens: 219 | output_tokens: 545

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Si el 114% es la **retención neta de ingresos (NRR)** estándar, significa que los clientes que ya tenías generaron este mes un 14% más de ingresos recurrentes que al inicio, **contando las subidas de plan** y descontando bajas y reducciones. No significa que no haya churn: las ampliaciones pueden compensarlo y más.

Tampoco implica que la retención de clientes supere el 100%. Pasaste de 40 clientes de pago a 36: una caída neta del 10%. Si entraron clientes nuevos durante el mes, incluso pudieron irse más de cuatro; el cambio neto no revela las bajas brutas.

Un ejemplo: empiezas con 100 € de ingresos; pierdes 20 € por bajas o reducciones, pero sumas 34 € por mejoras de plan. La NRR da 114%, aunque hubo pérdida de ingresos por churn antes de contar las ampliaciones.

Antes de priorizar adquisición, revisa **churn de clientes**, **retención bruta de ingresos (GRR, sin ampliaciones)** y **NRR**, idealmente por cohorte. Y confirma cómo define el panel “retención de ingresos”: las fórmulas pueden variar.