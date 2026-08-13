# Claude Opus 5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 30.762s | tokens_per_second: 66.6
- input_tokens: 262 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

## Primero: respira, el 31% no es tu churn

El 31% es un promedio ponderado de dos poblaciones que no tienen nada que ver entre sí. Al separarlas:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Blended | 200 | 62 | 31% |

Como el 89% de tu base es gratuita, la métrica agregada básicamente **te está reportando el comportamiento del plan free y llamándolo "churn de la plataforma"**. No mide salud de negocio.

## Segundo: el 9,1% tampoco es un número en el que puedas confiar

Y esto es lo más importante que te voy a decir. Con 22 usuarios de pago, **cada usuario vale 4,5 puntos porcentuales**. Un churn de 1 usuario = 4,5%. Dos = 9,1%. Tres = 13,6%.

El intervalo de confianza al 95% para 2/22 va aproximadamente de **2,5% a 27,8%**.

Traducción: con esta muestra no puedes distinguir estadísticamente si tu churn real es 5% o 20%. No es que tu churn "subió de 5% a 9%" — es que **nunca tuviste una medición capaz de detectar la diferencia**. Tu creencia de que estabas en 5% probablemente venía de un mes en que se fue 1 usuario en lugar de 2.

## Tercero: "churn free" y "churn pago" son fenómenos distintos

Un 33,7% mensual en plan gratuito puede ser perfectamente normal, o puede ser una señal. Depende de algo que no está en tus datos:

- **¿De dónde salieron esos 178?** Si hubo un pico de registros (lanzamiento, campaña, aparición en algún agregador), lo que estás viendo son curiosos que se fueron. Eso es normal y no es churn en ningún sentido económico.
- **¿Se activaron alguna vez?** Un usuario que se registró, nunca completó la acción principal y se fue a los 12 días no es un problema de retención: es un problema de activación u onboarding. Se arregla en un lugar distinto del producto.

Además, ojo con el denominador: si alguno de esos 62 se registró *durante* el mes y se fue en el mismo