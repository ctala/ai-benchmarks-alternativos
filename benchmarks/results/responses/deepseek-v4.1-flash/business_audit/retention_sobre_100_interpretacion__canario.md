# DeepSeek V4.1 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 33.783s | tokens_per_second: 189.7
- input_tokens: 165 | output_tokens: 6409

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa lectura no es correcta. El 114% es (casi seguro) **retención neta de ingresos** o **NRR**, no retención de clientes. La retención de clientes/clientes-logos **no puede superar el 100%**.

Con tus datos:

- El mes pasado: 40 clientes.
- Este mes: 36 clientes.
- Si no entraron clientes nuevos, retención de clientes = 36/40 = **90%**.
- Churn de clientes = 4/40 = **10%**.
- Si además entraron clientes nuevos, entonces de los 40 originales quedan menos de 36; el churn real de esa cohorte es **mayor al 10%**.

Que la retención de ingresos sea 114% significa que los ingresos de tu base existente son 1,14 veces los del mes pasado. Eso puede pasar porque varios clientes subieron de plan y compensaron con creces a los que se fueron. Ejemplo simplificado:

- 40 clientes x $100 = $4.000.
- Se van 4 clientes: -$400.
- Quedan 36 clientes, pero 8 suben de $100 a $220.
- Nuevo ingreso: 28 x $100 + 8 x $220 = $4.560.
- Retención de ingresos = $4.560 / $4.000 = **114%**.
- Retención de clientes = 36/40 = **90%**.
- Churn de clientes = **10%**.

Es decir: **ganaste ingresos por expansión, pero perdiste clientes**. No es que “prácticamente no se te vaya nadie”.

¿Puedes dejar de preocuparte por el churn y meter todo a captación? **No con este dato solo.** Puedes tener NRR >100% y churn de logos alto. Si el churn se concentra en clientes pequeños y los grandes expanden, podría ser tolerable, pero hay que medirlo. Si lo ignoras, puedes estar llenando un balde agujereado: captas gente nueva solo para compensar los que se van.

Lo que revisaría:

- Si el panel llama “retención de ingresos” a **NRR** o a **GRR**. La retención bruta de ingresos normalmente no supera 100%.
- Tu **GRR**: cuánto retienes sin contar expansiones. Ahí ves la fuga real de ingresos.
- **Retención/churn por cohortes**: de los 40 del mes pasado, cuántos siguen activos.
- **Churn temprano**: clientes que se van en los primeros 30/60/90 días.
- **Concentración de la expansión**: ¿pocos clientes están tapando la fuga del resto?
- **LTV/CAC y payback**: ¿cuánto cuesta captar para compensar el churn?

Conclusión: el 114% dice que tu ingreso recurrente existente crece pese a las bajas. No dice que no haya bajas ni que puedas dejar de trabajar retención. Puedes priorizar captación si los datos de GRR, cohortes y unit economics lo justifican, pero no dejar de preocuparte por el churn.