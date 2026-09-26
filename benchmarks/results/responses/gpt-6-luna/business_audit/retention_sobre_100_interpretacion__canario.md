# GPT-6 Luna — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6-luna`
- success: True  | final: 7.92 | quality: 8.0
- latency_total: 6.06s | tokens_per_second: 102.8
- input_tokens: 128 | output_tokens: 623

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No necesariamente. **“Retención de ingresos: 114%” probablemente significa retención neta de ingresos (NRR)**: los clientes que ya tenías al inicio del periodo generan ahora un 14% más de ingresos en conjunto, **después de contar** cancelaciones, bajadas de plan y subidas de plan. Normalmente no incluye los ingresos de clientes nuevos.

Eso **no significa que la retención de clientes sea del 114%**, ni que casi nadie se vaya. Puede haber bajas y, aun así, una NRR superior al 100% si las ampliaciones de los clientes que siguen compensan —y superan— los ingresos perdidos.

Tus cifras dan una señal distinta: pasaste de 40 a 36 clientes de pago, una caída neta de 4 (10%). Pero ese cambio **no revela por sí solo cuántos clientes cancelaron**: si adquiriste clientes durante el mes, las bajas brutas pudieron ser más de cuatro. Si no hubo altas, sí serían cuatro bajas sobre una base de 40.

Por tanto, **no dejaría de preocuparme por el churn ni pondría todo el esfuerzo en captar**. Revisaría, como mínimo:

- **Retención de clientes (logo retention)** y bajas brutas.
- **Retención bruta de ingresos (GRR)**, que muestra lo perdido por bajas y reducciones, sin contar ampliaciones.
- **NRR**, para ver si las subidas de plan están compensando esas pérdidas.
- La definición y el periodo que usa el panel: mensual, anual y con qué cohorte.

La NRR del 114% puede ser una buena señal de expansión entre los clientes que permanecen, pero por sí sola no demuestra que la base de clientes sea estable.