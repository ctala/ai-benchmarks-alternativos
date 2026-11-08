# GPT-6 Luna — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.74 | quality: 8.0
- latency_total: 7.842s | tokens_per_second: 91.4
- input_tokens: 128 | output_tokens: 717

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **“Retención de ingresos: 114%” no significa que retengas al 114% de tus clientes ni que casi nadie se vaya.** Si el panel usa la definición habitual de *retención neta de ingresos* (NRR), significa que los clientes que ya tenías al inicio del período generan al final un **14% más de ingresos en conjunto**, contando ampliaciones y restando cancelaciones y reducciones. Normalmente se excluyen los ingresos de clientes nuevos.

Por ejemplo, algunos clientes pueden haberse ido y otros haber subido de plan; las ampliaciones pueden compensar con creces los ingresos perdidos. Por eso la NRR puede superar el 100% aunque disminuya el número de clientes.

En tu caso, pasaste de **40 a 36 clientes**: son 4 menos, una caída neta del 10% en el recuento. Si no adquiriste clientes durante el período, eso equivaldría a 4 bajas; si sí los adquiriste, las bajas brutas podrían ser más.

No dejaría de vigilar el churn ni pondría todo el esfuerzo en captar. Revisa, además de la NRR:

- **Retención de clientes** o *logo retention/churn*: cuántos clientes se quedan o se van.
- **Retención bruta de ingresos (GRR)**: cuánto ingreso conservas antes de contar las ampliaciones.
- Altas y bajas brutas, y qué segmentos se están yendo.

También confirma cómo define el panel “retención de ingresos”: las fórmulas pueden variar. La NRR alta es una buena señal de expansión, pero por sí sola no demuestra que la base de clientes esté sana.