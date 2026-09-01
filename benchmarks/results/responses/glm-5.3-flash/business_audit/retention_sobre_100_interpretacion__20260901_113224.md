# GLM 5.3 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 71.991s | tokens_per_second: 37.7
- input_tokens: 138 | output_tokens: 2717

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, la lectura es incorrecta en los dos puntos. Tu propio contexto lo desmiente.

## Qué te está diciendo el 114%

Ese número es casi con seguridad **retención de ingresos neta (NRR)**, que mide cuántos ingresos conservas de la cohorte de clientes que tenías al inicio del período, contando subidas y bajadas de plan. No mide clientes: mide dólares.

- **Retención de clientes (logo retention):** 36/40 = **90%**. Perdiste el 10% de tu base en un mes. Anualizado, un churn mensual del 10% implica que te queda ~28% de tu base de clientes en 12 meses ((0,90)^12 ≈ 0,28). Eso no es "prácticamente no se va nadie".
- **Retención de ingresos neta:** 114%. Los que se quedaron subieron de plan con suficiente fuerza para compensar los ingresos perdidos y añadir un 14% neto.

Dos métricas distintas, y la segunda está ocultando la primera.

## Una señal que merece atención

Si los 4 clientes que se fueron eran "promedio" (10% de tus ingresos), para llegar a 114% necesitarías expansión de ~24% en un solo mes, lo cual es muy raro. Eso deja tres posibilidades, y conviene saber cuál es:

1. Los que se fueron eran clientes pequeños (menos doloroso en ingresos, pero revisa por qué se van).
2. La expansión vino de 1-2 cuentas grandes → **concentración**: con 36 clientes, que una cuenta grande baje de plan puede tirar tu NRR por debajo de 100% de golpe.
3. El panel no calcula lo que crees: verifica la ventana (mensual vs. cohortes anuales/trailing 12 meses) y la fórmula (algunos paneles incluyen erróneamente ingresos de clientes nuevos, que no forman parte del NRR estándar).

## Sobre tu plan de "solo captación"

Cambiar todo el esfuerzo a adquisición con 10% de churn mensual es como llenar un cubo con un agujero: necesitas reemplazar el 10% de tu base cada mes solo para no decrecer en clientes, pagando CAC cada vez. Además:

- La expansión de los clientes actuales es crecimiento sin CAC; el churn la está destruyendo.
- El churn de 4 clientes en un mes con base de 40 es estadísticamente ruidoso pero direccionalmente preocupante: entrevista a los que se fueron antes de escalar adquisición hacia un producto con fuga.

## Qué mirar junto al NRR

- **GRR (retención bruta de ingresos):** excluye expansiones, no puede superar 100%. Te muestra el suelo real.
- **Logo churn:** clientes perdidos / clientes iniciales. Tu 10% mensual es alto incluso para SMB.
- **Concentración de ingresos:** % de MRR en tus top 3 cuentas.

**Conclusión:** el 114% es una buena noticia sobre tu capacidad de monetizar a quienes se quedan, y una mala noticia disfrazada sobre quién se va. No dejes de preocuparte por el churn: ahora es precisamente cuando debes investigarlo.