# Mercury 2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `inception/mercury-2.5`
- success: True  | final: 7.97 | quality: 8.0
- latency_total: 5.203s | tokens_per_second: 313.1
- input_tokens: 149 | output_tokens: 1629

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa



No es correcto. El 114% mide la retención de ingresos (NRR), no la de usuarios (logo retention).

Perdiste 4 cuentas de 40, lo que representa una fuga del 10%. El aumento de ingresos se debe a que los restantes incrementaron su gasto, compensando la pérdida de volumen.

No debes descuidar la fuga. Adquirir una cuenta nueva suele ser más costoso que mantener una existente. Si ignoras esta pérdida, dependes excesivamente de la captación para crecer, lo que es ineficiente a largo plazo.

Usa ese NRR alto como ventaja, pero investiga la razón de las bajas para estabilizar la base.