# GPT-6 Luna Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.58 | quality: 8.0
- latency_total: 16.628s | tokens_per_second: 110.9
- input_tokens: 3071 | output_tokens: 1844

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Una retención de ingresos del 114% no significa que retengas al 114% de tus clientes.** Si el panel calcula *retención neta de ingresos* (NRR), significa que los ingresos de una cohorte de clientes existentes crecieron un 14% en el periodo, contando las bajas, las reducciones y las ampliaciones de plan. Las subidas de plan pueden compensar los ingresos perdidos por clientes que se fueron.

El recuento de clientes es otra métrica:

- Si los 36 de este mes son todos de los 40 que tenías, conservaste 36: **retención de clientes del 90%** y **churn de clientes del 10%**.
- Si entre los 36 hay clientes nuevos, no puedes calcular el churn de la cohorte original con esos totales; podrías haber perdido más de cuatro clientes y haber incorporado algunos nuevos.

Comprueba también la definición exacta del panel: una retención **bruta** de ingresos normalmente no supera el 100%; un 114% suele indicar retención **neta** o alguna definición distinta.

Así que no dejaría de preocuparme por el churn. La expansión de los clientes que se quedan puede estar ocultando bajas —y depender de unos pocos clientes que suben de plan puede ser arriesgado—. Sigue ambas cosas por separado: **churn de clientes**, **retención bruta de ingresos** y **retención neta de ingresos**, además de los motivos de baja.