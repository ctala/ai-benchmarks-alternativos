# Muse Glimmer 30B — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 12.824s | tokens_per_second: 120.8
- input_tokens: 145 | output_tokens: 1549

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. 114% de Retención de Ingresos no significa que retienes clientes por encima del 100%. Significa que retienes ingresos por encima del 100%.

Son dos métricas distintas y tú estás confundiendo retención de logos con retención de ingresos.

Con tus números:

**Retención de clientes / Logo Retention**
40 clientes el mes pasado -> 36 este mes
Logo Retention = 36 / 40 = 90%
Churn de logos = 10% mensual

10% mensual es muy alto. Anualizado es 1 - 0.9^12 ≈ 72% de churn anual de clientes. Es decir, si sigues así, en un año te quedas con menos de 1/3 de los logos que tienes hoy.

**Retención de ingresos = 114%**
Eso es Net Revenue Retention. Significa que el MRR que te generan los clientes que ya tenías el mes pasado es ahora un 14% mayor.

Cómo es posible con menos clientes? Porque los que se quedaron subieron de plan. Estás compensando la pérdida de 4 clientes con expansión de los que quedan.

Es la fórmula típica:
Net Revenue Retention = [MRR inicio del cohort - Churn MRR - Downgrade MRR + Expansion MRR] / MRR inicio del cohort

114% = 100% - churn de ingresos + expansión de ingresos

Tienes expansión, eso es bueno, pero está enmascarando un churn de logos real del 10% mensual.

No puedes dejar de preocuparte por el churn por 3 razones:

1. **La expansión no es infinita.** Puedes subir de plan a un cliente 1-2 veces, pero luego llega a tope. Si sigues perdiendo 10% de logos al mes, tarde o temprano se acaba el pool que puede expandirse.

2. **El coste de reemplazo es mayor.** Captar un cliente nuevo suele costar 3-5x más que retener uno. Estás perdiendo 4 clientes al mes y confiando en que el resto suba para compensar.

3. **114% puede ser engañoso.** Si el panel calcula retención de ingresos de forma "neta" incluyendo nuevos clientes, no es una métrica de cohort real. La retención pura debería medirse solo sobre el cohort inicial, sin sumar nuevos logos.

Lo que necesitas mirar en paralelo:

* **Logo Retention / Churn de clientes:** 90% mensual en tu caso. Objetivo SaaS saludable es >95% mensual.
* **Gross Revenue Retention:** Retención de ingresos sin contar expansión. Si es <90% es señal de sangría.
* **Net Revenue Retention:** El 114% que ves. Bueno si está >110-120% y se mantiene.
* **Expansion MRR vs Churn MRR:** De dónde viene ese +14%. ¿Es 1 cliente que duplicó su plan o 30 clientes que subieron un poco? La concentración importa.

En resumen: tienes un problema de retención de clientes que estás tapando con un buen momento de expansión. Eso es mejor que lo contrario, pero no es sostenible. Necesitas trabajar en captación Y en reducir el churn de logos, no elegir uno.

¿Quieres que te ayude a calcular tu Gross Revenue Retention real con los números de MRR de los 40 vs los 36?