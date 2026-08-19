# Seed 2.1 Turbo — business_audit/retention_sobre_100_interpretacion

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 6.88 | quality: 8.0
- latency_total: 114.098s | tokens_per_second: 71.8
- input_tokens: 169 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

Tu deducción es **incorrecta en dos puntos clave**, y no deberías dejar de preocuparte por el churn. Vamos a desglosarlo con precisión, usando tus propios datos:

---

### Primero: aclaración conceptual fundamental
Estás confundiendo dos métricas de naturaleza muy distinta, y tu error viene de asumir que la retención de ingresos mide lo mismo que la retención de clientes:
| Métrica | ¿Qué mide? | Valor máximo posible |
|---------|------------|----------------------|
| **Retención de clientes (o retención de logos)** | Porcentaje de CLIENTES (cantidad, sin importar cuánto pagan) que estaban al inicio del periodo y siguen activos al final. | 100% (nunca puedes retener más clientes de los que tenías al principio; el crecimiento de la cantidad de clientes viene de nuevas altas, no de retención). |
| **Retención neta de ingresos (NDR, *Net Revenue Retention*)** | Lo que tu panel llama "retención de ingresos": porcentaje de los ingresos de la base de clientes inicial que se mantiene al final del periodo, **incluyendo las expansiones (subidas de plan, upsell, cross-sell) de los clientes que se quedan**, y restando las pérdidas por churn y contracciones de plan. | Sin límite superior: puede superar el 100% si la expansión de los clientes que se quedan compensa más que las pérdidas. |

Tu 114% es NDR: significa que las subidas de plan de tus clientes que se quedaron compensaron con creces la pérdida de ingresos de los clientes que se fueron. Pero eso no implica que "no se vaya nadie": de hecho, con tus datos, el churn de clientes es bastante alto.

---

### Cálculo con tus datos (contexto: 40 clientes el mes pasado, 36 este mes)
Vamos a usar la suposición más favorable para ti: que no captaste ningún cliente nuevo en el mes (es decir, los 36 clientes de este mes son todos de la base inicial de 40). Si hubieras capturado nuevos, el churn sería aún mayor, así que