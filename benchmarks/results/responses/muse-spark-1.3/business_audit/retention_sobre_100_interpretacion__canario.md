# Muse Spark 1.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 17.776s | tokens_per_second: 128.4
- input_tokens: 143 | output_tokens: 2283

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Y esa es justo la lectura que parece buena pero esconde un problema.

Lo que tu panel llama **'Retención de ingresos: 114%' es Retención Neta de Ingresos (NRR, Net Revenue Retention), no retención de clientes.**

No significan lo mismo:

**1. Retención de clientes / logos: nunca puede ser >100%**
Mide cuántos clientes se quedan.
Fórmula: `(Clientes iniciales - Clientes perdidos) / Clientes iniciales`

En tu caso: pasaste de 40 a 36. Aunque no hayas captado a nadie nuevo este mes, tu retención es como máximo:

36 / 40 = **90%**

Es decir, **perdiste al menos al 10% de tus clientes en un mes.** Eso es un churn de logos del 10% mensual. Anualizado, eso es perder ~70% de tu base al año. Es muy alto.

Si además captaste algún cliente nuevo en el camino, es peor. Ejemplo: si captaste 2 y terminaste en 36, en realidad perdiste 6 de los 40 originales: retención del 85%.

**2. Retención Neta de Ingresos (NRR): sí puede ser >100%**
Mide cuántos *dólares* se quedan, incluyendo subidas y bajadas de plan.
Fórmula: `(MRR inicial + Expansión - Contracción - Churn) / MRR inicial`

Tu 114% significa esto:
Perdiste dólares por los 4+ clientes que se fueron, **pero los clientes que se quedaron pagaron tanto más (subidas de plan) que compensaron con creces esa pérdida.**

Ejemplo simplificado:
Mes pasado: 40 clientes x $100 = $4,000
Este mes: 36 clientes, pero ingresas $4,560 = 114% de $4,000
Tu ingreso medio por cliente que se quedó pasó de $100 a $126.6.

No es que "no se va nadie". Es que "los que se van me cuestan menos dólares de los que me dan extra los que se quedan y suben de plan".

### Por qué no puedes ignorar el churn y solo captar

Ese 114% está enmascarando una cubeta con fuga:

1.  **La expansión tiene techo, el churn no.** Un cliente solo puede subir de plan 1 o 2 veces. Pero puede irse el 10% cada mes indefinidamente. En unos meses te quedas sin base a la que hacer upsell.

2.  **Te vuelves dependiente de menos clientes.** Cada vez necesitas que menos clientes paguen más. Aumenta tu riesgo de concentración: si mañana se van 2 grandes, tu NRR se desploma.

3.  **Adquirir para tapar churn es carísimo.** En SaaS, retener suele costar 5-7x menos que adquirir. Si pierdes 10% mensual, tu equipo de captación tiene que correr solo para no encogerse, no para crecer.

Un buen NRR es 110-120%, sí. Pero los SaaS sanos lo consiguen con una retención de logos del 90%+ *anual* en SMB o 95%+ en Enterprise, no del 90% *mensual*.

### Lo que tienes que mirar esta semana

No te quedes solo con el 114%. Calcula estos dos:

**a) Gross Revenue Retention (GRR):** Igual que el NRR pero SIN contar la expansión. Te dice cuánto sangras de verdad. Seguro que el tuyo está por debajo del 90%.

`(MRR inicial - Contracción - Churn) / MRR inicial`

**b) Churn de logos mensual y motivo:** ¿Quiénes son esos 4 que se fueron? ¿Eran pequeños? ¿Nuevos? ¿Por qué se fueron vs. por qué los otros subieron?

Tu problema no es captación. Tu problema es que tienes dos productos en uno: uno que encanta a unos pocos (suben de plan) y uno que expulsa al 10% (se van). Hasta que no entiendas esa diferencia, meter todo en captación es echar agua en una cubeta rota.

¿Quieres que lo calculemos? Dime tu MRR del mes pasado y de este mes sin contar clientes nuevos, y te saco tu GRR real.