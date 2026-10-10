# Claude Opus 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 16.356s | tokens_per_second: 86.9
- input_tokens: 218 | output_tokens: 1422

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## No es correcto, y tus propios datos lo muestran

El 114% casi seguro es **retención neta de ingresos (NRR)**, no retención de clientes. Son métricas distintas:

| Métrica | Qué mide | Tu caso |
|---|---|---|
| **Retención de clientes (logos)** | Cuántos clientes siguen pagando | 36 de 40 → **90%** (como máximo) |
| **Retención neta de ingresos (NRR)** | Ingresos de la cohorte existente, sumando subidas de plan y restando bajas y bajadas | **114%** |

La retención de clientes **nunca puede superar el 100%**: no puedes retener más clientes de los que tenías. Lo que sí puede superar el 100% son los ingresos, si los que se quedan pagan bastante más.

Tu situación real es esta: **perdiste al menos 4 clientes (10%) en un mes, y las subidas de plan de otros lo compensaron con creces.**

## Por qué un 10% mensual de churn es serio

- **Acumulado en un año:** 0,90¹² ≈ 0,28. Si se mantiene, de cada 100 clientes de hoy te quedarían unos 28 dentro de 12 meses.
- **Puede ser peor de lo que parece:** si entre los 36 hay clientes nuevos de este mes, las bajas reales son más de 4. Por ejemplo, con 3 nuevos habrías perdido 7 (17,5%).
- **Dependes de pocos:** el 114% se apoya en que "varios" subieron de plan. Si uno o dos de esos clientes grandes se van, la NRR puede caer por debajo del 100% de golpe. Con 36 clientes, cada cuenta pesa mucho.
- **Captar no arregla el problema:** si metes todo el esfuerzo en adquisición, llenas un cubo con un agujero. Gran parte de lo que capturas se irá igual que los 4 de este mes, y el coste de adquisición se desperdicia.

## Qué revisaría en el panel

1. **¿El 114% es mensual o anual?** Un 114% mensual sería excepcional y conviene confirmarlo. Un 114% anual es bueno, pero no te dice nada del churn de logos.
2. **¿Excluye ingresos de clientes nuevos?** Si los incluye, no es una NRR real y está inflada.
3. **Desglosa el movimiento de MRR:** inicial, expansión, contracción, churn y nuevo. Así verás cuánto perdiste en bajas frente a cuánto ganaste en subidas.
4. **Logos perdidos vs. nuevos este mes,** para saber el churn real.

## Recomendación

No dejes el churn de lado. El dato bueno es que tienes clientes que valoran el producto lo suficiente para pagar más. El malo es que pierdes 1 de cada 10 al mes. Yo haría:

- **Hablar con los 4 (o más) que se fueron:** ¿precio, falta de valor, onboarding, encaje equivocado?
- **Comparar perfiles:** ¿en qué se parecen los que suben de plan y en qué los que se van? Eso te dice a quién captar.
- **Captar en función de eso:** atrae clientes parecidos a los que expanden, no clientes en general.

Así la captación y la retención se refuerzan en lugar de competir por tu tiempo.