# MiniMax M2.7 (directo) — business_audit/retention_sobre_100_interpretacion

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.33 | quality: 8.0
- latency_total: 21.163s | tokens_per_second: 37.4
- input_tokens: 128 | output_tokens: 791

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, tu interpretación es incorrecta. Y el dato que das al final (40 → 36 clientes) es justo la prueba.

## Lo que realmente significa "Retención de ingresos: 114%"

Esa métrica mide **cuánto ingreso retienes de tu base de clientes existente**, incluyendo expansiones. La fórmula simplificada:

```
Retención de ingresos = (Ingresos inicio de mes - churned + expansiones) / Ingresos inicio de mes
```

Un 114% significa que **de tu base de clientes del mes pasado, los ingresos que generan ahora son un 14% mayores**. Eso se explica así:

| Concepto | Efecto en ingresos |
|---|---|
| Ingresos de clientes que se fueron | − |
| Ingresos de clientes que bajaron de plan | − |
| Ingresos de clientes que subieron de plan | + |
| Nuevos upsells, add-ons | + |

**Resultado neto: +14%** sobre la base anterior.

## Tu situación real

| Dato | Valor |
|---|---|
| Clientes inicio de mes | 40 |
| Clientes fin de mes | 36 |
| Clientes perdidos (churn) | 4 |
| **Churn rate** | **10%** |

Perdiste el **10% de tus clientes**. Eso no es "que no se te va nadie".

## Por qué una métrica no cancela a la otra

La retención de ingresos puede estar altísima mientras el churn también es alto. Simplemente significa que **los que quedan gastan significativamente más**. Es una situación delicada, no una señal de alivio:

- El churn del 10% mensual implica que en ~8-10 meses renuevas casi toda tu base si no cambias nada
- La expansión actual de tus clientes puede tener techo
- Estás subsidando la fuga con el gasto de los que permanecen

## Respuesta directa a tu pregunta

> ¿Puedo dejar de preocuparme por el churn?

**No.** El 114% te está diciendo que tus clientes restantes son más valiosos, pero también que estás en una situación de riesgo: dependes de que sigan expandiéndose o de que los que quedan no se vayan. Si eso pasa, tu retención de ingresos caería en picado.

La retención de ingresos y la retención de clientes miden cosas distintas. Ambas importan.