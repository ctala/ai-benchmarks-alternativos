# MiniMax M2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 16.142s | tokens_per_second: 46.5
- input_tokens: 128 | output_tokens: 750
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y práctica de la métrica NRR y sus implicaciones para un emprendedor.

## Respuesta completa

No, esa interpretación no es correcta. Y el motivo está en los datos que das al final: **perdiste 4 clientes** (de 40 a 36). El 114% no contradice eso — lo que hace es ocultarlo parcialmente.

## Qué significa realmente el 114%

Lo que estás viendo es casi con seguridad **Net Revenue Retention (NRR)**, no retención bruta de clientes. Son métricas distintas:

- **GRR (Gross Revenue Retention)**: Mide cuánto ingresos conservas de los clientes que había al inicio del periodo. El máximo teórico es 100% — si alguien se va, baja.
- **NRR (Net Revenue Retention)**: Lo mismo, pero **suma** el crecimiento de los clientes que se quedaron (upsells, cross-sells, expansiones). Por eso puede superar el 100%.

Tienes 36 clientes este mes. Seguramente varios de los que quedaron pagaron más que antes, y eso compensó con creces la recaída de los 4 que se fueron. De ahí el 114%.

## Por qué no puedes dejar de preocuparte por el churn

| Métrica | Tu caso |
|---------|---------|
| Clientes inicio de mes | 40 |
| Clientes fin de mes | 36 |
| **Churn de clientes** | **10%** (4/40) |
| Ingresos inicio de mes | X |
| Ingresos fin de mes | ~1.14X |

El churn del 10% es significativo. En SaaS recurrentes, ese ritmo implica perder la mitad de tu base en ~7 meses si no se soluciona. El NRR alto solo significa que los que se quedan gastan más — no que los que se fueron no importen.

## La lectura honesta

Tienes dos problemas simultáneos:

1. **Fuga de clientes** — 4 personas dejaron el producto. Necesitas saber por qué.
2. **Expansión positiva** — los que quedan pagan más. Eso está bien, pero no compensa la fuga estructuralmente.

El NRR alto es un buen indicador de que tu producto genera valor para quienes se quedan. Pero el churn del 10% te está diciendo que hay un problema de ajuste producto-mercado con una parte de tus clientes. Ignorarlo es peligroso: si mañana el upsell se estanca, te quedas sin clientes y sin crecimiento.