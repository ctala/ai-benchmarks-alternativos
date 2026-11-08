# GPT-6 Luna Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.59 | quality: 8.0
- latency_total: 15.331s | tokens_per_second: 118.5
- input_tokens: 3018 | output_tokens: 1816

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Un 114% de retención de ingresos no significa que retengas al 114% de tus clientes.** Si el panel calcula la retención neta de ingresos (NRR), significa que los ingresos de una cohorte de clientes existentes crecieron un 14% durante el periodo, contando ampliaciones y normalmente restando bajas y reducciones, pero **sin contar clientes nuevos**. Las ampliaciones pueden compensar los ingresos perdidos por clientes que se van.

En tu caso, pasar de 40 clientes a 36 supone una caída neta del **10% en el número de clientes**. Si no incorporaste clientes nuevos, serían 4 bajas; si sí los incorporaste, podría haber habido más de 4 bajas. Para saber la retención de clientes y el churn reales, necesitas las bajas y altas por separado.

Así que no dejaría de preocuparme por el churn ni dedicaría todo el esfuerzo a captar clientes. Una NRR de 114% es una señal positiva de expansión, pero puede ocultar pérdidas de clientes. Sigue también:

- **Retención de clientes** y churn de clientes.
- **Retención bruta de ingresos (GRR)**, que muestra cuánto ingreso se conserva antes de contar las ampliaciones.
- **NRR por cohorte y por cliente**, para comprobar si el crecimiento está repartido o depende de unas pocas cuentas.

Comprueba además cómo define el panel «retención de ingresos»: si es NRR, puede superar el 100%; si es retención bruta, no.