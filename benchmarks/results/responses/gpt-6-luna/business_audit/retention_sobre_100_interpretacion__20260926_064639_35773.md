# GPT-6 Luna — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.89 | quality: 8.0
- latency_total: 6.553s | tokens_per_second: 109.6
- input_tokens: 128 | output_tokens: 718

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Un 114% de retención de ingresos no significa que retengas al 114% de tus clientes.** Si el panel mide *retención neta de ingresos* (NRR), normalmente compara los ingresos recurrentes de una cohorte de clientes existentes, incluyendo ampliaciones y reducciones de sus planes, pero excluyendo clientes nuevos.

Así, un 114% suele indicar que esa cohorte genera ahora un 14% más de ingresos recurrentes que al inicio del periodo. Las subidas de plan pueden compensar —o superar— los ingresos perdidos por cancelaciones o bajadas de plan. Por ejemplo: se parte de 100 €; se pierden 20 € por cancelaciones o reducciones y se ganan 34 € por ampliaciones: la NRR es 114%.

En cambio, pasar de **40 a 36 clientes de pago** significa que tu número de clientes activos cayó un **10% neto**. No permite saber cuántos cancelaron exactamente: si no entró nadie nuevo, habrías perdido 4; si entraron clientes nuevos, las bajas pudieron ser más numerosas.

Por tanto, **no dejaría de preocuparme por el churn ni dedicaría todo el esfuerzo a captar clientes**. Revisa, como mínimo:

- **Retención de clientes** y cancelaciones, por separado de los ingresos.
- **Retención bruta de ingresos (GRR)**, que excluye las ampliaciones y muestra cuánto ingreso conservas antes de contar ventas adicionales a clientes existentes.
- **NRR**, para ver el efecto combinado de bajas, reducciones y ampliaciones.
- Clientes nuevos, clientes perdidos y concentración de ingresos en los clientes que subieron de plan.

La lectura precisa también depende de qué fórmula y periodo use tu panel: conviene confirmar si ese 114% es NRR y qué clientes incluye en la cohorte.