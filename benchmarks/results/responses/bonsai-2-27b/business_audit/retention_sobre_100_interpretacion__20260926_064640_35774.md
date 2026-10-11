# Bonsai 2 27B — business_audit/retention_sobre_100_interpretacion

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 189.251s | tokens_per_second: 43.0
- input_tokens: 181 | output_tokens: 8147

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa



No. Ese **114% no significa que retienes más del 100% de clientes**. Significa algo distinto: que **los ingresos de tus clientes existentes subieron un 14%**, probablemente porque varios subieron de plan.

Es muy probable que tu panel esté mostrando **Net Revenue Retention / NRR** o “retención neta de ingresos”, no retención de clientes.

## Qué significa realmente un 114%

En términos simples:

> De cada 100 € de ingresos que te generaban tus clientes existentes el mes pasado, este mes te están generando 114 €.

Eso puede pasar porque:

- algunos se fueron,
- algunos bajaron de plan,
- pero otros subieron de plan suficiente para que el total suba.

No significa que “114% de clientes se quedaron”. La retención de clientes, medida en número de logos, **no puede superar el 100%**. Lo que puede superar el 100% es la **retención de ingresos**.

## Tu caso: 40 clientes a 36 clientes

Si el mes pasado tenías **40 clientes de pago** y este mes tienes **36**, entonces, como mínimo, **se fueron 4 clientes**, si no entraron clientes nuevos.

Eso implica:

> Retención de clientes por número de logos = 36 / 40 = **90%**

O sea: **no es que prácticamente no se vaya nadie**. Se fue el 10% de tu base de clientes.

Y si algunos de esos 36 son clientes nuevos, la retención de clientes antiguos sería peor. Por ejemplo:

- Si entraron 0 nuevos: 36 antiguos siguen → **90% de retención de logos**.
- Si entraron 4 nuevos: solo 32 antiguos siguen → **80%**.
- Si entraron 10 nuevos: solo 26 antiguos siguen → **65%**.
- Si entraron 20 nuevos: solo 16 antiguos siguen → **40%**.

Así que el número 40 → 36 ya te da una señal importante: **hay churn**.

## Ejemplo numérico

Supongamos que tus clientes pagaban $100 cada uno.

Mes pasado:

> 40 clientes × $100 = **$4,000 MRR**

Este mes, para que tu NRR sea **114%**, los ingresos de tus clientes antiguos deben ser:

> $4,000 × 1.14 = **$4,560**

Si no entraron clientes nuevos y solo quedan 36 antiguos:

> $4,560 / 36 = **$126.67 de ARPU promedio**

Eso significa que, aunque se fueron 4 clientes, los 36 que se quedaron subieron de plan de manera que el ARPU pasó de $100 a $126.67.

Eso es lo que explica el 114%.

No significa que la base de clientes sea perfecta. Significa que **los ingresos de la base antigua crecieron gracias a expansiones**.

## Por qué no puedes dejar de preocuparte por el churn

Porque puedes tener una situación así:

> NRR: 114%  
> Logo retention: 90%  
> Churn mensual: 10%  
> Expansion: fuerte

Y eso puede parecer bueno, pero también puede ser frágil.

Si los clientes siguen subiendo de plan, el 114% puede ocultar que muchos se van. Si mañana las expansiones se frenan, el churn aparece con toda su fuerza.

Un buen NRR no es sinónimo de buena retención. Es sinónimo de **expansión suficiente para compensar las salidas**.

## La métrica que realmente te falta: GRR

Lo que deberías revisar junto al 114% es la **Gross Revenue Retention / GRR**.

De forma simplificada:

### NRR

Mide:

> ¿Cuánto crecen los ingresos de mis clientes existentes, contando subidas de plan?

Ese puede ser 114%.

### GRR

Mide:

> ¿Cuánto de los ingresos de mis clientes existentes se queda, sin contar las expansiones?

Es decir, mide el efecto de churn, downgrades y cancelaciones.

Si tu NRR es 114%, pero tu GRR es, por ejemplo, 80%, significa que:

- perdiste bastante ingresos por churn/downgrades,
- pero tus upsells fueron tan grandes que subieron el total a 114%.

Eso es una señal de alerta.

En cambio, si tu NRR es 114% y tu GRR es 95% o 97%, entonces la expansión está siendo fuerte pero la base de clientes también está relativamente estable. Eso sí es más sano.

## Cómo interpretar tu panel

Pregúntate o verifica:

1. **¿El 114% es NRR o GRR?**
   - Si es NRR, incluye upsells.
   - Si es GRR, normalmente no debería incluir expansiones, y un 114% sería inusual; podría deberse a aumentos de precio o a una definición extraña.

2. **¿Cuál es mi logo retention?**
   - Clientes antiguos que siguen activos / clientes antiguos del mes anterior.
   - Con 40 → 36, si no hay nuevos, es 90%.

3. **¿Cuál es mi churn mensual?**
   - Clientes antiguos que se fueron / clientes antiguos del mes anterior.
   - Con 40 → 36 y sin nuevos, es 10%.

4. **¿Cuál es mi GRR?**
   - Ingresos de clientes antiguos al final, sin contar expansiones, dividido por ingresos de clientes antiguos al inicio.

5. **¿Cuánto suben mis clientes existentes?**
   - Expansion revenue / MRR de clientes antiguos.
   - Es decir: ¿cuánto dinero nuevo generan los upsells?

6. **¿Cuánto sube mi ARPU de clientes existentes?**
   - MRR de clientes existentes / número de clientes existentes.
   - Si sube mucho, puede estar ocultando churn.

## Con 40 clientes, hay que tener cuidado

Con una base de 40 clientes, un solo cliente puede mover mucho los porcentajes.

Un cliente de $100 es el 2.5% de tu MRR si tu base es $4,000.

Por eso, con 40 clientes:

- 2-3 salidas pueden hacer que el churn parezca alto.
- 2-3 upsells pueden hacer que el NRR parezca muy bueno.
- Una sola gran expansión puede distorsionar el mes.

No puedes tomar decisiones de churn solo con un mes. Idealmente necesitas mirar 3 a 6 meses, o al menos varias cohortes.

## ¿Puedes dedicar más esfuerzo a captar gente nueva?

Quizá, **pero no todavía sin más datos**.

Puedes priorizar más adquisición si:

- NRR > 100%,
- GRR alta, por ejemplo 90% o más,
- churn mensual bajo o estable,
- logo retention aceptable,
- tus clientes existentes se expanden de forma consistente.

En ese caso, sí puedes pensar:

> “Mi base existente está creciendo. Puedo invertir más en adquisición porque el churn no me está destruyendo.”

Pero no puedes decir:

> “Mi NRR es 114%, por tanto no tengo churn.”

Eso no es cierto.

## Mi lectura de tu caso

Con el contexto que das:

- 40 clientes el mes pasado,
- 36 este mes,
- varios subieron de plan,
- panel muestra retención de ingresos del 114%,

lo más probable es que tengas:

> **NRR del 114% por expansiones, pero una retención de clientes del 90% o menos.**

Y si algunos de los 36 son nuevos, la retención de clientes antiguos puede estar aún peor.

Así que la lectura correcta es:

> No es que nadie se vaya. Es que los que se quedan o los que suben de plan están generando suficiente ingreso para que el total suba.

Eso puede ser bueno. Pero no es una excusa para ignorar el churn.

## Qué haría yo

1. **No dejaría de medir churn.**
2. **Pediría ver GRR y logo retention.**
3. **Calcularía cuántos de los 36 son antiguos y cuántos son nuevos.**
4. **Vería si los 114% vienen de 2 upsells grandes o de una expansión amplia.**
5. **Observaría 3 meses antes de decidir si lanzar más adquisición.**

Si tu GRR es alta, entonces sí puedes meter más esfuerzo en captar gente nueva.

Si tu GRR es baja, entonces estás construyendo sobre una base que se fuga. En ese caso, captar más gente puede ser solo llenar un cubo con agujeros.

## Resumen directo

No, no es correcto pensar que tu retención de clientes está por encima del 100%.

El **114% de retención de ingresos** significa que tus clientes existentes te están generando 14% más de ingresos que el mes anterior.

Tu caso de 40 a 36 clientes sugiere que **sí se fueron clientes**. Si no entraron nuevos, tu retención por clientes es del **90%**.

No deberías dejar de preocuparte por el churn. Deberías revisar si ese 114% viene de una expansión sana o de unos pocos upsells que están ocultando salidas.

Regla práctica:

> **NRR alto + GRR alta = base sana, puedes invertir en adquisición.**  
> **NRR alto + GRR baja = expansión ocultando churn, primero arregla retención.**