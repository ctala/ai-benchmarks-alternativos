# Muse Glimmer 30B — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 122.849s | tokens_per_second: 14.0
- input_tokens: 145 | output_tokens: 1719
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una explicación detallada y contextualizada de la retención de ingresos y su relación con el churn.

## Respuesta completa

No. Retención de ingresos ≠ retención de clientes, y la retención de clientes no puede estar por encima del 100%.

**114% es Retención Neta de Ingresos, NRR. No es que no se te vaya nadie.**

Con tus números:

* Clientes inicio: 40
* Clientes fin: 36
* Logos perdidos: 4

Tu retención de clientes / logo retention es 36/40 = 90%. Tienes un churn de clientes del 10% en el mes. Eso es churn real y no desaparece porque el ingreso suba.

El 114% significa que el ingreso que te dejaron los clientes que ya tenías el mes pasado creció un 14% neto después de churn, contracciones y expansiones.

Es decir:
Gross Revenue Retention = ingreso de los clientes que se quedaron sin contar subidas de plan.
Con tus datos es ~90% si no hubo contracciones. Perdiste el 10% de ingreso por los 4 clientes que se fueron.

Net Revenue Retention = Gross Revenue Retention + Expansion - Contracción
114% = 90% + expansión de los que se quedaron

Para que cuadre, los 36 clientes que permanecen tuvieron que subir su MRR de media un ~26-27% para compensar los 4 que se fueron y dejar el total +14%. Eso es expansión, no retención.

Por qué no puedes dejar de preocuparte por el churn:

* **El NRR alto puede esconder churn alto.** Estás sustituyendo logos perdidos con subidas de plan de los que quedan. Si la expansión se frena, el churn de clientes se vuelve caída de ingresos.
* **Churn de logos es un leading indicator.** La expansión es un lagging indicator. Pierdes clientes ahora y el impacto en ingresos lo notas después.
* **Concentración de riesgo.** Si ese 14% de crecimiento viene de 2-3 clientes que subieron de plan, tu NRR es frágil.
* **CAC vs expansión.** Captar gente nueva es caro. Retener y expandir es 5-7x más barato, pero necesitas ambas.

Métricas que necesitas mirar en paralelo:

* **Logo Retention / Churn de clientes:** 90% en tu caso. Benchmark SaaS sano >95% mensual.
* **Gross Revenue Retention:** Ingreso de clientes existentes sin expansion. Te dice el churn puro.
* **Net Revenue Retention:** El 114% que ves. Bueno >110% es excelente, pero solo con Gross sano.
* **Expansion MRR y Contraction MRR:** De dónde viene realmente el +14%.

No metas todo el esfuerzo en captación. Con 10% de churn mensual estás perdiendo ~1 de cada 10 clientes cada mes. Mantén trabajo en reducción de churn y activación, y usa la expansión como acelerador, no como sustituto.

¿Tu panel calcula el 114% solo sobre la cohorte existente o incluye nuevos clientes? Si incluye nuevos, no es NRR, es crecimiento de MRR total y la lectura es aún más engañosa.