# GPT-6.1 Terra — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 9.035s | tokens_per_second: 70.7
- input_tokens: 128 | output_tokens: 639

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No necesariamente. **Retención de ingresos del 114% no significa retención de clientes del 114%**, ni que casi nadie se vaya.

Si el panel mide la **retención neta de ingresos (NRR)**, ese 114% significa que los clientes que ya tenías al inicio del período generan ahora un 14% más de ingresos en conjunto. Las subidas de plan pueden compensar los ingresos perdidos por bajas o reducciones de plan. Conviene comprobar que el panel excluye a los clientes nuevos y qué período utiliza.

En tu caso, pasaste de 40 a 36 clientes:

- Si los 36 son clientes que ya tenías, perdiste 4: un **churn de clientes del 10%** y una retención del 90%.
- Si entre los 36 hay clientes nuevos, perdiste más de 4 de los originales, así que el churn de esa cohorte fue mayor.

Por tanto, **no dejaría de vigilar el churn**. Una NRR del 114% puede ser una buena señal de expansión, pero también puede ocultar que estás perdiendo clientes. Antes de volcar todo el esfuerzo en captación, revisaría cuántos se fueron, cuánto ingreso representaban y si las subidas de plan proceden de muchos clientes o de unos pocos.