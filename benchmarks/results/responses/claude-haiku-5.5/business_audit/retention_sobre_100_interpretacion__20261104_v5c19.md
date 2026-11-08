# Claude Haiku 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.77 | quality: 8.0
- latency_total: 8.111s | tokens_per_second: 169.3
- input_tokens: 218 | output_tokens: 1373

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, no es correcto. Un NRR (retención neta de ingresos) del 114% significa que los ingresos que te generaban los clientes de hace un periodo son hoy un 14% mayores, después de descontar bajas, downgrades y sumar upgrades. No significa que no se vaya nadie.

Tus datos muestran justo eso: pasaste de 40 a 36 clientes de pago. Si no hubo altas nuevas, perdiste 4 de 40, un 10% de bajas de clientes en un mes, que es una tasa alta para SaaS. Y si hubo altas, las bajas reales fueron más de 4, porque las nuevas altas compensan parte de ellas en el recuento neto.

El 114% puede ser compatible con esas bajas porque los upgrades de los clientes que se quedaron pesan más en euros que lo que pierdes con los que se van. Eso es una buena señal, pero tiene dos riesgos:

- **Puede esconder una fuga concentrada.** Si los que suben de plan son pocos y grandes, la mayoría de tus clientes pequeños podría estar yéndose. El NRR promedia y no te dice dónde está el problema.
- **Depende de que la expansión siga.** Si los upgrades son puntuales (por ejemplo, una campaña o un cambio de precios), el 114% puede caer rápido.

Para entender tu situación real, mira:

1. **Logo churn mensual:** cuántos clientes se fueron sobre el total al inicio del mes (aquí, probablemente alrededor del 10%, con los datos que das).
2. **GRR (retención bruta de ingresos):** mide solo pérdidas (bajas y downgrades), sin contar upgrades. Si está muy por debajo del 90%, tienes un problema de retención aunque el NRR sea 114%.
3. **Churn por segmento o plan:** ¿quién se va? ¿Clientes de un plan, de un canal, de una cohorte concreta?
4. **Motivos de baja:** entrevista o encuesta a quienes cancelaron.

Sobre tu pregunta: no, no deberías dejar de preocuparte por el churn ni volcar todo en captar. Con un 10% mensual de bajas de clientes, cada cliente que captas se pierde por la puerta trasera, y el crecimiento se vuelve muy caro. Lo sensato es entender por qué se van antes de decidir cuánto invertir en adquisición. La expansión de tus clientes actuales es una oportunidad real, pero no sustituye a arreglar la fuga.