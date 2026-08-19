# Sakana Namazu — business_audit/retention_sobre_100_interpretacion

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 9.552s | tokens_per_second: 214.4
- input_tokens: 161 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Es incorrecto, y sería un error estratégico grave dejar de preocuparte por el *churn* de clientes.**

Tus clientes se están yendo. Pasaste de 40 a 36: eso es un **10% de *churn* de clientes** (logo churn) en un solo mes. Si esa tasa se sostiene, anualmente perderías casi tres de cada cuatro clientes (0,9^12 ≈ 28% de retención de clientes). Eso no es “prácticamente no se me va nadie”; es una fuga muy seria.

Lo que está pasando es una distinción clásica de SaaS que el panel está agrupando en una sola cifra halagadora:

---

### 1. Estás confundiendo dos métricas distintas

| Métrica | ¿Qué mide? | ¿Puede ser >100%? |
|---|---|---|
| **Retención de clientes** (Logo Retention) | ¿Qué % de clientes se quedan? | **No**. El máximo es el 100%. |
| **Retención de ingresos** (Revenue Retention, normalmente NRR) | ¿Qué ingresos mantengo/expando de mi base actual? | **Sí**, si los upgrades superan el dinero perdido por clientes que se van o bajan de plan. |

Tu 114% es **Net Revenue Retention (NRR)**, no retención de clientes. Significa que los upgrades (`expansion revenue`) de los clientes que se quedaron compensaron con creces la pérdida de ingresos de los 4 que se fueron.

**Ejemplo con tus números (ilustrativo):**

*   **Mes pasado:** 40 clientes × \$100 = \$4.000 MRR.
*   **Este mes de esos 40 iniciales:** 36 se quedaron, 4 se fueron.
*   **Sin upgrades**, tu MRR sería \$3.600 (90% de retención bruta de ingresos / Gross Revenue Retention).
*   Pero con los upgrades de los que subieron de plan, tu MRR de esa cohorte llegó a **\$4.560** (\$4.000 × 1,14).

Eso es financieramente positivo, pero no mágico: **berretines de clientes sustituidos por subidas de precio de los fieles**.

---

### 2. Por qué NO puedes ignorar el churn y meter todo en adquisición

Un NRR > 100% con un logo churn alto es una señal de tensión, no de salud plena:

*   **Es un balde con agujeros.** Estás gastando CAC para llenarlo, pero la base se fuga. Si tienes un churn del 10% mensual, cada nuevo cliente que ganes debe compensar esa fuga antes de generar crecimiento neto real. Eso encarece masivamente tu crecimiento.
*   **La expansión tiene límites.** Puedes subir de plan a un cliente solo un número finito de veces. Si la base de clientes se erosiona, te quedas sin “suelo” sobre el cual expandir. Los upgrades vienen de clientes satisfechos que se quedan; si la causa del churn sigue ahí, tarde o temprano también se irán los que hoy te están pagando más.
*   **Concentración de riesgo.** Con 36 clientes, cada baja es proporcionalmente más dolorosa. Si entre los 4 que se fueron había uno de alto valor, la expansión de los demás lo tuvo que compensar. Eso aumenta la dependencia de pocos clientes grandes.
*   **Causa raíz.** Un churn del 10% en un mes sugi