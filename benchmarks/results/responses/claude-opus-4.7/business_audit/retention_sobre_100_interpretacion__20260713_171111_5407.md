# Claude Opus 4.7 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 18.996s | tokens_per_second: 49.4
- input_tokens: 221 | output_tokens: 938
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y práctica de la métrica de retención de ingresos.

## Respuesta completa

No, la lectura correcta es bastante distinta a la que estás haciendo. Vamos por partes.

## Qué mide realmente ese 114%

Lo que tienes es **NRR (Net Revenue Retention)**, o retención neta de ingresos. Mide cuánto ingreso conservas de tu base de clientes existente, incluyendo:

- **–** lo que pierdes por churn (clientes que se van)
- **–** lo que pierdes por downgrades
- **+** lo que ganas por expansiones (upgrades, cross-sell, más asientos, etc.)

Un 114% significa que **el mismo grupo de clientes que tenías antes ahora te paga un 14% más en neto**. No dice nada sobre cuántos clientes conservas.

## Tus números lo confirman

Pasaste de 40 a 36 clientes. Eso es una **retención de clientes (logo retention) del 90%**, o equivalentemente un **churn del 10% mensual**. Eso es alto. Muy alto. Si se mantiene, en 12 meses habrías perdido aproximadamente el 72% de tu base actual.

Lo que está pasando es que los upgrades de los que quedaron están **compensando y camuflando** la salida de esos 4 clientes en la métrica de ingresos. Contablemente hoy estás mejor, pero estructuralmente tienes un problema.

## Por qué esto es peligroso

1. **El NRR alto por expansión es frágil**: depende de que los clientes que quedan sigan creciendo. Si el mes que viene no hay upgrades, el churn queda al descubierto.
2. **Estás perdiendo la parte baja del funnel**: probablemente los que se van son clientes más pequeños o nuevos, que son justo el perfil que captas cuando inviertes en adquisición. Meterías agua en un cubo con agujero.
3. **CAC payback se dispara**: si adquieres clientes que luego se van rápido, el coste de adquisición no se amortiza.

## Qué mirar en paralelo

- **GRR (Gross Revenue Retention)**: como el NRR pero sin contar expansiones. Te dirá cuánto ingreso pierdes realmente. Debería estar idealmente por encima del 90%.
- **Logo churn**: ese 10% mensual.
- **Segmentación del churn**: ¿quiénes se van? ¿plan, antigüedad, tamaño?

## Respuesta directa

No, no puedes dejar de preocuparte por el churn. Tienes un churn de clientes elevado enmascarado por expansiones de tus mejores cuentas. Antes de acelerar adquisición, entiende **por qué se van esos 4** y arréglalo, o vas a escalar el problema.