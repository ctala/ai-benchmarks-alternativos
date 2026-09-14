# Muse Glimmer 30B — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 24.292s | tokens_per_second: 62.1
- input_tokens: 145 | output_tokens: 1509

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, no es correcto. 114% de Retención de Ingresos no significa que no se te va nadie y mucho menos que la retención de clientes está por encima del 100%.

La retención de clientes nunca puede ser >100%. La retención de ingresos sí puede.

Tienes dos métricas distintas y estás mezclando logo churn con revenue churn.

**Lo que te está pasando con tus números**

Mes anterior: 40 clientes de pago
Mes actual: 36 clientes de pago

Logo churn = 4 / 40 = 10% mensual. Eso es churn real de clientes.
Anualizado es ~ 70% de churn anual de logos. No es 0%.

Tu panel dice Retención de Ingresos 114%. Eso es Net Revenue Retention, NRR.

NRR = [MRR inicio - MRR churn - MRR contracción + MRR expansión] / MRR inicio

114% significa que del MRR que tenías el mes pasado con esos 40 clientes, ahora sigues cobrando el 114% aunque hayas perdido 4 clientes. Lo compensaste y superaste con subidas de plan de los que se quedaron.

Ejemplo simplificado:
Si tenías 40 clientes x $100 = $4.000 MRR inicio
Ahora tienes 36 clientes que generan $4.560 MRR
NRR = 4.560 / 4.000 = 114%

Perdiste 4 logos, pero los 36 que quedaron subieron su gasto medio de $100 a ~$127.

Es decir tienes:
* **Gross Revenue Retention < 100%**: pierdes ingresos por churn y downsell. No lo ves en el 114%.
* **Expansión > Churn**: la expansión de los clientes existentes tapa la pérdida y te deja en +14% neto.

**Por qué no puedes dejar de preocuparte por el churn**

1. **NRR alto puede esconder un logo churn alto.** Estás creciendo en ingresos por los mismos clientes que se quedan, pero tu base se está encogiendo. Si la expansión se frena, el churn te come todo.
2. **Adquisición es más cara que retención.** El cliente que se va te quita no solo su MRR, sino el LTV y el potencial de expansión que nunca vas a monetizar.
3. **Riesgo de concentración.** Si 4 clientes se van y 2 clientes grandes suben de plan, tu NRR se mantiene pero tu base es más frágil.

Lo que sí puedes hacer es dejar de preocuparte por el churn *solo* como pérdida de ingresos, porque la expansión lo compensa hoy. Pero no por el churn de logos.

Métricas que necesitas mirar en paralelo:
* **Logo Retention / Churn Rate:** 36/40 = 90% mensual. Objetivo sano suele ser >95-97% mensual según tu modelo.
* **Gross Revenue Retention:** MRR inicio - churn - contracción / MRR inicio. Te dirá cuánto retienes sin expansión.
* **Net Revenue Retention:** el 114% que ya ves.
* **Expansion MRR y Contraction MRR:** quién sube, quién baja y por qué.

Conclusión: tienes un gran motor de expansión, eso es excelente. Pero sigues perdiendo 1 de cada 10 clientes al mes. Trabaja en captar gente nueva Y en reducir el logo churn, porque la expansión no es infinita y el churn sí es un agujero que se agranda con el tiempo.