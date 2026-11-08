# Mercury 2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.36 | quality: 10.0
- latency_total: 7.051s | tokens_per_second: 239.7
- input_tokens: 152 | output_tokens: 1690

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa



No, no es correcto. Una retención de ingresos (NRR) de 114% indica que el crecimiento por expansiones y upgrades compensó la pérdida de facturación, pero no significa que la base de clientes sea estable.

En tu caso, perdiste el 10% de tu base (pasaste de 40 a 36 clientes). Ese es un churn de usuarios real. El hecho de que varios suban de plan está ocultando la erosión en tu base de usuarios.

No dejes de preocuparte por el churn. Adquirir clientes nuevos es significativamente más costoso que retener los existentes. Si ignoras la pérdida de usuarios, la expansión dejará de cubrir el vacío y el NRR caerá. Analiza por qué se van esos 4 clientes mientras mantienes el momentum de upsell.